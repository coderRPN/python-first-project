monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    "Dec": "Duplicate",
    1: "One",
    2: "Two"
}

print(monthConversions["Jan"])
print(monthConversions.get("Feb"))
print(monthConversions.get("mar", "Not a valid key"))
print(monthConversions.get("Dec"))
print(monthConversions.get(1))
print(monthConversions[2])
