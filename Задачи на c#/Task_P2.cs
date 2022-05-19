/*
 * @author Usmanova Aigul
 * 11912
 * TaskP2
 */
using System;

namespace ConsoleApp12
{
    class Program
    {
        /*необходимо вывести на экран все элементы из закрашенной области*/
        //написать метод, который делает это
        //предполагается, что ромб можно построить только вокруг матрице с нечётным количеством строк и столбцов

        static void Main()
        {
            int[,] mas = new int[5, 5];
            Input(mas, 5);
            Output(mas, 5);
            Console.WriteLine("");
            Matrix(mas, 5);
        }

        static void Input(int[,] mas, int n)
        //так как матрица квадратная нам понадибится только n 
        {
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < n; ++j)
                {
                    mas[i, j] = Convert.ToInt32(Console.ReadLine());
                }
            }
        }
        static void Output(int[,] mas, int n)
        //так как матрица квадратная нам понадибится только n 
        {
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < n; ++j)
                {
                    Console.Write(mas[i, j]);
                }
                Console.WriteLine("");
            }
        }

        static void Matrix(int[,] mas, int n)
        {
            int i = 0;
            int k = n / 2; int p = n / 2;    //переменный p и k отвечаются за сдвиг по столбцам одновременно вправо и влево и доходят до середине матрицы
            while ((p > 0) && (k < n - 1))
            {
                for (int j = p; j <= k; ++j)
                {
                    Console.WriteLine(mas[i, j]);
                }
                p--; k++;
            i++;
            }
            
            p = 0; k = n - 1;
            while ((k >= n / 2) && (p <= n / 2)) //начиная с середины всех строк идёт сужение по столбцам
            {
                for (int j = p; j <= k; ++j)
                    Console.WriteLine(mas[i, j]);
                p++; k--;
            i++;
            }
        }
    }
}
