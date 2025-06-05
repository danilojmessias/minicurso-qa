from behave import given, when, then
from selenium import webdriver
from features.actions.login_actions import LoginActions

@given("o usuário está na página de login")
def step_abre_pagina_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://paulohlsena.github.io/formulario-testes/")
    context.login = LoginActions(context.driver)

@when("ele preenche usuário e senha válidos")
def step_preenche_credenciais(context):
    context.login.fill_all_fields()


