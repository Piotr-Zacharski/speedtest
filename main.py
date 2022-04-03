import speedtest

speed = speedtest.Speedtest()

bytes_num = 1000000

downs = round(speed.download()/bytes_num, 2)

uplods = round(speed.upload()/bytes_num, 2)

print(f'Prędkość pobierania: {downs} Mbps')
print(f'Prędkość wysyłania: {uplods} Mbps')