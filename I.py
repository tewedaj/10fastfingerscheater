import pytesseract as te
te.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #you must download and install tesseract and if you install it in any other location than this one here you must change this directory
from PIL import Image
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

path = "C:\hu\chromedriver.exe"  # this is the path to the driver
chrom_opt = webdriver.ChromeOptions()
chrom_opt.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=path, options=chrom_opt)
def Login(email,password):#this function alone is usless it just loged in
    driver.get("https://10fastfingers.com/login")
    time.sleep(15)
    UserName = driver.find_element_by_name("data[User][email]")
    Password = driver.find_element_by_name("data[User][password]")
    loginButton = driver.find_element_by_id("login-form-submit")
    UserName.send_keys(email)
    Password.send_keys(password)
    loginButton.click()
def TypeFast(email,password,w):#this function will login and type crazy fast
    Login(email,password)
    time.sleep(29)
    x=0
    if w == None:
        w = 210
    while x < w: #if it finshes the whole thing 10fastfinger will actually know this is a bot so you can go ahead and finsh the whole thing your self
        words=driver.find_element(By.XPATH,"//span[@class='highlight']").text
        writer = driver.find_element(By.CLASS_NAME, "form-control")
        writer.send_keys(words," ")
        x+=1
def passAntiCheat():
    driver.get("https://10fastfingers.com/anticheat/view/1/1")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[@id='start-btn']").click()
    inputfiled = driver.find_element(By.XPATH,"//*[@id='word-input']")
    time.sleep(5)
    wordc = driver.find_element(By.XPATH,"//*[@id='word-img']/img")
    wordc.screenshot("wordmanssss.png")
    time.sleep(1)
    img = Image.open("wordmanssss.png")
    anticheat =te.image_to_string(img) #anti anti cheat go brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    abss=anticheat.split(" ")
    m =0
    for word in abss:
        if m == 30:
            break
        inputfiled.send_keys(word," ")
        m+=1

def AntiCheatOnly(email,password):
    Login(email,password)
    passAntiCheat()
def TypeFastAndPassAntiCheat(email,password,words):
    TypeFast(email,password,words)
    time.sleep(50)
    passAntiCheat()
def TypeFastAno(w):
    driver.get("https://10fastfingers.com/typing-test/english")
    time.sleep(29)
    x = 0
    if w == None:
        w = 210
    while x < w:
        words = driver.find_element(By.XPATH, "//span[@class='highlight']").text
        writer = driver.find_element(By.CLASS_NAME, "form-control")
        writer.send_keys(words, " ")
        x += 1