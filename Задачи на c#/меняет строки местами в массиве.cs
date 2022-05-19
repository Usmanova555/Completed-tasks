using System;

namespace поменять_в_массиве_строки_1_с_n__2_c_n_1_итд
{
    class Program
    {
        static void Main(string[] args)
        {
            int n;
            int m;
            n = Convert.ToInt32(Console.ReadLine());
            m = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("   ");
            int[,] a = new int[n, m];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    a[i, j] = Convert.ToInt32(Console.ReadLine());
                }
            }
            int tmp;
            for (int j = 0; j<m; j++)
            {
                for (int i = 0; i<n; i++)
                {
                    tmp = a[i, j];
                    a[i, j] = a[n-i-1, j];
                    a[n-i-1, j] = tmp;
                }
            }
            Console.WriteLine("Получившийся массив: ");
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    Console.WriteLine(a[n-i-, j]);
                }
            }
        }
    }
}
