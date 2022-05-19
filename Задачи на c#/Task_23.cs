/*
 * @author Usmanova Aigul
 * 11912
 * Task_23
 */
using System;

namespace ConsoleApp3
{
    class Program
    {
        static void Main(string[] args)
        {
            int n;
            Console.WriteLine("Введите количсество цифр в числе: ");
            n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите число");
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
            {
                a[i] = Convert.ToInt32(Console.ReadLine());
            }
            int b;
            Console.WriteLine("Введите любую цифру от 1 до 9: ");
            b = Convert.ToInt32(Console.ReadLine());
            int[] k = new int[n];
            int[] celch = new int[n];

            k[n-1] = (a[n - 1] * b) % 10;
            if ((a[n - 1] * b)>=10)
            { 
                celch[n-2] = (a[n - 1] * b) / 10;
            }
            

            for (int i = (n - 2); i > 0; i--)
            {
                    k[i] = ((a[i] * b) + celch[i]) % 10;
                    celch[i-1] = ((a[i] * b) + celch[i]) / 10;
            }
            k[0] = a[0] * b + celch[0];
            for (int i=0; i<n; i++)
            {
                Console.Write(k[i]);
            }
            Console.ReadLine();
        }
    }
}
