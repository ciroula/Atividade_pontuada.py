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
                                        Endereco("sal", 15, "casa", "846", "salva", Unidade_Federativa.BAHIA),
                                        "4186", "1565", 25.000, 50.000)