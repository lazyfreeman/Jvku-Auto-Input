from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yaml

# 读取配置文件
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

username = config['username']
password = config['password']
text = config['text']

driver = webdriver.Edge()
driver.get("https://www.pigai.org")

# 登录
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element("css selector", "#ulogin img").click()

driver.execute_script("alert('打开你需要写的作文的提交页面，之后回到终端按 Enter 键');")
input("打开你需要写的作文的提交页面，之后回到终端按 Enter 键")
text_input = driver.find_element("css selector", "textarea#contents")

text_input.send_keys(text)

# 保持浏览器打开，直到手动关闭
driver.execute_script("alert('请检查作文并手动提交，之后回到终端按 Enter 键关闭浏览器');")
input("请检查作文并手动提交，之后回到终端按 Enter 键关闭浏览器")
driver.quit()  # 关闭浏览器