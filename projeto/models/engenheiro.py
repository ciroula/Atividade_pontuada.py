from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: Estado_Civil, 
                 dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crea:str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.crea = crea

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"CREA: {self.crea}")