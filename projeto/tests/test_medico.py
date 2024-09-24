import pytest

from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
# from projeto.models.funcionario import Funcionario

@pytest.fixture
def criar_medico():
    medico = Medico(7,"Silvestre", 5656, "dwqdwq", 
                Endereco("Rua A", 77, "Casa", "8888","Salvador", Unidade_Federativa.BAHIA), Sexo.MASCULINO,
                Estado_Civil.CASADO,"08/07/2000", "321312", "321321", "321321", Setor.ENGENHARIA, 32133, "A04")
    return medico

def test_validando_id_do_medico(criar_medico):
    assert criar_medico.id == 7
def test_modificando_id_do_medico(criar_medico):
    criar_medico.id == 8
    assert criar_medico.id == 7
def test_modificando_nome_do_medico(criar_medico):
    criar_medico.nome == "Revoada"
    assert criar_medico.nome == "Silvestre"
def test_validando_nome_do_medico(criar_medico):
    assert criar_medico.nome == "Silvestre"


def test_id_medico_letras_retorna_mensagem_excecao(criar_medico):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        Medico("7","Silvestre", 5656, "dwqdwq", 
                    Endereco("Rua A", 77, "Casa", "8888","Salvador", Unidade_Federativa.BAHIA), Sexo.MASCULINO,
                    Estado_Civil.CASADO,"08/07/2000", "321312", "321321", "321321", Setor.ENGENHARIA, 32133, "A04")

def test_telefone_medico_invalido(criar_medico):
   with pytest.raises(TypeError, match= "Digite apenas números: "):
    Medico(7,"Silvestre", "5656", "dwqdwq", 
                Endereco("Rua A", 77, "Casa", "8888","Salvador", Unidade_Federativa.BAHIA), Sexo.MASCULINO,
                Estado_Civil.CASADO,"08/07/2000", "321312", "321321", "321321", Setor.ENGENHARIA, 32133, "A04")