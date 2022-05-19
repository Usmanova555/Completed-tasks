using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    class Resource : Edition//электронный ресурс
    {
        public string Name;
        public string LastName;
        public string Link; //ссылка
        public string Annotation;
        public Resource(string name, string lastName, string link, string annotation)
        {
            this.Name = name;
            this.LastName = lastName;
            this.Link = link;
            this.Annotation = annotation;
        }
        public Resource()
        {

        }
        public override void Info()
        {
            Console.WriteLine("Введите название электронного ресурса");
            Name = Console.ReadLine();
            Console.WriteLine("Введите фамилию автора");
            LastName = Console.ReadLine();
            Console.WriteLine("Введите ссылку на электронный ресурс");
            Link = Console.ReadLine();
            Console.WriteLine("Введите аннотацию");
            Annotation = Console.ReadLine();
        }
        public override void Desired(string LASTName)
        {
            if (LastName == LASTName) Console.WriteLine($"Данное издание принадлежит автору: {LastName}");
        }
    }
}
