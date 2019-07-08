s=input()
count=0
for i in range(len(s)):
    if (s[i].isdigit() or s[i].isalpha() or s[i]==" "):
        continue
    else:
        count+=1
print(count)    
