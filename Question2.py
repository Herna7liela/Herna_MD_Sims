# A pangram is a sentence that contains all the letters of the English alphabet at least
# once, for example: The quick brown fox jumps over the lazy dog. Your task here is to
# write a function to check a sentence to see if it is a pangram or not.

# have to make pangram a variable
# condition for pangram which contains all the letters of the alphabet
possible = input("Enter a sentece to check if its a pangram: ")
possibleset = []
def is_pangram(possible):
    possible = possible.lower()
    possibleset = set('abcdefghijklmnopqrstuvwxyz')

for c in possibleset:
    if c not in possible:
        print ("True")
    else:
        print ("False")
    possible = input("Enter a sentece to check if its a pangram: ")
            
##if possible == possibleold:
    #print ("True")
##else:
    #print ("False")

# possible = input("Enter a sentece to check if its a pangram: ")