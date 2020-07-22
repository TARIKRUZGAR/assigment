

def funk(sentenses):
    kume = dict()
    for i in sentenses:
        c= 0
        for j in sentenses:
            if i==j:
                c+=1
        kume[i] = c
    print(kume)


funk(sentenses="merhabalar")
