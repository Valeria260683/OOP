"""Создайте класс Zebra, внутри которого есть метод which_stripe, который поочередно
печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"
Пример работы с классом Zebra
z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"
"""
class Zebra:
  def __init__(self):
    self.stripe = "Полоска белая"

  def which_stripe(self):
    print(self.stripe)
    if self.stripe == "Полоска белая":
        self.stripe = "Полоска черная"
    else:
        self.stripe = "Полоска белая"