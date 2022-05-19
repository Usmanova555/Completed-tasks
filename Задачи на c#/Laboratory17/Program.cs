using System;
using System.IO;

namespace Lab_17
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Задание №1");
            Console.WriteLine("Введите название оконченной школы");
            string school = Console.ReadLine();
            StreamReader In = new StreamReader("Input.txt");
            StreamWriter Out = new StreamWriter("Output.txt");
            int n = File.ReadAllLines("Input.txt").Length;
            int c = 0;
            Student[] students = new Student[n];
            while (!In.EndOfStream)
            {
                string s = In.ReadLine();
                string[] mas = s.Split(' ');
                if (mas.Length > 5)
                {
                    for (int i = 6; i < mas.Length; i++)
                    {
                        mas[5] = mas[5] + " " + mas[i];
                    }
                }
                students[c] = new Student(mas[0], mas[1], mas[2], mas[3], mas[4], mas[5]);
                c++;
            }
            In.Close();
            for (int i = 0; i<students.Length-1; i++)
            {
                if (students[i].CompareTo(students[i+1]) == -1)
                {
                    Student w = students[i + 1];
                    students[i + 1] = students[i];
                    students[i] = w;
                }
            }
            foreach (Student m in students)
            {
                if (m.WhichSchool(school))
                {
                    Out.WriteLine(m.ToString(), true);
                }
            }
            Out.Close();

            Console.WriteLine("");
            Console.WriteLine("Задание №2");
            StreamReader In1 = new StreamReader("Input1.txt");
            StreamWriter Out1 = new StreamWriter("Output1.txt");
            c = 0;
            n = File.ReadAllLines("Input.txt").Length;
            StudentEkz[] studentEkz = new StudentEkz[n];
            while (!In1.EndOfStream)
            {
                string s = In1.ReadLine();
                string[] mas = s.Split(' ');
                studentEkz[c] = new StudentEkz(mas[0], mas[1], mas[2], int.Parse(mas[3]), int.Parse(mas[4]), int.Parse(mas[5]), int.Parse(mas[6]));
                c++;
            }
            In1.Close();
            for (int i = 0; i < studentEkz.Length - 1; i++)
            {
                if (studentEkz[i].CompareTo(studentEkz[i + 1]) == -1)
                {
                    StudentEkz w = studentEkz[i + 1];
                    studentEkz[i + 1] = studentEkz[i];
                    studentEkz[i] = w;
                }
                else if (studentEkz[i].CompareTo(studentEkz[i + 1]) == -1)
                {

                }
            }
            foreach (StudentEkz m in studentEkz)
            {
                if (m.Session())
                {
                    Out1.WriteLine(m.ToString(), true);
                }
            }
            Out1.Close();
        }
    }
}
