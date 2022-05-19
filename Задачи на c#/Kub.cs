using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    class Kub : Line
    {
        private readonly int C; //Поле для чтения объявляется с ключевым словом readonly
        public Kub(int a, int b, int c) : base(a,b)
        {
            this.C = c;
        }
        public Kub()
        {
            
        }
        public override double Value(int x)
        {
            double y = A * Math.Pow(x, 2) + B * x + C;
            return (double)y;
        }
        public override void Print()
        {
            Console.WriteLine("Квадратное уравнение, задающееся переменными A, B и C");
            Console.WriteLine("Переменная А = " + A);
            Console.WriteLine("Переменная B = " + B);
            Console.WriteLine("Введите переменную C");
            Console.WriteLine("C = " + C);
        }
    }
}
