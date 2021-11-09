
#készítette:Horváth Hajnalka
#dátum:2021.11.05.

print( "Készítette:Horváth Hajnalka Dátum:2021.11.05" )
print( "A program három tehenészeti telephely egy hónapos tejhozamát vizsgálja meg,és el kell döntenie kell e több tehenet vásárolni") 
print( "500liter tejhozam alatt kell tehenet vásárolni")

#három értékből számolok átlagot

telephely1 = 452.35
telephely2 = 628.45
telephely3 = 553.0

atlag = (telephely1+telephely2+telephely3)/3

	

if atlag <= 500:
	print("Átlag tejhozam: " ,atlag , "liter : tehenet kell vásárolni")

else:
	print("átlag tejhozam:" ,atlag , "liter: nem kell tehenet venni")

