Feature: Cadastro de usuario invalido
    Scenario: Preenchimento e envio do formulario invalido
    Given o usuario esta na pagina de login
    When ele preenche com nome vazio
    Then valido que mensagem de sucesso nao existe