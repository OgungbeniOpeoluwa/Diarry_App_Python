import unittest

import pytest

from diary.diary_ import Diary
from diary.invalid_entry_identity_exception import InvalidEntryIdentityException


class MyTestCase(unittest.TestCase):
    def test_something(self):
        diary = Diary("opeoluwa", "1999")
        result = diary.islocked
        self.assertTrue(result)

    def test_unlock_diary(self):
        diary = Diary("delighted", "2003")
        result = diary.unlock_diary("2003")
        self.assertFalse(diary.islocked)

    def test_lock_diary(self):
        diary = Diary("ope", '1999')
        diary.lock_diary()
        self.assertTrue(diary.islocked)

    def test_create_entry(self):
        diary = Diary("ope", "1999")
        diary.unlock_diary("1999")
        result = diary.create_entry("my last holiday", "I had a lot of fun")
        self.assertEqual(1, diary.numberOfEntry)

    def test_find_entry_by_id(self):
        diary = Diary("ope", '1999')
        diary.unlock_diary("1999")
        result = diary.create_entry("my last holiday", "I had a lot of fun")
        self.assertEqual("1", diary.find_entry_by_id("1").get_identity())

    def test_find_entry_by_id_for_two_account(self):
        diary = Diary("ope", '1999')
        diary.unlock_diary("1999")
        diary.create_entry("my last holiday", "I had a lot of fun")
        diary.create_entry("my last holiday", "I had a lot of fun")
        self.assertEqual("1", diary.find_entry_by_id("1").get_identity())
        self.assertEqual("2", diary.find_entry_by_id("2").get_identity())

    def test_delete_entry(self):
        diary = Diary("ope", '1999')
        diary.unlock_diary("1999")
        diary.create_entry("my last holiday", "I had a lot of fun")
        diary.create_entry("my holiday", "I had a lot of fun")
        diary.delete_entry("1")
        self.assertEqual(1, diary.numberOfEntry)
        self.assertEqual("my holiday", diary.find_entry_by_id("2").get_title())

    def test_update_entry(self):
        diary = Diary("ope", "1990")
        diary.unlock_diary("1990")
        diary.create_entry("my last holiday", "I had a lot of fun.")
        diary.update_entry("1", "This day was bad", "i couldnt meet my guy.")
        self.assertEqual("This day was bad", diary.find_entry_by_id("1").get_title())
        self.assertEqual("I had a lot of fun. i couldnt meet my guy.", diary.find_entry_by_id("1").get_body())

    def test_find_entry_doesnt_exist(self):
        diary = Diary("ope", "1999")
        diary.unlock_diary("1999")
        with pytest.raises(InvalidEntryIdentityException) as ex:
            diary.find_entry_by_id("1")
        assert(str(ex.value)) == "Invalid Entry Identity"




if __name__ == '__main__':
    unittest.main()
