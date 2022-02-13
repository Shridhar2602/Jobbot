import matplotlib.pyplot as plt
import Scraper.scrap as scrap

def write_roles(Y, Roles):

	if (len(Roles) != 0):
		count = 0
		y = Y

		desc = ""
		for j in range(len(Roles)):
			desc += Roles[j]
			count += 1
			if ((count == 60) or (j == len(Roles) - 1)):
				count = 0
				plt.annotate(desc, (.02, y), weight='regular', fontsize=10)
				y = y - 0.02
				desc = ""

		return(y - 0.02)

	else:
		return Y

def write_Projects(Y, Projects):

	if (len(Projects) != 0):

		y = Y
		plt.annotate("PROJECTS", (.02, y), weight='bold', fontsize=10, color='#58C1B2')
		Y = y - 0.027

		count = 0
		x1 = 0.02
		y1 = Y

		if (len(Projects) <= 3):
			number_of_projects = len(Projects)
		else:
			number_of_projects = 3

		for i in range(number_of_projects):
			title = Projects[i][0]

			plt.annotate(title, (x1, y1), weight='bold', fontsize=10)
			y1 = y1 - 0.02

			if (len(Projects[i]) > 1):
				plt.annotate(Projects[i][1], (x1, y1), weight='regular', fontsize=9, alpha=.6)
				y1 = y1 - 0.02


			if (len(Projects[i]) > 3):
				desc = "- "
				for j in range(len(Projects[i][3])):
					desc += Projects[i][3][j]
					count += 1
					if (((count > 60) and Projects[i][3][j] == " ") or (j == len(Projects[i][3]) - 1) or Projects[i][3][j] == "."):
						count = 0
						plt.annotate(desc, (.02, y1), weight='regular', fontsize=10)
						y1 = y1 - 0.02

						if (Projects[i][3][j] == "."):
							y1 = y1 - 0.02
							break

						desc = ""

		return y1

	else:
		return Y

def write_Experience(Y_to_be_carried, Experiences):

	if (len(Experiences) != 0):

		y = Y_to_be_carried
		plt.annotate("EXPERIENCE", (.02, y), weight='bold', fontsize=10, color='#58C1B2')
		Y_to_be_carried = y - 0.027

		x1 = 0.02
		y1 = Y_to_be_carried

		if (len(Experiences) <= 3):
			number_of_experiences = len(Experiences)
		else:
			number_of_experiences = 3

		for i in range(number_of_experiences):
			title = ""
			title = Experiences[i][0] + " -- " + Experiences[i][1]
			plt.annotate(title, (x1, y1), weight='bold', fontsize=10)
			y1 = y1 - 0.02

			plt.annotate(Experiences[i][2], (x1, y1), weight='regular', fontsize=9, alpha=.6)
			y1 = y1 - 0.02

			desc = "- "
			count = 0

			if(len(Experiences[i])>4):
				for j in range(len(Experiences[i][4])):
					desc += Experiences[i][4][j]
					count += 1
					if (((count > 60) and Experiences[i][4][j] == " ") or (j == len(Experiences[i][4]) - 1) or
							Experiences[i][4][j] == "."):
						count = 0
						plt.annotate(desc, (x1, y1), weight='regular', fontsize=9)
						y1 = y1 - 0.02
						desc = ""

						if (Experiences[i][4][j] == "."):
							y1 = y1 - 0.02
							break

		return y1

	else:
		return Y_to_be_carried

def write_Education(Y_to_be_carried, Education):

	if (len(Education) != 0):

		y = Y_to_be_carried
		plt.annotate("EDUCATION", (.02, y), weight='bold', fontsize=10, color='#58C1B2')
		Y_to_be_carried = y - 0.027

		x1 = 0.02
		y1 = Y_to_be_carried

		if (len(Education) <= 3):
			number_of_qualifications = len(Education)
		else:
			number_of_qualifications = 3

		for i in range(number_of_qualifications):
			university = Education[i][0]
			qualification = Education[i][1]

			plt.annotate(university, (x1, y1), weight='bold', fontsize=10)
			y1 = y1 - 0.02

			plt.annotate(qualification, (x1, y1), weight='regular', fontsize=10)
			y1 = y1 - 0.02

			if (len(Education[i]) > 2):
				duration = Education[i][2]
				plt.annotate(duration, (x1, y1), weight='regular', fontsize=9, alpha=.6)
				y1 = y1 - 0.02

			y1 = y1 - 0.02

		return y1

	else:
		return Y_to_be_carried


