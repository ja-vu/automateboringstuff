import os

def walkTree():
    for folderName, subfolders, filenames in os.walk('c:\\Workspace\\automateboringstuff\\section11\\delicious'):
        print("The folder is: " + folderName)
        print("The subfolders in " + folderName + ' are: ' + str(subfolders))
        print("The filenames in " + folderName + " are: " + str(filenames))
        print()

walkTree()