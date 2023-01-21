### Question 2
# Create an empty dictionary called dog
dog = dict()
# Adding data to dog dictionary
dog['name'] ='cutie'
dog['color'] ='white'
dog['breed'] ='bulldog'
dog['legs'] = 4
dog['age'] = 6
print("dog dictionary : ", dog)
# creating student dictionary with data
student = {
    "first_name": "ranjith",
    "last_name": "kusthapuram",
    "gender": "male",
    "age": 26,
    "marital status": "single",
    "skills": ["java", "Artificial intelligence"],
    "country": "India",
    "city": "Hyderabad",
    "address": "2-7-274 kothapet"
}
print("student dictionary : ", student)
# length of the student dictionary
len_student = len(student)
# skills of the student from the dictionary
skills = student['skills']
# type of skills
print("type of skills :",type(skills))
# updating student skills
student['skills'].extend(["AI"])
print("updated student skills : ", student["skills"])
# keys of student dictionary
print("keys of student dictionary : ", list(student.keys()))
# values of student dictionary
print("values of student dictionary : ", list(student.values()))
