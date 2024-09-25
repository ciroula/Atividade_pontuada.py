from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import Estado_Civil
from abc import ABC,abstractmethod

class Juridica(Pessoa,ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual
    
    
    @abstractmethod
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"CNPJ: {self.cnpj}"
                f"Inscricao Estadual: {self.inscricaoEstadual}")
    
'''    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (f"\nCNPJ: {self.cnpj}"
                f"\nInscrição estadual: {self.inscricaoEstadual}"
                f"\nPrestação de serviço: {self.prestacaoServico}")'''