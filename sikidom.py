import math
class kor:
    r=0
    def __init__(self,sugar=1):
        self.r=sugar
    
    def kerulet(self):
        return 2*self.r+math.pi

    def terulet(self):
        return self.r*self.r*math.pi

    def terulet2(self):
        return self.r**2*math.pi

class hszog:
    a,b,c=0,0,0
    def __init__(self,a=1,b=1,c=1) -> None:
        self.a=a
        self.b=b
        self.c=c
    
    def kerulet(self):
        return self.a+self.b+self.c
    
    def terulet(self):
        s=self.kerulet()/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**(0.5)