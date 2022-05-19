/*
 * @author Usmanova Aigul
 * 11912
 * Task22
 */
using System;

namespace Task__22
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите количество элементов: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] a = new int[n];

            Console.WriteLine("Введите элементы: ");
            for (int i = 0; i < n; i++)
                a[i] = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(" ");

            int max = a[0];
            int min = a[0];
            int maxi = 0;
            int mini = 0;

            for (int i = 0; i < n; i++)
            {
                if (a[i] > max)
                {
                    maxi = i;
                }
                if (a[i] < min)
                {
                    mini = i;
                }
            }

            int k;
            k = n - (Math.Abs(mini - maxi)) + 1;
        
            int[] b = new int[k];
            if (maxi < mini)
            {
                for (int j = 0; j <= maxi; j++)
                {
                    for (int i = 0; i <= maxi; i++)
                    {
                        b[j] = a[i];
                        Console.WriteLine(b[j]);
                    }
                }
                for (int i = mini; i < n; i++)
                {
                    for (int j = (maxi + 1); j < k; j++)
                    {
                        b[j] = a[i];
                        Console.WriteLine(b[j]);
                    }
                }
            }
            if (mini < maxi)
            {
                for (int j = 0; j <= mini; j++)
                {
                    for (int i = 0; i <= mini; i++)
                    {
                        b[j] = a[i];
                        Console.WriteLine(b[j]);
                    }
                }
                for (int i = maxi; i < n; i++)
                {
                    for (int j = (mini + 1); j < k; j++)
                    {
                        b[j] = a[i];
                        Console.WriteLine(b[j]);
                    }
                }
            }
            else
            {
                for (int i = 0; i < n; i++) 
                {
                    Console.WriteLine(a[i]); 
                }
            }
            Console.ReadKey();
        }
    }
}
