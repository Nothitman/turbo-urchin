import items, enemies


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


class StartingRoom(MapTile):
    def intro_text(self):
        return "You find yourself in a cave which is dimly lit. You are at a crossroads, which way do you go?"

    def modify_player(self, player):
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp = self.enemy.damage
            print("Enemy does {} damage. You have {} HP Remaining".format(self.enemy.damage, self.the_player.hp))

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """Just an empty room in the cave, nothing to see here."""

    def modify_player(self, player):
        pass

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """A giant spider jumps out in front of you!"""
        else:
            """The spider has no life left in him."""

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x , y, items.Dagger())

    def intro_text(self):
        return """You have found a dagger."""

class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """An Ogre steps out from behind a rock."""
        else:
            """The Ogre has been slain."""

class FindGoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x , y, items.Gold())
