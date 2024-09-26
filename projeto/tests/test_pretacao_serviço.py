import pytest

from projeto.models.prestacao_servico import PrestacaoServico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
# from projeto.models.funcionario import Funcionario

@pytest.fixture
def criar_prestacao_servico():
    prestacao_servico = PrestacaoServico(17, "Michel", 7878, "Michell@", 
                                        Endereco("sal", 15, "casa", "4568", "salva", Unidade_Federativa.BAHIA),
                                        "4186", "456", 25.000, 50.000)
    return prestacao_servico

def test_validando_id_do_prestacao_servico(criar_prestacao_servico):
    assert criar_prestacao_servico.id == 17
def test_modificando_id_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.id == 8
    assert criar_prestacao_servico.id == 17

def test_modificando_nome_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.nome == "brig"
    assert criar_prestacao_servico.nome == "Michel"
def test_validando_nome_do_prestacao_servico(criar_prestacao_servico):
    assert criar_prestacao_servico.nome == "Michel"

def test_modificando_telefone_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.telefone == 5695
    assert criar_prestacao_servico.telefone == 7878
def test_validando_telefone_do_prestacao_servico(criar_prestacao_servico):
    assert criar_prestacao_servico.telefone == 7878

def test_modificando_email_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.email == "CriaDa2@"
    assert criar_prestacao_servico.email == "Michell@"
def test_validando_email_do_prestacao_servico(criar_prestacao_servico):
    assert criar_prestacao_servico.email == "Michell@"

def test_modificando_logradouro_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.endereco.logradouro == "cajacity"
    assert criar_prestacao_servico.endereco.logradouro == "sal"
def test_validando_logradouro_do_prestacao_servico(criar_prestacao_servico):
    assert criar_prestacao_servico.endereco.logradouro == "sal"

def test_modificando_numero_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.endereco.numero == 16
    assert criar_prestacao_servico.endereco.numero == 15
def test_validando_numero_do_prestacao_servico(criar_prestacao_servico):
    assert criar_prestacao_servico.endereco.numero == 15

def test_modificando_complemento_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.endereco.complemento == "apart"
    assert criar_prestacao_servico.endereco.complemento == "casa"
def test_validando_complemento_do_prestacao_servico(criar_prestacao_servico):
    assert criar_prestacao_servico.endereco.complemento == "casa"

def test_modificando_cep_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.endereco.cep == "422"
    assert criar_prestacao_servico.endereco.cep == "4568"
def test_validando_cep_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.endereco.cep == "56456"
    assert criar_prestacao_servico.endereco.cep == "4568"

def test_modificando_cnpj_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.cnpj == "422"
    assert criar_prestacao_servico.cnpj == "4186"
def test_validando_cnpj_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.cnpj == "56456"
    assert criar_prestacao_servico.cnpj == "4186"

def test_modificando_inscricaoEstadual_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.inscricaoEstadual == "422"
    assert criar_prestacao_servico.inscricaoEstadual == "456"
def test_validando_inscricaoEstadual_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.inscricaoEstadual == "56456"
    assert criar_prestacao_servico.inscricaoEstadual == "456"

def test_modificando_contratoInicio_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.contratoInicio == 26.000
    assert criar_prestacao_servico.contratoInicio == 25.000
def test_validando_contratoInicio_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.contratoInicio == 26.000
    assert criar_prestacao_servico.contratoInicio == 25.000

def test_modificando_contratoFim_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.contratoFim == 56.000
    assert criar_prestacao_servico.contratoFim == 50.000
def test_validando_contratoFim_do_prestacao_servico(criar_prestacao_servico):
    criar_prestacao_servico.contratoFim == 56.000
    assert criar_prestacao_servico.contratoFim == 50.000



def test_id_medico_letras_retorna_mensagem_excecao(criar_prestacao_servico):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        PrestacaoServico("17" ,"Michel", 7878, "Michell@", 
                                        Endereco("sal", 15,"casa", "4568", "sal", Unidade_Federativa.BAHIA),
                                        "4186", "456", 25.000, 50.000,)

def test_telefone_prestacao_servico_invalido(criar_prestacao_servico):
   with pytest.raises(TypeError, match= "Digite apenas números."):
    prestacao_servico = PrestacaoServico(17 ,"Michel", "7878", "Michell@", 
                                        Endereco("sal", 15,"casa", "4568", "sal", Unidade_Federativa.BAHIA),
                                        "4186", "456", 25.000, 50.000,)