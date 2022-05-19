using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    class Triangle : Rectangle
    {
        public int C;
        public Triangle(int a, int b, int c) : base(a, b)
        {
            this.C = c;
        }
        public Triangle()
        {
            C = 0;
        }
        public override double Perimetr()
        {
            return (A + B + C);
        }
        public override double Square()
        {
            double d1 = Math.Sqrt(Perimetr() * (Perimetr() - A) * (Perimetr() - B) * (Perimetr() - C));
            return d1;
        }
        public override void Print()
        {
            Console.WriteLine("Треугольник со сторонами A, B, C");
            Console.WriteLine("Введите сторону A");
            A = int.Parse(Console.ReadLine());
            Console.WriteLine("Введите сторону B");
            B = int.Parse(Console.ReadLine());
            Console.WriteLine("Введите сторону C");
            C = int.Parse(Console.ReadLine());
        }
    }
}
