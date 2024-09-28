"""
RegistrationPage para a página de registro.

Esta classe define métodos específicos para interações com a página de registro.

Classes:
    RegistrationPage: Página de registro.
"""

from src.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    FIRSTNAME =	(By.ID,'customer.firstName')
    LASTNAME  =	(By.ID,'customer.lastName')
    ADRESS    =	(By.ID,'customer.address.street')
    CITY      =	(By.ID,'customer.address.city')
    STATE     =	(By.ID,'customer.address.state')
    ZYPCODE   =	(By.ID,'customer.address.zipCode')
    PHONE     =	(By.ID,'customer.phoneNumber')
    SSN       =	(By.ID,'customer.ssn')
    USERNAME  =	(By.ID,'customer.username')
    PASSWORD  =	(By.ID,'customer.password')
    CONFIRM   =(By.ID,'repeatedPassword')
    REGISTER_BUTTON  = (By.XPATH, "//input[@value='Register']")

    def register(self, firstname, lastname, address, city, state, zypcode, phone,ssn,user, password,confirm):
        """
        Realiza o registro de um novo usuário.

        Args:
            firstname (str): O primeiro nome.
            lastname (str): O sobrenome.
            address (str): O endereço.
            city (str): A cidade.
            state (str): O estado.
            zypcode (str): O código postal.
            phone (str): O número de telefone.
            ssn (str): O número de seguro social.
            user (str): O Usuário.
            password (str): A senha.
            confirm (str): A confirmaçao da senha.

        Returns:
            None
        """
  

        self.enter_text(self.FIRSTNAME, firstname)
        self.enter_text(self.LASTNAME, lastname)
        self.enter_text(self.ADRESS, address)
        self.enter_text(self.CITY, city)
        self.enter_text(self.STATE, state)
        self.enter_text(self.ZYPCODE, zypcode)
        self.enter_text(self.PHONE, phone)
        self.enter_text(self.SSN, ssn)
        self.enter_text(self.USERNAME, user)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.CONFIRM, confirm)
        self.click(self.REGISTER_BUTTON)

