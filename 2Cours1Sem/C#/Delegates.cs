using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace ConsoleApp6
{
    class Fridge
    {
        public double Volume { get; set; }
        public string Model { get; set; }
        public double Height { get; set; }
        public double Width { get; set; }
        public double Depth { get; set; }
    }
    class EvenText
    {
        static void refrenSolo()
        {
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Thread.Sleep(300);
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Thread.Sleep(300);
            Console.Beep(659, 300);
            Console.Beep(783, 300);
            Console.Beep(523, 300);
            Console.Beep(587, 300);
            Console.Beep(659, 300);
            Console.Beep(261, 300);
            Console.Beep(293, 300);
            Console.Beep(329, 300);
            Console.Beep(698, 300);
            Console.Beep(698, 300);
            Console.Beep(698, 300);
            Thread.Sleep(300);
            Console.Beep(698, 300);
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Thread.Sleep(300);
            Console.Beep(659, 300);
            Console.Beep(587, 300);
            Console.Beep(587, 300);
            Console.Beep(659, 300);
            Console.Beep(587, 300);
            Thread.Sleep(300);
            Console.Beep(783, 300);
            Thread.Sleep(300);
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Thread.Sleep(300);
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Thread.Sleep(300);
            Console.Beep(659, 300);
            Console.Beep(783, 300);
            Console.Beep(523, 300);
            Console.Beep(587, 300);
            Console.Beep(659, 300);
            Console.Beep(261, 300);
            Console.Beep(293, 300);
            Console.Beep(329, 300);
            Console.Beep(698, 300);
            Console.Beep(698, 300);
            Console.Beep(698, 300);
            Thread.Sleep(300);
            Console.Beep(698, 300);
            Console.Beep(659, 300);
            Console.Beep(659, 300);
            Thread.Sleep(300);
            Console.Beep(783, 300);
            Console.Beep(783, 300);
            Console.Beep(698, 300);
            Console.Beep(587, 300);
            Console.Beep(523, 600);
            Thread.Sleep(600);
        }
        static void coupleSolo()
        {
            Console.Beep(392, 300);
            Console.Beep(659, 300);
            Console.Beep(587, 300);
            Console.Beep(523, 300);
            Console.Beep(392, 600);
            Thread.Sleep(300 * 2);
            Console.Beep(392, 300);
            Console.Beep(659, 300);
            Console.Beep(587, 300);
            Console.Beep(523, 300);
            Console.Beep(440, 600);
            Thread.Sleep(600);
            Console.Beep(440, 300);
            Console.Beep(698, 300);
            Console.Beep(659, 300);
            Console.Beep(587, 300);
            Console.Beep(783, 600);
            Thread.Sleep(600);
            Console.Beep(880, 300);
            Console.Beep(880, 300);
            Console.Beep(783, 300);
            Console.Beep(622, 300);
            Console.Beep(659, 600);
            Thread.Sleep(600);
            Console.Beep(392, 300);
            Console.Beep(659, 300);
            Console.Beep(587, 300);
            Console.Beep(523, 300);
            Console.Beep(392, 600);
            Thread.Sleep(600);
            Console.Beep(392, 300);
            Console.Beep(659, 300);
            Console.Beep(587, 300);
            Console.Beep(523, 300);
            Console.Beep(440, 600);
            Thread.Sleep(600);
            Console.Beep(440, 300);
            Console.Beep(698, 300);
            Console.Beep(659, 300);
            Console.Beep(587, 300);
            Console.Beep(783, 600);
            Thread.Sleep(600);
            Console.Beep(880, 300);
            Console.Beep(783, 300);
            Console.Beep(698, 300);
            Console.Beep(587, 300);
            Console.Beep(523, 600);
            Thread.Sleep(600);
        }
        private static void MissionImpossible()
        {
            Console.Beep(784, 150);
            Thread.Sleep(300);
            Console.Beep(784, 150);
            Thread.Sleep(300);
            Console.Beep(932, 150);
            Thread.Sleep(150);
            Console.Beep(1047, 150);
            Thread.Sleep(150);
            Console.Beep(784, 150);
            Thread.Sleep(300);
            Console.Beep(784, 150);
            Thread.Sleep(300);
            Console.Beep(699, 150);
            Thread.Sleep(150);
            Console.Beep(740, 150);
            Thread.Sleep(150);
            Console.Beep(784, 150);
            Thread.Sleep(300);
            Console.Beep(784, 150);
            Thread.Sleep(300);
            Console.Beep(932, 150);
            Thread.Sleep(150);
            Console.Beep(1047, 150);
            Thread.Sleep(150);
            Console.Beep(784, 150);
            Thread.Sleep(300);
            Console.Beep(784, 150);
            Thread.Sleep(300);
            Console.Beep(699, 150);
            Thread.Sleep(150);
            Console.Beep(740, 150);
            Thread.Sleep(150);
            Console.Beep(932, 150);
            Console.Beep(784, 150);
            Console.Beep(587, 1200);
            Thread.Sleep(75);
            Console.Beep(932, 150);
            Console.Beep(784, 150);
            Console.Beep(554, 1200);
            Thread.Sleep(75);
            Console.Beep(932, 150);
            Console.Beep(784, 150);
            Console.Beep(523, 1200);
            Thread.Sleep(150);
            Console.Beep(466, 150);
            Console.Beep(523, 150);
        }
        public delegate void MessageDelegate(string message);
        public event MessageDelegate Message;
        static void PrintMessage1(string message)
        {
            Console.WriteLine(message);
        }
        static void PrintMessage2(string message)
        {
            Console.WriteLine(message[0]);
        }
        static void Main(string[] args)
        {
            List<int> list = new List<int>();
            for (int i = 0; i < 100; i++)
            {
                list.Add(i);
            }
            List<double> newList = list.Where(x => x > 60 && x % 10 == 0).Select(x => Math.Sqrt(x)).ToList();
            for (int i = 0; i < newList.Count; i++)
            {
                Console.WriteLine(newList[i]);
            }

            Fridge fridge1 = new Fridge()
            {
                Volume = 306.0,
                Model = "ABC",
                Height = 1835.3,
                Width = 527.2,
                Depth = 611.0
            };
            Fridge fridge2 = new Fridge()
            {
                Volume = 300.0,
                Model = "DBCd",
                Height = 1533.3,
                Width = 526.2,
                Depth = 618.0
            };
            Fridge fridge3 = new Fridge()
            {
                Volume = 206.0,
                Model = "BBCq",
                Height = 1635.3,
                Width = 529.2,
                Depth = 411.0
            };
            Fridge fridge4 = new Fridge()
            {
                Volume = 506.0,
                Model = "ZBCy",
                Height = 1842.3,
                Width = 564.2,
                Depth = 675.0
            };
            Fridge fridge5 = new Fridge()
            {
                Volume = 346.0,
                Model = "YBCu",
                Height = 1742.3,
                Width = 542.2,
                Depth = 685.0
            };
            List<Fridge> listFridge = new List<Fridge>();
            listFridge.Add(fridge1);
            listFridge.Add(fridge2);
            listFridge.Add(fridge3);
            listFridge.Add(fridge4);
            listFridge.Add(fridge5);
            List<Fridge> NewFridges = listFridge.OrderBy(fridge => fridge.Model).Where(fridge => fridge.Height > 1600).ToList();
            for (int i = 0; i < NewFridges.Count; i++)
            {
                Console.WriteLine(NewFridges[i].Model);
            }
            EvenText e = new EvenText();
            e.Message += PrintMessage1;
            e.Message += PrintMessage2;
            e.Message("Test");
            //Thread myThread = new Thread(new ThreadStart(MissionImpossible));
            Thread myThread = new Thread(new ThreadStart(coupleSolo));
            //Thread myThread = new Thread(new ThreadStart(refrenSolo));
            myThread.Start();
        }
    }
}
