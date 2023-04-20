colors = ["red", "green", "yellow"]

print(colors)
print(colors[1])
print(type(colors))

colors.append("black")
print(colors)

# remove green
colors.remove("green")

# insert pink at index 0
colors.insert(0, "pink")

print(colors)

colors.sort()
print(colors)

colors.reverse()
print(colors)

# tuple - immutable
signal = ("red", "green", "yellow")

print(signal)
print(signal[0])
print(type(signal))

student = {
    "id": 101,
    "name": "John",
    "mark": [45, 75, 89],
    "percentage": 65.5,
    "group": "red"
}
print(student)
print(type(student))

print(student["name"])
print(student["percentage"])
print(student["mark"])
print(student["mark"][0])

mobile_app = {
    "platformName": "android",
    "platformVersion": 11,
    "browserName": "chrome"
}

print(mobile_app)
print(mobile_app["platformName"])

data = [["admin", "pass"], ["john", "john123"]]

print(data[0][0])