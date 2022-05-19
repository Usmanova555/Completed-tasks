/*
 * @author Usmanova Aigul
 * 11912
 * Task_25
 */
using System;

namespace _25
{
    class Program
    {
        static void Main(string[] args)
        {
            //программа не берёт в счёт главную диагональ, хотя можно предположить, что она параллельна самой себе
            int m;
            m = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите матрицу а: ");
            int[,] a = new int[m, m];
                for (int i = 0; i < m; i++)
                {
                    for (int j = 0; j < m; j++)
                    {
                        a[i, j] = Convert.ToInt32(Console.ReadLine());
                    }
                }
                int sum = a[m - 1, 0];
                int ind = -(m - 1);
                for (int i = 1; i < m - 1; i++)
                {
                    int p = 0;

                    int j = i;
                    int j1 = 0;
                    while (j < m)
                    {
                        p += a[j, j1];
                        j++;
                        j1++;
                    }
                    if (p > sum)
                    {
                        sum = p;
                        ind = -i;
                    }
                }
                for (int i = 1; i < m-1 ; i++)
                {
                    int p = 0;

                    int j = 0;
                    int j1 = i;
                    while (j < m-1)
                    {
                        p += a[j, j1];
                        j++;
                        j1++;
                    }
                    if (p > sum)
                    {
                        sum = p;
                        ind = i;
                    }
                }
                Console.WriteLine(" ");
                if (ind > 0)
                {
                    int j = 0;
                    int j1 = ind;
                    while (j < m)
                    {
                        Console.WriteLine(a[j, j1]);
                        j++;
                        j1++;
                    }
                }
                else
                {
                    int j = ind;
                    int j1 = 0;
                    while (j < m)
                    {
                        Console.WriteLine(a[j, j1]);
                        j++;
                        j1++;
                    }
                }
            Console.ReadKey();
        }
    }
}
