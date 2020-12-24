# Automated script which completes the mcdonalds survey. 
#
# ## Dependencies

# +
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Get Users Input
CN1_Input = input()
CN2_Input = input()
CN3_Input = input()
CN4_Input = input()
CN5_Input = input()
CN6_Input = input()

# start webdriver, navigate to the survey site and have window take fullscreen
driver = webdriver.Firefox()
driver.get("https://www.mcdvoice.com/")
driver.maximize_window()
# -

### Enter input into Survey ###
CN1 = driver.find_element_by_name("CN1")
CN1.click()
CN1.send_keys(CN1_Input)
driver.implicitly_wait(135)

CN2 = driver.find_element_by_name("CN2")
CN2.click()
CN2.send_keys(CN2_Input)
driver.implicitly_wait(135)

CN3 = driver.find_element_by_name("CN3")
CN3.click()
CN3.send_keys(CN3_Input)
driver.implicitly_wait(135)

CN4 = driver.find_element_by_name("CN4")
CN4.click()
CN4.send_keys(CN4_Input)
driver.implicitly_wait(135)

CN5 = driver.find_element_by_name("CN5")
CN5.click()
CN5.send_keys(CN5_Input)
driver.implicitly_wait(135)

CN6 = driver.find_element_by_name("CN6")
CN6.click()
CN6.send_keys(CN6_Input)
driver.implicitly_wait(135)

NextButton = driver.find_element_by_name("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Next Section

# DriveThru = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'R004000.2')))
DriveThru = driver.find_element_by_xpath('//*[@id="FNSR004000"]/div[2]/div/div[4]/span/span')
DriveThru.click()
# DriveThru.send_keys(Keys.SPACE)

NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Next Section
EmployeeOrder = driver.find_element_by_xpath('//*[@id="FNSR000455"]/div[2]/div/div[2]/span/span')
EmployeeOrder.click()

NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Overall satisfaction
HighlySatisfied = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span')
HighlySatisfied.click()

NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Please rate your satisfaction with...
OrderAccuracy = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span')
OrderAccuracy.click()
cleanliness = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span')
cleanliness.click()
temperature = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[4]/td[2]/span')
temperature.click()
quality = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[5]/td[2]/span')
quality.click()
friendliness = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[6]/td[2]/span')
friendliness.click()
ease = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[7]/td[2]/span')
ease.click()

NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Please rate your satisfaction with (part 2)...
service = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span')
service.click()
taste = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span')
taste.click()
value = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[4]/td[2]/span')
value.click()

NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# What items did you order
breakfast_sandwich = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/div[1]/div[2]/div/div[2]/span/span')
breakfast_sandwich.click()
coffee = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/div[1]/div[2]/div/div[3]/span/span')
coffee.click()
# TODO add 3 cookies
NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Satisfaction with selected items
breakfast_sandwich_satisfaction = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span')
breakfast_sandwich_satisfaction.click()
coffee_satisfaction = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span')
coffee_satisfaction.click()

NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Did you experience a problem during your visit?
No = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span')
No.click()
NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Based on this visit, what is the likelihood that you will…
recommend = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span')
recommend.click()
returnto = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span')
returnto.click()

NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# General Feedback screen.
NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Were you asked to pull forward?
No = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span')
No.click()
NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# How valued did you feel as a customer?
HighlyValued = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span')
HighlyValued.click()
NextButton = driver.find_element_by_id("NextButton")
NextButton.click()
driver.implicitly_wait(135)

# Which fastfood is your favorite?
McDonalds = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div/div[1]/div[2]/div/div[8]/span/span')
McDonalds.click()
NextButton = driver.find_element_by_id("NextButton")
NextButton.click()

# Demographics
NextButton = driver.find_element_by_id("NextButton")
NextButton.click()