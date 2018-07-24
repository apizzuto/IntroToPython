'''
TITLE: Ex-6-1
AUTHOR: Alex Pizzuto
DATE: 3/05/17
DESCRIPTION: Rearranges names into a list of names last, first

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/05/17

'''
file = open('names-first-last.txt','r')
ofile = open('names-last-first.txt','w')
for line in file:
    nameList = line.split()
    ofile.write(nameList[1]+', '+nameList[0]+'\n')
file.close()
ofile.close()
