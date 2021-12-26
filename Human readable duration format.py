def format_duration(seconds):
    if seconds == 0:
        return("now")
    years = int(seconds / 31536000)
    seconds = seconds - years * 31536000
    days = int(seconds /86400)
    seconds = seconds - days*86400
    hours = int(seconds/3600)
    seconds = seconds - hours * 3600
    minutes = int(seconds / 60)
    seconds = seconds - minutes*60
    list1 = []
    if years ==0:
        years_str = ""
    elif years == 1:
        years_str = "year"
        list1.append("1 year")
    else:
        years_str = "years"
        list1.append(str(years) + " years")
    
    if days ==0:
        days_str = ""
    elif days == 1:
        days_str = "day"
        list1.append("1 day")
    else:
        days_str = "days"
        list1.append(str(days) + " days")
    
    if hours ==0:
        hours_str = ""
    elif hours == 1:
        hours_str = "hour"
        list1.append("1 hour")
    else:
        hours_str = "hours"
        list1.append(str(hours) + " hours")
    
    if minutes ==0:
        minutes_str = ""
    elif minutes == 1:
        minutes_str = "minute"
        list1.append("1 minute")
    else:
        minutes_str = "minutes"
        list1.append(str(minutes) + " minutes")
    
    if seconds ==0:
        seconds_str = ""
    elif seconds == 1:
        seconds_str = "second"
        list1.append("1 second")
    else:
        seconds_str = "seconds"
        list1.append(str(seconds) + " seconds")
    if len(list1) == 1:
        return ''.join(list1)
    templist = list1[:-1]
    temp = ", ".join(templist)
    temp = temp + " and " + list1[-1]
    
    list2 = list(temp)
    
    return ''.join(list2)

print(format_duration(7401745))
