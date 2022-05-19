using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    class Line : Function
    {
        public int A;
        public int B;
        public Line(int a, int b)
        {
            this.A = a;
            this.B = b;
        }
        public Line()
        {

        }
        public override double Value(int x)
        {
            return (A * x + B);
        }
        public override void Print()
        {
            Console.WriteLine("Линейное уравнение, задающееся переменными A и B");
            Console.WriteLine("A = " + A);
            Console.WriteLine("B = " + B);
        }
    }
}
