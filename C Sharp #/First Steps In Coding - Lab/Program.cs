﻿using System;

namespace _08.PetShop
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double dogPrice = 2.50;
            int catPrice = 4;
            int numberOfDogFood = int.Parse(Console.ReadLine());
            int numberOFCatFood = int.Parse(Console.ReadLine());
            double dogMoney = numberOfDogFood * dogPrice;
            int catMoney = numberOFCatFood * catPrice;
            double finalPrice = dogMoney + catMoney;

            Console.WriteLine($"{finalPrice} lv.");
        }
    }
}
