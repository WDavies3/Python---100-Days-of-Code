#calculates percent compatibility between two people
#this calculator counts the number of the letters 
#t.r.u.e. and l.o.v.e. in the two names, adds up the 
#number, and the count of the true is the first number
#in the percent and the count of the love is the second
#number in the percent

def loveCalculator(name1 = "", name2 = ""):
    bothNames = name1.lower() + name2.lower()
    letterDict = {}
    true = 0
    love = 0
    for c in bothNames:
        letterDict[c] = letterDict[c] + 1 if c in letterDict else 1
    for c in "true":
        if c in letterDict:
            true += letterDict[c]
    for c in "love":
        if c in letterDict:
            love += letterDict[c]
    return int(str(true) + str(love))

print(loveCalculator("Jim", "Pam"))
print(loveCalculator("Romeo", "Juliet"))

