using System;

namespace _04.InchesToCentimeters
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double centimeters = double.Parse(Console.ReadLine());
            double intches = centimeters * 2.54;
            Console.WriteLine(intches);
        }
    }
}
