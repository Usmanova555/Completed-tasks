using System;
using System.Collections.Generic;
using System.Text;

namespace RationalFraction
{
    class RationalFraction
    {
        int x;
        int y;

        public RationalFraction()
        { 
            //x = 0; y = 0;
        }
        public RationalFraction(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
        public void Reduce()
        { /*надо найти наибольший общий делитель - переменная nod, 
          когда он нашёлся, числитель и знаменатель делятся на него*/
            int ch;
            int nod = 1;
            if (x > y) ch = x;
            else ch = y;

            for (int i = 2; i < ch / 2; i++)
            {
                if (x % i == 0 && y % i == 0)
                {
                    nod = i;
                }
            }
            x /= nod;
            y /= nod;
        }
        public RationalFraction Add(RationalFraction d)
        {
            return new RationalFraction((x * d.y + y * d.x), (y * d.y));
        }
        public void Add2(RationalFraction d)
        {
            x = x * d.y + y * d.x;
            y = y * d.y;
        }
        public RationalFraction Sub(RationalFraction d)
        {
            return new RationalFraction((x * d.y - y * d.x), (y * d.y));
        }
        public void Sub2(RationalFraction d)
        {
            x = x * d.y - y * d.x;
            y = y * d.y;
        }
        public RationalFraction Mult(RationalFraction d)
        {
            return new RationalFraction(x * d.x, y * d.y);
        }
        public void Mult2(RationalFraction d)
        {
            x *= d.x;
            y *= d.y;
        }
        public RationalFraction Div(RationalFraction d)
        {
            return new RationalFraction((x * d.y), (y * d.x));
        }
        public void Div2(RationalFraction d)
        {
            x = x * d.y;
            y = y * d.x;
        }
        public override string ToString()
        {
            return x + "/" + y;
        }
        public double Value()
        {
            double res;
            res = (double)x / y;
            return res;
        }
        public bool Equals(RationalFraction d)
        {
            if (x == d.x && y == d.y) return true;
            else return false;
        }
        public int NumberPart()
        {
            if (x / y > 0) return (x / y);
            else return 0;
        }
    }
}
