using System;

namespace вывести_все_элементы__m_и_n_строки__вывести_3_стр
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

            Console.WriteLine("Элементы n-ой строки: ");
            for (int j = 0; j < m; j++)

            {
                int i = n-1;
                Console.Write(a[i, j]);
            }

            Console.WriteLine("  ");

            Console.WriteLine("Элементы m-ого столбца: ");
            for (int i = 0; i < n; i++)
            {
                int j = m-1;
                Console.Write(a[i, j]);
            }

            Console.WriteLine("  ");
            Console.WriteLine("Сумма всех элементов третьей строки: ");
            int sum = 0;
            for (int j=0; j<m; j++)
            {
                int i = 2;
                sum += a[i, j];
            }
            Console.WriteLine(sum);

            Console.ReadKey();
        }
    }
}
