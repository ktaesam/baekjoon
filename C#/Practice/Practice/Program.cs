using System;

namespace Practice
{
    public class Rectangle
    {
        /*Comment*/
        double length;
        double width;

        public void AcceptDetails()
        {
            length = 4.5;
            width = 3.5;
        }
        public double GetArea()
        {
            return length * width;
        }
        public void Display()
        {
            Console.WriteLine("L : {0}", length);
            Console.WriteLine("W : {0}", width);
            Console.WriteLine("A : {0}", GetArea());
        }
    }
    class ExcuteRectangle
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Rectangle r1 = new Rectangle();
            r1.AcceptDetails();
            r1.Display();

            Console.ReadKey();
        }
    }
}
