import socket
import random

class Exp(Exception):
    def __init__(self, a): self.a = a
    
class Exp2(Exception):
    def __init__(self, a): self.a = a
    
class Play:
    def __init__(self):
        self.mesta = ['O'] * 64 
        self.letter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.kolv = 0

    def add(self, pos2):
        if self.mesta[self.letter[pos2[0].upper()]*8 + int(pos2[1]) - 1] == 'O':
            self.mesta[self.letter[pos2[0].upper()]*8 + int(pos2[1]) - 1] = 'S'
            self.kolv += 1
        else: raise Exp('Это место занято!')

    def smena_mest(self, pos2): return self.letter[pos2[0].upper()]*8 + int(pos2[1]) - 1
    
    def kick(self, pos2):
        if self.mesta[self.smena_mest(pos2)] == 'S' or self.mesta[self.smena_mest(pos2)] == 'O':
            f = self.mesta[self.smena_mest(pos2)]
            if f == 'S':
                self.mesta[self.smena_mest(pos2)] = 'D'
                self.kolv -= 1
                return True
            else: self.mesta[self.smena_mest(pos2)] = 'X'
            return False
        else: raise Exp2('Здесь уже побито.')
    
    def random_mesto(self):
        letter2 = [i for i in self.letter.keys()]
        number = [i for i in range(1,9)]
        sss = random.choice(letter2) + str(random.choice(number))
        return sss
    
    def rules(self):
        p = "Правила игры:\n"
        p += "10 кораблей на одном игровом поле\n"
        p += "S - корабль, D - подбитый корабль, O - пустая клетка, X - битая пустая клетка\n"
        return p
    
    def begin(self, action):
        c = win.recv(1024).decode('utf-8')
        try:
            if start == 'add': self.add(c)
            else: return self.kick(c)
        except Exp2:
            print('Здесь уже побито. Введите координаты ещё раз.')
            self.begin(start)
        except Exp:
            print('Здесь уже стоит корабль. Введите координаты ещё раз.')
            self.begin(start)
            
    def random_play(self):
        free = [i for i in range(64)]
        while self.kolv < 10:
            rnd_pos = self.random_mesto()
            if self.smena_mest(rnd_pos) in free:
                self.add(rnd_pos)
                free.remove(self.smena_mest(rnd_pos))
                
    def __str__(self):
        p = 'A  B  C  D  E  F  G  H\n'
        f = 0
        for i in range(8):
            p += str(i+1)
            p += f' {self.positions[f]}  {self.positions[f+8]}  {self.positions[f+16]}  {self.positions[f+24]}  {self.positions[f+32]}  {self.positions[f+40]}  {self.positions[f+48]}'
            p += f' {self.positions[f+56]}\n'
            f += 1
        return p

def view(_from, _to):
    for i in range(64):
        if _from.mesta[i] == 'X' or _from.mesta[i] == 'D': _to.mesta[i] = _from.mesta[i]
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
win, addr = sock.accept()
print('connected:', addr)

s = Play()
s.random_play()
s2 = Play()
win.send(bytes(str(s.rules()), encoding='utf-8'))
s_opt = [i for i in range(64)]
ss = Play()
print(s)
change = 'human'
i = 0
finish = False
while i < 30:
    repeat = ''
    if i == 0:
        while s2.kolv < 10:
            win.to(bytes('Введите место для корабля: ', encoding='utf-8'))
            s2.begin('add')
            win.to(str(s2).encode('utf-8'))
    if change == 's2':
        i += 1
        win.to('Ходите'.encode('utf-8'))
        if s.begin('take_hit') == False:
            view(s, ss)
            repeat += 'Промах\n' 
            repeat += str(ss)
            repeat += '\nСейчас ходит компьютер...\n'
            win.to(repeat.encode('utf-8'))
            change = 'computer'
        else:
            view(s, ss)
            repeat += '\nПрямое попадание!\n'
            repeat += str(ss)
            win.to(repeat.encode('utf-8'))
        if s.kolv != 0:
            win.to(repeat.encode('utf-8'))
        else:
            repeat += '\nЭто победа!'
            win.to(repeat.encode('utf-8'))
            finish = True
            break
    else:
        s = s.random_mesto()
        if s.smena_mest(s) in s_options:
            s_opt.remove(s.smena_mest(s))
            if s2.kick(s) == False:
                change = 'human'
                repeat += 'Промах\n'
            else:
                repeat += f'Вас подбили на {s}\n'
                repeat += 'Ваша доска:\n' + str(s2
            if (s2.kolv != 0): win.to(repeat.encode('utf-8'))
            else:
                win.to(str(repeat +'\nКонец, вы проиграли.').encode('utf-8'))
                finish = True
                break
    if finish: break
    if i == 30: win.to('\nКонец, вы проиграли.'.encode('utf-8'))
win.close()





