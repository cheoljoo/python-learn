import numpy



class MyClass:
    
    model=0
    
    def __init__(self):            
        self.model=numpy.random.rand(2,2)*100
        print "MyClass instantiated"
        print self.model        
    def __del__(self):
        print "MyClass deleted"
    def Sum(self):          
        return numpy.sum(self.model)
    def Avr(self, count):      
        return numpy.sum(self.model)/count
        

instance = MyClass()
print('instance',instance)
print('Sum',instance.Sum())
print('Avr',instance.Avr(2))
del instance
print('program end')
