using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Grades
{
    public class NameChangedEventArgs : EventArgs
    {
        public NameChangedEventArgs(String oldName, String newName)
        {
            this.OldName = oldName;
            this.NewName = newName;
        }

        public String OldName { get; set; }
        public String NewName { get; set; }
    }
}
