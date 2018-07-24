'''
TITLE: Ex-7-1
AUTHOR: Alex Pizzuto
DATE: 3/22/17
DESCRIPTION: Intro to dictionaries

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/22/17

'''
firstName = { "president@whitehouse.gov": "Barack",
              "bill@microsoft.com": "Bill",
              "ctuckey@luc.edu": "Curtis",
              "santa@northpole.arc": "Santa",
              "chunkylover53@aol.com": "Homer"
              }
lastName = { "president@whitehouse.gov": "Obama",
              "bill@microsoft.com": "Gates",
              "ctuckey@luc.edu": "Tuckey",
              "santa@northpole.arc": "Claus",
              "chunkylover53@aol.com": "Simpson"
              }
telephone = { "president@whitehouse.gov": "888-the-prez",
              "bill@microsoft.com": "999-555-0001",
              "ctuckey@luc.edu": "700-288-2539",
              "santa@northpole.arc": "867-000-0000",
              "chunkylover53@aol.com": "888-555-1212"
              }
def lookup():
    key = input("Enter an email: ")
    formStr = "Name: {0} {1} | Email: {2} | Telephone: {3}"
    print(formStr.format(firstName[key],lastName[key],key,telephone[key]))

num = int(input("How many emails would you like to look up? "))
for i in range(num):
    lookup()
    i +=1
