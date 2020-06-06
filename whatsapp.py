from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

input("Enter any button after you scan the qr code")

name=input("Enter the name of the person to whom you need to send the msg")
msg=input("Enter the message")
count=int(input("Enter the count"))

try:
    user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
except:
    print("An error occured.(check the name you typed)\n Note: This project works for the whatspp web version 2.2023.2")
user.click()

msg_box = driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text'][@data-tab='1']")

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_1U1xa')
    button.click()
