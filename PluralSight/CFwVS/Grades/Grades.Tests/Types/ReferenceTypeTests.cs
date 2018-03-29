using Microsoft.VisualStudio.TestTools.UnitTesting;
namespace Grades.Tests.Types
{
    using System;
    using Microsoft.VisualStudio.TestTools.UnitTesting;

    [TestClass]
    public class ReferenceTypeTests
    {
        [TestMethod]
        public void WrappedPrimitives()
        {
            Int32 x1 = 4;
            Double x2 = 4.1234;
            Double x3 = x1;
            Assert.AreEqual(x1, x3);
            x3 = x2;
            Assert.AreEqual(x2, x3);
        }

        [TestMethod]
        public void MyTestMethod()
        {
            String name = "maRk".ToUpper();
            Assert.AreEqual(name, "Mark");
        }
    }
}
