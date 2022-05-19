using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Task3
{
    class Program
    {
        static void Main(string[] args)
        {
            double a, b, c;
            Console.WriteLine("Введите a");
            a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите b");
            b = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите c");
            c = Convert.ToInt32(Console.ReadLine());
            
                double D = Math.Pow (b,2) - 4 * a * c;
                if (D < 0)
                {
                    Console.WriteLine("Корней нет");
                }
                else if (D>0)
                {
                    double x1 = (-b + Math.Sqrt(D)) / (2 * a);
                    double x2 = (-b - Math.Sqrt(D)) / (2 * a);
                Console.WriteLine("Корни уравнения: x1={0}, x2={1}", x1, x2);
                }
                else
            {
                double x1 = (-b )/( 2 * a);
                Console.WriteLine("Корень уравнения: " + x1);
            }
                {
                    Console.ReadKey();
                }
        }
    }
}
