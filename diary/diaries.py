from diary.diary_ import Diary


class Diaries:
    list_of_diary = []
    numbers_of_diary = 0

    def add(self, username, password):
        self.numbers_of_diary += 1
        diary = Diary(username, password)
        self.list_of_diary.append(diary)

    def get_number_of_diary_added(self):
        return self.numbers_of_diary

    def find_by_username(self, username):
        for diary in self.list_of_diary:
            if diary.get_username() == username:
                return diary

    def delete_diary(self, username, password):
        diary = self.find_by_username(username)
        if diary.get_password() == password:
            return diary
        self.numbers_of_diary -= 1
        pass
