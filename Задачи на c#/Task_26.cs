/*
 * @author Usmanova Aigul
 * 11912
 * Task_26
 */
using System;

namespace _26
{
    class Program
    {
        static void Main(string[] args)
        {
            int m;
            int n;
            m = Convert.ToInt32(Console.ReadLine());
            n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите матрицу a: ");
            if (m == n)
            {
                int[,] a = new int[m, n];
                for (int i = 0; i < m; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        a[i, j] = Convert.ToInt32(Console.ReadLine());
                    }
                }
                int max = a[0, 0];
                for (int i = 0; i < m; i++)
                {
                    int sum = 0;
                    int x = 0;
                    int y = 0;
                    int t;
                    for (int j = i; j < m + i; j++)
                    {
                        t = j;
                        if (t > m - 1)
                        {
                            t = x;
                            x++;
                        }
                        sum += a[y, t];
                        if (sum > max) max = sum;
                        y++;
                    }
                }
                Console.WriteLine("Максимальная сумма элементов диагонали: " + max);
            }
            Console.ReadKey();
        }
    }
}
