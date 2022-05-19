/*
 * @author Usmanova Aigul
 * 11912
 * Task_32
 */
using System;

namespace homework
{
    class Program
    {
        static void Factorial(int n)
        {
            int fact = 1;
            for (int k = 2; k<=n; k++)
            {
                fact *= k;
            }
            Console.WriteLine("Значение n!: ");
            Console.WriteLine(fact);
        }

        static void Main()
        {
            Factorial(16);
        }
    }
}
