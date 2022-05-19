using System;
using System.Collections.Generic;
using System.Text;

namespace Lab_17
{
    class StudentEkz : IComparable
    {
        string Surname;
        string Name;
        string Patronymic;
        protected int Group;
        int One, Two, Three;
        public StudentEkz(string surname, string name, string patronymic, int group, int one, int two, int three)
        {
            this.Surname = surname;
            this.Name = name;
            this.Patronymic = patronymic;
            this.Group = group;
            this.One = one;
            this.Two = two;
            this.Three = three;
        }
        public int CompareTo(object obj) //сортирует учеников по номеру их группы
        {
            StudentEkz s = (StudentEkz)obj;
            int a;
            if (Group > s.Group) a = 1;
            else if (Group == s.Group) a = 0;
            else a = -1;
            return a;
        }
        public bool Session()
        {
            if ((One > 3) || (Two > 3) || (Three > 3)) return true;
            else return false;
        }
        public override string ToString()
        {
            return (Surname + " " + Name + " " + Patronymic + " " + Group + " " + One + " " + Two + " " + Three);
        }
    }
}
