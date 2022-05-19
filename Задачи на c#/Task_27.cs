/*
 * @author Usmanova Aigul
 * 11912
 * Task_27
 */
using System;

namespace ConsoleApp4
{
    class Program
    {
        static void Main(string[] args)
        {
            int m;
            int n;
            int l;
            m = Convert.ToInt32(Console.ReadLine());
            n = Convert.ToInt32(Console.ReadLine());
            l = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите матрицу a: ");
            int[,] a = new int[m, n];
            for (int i = 0; i< m; i++)
            {
                for (int j=0; j<n; j++)
                {
                    a[i, j] = Convert.ToInt32(Console.ReadLine());
                }
            }
            Console.WriteLine("Введите матрицу b: ");
            int[,] b = new int[n, l];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < l; j++)
                {
                    b[i, j] = Convert.ToInt32(Console.ReadLine());
                }
            }
            int[,] c = new int[m, l];
            for (int i = 0; i<m; i++)
            {
                for (int j = 0; j<l; j++)
                {
                    for (int k = 0; k<n; k++)                   
                    {
                        c[i, j] += a[i, k] * b[k, j];
                    }
                }
            }
            Console.WriteLine("Получившаяся матрица: ");
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < l; j++)
                {
                    Console.WriteLine(c[i, j]);
                }
            }
            Console.ReadKey();
        }
    }
}
