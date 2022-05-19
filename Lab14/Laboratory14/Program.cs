using System;

namespace Laboratory14
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Введите номер задания");
            int number = int.Parse(Console.ReadLine());

            if (number == 1)
            {
                Console.WriteLine("Введите размер массива");
                int n = int.Parse(Console.ReadLine());
                Figure[] mas = new Figure[n];
                string aa = "Rectangle"; string bb = "Circle"; string cc = "Triangle";
                for (int i = 0; i<n; ++i)
                {
                    Console.WriteLine();
                    Console.WriteLine("Введите название фигуры");
                    string figure = Console.ReadLine();
                    if (figure == aa)
                    {
                        mas[i] = new Rectangle();
                        mas[i].Print();
                        Console.WriteLine($"Периметр прямоугольника = {mas[i].Perimetr()}");
                        Console.WriteLine($"Площадь прямоугольника = {mas[i].Square()}");
                    }
                    if (figure == bb)
                    {
                        mas[i] = new Circle();
                        mas[i].Print();
                        Console.WriteLine($"Периметр круга = {mas[i].Perimetr()}");
                        Console.WriteLine($"Площадь круга = {mas[i].Square()}");
                    }
                    if (figure == cc)
                    {
                        mas[i] = new Triangle();
                        mas[i].Print();
                        Console.WriteLine($"Периметр треугольника = {mas[i].Perimetr()}");
                        Console.WriteLine($"Площадь треугольника = {mas[i].Square()}");
                    }
                }
            }
            if (number == 2)
            {
                Function[] func = new Function[5];
                func[0] = new Line(2, 3);
                func[1] = new Kub(3, 4, -6);
                func[2] = new Hyperbola(3, -4);
                func[3] = new Kub(2, 3, -1);
                func[4] = new Line(4, -2);

                for (int i = 0; i<5; i++)
                {
                    func[i].Print();
                    Console.WriteLine("Значение данной функции в точке x = " + func[i].Value());
                    Console.WriteLine();
                }
            }
            if (number == 3)
            {
                string aa = "Book", bb = "Article", cc = "Resource";
                Console.WriteLine("Введите размер массива");
                int n = int.Parse(Console.ReadLine());                
                Edition[] ed = new Edition[n];
                for (int i = 0; i<n; i++)
                {
                    Console.WriteLine();
                    Console.WriteLine("Введите название того, что вы будете искать: Book, Article или Resource");
                    string poisk = Console.ReadLine();
                    if (poisk == aa)
                    {
                        ed[i] = new Book();
                        Console.WriteLine("Введите информацию о книге");
                        Console.WriteLine();
                        ed[i].Info();
                        //поиск изданий по фамилии автора
                        ed[i].Desired();

                    }
                    if (poisk == bb)
                    {
                        ed[i] = new Article();
                        Console.WriteLine("Введите информацию о статье: ");
                        Console.WriteLine();
                        ed[i].Info();
                        ed[i].Desired();

                    }
                    if (poisk == cc)
                    {
                        ed[i] = new Resource();
                        Console.WriteLine("Введите информацию об электронном ресурсе");
                        Console.WriteLine();
                        ed[i].Info();
                        ed[i].Desired();
                    }
                }
            }  
        }
    }
}
