#learning python
#learning to work with lists and functions
#


import string

lcase = list(string.ascii_lowercase)
ucase = list(string.ascii_uppercase)
puncs = list(string.punctuation)
dgits = list(string.digits)

def ask():
    var = input("enter a string or enter to exit: ")
    if var != '':
        print(var)
        return(var)
    else:
        return(var)

#validate input
def vldate (stng, lcse , ucse, pncs, dgts):
    for w in stng:
        if w in lcse:
            rslt = cnt(lcse,w)
            print(w, "is lower case in position", rslt)
        elif w in ucse:
            rslt = cnt(ucse,w)
            print(w, "is upper case in position", rslt)
        elif w in puncs:
            rslt = cnt(puncs, w)
            print(w, "is punctution", rslt)
        elif w in dgts:
            rslt = cnt(dgts,w)
            print(w, "be digits", rslt)
        else:
            print(w, "is something I don't know")


def cnt (ltrs,stng):
    for x in stng:
        p = ltrs.index(x)
        rslt = p + 1
        return rslt
        
        


#run things
x = ask()

if x == "":
    print("Good bye")
    exit
else:
    vldate(x, lcase , ucase, puncs, dgits)

#rslt = vldate(x, lcase, ucase, puncs, dgits)
#print(x)
