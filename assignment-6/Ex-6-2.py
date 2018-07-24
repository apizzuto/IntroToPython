'''
TITLE: Ex-6-2
AUTHOR: Alex Pizzuto
DATE: 3/05/17
DESCRIPTION: File concatenation program

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/05/17

'''
files = input('file concatenation program. \nEnter files to be concatenated: ')
fileList = files.split()
ofilename = input('Enter name of new file: ')
ofile = open(ofilename,'w')
for file in fileList:
    file = open(file,'r')
    for line in file:
        ofile.write(line)
    file.close()
ofile.close()
print('Files {} were successfully written to {}'.format(files,ofilename))
