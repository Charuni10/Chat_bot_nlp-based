arr=["cat","listen","silent","kitten","salient"]
lst={}
for i in arr:
    stri=str(sorted(i))
    if stri in lst:
        lst[stri].append(i)
    else:
        lst[stri]=[i]
print(len(lst))
