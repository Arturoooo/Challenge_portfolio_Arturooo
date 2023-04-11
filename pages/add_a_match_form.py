from pages.base_page import BasePage


class Dashboard(BasePage):
    My_team_input_xpath = "//*[@name='myTeam']"
    Enemy_team_input_xpath = "//*[@name='enemyTeam']"
    My_team_score_input_xpath = "//*[@name='myTeamScore']"
    Match_at_home_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[1]/span[1]"
    Match_out_home_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[1]/span[1]"
    Date_input_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    Submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"
    Clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    General_input_xpath = "//*[@name='general']"
    Time_played_input_xpath = "//*[@name='timePlayed']"
    pass