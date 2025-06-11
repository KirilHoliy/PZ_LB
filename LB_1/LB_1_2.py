Інвентаризація — тема: Види тварин у зоопарку


zoopark = {
   "лев": 6,
   "пінгвін": 3,
   "панда": 2,
   "слон": 7
}


def onovyty_populyatsiyu(tvaryna, kilkist):
   zoopark[tvaryna] = zoopark.get(tvaryna, 0) + kilkist
   if zoopark[tvaryna] < 0:
       zoopark[tvaryna] = 0


onovyty_populyatsiyu("пінгвін", -2)
onovyty_populyatsiyu("кенгуру", 5)


print("Стан зоопарку:", zoopark)


znykayuchi_vydy = [t for t, k in zoopark.items() if k < 5]
print("Зникаючі види:", znykayuchi_vydy)
