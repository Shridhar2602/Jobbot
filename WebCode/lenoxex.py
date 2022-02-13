from selenium import webdriver
import time
import os


str1 = os.path.dirname(__file__)

#if not using firefox Comment this out this is for firefox
firefox_path = str1 + "/../drivers/geckodriver"
chrome_path = str1 + "/../drivers/chromedriver"

def web(mylist, loc):
	#Uncomment this line to use Chrome
	# web_driver = webdriver.Chrome(executable_path=chrome_path )
	
	#if not using firefox Comment this out this is for firefox
	web_driver = webdriver.Firefox(executable_path=firefox_path)

	print(mylist[0])

	url = 'https://lenoxexsearch.com/submit-resume/'
	web_driver.get('https://lenoxexsearch.com/submit-resume/')

	time.sleep(2)

	your_name = mylist[0]
	name = web_driver.find_element_by_xpath('//*[@id="candidate_name"]')
	name.send_keys(your_name)

	your_email = mylist[5]
	email = web_driver.find_element_by_xpath('//*[@id="candidate_email"]')
	email.send_keys(your_email)

	your_city = mylist[2]
	city = web_driver.find_element_by_xpath('//*[@id="candidate_location"]')
	city.send_keys(your_city)

	your_num = mylist[3]
	num = web_driver.find_element_by_xpath('// *[ @ id = "candidate_phone"]')
	num.send_keys(your_num)

	resume_file = web_driver.find_element_by_xpath('//*[@id="resume_file"]')
	resume_file.send_keys(loc)

	#It will submit so dont uncomment
	# submit = web_driver.find_element_by_xpath('//*[@id="submit-resume-form"]/p/input[5]')
	# submit.click()