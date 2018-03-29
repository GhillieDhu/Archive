using System;

namespace Hello
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Your name: ");
            String name = Console.ReadLine();

            Console.Write("How many hours of sleep did you get last night? ");
            Int32 hoursOfSleep = Int32.Parse(Console.ReadLine());

            Console.WriteLine("Hello, " + name);
            if (hoursOfSleep >= 8)
            {
                Console.WriteLine("You are well rested");
            }
            else
            {
                Console.WriteLine("You need more sleep");
            }
        }
    }
}
