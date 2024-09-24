from projeto.models.fisica import Fisica
from abc import ABC,abstractmethod

from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.sexo import Sexo

class Cliente(Fisica,ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: Estado_Civil, dataNascimento: str, protocolo_de_Atendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)

        self.protoco_de_Atendimento = protocolo_de_Atendimento
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"Protocolo de Atendimento: {self.protoco_de_Atendimento}")