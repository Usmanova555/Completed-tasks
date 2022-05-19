using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    class Hyperbola : Line
    {
        public Hyperbola (int a, int b) : base(a,b)
        {

        }
        public Hyperbola()
        {
            
        }
        public override double Value(int x)
        {
            double y = A / x + B;
            return y;
        }
        public override void Print()
        {
            Console.WriteLine("Гипербола, задающаяся переменными A и B");
            Console.WriteLine("A = " + A);
            Console.WriteLine("B = " + B);
        }
    }
}
