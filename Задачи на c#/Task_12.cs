/*
 * @author Usmanova Aigul
 * 11912
 * Task_12
 */
using System;

namespace _12
{
    class Program
    {
        static void Main(string[] args)
        {
            int n;
            int k;
            int t;
            n = Convert.ToInt32(Console.ReadLine());
            if ((n % 10) < ((n / 10) % 10))
            {
                do
                {
                    k = n % 10;
                    t = (n / 10) % 10;
                    n /= 10;
                }
                while (k < t);
            }
            if (n < 10)
            {
                Console.WriteLine("Да");
            }
            else
            {
                Console.WriteLine("Нет");
            }
        }
    }
}
