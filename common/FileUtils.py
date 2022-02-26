import os

'''
@function get files from a folder
@description 
   no recursion and file extension name is '.hosts' only.
@Author Jiage
@Date 2021-08-20
'''
def getFiles(pathName):
    f = []
    for root, dirs, files in os.walk(pathName):
        for file in files:
            # .hosts file only
            if not file.endswith('.hosts'):
                continue
            file_path = os.path.join(root, file)
            f.append(file_path)
        # parents folder level 1 only
        break
    return f