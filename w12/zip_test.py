import zipfile

zf = zipfile.ZipFile('sample.zip', 'w')
zf.write('email_list.xlsx')
zf.write('sample.xlsx')
zf.close()

uzf = zipfile.ZipFile('sample.zip', 'r')
uzf.extractall(path='/Users/choidaehan')