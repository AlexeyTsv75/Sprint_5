import random

new_correct_user = {'name': 'Alex',
                    'e-mail': 'alex_qa5' + str(random.randint(100, 999)) + '@ya.ru',
                    'password': str(random.randint(100000, 999999))}
new_user_wrong_password = {'name': 'Alex',
                           'e-mail': 'alex_qa5' + str(random.randint(100, 999)) + '@ya.ru',
                           'password': str(random.randint(10000, 99999))}
registered_user = {'name': 'Alex',
                   'e-mail': 'alex_tsv_qa5496@ya.ru',
                   'password': '123456'}

