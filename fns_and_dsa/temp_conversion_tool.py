FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def display_conversion_menu():
    try:
        enter_temperature = float(input("Enter the temperature to convert: "))
        conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if conversion_type == "C":
            result = convert_to_fahrenheit(enter_temperature)
            print(f"{enter_temperature}°C is {result:2f}°F")
        elif conversion_type == "F":
            result = convert_to_celsius(enter_temperature)
            print(f"{enter_temperature}°F is {result:2f}°C")
        else:
            print("Invalid input. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.") 

if __name__ == "__main__":
    display_conversion_menu()