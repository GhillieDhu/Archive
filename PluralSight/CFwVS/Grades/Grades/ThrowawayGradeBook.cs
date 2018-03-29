using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Grades
{
    public class ThrowawayGradeBook : GradeBook
    {
        public override GradeStatistics ComputeStatistics()
        {
            Double LowestGrade = Double.MaxValue;
            foreach (Double grade in this)
            {
                LowestGrade = Math.Min(LowestGrade, grade);
            }
            this.Remove(LowestGrade);
            return base.ComputeStatistics();
        }
    }
}
