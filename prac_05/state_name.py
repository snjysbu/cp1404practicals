# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_CODES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(STATE_CODES)

state_code = input("Enter short state: ")
while state_code != "":
    if state_code in STATE_CODES:
        print(state_code, "is", STATE_CODES[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
