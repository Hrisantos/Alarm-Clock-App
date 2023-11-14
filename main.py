from alarm_clock import AlarmClock

alarma = AlarmClock()

setare_alarma = True

while setare_alarma:
    optiune_aleasa = int(input("1 - Set Alarm, 2 - Quit:\t"))
    if optiune_aleasa == 1:
        ora_aleasa = int(input("Seteaza ora (0-23)\t"))
        min_aleasa = int(input("Seteaza min (0-59)\t"))

        alarma.set_alarm(hour=ora_aleasa, minute=min_aleasa)
        alarma.check_alarm()
    else:
        print("Goodbye!")
        setare_alarma = False
else:
    print("Invalid choice. Please select a valid option.")
    optiune_aleasa = int(input("1 - Set Alarm, 2 - Quit"))
