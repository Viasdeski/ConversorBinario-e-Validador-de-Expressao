class Binario():
    def __init__(self):
        self.binario = []
    
    def peek(self): # retorna qual item esta no topo
        return self.binario[-1]
    
    def push(self, item): # metodo de inserir item
        self.binario.append(item)
       
    def is_empty(self): # teste se é vazia
        if len(self.binario) > 0:
            return False
        return True
        
    def pop(self): # remover o topo e retornar item para usuario
        if self.is_empty():# tratar caso de underflow
            print("Lista Vazia!")
            return None
        return self.binario.pop()
    
    def __len__(self): # retorna o total de itens
        return len(self.binario)
    
    def __str__(self): # representacao da pilha como string
        return str(self.binario)
         
    def dec2bin(self,decimal):
        while (decimal / 2) > 0:
            numeral,bin = divmod(decimal,2)
            self.push(bin)
            decimal = numeral
            
            
        
            
