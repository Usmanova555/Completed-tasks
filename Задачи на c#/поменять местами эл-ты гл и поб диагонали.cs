using System;

namespace поменять_местами_элты_гл_и_поб_диагонали
{
    class Program
    {
        static void Main(string[] args)
        {
            int m;
            int n;
            int tmp;
            m = Convert.ToInt32(Console.ReadLine());
            n = Convert.ToInt32(Console.ReadLine());
            if (m == n)
            {
                Console.WriteLine("Введите матрицу а: ");
                int[,] a = new int[m, n];
                for (int i = 0; i < m; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        a[i, j] = Convert.ToInt32(Console.ReadLine());
                    }
                }
                for (int i = 0; i < m; i++)
                {
                    tmp = a[i, i];
                    a[i, i] = a[i, n - i - 1];
                    a[i, n - i - 1] = tmp;
                }
                Console.WriteLine("Изменённая матрица: ");
                for (int i = 0; i < m; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        Console.WriteLine(a[i, j]);
                    }
                }
            }
        }
    }
}
