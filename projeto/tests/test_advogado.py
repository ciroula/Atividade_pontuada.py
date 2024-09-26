import pytest

from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def criar_advogado():
    advogado = Advogado(15,"Michel", 222, "Mychel@", 
                Endereco("tan", 15, "casa", "48598","RJ", Unidade_Federativa.RIO_DE_JANEIRO), Sexo.MASCULINO,
                Estado_Civil.SOLTEIRO,"2/4/6", "321321", "321321", "321321", Setor.OPERACOES, 321321, "A04")
    return advogado

def test_validando_id_do_advogado(criar_advogado):
    assert criar_advogado.id == 15
def test_modificando_id_do_advogado(criar_advogado):
    criar_advogado.id == 8
    assert criar_advogado.id == 15

def test_validando_telefone_do_advogado(criar_advogado):
    assert criar_advogado.telefone == 222
def test_modificando_telefone_do_advogado(criar_advogado):
    criar_advogado.telefone == 456
    assert criar_advogado.telefone == 222

def test_modificando_nome_do_advogado(criar_advogado):
    criar_advogado.nome == "brig"
    assert criar_advogado.nome == "Michel"
def test_validando_nome_do_advogado(criar_advogado):
    assert criar_advogado.nome == "Michel"

def test_modificando_email_do_advogado(criar_advogado):
    criar_advogado.email == "CriaDa2@"
    assert criar_advogado.email == "Mychel@"
def test_validando_email_do_advogado(criar_advogado):
    assert criar_advogado.email == "Mychel@"

def test_modificando_logradouro_do_advogado(criar_advogado):
    criar_advogado.endereco.logradouro == "cajacity"
    assert criar_advogado.endereco.logradouro == "tan"
def test_validando_logradouro_do_advogado(criar_advogado):
    assert criar_advogado.endereco.logradouro == "tan"

def test_modificando_numero_do_advogado(criar_advogado):
    criar_advogado.endereco.numero == 16
    assert criar_advogado.endereco.numero == 15
def test_validando_numero_do_advogado(criar_advogado):
    assert criar_advogado.endereco.numero == 15

def test_modificando_complemento_do_advogado(criar_advogado):
    criar_advogado.endereco.complemento == "apart"
    assert criar_advogado.endereco.complemento == "casa"
def test_validando_complemento_do_advogado(criar_advogado):
    assert criar_advogado.endereco.complemento == "casa"

def test_modificando_cep_do_advogado(criar_advogado):
    criar_advogado.endereco.cep == "422"
    assert criar_advogado.endereco.cep == "48598"
def test_validando_cep_do_advogado(criar_advogado):
    criar_advogado.endereco.cep == "56456"
    assert criar_advogado.endereco.cep == "48598"

def test_modificando_dataNascimento_do_advogado(criar_advogado):
    criar_advogado.dataNascimento == "5/4/4"
    assert criar_advogado.dataNascimento == "2/4/6"
def test_validando_dataNascimento_do_advogado(criar_advogado):
    assert criar_advogado.dataNascimento == "2/4/6"

def test_modificando_cpf_do_advogado(criar_advogado):
    criar_advogado.cpf == "5/4/4"
    assert criar_advogado.cpf == "321321"
def test_validando_cpf_do_advogado(criar_advogado):
    assert criar_advogado.cpf == "321321"

def test_modificando_rg_do_advogado(criar_advogado):
    criar_advogado.rg == "5469"
    assert criar_advogado.rg == "321321"
def test_validando_rg_do_advogado(criar_advogado):
    assert criar_advogado.rg == "321321"

def test_modificando_matricula_do_advogado(criar_advogado):
    criar_advogado.matricula == "74856"
    assert criar_advogado.matricula == "321321"
def test_validando_matricula_do_advogado(criar_advogado):
    assert criar_advogado.matricula == "321321"

def test_modificando_salario_do_advogado(criar_advogado):
    criar_advogado.salario == 15648
    assert criar_advogado.salario == 321321
def test_validando_salario_do_advogado(criar_advogado):
    assert criar_advogado.salario == 321321

def test_modificando_oab_do_advogado(criar_advogado):
    criar_advogado.oab == "74856"
    assert criar_advogado.oab == "A04"
def test_validando_oab_do_advogado(criar_advogado):
    assert criar_advogado.oab == "A04"



def test_id_advogado_letras_retorna_mensagem_excecao(criar_advogado):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        Advogado("15","Michel", 222, "Mychel@", 
                Endereco("tan", 15, "casa", "48598","RJ", Unidade_Federativa.RIO_DE_JANEIRO), Sexo.MASCULINO,
                Estado_Civil.SOLTEIRO,"2/4/6", "321321", "321321", "321321", Setor.OPERACOES, 321321, "A04")
        
def test_telefone_advogado_invalido(criar_advogado):
   with pytest.raises(TypeError, match= "Digite apenas números."):
    Advogado(15,"Michel", "222", "Mychel@", 
                Endereco("tan", 15, "casa", "48598","RJ", Unidade_Federativa.RIO_DE_JANEIRO), Sexo.MASCULINO,
                Estado_Civil.SOLTEIRO,"2/4/6", "321321", "321321", "321321", Setor.OPERACOES, 321321, "A04")