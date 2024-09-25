from .endereco import Endereco
from .juridica import Juridica

class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, contratoInicio: float,contratoFim: float) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"Inicio do contrato: {self.contratoInicio}"
            f"Final do contrato: {self.contratoFim}"
            )
    
