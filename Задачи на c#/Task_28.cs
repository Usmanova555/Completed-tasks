/*
 * @aigul Aigul Usmanova 
 * 11912
 * Task_28
 */
using System;

namespace Task28
{
    class Program
    {
        //Написать метод, который проверяет, что в двумерном массиве каждая сумма элементов на побочных диагоналях является четной

        //так как мы рассматриваем побочные диагонали, то предпологаем, что матрица 
        //квадратная.
        static void Input(int[,] mas, int n, int m)
         {
             for (int i = 0; i < n; i++)
             {
                 for (int j = 0; j < m; j++)
                 {
                     mas[i, j] = Convert.ToInt32(Console.ReadLine()); 
                 }
             }
         }
         static void Output(int[,] mas, int n, int m)
         {
             for (int i = 0; i<n; i++)
             {
                 for (int j = 0; j<m; j++)
                 {
                     Console.Write(mas[i, j] + " ");
                 }
                 Console.WriteLine("");
             }
         }
         static void Diagonalka(int [,]mas, int n, int m)
         {
             if (m == n)
             {
                 bool F = true;
                 int t = 0;
                 int sum;
             for (int f = 0; f < n; f++)
                 {
                    sum = 0;
                     for (int i = 0; i<n; i++)
                     {
                         if (t >= n) t -= n;
                         sum += mas[i, t];
                         t += n - 1;
                     }
                 if (sum % 2 != 0) F = false;
                 }
                 if (F) Console.WriteLine("Каждая сумма элементов на побочных диагоналях чётна");
                 else Console.WriteLine("Не верно, есть диагональ с нечётной суммой элементов");
             }
         }

         static void Main ()
         {
             int n = Convert.ToInt32(Console.ReadLine());
             int m = Convert.ToInt32(Console.ReadLine());
             Console.WriteLine(" ");
             int[,] mas = new int[n, m];
             Input(mas, n, m);
             Console.WriteLine("Выведем массив для наглядности:");
             Output(mas, n, m);
             Console.WriteLine("");
             Diagonalka(mas, n, m);
             Console.ReadKey(); 
         }
    }
}
