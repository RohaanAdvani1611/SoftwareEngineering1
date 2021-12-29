# SE Assignment 4: ROHAAN ADVANI - 111903151

# Create a student information form, store student information
# in file and also display the information from the file.


def student_name():
	name = input("Enter Student Name : ")
	fp.write("Name: " + name + "\n")
	return


def student_dob():
	dob = input("Enter Student DOB(dd/mm/yy) : ")
	fp.write("DOB: " + dob + "\n")
	return


def student_rollno():
	rollno = input("Enter Student Roll No : ")
	fp.write("Roll No: " + rollno + "\n")
	return


def student_contact():
	contact = input("Enter Student Contact no : ")
	fp.write("Contact: " + contact + "\n")
	return


def student_email():
	email = input("Enter Student email : ")
	fp.write("Email ID: " + email + "\n")
	return


def student_address():
	address = input("Enter Student Address : ")
	fp.write("Address: " + address +"\n")
	return


def student_branch():
	branch = input("Enter Student branch : ")
	fp.write("Branch: " + branch + "\n")
	return


fp = open("student_list.txt", "w")
while True:
	print("\nEnter Student Info:-")
	student_name()
	student_dob()
	student_rollno()
	student_contact()
	student_email()
	student_address()
	student_branch()

	new_student = input("\nAdd New Student?(yes/no):")
	if new_student.upper() == "YES" or new_student.upper() == "Y":
		fp.write("\n")
		continue
	else:
		display = input("\nDisplay Student List?(yes/no):")
		if display.upper() == "YES" or display.upper() == "Y":
			f = open("student_list.txt", "r")
			print("\n")
			print(f.read())
			break
	fp = open("student_list.txt", "a")
fp.close()