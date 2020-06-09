#Social Situation Analyzer System
#Nathan Wagstaff Assn 7
#CS 1400

#Intro
print("Welcome to the Social Situation Analyzer System")

#first person submission
print("Person One")
name1 = input(format("Enter your name: ", ">25"))
x1, y1 = input(format("Enter your position (x y): ", ">35")).split()
radius1 = input(format("Enter your personal space radius: ", ">42"))

#second person submission
print("Person Two")
name2 = input(format("Enter your name: ", ">25"))
x2, y2 = input(format("Enter your position (x y): ", ">35")).split()
radius2 = input(format("Enter your personal space radius: ", ">42"))

#formulas
import math
x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
equation1 = math.pow(x2 - x1, 2)
equation2 = math.pow(y2 - y1, 2)
distance = math.sqrt(equation1 + equation2)
radius1, radius2 = int(radius1), int(radius2)
radiusAdd = radius1 + radius2

#person test
if distance < radius1 and distance < radius2:
    personTest = f"{name1} and {name2} are in each other's personal space."
elif distance < radius2:
    personTest = f"{name1} is in {name2}'s personal space."
elif distance < radius1:
    personTest = f"{name2} is in {name1}'s personal space."
else:
    personTest = f"Neither {name1} or {name2} is in the other's personal space."



#space test
if distance > radiusAdd:
    spaceTest = f"{name1} and {name2}'s personal spaces do not overlap."
else:
    spaceTest = f"{name1} and {name2}'s personal spaces overlap."

#results
print("Social Situation Analysis Results \n",
      format(f"Person Test: ", ">20"), personTest, "\n",
      format(f"Space Test: ", ">19"), spaceTest)

