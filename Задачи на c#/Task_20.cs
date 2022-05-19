﻿/*
 * @author Usmanova Aigul
 * 11912
 * Task_20
 */
using System;

namespace _20
{
    class Program
    {
        static void Main(string[] args)
        {
            int n; int k = 0;
            n = Convert.ToInt32(Console.ReadLine());
            int[] arr = new int[n];
            Console.WriteLine("Введите числа с клавиатуры: ");
            for (int i = 0; i < n; i++)
            {
                arr[i] = Convert.ToInt32(Console.ReadLine());
            }
            //сортировка реализована неверно. Распечатайте отсортированный массив в конце
            for (int i = 1; i <= (n - 1); i++)
            {
                for (int j = 1; j <= (n - i); j++)
                {
                    if (arr[j] > arr[j + 1])// здесь будет выход за границы массива, т.е. j+1 может стать >=n
                    {
                        k = arr[i];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = k;
                    }
                }
            }
            int p = arr[0];
            for (int i = 1; i < n; i++)
            {
                if (p == arr[i])
                {
                    Console.WriteLine("В массиве есть неуникальные элементы");
                    return;
                }
                p = arr[i];
            }
            Console.WriteLine("Все элементы уникальны");
            Console.ReadKey();
        }
    }
}
