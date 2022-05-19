using System;
using System.Collections.Generic;
using System.Text;

namespace classPerson
{
    class Worker : Person
    {
        public int Oklad { get; protected set; }
        public int Premium { get; protected set; }

        private int yearsOfWork; 
        public int YearsOfWork
        {
            get
            {
                return yearsOfWork;
            }
            private set
            {
                if (value >= 0)
                    yearsOfWork = value;
                else Console.WriteLine("Такого стажа работы не существует");
            }
        }

        public Worker(string lastName, string name, string age, char Gender, int Oklad, int Premium, int YearsOfWork) : base(lastName, name, age, Gender)
        {
            this.Oklad = Oklad;
            this.Premium = Premium;
            this.YearsOfWork = YearsOfWork;
        }
        public Worker() : base()
        {
            Oklad = 0;
            Premium = 0;
            YearsOfWork = 0;
        }
        public override void Read()
        {
            base.Read();
            Console.WriteLine("Введите фиксированную зарплату");
            Oklad = int.Parse(Console.ReadLine());

            Console.WriteLine("Введите размер премии в %");
            Premium = int.Parse(Console.ReadLine());

            Console.WriteLine("Введите стаж работы работника");
            YearsOfWork = int.Parse(Console.ReadLine());
            Console.WriteLine();
        }
        public override void Print()
        {
            base.Print();
            Console.WriteLine("Зарплата " + Oklad);
            Console.WriteLine("{0}% премии" + Premium);
            Console.WriteLine("Стаж работы " + YearsOfWork);
        }
        public virtual double SumSalary() //оклад + премия
        {
            return ((1 + (double)Premium / 100) * Oklad);
        }
        public double IncomeTax() //расчёт подоходного налога
        {
            return SumSalary() * 0.13;
        }
        public void SumPremium() 
        {
            if (YearsOfWork > 10) Premium *= 2;
        }
        public double TotalSalary() //общая сумма
        {
            return SumSalary() - IncomeTax();
        }
    }
}
