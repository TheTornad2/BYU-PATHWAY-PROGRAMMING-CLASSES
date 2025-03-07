# This program analyzes life expectancy data and provides insights based on user input.
# Added features: user input for country analysis and identifying trends in the data.


def load_data(filename):
    """Load the dataset and return the data as a list of lines."""
    with open(filename, "r") as file:
        data = file.readlines()  # Read all lines
    return data


def analyze_life_expectancy(data):
    """Analyze life expectancy data to find min and max values."""
    min_life = float("inf")
    max_life = float("-inf")
    min_country = ""
    max_country = ""
    total_life = 0
    count = 0

    for line in data:
        parts = line.strip().split(",")
        if len(parts) < 4:
            continue  # Skip if there aren't enough data points
        try:
            country = parts[0]
            year = int(parts[2])  # Convert to integer
            life_expectancy = float(parts[3])  # Convert to float
        except ValueError:
            continue  # Skip this line if conversion fails

        # Update min and max life expectancy
        if life_expectancy < min_life:
            min_life = life_expectancy
            min_country = country

        if life_expectancy > max_life:
            max_life = life_expectancy
            max_country = country

        total_life += life_expectancy
        count += 1

    average_life = total_life / count if count else 0
    return (min_life, min_country, max_life, max_country, average_life)


def analyze_year(data, year):
    """Find average life expectancy for a specific year and min/max countries."""
    total_life = 0
    count = 0
    min_life = float("inf")
    max_life = float("-inf")
    min_country = ""
    max_country = ""

    for line in data:
        parts = line.strip().split(",")
        if len(parts) < 4:
            continue  # Skip if there aren't enough data points
        try:
            country = parts[0]
            current_year = int(parts[2])
            life_expectancy = float(parts[3])
        except ValueError:
            continue  # Skip this line if conversion fails

        if current_year == year:
            total_life += life_expectancy
            count += 1

            # Update min and max life expectancy for that year
            if life_expectancy < min_life:
                min_life = life_expectancy
                min_country = country
            if life_expectancy > max_life:
                max_life = life_expectancy
                max_country = country

    average_life = total_life / count if count else 0
    return (average_life, min_country, min_life, max_country, max_life)


def main():
    filename = "life-expectancy.csv"
    data = load_data(filename)

    # Overall analysis
    min_life, min_country, max_life, max_country, overall_average = (
        analyze_life_expectancy(data)
    )

    print(f"The overall min life expectancy is: {min_life} from {min_country}")
    print(f"The overall max life expectancy is: {max_life} from {max_country}")
    print(f"The overall average life expectancy is: {overall_average:.2f}")

    # Year-specific analysis
    year_input = int(input("Enter the year of interest: "))
    average_life, min_country, min_life, max_country, max_life = analyze_year(
        data, year_input
    )

    print(f"\nFor the year {year_input}:")
    print(f"The average life expectancy across all countries was {average_life:.2f}")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}")
    print(f"The min life expectancy was in {min_country} with {min_life:.3f}")


if __name__ == "__main__":
    main()
