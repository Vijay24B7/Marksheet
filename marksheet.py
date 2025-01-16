
import os
import re
import math

schoolinfo = ["School Name", "Address"]
school = {}

# Function to get School Information
def get_school_info(a):
	x = input(f"Enter {a}: ")
	y = re.findall("\w[ ]{2,}\w", x)
	try:
		if(len(y) == 0 and len(x) < 50):
			return x
		raise Exception
			
	except:
		print(f"The {a} cannot have more than 50 letters and more than one space")
		return get_school_info(a)



for i in schoolinfo:
	school[i] = get_school_info(i).capitalize()



# Getting student information 
st_info = ["Name", "Father's Name", "Mother's Name"]
st = {}


def validation_roll():
	'''Function to check if a roll number is valid or not'''
	x = input("Enter your roll no: ")
	y = re.findall("[^0-9]", x)
	try:
		if (len(y) == 0):
			return x
		raise ValueError("Enter valid roll number( Roll number should not contain alphabets, or special characters)")
	except:
		print("Enter valid number(Roll number should not contain alphabets or special characters)")
		return validation_roll()


def validation_name(str):
	#Function to validate names
	x = input(f"Enter your {str}: ")
	y = len(x)
	try:
		if y <= 30:
			z = re.findall("[^a-zA-Z\s]|\w[ ]{2,}\w", x)
			if len(z) == 0:
				return x
			else:
				raise Exception("The name should not be more than 30 characters and should not contain special symbols")
		elif y > 30:
			raise Exception(f"The length of {str} cannot exceed 30 letters")
	except:
			print("Enter valid name. (The name cannot be more than 30 characters and should not contain numbers or special character)")
			return validation_name(str)

st["rollno"] = validation_roll()

for s in st_info:
	st[s] = validation_name(s)

#print(stinfo)



avg = 0
marks = {}

#Function to validate the marks
def validate(s):
	try:
		m = float(input(f"Enter marks for {s} :"))
		if(isinstance(m, float) and (m >= 0 and m <= 100)):
			m = math.ceil(m)
			return m
		else:
			raise Exception("Please enter valid number")
	except:
		print("Enter Valid Number (Marks should be positive and should not contain alphabets)")
		m = validate(s)
		return m

grades = {}
subjects = ["Hindi", "English", "Maths", "Social Science", "Science"]
columns = {
	"Subjects": 16, 
	"Max. Marks": 14,
	"Obt. Marks": 14, 
	"Grades": 8, 
	"Result": 8}
mm = 100
#getting marks from user
for s in subjects:
	marks[s] = validate(s)
 

#for k, v in marks.items():
#	print(f"{k} : {v}")
#Function to assign grades for marks
def assign_grades(m):
	if((m > 85) and (m < 100)):
		return "A1"
	elif((m > 74) and (m <= 85)):
		return "A2"
	elif((m > 65) and (m <= 74)):
		return "B2"
	elif((m > 55) and (m <= 64)):
		return "B1"
	elif((m > 45) and (m <= 54)):
		return "C2"
	elif((m > 33) and (m <= 44)):
		return "C1"
	else:
		return "D"

for s in subjects:
	grades[s] = assign_grades(marks[s])

#Function to check if the student is pass or fail
def check_result(m):
	global avg
	total = 0
	for x in m.values():
		total += x
	avg = total/len(marks)
	return "PASS" if avg > 33 else "FAIL"

#function for displaying marks and grades g for grades and s for subjects and c for columns
def marks_info(g, s, c):
	print("Marks".ljust(63, " "), end = "|\n|")
	print("".center(64, "-"), end = "|\n|")
	#s_list = s.keys()	#s_list stores the list of subjects
	for k, v in c.items():
		print(f"{k}".center(v," "), end = "|")
		
	print(end = "\n|")
	for k, v in c.items():
		print("".center(v, "-"), end = "|")
	print(end = "\n| ")
	for k, v in g.items():
		print(f"{k}".ljust(15,' '), end = "| ")
		print(f"{mm}".rjust(12, " "), end = " | ")
		print(f"{marks[k]:03}".rjust(10, " ") if (marks[k] > 33) else f"{marks[k]:03}".rjust(10, " ")+"F", end = "   | " if (marks[k] > 33) else "  | ")
		print(f"{v}".rjust(7, " ") if v != 'D' else f"{v}".rjust(6, " "), end = "|" if v!= "D" else " |")
		if(s.index(k) == (len(g)//2)):
			print(check_result(marks).center(8, " "), end = "|")
		else:
			print("".ljust(8, " "),end = "|") 
		print(end = "\n| ")
	print("\b".ljust(65,"-"), end = "|\n| ")


#result will store if the student is pass or fail
result = check_result(marks) 
result = "PASSED" if (avg > 33) else "FAILED"
print(f"Average = {avg}\tPercentage = {avg}%\nResult = {result}")

'''def eline(s = "line",):
	if s == "text":
		return " |\n| "
	else:
		return " |\n"

def line(pos = "middle", length = 60, c = "notext"):
	if(pos == "upper"):
		print("".center(length, "_"), end = "\n| ")
	elif(pos == "lower"):
		print("|".ljust(length-2, "_"), end = eline())
	else:
		print("|".ljust(length-2, "-"), end = eline(c))
'''
#Function to display school information
def school_info(s):
	global schoolinfo
	print("".center(66, "_"), end = "\n| ")
	print("School Info".ljust(62, " "), end = " |\n|")
	print("".center(64, "-"), end = "|\n| ")
	print(f"{s[schoolinfo[0]]}".center(62, " "), end = " |\n| ")
	print(f"{s[schoolinfo[1]]}".center(62, " "), end= " |\n|")
	print("".center(64, "-"), end = "|\n| ")

#Function to display student information
def student_info(st):
	print("Student Info".ljust(62, " "), end = " |\n|")
	print("".center(64, "-"), end = "|\n| ")
	labels = list(st.keys())
	for i in labels:
		print(f"{i}".ljust(15, " "), f"{st[i]}".ljust(44, " "), sep = "|  ", end = " |\n| " if labels.index(i) != len(labels)-1 else " |\n|")
	print("".center(64, "-"), end = "|\n| ")

# Function to display overall score, a is for average
def overall(a):
	print("Overall Score".ljust(63, " "), end = "|\n|")
	print("".center(64, "-"), end = "|\n| ")
	print("Percentage".ljust(15, " "), end = "| ")
	print(f"{a}%".ljust(12, " "), end = " | ")
	print("Grade".ljust(12," "), end = " | ")
	print(assign_grades(a).ljust(15, " "), end = " |\n|")
	print("".ljust(16, "_"), "".ljust(14, "_"), "".ljust(14, "_"), "".ljust(16, "_"), sep = "|", end = "_|\n")

os.system("clear") 
school_info(school)
student_info(st)
marks_info(grades, subjects, columns)
overall(avg)
