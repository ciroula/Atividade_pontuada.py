import pytest

from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
# from projeto.models.funcionario import Funcionario

@pytest.fixture
def criar_cliente():
    cliente = Cliente(15, "Michel", 4548, "Mychel@", 
                      Endereco("tan", 15, "casa", "48598", "sal", Unidade_Federativa.BAHIA),
                      Sexo.MASCULINO, Estado_Civil.DIVORCIADO, "2/4/6", 65)
    return cliente

def test_validando_id_do_cliente(criar_cliente):
    assert criar_cliente.id == 15
def test_modificando_id_do_cliente(criar_cliente):
    criar_cliente.id == 8
    assert criar_cliente.id == 15
def test_modificando_nome_do_cliente(criar_cliente):
    criar_cliente.nome == "brig"
    assert criar_cliente.nome == "Michel"
def test_validando_nome_do_cliente(criar_cliente):
    assert criar_cliente.nome == "Michel"


def test_id_cliente_letras_retorna_mensagem_excecao(criar_cliente):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        Cliente("15", "Michel", 4548, "Mychel@", 
                      Endereco("tan", 15, "casa", "48598", "sal", Unidade_Federativa.BAHIA),
                      Sexo.MASCULINO, Estado_Civil.DIVORCIADO, "2/4/6", 65)

def test_telefone_cliente_invalido(criar_cliente):
   with pytest.raises(TypeError, match= "Digite apenas números: "):
    Cliente(15, "Michel", "4548", "Mychel@", 
                      Endereco("tan", 15, "casa", "48598", "sal", Unidade_Federativa.BAHIA),
                      Sexo.MASCULINO, Estado_Civil.DIVORCIADO, "2/4/6", 65)