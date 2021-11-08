#['varos', 'nev1', 'nev2', 'ferohely']
try:
    f=open("vb2018.txt",encoding="utf-8")
except:
    print("Nincs meg a file!")
else:
    f.readline()
    kisStadion=open("vb40alatt.txt","w",encoding="utf-8")
    kisStadion.write("Név;Férőhely\n")
    legkevesebb=[]
    lkFerohely=100000000
    for sor in f:
        sor=sor.rstrip("\n").split(";")
        #print(sor)
        if (int(sor[3])>40000):
            kisStadion.write(sor[1]+";"+sor[3]+"fő\n")
        
        if (int(sor[3])<lkFerohely):
            lkFerohely=int(sor[3])
            legkevesebb=sor

    print("Legkevesebb:")
    print("\tNév: "+legkevesebb[1])    
    print("\tHely: "+legkevesebb[3])    
    kisStadion.close()
    f.close()
    
    f=open("vb2018.txt",encoding="utf-8")
    
    print("7. feladat - Kérem a város nevét:", end="")
    varos=input()
    while(len(varos)<3):
        print("7. feladat - Kérem a város nevét:", end="")
        varos=input()
    
    sor=f.readline()
    nincsMeg=True
    while(sor and nincsMeg):
        sor=sor.rstrip("\n").split(";")
        if (sor[0].lower()==varos.lower()):
            nincsMeg=False;            
        sor=f.readline()
    if nincsMeg:
        print("8. Feladat - A megadott város nem VB helyszín!")
    else:
        print("8. Feladat - A megadott város VB helyszín!")

    f.close()