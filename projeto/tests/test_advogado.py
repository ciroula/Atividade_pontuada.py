import pytest

from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def criar_advogado():
    advogado = Advogado(7,"Revoada", 222, "qqq", 
                Endereco("Rua B", 88, "Casa", "9999","RJ", Unidade_Federativa.RIO_DE_JANEIRO), Sexo.MASCULINO,
                Estado_Civil.SOLTEIRO,"08/07/2000", "321312", "321321", "321321", Setor.OPERACOES, 32133, "A04")
    return advogado

def test_avaliando_nome_advogado(criar_advogado):
    assert criar_advogado.nome == "Revoada"

def test_id_advogado_letras_retorna_mensagem_excecao(criar_advogado):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        Advogado("7","Revoada", 222, "qqq", 
                Endereco("Rua B", 88, "Casa", "9999","RJ", Unidade_Federativa.RIO_DE_JANEIRO), Sexo.MASCULINO,
                Estado_Civil.SOLTEIRO,"08/07/2000", "321312", "321321", "321321", Setor.OPERACOES, 32133, "A04")