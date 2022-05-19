using System;

namespace vector2d
{
    class Vector2D
    {
        double x, y;
        public Vector2D()
        {
            x = 0; y = 0;
        }
        public Vector2D(double x1, double y1)
        {
            x = x1;
            y = y1;
        }
        public Vector2D Add(Vector2D v)
        {
            return new Vector2D(x + v.x, y + v.y);
        }
        public void Add2(Vector2D v)
        {
            x += v.x; y += v.y;
        }
        public Vector2D Sub(Vector2D v)
        {
            return new Vector2D(x - v.x, y - v.y);
        }
        public void Sub2(Vector2D v)
        {
            x -= v.x; y -= v.y;
        }
        public Vector2D Mult(double a)
        {
            return new Vector2D(x * a, y * a);
        }
        public void Mult2(double a)
        {
            x *= a; y *= a;
        }
        public override string ToString()
        {
            return x + "/" + y;
        }
        public double Length()
        {
            return Math.Sqrt(x * x + y * y);
        }
        public double ScalarProduct(Vector2D v)
        {
            return (x * v.x + y * v.y);
        }
        public double Cos(Vector2D v)
        {
            return ((x * v.x + y * v.y) / (Math.Sqrt(x * x + v.x * v.x) * Math.Sqrt(y * y + v.y * v.y)));
        }
        public bool Equals(Vector2D v)
        {
            if (x == v.x && y == v.y) return true;
            else return false;
        }
    }
}
