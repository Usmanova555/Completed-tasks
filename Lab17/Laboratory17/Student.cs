using System;
using System.Collections.Generic;
using System.Text;

namespace Lab_17
{
    class Student
    {
        string Surname;
        string Name;
        string Patronymic;
        protected DateTime Age;
        string Sity;
        string School;
        public Student(string surname, string name, string patronymic, string age, string sity, string school)
        {
            this.Surname = surname;
            this.Name = name;
            this.Patronymic = patronymic;
            this.Age = DateTime.Parse(age);
            this.Sity = sity;
            this.School = school;
        }
        public int CompareTo(object obj) //сортирует учеников по их году рождения
        {
            Student s = (Student)obj;
            int a;
            if (Age > s.Age) a = 1;
            else if (Age == s.Age) a = 0;
            else a = -1;
            return a;
        }
        public bool WhichSchool(string f)
        {
            if (School == f) return true;
            else return false;
        }
        public override string ToString()
        {
            return (Surname + " " + Name + " " + Patronymic + " " + Age + " " + Sity + " " + School);

        }   
    }
}
