using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    abstract class Edition
    {
        abstract public void Info();
        abstract public void Desired(string LASTName="Коргачёв"); //искомое ли издание?
    }
}
