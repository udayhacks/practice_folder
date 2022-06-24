class uday():
    def __init__(self,name , date ) :
        self.names= name 
        self.dates= date
        
        
    @classmethod 
    def agefrom2000(cls ,name ,age ):
        return cls(name,2000-age)
    
    @staticmethod 
    def isadult(age):
        return age>18
    
    
    
    q = uday("uday",1990)
    print(q.)
    
        
        