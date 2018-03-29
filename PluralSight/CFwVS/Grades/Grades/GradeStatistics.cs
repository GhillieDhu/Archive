using System;
using System.Collections;

namespace Grades
{
    public class GradeStatistics
    {
        public GradeStatistics(GradeBook book)
        {
            this.HighestGrade = Double.MinValue;
            this.LowestGrade = Double.MaxValue;
            this.AverageGrade = 0;
            IEnumerable grades = book.GetGrades();
            //this.HighestGrade = 
            Int32 count = 0;
            foreach (Double grade in grades)
            {
                this.HighestGrade = Math.Max(this.HighestGrade, grade);
                this.LowestGrade = Math.Min(this.LowestGrade, grade);
                this.AverageGrade += grade;
                count++;
            }
            this.AverageGrade /= count;
        }

        internal void DisplayStats()
        {
            Console.WriteLine(this.HighestGrade);
            Console.WriteLine(this.AverageGrade);
            Console.WriteLine(this.LowestGrade);
        }

        public Char LetterGrade
        {
            get
            {
                Char result;
                if (AverageGrade >= 60)
                {
                    if (AverageGrade >= 70)
                    {
                        if (AverageGrade >= 80)
                        {
                            if (AverageGrade >= 90)
                            {
                                result = 'A';
                            }
                            else {
                                result = 'B';
                            }
                        }
                        else {
                            result = 'C';
                        }
                    }
                    else {
                        result = 'D';
                    }
                }
                else {
                    result = 'F';
                }
                return result;
            }
        }

        Double HighestGrade;
        Double LowestGrade;
        Double AverageGrade;
    }
}