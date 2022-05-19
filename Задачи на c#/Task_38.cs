/*
 * @author Usmanova Aigul
 * 11912
 * Task_38
 */
using System;

namespace ConsoleApp6
{
    class Program
    {
        static void Main()
        {
            string s;
            Console.WriteLine("Строка s: ");
            s = Console.ReadLine();
            string s1;
            Console.WriteLine("Строка s1: ");
            s1 = Console.ReadLine();
            int j = 0;
            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] < s1[j])
                {
                    Console.WriteLine("Строка s стоит раньше строки s1");
                    return;
                }
                if (s[i] > s[j])
                {
                    Console.WriteLine("Строка s1 стоит раньше строки s");
                    return;
                }
                if (s[i] == s1[j]) j++;
            }
            Console.ReadKey();
        }
    }
}
