from diary.DiaryLockException import DiaryLockException
from diary.Entry import Entry
from diary.invalid_entry_identity_exception import InvalidEntryIdentityException


class Diary:
    islocked = True
    numberOfEntry = 0
    list_of_entry = []

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def islocked(self):
        return self.islocked

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def unlock_diary(self, password):
        if self.get_password() == password:
            self.islocked = False

    def lock_diary(self):
        self.islocked = True

    def create_entry(self, title, body):
        if not self.islocked:
            self.numberOfEntry += 1
            result = self.generate_id()
            entry = Entry(result, title, body)
            self.list_of_entry.append(entry)
        else:
            raise DiaryLockException("Diary is Locked, Cant Create Entry")

    def generate_id(self):
        return str(self.numberOfEntry)

    def get_number_of_entry(self):
        return self.numberOfEntry

    def find_entry_by_id(self, identity):
        for entry in self.list_of_entry:
            if entry.get_identity() == identity:
                return entry
        raise InvalidEntryIdentityException("Invalid Entry Identity")

    def delete_entry(self, identity):
        result = self.find_entry_by_id(identity)
        self.list_of_entry.remove(result)
        self.numberOfEntry -= 1

    def update_entry(self, identity, title, body):
        entry = self.find_entry_by_id(identity)
        entry.set_title(title)
        update = entry.get_body() + " " + body
        entry.set_body(update)

