using System;

namespace lesson07._10
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                int a = Convert.ToInt32(Console.ReadLine());
                int b = Convert.ToDouble(Console.ReadLine());
            } 
            catch (Exeption e)      //здесь содержатся сведения об ошибке, либо просто catch, может отсутствовать
            {
                Console.WriteLine("Число введено неверно"+e.ToString);
                                                        //(e.Message)
                                                        //(e.ShowMessage)    //обработка ошибки
                return; //остановить программу - выход из метода 
            }
            finally //корректное завершение всех ..., может отсутствовать (но д.б. либо catch либо finally)
            {
                //независимо от того, была ошибка или нет, надо что-то делать
            }
        }
    }
}
