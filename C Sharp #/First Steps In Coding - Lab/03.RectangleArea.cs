﻿using System;
using System.Dynamic;

namespace _03.RectangleArea
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int side1 = int.Parse(Console.ReadLine());
            int side2 = int.Parse(Console.ReadLine());
            int area = side1 * side2;
            Console.WriteLine(area);
        }
    }
}
