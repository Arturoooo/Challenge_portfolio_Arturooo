from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddPlayer(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button"
    add_a_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"
    login_url = 'https://scouts.futbolkolektyw.pl/en/'
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def click_on_the_add_a_player_button(self):
        self.click_on_the_element(self.add_a_player_xpath)

    def click_on_the_button(self, selector, selector_type=By.XPATH):
        return self.click_on_the_element(selector_type)