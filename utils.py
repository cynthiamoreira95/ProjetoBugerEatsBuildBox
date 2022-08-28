
import selenium
import browser
from browser import Browser


class Utils(Browser):
    def navegar(self, url):
        self.driver.get(url)

    def clicar_btn_cadastro(self):
        self.driver.find_element('xpath', '//*[@id="page-home"]/div/main/a/strong').click()

    def preenche_dados(self, nome):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[1]/div[1]/input').send_keys(
            nome)

    def preenche_cpf(self, numero):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[1]/div[2]/input').send_keys(
            numero)

    def preenche_email(self, email):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[2]/div[1]/input').send_keys(
            email)

    def preenche_whatsapp(self, numero):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[2]/div[2]/input').send_keys(
            numero)

    def preenche_cep(self, numero):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[2]/div[1]/div[1]/input').send_keys(
            numero)

    def preenche_numero_casa(self, numero):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[2]/div[3]/div[1]/input').send_keys(
            numero)

    def clicar_btn_buscar_cep(self):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[2]/div[1]/div[2]/input').click()

    def entrega_moto(self):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[3]/ul/li[1]/img').click()

    def entrega_bicicleta(self):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[3]/ul/li[2]/img').click()

    def entrega_van_carro(self):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[3]/ul/li[3]/img').click()


    def scroll_down(self):
        self.driver.execute_script('window.scroll(0,2000)')

    def clicar_btn_foto_cnh(self):
        self.driver.find_element('xpath', "//div[@class='dropzone']").click()

    def submit(self):
        self.driver.find_element('xpath', '//*[@id="page-deliver"]/form/button').click()

    def fechar(self):
        self.driver.find_element('xpath', '/html/body/div[2]/div/div[6]/button[1]').click()
