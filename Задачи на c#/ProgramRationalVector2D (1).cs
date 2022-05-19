using System;

namespace RationalVector2D
{
    class program
    {
        static void Main()
        {
            RationalVector2D dd = new RationalVector2D(new RationalFraction(3, 4), new RationalFraction(3, 6));
            RationalVector2D ss = new RationalVector2D(new RationalFraction(2, 3), new RationalFraction(2, 4));
            RationalVector2D d3 = dd.Add(ss);
            Console.WriteLine("Сложение рациональных векторов: " + d3);

            Console.WriteLine("");

            RationalFraction d4 = dd.ScalarProduct(ss);
            d4.Reduce();
            Console.WriteLine("Скалярное произведение: " + d4.ToString());

            Console.WriteLine("");

            Console.WriteLine("Длина вектора: " + dd.Length());

            Console.WriteLine("");

            Console.WriteLine("Равны ли лва вектора? " + dd.Equals(ss));

            Console.WriteLine("");

        }
    }
}
