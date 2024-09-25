from projeto.models.endereco import Endereco
from abc import ABC,abstractmethod
class Pessoa(ABC):
    def __init__(self,id:int, nome:str, telefone:int, email:str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = nome
        self.telefone = self._verificarTelefone(telefone)
        self.email = email
        self.endereco = endereco
    


    def _verificar_id(self, id):
        if not isinstance (id,int):
            raise TypeError("ID só pode ser numeros.")
        return id  
    
    def _verificarTelefone(self,telefone):
        if not isinstance (telefone,int):
            raise TypeError("Digite apenas números.")
        if telefone < 0:
            raise ValueError("Não pode ser negativo")
        return telefone
    
    @abstractmethod
    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}")