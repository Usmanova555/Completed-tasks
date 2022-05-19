/**
 * @author Usmanova Aigul

* 11-912

* Task 07 

*/
using System;

namespace Task_7
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 6;
            while (n <= 30)
            {
                if (n % 3 == 0)
                {
                    Console.Write("{0} ", n);
                }
                else
                {
                    Console.WriteLine("");
                }
                n++;
            }

        }
    }
}
