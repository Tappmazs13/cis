#készítette:Horváth Hajnalka
#dátum:2021.11.05.


print("Készítette:Horváth Hajnalka Dátum:2021.11.05")

#Dolgozók szám:

beFajl = open( "feherBt.txt", "r",encoding="utf-8")


counter = 0
row = beFajl.readlines()[1:]
for line in row:
	

		counter +=1
print("Dolgozók szám:", counter)

#Nyíregyházi dolgozók száma

beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]
nyiregyhaziak = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Nyíregyháza"):
		nyiregyhaziak += 1

	
print ("Nyíregyházi dolgozók:", nyiregyhaziak)

#Győriek össz fizetése

beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]
gyorFizu = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Győr"):
		gyorFizu += float (lineSpt [3]) 

	
print ("Győriek fizetése:", gyorFizu)

#Győri dolgozók fizetésének átlaga

beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]

counter = 0
GyoriFizu = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Győr"):
		GyoriFizu += float (lineSpt [3])
		counter += 1

atl = GyoriFizu / counter	
beFajl.close()

kiFajl = open( "gyoriek.txt", "w", encoding="utf-8")
kiFajl.write( "Győri dolgozók fizetésének átlaga: ")
kiFajl.write("\n")	
kiFajl.write( str (atl))
kiFajl.close()
print("Győri dolgozók átlag fizetésének txt-je elkészült!")
