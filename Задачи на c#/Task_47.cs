﻿/*
 * @author Usmanova Aigul
 * 11912
 * Task47
 */
using System;

namespace _000111
{
    class Program
    {
        static void Main(string[] args)
        {
            //автомат выдаст, что строка 1101010 правильная, хотя нет. И так же со строкой 0010101. Ошибка появилась за счет петли в состоянии 2.
            /*программа которая проверяет то, что в двоичных строках либо только 0, либо только 1,либо цифры чередуются  и вывести такие строки на экран*/
            string[] arr = new string[] { "11", "123", "010101", "293", "01010", "010", "00001111" };
            int n = arr.Length;
            for (int i = 0; i < n; ++i) //проходимся по всем словам, i отвечает за номер слова
            {
                int sost = 1;
                foreach (char c in arr[i])
                {
                    switch (sost)
                    {
                        case 0:
                            return; //если case=0, то игнорируем этот символ и выходим из switch

                        case 1:
                            if (c == '1') sost = 2;
                            else if (c == '0') sost = 3;
                            else sost = 0; //то есть ни 0, ни 1, поэтому ошибка
                            break;

                        case 2:
                            if (c == '0') sost = 4;
                            else if (c == '1') sost = 2;
                            else sost = 0;
                            break;

                        case 3:
                            if (c == '1') sost = 6;
                            else if (c == '0') sost = 3;
                            else sost = 0;
                            break;

                        case 4:
                            if (c == '1') sost = 5;
                            else sost = 0;
                            break;

                        case 5:
                            if (c == '0') sost = 4;
                            else sost = 0;
                            break;

                        case 6:
                            if (c == '0') sost = 7;
                            else sost = 0;
                            break;

                        case 7:
                            if (c == '1') sost = 6;
                            else sost = 0;
                            break;
                    }
                    if (sost == 0) break; //мы проигнорировали символ, но нужно также проигнорировать всё число, так что break пропускает это число и дальше переходим к следующему
                }
                if (sost != 0)
                Console.WriteLine(arr[i]);
            }
        }
    }
}
