import unittest
import pytest
from task_1 import filter_the_list

my_list = [[
     {'visit1': ['Москва', 'Россия']}, 
     {'visit2': ['Дели', 'Индия']},
     {'visit3': ['Владимир', 'Россия']}
    ],
    [
     {'visit1': ['Москва', 'Россия']}, 
     {'visit2': ['Дели', 'Индия']},
     {'visit3': ['Владимир', 'Россия']}, 
     {'visit4': ['Лиссабон', 'Португалия']},
     {'visit5': ['Париж', 'Франция']},
     {'visit6': ['Лиссабон', 'Португалия']},
     {'visit7': ['Тула', 'Россия']}, 
     {'visit8': ['Тула', 'Россия']}, 
     {'visit9': ['Курск', 'Россия']}, 
     {'visit10': ['Архангельск', 'Россия']} 
    ]]

class TestMain(unittest.TestCase):

    def test_len_list(self):
        result = filter_the_list(my_list[0])
        self.assertEqual(len(result), 2) 
        self.assertNotEqual(len(result), 1) 
        

    def test_isinstance_list(self):
        result = filter_the_list(my_list[0])
        self.assertIsInstance(result, list) 
        self.assertNotIsInstance(result, str)

@pytest.mark.parametrize('my_list', my_list)
def test_len(my_list):
    result = filter_the_list(my_list)
    assert len(result) == 2 or 6  
        

if __name__ == '__main__':
    unittest.main()     




