#Task 4: Finally: Add a finally block that thanks the user for using the weather forecast application, 
# ensuring that this message is displayed regardless of whether an exception was caught or not.

def weather_app():
    try:
        temp_f = float(input("Enter the temperature in F: "))
        if temp_f < -50 or temp_f > 150:
            raise ValueError 
        
        else:
            temp_c = (temp_f - 32) * 5 / 9
            print(f"Temperature in Celsius is {temp_c}C")
    except ValueError:
        print("Invalid input. Enter a numerical temperature.")
    finally:
        return "Thanks for using our wheather app!"
    
print(weather_app())