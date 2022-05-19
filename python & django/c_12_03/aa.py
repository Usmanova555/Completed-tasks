import socket
sss = socket.socket()
sss.connect(('localhost', 9090))
print(kick.recv(1024).decode('utf-8'))
go = True
aa = 0
k = 0

while go and k <= 30:
    while aa <= 10:
        print(sss.recv(1024).decode('utf-8'))
        kick.send(input().encode('utf-8'))
        print(sss.recv(1024).decode('utf-8'))
        aa += 1
    one = kick.recv(1024).decode('utf-8')
    print(str(one))
    if one.find('\nКонец. Проигрыш.') != -1:
        break
    kick.send(input().encode('utf-8'))
    k+=1
    two = sss.recv(1024).decode('utf-8')
    print(two)
    if two.endswith('Победа.'):
        go = False
        break
    elif two.endswith('Сейчас ходит компьютер'):
        lose = True
        play = sss.recv(1024).decode('utf-8')
        print(play)
        if play.find('Вы были подбиты на') != -1:
            lose = False
            while not lose:
                play = sss.recv(1024).decode('utf-8')
                print(play)
                if play.rfind('Вы были подбиты на') == -1: lose = True
                if play.endswith('Конец. Проигрыш'): go = False
    if k+1 == 31: print('Конец. Проигрыш')
kick.close()
