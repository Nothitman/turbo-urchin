import items, enemies, actions, world


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            move.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
 
        return moves


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

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

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

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True
