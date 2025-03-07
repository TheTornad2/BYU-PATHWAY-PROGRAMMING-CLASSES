def calculate_wind_chill(temperature, wind_speed):
    """Calculate wind chill based on temperature and wind speed."""
    wind_chill = (
        35.74
        + (0.6215 * temperature)
        - (35.75 * (wind_speed**0.16))
        + (0.4275 * temperature * (wind_speed**0.16))
    )
    return wind_chill


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit


def main():
    # Get temperature from user
    temp_input = float(input("What is the temperature? "))
    scale = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    # Convert Celsius to Fahrenheit if needed
    if scale == "C":
        temperature = celsius_to_fahrenheit(temp_input)
    else:
        temperature = temp_input

    # Display wind chill for wind speeds from 5 to 60 mph
    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(
            f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F"
        )


if __name__ == "__main__":
    main()
