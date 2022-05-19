using System;

namespace C2task
{
    class Program
    {
        static void Main(string[] args)
        {
            int x1, x2, x3, x4;
            int N;
            for (N = 1000; N <= 9999; N++) ;
            {
                x1 = N % 10;
                x2 = (N / 10) % 10;
                x3 = (N / 100) % 10;
                x4 = N / 1000;
                if (x1 != x2 && x1 != x3 && x1 != x4 && x2 != x3 && x2 != x4 && x3 != x4) ;
                {
                    Console.WriteLine(N);
                }
            }
        }
    }
}
