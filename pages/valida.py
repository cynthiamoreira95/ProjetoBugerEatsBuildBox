from browser import Browser
class Valida(Browser):
    def get_text_title(self):
        return self.driver.find_element('xpath','/html/body/div[2]/div/div[6]/button[1]').text
