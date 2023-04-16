from pages.base_page import BasePage
import time


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    add_a_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def add_a_player(self):
        time.sleep(5)
        assert self.click_on_the_element(self.add_a_player_xpath)
