colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "beige": "#f5f5dc", "BlanchedAlmond": "#ffebcd",
           "brown": "#a52a2a", "burlywood": "#deb887", "CadetBlue": "#5f9ea0", "chocolate": "#d2691e",
           "coral": "#ff7f50", "firebrick": "#b22222"}

input_colour = input("Please enter a colour: ")
while input_colour != "":
    if input_colour in colours:
        print(input_colour, "is", colours[input_colour])
    else:
        print("Wrong Colour!")
    input_colour = input("Please enter a colour")