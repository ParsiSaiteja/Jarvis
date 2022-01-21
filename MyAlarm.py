import datetime
import winsound # pip install PlaySound

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    altime = altime[11:-3]
    print(altime)

    Hour = altime[:2]
    Hour = int(Hour)
    Minute = altime[3:5]
    Minute = int(Minute)

    print(f"Done, alarm is set for {Timing}")

    while True:
        if Hour == datetime.datetime.now().hour:
            if Minute == datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('xyz',winsound.SND_LOOP)

            elif Minute<datetime.datetime.now().minute:
                break

if __name__ == '__main__':
    alarm('2:00 PM')