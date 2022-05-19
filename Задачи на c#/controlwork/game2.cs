using System;
using System.Collections.Generic;
using System.Text;

namespace controlwork
{
    class Game2 : Gamer
    {
        public Game2()
        {

        }
        public void Game(int hp1, string name1, int hp2, string name2)
        {
            Random r = new Random();
            Gamer Player1 = new Gamer(name1, hp1);
            Gamer Player2 = new Gamer(name2, hp2);
            while (Player1.HP > 0 || Player2.HP > 0)
            {

                int damage = r.Next(1, 10);
                Player2.HP -= damage;
                Console.WriteLine($"{damage} удар нанёс первый игрок\n{Player2.HP} Осталось у второго игрока");
                if (Player2.HP <= 0) break;
                int damage1 = r.Next(1, 10);

                Player1.HP -= damage1;
                Console.WriteLine($"{damage1} удар нанёс второй игрок\n{Player1.HP} Осталось у первого игрока");
                if (Player1.HP <= 0) break;
            }
            Console.WriteLine("");
            if (Player1.HP <= 0) Console.WriteLine("Выиграл игрок №2!"); else Console.WriteLine("Выиграл игрок №1!");
        }

    }
}
