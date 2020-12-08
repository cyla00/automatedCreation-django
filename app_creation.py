import os
import sys
import time

urls = 'urls.py'
forms = 'forms.py'
filters = 'filters.py'
decorators = 'decorators.py'
templates = 'templates'

def app():
    app_name = input('choose an app name: ')
    if os.path.isdir('./' + app_name):
        print(app_name + ' exists')
    else:
        comando_app = 'python manage.py startapp ' + app_name
        os.system(comando_app)
        os.chdir(app_name)
        fileURLS = open(urls, 'w+')
        fileURLS.write('./' + app_name)
        print(f'{urls} created')
        time.sleep(0.5)
        fileFORMS = open(forms, 'w+')
        fileFORMS.write('./' + app_name)
        print(f'{forms} created')
        time.sleep(0.5)
        fileFILTER = open(filters, 'w+')
        fileFILTER.write('./' + app_name)
        print(f'{filters} created')
        time.sleep(0.5)
        fileDECO = open(decorators, 'w+')
        fileDECO.write('./' + app_name)
        print(f'{decorators} created')
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