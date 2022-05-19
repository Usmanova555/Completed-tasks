using System;
using System.Collections.Generic;
using System.Text;

namespace classPerson
{
    class WorkerHours : Worker
    {
        public int Hours { get; private set; }
        public int HoursSalary { get; private set; }
        public WorkerHours(string lastName, string name, string age, char Gender, int oklad, int Premium, int YearsOfWork, int hours) : base(lastName, name, age, Gender, oklad, Premium, YearsOfWork)
        {
            Hours = hours;
            HoursSalary = Oklad;
            Oklad *= Hours;
        }
        public WorkerHours():base()
        {
            Hours = 0;
            HoursSalary = 0;
        }
        public new void Read()
        {
            base.Read();
            Console.WriteLine("Введите количество часов, которые проработал сотрудник ");
            Hours = int.Parse(Console.ReadLine());
            HoursSalary = Oklad;
            Oklad *= Hours;
        }
        public new void Print()
        {
            base.Print();
            Console.WriteLine("");
        }
    }
}
