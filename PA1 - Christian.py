
# The code will provide the recommended daily calorie, protein, and sugar intake
# The program will take gender and body weight in account
# Disclaimer: The code will have the most accuracy if the user is in high school or college
print("Recommendations for Maintaining Body Weight")

# The User will indicate their gender by typing "male" or "female"
gender = input("What is your gender?")

# The user will now input his/her weight to determine the recommended intake of calories, protein, and sugar
weight = input("How much do you weigh?")
weight = int(weight)

# The program will enter the weight into an equation for caloric and sugar intake because it's gender dependent
if gender == "male":
    calories = 5.4 * weight + 1201
    calories = int(calories)
    sugar = 37.5

if gender == "female":
    calories = 5.6 * weight + 1001
    sugar = 25

# According to the calculator being used, recommended protein intake is gender independent
protein = 0.4 * weight - 4
protein = int(protein)

print("The recommended calorie intake is", calories, "calories")
print("The recommended protein intake is", protein, "grams")
print("The recommended sugar intake is", sugar, "grams")
