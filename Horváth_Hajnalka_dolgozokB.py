
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

#Szegedi dolgozók száma

beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]
szegedi = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Szegedi"):
		szegedi += 1

	
print ("Szegedi dolgozók:", szegedi)

#Miskolciak fizetése

beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]
miskolcFizu = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Miskolc"):
		miskolcFizu += float (lineSpt [3]) 

	
print ("Miskolc fizetése:", miskolcFizu)

#Miskolc dolgozók fizetésének átlaga

beFajl = open( "feherBt.txt", "r",encoding="utf-8")

row = beFajl.readlines()[1:]

counter = 0
miskolcFizu = 0
for line in row:
	
	lineSpt = line.split(":")
	if (lineSpt[1] == "Miskolc"):
		miskolcFizu += float (lineSpt [3])
		counter += 1

atl = miskolcFizu / counter	
beFajl.close()

kiFajl = open( "miskolc.txt", "w", encoding="utf-8")
kiFajl.write( "Miskolc dolgozók fizetésének átlaga: ")
kiFajl.write("\n")	
kiFajl.write( str (atl))
kiFajl.close()
print("Miskolc dolgozók átlag fizetésének txt-je elkészült!")
