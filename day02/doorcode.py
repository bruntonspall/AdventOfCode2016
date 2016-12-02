def calculate_doorcode(inputs, button = 5):
    for n in inputs:
        if n == "U":
            if button > 3: 
                button = button - 3 
        if n == "D":
            if button < 7: 
                button = button + 3
        if n == "L":
            if button % 3 != 1 and button != 1:
                button = button - 1 
        if n == "R":
            if button % 3 != 0:
                button = button + 1
    return button

lookup = {
        "1":"1311",
        "2":"2623",
        "3":"1724",
        "4":"4834",
        "5":"5556",
        "6":"2A57",
        "7":"3B68",
        "8":"4C79",
        "9":"9989",
        "A":"6AAB",
        "B":"7DAC",
        "C":"8CBC",
        "D":"BDDD",
        }

def calculate_rotated_doorcode(inputs, button = "5"):
    for n in inputs:
        if n == "U":
            button = lookup[button][0]
        if n == "D":
            button = lookup[button][1]
        if n == "L":
            button = lookup[button][2]
        if n == "R":
            button = lookup[button][3]
    return button

def code_from_file(f):
    solution = ""
    button = "5"
    for line in open(f).readlines():
        button = calculate_rotated_doorcode(line.strip(), button)
        solution += str(button)
    return solution
