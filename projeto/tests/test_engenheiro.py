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

def test_modificando_nome_do_engenheiro(criar_engenheiro):
    criar_engenheiro.nome == "brig"
    assert criar_engenheiro.nome == "Michel"
def test_validando_nome_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.nome == "Michel"

def test_modificando_telefone_do_engenheiro(criar_engenheiro):
    criar_engenheiro.telefone == 5695
    assert criar_engenheiro.telefone == 7484
def test_validando_telefone_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.telefone == 7484

def test_modificando_email_do_engenheiro(criar_engenheiro):
    criar_engenheiro.email == "CriaDa2@"
    assert criar_engenheiro.email == "mychel@"
def test_validando_email_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.email == "mychel@"

def test_modificando_logradouro_do_engenheiro(criar_engenheiro):
    criar_engenheiro.endereco.logradouro == "cajacity"
    assert criar_engenheiro.endereco.logradouro == "casa"
def test_validando_logradouro_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.endereco.logradouro == "casa"

def test_modificando_numero_do_engenheiro(criar_engenheiro):
    criar_engenheiro.endereco.numero == 16
    assert criar_engenheiro.endereco.numero == 2
def test_validando_numero_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.endereco.numero == 2

def test_modificando_complemento_do_engenheiro(criar_engenheiro):
    criar_engenheiro.endereco.complemento == "apart"
    assert criar_engenheiro.endereco.complemento == "grande"
def test_validando_complemento_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.endereco.complemento == "grande"

def test_modificando_cep_do_engenheiro(criar_engenheiro):
    criar_engenheiro.endereco.cep == "422"
    assert criar_engenheiro.endereco.cep == "4120"
def test_validando_cep_do_engenheiro(criar_engenheiro):
    criar_engenheiro.endereco.cep == "56456"
    assert criar_engenheiro.endereco.cep == "4120"

def test_modificando_dataNascimento_do_engenheiro(criar_engenheiro):
    criar_engenheiro.dataNascimento == "5/4/4"
    assert criar_engenheiro.dataNascimento == "24/11"
def test_validando_dataNascimento_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.dataNascimento == "24/11"

def test_modificando_cpf_do_engenheiro(criar_engenheiro):
    criar_engenheiro.cpf == "584"
    assert criar_engenheiro.cpf == "866"
def test_validando_cpf_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.cpf == "866"

def test_modificando_rg_do_engenheiro(criar_engenheiro):
    criar_engenheiro.rg == "5456"
    assert criar_engenheiro.rg == "70565"
def test_validando_rg_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.rg == "70565"

def test_modificando_matricula_do_engenheiro(criar_engenheiro):
    criar_engenheiro.matricula == "5456"
    assert criar_engenheiro.matricula == "2516"
def test_validando_matricula_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.matricula == "2516"

def test_modificando_salario_do_engenheiro(criar_engenheiro):
    criar_engenheiro.salario == 65.000
    assert criar_engenheiro.salario == 50.000
def test_validando_salario_do_engenhheiro(criar_engenheiro):
    assert criar_engenheiro.salario == 50.000

def test_modificando_crea_do_engenheiro(criar_engenheiro):
    criar_engenheiro.crea == "5456"
    assert criar_engenheiro.crea == "5698"
def test_validando_crea_do_engenheiro(criar_engenheiro):
    assert criar_engenheiro.crea == "5698"

def test_validar_genero_engenheiro(criar_engenheiro):
    assert criar_engenheiro.sexo == Sexo.MASCULINO

def test_validar_unidade_federativa_engenheiro(criar_engenheiro):
    assert criar_engenheiro.endereco.unidadefederativa == Unidade_Federativa.BAHIA

def test_validar_estado_civil_engenheiro(criar_engenheiro):
    assert criar_engenheiro.estadoCivil == Estado_Civil.SOLTEIRO

def test_validar_setor_engenheiro(criar_engenheiro):
    assert criar_engenheiro.setor == Setor.JURIDICO


def test_id_engenheiro_letras_retorna_mensagem_excecao(criar_engenheiro):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        Engenheiro("1", "Michel", 7484, "mychel@", 
                            Endereco("casa", 2, "grande", "4120", "salv", Unidade_Federativa.BAHIA),
                            Sexo.MASCULINO, Estado_Civil.SOLTEIRO, "24/11", "866", "70565", "2516",
                            Setor.JURIDICO, 50.000, "5698")

def test_telefone_engenheiro_invalido(criar_engenheiro):
   with pytest.raises(TypeError, match= "Digite apenas números."):
    Engenheiro(1, "Michel", "7484", "mychel@", 
                            Endereco("casa", 2, "grande", "4120", "salv", Unidade_Federativa.BAHIA),
                            Sexo.MASCULINO, Estado_Civil.SOLTEIRO, "24/11", "866", "70565", "2516",
                            Setor.JURIDICO, 50.000, "5698")
