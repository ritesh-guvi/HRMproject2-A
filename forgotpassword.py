from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Ritesh:
    def __init__(self, url):
       self.url = url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       
      
      
       
       
    
    def login(self):

        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        
        
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()

        
         
        self.username = 'Admin'

        
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        
        
        
        
        
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]').click()
        
        
        
    
        

        
                                 
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

Ritesh(url).login()