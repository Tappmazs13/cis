
#készítette:Horváth Hajnalka
#dátum:2021.11.05.

print( "Készítette:Horváth Hajnalka Dátum:2021.11.05" )
print( "A program három nap átlag hőmérsékletét számolja ki,ez alapján eldöntjük kell e fűteni? ")
print( "A fűtést csak 15°C alatt kell  bekapcsolni")


nap01 = 11.4
nap02 = 18.2
nap03 = 16.0

atlag = (nap01+nap02+nap03)/3

	

if atlag >= 15:
	print("Átlag hőmérséklet: " ,atlag , "fok.:nem kell fűteni")

else:
	print("átlag hőmérésklet:" ,atlag , "fok!:kell fűteni")
