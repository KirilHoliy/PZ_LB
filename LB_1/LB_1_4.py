Управління задачами — тема: План втечі з планети Земля

plan_vtechi = {
   "побудувати ракету": "в процесі",
   "знайти пілота": "очікує",
   "заправити паливо": "очікує"
}


def dodaty_misiyu(nazva, status="очікує"):
   plan_vtechi[nazva] = status


def vydalyty_misiyu(nazva):
   plan_vtechi.pop(nazva, None)


def zminyty_status(nazva, status):
   if nazva in plan_vtechi:
       plan_vtechi[nazva] = status


dodaty_misiyu("запустити двигун")
zminyty_status("побудувати ракету", "виконано")


ochikuyut_misiyi = [m for m, s in plan_vtechi.items() if s == "очікує"]
pri
nt("Очікують дії:", ochikuyut_misiyi)
