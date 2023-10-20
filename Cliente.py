class Cliente:
    def __init__(self,n,fone):
        self._nome = n
        self._telefone = fone

    #Método GET
    def get_nome(self):
        return self._nome 
    
    #Método SET
    def set_nome(self, nome):
        self._nome = nome
        


'''
class Learning:
    def __init__(self, name, age, gender):
        self.title = learn
        self.subtitle = python
        self.paragraph = everyday
'''        
'''    
>>>Programmer = Learning("lean",python,"everyday")
>>>print Sue 
<_main_.Programmer instance at 0x32111320>
>>>print Programmer.subtitle
python
'''