def write_Skills(Skills):
	x1 = .663
	y1 = 0.66

	if(len(Skills) != 0):
		for i in range(len(Skills)):
			if (Skills[i] != 'Passed LinkedIn Skill Assessment'):
				Skill_split = Skills[i].split(" ")

				if(Skill_split[0] != "Endorsed" and Skill_split[0] != '·'):
					plt.annotate(Skills[i], (x1, y1), weight='regular', fontsize=11, color='#ffffff')
					y1 = y1 - 0.025

		plt.annotate("SKILLS", (.663, .70), weight='bold', fontsize=15, color='#ffffff')


def write_Contact_Details(Location, Contact, Email, Profile_link):

	Link_split = Profile_link.split("/")
	Profile_link_1 = "www.linkedin.com/in/" + Link_split[4] + "/"

	plt.annotate("Contact Details", (.663, .973), weight='bold', fontsize=15, color='#ffffff')

	plt.annotate(Profile_link_1, (.663, .94), weight='regular', fontsize=11, color='#ffffff')

	Phone_number_string = "Phone Number: "
	plt.annotate(Phone_number_string, (.663, .91), weight='regular', fontsize=10, color='#ffffff')
	plt.annotate(Contact, (.663, .89), weight='regular', fontsize=10, color='#ffffff')

	Location_string = "Location: "
	plt.annotate(Location_string, (.663, .85), weight='regular', fontsize=10, color='#ffffff')
	plt.annotate(Location, (.663, .83), weight='regular', fontsize=10, color='#ffffff')

	Email_string = "Email: "
	plt.annotate(Email_string, (.663, .79), weight='regular', fontsize=10, color='#ffffff')
	plt.annotate(Email, (.663, .77), weight='regular', fontsize=10, color='#ffffff')


def Build_Start(username,password):

	plt.rcParams['font.family'] = 'sans-serif'
	plt.rcParams['font.sans-serif'] = 'STIXGeneral'
	fig, ax = plt.subplots(figsize=(8.9, 11))
	# Decorative Lines
	ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
	plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=330)
	plt.axhline(y=.74, xmin=0, xmax=1, color='#ffffff', linewidth=3)
	# set background color
	ax.set_facecolor('white')
	# remove axes
	plt.axis('off')

	LIST_OF_ENTITIES = scrap.begin(username,password)


	Y_to_be_carried = 0.9400

	y = Y_to_be_carried
	Name = LIST_OF_ENTITIES[0]
	plt.annotate(Name, (.02, y), weight='bold', fontsize=20)
	y = y - 0.03
	Y_to_be_carried = y


	Roles = LIST_OF_ENTITIES[1]
	Y_to_be_carried = write_roles(Y_to_be_carried, Roles)


	Projects = LIST_OF_ENTITIES[8]
	Y_to_be_carried = write_Projects(Y_to_be_carried, Projects)


	Experiences = LIST_OF_ENTITIES[6]
	Y_to_be_carried = write_Experience(Y_to_be_carried, Experiences)


	Education = LIST_OF_ENTITIES[7]
	Y_to_be_carried = write_Education(Y_to_be_carried, Education)

	Skills = LIST_OF_ENTITIES[9]
	write_Skills(Skills)


	Profile_link = LIST_OF_ENTITIES[10]
	Location = LIST_OF_ENTITIES[2]
	Contact = LIST_OF_ENTITIES[3]
	Email = LIST_OF_ENTITIES[5]
	write_Contact_Details(Location, Contact, Email, Profile_link)


	# plt.savefig('resume.png', dpi=300, bbox_inches='tight')
	#plt.show()
	plt.savefig('resume.pdf')
	return LIST_OF_ENTITIES
