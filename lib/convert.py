def convert_to_24_hour(hour, minute, period):
    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    # Format the result as a four-digit string
    result = "{:02d}{:02d}".format(hour, minute)
    return result

# Examples
print(convert_to_24_hour(8, 30, "am"))  # Output: 0830
print(convert_to_24_hour(8, 30, "pm"))  # Output: 2030
print(convert_to_24_hour(12, 0, "pm"))  # Output: 1200
print(convert_to_24_hour(12, 15, "am")) # Output: 0015
