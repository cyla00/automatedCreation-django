import os
import sys
import time

files = ['urls', 'forms', 'filters', 'decorators']
py = '.py'
templates = 'templates'

def app():
    app_name = input('choose an app name: ')
    if os.path.isdir('./' + app_name):
        print(app_name + ' exists')
    else:
        comando_app = 'python manage.py startapp ' + app_name
        os.system(comando_app)
        os.chdir(app_name)

        for file in files:
            file_creation = open(f'{file}{py}', 'w+')
            file_creation.write('./' + app_name)
            print(f'{file} created')
            time.sleep(0.5)

        os.mkdir(templates)
        print(f'{templates} folder created')
        time.sleep(0.5)
        os.chdir(templates)
        inner_templates = app_name
        os.mkdir(inner_templates)
        print(f'inner templates {inner_templates} folder created')
        time.sleep(0.5)
        print(f'{app_name} + inner files created OK.')
        print('quitting...')
        time.sleep(2)
        quit()