/* 
 * @author Usmanova Aigul
 * 11912
 * Task 13
 * */
using System;

namespace Task_13
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите шестизначное число: ");
            int n = Convert.ToInt32(Console.ReadLine());

            int sum = 0; int sum1 = 0;
            int ost = 0;
            int i = 1;
            int k = 10;

            while (i <= 3) 
            {
                ost = n % k;
                sum += ost;
                n = n / k;
                i++;
            }
            i = 1;

            while (i <= 3) 
            {
                ost = n % k;
                sum1 += ost;
                n = n / k;
                i++;
            }
            if (sum == sum1)
            {
                Console.WriteLine("Этот билет счастливый!");
            }
            else
            {
                Console.WriteLine("Это обычный билет");
            }
            Console.ReadKey();
        }
    }
}
