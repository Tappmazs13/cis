list=[]
vegJel="0"
# Adatbekérés "*" végjelig
db=1
print("Adatok bekérése "+vegJel+" végjelig!")
print("Kérem a "+str(db)+". számot: ", end="")
a=input()
while (a!=vegJel):
    try:
        a=float(a)
    except:
        print("Számokat írj be, pl.: 35.68!")
    else:
        list.append(a)
        db+=1
    print("Kérem a "+str(db)+". számot: ", end="")
    a=input()

print(list)
if(list):
    print("A darabok száma: "+ str( len(list) )+" db" )
    print("A számok összege: "+ str( sum(list) ) )
    print("A számok átlaga: "+ str( round(sum(list)/len(list),2) ) )
    print("A legkisebb szám: "+ str( min(list)))
    print("A legnagyobb szám: "+ str( max(list)))

    print()
    print("Kérem az elvárt átlagot:", end="")
    elvartAtlag=input()
    try:
        elvartAtlag=float(elvartAtlag)
    except:
        print("Számokat írj be, pl.: 35.68!")
    else:
        print("Kérem az tűrést százalék:", end="")
        tures=input()
        try:
            tures=float(tures)
        except:
            print("Számokat írj be, pl.: 35.68!")
        else:
            atlag=sum(list)/len(list)
            print("Határok")
            #print(elvartAtlag-(elvartAtlag*tures/100))
            #print(elvartAtlag+(elvartAtlag*tures/100))
            if (atlag>=elvartAtlag-(elvartAtlag*tures/100)) and (atlag<=(elvartAtlag+(elvartAtlag*tures/100))):
                print("Az eredmények megfelelőek!")
            else:
                print("Az adatok nem felelnek meg az elvárásnak!")
