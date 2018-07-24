'''
TITLE: Ex-5-2
AUTHOR: Alex Pizzuto
DATE: 2/22/17
DESCRIPTION: Prompts user for name of an input file
and writes the lines of the file into
'numbered-lines.txt' with lines numbered
MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/22/17

'''
file = open(input('Enter the name of your file: '),"r")
ofile = open("numbered-lines.txt","w")
n=1
for line in file:
    ofile.write("({0}) ".format(n)+line)
    n=n+1
file.close()
ofile.close()
