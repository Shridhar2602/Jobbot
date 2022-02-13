from selenium import webdriver
from bs4 import BeautifulSoup
import time

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


def Enter_into_link(link, driver):
	driver.get(link)
	scroll(driver)
	time.sleep(10)
	src = driver.page_source
	soup = BeautifulSoup(src, 'lxml')

	return soup

def extract_experience(Common, driver, profile_url):

	Experiences = []
	for i in range(len(Common)):
		if (Common[i].find("div", {"id": "experience"}) and Common[i].find("div", {"class": "pv-profile-card-anchor"})):

			is_Futher = Common[i].find("div", {"class": "pvs-list__footer-wrapper"})

			if (is_Futher):
				Experience_link = profile_url + "details/experience/"

				soup_for_experience = Enter_into_link(Experience_link, driver)

				Experience_loc = soup_for_experience.find("ul", {"class": "pvs-list"})
				Experience_loc_0 = Experience_loc.find_all("li", {"class": "pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})

				for j in range(len(Experience_loc_0)):
					Experiences.append([])
					Experience_loc_1 = Experience_loc_0[j].find_all("span", {"aria-hidden": "true"})

					for k in range(len(Experience_loc_1)):
						Experiences[j].append(Experience_loc_1[k].get_text().strip())

				print("Experiences:", Experiences)

			else:
				Experience_loc = Common[i].find("ul", {"class": "pvs-list ph5 display-flex flex-row flex-wrap"})
				Experience_loc_0 = Experience_loc.find_all("li", {"class": "artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"})

				for j in range(len(Experience_loc_0)):
					Experiences.append([])
					Experience_loc_1 = Experience_loc_0[j].find_all("span", {"aria-hidden": "true"})

					for k in range(len(Experience_loc_1)):
						Experiences[j].append(Experience_loc_1[k].get_text().strip())

				print("Experiences:", Experiences)

	return Experiences

def extract_Education(Common, driver, profile_url):

	Qualifications = []

	for i in range(len(Common)):
		if (Common[i].find("div", {"id": "education"}) and Common[i].find("div", {"class": "pv-profile-card-anchor"})):
			is_Futher = Common[i].find("div", {"class": "pvs-list__footer-wrapper"})

			if(is_Futher):
				Education_link = profile_url + "details/education/"
				soup_for_education = Enter_into_link(Education_link, driver)

				Education_loc = soup_for_education.find("ul", {"class": "pvs-list"})
				Education_loc_0 = Education_loc.find_all("li", {"class": "pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})

				for j in range(len(Education_loc_0)):
					Qualifications.append([])
					Education_loc_1 = Education_loc_0[j].find_all("span", {"aria-hidden": "true"})

					for k in range(len(Education_loc_1)):
						Qualifications[j].append(Education_loc_1[k].get_text().strip())

				print("Qualifications:", Qualifications)

			else:
				Education_loc = Common[i].find("ul", {"class": "pvs-list ph5 display-flex flex-row flex-wrap"})
				Education_loc_0 = Education_loc.find_all("li", {"class": "artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"})

				for j in range(len(Education_loc_0)):
					Qualifications.append([])
					Education_loc_1 = Education_loc_0[j].find_all("span", {"aria-hidden": "true"})

					for k in range(len(Education_loc_1)):
						Qualifications[j].append(Education_loc_1[k].get_text().strip())

				print("Qualifications:", Qualifications)

	return Qualifications

def extract_Skills(Common, driver, profile_url):

	Skills =[]
	for i in range(len(Common)):
		if (Common[i].find("div", {"id": "skills"}) and Common[i].find("div", {"class": "pv-profile-card-anchor"})):
			is_Futher = Common[i].find("div", {"class": "pvs-list__footer-wrapper"})

			if (is_Futher):
				Skill_link = profile_url + "details/skills/"

				soup_for_skills = Enter_into_link(Skill_link, driver)

				Skills_list_loc = soup_for_skills.find("ul", {"class": "pvs-list"})
				Skills_list_loc_1 = Skills_list_loc.find_all("span", {"aria-hidden": "true"})

				for j in range(len(Skills_list_loc_1)):
					Skills.append(Skills_list_loc_1[j].get_text().strip())

				print("List of Skills:", Skills)

			else:
				Skills_list_loc = Common[i].find("ul", {"class": "pvs-list ph5"})
				Skills_list_loc_1 = Skills_list_loc.find_all("span", {"aria-hidden": "true"})

				for j in range(len(Skills_list_loc_1)):
					if(Skills_list_loc_1[j].get_text().strip() != "Passed LinkedIn Skill Assessment"):
						Skills.append(Skills_list_loc_1[j].get_text().strip())

				print("List of Skills:", Skills)

	return Skills

def extract_Projects(Common, driver, profile_url):

	Projects = []
	for i in range(len(Common)):
		if (Common[i].find("div", {"id": "projects"}) and Common[i].find("div", {"class": "pv-profile-card-anchor"})):
			is_Futher = Common[i].find("div", {"class": "pvs-list__footer-wrapper"})

			if (is_Futher):
				Project_link = profile_url + "details/projects/"

				soup_for_projects = Enter_into_link(Project_link, driver)

				Projects_loc = soup_for_projects.find("ul", {"class": "pvs-list"})
				Projects_list_loc_1 = Projects_loc.find_all("li", {"class": "pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})

				for j in range(len(Projects_list_loc_1)):
					Projects_list_loc_2 = Projects_list_loc_1[j].find_all("span", {"aria-hidden": "true"})

					Projects.append([])
					for k in range(len(Projects_list_loc_2)):
						Projects[j].append(Projects_list_loc_2[k].get_text().strip())

				print(Projects)
			else:
				Projects_loc = Common[i].find("ul", {"class": "pvs-list ph5 display-flex flex-row flex-wrap"})
				Projects_list_loc_1 = Projects_loc.find_all("li", {"class": "artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"})

				for j in range(len(Projects_list_loc_1)):
					Projects_list_loc_2 = Projects_list_loc_1[j].find_all("span", {"aria-hidden": "true"})

					Projects.append([])
					for k in range(len(Projects_list_loc_2)):
						Projects[j].append(Projects_list_loc_2[k].get_text().strip())

				print(Projects)

	return Projects

def get_Major(soup,driver,profile_url):

	Common = soup.find_all("section", {"class": "artdeco-card ember-view break-words pb3 mt4"})

	EXPERIENCES = extract_experience(Common, driver, profile_url)
	EDUCATION = extract_Education(Common, driver, profile_url)
	PROJECTS = extract_Projects(Common, driver, profile_url)
	SKILLS = extract_Skills(Common, driver, profile_url)

	lst = []
	lst.append(EXPERIENCES)
	lst.append(EDUCATION)
	lst.append(PROJECTS)
	lst.append(SKILLS)

	return lst
