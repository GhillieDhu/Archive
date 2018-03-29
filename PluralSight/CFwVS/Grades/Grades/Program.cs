namespace Grades
{
    using System;

    class Program
    {
        static void Main(string[] args)
        {
            GradeBook book = new ThrowawayGradeBook();
            book.AddGrade(91);
            book.AddGrade(89.5);
            book.AddGrade(75);

            book.NameChanged += Herpa;
            book.NameChanged += Derpa;

            book.Name = "I hate static typing";

            GradeStatistics stats = book.ComputeStatistics();
            stats.DisplayStats();

            Int32 goofus = 32;
            WriteResult("Derp", goofus);
        }

        static void WriteResult(String description, Double result)
        {
            Console.WriteLine($"{description}: {result:P0} {result:F7}"); //String interpolation + formatting
        }

        static void Herpa(object sender, NameChangedEventArgs args)
        {
            Console.WriteLine($"{args.OldName}");
        }

        static void Derpa(object sender, NameChangedEventArgs args)
        {
            Console.WriteLine($"{args.NewName}");
        }
    }
}
