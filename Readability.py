text=input("Enter text")


letters=0
for ch in text:
    if ch.isalpha():
        letters+=1

words_list=text.split()
words=len(words_list)

sentences=text.count(".")+text.count("?")+text.count("!")

L=(letters/words)*100
S=(sentences/words)*100

X=0.0588 * L - 0.296 * S - 15.8
Grade = round(X)

#print(Grade)
if Grade <1:
    print("Below 1")
elif Grade>16:
    print("16+")
else:
    print(Grade)


