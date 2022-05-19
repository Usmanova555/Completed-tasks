/*
 * @author Usmanova Aigul
 * 11912
 * Task_34
 */
using System;

namespace Fibbonachi
{
    class Program
    {
        //Ряд Фибоначи 1, 1, 2, 3, 5, 8, 13, 21, … Формула вычисления n-го числа Fn=Fn-1+Fn-2
        static void Fibonachi(int[] a, int n)
        {
            a[0] = 1; a[1] = 1;
            for (int i=2; i<n; i++)
            {
                a[i] = a[i - 1] + a[i - 2];
            }
            Console.WriteLine(a[n - 1]); 
        }

        static void Main ()
        {
            int[] a = new int[7];
            Fibonachi(a, 7);      //7-ой элемент программа выведет 13
            Console.ReadKey();
        }
    }
}
