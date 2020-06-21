import random as rnd
import re

list1 = list(range(10))
list2 = list(range(10))

for i in range(10):
    list1[i] = rnd.randint(1, 100)

print(list1)

for i in range(10):
    if list1[i] > 50:
        list2[i] = "High"
    else:
        list2[i] = "Low"

print(list2)

listOfNames = ["Liam",	"Emma", "Noah",	"Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia",
"Benjamin", "Charlotte", "Elijah", "Mia", "Lucas", "Amelia", "Mason", "Harper", "Logan", "Evelyn",
"Alexander", "Abigail", "Ethan", "Emily", "Jacob", "Elizabeth", "Michael", "Mila", "Daniel", "Ella",
"Henry", "Avery", "Jackson", "Sofia", "Sebastian", "Camila", "Aiden", "Aria", "Matthew", "Scarlett",
"Samuel", "Victoria", "David", "Madison", "Joseph", "Luna", "Carter", "Grace", "Owen", "Chloe",
"Wyatt", "Penelope", "John", "Layla", "Jack", "Riley", "Luke", "Zoey", "Jayden", "Nora",
"Dylan", "Lily", "Grayson", "Eleanor", "Levi", "Hannah", "Isaac", "Lillian", "Gabriel", "Addison",
"Julian", "Aubrey", "Mateo", "Ellie", "Anthony", "Stella", "Jaxon", "Natalie", "Lincoln", "Zoe",
"Joshua", "Leah", "Christopher", "Hazel", "Andrew", "Violet", "Theodore", "Aurora", "Caleb", "Savannah",
"Ryan", "Audrey", "Asher", "Brooklyn", "Nathan", "Bella", "Thomas", "Claire", "Leo", "Skylar"]

listOfNames1 = list()
listOfNames2 = list()

for i in listOfNames:
    if re.match("[a-mA-M]", i):
        listOfNames1.append(i)
    else:
        listOfNames2.append(i)

print(listOfNames1)
print(listOfNames2)