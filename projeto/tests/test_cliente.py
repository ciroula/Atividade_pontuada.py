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
                      Endereco("tan", 15, "casa", "48598", "salva", Unidade_Federativa.BAHIA),
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

def test_modificando_email_do_cliente(criar_cliente):
    criar_cliente.email == "CriaDa2@"
    assert criar_cliente.email == "Mychel@"
def test_validando_email_do_cliente(criar_cliente):
    assert criar_cliente.email == "Mychel@"

def test_modificando_logradouro_do_cliente(criar_cliente):
    criar_cliente.endereco.logradouro == "cajacity"
    assert criar_cliente.endereco.logradouro == "tan"
def test_validando_logradouro_do_cliente(criar_cliente):
    assert criar_cliente.endereco.logradouro == "tan"

def test_modificando_numero_do_cliente(criar_cliente):
    criar_cliente.endereco.numero == 16
    assert criar_cliente.endereco.numero == 15
def test_validando_numero_do_cliente(criar_cliente):
    assert criar_cliente.endereco.numero == 15

def test_modificando_complemento_do_cliente(criar_cliente):
    criar_cliente.endereco.complemento == "apart"
    assert criar_cliente.endereco.complemento == "casa"
def test_validando_complemento_do_cliente(criar_cliente):
    assert criar_cliente.endereco.complemento == "casa"

def test_modificando_cep_do_cliente(criar_cliente):
    criar_cliente.endereco.cep == "422"
    assert criar_cliente.endereco.cep == "48598"
def test_validando_cep_do_cliente(criar_cliente):
    criar_cliente.endereco.cep == "56456"
    assert criar_cliente.endereco.cep == "48598"

def test_modificando_dataNascimento_do_cliente(criar_cliente):
    criar_cliente.dataNascimento == "5/4/4"
    assert criar_cliente.dataNascimento == "2/4/6"
def test_validando_dataNascimento_do_cliente(criar_cliente):
    assert criar_cliente.dataNascimento == "2/4/6"

def test_modificando_protocoloAtendimento_do_cliente(criar_cliente):
    criar_cliente.protocoloAtendimento == 89
    assert criar_cliente.protocoloAtendimento == 65
def test_validando_protocoloAtendimento_do_cliente(criar_cliente):
    assert criar_cliente.protocoloAtendimento == 65

def test_id_cliente_letras_retorna_mensagem_excecao(criar_cliente):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        Cliente("15", "Michel", 4548, "Mychel@", 
                      Endereco("tan", 15, "casa", "48598", "salva", Unidade_Federativa.BAHIA),
                      Sexo.MASCULINO, Estado_Civil.DIVORCIADO, "2/4/6", 65)

def test_telefone_cliente_invalido(criar_cliente):
   with pytest.raises(TypeError, match= "Digite apenas números."):
    Cliente(15, "Michel", "4548", "Mychel@", 
                      Endereco("tan", 15, "casa", "48598", "salva", Unidade_Federativa.BAHIA), 
                      Sexo.MASCULINO, Estado_Civil.DIVORCIADO, "2/4/6", 65)

#id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: Estado_Civil, dataNascimento: str, protocolo_de_Atendimento: int