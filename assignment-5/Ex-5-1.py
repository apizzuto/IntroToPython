'''
TITLE: Ex-5-1
AUTHOR: Alex Pizzuto
DATE: 2/22/17
DESCRIPTION: Computes Exam One average score

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/22/17

'''
file = open("exam-1-scores.txt","r")
sum = 0
i=0
for line in file:
    sum = sum+int(line)
    i=i+1
ave=sum/i
print('The average exam score was {0:.0f}.'.format(ave))
file.close()
