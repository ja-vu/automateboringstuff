import os
import shutil

print(os.getcwd())
# os.rmdir('c:\\Workspace\\automateboringstuff\\section11\\test')
# shutil.rmtree('c:\\Workspace\\automateboringstuff\\section11\\test_backup')

os.chdir('c:\\Workspace\\automateboringstuff\\section11')
for filename in os.listdir():
    if filename.endswith('txt'):
        #os.unlink(filename)
        print(filename)

