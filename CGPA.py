
def cgpaCalculator():
	TotalScore= 0

	obtainedGrade = 0

	numberOfCourses = int(input("Please Enter the number of Courses you Offered: "))
	
	for x in range(numberOfCourses):
		Course1 = input("Enter The Course code of the  course you took:")
		gradepoint = int(input ("credit of the course: "))
		score = int(input("Please Enter your Score: "))
		
		TotalScore += gradepoint* 5
		if (score >= 90):
			grade = 10
		elif(score < 90 and  score >= 80):
			grade = 9 
		elif(score < 80 and  score >= 70 ):
			grade = 8
		elif(score < 70 and  score >= 60):
			grade = 7
		elif (score < 60 and  score>= 50):
			grade = 6
		else :
			grade = 0 


		obtainedGrade += gradepoint*grade

	Cgpa =float((obtainedGrade / TotalScore) * 5)
	print("THANKS FOR ALL YOUR INPUT YOUR CGPA IS : " + str(Cgpa))


cgpaCalculator()






