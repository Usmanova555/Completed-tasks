/*
 * @author Usmanova Aigul
 * 11912
 * Task_43
 */
using System;

namespace mom_to_dad
{
    class Program
    {
        static void Main(string[] args)
        {
            //замена слова mom на dad
            string s = "avtomat mom hello mom fff";
            int n = s.Length;
            char[] res = new char[n]; //его размер будет n потому что слова одинаковой длины
            int i = 0; int j = 0;
            int sost = 1;
            while (i < n)
            {
                switch (sost)
                {
                    case 1:
                        if (s[i] == 'm') sost = 3;

                        else if (s[i] == ' ')
                        {
                            sost = 2; res[j] = ' ';
                            j++;
                        }
                        else
                        {
                            res[j] = s[i]; sost = 2; j++;
                        }
                        break;

                    case 2:
                        if (s[i] == ' ')
                        {
                            res[j] = ' ';
                            j++;
                        }
                        else if (s[i] == 'm') sost = 3;
                        else
                        {
                            res[j] = s[i]; sost = 1;
                            j++;
                        }
                        break;

                    case 3:
                        if (s[i] == 'o') sost = 4;
                        else
                        {
                            sost = 1; res[j] = 'm'; res[j + 1] = s[i]; j += 2;
                        }
                        break;

                    case 4:
                        if (s[i] == 'm') sost = 5;
                        else
                        {
                            sost = 1; res[j] = 'm'; res[j + 1] = 'o'; res[j + 2] = s[i]; j += 3;
                        }
                        break;

                    case 5:
                        if ((s[i] == ' ') || (s[i] == '.') || (s[i] == '!') || (s[i] == '?') || (s[i] == ','))
                        {
                            res[j] = 'm'; res[j + 1] = 'o'; res[j + 2] = 'm'; res[j + 3] = s[i];
                            j += 4;
                            sost = 6;
                        }
                        else
                        {
                            res[j] = 'm'; res[j + 1] = 'o'; res[j + 2] = 'm'; j += 3;
                            sost = 1;
                        }
                        break;

                    case 6:
                        if (s[i] == ' ')
                        {
                            sost = 2;
                            res[j] = ' '; j++;
                        }
                        else if (s[i] == 'm') sost = 3;
                        else
                        {
                            res[j] = s[i]; j++;
                            sost = 1;
                        }
                        break;
                }
                i++;
            }
            for (int k = 0; k < n; k++)
            {
                Console.Write(res[k]);
            }
        }
    }
}
