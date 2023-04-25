from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button"
    add_a_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = 'Scouts Panel'
    futbol_kolektyw_logo_xpath = '//*[@title ="Logo Scouts Panel"]'
    Name_placeholder_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input'
    Submit_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]/span[1]'
    add_language_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[15]/button/span[1]'
    remove_language_button_xpath = '//*[@title ="Remove language"]'
    surname_placeholder_xpath = '//*[@name ="surname"]'
    main_position_placeholder_xpath = '//*[@name ="mainPosition"]'
    age_placeholder_xpath = '//*[@name ="age"]'
    dropdown_list_xpath = '//*[@aria-haspopup ="listbox"]'
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

    def type_in_name(self, name):
        self.field_send_keys(self.Name_placeholder_xpath, name)

    def click_on_the_button(self):
        self.click_on_the_element(self.Submit_button_xpath)

    def click_on_add_language_button(self):
        self.click_on_the_element(self.add_language_button_xpath)

    def click_on_remove_language_button(self):
        self.click_on_the_element(self.remove_language_button_xpath)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_placeholder_xpath, surname)
    def type_in_position(self, position):
        self.field_send_keys(self.main_position_placeholder_xpath, position)
    def type_in_age(self, age):
        self.field_send_keys(self.age_placeholder_xpath, age)

    def click_on_the_dropdown_list(self):
        self.click_on_the_element(self.dropdown_list_xpath)

    def wait_for_button_will_be_clickable(self):
        pass

