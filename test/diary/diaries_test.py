import unittest

from diary.diaries import Diaries


class MyTestCase(unittest.TestCase):
    def test_something(self):
        diary = Diaries()
        diary.add("opeoluwa", "1999")
        self.assertEqual(1, diary.numbers_of_diary)

    def test_diary_find_by_username(self):
        diary = Diaries()
        diary.add("opeoluwa", "1999")
        result = diary.find_by_username("opeoluwa")
        self.assertEqual("opeoluwa", result.get_username())

    def test_delete_diary(self):
        diary = Diaries()
        diary.add("opeoluwa", "1999")
        diary.delete_diary("opeoluwa", "1999")
        self.assertEqual(1, diary.numbers_of_diary)


if __name__ == '__main__':
    unittest.main()
