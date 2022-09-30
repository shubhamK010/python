# function doing task instead of returning a value
def banner_text(text):
    screen_width = 120
    if len(text) > screen_width-4:
        print("The lenght of text is greater than limit {}".format(screen_width-4))
    if text == "*":
        print("*"*screen_width)
    else:
        center_text = text.center(screen_width-4)
        print("*{}*".format(center_text))