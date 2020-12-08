import os
import sys
import time

def superuser_creation():
    yes = 'Y'
    no = 'N'
    quest = input(f'do you want to create a superuser on default DB settings? {yes}/{no}: ')
    if quest == yes:
        try:
            migration = 'python manage.py migrate'
            print('migrating...')
            os.system(migration)
            time.sleep(0.5)
            comando_user = 'python manage.py createsuperuser'
            if comando_user:
                os.system(comando_user)
                time.sleep(0.5)
            else:
                print('superuser creation ERROR')
        except Exception as err:
            print(err)
    else:
        print('skipping superuser creation...')