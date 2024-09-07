from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

User_name = "YOUR_TEAMS_USER_NAME/EMAIL"
Password = "your_password"

# Setting up the Chrome driver to automate
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigating to a MS Teams Link
url = "https://teams.microsoft.com/v2/"
driver.get(url)
print("Opened Browser")
time.sleep(15)
# Find the input Email Field Attributes/Tags
input_email = driver.find_element(By.ID, 'i0116')
print("Full Screen...")
driver.fullscreen_window()
# Input Email into its field
print("Entering Email...")
input_email.send_keys(User_name)
# time.sleep(1)
print("Entered Email...")

print("Clicking Next...")
# Find the Next the button by its ID.
email_button_next = driver.find_element(By.ID, 'idSIButton9')
# Click on Next Button
email_button_next.click()
print("Clicked Next...")
time.sleep(3)

print("Entering Password...")
# i0118
# Find the input Password Field Attributes/Tags
input_password = driver.find_element(By.ID, 'i0118')
# Input Password into the field
input_password.send_keys(Password)
print("Entered Password...")
# time.sleep(3)

print("Clicking Next...")
# idSIButton9
# Find the Next the button by its ID.
password_button_next = driver.find_element(By.ID, 'idSIButton9')
# Click on Next Button
password_button_next.click()
print("Clicked Next...")
time.sleep(3)

print("Clicking CheckBox...")
# KmsiCheckboxField
# Find the CheckBox by its ID.
checkBox_button = driver.find_element(By.ID, 'KmsiCheckboxField')
# Click on Next Button
checkBox_button.click()
print("Clicked CheckBox...")
# time.sleep(1)

print("Clicking Yes Button...")
# idSIButton9
# Find the Yes Button by its ID.
yes_button_next = driver.find_element(By.ID, 'idSIButton9')
# Click on Yes Button
yes_button_next.click()
print("Click Yes Button")
print("Finding Switch Now Button")
time.sleep(100)
print("Clicking Switch Now")
# Find the Switch Now Button by its Class.
yes_button_next = driver.find_element(By.CLASS_NAME, 'ts-btn-fluent-primary')
# Click on Next Button
yes_button_next.click()
print("Click Switch Now")
time.sleep(100)



print("Logged In")
time.sleep(70)
print("Navigating...")
driver.get(url)
driver.fullscreen_window()
time.sleep(60)
current_source_url = driver.current_url
html_content = requests.get(current_source_url)
html_source = driver.page_source
print(html_source)
# with open("pagehtml.txt", "w") as html:
#     html.write(html_content.text[0:235768])
# time.sleep(10)


# with open("tst.txt", 'r') as file:
#     page_HTML = file.read()
page_HTML = html_content.text 
    
page_HTML_start_ind = page_HTML.find("chat_list_unread_text")
page_HTML_stop_ind = page_HTML.find("chatListItem_unreadIndicator")
# 
# print(fr"start_ind: {start_ind}, Stop-ind: {stop_ind} total: {stop_ind-start_ind}" )


Unread_chatBox_ID = page_HTML[page_HTML_start_ind:page_HTML_stop_ind]   
# print(res)


ID_Tag_strt_ind = Unread_chatBox_ID.find("id=")+4
Unread_chatBox_ID = Unread_chatBox_ID[ID_Tag_strt_ind:]
ID_Tag_end_ind = Unread_chatBox_ID.find("@unq.gbl.spaces")+15
Unread_chatBox_ID = Unread_chatBox_ID[:ID_Tag_end_ind]
print(Unread_chatBox_ID)



with open("res.txt", 'w') as Unread_chatBox_ID_File:
    Unread_chatBox_ID_File.write(Unread_chatBox_ID)

# chat-list-item_19:237287d1-e536-471e-b263-629c9662ae65_66f08b00-dabe-43c6-9325-bbed4f836cf0@unq.gbl.spaces
# Find the unread chatbox by its ID.
driver.fullscreen_window()
yes_button_next = driver.find_element(By.ID, Unread_chatBox_ID)
# Click on Next Button
yes_button_next.click()
print("Clicked In")
# time.sleep(3)
# Close the browser after 5 seconds


time.sleep(30)


driver.quit()   