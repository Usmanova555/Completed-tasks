using System;
using System.Collections.Generic;
using System.Text;

namespace controlwork
{
    public class Gamer
    { 
        public string Name { set; get; }
        public int HP { set; get; }
        public Gamer(string name, int hp)
        {
            Name = name;
            HP = hp;
        }
        public Gamer()
        {

        }
        public void Input()
        {
            Console.WriteLine("Введите имя игрока : ");
            Name = Console.ReadLine();
            Console.WriteLine("Введите запас здоровья (HP): ");
            HP = int.Parse(Console.ReadLine());
        }
    }
}
