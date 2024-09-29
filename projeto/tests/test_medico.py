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
    medico = Medico(7,"Michel", 5656, "Mychel@", 
                Endereco("tan", 15, "casa", "48598","Salvador", Unidade_Federativa.BAHIA), Sexo.MASCULINO,
                Estado_Civil.CASADO,"2/4/6", "321321", "321321", "321321", Setor.ENGENHARIA, 32133, "A04")
    return medico

def test_validando_id_do_medico(criar_medico):
    assert criar_medico.id == 7
def test_modificando_id_do_medico(criar_medico):
    criar_medico.id == 8
    assert criar_medico.id == 7

def test_modificando_nome_do_medico(criar_medico):
    criar_medico.nome == "brig"
    assert criar_medico.nome == "Michel"
def test_validando_nome_do_medico(criar_medico):
    assert criar_medico.nome == "Michel"
    
def test_modificando_telefone_do_medico(criar_medico):
    criar_medico.telefone == 5695
    assert criar_medico.telefone == 5656
def test_validando_telefone_do_medico(criar_medico):
    assert criar_medico.telefone == 5656

def test_modificando_email_do_medico(criar_medico):
    criar_medico.email == "CriaDa2@"
    assert criar_medico.email == "Mychel@"
def test_validando_email_do_medico(criar_medico):
    assert criar_medico.email == "Mychel@"

def test_modificando_logradouro_do_medico(criar_medico):
    criar_medico.endereco.logradouro == "cajacity"
    assert criar_medico.endereco.logradouro == "tan"
def test_validando_logradouro_do_medico(criar_medico):
    assert criar_medico.endereco.logradouro == "tan"

def test_modificando_numero_do_medico(criar_medico):
    criar_medico.endereco.numero == 16
    assert criar_medico.endereco.numero == 15
def test_validando_numero_do_medico(criar_medico):
    assert criar_medico.endereco.numero == 15

def test_modificando_complemento_do_medico(criar_medico):
    criar_medico.endereco.complemento == "apart"
    assert criar_medico.endereco.complemento == "casa"
def test_validando_complemento_do_medico(criar_medico):
    assert criar_medico.endereco.complemento == "casa"

def test_modificando_cep_do_medico(criar_medico):
    criar_medico.endereco.cep == "422"
    assert criar_medico.endereco.cep == "48598"
def test_validando_cep_do_medico(criar_medico):
    criar_medico.endereco.cep == "56456"
    assert criar_medico.endereco.cep == "48598"

def test_modificando_dataNascimento_do_medico(criar_medico):
    criar_medico.dataNascimento == "5/4/4"
    assert criar_medico.dataNascimento == "2/4/6"
def test_validando_dataNascimento_do_medico(criar_medico):
    assert criar_medico.dataNascimento == "2/4/6"
    
def test_modificando_cpf_do_medico(criar_medico):
    criar_medico.cpf == "45658"
    assert criar_medico.cpf == "321321"
def test_validando_cpf_do_medico(criar_medico):
    assert criar_medico.cpf == "321321"

def test_modificando_rg_do_medico(criar_medico):
    criar_medico.rg == "5469"
    assert criar_medico.rg == "321321"
def test_validando_rg_do_medico(criar_medico):
    assert criar_medico.rg == "321321"

def test_modificando_matricula_do_medico(criar_medico):
    criar_medico.matricula == "74856"
    assert criar_medico.matricula == "321321"
def test_validando_matricula_do_medico(criar_medico):
    assert criar_medico.matricula == "321321"

def test_modificando_salario_do_medico(criar_medico):
    criar_medico.salario == 74856
    assert criar_medico.salario == 32133
def test_validando_salario_do_medico(criar_medico):
    assert criar_medico.salario == 32133

def test_modificando_crm_do_medico(criar_medico):
    criar_medico.crm == "B04"
    assert criar_medico.crm == "A04"
def test_validando_crm_do_medico(criar_medico):
    assert criar_medico.crm == "A04"

def test_validar_genero_medico(criar_medico):
    assert criar_medico.sexo == Sexo.MASCULINO

def test_validar_unidade_federativa_medico(criar_medico):
    assert criar_medico.endereco.unidadefederativa == Unidade_Federativa.BAHIA

def test_validar_estado_civil_medico(criar_medico):
    assert criar_medico.estadoCivil == Estado_Civil.CASADO

def test_validar_setor_medico(criar_medico):
    assert criar_medico.setor == Setor.ENGENHARIA


def test_id_medico_letras_retorna_mensagem_excecao(criar_medico):
    with pytest.raises(TypeError, match= "ID só pode ser numeros."):
        Medico("7","Michel", 5656, "Mychel@", 
                    Endereco("tan", 15, "casa", "48598","Salvador", Unidade_Federativa.BAHIA), Sexo.MASCULINO,
                    Estado_Civil.CASADO,"2/4/6", "321321", "321321", "321321", Setor.ENGENHARIA, 32133, "A04")

def test_telefone_medico_invalido(criar_medico):
   with pytest.raises(TypeError, match= "Digite apenas números."):
    Medico(7,"Michel", "5656", "Mychel@", 
                Endereco("tan", 15, "casa", "48598","Salvador", Unidade_Federativa.BAHIA), Sexo.MASCULINO,
                Estado_Civil.CASADO,"2/4/6", "321321", "321321", "321321", Setor.ENGENHARIA, 32133, "A04")