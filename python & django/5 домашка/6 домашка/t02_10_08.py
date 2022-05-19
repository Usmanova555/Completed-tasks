class Gamer:
    name = ''
    hp = 0

    def gamer(self, name, hp):
        self.name = name
        self.hp = hp

    def __get__(self, name, hp):
        return name, hp

    def __set__(self, name, hp, value):
        name.value = value
        hp.value = value

    def input(self):
        print('Введите имя игрока: ')
        name = str(input())
        print('Введите запас здоровья: ')
        hp = int(input())


class Game(Gamer):
    def gameCicle(self, hp1, name1, hp2, name2):
        from random import randint
        player1 = Gamer(self, name1, hp1)
        player2 = Gamer(name2, hp2)
        while (player1.hp > 0) or (player2.hp > 0):
            damage = randint(1, 10)
            player2.hp -= damage
            print(f'{damage} урон нанёс первый игрок\n{player2.hp} осталось у второго игрока')
            if player2.hp <= 0: break

            damage1 = randint(1, 10)
            player1.hp -= damage1
            print(f'{damage} урон нанёс второй игрок\n{player1.hp} осталось у первого игрока')
            if player1.hp <= 0: break
        if player1.hp <= 0:
            print('победил игрок номер 2')
        else:
            print('победил игрок номер 1')


class Program(Gamer, Game):
    game = Game()
    gamer1 = Gamer()
    gamer2 = Gamer()

    gamer1.input()
    gamer2.input()
    game.gameCicle(gamer1.hp, gamer1.name, gamer2.hp, gamer2.name)
