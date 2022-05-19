/*
 * @author Usmanova Aigul
 * 11912
 * Task_31
 */
using System;

namespace Task_31
{  //проверить что в каждом двумерном массиве есть такая строка, что все элементы делятся на три
    class Program
    {
        static void Input(int[,,] Trimas, int x, int n, int m)
        {
            for (int k = 0; k < x; k++)
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < m; j++)
                    {
                        Trimas[k, i, j] = Convert.ToInt32(Console.ReadLine());
                    }
                }
                Console.WriteLine(" ");
            }
        }
        static void Proverka(int[,,] Trimas, int x, int n, int m)
        {
            int[,] Dvamas = new int[n, m];

            int sum = 0;
            int prov = 0;
            int prov1 = 0;
            int R;                  //переменная будет брать на себя значение элементов трёхмерного массива и присваивать их 0-му, потом 1-му и т.д. двумерным массивам
            Console.WriteLine(" ");
            for (int k = 0; k < x; k++)
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < m; j++)
                    {
                        R = Trimas[k, i, j];
                        Dvamas[i, j] = R;    //завожу двумерный массив, с которым буду работать в трёхмерном массиве
                        if ((R % 3) == 0) sum++;
                    }

                    if (sum == m)        //значит в этой строке двумерного массива все элементы делятя на 3, поэтому 
                                         //мы можем переходить к следующему массиву
                        prov++;
                    sum = 0;
                }
                if (prov > 0)           //значит что в массиве есть строка в которой все элементы делятся на 3
                {
                    prov1++;        //увеличиваю на 1, чтобы сделать проверку после выполнения всего цикла
                    prov = 0;       //обнуляю, чтобы использовать эту переменную и при проверки остальных массивов
                }
            }
            if (prov1 == x)     //если значение prov1 стало равно количеству двумерных массивов, то в каждом массиве есть
                                //такая строка, в которой все элементы делятся на 3
                Console.WriteLine("В каждом двумерном массиве есть такая строка, в которой все элементы делятся на 3.");
            else
                Console.WriteLine("Условие не выполнилось!");
        }

            static void Main()
            {
            int[, ,]Trimas  = new int[2,3,4];
            Input(Trimas, 2, 3, 4);
            Proverka(Trimas, 2, 3, 4); 
            Console.ReadKey();
            }
        }
}
