using System;

namespace Task_4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите день: ");
            int d = Convert.ToInt32(Console.ReadLine());
            Console.Write("Введите месяц: ");
            int m = Convert.ToInt32(Console.ReadLine());
            Console.Write("Введите год: ");
            int g = Convert.ToInt32(Console.ReadLine());
            if ((m == 12) & (d == 31))
            {
                Console.WriteLine("Дата следующего дня: {0}.{1}.{2}", 1, 1, (g + 1));
            }
            else if (((m == 1) | (m == 3) | (m == 5) | (m == 7) | (m == 8) | (m == 10)) & (d == 31))
            {
                Console.WriteLine("Дата следующего дня: {0}.{1}.{2}", 1, (m + 1), g);
            }
            else if (((m == 2) | (m == 4) | (m == 6) | (m == 9) | (m == 11)) & (d == 30))
            {
                Console.WriteLine("Дата следующего дня: {0}.{1}.{2}", 1, (m + 1), g);
            }
            else if ((m == 2) & (d == 28) & ((g % 4) != 0))
            {
                Console.WriteLine("Дата следующего дня: {0}.{1}.{2}", 1, 3, g);
            }
            else if (((g % 4) == 0) & (d==28) & (m == 2))
            {
                Console.WriteLine("Дата следующего дня:{0}.{1}.{2}", (d + 1), m, g);
            }
            else
            {
                Console.WriteLine("Дата следующего дня: {0}.{1}.{2}", (d + 1), (m), g);
            }
        }
    }
}
