using System;
using System.IO;

namespace controlwork
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Задание 1");
            Number1();

            Console.WriteLine("Задание 2");
            Number2();
        }
        static void Number1()
        {

            StreamReader In = new StreamReader("Input.txt");
            int count = 0; 
            string word = "";
            while ((word = In.ReadLine()) != null) count++;

            Worker[] w = new Worker[count];

            In.BaseStream.Position = 0;
            string[] words = new string[4];
            int i = 0;
            while ((word = In.ReadLine()) != null)
            {
                words = word.Split(' ');
                w[i] = new Worker(words[0], words[1], words[2], int.Parse(words[3]));
                i++;

            }
            for (int t = 0; t < i - 1; t++)
            {
                if (w[t].CompareTo(w[t + 1]) == 1)
                {
                    Worker s = w[t];
                    w[t] = w[t + 1];
                    w[t + 1] = s;
                }
            }
            StreamWriter Out = new StreamWriter("Output.txt", true);

            for (int k = 0; k < i; k++)
            {
                Out.WriteLine(w[k]);
            }
            Out.WriteLine("");

            In.Dispose();
            Out.Dispose();
            Console.WriteLine("Введите название занимаемой должности");
            string nw = Console.ReadLine();
            foreach (Worker m in w)
            {
                if (m.IfTrue(nw))
                {
                    Out.WriteLine(m.ToString(), true);
                }
            }
            Out.Close();

        }
        static void Number2()
        {
            Game2 game = new Game2();
            Gamer gamer1 = new Gamer();
            Gamer gamer2 = new Gamer();
            gamer1.Input();
            gamer2.Input();
            game.Game(gamer1.HP, gamer1.Name, gamer2.HP, gamer2.Name);
        }
    }
}
