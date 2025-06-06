Feature: Cadastro de usuario valido
    Scenario: Preenchimento e envio do formulario
    Given o usuario esta na pagina de login
    When ele preenche usuario e senha validos
    Then valido a mensagem de sucesso