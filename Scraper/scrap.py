from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
from selenium.webdriver.common.by import By
import Scraper.scrap_assist as scrap_assist

def scroll(driver):
	initialScroll = 0
	finalScroll = 1000
	start = time.time()

	while True:
		driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
		# this command scrolls the window starting from
		# the pixel value stored in the initialScroll
		# variable to the pixel value stored at the
		# finalScroll variable
		initialScroll = finalScroll
		finalScroll += 1000

		# we will stop the script for 3 seconds so that
		# the data can load
		time.sleep(3)
		# You can change it as per your needs and internet speed

		end = time.time()

		# We will scroll for 20 seconds.
		# You can change it as per your needs and internet speed
		if round(end - start) > 20:
			break

def login_into_linkedIn(driver, username, password):

	# Opening linkedIn's login page
	driver.get("https://linkedin.com/uas/login")

	# waiting for the page to load
	time.sleep(5)

	Username = driver.find_element(By.ID, "username")
	# Enter Your Username

	Username.send_keys(username)

	pword = driver.find_element(By.ID, "password")
	# Enter Your Password
	pword.send_keys(password)

	# Clicking on the log in button
	driver.find_element(By.XPATH, "//button[@type='submit']").click()

def Enter_into_link(link,driver):

	driver.get(link)
	scroll(driver)
	time.sleep(10)
	src_for_profile = driver.page_source
	soup = BeautifulSoup(src_for_profile, 'lxml')

	return soup

def extract_URL_link(driver, profile_url):
	contact_url = profile_url + "overlay/contact-info/"

	driver.get(contact_url)
	scroll(driver)
	time.sleep(8)

	src = driver.page_source

	# Now using beautiful soup
	soup = BeautifulSoup(src, 'lxml')
	Link = soup.find('div', {'class': 'pv-contact-info__ci-container t-14'})

	if Link:
		Profile_link_loc = Link.find("a")
		if Profile_link_loc:
			Profile_link = Profile_link_loc.get_text().strip()
		else:
			Profile_link = "None"
	else:
		Profile_link = "None"

	return Profile_link

def extract_name(soup):
	intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

	# Extracting the Name
	name_loc = intro.find("h1")
	name = name_loc.get_text().strip()

	return name

def extract_roles(soup):
	intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
	Roles_loc = intro.find("div", {'class': 'text-body-medium'})

	Roles = Roles_loc.get_text().strip()

	return Roles

def extract_location(soup):
	intro = soup.find('div', {'class': 'pb2 pv-text-details__left-panel'})

	location = intro.find("span", {'class': 'text-body-small'}).get_text().strip()

	return location

def extract_phone_number(soup):
	Phone_Number = soup.find('span', {'class': 't-14 t-black t-normal'})

	if Phone_Number:
		Number = Phone_Number.get_text().strip()
	else:
		Number = "None"

	return Number

def extract_Address(soup):
	Address_sec = soup.find('section', {'class': 'pv-contact-info__contact-type ci-address'})

	if Address_sec:
		Address_loc_0 = Address_sec.find('div', {'class': 'pv-contact-info__ci-container t-14'})
		if Address_loc_0:
			Address_loc_1 = Address_loc_0.find("a")
			if Address_loc_1:
				Address = Address_loc_1.get_text().strip()
			else:
				Address = "None"
		else:
			Address = "None"
	else:
		Address = "None"

	return Address

def extract_email(soup):
	Email_sec = soup.find('section', {'class': 'pv-contact-info__contact-type ci-email'})

	if Email_sec:
		Email_loc_0 = Email_sec.find('div', {'class': 'pv-contact-info__ci-container t-14'})
		if Email_loc_0:
			Email_loc_1 = Email_loc_0.find("a")
			if Email_loc_1:
				Email = Email_loc_1.get_text().strip()
			else:
				Email = "None"
		else:
			Email = "None"
	else:
		Email = "None"

	return Email

def begin(username, password):

	str1 = os.getcwd()
	str2 = "chromedriver"
	loc = str1 + "/" + str2

	firefox_path = os.path.dirname(__file__) + "/../drivers/geckodriver"
	chrome_path = os.path.dirname(__file__) + "/drivers/chromedriver"


	# Creating a webdriver instance
	#driver = webdriver.Chrome(loc)
	driver = webdriver.Firefox(executable_path=firefox_path)

	# Now we login into linkedIn
	login_into_linkedIn(driver, username, password)

	driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/a/div[2]').click()

	time.sleep(8)

	profile_url = driver.current_url #"https://www.linkedin.com/in/ca-sahil-jindal-448149164/"


	soup_for_profile = Enter_into_link(profile_url, driver)

	NAME = extract_name(soup_for_profile)
	ROLES = extract_roles(soup_for_profile)
	LOCATION = extract_location(soup_for_profile)

	contact_url = profile_url + "overlay/contact-info/"
	soup_for_contact_info = Enter_into_link(contact_url, driver)

	PHONE_NUMBER = extract_phone_number(soup_for_contact_info)
	ADDRESS = extract_Address(soup_for_contact_info)
	EMAIL = extract_email(soup_for_contact_info)

	print("Name: ", NAME)
	print("Roles: ", ROLES)
	print("Location: ", LOCATION)
	print("Phone Number: ", PHONE_NUMBER)
	print("Address: ", ADDRESS)
	print("Email: ", EMAIL)

	List = scrap_assist.get_Major(soup_for_profile, driver, profile_url)

	EXPERIENCES = List[0]
	EDUCATION = List[1]
	PROJECTS = List[2]
	SKILLS = List[3]

	print("Experiences: ")
	for i in range(len(EXPERIENCES)):
		print(EXPERIENCES[i])

	print("Education: ")
	for i in range(len(EDUCATION)):
		print(EDUCATION[i])

	print("Projects: ")
	for i in range(len(PROJECTS)):
		print(PROJECTS[i])

	print("Skills: ")
	for i in range(len(SKILLS)):
		print(SKILLS[i])

	FINAL_LIST = []
	FINAL_LIST.append(NAME)				# 0
	FINAL_LIST.append(ROLES)			# 1
	FINAL_LIST.append(LOCATION)			# 2
	FINAL_LIST.append(PHONE_NUMBER)		# 3
	FINAL_LIST.append(ADDRESS)			# 4
	FINAL_LIST.append(EMAIL)			# 5
	FINAL_LIST.append(EXPERIENCES)		# 6
	FINAL_LIST.append(EDUCATION)		# 7
	FINAL_LIST.append(PROJECTS)			# 8
	FINAL_LIST.append(SKILLS)			# 9
	FINAL_LIST.append(profile_url)		# 10

	driver.close()
	driver.quit()
	return FINAL_LIST