import sikidom

circle=sikidom.kor();
print("Kerulet: "+str(circle.kerulet()) )
print("Terulet: "+str(circle.terulet()) )
print("Terulet2: "+str(circle.terulet2()) )

circle=sikidom.kor(10);
print("Kerulet: "+str(circle.kerulet()) )
print("Terulet: "+str(circle.terulet()) )
print("Terulet2: "+str(circle.terulet2()) )

haromSzog=sikidom.hszog(5,5,6)
print()
print("Háromszog kerulet:"+str(haromSzog.kerulet()))
print("Háromszog terulet:"+str(haromSzog.terulet()))

haromSzog=sikidom.hszog()
print()
print("Háromszog kerulet:"+str(haromSzog.kerulet()))
print("Háromszog terulet:"+str(haromSzog.terulet()))