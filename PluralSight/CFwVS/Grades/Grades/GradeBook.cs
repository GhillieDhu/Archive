using System;
using System.Collections;
using System.Collections.Generic;

namespace Grades
{
    public class GradeBook : IEnumerable
    {

        public GradeBook()
        {
            this.grades = new List<Double>();
        }

        public List<Double> GetGrades()
        {
            return this.grades;
        }

        public void AddGrade(Double grade)
        {
            this.grades.Add(grade);
        }

        public virtual GradeStatistics ComputeStatistics()
        {
            GradeStatistics stats = new GradeStatistics(this);
            return stats;
        }

        public IEnumerator GetEnumerator()
        {
            return grades.GetEnumerator();
        }

        private List<Double> grades;

        private String _name = "Unnamed";

        public String Name
        {
            get
            {
                return _name;
            }
            set
            {
                NameChanged(this, new NameChangedEventArgs(_name, value));
                _name = value;
            }
        }

        public event NameChangedDelegate NameChanged;
    }
}
