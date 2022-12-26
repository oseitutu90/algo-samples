# Description: Calculate the BMI and write the data to a CSV file
import csv

def calculate_bmi(filename, name, age, weight, height):
    # Calculate the BMI
    bmi = round(weight / (height**2),2)
    # Write the data to the CSV file
    with open(filename, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, weight, height, bmi])

# Read input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))

# Call the calculate_bmi function with the name of the CSV file and the input data
calculate_bmi('people.csv', name, age, weight, height)

print("Data written to CSV file")
