'''
TITLE: Final Exam Question 1b
AUTHOR: Alex Pizzuto
DATE: 5/1/17
DESCRIPTION: Acronyms from inputs

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 5/1/17

'''

def simpleAcronym(phrase):
    pList = phrase.split()
    result = ''
    for item in pList:
        result = result + item[0]
    return result

print("simpleAcronym('National Football League') returns "+simpleAcronym("National Football League"))
print("simpleAcronym('National Hockey League') returns "+simpleAcronym("National Hockey League"))
print("simpleAcronym('American Cancer Society') returns "+simpleAcronym("American Cancer Society"))
