/* 
 * @author Usmanova Aigul
 * 11912
 * Task17
 */
using System;

namespace Task1._17
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите число элементов массива: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] arr = new int[n];
            int j = 1;
            for (int i = 0; i < n; i++)
            {
                if ((i % 2) == 0)
                {
                    arr[i] = j;
                    Console.WriteLine(arr[i]);
                }
                else
                {
                    arr[i] = j * (-1);
                    Console.WriteLine(arr[i]);
                }
                j += 2;
            }
        }
    }
}
