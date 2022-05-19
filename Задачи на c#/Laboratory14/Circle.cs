using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    class Circle : Figure 
    {
        public int R;
        public Circle(int r) 
        {
            this.R = r;
        }
        public Circle()
        {
            R = 0;
        }
        public override double Perimetr()
        {
            double pi = Math.PI;
            return (double)R * 2 * pi;
        }
        public override double Square()
        {
            double pi = Math.PI;
            return (double)pi * R * R;
        }
        public override void Print()
        {
            Console.WriteLine("Круг с радиусом R");
            Console.WriteLine("Введите радиус R");
            R = int.Parse(Console.ReadLine());
        }
    }
}
