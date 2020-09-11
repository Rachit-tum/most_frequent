def my_func(word):
    b={}
    a=[]
    c=[]
    d=[]
    e=[]
    f={}
    for i in word:
        b[i]=word.count(i)
    for i in b:
        a.append(i)
        c.append(b[i])
    for i in range(len(word)):
        d.append(max(c))
        e.append(a[c.index(max(c))])
        a.remove(a[c.index(max(c))])
        c.remove(max(c))
        if a==[] and c==[]:
            break
    for i in range(len(e)):
        f[e[i]]=d[i]
        print(e[i],"occured: ", d[i]," times" )
        
        


my_func(input("Give A WORD: "))


        
    
