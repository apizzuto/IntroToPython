'''
TITLE: Ex-4-2
AUTHOR: Alex Pizzuto
DATE: 2/8/17
DESCRIPTION: Prints a list of strings as one string with vertical bars

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/8/17

'''

def barred(myList):
    """Join the strings in myList and add a bar between each"""
    st='|'
    for a in myList:
        st=st+a+"|"
    return st

def main():
    print(barred(["I","like","chocolate","cake"]))
    print(barred(["my","bars","are","straight","fire","right","now"]))
    print(barred(["short","list"]))
    print(barred(["pizza"]))

main()
