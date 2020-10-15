from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import discord
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
#driver = webdriver.Chrome('/Users/Demosthenix/Downloads/chromedriver-1', options=chrome_options)
driver = webdriver.Chrome('/Users/Demosthenix/Downloads/chromedriver-1')
driver.get('https://www.cleverbot.com/')
def getResp(msg, driver=driver):
    try:
        agree = driver.find_element(By.XPATH, '//*[@id="noteb"]/form/input')
        agree.click()
    except:
        pass

    target = driver.find_element(By.XPATH, '//*[@id="avatarform"]/input[1]')
    target.send_keys(msg)
    target.send_keys(Keys.ENTER)
    #time.sleep(10)
    delay = 20
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="snipTextIcon"]')))
    return driver.find_element(By.XPATH, '//*[@id="line1"]/span[1]').text

client = discord.Client()

TOKEN = 'XXXXXXXXXXXXX'


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif client.user in message.mentions:
        msg = ' '.join(message.content.split('<@!642391597400588294>'))
        await message.channel.trigger_typing()
        resp = getResp(msg)
        await message.channel.send(resp)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)

