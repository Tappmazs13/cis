list=[]
vegJel="0"
# Adatbekérés "*" végjelig
db=1
print("Adatok bekérése "+vegJel+" végjelig!")
print("Kérem a "+str(db)+". számot: ", end="")
a=input()
while (a!=vegJel):
    list.append(a)
    db+=1
    print("Kérem a "+str(db)+". számot: ", end="")
    a=input()

print(list)
print("A darabok száma: "+ str( len(list) )+" db" )
print("A számok összege: "+ str( sum(list) ) )
if (len(list)>0):
    print("A számok átlaga: "+ str( round(sum(list)/len(list),2) ) )
    print("A legkisebb szám: "+ str( min(list)))
    print("A legnagyobb szám: "+ str( max(list)))

if (list):
    print()
    print("Kérem az elvárt átlagot:", end="")
    elvartAtlag=float(input())
    print("Kérem az tűrést százalék:", end="")
    tures=float(input())
    atlag=sum(list)/len(list)
    if (atlag>=elvartAtlag-(elvartAtlag*tures/100)) and (atlag<=(elvartAtlag+(elvartAtlag*tures/100))):
        print("Az eredmények megfelelőek!")
    else:
        print("Az adatok nem felelnek meg az elvárásnak!")
