/*
 * @author Usmanova Aigul
 * 11912
 * Task_35
 */
using System;

namespace Task35
{
    class Program
    {
        static int Fibonachi(int n)
        {
            if (n==0)
            {
                return 0;
            }
            if (n==1)
            {
                return 1;
            }
            return Fibonachi(n - 1) + Fibonachi(n - 2);
        }

        static void Main()
        {
            int otvet = Fibonachi(7);
            Console.WriteLine(otvet);
            Console.ReadKey();
        }
    }
}
