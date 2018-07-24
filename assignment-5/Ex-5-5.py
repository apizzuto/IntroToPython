'''
TITLE: Ex-5-5
AUTHOR: Alex Pizzuto
DATE: 2/22/17
DESCRIPTION: Using the join method to define
spacedOut and barred as seen before
MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/22/17

'''
def spacedOut(myList):
    """Join the strings in myList and add a space between each"""
    st=" ".join(myList)
    return st

def barred(myList):
    """Join the strings in myList and add a bar between each"""
    st='|'+'|'.join(myList)+'|'
    return st

def main():
    print(spacedOut(["I","like","chocolate","cake"]))
    print(spacedOut(["look","at","the","spaces","in","my","new","string"]))
    print(spacedOut(["short","list"]))
    print(spacedOut(["pizza"]))
    print(barred(["I","like","chocolate","cake"]))
    print(barred(["my","bars","are","straight","fire","right","now"]))
    print(barred(["short","list"]))
    print(barred(["pizza"]))

main()


