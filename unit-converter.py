def convert_length():
    print("\nLength Conversion (meters to other units)")
    meters = float(input("Enter length in meters: "))
    print(f"{meters} meters is:")
    print(f" - {meters * 100} centimeters")
    print(f" - {meters * 39.3701} inches")
    print(f" - {meters * 3.28084} feet")
    print(f" - {meters * 1.09361} yards")
    print(f" - {meters / 1000} kilometers")

def convert_temperature():
    print("\nTemperature Conversion (Celsius to other units)")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    print(f"{celsius}°C is:")
    print(f" - {fahrenheit}°F")
    print(f" - {kelvin} K")

def convert_weight():
    print("\nWeight Conversion (kilograms to other units)")
    kg = float(input("Enter weight in kilograms: "))
    print(f"{kg} kilograms is:")
    print(f" - {kg * 1000} grams")
    print(f" - {kg * 2.20462} pounds")
    print(f" - {kg * 35.274} ounces")

def main():
    while True:
        print("\n=== Unit Converter ===")
        print("1. Convert Length")
        print("2. Convert Temperature")
        print("3. Convert Weight")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_temperature()
        elif choice == "3":
            convert_weight()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
