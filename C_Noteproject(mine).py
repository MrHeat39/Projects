Note = int(input("tell me about your Note and i will classify it "))
if Note <= 20 and Note >=17 :
    print("excellent!")
elif Note <= 16 and Note >= 14 :
    print("perfect")
elif Note <= 13 and Note >= 10 :
    print("good")
elif Note <= 9 and Note >= 1 :
    print("fail")
elif Note == 0 :
    print("bro what are you doing?")

######################################################

if Note < 0  :
    print("invailed Note!")
elif  Note >= 21 :
    print("invailed Note!")