# import zipfile,os
# examplezip=zipfile.ZipFile('sample-zip-file.zip')
# # print(examplezip.namelist()) this gives the list of file and folder in the zip file
# sample_txt=examplezip.getinfo('sample.txt')
# print(sample_txt.file_size)
# print(sample_txt.compress_size)
# examplezip.close()

# Extracting zip file

# import zipfile,os
# examplezip=zipfile.ZipFile('sample-zip-file.zip')
# examplezip.extract('sample.txt')

# examplezip.close()

# zipping a file

import zipfile,os
newZip=zipfile.ZipFile('new.zip','w')
newZip.write('sample.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()