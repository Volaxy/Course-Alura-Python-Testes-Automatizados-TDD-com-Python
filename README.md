# Testes Automatizados: TDD com Python

Curso da Alura sobre testes com **Python** e tratamentos de exceção

## Objetivo Final &#x1F3AF;

Trabalhar com exceções com a classe `Bank` e realizar testes utilizando as bibliotecas do **Python**.

URL do curso -> [Testes Automatizados: TDD com Python](https://cursos.alura.com.br/course/tdd-com-python)

![Testes Automatizados: TDD com Python](https://www.alura.com.br/assets/api/share/curso-tdd-com-python.png)

## Links Úteis &#x1F517;
* [PyTest](https://docs.pytest.org) - Site para a biblioteca de testes **PyTest**.

## Siglas &#x1F5FA;
*

## Atalhos &#x2328;
* ***CTRL*** + ***P*** para mostrar quais parâmetros o construtor de um objeto espera receber.
* Para criar um novo **Teste** na aplicação **Python** na IDE **Pycharm**:
    * 1º) Pôr o mouse sobre o nome da classe que se quer testar.
    * 2º) ***CTRL*** + ***SHIFT*** + ***T*** para criar o novo teste.

## 01 - Por que Testar &#x1F516;
* O porquê testar.
* Como começar a testar com Python.
* Conhecemos a biblioteca `unittest`.
* Como escrever e rodar um teste com o Pycharm.

### 01 - Conhecendo o Domínio
* Criar um arquivo principal para testar o programa.

### 02 - Implementando o Avaliador de Leilões
* Antes de enviar um código para produção, é necessário verificar se o programa possui *bugs*.

### 03 - Começando com Testes de Unidade
* Utilizar um *Framework* para testar as aplicações **Python**.
* Usar o método `assertEqual(EXPECTED_VALUE, VALUE_RECEIVED)` para verificar se o valor corresponde ao esperado.

## 02 - Boas Práticas e mais alguns Testes &#x1F516;
* Formas de nomear os testes.
* Porque é importante dar nomes semânticos aos testes.
* Como isolar o cenário com o método `setUp`.

### 01 - Criando um novo Teste
* Criando um novo teste.

### 02 - Renomeando os Testes
* Nomear o nome dos métodos.

### 03 - Mais Testes e Classes de Equivalência
* **Classes de Equivalência** são testes parecidos com outros testes já feitos.

### 04 - Isolando a Criação do Cenário
* O método `setUp()` é executado antes de cada teste.

## 03 - Remodelando as Classes de Domínio &#x1F516;
* Como realizar uma cópia rasa de lista.
* Um pouco de programação defensiva.
* Conceitos como encapsulamento e comportamento.
* Como os testes ajudam na modelagem das classes.

### 01 - Um Pouco de Encapsulamento
* Encapsular os métodos da classe `Auction`.
* Retornar uma **cópia** de uma lista com `[:]`.

### 02 - Estado e Comportamento
* Encapsular a classe `Measurer` dentro de `Auction`.

## 04 - Novas Regras de Negócio e Testando Exceções &#x1F516;
* Como testar exceções com a `unittest`.
* O que são baby steps.
* Vimos que testes também são refatorados para atender as novas regras de negócio.

### 01 - Duas Novas Regras e Novos Testes
* Implementar novas regras de negócio.

### 02 - Testando Exceções e TDD
* Tratar exceções caso o caso de uso seja inválido.

### 03 - Uma Conversa sobre Passos de Bebê
* Modos de implementar uma regra de negócio.

## 05 - Adicionando Funcionalidades na Classe Usuário &#x1F516;
* O que é a biblioteca `pytest`.
* Como testar exceções com ela.
* As diferenças com a biblioteca `unittest`.
* Onde colocar os módulos de testes.

### 01 - Conhecendo a Pytest
* Instalar a biblioteca **PyTest**.

### 02 - Primeiros Testes com Pytest
* Criar primeiro teste com a biblioteca.

### 03 - Um Pouco mais de Testes
* Implementar regras de negocio relacionadas ao valor da carteira.

### 04 - Testando Exceções e Fixtures
* Usar a *annotation* `@pytest.fixture`.

## 06 - Refatorando o Projeto &#x1F516;
* Criar exceções.
* Técnicas de refatoração.
* A importância de manter um código legível.

### 01 - Isolando as Condições
* Refatoração da classe `Auction`.

### 02 - Criando uma Exceção ao Negócio
* Criar uma nova exceção.