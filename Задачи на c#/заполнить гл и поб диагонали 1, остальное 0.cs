using System;

namespace заполнить_массив
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] a = new int[7,7];
            for (int i = 0; i < 7; i++)
            {
                for (int j = 0; j < 7; j++)
                {
                    a[i, j] = 0;
                }
            }
            for (int i = 0; i<7; i++)
            {
                for (int j = 0; j<7; j++)
                {
                    if (i == j) a[i, j] = 1;
                }
            }
            for (int i = 0; i<7; i++)
            {
                for (int j=0; j<7; j++)
                {
                    if (i==6-j) a[i, j] = 1;
                }
            }
            for (int i = 0; i < 7; i++)
            {
                Console.WriteLine();
                for (int j = 0; j < 7; j++)
                {
                    Console.Write(a[i, j]);
                }
            }
        }
    }
}
