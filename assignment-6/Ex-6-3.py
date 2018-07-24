'''
TITLE: Ex-6-3
AUTHOR: Alex Pizzuto
DATE: 3/05/17
DESCRIPTION: Takes a csv and separates entries with tabs

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/05/17

'''
def commasToTabs(st):
    myList = st.split(',')
    return "\t".join(myList)

file = open('numbers.csv','r')
for line in file:
    print(commasToTabs(line))
