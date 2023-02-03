from atm import ATM

stephane = ATM(1500, "stephane")
fatima = ATM(1000, "fatima")
stephane.retrait(300)
fatima.depot(150)
stephane.transfert("fatima","stephane", 150)
