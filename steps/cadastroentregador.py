import time
from behave import given, when, then

from browser import Browser
from utils import Utils
from pages.valida import Valida
from nose.tools import assert_equal

import pyautogui

utils = Utils()
browser = Browser()
valida = Valida()


@given(u'que esteja na home do site')
def step_impl(context):
    utils.navegar('https://buger-eats.vercel.app/')


@given(u'clicar em "Cadastre-se para fazer entregas"')
def step_impl(context):
    """

    :param context:
    """
    utils.clicar_btn_cadastro()


@given(u'preencha os campos do formulario com dados validos')
def step_impl(context):
    """

    :param context:
    """
    utils.preenche_dados('Maverick Vinãles')
    utils.preenche_cpf('00000011122')
    utils.preenche_email('teste@teste.com')
    utils.preenche_whatsapp('99909876678')
    utils.preenche_cep('00000000')
    utils.clicar_btn_buscar_cep()
    utils.preenche_numero_casa('1')
    utils.scroll_down()
    utils.entrega_moto()
    utils.scroll_down()
    time.sleep(5)


@given(u'inserir uma imagem de cnh')
def step_impl(context):
    """

    :param context:
    """
    utils.clicar_btn_foto_cnh()
    pyautogui.click()
    time.sleep(2)
    pyautogui.write("CNH")
    pyautogui.press('enter')
    pyautogui.moveTo(x = 244, y = 192)
    pyautogui.doubleClick()


@when(u'clicar em cadastre-se para fazer entregas')
def step_impl(context):
    """

    :param context:
    """
    utils.submit()


@then(u'valido envio dos dados com sucesso')
def step_impl(context):
    """

    :param context:
    """
    assert_equal(valida.get_text_title(), 'Fechar')
    utils.fechar()