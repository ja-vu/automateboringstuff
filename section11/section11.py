import os

path = r'c:\\spam\\eggs.png'
new_path = '\\'.join(['folder1','folder2','folder3','file.png'])
newnewpath = os.path.join('folder1', 'folder2', 'folders3', 'file.png')


'''
Use os.path.join() to join folders and file. This function works for any OS
Use os.getcwd() to return current path of folder
'''

print(newnewpath)
print(os.getcwd())
print(os.chdir('c:\\Workspace\\automateboringstuff\\section11'))

print(os.path.abspath('..\\section11.py'))

print(os.path.exists('c:\\hello'))
print(os.path.isfile('section11.py'))
print(os.path.getsize('section11.py'))
print(os.listdir('c:\\workspace\\automateboringstuff\\section11'))

totalSize = 0
for filename in os.listdir('c:\\workspace\\automateboringstuff\\section11\\spam'):
    if not os.path.isfile(os.path.join('c:\\workspace\\automateboringstuff\\section11\\spam', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\workspace\\automateboringstuff\\section11\\spam', filename))

print(totalSize)

# os.makedirs('c:\\workspace\\automateboringstuff\\section11\\delicious\\walnut\\waffles')