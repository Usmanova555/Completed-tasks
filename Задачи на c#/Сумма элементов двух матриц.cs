using System;

namespace _11
{
    class Program
    {
        //сумма элементов двух матриц 
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
            Console.WriteLine ("Введите матрицу b: ");
            int[,] b = new int[m, n];
            {
                for (int i = 0; i < m; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        b[i, j] = Convert.ToInt32(Console.ReadLine());
                    }
                }
            }
            int[,] c = new int [m,n];
            Console.WriteLine("Сумма элементов двух матриц: ");
            for (int i = 0; i < m; i++) 
            {
                for (int j = 0; j < n; j++)
                {
                    c[i, j] = a[i, j] + b[i, j];
                    Console.WriteLine(c[i, j]);
                }
            }
        }
    }
}
