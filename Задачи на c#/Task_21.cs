﻿/*
 * @author Usmanova Aigul
 * 11912
 * Task 21
 */
using System;
/*Дан отсортированный по возрастанию массив. 
Вводится число k. Найти число k в массиве методом деления пополам 
(алгоритм бинарного поиска), вывести индекс элемента массива, если 
такой есть. Количество элементов массива может быть нечетным. 
Рекурсию не использовать. */
namespace Task_21
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = new int[30];
            Random rnd = new Random();
            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] = rnd.Next(10, 101);
            }
            Array.Soft(arr); //Array.Sort, а не Array.Soft ?
            for (int i = 0; i < arr.Length; i++)
            {
                Console.Write("{0},", arr[i]);
            }
            int Start = 0;
            int End = arr.Length;
            int Center = (Start + End) / 2;
            int k = 23;
            //Работать не будет. Не будут просмотрены все элементы. Либо всегда поиск будет осуществляться в левой половине, либо в правой. 
            while (k < arr[Center])
            {
                End = Center;
                Center = (End + Start) / 2;
                if (k == arr[Center])
                {
                    Console.WriteLine("The Index is{0}", Center);
                    break;
                }
            }
            while (k > arr[Center])
                {
                Start = Center;
                Center = (End + Start) / 2;
                if (k == arr[Center])
                {
                    Console.WriteLine("The Index is{0}", Center);
                    break;
                }
            }
        }
    }
}
