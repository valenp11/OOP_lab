from selenium import webdriver
from selenium.webdriver.common.by import By 

url = "https://www.alza.cz/iphone-15?dq=7927612"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(1)

price = driver.find_element(by=By.CLASS_NAME, value="price-box__price")
price_xpath = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[3]/div[4]/div/div/div[3]/div[6]/div[5]/div[1]/div[1]/div[1]/div/span/span")

print(price.text)
print(price_xpath.text)

