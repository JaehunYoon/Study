using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace test
{
    class Calculator
    {
        static void Main(string[] args)
        {
            while (true)
            {              
                Console.Write("Calc >> ");
                string formula = Console.ReadLine();
                Console.WriteLine(formula);

                string[] split_formula = formula.Split(' ');

                for (int i = 0; i < split_formula.Length; i++)
                    Console.WriteLine(split_formula[i]);
            }
        }
    }
}
