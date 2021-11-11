import selenium
from selenium import webdriver


class Autolog:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.edureka.co/")

bot = Autolog()
bot.login()

