using System;

namespace _07.AreaofFigures
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string figure = Console.ReadLine();
            

            if (figure == "square")
            {
                double side = double.Parse(Console.ReadLine());
                double area = side * side;
                Console.WriteLine("{0:F3}", area);
            }
            else if (figure == "rectangle")
            {
                double side1 = double.Parse((Console.ReadLine()));
                double side2 = double.Parse((Console.ReadLine()));
                double area = side1 * side2;
                Console.WriteLine("{0:F3}", area);
            }
            else if (figure == "circle")
            {
                double diameter = double.Parse((Console.ReadLine()));
                double area = diameter * diameter * Math.PI;
                Console.WriteLine("{0:F3}", area);
            }
            else if (figure == "triangle")
            {
                double side = double.Parse(Console.ReadLine());
                double high = double.Parse(Console.ReadLine());
                double area = side * high / 2;
                Console.WriteLine("{0:F3}", area);
            }
            
        }
    }
}
