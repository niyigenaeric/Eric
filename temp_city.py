# Input city name
city = input("Enter the city name: ")

# List to store temperature readings
temperature_readings = []

# Input temperature readings for 7 days
for day in range(1, 8):
    temp = float(input(f"Enter the temperature for day {day} in {city}: "))
    temperature_readings.append(temp)

# Print the temperature readings
print(f"\nTemperature readings for the week in {city}:")
for day, temp in enumerate(temperature_readings, start=1):
    print(f"Day {day}: {temp}°C")
