/*
 * @author Usmanova Aigul
 * 11912
 * Task_40
 */
using System;

namespace ConsoleApp7
{
    class Program
    {
        static void Main()
        {
            string str = "Does Maria live in the - Village?";

            //появится массив с элементами слов этого предложения
            bool prov;
            int ctr = 0;
            foreach (string item in str.Split(new char[] { ' ', '-', ',', '.', '!', '?'}, StringSplitOptions.RemoveEmptyEntries))
            {
                prov = false;
                foreach (char ch in item)
                    if (ch >= 'A' && ch <= 'Z')
                        prov = true;
                if (prov) ctr++;
            }
            Console.WriteLine("Количество слов, которые начинаются на заглавную английскую буквы: ");
            Console.WriteLine(ctr);
        }
    }
}
