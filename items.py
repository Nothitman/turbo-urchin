class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold", description="A round coin with {} stamped on the front.", value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock", description="A blunt rock to bash your enemies with.", value="0", damage="5")

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",description="A sharp dagger to stab and slash enemies with.", value="10", damage="10")
