/*
 * @author Usmanova Aigyl
 * 11912
 * Task_29
 */
using System;

namespace Task_29
{
    class Program
    {
        static void Input(int[,] mas, int x, int y)
        {
            for (int i = 0; i < x; i++)
            {
                for (int j = 0; j < y; j++)
                {
                    mas[i, j] = 5;
                }
            }
        }
        static void Output(int[,] mas, int x, int y)
        {
            for (int i = 0; i < x; i++)
            {
                for (int j = 0; j < y; j++)
                {
                    Console.Write(mas[i, j] + " ");
                }
                Console.WriteLine("");
            }
        }
        static void Triangle(int[,] mas, int x, int y)
        {
            int m = x;
            int n = 0;
            for (int i = 0; i < x; i++)
            {
                for (int j = 0; j < y; j++)
                {
                    if (((j > n) && (j < (m - 1))) || (j < n) && (j > (m - 1))) 
                    {
                        mas[i, j] = 0;
                    }

                }
                n++;
                m--;
            }
        }
        static void Main()
        {
            int[,] mas = new int[5, 5];
            Input(mas, 5, 5);
            Output(mas, 5, 5);
            Console.WriteLine("  ");
            Triangle(mas, 5, 5);
            Output(mas, 5, 5);
            Console.ReadKey();
        }
    }
}
