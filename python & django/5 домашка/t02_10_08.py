import random

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Game:
    def __init__(self, *args):
        self.players_list = [*args]
    
    def hit(self, attacker_name, victim_name):
        for i in self.players_list:
            if i.name == attacker_name:
                attacker = i
            elif i.name == victim_name:
                victim = i
        print("{} HP - {}, {} HP - {}".format(attacker.name, attacker.hp, victim.name, victim.hp))
        if attacker.hp <= 0 or victim.hp <= 0:
            for i in [attacker, victim]:
                if i.hp <= 0:
                    print(i.name, "has already lost!")
            return

        damage = int(input("Enter damage ([1;9]): "))
        if damage > 9 or damage < 1:
            print("Damage is too big or too small")
            return

        chance = 1
        if input("Do you want to test your luck? (Y/N): ").lower() == 'y':
            chance = round(random.random(), 1)
            if chance == 0:
                print("Zero percent chance... Better luck next time!")
                return
                
            damage *= round(1/chance, 1)
            print("Your hit chance is {}%, your damage is {}".format(chance * 100, damage))
        
        if chance >= round(random.random(), 1):
            victim.hp -= damage
            print("{} HP - {}, {} HP - {}".format(attacker.name, attacker.hp, victim.name, victim.hp))
            if victim.hp <= 0:
                print(attacker.name, "wins!")
        else:
            print("Miss! :(")

new_game = Game(Player('Alex', 99), Player('Jason', 100))
new_game.hit('Alex', 'Jason')
print()
new_game.hit('Alex', 'Jason')


