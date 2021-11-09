#készítette:Horváth Hajnalka
#dátum:2021.11.5.

print("készitette:Horváth Hajnalka Dátum:2021.11.05")
print("A program a bekért adatokból kiszámítja egy téglatest térfogatát")


oldalak=[]


def terfogat(oldalak):
	getTerfogat=1
	for i in range(0, len(oldalak)):
		terfogat=getTerfogat*oldalak[i]
		return terfogat

for i in range(0,3):
		oldalak.append(int(input("Kérem a téglatest" + str(i+1) + ". oldalának méretét:")))
	
result = terfogat(oldalak)

print("A téglatest térfogata:" , result)
