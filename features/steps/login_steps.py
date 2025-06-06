from behave import given, when, then
from selenium import webdriver
from features.actions.login_actions import LoginActions

@given("o usuario esta na pagina de login")
def step_abre_pagina_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://paulohlsena.github.io/formulario-testes/")
    context.login = LoginActions(context.driver)

@when("ele preenche usuario e senha validos")
def step_preenche_credenciais(context):
    context.login.fill_all_fields()
    context.login.click_on_submit()

@when("ele preenche com nome vazio")
def step_preenche_credenciais(context):
    context.login.fill_all_fields_without_name()
    context.login.click_on_submit()

@then("valido a mensagem de sucesso")
def step_validate_message(context):
    context.login.validate_success_message()

@then("valido que mensagem de sucesso nao existe")
def step_validate_message(context):
    context.login.validate_success_message_not_present()


