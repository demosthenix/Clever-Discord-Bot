from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from googletrans import Translator
import discord
import time

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
#driver = webdriver.Chrome('/Users/Demosthenix/Downloads/chromedriver-1')
driver.get('https://www.cleverbot.com/')
def getResp(msg, driver=driver):
    try:
        agree = driver.find_element(By.XPATH, '//*[@id="noteb"]/form/input')
        agree.click()
    except:
        pass

    target = driver.find_element(By.XPATH, '//*[@id="avatarform"]/input[1]')
    trans = Translator()
    msg_lang = trans.detect(msg).lang
    if msg_lang != 'en' or msg_lang != 'hi':
        msg = trans.translate(msg, src=msg_lang, dest='en').text
    target.send_keys(msg)
    target.send_keys(Keys.ENTER)
    #time.sleep(10)
    delay = 20
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="snipTextIcon"]')))
    resp = driver.find_element(By.XPATH, '//*[@id="line1"]/span[1]').text
    if msg_lang != 'en' or msg_lang != 'hi':
        resp = trans.translate(resp, src='en', dest=msg_lang).text
    return resp

client = discord.Client()

TOKEN = 'NjQyMzkxNTk3NDAwNTg4Mjk0.XcWPyw.Q-rQYdu3RCYHxADVmmPBzQkKgBE'


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

