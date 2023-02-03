import self as self


class ATM:
    def __init__(self, montant, utilisateur):
        self.montant = montant
        self.utilisateur = utilisateur
        print("solde de {} : {} euros".format(self.utilisateur, self.montant))

    def retrait(self, montantRetrait):
        self.montant -= montantRetrait
        print("nouveau solde de {}: {} euros".format(self.utilisateur, self.montant))

    def depot(self, montantDepot):
        self.montant += montantDepot
        print("nouveau solde de {}: {} euros".format(self.utilisateur, self.montant))



