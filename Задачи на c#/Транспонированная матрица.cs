using System;

namespace nh
{
    class Program
    {
        static void Main(string[] args)
        {
            int m;
            int n;
            m = Convert.ToInt32(Console.ReadLine());
            n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите матрицу а: ");
            int[,] a = new int[m, n];
            {
                for (int i = 0; i < m; i++)
                {
                    for (int j = 0; j < n; j++)
                    {

                        a[i, j] = Convert.ToInt32(Console.ReadLine());
                    }
                }
            }
            int[,] b = new int[n, m];
            Console.WriteLine("Транспонированная матрица: ");
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    b[i, j] = a[j, i];
                }
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    Console.WriteLine(b[i, j]);
                }
            }
        }
    }
}
