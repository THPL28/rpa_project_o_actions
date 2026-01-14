"""
RegistrationPage para a página de registro.

Esta classe define métodos específicos para interações com a página de registro.

Classes:
    RegistrationPage: Página de registro.
"""

from .base_page import BasePage

class RegistrationPage(BasePage):
    FIRSTNAME = "id:customer.firstName"
    LASTNAME  = "id:customer.lastName"
    ADDRESS   = "id:customer.address.street"
    CITY      = "id:customer.address.city"
    STATE     = "id:customer.address.state"
    ZIPCODE   = "id:customer.address.zipCode"
    PHONE     = "id:customer.phoneNumber"
    SSN       = "id:customer.ssn"
    USERNAME  = "id:customer.username"
    PASSWORD  = "id:customer.password"
    CONFIRM   = "id:repeatedPassword"
    REGISTER_BUTTON = "xpath://input[@value='Register']"

    def register(self, data):
        """Realiza o registro de um novo usuário usando um dicionário de dados."""
        self.enter_text(self.FIRSTNAME, data['firstname'])
        self.enter_text(self.LASTNAME, data['lastname'])
        self.enter_text(self.ADDRESS, data['address'])
        self.enter_text(self.CITY, data['city'])
        self.enter_text(self.STATE, data['state'])
        self.enter_text(self.ZIPCODE, data['zipcode'])
        self.enter_text(self.PHONE, data['phone'])
        self.enter_text(self.SSN, data['ssn'])
        self.enter_text(self.USERNAME, data['username'])
        self.enter_text(self.PASSWORD, data['password'])
        self.enter_text(self.CONFIRM, data['confirm'])
        self.click(self.REGISTER_BUTTON)

