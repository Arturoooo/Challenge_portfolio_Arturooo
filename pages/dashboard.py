from pages.base_page import BasePage


class Dashboard(BasePage):
    Main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    Players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    Language_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    Sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    Players_count_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[1]/div"
    Matches_count_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[2]/div"
    Shortcuts_add_player_hyperlink_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a"
    Events_count_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[4]/div"
    Dev_team_contact_hyperlink_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a"
    Activity_Panel_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div"
    pass