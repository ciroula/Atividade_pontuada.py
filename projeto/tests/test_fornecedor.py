import pytest

from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
# from projeto.models.funcionario import Funcionario

@pytest.fixture
def criar_fornecedor():
    fornecedor = Fornecedor(17, "Michel", 7878, "mychellv@", 
                            Endereco("car", 5, "casa", "4568", "salv", Unidade_Federativa.BAHIA), 
                            "485648", "456", "carro")
    return fornecedor

def test_validando_id_do_fornecedor(criar_fornecedor):
    assert criar_fornecedor.id == 17
def test_modificando_id_do_fornecedor(criar_fornecedor):
    criar_fornecedor.id == 8
    assert criar_fornecedor.id == 17
def test_modificando_nome_do_fornecedor(criar_fornecedor):
    criar_fornecedor.nome == "carlos"
    assert criar_fornecedor.nome == "Michel"
def test_validando_nome_do_fornecedor(criar_fornecedor):
    assert criar_fornecedor.nome == "Michel"


def test_id_fornecedor_letras_retorna_mensagem_excecao(criar_fornecedor):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        Fornecedor("17", "Michel", 7878, "mychellv@", 
                            Endereco("car", 5, "casa", "4568", "salv", Unidade_Federativa.BAHIA), 
                            "485648", "456", "carro")

def test_telefone_fornecedor_invalido(criar_fornecedor):
   with pytest.raises(TypeError, match= "Digite apenas números."):
    Fornecedor(17, "Michel", "7878", "mychellv@", 
                            Endereco("car", 5, "casa", "4568", "salv", Unidade_Federativa.BAHIA), 
                            "485648", "456", "carro")