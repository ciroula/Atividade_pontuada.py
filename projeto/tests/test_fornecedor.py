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
    criar_fornecedor.nome == "brig"
    assert criar_fornecedor.nome == "Michel"
def test_validando_nome_do_fornecedor(criar_fornecedor):
    assert criar_fornecedor.nome == "Michel"

def test_modificando_telefone_do_fornecedor(criar_fornecedor):
    criar_fornecedor.telefone == 5695
    assert criar_fornecedor.telefone == 7878
def test_validando_telefone_do_fornecedor(criar_fornecedor):
    assert criar_fornecedor.telefone == 7878

def test_modificando_email_do_fornecedor(criar_fornecedor):
    criar_fornecedor.email == "CriaDa2@"
    assert criar_fornecedor.email == "mychellv@"
def test_validando_email_do_fornecedor(criar_fornecedor):
    assert criar_fornecedor.email == "mychellv@"

def test_modificando_logradouro_do_fornecedor(criar_fornecedor):
    criar_fornecedor.endereco.logradouro == "cajacity"
    assert criar_fornecedor.endereco.logradouro == "car"
def test_validando_logradouro_do_fornecedor(criar_fornecedor):
    assert criar_fornecedor.endereco.logradouro == "car"

def test_modificando_numero_do_fornecedor(criar_fornecedor):
    criar_fornecedor.endereco.numero == 16
    assert criar_fornecedor.endereco.numero == 5
def test_validando_numero_do_fornecedor(criar_fornecedor):
    assert criar_fornecedor.endereco.numero == 5

def test_modificando_complemento_do_fornecedor(criar_fornecedor):
    criar_fornecedor.endereco.complemento == "apart"
    assert criar_fornecedor.endereco.complemento == "casa"
def test_validando_complemento_do_fornecedor(criar_fornecedor):
    assert criar_fornecedor.endereco.complemento == "casa"

def test_modificando_cep_do_fornecedor(criar_fornecedor):
    criar_fornecedor.endereco.cep == "422"
    assert criar_fornecedor.endereco.cep == "4568"
def test_validando_cep_do_fornecedor(criar_fornecedor):
    criar_fornecedor.endereco.cep == "56456"
    assert criar_fornecedor.endereco.cep == "4568"

def test_modificando_inscricaoEstadual_do_fornecedor(criar_fornecedor):
    criar_fornecedor.inscricaoEstadual == "422"
    assert criar_fornecedor.inscricaoEstadual == "456"
def test_validando_inscricaoEstadual_do_fornecedor(criar_fornecedor):
    criar_fornecedor.inscricaoEstadual == "56456"
    assert criar_fornecedor.inscricaoEstadual == "456"

def test_modificando_produto_do_fornecedor(criar_fornecedor):
    criar_fornecedor.produto == "casa"
    assert criar_fornecedor.produto == "carro"
def test_validando_produto_do_fornecedor(criar_fornecedor):
    criar_fornecedor.produto == "moto"
    assert criar_fornecedor.produto == "carro"

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