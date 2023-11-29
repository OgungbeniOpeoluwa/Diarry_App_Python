import datetime


class Entry:
    datetime = 0

    def __init__(self, identity, title, body):
        self._title = title
        self._body = body
        self.identity = identity
        self._datetime = 0

    def get_identity(self):
        return self.identity

    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_body(self, body):
        self._body = body

    def get_body(self):
        return self._body

    def __str__(self):
        self._datetime = datetime.datetime
        current_time = self._datetime.now()
        return f"""
        {current_time.strftime("%m/%d/%Y, %H:%M:%S")}
            {self._title}
        {self._body}
        """
