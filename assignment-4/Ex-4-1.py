'''
TITLE: Ex-4-1
AUTHOR: Alex Pizzuto
DATE: 2/8/17
DESCRIPTION: Prints a list of strings as one spaced out string

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/8/17

'''

def spacedOut(myList):
    """Join the strings in myList and add a space between each"""
    st=''
    for a in myList:
        st=st+a+" "
    return st

def main():
    print(spacedOut(["I","like","chocolate","cake"]))
    print(spacedOut(["look","at","the","spaces","in","my","new","string"]))
    print(spacedOut(["short","list"]))
    print(spacedOut(["pizza"]))

main()
