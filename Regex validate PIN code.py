def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return("false")
    digit_count = 0
    for i in pin:
        if str(i).isdigit() == True:
            digit_count += 1
    if digit_count == len(pin):
        return("true")
    else:
        return("false")
