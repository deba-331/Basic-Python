#Alarm clock
from datetime import datetime
alarm_time= input('Alarm time in the format HH:MM:SS AM/PM \n')
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_second=alarm_time[6:8]
alarm_AM_PM=alarm_time[9:11]
print('Setting an alarm')
while True:
    time=datetime.now()
    current_hour=time.strftime("%I")
    current_minute=time.strftime("%M")
    current_second=time.strftime("%S")
    current_AM_PM=time.strftime("%p")
    if current_hour==alarm_hour:
            if current_minute==alarm_minute:
                    if current_second==alarm_second:
                            if current_AM_PM==alarm_AM_PM:
                                print('it is time to Wake up')
                                break
    


