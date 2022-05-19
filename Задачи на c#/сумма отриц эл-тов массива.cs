using System;

namespace Task_16
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
                arr[i] = Convert.ToInt32(Console.ReadLine());
            int s = 0;
            for (int i = 0; i < n; i++) 
                if (arr[i] < 0) s += arr[i];
            Console.WriteLine(s);
        }
    }
}
