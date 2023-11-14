# Define a dictionary of color names and their hexadecimal codes
COLOR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "bisque": "#ffe4c4",
    "cadetblue": "#5f9ea0",
    "coral": "#ff7f50",
    "darkorchid": "#9932cc",
    "dodgerblue": "#1e90ff",
    "firebrick": "#b22222",
    "green": "#00ff00",  # Basic color: Green
    "blue": "#0000ff",  # Basic color: Blue
    "red": "#ff0000",   # Basic color: Red
    "yellow": "#ffff00",  # Basic color: Yellow
}

# Convert color name keys to lowercase for case-insensitive lookup
COLOR_CODES = {color.lower(): code for color, code in COLOR_CODES.items()}

while True:
    color_name = input("Enter a color name (or blank to quit): ").lower()

    if color_name == "":
        break  # Exit the loop if the user enters a blank line

    color_code = COLOR_CODES.get(color_name, "Color not found")
    print(f"The hexadecimal code for {color_name} is {color_code}")
