from abc import ABC,abstractmethod
 
class parent(ABC):  
    @abstractmethod    
    def name(self):
        pass
 
class child(parent):
    def name(self):
        print("Aniket")
 
child_instance = child()
child_instance.name()