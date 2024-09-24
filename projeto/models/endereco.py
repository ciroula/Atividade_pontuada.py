from projeto.models.enums.unidade_federativa import Unidade_Federativa
class Endereco: 
    def __init__(self, logradouro : str, numero : int, complemento: str, cep: str, cidade: str, unidadefederativa: Unidade_Federativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.unidadefederativa = unidadefederativa
    def __str__(self) -> str:
        return (
            f"\n=== Endereço ==="
            f"\nLogradouro: {self.logradouro}"
            f"\nNumero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUF: {self.unidadefederativa.estado} / {self.unidadefederativa.sigla}"
        )