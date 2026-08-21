from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        user_input = float(input("Enter a number: "))
        
        sq = square(user_input)
        even_check = is_even(user_input)
        fahrenheit = celsius_to_fahrenheit(user_input)
        
        print(f"\nResults for {user_input}:")
        print(f"Square: {sq}")
        print(f"Even? {'Yes - it is even' if even_check else 'No - it is odd'}")
        print(f"{user_input}°C is {fahrenheit}°F")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    try:
        name = input("Enter your name: ")
        print(greet(name))
        
        user_input = float(input("Enter a number: "))
        
        sq = square(user_input)
        even_check = is_even(user_input)
        fahrenheit = celsius_to_fahrenheit(user_input)
        
        print(f"\nResults for {user_input}:")
        print(f"Square: {sq}")
        print(f"Even? {'Yes - it is even' if even_check else 'No - it is odd'}")
        print(f"{user_input}°C is {fahrenheit}°F")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()