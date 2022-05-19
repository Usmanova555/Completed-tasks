/*
 * @author Usmanova Aigul
 * 11911
 * RationalFunction class
 */

using System;

namespace RationalFraction
{
    class RationalFunction
    {
        static void Main()
        {
            RationalFraction d1 = new RationalFraction(4, 6);
            RationalFraction d2 = new RationalFraction(2, 4);
            //выводит на экран дроби d1 и d2
            Console.WriteLine("d1: " + d1.ToString());
            Console.WriteLine("d2: " + d2.ToString());

            Console.WriteLine("");

            RationalFraction d3 = d1.Add(d2);
            d3.Reduce(); //сокращает дробь с суммой
            Console.WriteLine("Сумма двух дробей " + d3.ToString());

            RationalFraction d4 = d1.Sub(d2);
            d4.Reduce(); //сокращает дробь с разностью
            Console.WriteLine("Разность двух дробей " + d4.ToString());

            Console.WriteLine("");

            d1.Add2(d2);
            d1.Reduce();
            Console.WriteLine("Изменённое d1 (сумма двух дробей): " + d1.ToString());

            d1.Sub2(d2);
            d1.Reduce();
            Console.WriteLine("Изменённое d1 (разность двух дробей): " + d1.ToString());

            Console.WriteLine("");

            RationalFraction dd = new RationalFraction(3, 4);
            RationalFraction ss = new RationalFraction(5, -6);
            Console.WriteLine("Новый объект dd: " + dd);
            Console.WriteLine("Новый объект ss: " + ss);

            Console.WriteLine("");

            RationalFraction d5 = dd.Mult(ss);
            d5.Reduce();
            Console.WriteLine("Произведение: " + d5);

            RationalFraction d6 = dd.Div(ss);
            d6.Reduce();
            Console.WriteLine("Деление: " + d6);

            Console.WriteLine("");

            dd.Mult2(ss);
            dd.Reduce();
            Console.WriteLine("Новое произведение, результат записывается в dd: " + dd);

            dd.Div2(ss);
            dd.Reduce();
            Console.WriteLine("Новое частное, результат записывается в dd: " + dd);

            Console.WriteLine("");

            Console.WriteLine($"Строковое представление дробей dd: {dd.Value()}, ss: {ss.Value()}");

            Console.WriteLine("");

            Console.WriteLine("Дроби равны? " + dd.Equals(ss));
            /*на данном этапе объекты dd и ss уже будут сокращены, поэтому сокращать их нет смысла
             * но можно создать новые объекты и наих примере посмотреть как сокращать дроби перед их сравнением, например:*/
            Console.WriteLine("");

            RationalFraction bool1 = new RationalFraction(2, -33);
            bool1.Reduce();
            RationalFraction bool2 = new RationalFraction(2, -33);
            bool2.Reduce();
            Console.WriteLine("bool1: " + bool1.ToString());
            Console.WriteLine("bool2: " + bool2.ToString());

            Console.WriteLine("");

            Console.WriteLine("Дроби равны? " + bool1.Equals(bool2));

            Console.WriteLine("");

            Console.WriteLine("Целая часть, а при её отсутствии 0: " + dd.NumberPart());
        }
    }
}