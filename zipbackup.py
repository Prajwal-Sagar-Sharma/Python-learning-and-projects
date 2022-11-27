# import zipfile,os
# # zip_backup=zipfile.ZipFile('backup.zip','w')
# # def backup(folder_path):
# #     os.chdir(folder_path)
# #     for i in os.listdir():
# #         if os.path.isfile(i):
# #             zip_backup.write(i,compress_type=zipfile.ZIP_DEFLATED)
    
# # backup('E:\My Python Journey')


# zip_file=zipfile.ZipFile('backup.zip')
# print(zip_file.namelist())
# zip_file.extract('sample.txt')