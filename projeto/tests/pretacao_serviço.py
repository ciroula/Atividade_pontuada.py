import pytest

from projeto.models.prestacao_servico import PrestacaoServico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
# from projeto.models.funcionario import Funcionario

@pytest.fixture
def criar_prestacaoServico():
    prestacaoServico = PrestacaoServico("Michel", 15664, "Mych@", 
                                        Endereco("sal", 15, "casa", "846", "salva", Unidade_Federativa.BAHIA),
                                        "4186", "1565", 25.000, 50.000)
    return prestacaoServico

def test_modificando_nome_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.nome == "Revoada"
    assert criar_prestacaoServico.nome == "Michel"
def test_validando_nome_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.nome == "Michel"


def test_telefone_prestacaoServico_invalido(criar_prestacaoServico):
   with pytest.raises(TypeError, match= "Digite apenas números: "):
    PrestacaoServico("Michel", 15664, "Mych@", 
                                        Endereco("sal", 15,"casa", "846", "salva", Unidade_Federativa.BAHIA),
                                        "4186", "1565", 25.000, 50.000,)
    
def test_modificando_email_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.email == "CriaDa2@"
    assert criar_prestacaoServico.email == "Mych@"
def test_validando_email_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.email == "Mych@"

def test_modificando_logradouro_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.logradouro == "cajacity"
    assert criar_prestacaoServico.logradouro == "city"
def test_validando_logradouro_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.logradouro == "city"

def test_modificando_numero_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.numero == 16
    assert criar_prestacaoServico.numero == 15
def test_validando_numero_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.numero == 15

def test_modificando_complemento_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.complemento == "apart"
    assert criar_prestacaoServico.complemento == "casa"
def test_validando_complemento_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.complemento == "casa"

def test_modificando_cep_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.cep == "422"
    assert criar_prestacaoServico.cep == "846"
def test_validando_cep_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.cep == "846"

def test_modificando_cidade_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.cidade == "perna"
    assert criar_prestacaoServico.cidade == "salva"
def test_validando_cidade_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.cidade == "salva"

def test_modificando_cnpj_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.cnpj == "8585"
    assert criar_prestacaoServico.cnpj == "4186"
def test_validando_cnpj_do_prestacaoServico(8585iar_prestacaoServico):
    assert criar_prestacaoServico.cnpj == "4186"

def test_modificando_inscricaoEstadual_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.inscricaoEstadual == "4656"
    assert criar_prestacaoServico.inscricaoEstadual == "1565"
def test_validando_inscricaoEstadual_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.inscricaoEstadual == "1565"

def test_modificando_contratoInicio_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.contratoInicio == 22.000
    assert criar_prestacaoServico.contratoInicio == 25.000
def test_validando_contratoInicio_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.contratoInicio == 25.000

def test_modificando_contratoFim_do_prestacaoServico(criar_prestacaoServico):
    criar_prestacaoServico.contratoFim == 44.000
    assert criar_prestacaoServico.contratoFim == 50.000
def test_validando_contratoFim_do_prestacaoServico(criar_prestacaoServico):
    assert criar_prestacaoServico.contratoFim == 50.000

