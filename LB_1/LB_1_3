Статистика продажів — тема: Продаж метеоритів NASA

prodazhi = [
   {"meteoryt": "Orion-X", "kilkist": 1, "tsina": 100000},
   {"meteoryt": "Vega-5", "kilkist": 3, "tsina": 45000},
   {"meteoryt": "Orion-X", "kilkist": 2, "tsina": 95000}
]


def dokhid_po_meteorytah(zvity):
   dohody = {}
   for z in zvity:
       name = z["meteoryt"]
       suma = z["kilkist"] * z["tsina"]
       dohody[name] = dohody.get(name, 0) + suma
   return dohody


dokhody = dokhid_po_meteorytah(prodazhi)
print("Дохід з метеоритів:", dokhody)


kosmos_hity = [k for k, s in dokhody.items() if s > 100000]
print("Метеорити з доходом > 100000:", kosmos_hity)
