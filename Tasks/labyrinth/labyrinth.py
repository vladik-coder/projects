from random import randint
import abc

class Wall:
    def __init__(self):
        self.name = 'wall'

    def __repr__(self):
        return self.name

    def with_door(self):
        self.name = 'wall with door'
        self.door = Door()
        return self


class Door:
    def __init__(self):
        self.name = 'door'

class Room:
    def __init__(self, wall, count):
        self.walls = [wall]
        for i in range(3):
            self.walls.append(Wall())
        self.name = 'room '+ str(count)

    def get_walls(self):
        return self.walls

    def rand_wall(self):
        rand_index = randint(0,3)
        walls = self.get_walls()
        return walls[rand_index]

    def __repr__(self):
        return self.name


class Builder:
    def __init__(self, count = 1):
        self.rooms = []
        self.count = count

    def start_build(self):
        room = Room(Wall(),self.count)
        self.rooms.append(room)
        self.count +=1
        print(f'{room} created')
        return self.rooms

    def get_rooms(self):
        return self.rooms

    def rand_room(self):
        rand_index = randint(0,len(self.get_rooms())-1)
        rand_room = self.get_rooms()[rand_index]
        return rand_room

    def build_rooms(self, room_quantity):
        while room_quantity > len(self.get_rooms()):
            rand_room = self.rand_room()
            x=[wall for wall in rand_room.get_walls() if wall.name == 'wall']
            while len(x) == 0:
                rand_room = self.rand_room()
                x = [wall for wall in rand_room.get_walls() if wall.name == 'wall']
            rand_wall = rand_room.rand_wall()
            while rand_wall.name != 'wall':
                rand_wall = rand_room.rand_wall()
            rand_wall.with_door()
            self.get_rooms().append(Room(rand_wall,self.count))
            print(f'room {self.count} created')
            self.count +=1

class Character(abc.ABC):

    @abc.abstractmethod
    def move(self):
        pass


    @abc.abstractmethod
    def fight(self):
        pass

class Hero(Character):
    def __init__(self,lab):
        self.lab = lab
        self.room = lab[0]

    def move(self):
        room = self.room
        rand_wall = room.rand_wall()
        while rand_wall.name != 'wall with door':
            rand_wall = room.rand_wall()
        for room in self.lab:
            for wall in room.get_walls():
                if wall.name == 'wall with door' and wall.door == rand_wall.door and room != self.room:
                    self.room = room
                    print(f'hero in the {room}')
                    return self.room

    def fight(self):
        print('Hero fights')
        print('Hero wins!')


class Monster(Character):
    def __init__(self, lab):
       self.room = lab[-1]
       self.lab = lab

    def move(self):
        room = self.room
        rand_wall = room.rand_wall()
        while rand_wall.name != 'wall with door':
            rand_wall = room.rand_wall()
        for room in self.lab:
            for wall in room.get_walls():
                if wall.name == 'wall with door' and wall.door == rand_wall.door and room != self.room:
                    self.room = room
                    print(f'monster in the {room}')
                    return self.room

    def fight(self):
        print('Monster fights')

class Game:

    def __init__(self):
        b = Builder()
        b.start_build()
        b.build_rooms(int(input('Enter the quantity of rooms:\n')))
        lab = b.get_rooms()
        self.hero = Hero(lab)
        self.monster = Monster(lab)

    def start_game(self):
        while self.hero.room != self.monster.room:
            self.hero.move()
            if self.hero.room != self.monster.room:
                self.monster.move()
        for character in [self.monster, self.hero]:
            character.fight()

game = Game()
game.start_game()