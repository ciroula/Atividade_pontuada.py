import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

@pytest.fixture

def criar_engenheiro():
    engenheiro = Engenheiro(1, "Michel", 7484, "mychel@", 
                            Endereco("casa", 2, "grande", "4120", "salv", Unidade_Federativa.BAHIA),
                            Sexo.MASCULINO, Estado_Civil.SOLTEIRO, "24/11", "866", "70565", "2516",
                            Setor.JURIDICO, 50.000, "5698")
    return engenheiro

def test_validando_id_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.id == 1
def test_modificando_id_do_engenheiro(criar_engenheiro):
    criar_engenheiro.id == 8
    assert criar_engenheiro.id == 1
def test_id_engenheiro_letras_retorna_mensagem_excecao(criar_engenheiro):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        Engenheiro("1", "Michel", 7484, "mychel@", 
                            Endereco("casa", 2, "grande", "4120", "salv", Unidade_Federativa.BAHIA),
                            Sexo.MASCULINO, Estado_Civil.SOLTEIRO, "24/11", "866", "70565", "2516",
                            Setor.JURIDICO, 50.000, "5698")

def test_validando_nome_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.nome == "Michel"
def test_modificando_nome_do_engenheiro(criar_engenheiro):
    criar_engenheiro.nome == "Marcos"
    assert criar_engenheiro.nome == "Michel"

def test_validando_telefone_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.telefone == 7484
def test_modificando_telefone_do_engenheiro(criar_engenheiro):
    criar_engenheiro.telefone == 1546
    assert criar_engenheiro.telefone == 7484
def test_telefone_engenheiro_invalido(criar_engenheiro):
   with pytest.raises(TypeError,match = "Digite apenas números: "):
       Engenheiro(1, "Michel", "7484", "mychel@", 
                            Endereco("casa", 2, "grande", "4120", "salv", Unidade_Federativa.BAHIA),
                            Sexo.MASCULINO, Estado_Civil.SOLTEIRO, "24/11", "866", "70565", "2516",
                            Setor.JURIDICO, 50.000, "5698")
       
