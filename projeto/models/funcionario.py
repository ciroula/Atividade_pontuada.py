from projeto.models.fisica import Fisica
from abc import ABC,abstractmethod

from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor


class Funcionario(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: Estado_Civil, dataNascimento: str, cpf:str, rg:str,matricula:str, setor : Setor, salario : float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def _verificar_salario(self):
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"CPF: {self.cpf}"
                f"RG: {self.rg}"
                f"Matricula: {self.matricula}"
                f"Setor: {self.setor.value}"
                f"Salario: {self.salario}")