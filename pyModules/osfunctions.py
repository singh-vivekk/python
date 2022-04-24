import os
from datetime import date

today = date.today()
print("Today's date : ", today)

print('The directory of os is:\n',dir(os))

print('The current Working Directory is',os.getcwd())

print('creating a directory',os.mkdir('NewDir_'+ str(today)))

print('List of directories after creating a directory :',os.listdir('../'))

print('removing a directory',os.rmdir('NewDir_'+ str(today)))

print('List of directories after removing a directory:',os.listdir())
print('To check whether main.py is present in cwd or not',os.path.isfile('main.py'))
print('To check whether sample.txt is present in cwd or not',os.path.isfile('sample.txt'))
print('the size of main.py file is',os.path.getsize('main.py'))
print('To check whether file is present or not ',os.path.isfile('main.py'))
#print('To remove a file from the current working directory',os.remove('sample1.txt'))
os.chdir('C:/Users/hp/Desktop/Pythonexamples/')
print('After changing the current Working Directory is',os.getcwd())
print('The path is',os.environ.get('Path'))
print('Checking if certain path exists or not',os.path.exists('C:/Users/hp/PycharmProjects/pythonProject1/venv/Scripts'))
