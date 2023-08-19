
def convert_24hr_to_12hr(hour_24) :

    hour_24 = hour_24.split(":")
    hour = int(hour_24[0])
    minutes = int(hour_24[1])
    time_in_12_format = None

    if hour == 0 :
        time_in_12_format = f"{12:02}:{minutes:02} AM"
    elif hour < 12 :
        time_in_12_format = f"{hour:02}:{minutes:02} AM"
    elif hour == 12 :
        time_in_12_format = f"{hour:02}:{minutes:02} PM"
    elif hour > 12 :
        time_in_12_format = f"{(hour - 12):02}:{minutes:02} PM"
    return time_in_12_format


hour_24 = "13:5"
result  = convert_24hr_to_12hr(hour_24)

print(f"time 24hour to 12hour ( {hour_24} ) => {result}")