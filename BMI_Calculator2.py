def calculateBMI(height, weight):
    return round(weight / (height**2) * 703)

def interpretBMI(BMI):
    if BMI < 18.5:
        return "underweight"
    if BMI < 25:
        return "normal weight"
    if BMI < 30:
        return "overweight"
    if BMI < 35:
        return "obese"
    return "clinically obese"

#Enter your Height in inches
height = int(input("Enter your height in inches? "))
#Enter your Weight in pounds
weight = int(input("Enter your weight in pounds? "))
#calculate your BMI
BMI = calculateBMI(height, weight)
#results
results = interpretBMI(BMI)
#print the BMI
print(f"Your BMI is {BMI}")
#print the results
print(f"Your BMI indicates you are {results}")


