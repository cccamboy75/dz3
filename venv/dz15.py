#x = 0 #-> 0 дней, 00:00:00
#x = 224930 #-> 2 дня, 14:28:50
#x = 8639999 #-> 99 дней, 23:59:59
#x = 22493 #-> 0 дней, 06:14:53
#x = 7948799 #-> 91 день, 23:59:59

x = int(input("Введите число от 0 до 8639999: "))

days = x // 86400  # делим наше число без остатка на колво секунд в дне и пол колво дней
n2 = x % 86400   # остаток от деления на колво дней
hours = n2 // 3600   #делим на остаток от деления от кол дней и узнаем кол часов
n4 = n2 % 3600
minutes = n4 // 60     # минуты
seconds = n4 % 60      #секунды

days = str(days)
hours = str(hours)
minutes = str(minutes)
seconds = str(seconds)

lst = ["4", "5", "6", "7", "8", "9"]
if days == 0 or str(days)[-1] in lst:
    xdays = "дней"
elif days == 1 or str(days)[-1] == "1":
    xdays = "день"
else:
    xdays = "дня"
text = f"{days} {xdays}, {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}"
print(text)


#day = 'days'
#hour = 'hour'
#minute = 'minutes'
#second = 'seconds'

#в одном дне 86400 сек
#в часе 3600 сек
# в минуте 60сек
