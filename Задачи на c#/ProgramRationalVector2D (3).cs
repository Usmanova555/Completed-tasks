using System;
using System.Collections.Generic;
using System.Text;

namespace RationalVector2D
{
    class RationalVector2D
    {
        RationalFraction a;
        RationalFraction b;

        public RationalVector2D()
        {
            a = new RationalFraction(0, 0);
            b = new RationalFraction(0, 0);
        }
        public RationalVector2D(RationalFraction a, RationalFraction b)
        {
            this.a = a;
            this.b = b;
        }
        public RationalVector2D Add(RationalVector2D v)
        {
            return new RationalVector2D(a.Add(v.a), b.Add(v.b));
        }
        public override string ToString()
        {
            return a.ToString() + ',' + b.ToString();
        }
        public double Length() //длина вектора
        {
            return Math.Sqrt((a.Mult(a)).Add(b.Mult(b)).Value());
        }
        public RationalFraction ScalarProduct(RationalVector2D v)
        {
            return (a.Mult(v.a)).Add(b.Mult(v.b));
        }
        public bool Equals(RationalVector2D v)
        {
            if (a.Equals(v.a) && b.Equals(v.b)) return true;
            else return false;
        }
    }
}
