# BMI Calculator - Command Line Version

def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 24.9:
        return "Normal weight"
    elif bmi >= 25 and bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    
    # Get user input
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Classify BMI
    category = classify_bmi(bmi)
    
    # Display the result
    print("\nYour BMI is:", round(bmi, 2))
    print("Category:", category)

if __name__ == "__main__":
    main()
