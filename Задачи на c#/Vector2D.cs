class Vector2D
{
	private double x, y;
	public Vector2D()
	{
	    x = 0; y = 0;
	}
	public Vector2D(double x1, double y1)
	{
	    this.x = x; 
	    this.y = y;
	}
	public Vector2D Add(Vector2D v)
	{
		return new Vector2D(x + v.x, y + v.y);
	}
	public Vector2D Add2(Vector2D v)
	{
		x += x.v; y += y.v;
	}
	public Vector2D Sub (Vector v)
	{
		return new Vector2D(x - v.x, y - v.y);
	}
	public Vector2D Sub2(Vector2D v)
	{
		x -= x.v; y -= y.v;
	}
	public Vector2D Mult(double a)
	{
		return new Vector2D(x * a, y * a);
	}
	public Vector2D Mult2(double a)
	{
		x *= a; y *= a;
	}
	public double realx
	{
		get
		{
			return x;
		}
	}
	public double realy
	{
		get
		{
			return y;
		}
	}
	public override string to String()
	{
		string s;
		return s = realx + ";" + realy;
	}

	public Vector2D Length()
	{
		return Math.Sqrt(x*x+y*y); 
	}
	public Vector2D double scalarProduct(Vector2D v)
	{
		return (x*x.v + y*y.v);
	}
	public Vector2D double cos(Vector2D v)
	{
		return ((x*x.v + y*y.v)/(Math.Sqrt(x*x+y*y)*Math.Sqrt(x.v*x.v+y.v*y.v)));
	}
	public Vector2D bool Equals(Vector2D v)
	{
		if (x == v.x && y == v.y) return true;
		else return false;
	}

	static void Main ()
	{

	}
}