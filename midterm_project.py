# BMI Calculator and Weight Recommendation Program

# Constants for BMI categories
UNDERWEIGHT = 18.5
NORMAL_WEIGHT = 24.9
OVERWEIGHT = 29.9

# Welcome message
print("Hey! Welcome to the BMI Calculator and Weight Recommendation Program!")

# Get user input for height, weight, and age
height_meters = float(input("Enter your height in meters: "))
weight_kg = float(input("Enter your weight in kilograms: "))
age = int(input("Enter your age: "))

# Calculate BMI
bmi = weight_kg / (height_meters ** 2)

# Determine BMI category and provide recommendations
print("\nBMI Result:")
print(f"Your BMI is: {bmi:.2f}")

if bmi < UNDERWEIGHT:
    print("You are underweight. Consider gaining weight for a healthier BMI.")
    weight_to_gain = NORMAL_WEIGHT * (height_meters ** 2) - weight_kg
    print(f"To reach a normal weight, you need to gain approximately {weight_to_gain:.2f} kilograms.")
elif UNDERWEIGHT <= bmi <= NORMAL_WEIGHT:
    print("You have a normal weight. Keep maintaining a healthy lifestyle!")
elif NORMAL_WEIGHT < bmi <= OVERWEIGHT:
    print("You are overweight. Consider losing weight for a healthier BMI.")
    weight_to_lose = weight_kg - NORMAL_WEIGHT * (height_meters ** 2)
    print(f"To reach a normal weight, you need to lose approximately {weight_to_lose:.2f} kilograms.")
else:
    print("You are in the obese category. Consult with a healthcare professional for personalized advice.")

# Thank you message
print("\nThank you for using the BMI Calculator and Weight Recommendation Program!")



