using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    class Rational
    {
        public Rational(int numerator, int denumenator)
        {
            int g = Rational.Ged(numerator, denumenator);
            if (numerator / g > 0 && denumenator / g < 0)
            {
                Numerator = (numerator / g) * (-1);
                Denumenator = (denumenator / g) * (-1);
            }
            else
            {
                Numerator = numerator / g;
                Denumenator = denumenator / g;
            }
        }
        public int Numerator { get; set; }
        public int Denumenator { get; set; }
        public override String ToString()
        {
            return String.Format("{0}/{1}", this.Numerator, this.Denumenator);
        }
        public static Rational operator +(Rational r1, Rational r2)
        {
            return new Rational(r1.Numerator * r2.Denumenator + r2.Numerator * r1.Denumenator,
                r1.Denumenator * r2.Denumenator);
        }
        public static Rational operator -(Rational r1, Rational r2)
        {
            return new Rational(r1.Numerator * r2.Denumenator - r2.Numerator * r1.Denumenator,
                r1.Denumenator * r2.Denumenator);
        }
        public static Rational operator *(Rational r1, Rational r2)
        {
            return new Rational(r1.Numerator * r2.Numerator, r1.Denumenator * r2.Denumenator);
        }
        public static Rational operator /(Rational r1, Rational r2)
        {
            return new Rational(r1.Numerator * r2.Denumenator, r1.Denumenator * r2.Numerator);
        }
        protected static int Ged(int x, int y)
        {
            while (x * y != 0)
            {
                if (Math.Abs(x) > Math.Abs(y))
                {
                    x = x % y;
                }
                else
                {
                    y = y % x;
                }
            }
            return x + y;
        }
    }
    class OneBasedArray<T>
    {
        private T[] data;
        public OneBasedArray(T[] data)
        {
            this.data = data;
        }
        public int Length { get { return data.Length; } }
        public T[] ToArray()
        {
            return data;
        }
        public T this[int index]
        {
            get
            {
                return data[index - 1];
            }
            set
            {
                data[index - 1] = value;
            }
        }
    }
    
    class Matrix<T>
    {
        //Matrix(int m, int n)
        //{

        //}
        //Matrix(int[,] data)
        //{

        //}
        //int RawCount
        //int ColumnCount
        //operator +(Matrix m1, Matrix m2)
        //operator *(Matrix m1, Matrix m2)
        //operator *(Matrix m1, T c) //умножение на скаляр
        //ToString() //преобразует матрицу в строку например, "1 2 3 \n 4 5 6 \n 7 8 9"
        ////throw new Arangement Exeprion вызов исключения, например, если размеры не совпадают или еще что-то
        ///this[int r, int c]

        private T[,] data;
        public Matrix(T[,] data)
        {
            this.data = data;
        }
        public Matrix(int m, int n)
        {
            this.data = new T[m, n];
        }
        public string Tostring()
        {
            try
            {
                string text = "";
                for (int i = 0; i < this.RawCount; i++)
                {
                    for (int j = 0; j < this.ColumnCount; j++)
                    {
                        text = text + Convert.ToString(this[i, j]) + " ";
                    }
                    text = text + "\n";
                }
                return text;
            }
            catch
            {
                throw new Exception("Wrong!");
            }
        }
        public T this[int iindex, int jindex]
        {
            get
            {
                return data[iindex, jindex];
            }
            set
            {
                data[iindex, jindex] = value;
            }
        }
        public int RawCount { get { return data.GetUpperBound(0) + 1; } }
        public int ColumnCount { get { return data.Length/RawCount; } }
        public static dynamic Sum(dynamic a, dynamic b)
        {
            return a + b;
        }
        public static dynamic Multiplication(dynamic a, dynamic b)
        {
            return a * b;
        }
        public static Matrix<T> operator +(Matrix<T> matr1, Matrix<T> matr2)
        {
            Matrix<T> matr3 = new Matrix<T>(matr1.RawCount,matr1.ColumnCount);
            try
            {
                for (int i = 0; i < matr1.RawCount; i++)
                {
                    for (int j = 0; j < matr1.ColumnCount; j++)
                    {
                        matr3[i, j] = Sum(matr1[i, j], matr2[i, j]);
                    }
                }
                return matr3;
            }
            catch
            {
                throw new Exception("Wrong summation array!!!");
            }
        }
        public static Matrix<T> operator *(Matrix<T> matr1, Matrix<T> matr2)
        {
            Matrix<T> matr3 = new Matrix<T>(matr1.RawCount, matr2.ColumnCount);
            //if (matr1.ColumnCount!=matr2.RawCount)
            //{
            //    throw new Exception("Wrong!!!");
            //}
            try
            {
                if (matr1.ColumnCount != matr2.RawCount)
                {
                    throw new Exception("Wrong!!!");
                }
                for (int i = 0; i < matr3.RawCount; i++)
                {
                    for (int j = 0; j < matr3.ColumnCount; j++)
                    {
                        for (int q = 0; q < matr2.RawCount; q++)
                        {
                            matr3[i, j] = Sum(matr3[i, j], Multiplication(matr1[i, q], matr2[q, j]));
                        }
                    }
                }
                return matr3;
            }
            catch
            {
                throw new Exception("Wrong multiolication array!!!");
            }
        }
        public static Matrix<T> operator *(Matrix<T> matr, T c)
        {
            try
            {
                for (int i = 0; i < matr.RawCount; i++)
                {
                    for (int j = 0; j < matr.ColumnCount; j++)
                    {
                        matr[i, j] = Multiplication(matr[i,j],c);
                    }
                }
                return matr;
            }
            catch
            {
                throw new Exception("Wrong multiplication on scalar!!!");
            }
        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            //Rational r1 = new Rational(1, 2);
            //Rational r2 = new Rational(3, 4);
            //Rational r3 = r1 + r2;
            //Rational r4 = r1 - r2;
            //Rational r5 = r1 * r2;
            //Rational r6 = r1 / r2;
            //Console.WriteLine(r3);
            //Console.WriteLine(r4);
            //Console.WriteLine(r5);
            //Console.WriteLine(r6+"\n");

            //int[] a = new int[] { 1, 2, 3, 4, 5 };
            //OneBasedArray<int> x = new OneBasedArray<int>(a);
            //Console.WriteLine(x[3]);
            //x[3] = 56;
            //Console.WriteLine(x[3]+"\n");

            int[,] b = new int[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 }, { 10, 11, 12 } };
            int[,] c = new int[,] { { 2, 4, 6 }, { 8, 10, 12 }, { 14, 16, 18 }, { 20, 22, 24} };
            int[,] d = new int[,] { { 1, 2, 3, 4 }, { 5, 6, 7, 8 } };
            Matrix<int> y = new Matrix<int>(b);
            Matrix<int> z = new Matrix<int>(c);
            Matrix<int> x = new Matrix<int>(d);
            Console.WriteLine("Raws = " + y.RawCount + "\nColumns = " + y.ColumnCount);
            Console.WriteLine("Print first array\n" + y.Tostring());
            Console.WriteLine("Print second array\n" + z.Tostring());
            Console.WriteLine("Print third array\n" + x.Tostring());
            Matrix<int> matr3 = y + z;
            Console.WriteLine("Summation array\n" + matr3.Tostring());
            matr3 = matr3 * 4;
            Console.WriteLine("Multiplication on scalar\n" + matr3.Tostring());
            matr3 = x * y;
            Console.WriteLine("Multiplication array\n" + matr3.Tostring());
        }
    }
}
//реализовать матрицу