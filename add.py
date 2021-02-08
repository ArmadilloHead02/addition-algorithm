import time
from datetime import datetime

print("Enter 2 numbers to be added")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

start = int(datetime.now().strftime("%S"))

time.sleep(int(num1))
time.sleep(int(num2))

print(num1 + " + " + num2 + " is...")
print(int(datetime.now().strftime("%S")) - start)