from selenium import webdriver

# gets name, message and count of the message to be send.
name=input("Name of the person to whom you need to send the msg : ")
msg=input("Message : ")
count=int(input("No.of the times the message has to be send : "))

# initializing the driver for chrome 
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# to proceed after scanning qr code in web.whatsapp
input("Enter any button after you scan the qr code")

try:
    # Find the user using the title attribute in whatsapp code
    user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
except:
    # Error while trying to search for user
    print("An error occured.(check the name you typed)\n Note: This project works for the whatspp web version 2.2023.2")
    exit()

# Click the whatsapp user and get into to send the message
user.click()

# Message box is selected
msg_box = driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text'][@data-tab='1']")

# Sends the message as many times as the count is specified.
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_1U1xa')
    button.click()
