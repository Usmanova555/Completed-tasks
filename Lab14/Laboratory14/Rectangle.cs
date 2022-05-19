using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    class Rectangle : Figure
    {
        public int A;
        public int B;
        public Rectangle(int a, int b)
        {
            this.A = a;
            this.B = b;
        }
        public Rectangle()
        {
            A = 0;
            B = 0;
        }
        public override double Perimetr()
        {
            return (A + B) * 2;
        }
        public override double Square()
        {
            return (A * B);
        }
        public override void Print()
        {
            Console.WriteLine("Прямоугольник со сторонами A и B");
            Console.WriteLine("Введите сторону A");
            A = int.Parse(Console.ReadLine());
            Console.WriteLine("Введите сторону B");
            B = int.Parse(Console.ReadLine());
        }
    }
}
