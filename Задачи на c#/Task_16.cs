/*
 * @author Usmanova Aigul
 * 11912
 * Task_16
 */
using System;

namespace _16
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите число от 3 до 8: ");
            int k;
            k = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите число в данной степени счисления: ");
            int n;
            n = Convert.ToInt32(Console.ReadLine());
            int t;
            int p;
            double sum = 0;
            p = 0;
            do
            {
                t = n % 10;
                sum += t * Math.Pow(k, p);
                n /= 10;
                p++;
            }
            while (n > 1);
            Console.WriteLine(sum);
        }
    }
}
