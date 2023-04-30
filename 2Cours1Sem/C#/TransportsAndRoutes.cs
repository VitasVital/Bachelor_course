using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp4
{
    interface ITransport
    {
        int PassengerCapacity { get; set; }
        string Model { get;  set; }
    }
    class Buss : ITransport
    {
        public int PassengerCapacity { get; set; }
        public string Model { get; set; }
        public Buss(int PassengerCapacity, string Model)
        {
            this.PassengerCapacity = PassengerCapacity;
            this.Model = Model;
        }
    }
    class Trolleybuss : ITransport
    {
        public int PassengerCapacity { get; set; }
        public string Model { get; set; }
        public Trolleybuss(int PassengerCapacity, string Model)
        {
            this.PassengerCapacity = PassengerCapacity;
            this.Model = Model;
        }
    }
    class Tram : ITransport
    {
        public int PassengerCapacity { get; set; }
        public string Model { get; set; }
        public Tram(int PassengerCapacity, string Model)
        {
            this.PassengerCapacity = PassengerCapacity;
            this.Model = Model;
        }
    }
    class Depot<T> where T:ITransport
    {
        List<Route<Stop>> routes;
        List<ITransport> transports;
        public Depot(List<Route<Stop>> routes, List<ITransport> transports)
        {
            this.routes = routes;
            this.transports = transports;
        }
        public Dictionary<ITransport, Route<Stop>> Distribute()
        {
            Dictionary<ITransport, Route<Stop>> distribute = new Dictionary<ITransport, Route<Stop>>();
            for (int i=0;i<transports.Count;i++)
            {
                for (int j=i;j<transports.Count;j++)
                {
                    if (transports[i].PassengerCapacity > transports[j].PassengerCapacity)
                    {
                        ITransport help = transports[i];
                        transports[i] = transports[j];
                        transports[j] = help;
                    }
                }
            }
            for (int i=0;i<routes.Count;i++)
            {
                for (int j=i;j<routes.Count;j++)
                {
                    if (routes[i].flow > routes[j].flow)
                    {
                        Route<Stop> help = routes[i];
                        routes[i] = routes[j];
                        routes[j] = help;
                    }
                }
            }
            for (int i=0;i<transports.Count;i++)
            {
                if (i < routes.Count)
                {
                    distribute.Add(transports[i], routes[i]);
                }
            }
            return distribute;
        }
    }
    class Stop
    {
        public string Name { get; set; }
        public int Flow { get; set; } //поток
        public Stop(string Name, int Flow)
        {
            this.Name = Name;
            this.Flow = Flow;
        }
    }
    class Route<T>
    {
        List<Stop> stops;
        public int Number { get; set; }
        public int flow = 0;
        public Route(List<Stop> stops, int Number)
        {
            this.stops = stops;
            this.Number = Number;
            for (int i=0;i<stops.Count;i++)
            {
                this.flow += stops[i].Flow;
            }
        }
        public void PrintStops()
        {
            Console.WriteLine($"\tМаршрут №{this.Number}");
            for (int i=0;i<stops.Count;i++)
            {
                Console.WriteLine($"\t{stops[i].Name}\n" +
                    $"\t\t{stops[i].Flow} человек");
            }
            Console.WriteLine();
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            List<Stop> stops = new List<Stop>();
            List<Route<Stop>> routes = new List<Route<Stop>>();

            stops.Add(new Stop("Адорацкого", 4));
            stops.Add(new Stop("Фатыха Амирхана", 8));
            stops.Add(new Stop("Мусина", 7));
            stops.Add(new Stop("Парк победы", 5));
            stops.Add(new Stop("Магазин океан", 7));
            stops.Add(new Stop("Улица декабристов", 7));
            stops.Add(new Stop("Тандем", 2));
            stops.Add(new Stop("Энергетический университет", 4));
            stops.Add(new Stop("Центральный стадион", 3));
            stops.Add(new Stop("Чернышевского", 1));
            stops.Add(new Stop("Педагогический университет", 4));
            stops.Add(new Stop("Комбинат здоровье", 2));
            Route<Stop> route15 = new Route<Stop>(stops, 15);
            routes.Add(route15);

            stops.Clear();
            stops.Add(new Stop("Тандем", 2));
            stops.Add(new Stop("Энергетический университет", 4));
            stops.Add(new Stop("Центральный стадион", 6));
            stops.Add(new Stop("Чернышевского", 1));
            stops.Add(new Stop("Педагогический университет", 4));
            stops.Add(new Stop("Комбинат здоровье", 2));
            stops.Add(new Stop("Четаева", 5));
            stops.Add(new Stop("Чистопольская", 4));
            stops.Add(new Stop("Сибгата Хакима", 7));
            stops.Add(new Stop("Мост Миллениум", 9));
            stops.Add(new Stop("Парк Горького", 3));
            stops.Add(new Stop("Улица Толстого", 6));
            Route<Stop> route75 = new Route<Stop>(stops, 75);
            routes.Add(route75);

            stops.Clear();
            stops.Add(new Stop("Тандем", 2));
            stops.Add(new Stop("Энергетический университет", 4));
            stops.Add(new Stop("Дворец спорта", 5));
            stops.Add(new Stop("ЦУМ", 3));
            stops.Add(new Stop("Чернышевского", 7));
            stops.Add(new Stop("Колхозный рынок", 2));
            stops.Add(new Stop("Гаврилова", 5));
            stops.Add(new Stop("Казань Арена", 4));
            stops.Add(new Stop("Ветеринарная академия", 9));
            stops.Add(new Stop("Академика Арбузова", 10));
            stops.Add(new Stop("Халитова", 13));
            stops.Add(new Stop("Журналистов", 6));
            routes.Add(route75);
            Route<Stop> route47 = new Route<Stop>(stops, 47);
            routes.Add(route47);

            stops.Clear();
            stops.Add(new Stop("Четаева", 5));
            stops.Add(new Stop("Чистопольская", 4));
            stops.Add(new Stop("Сибгата Хакима", 7));
            stops.Add(new Stop("Мост Миллениум", 9));
            stops.Add(new Stop("Парк Горького", 3));
            stops.Add(new Stop("Улица Толстого", 6));
            stops.Add(new Stop("Адорацкого", 4));
            stops.Add(new Stop("Фатыха Амирхана", 8));
            stops.Add(new Stop("Мусина", 7));
            stops.Add(new Stop("Парк победы", 5));
            stops.Add(new Stop("Магазин океан", 3));
            stops.Add(new Stop("Улица декабристов", 7));
            Route<Stop> route28 = new Route<Stop>(stops, 28);
            routes.Add(route28);

            stops.Clear();
            stops.Add(new Stop("Гаврилова", 5));
            stops.Add(new Stop("Казань Арена", 4));
            stops.Add(new Stop("Ветеринарная академия", 9));
            stops.Add(new Stop("Академика Арбузова", 10));
            stops.Add(new Stop("Халитова", 13));
            stops.Add(new Stop("Журналистов", 6));
            stops.Add(new Stop("Тандем", 2));
            stops.Add(new Stop("Энергетический университет", 4));
            stops.Add(new Stop("Центральный стадион", 7));
            stops.Add(new Stop("Чернышевского", 1));
            stops.Add(new Stop("Педагогический университет", 4));
            stops.Add(new Stop("Комбинат здоровье", 2));
            stops.Add(new Stop("Четаева", 5));
            Route<Stop> route60 = new Route<Stop>(stops, 60);
            routes.Add(route60);

            List<ITransport> transports = new List<ITransport>();
            ITransport buss1 = new Buss(30, "Higer");
            ITransport trolleybuss1 = new Trolleybuss(20, "Volga");
            ITransport tram1 = new Tram(40, "Boychik");
            ITransport buss2 = new Buss(25, "Samara");
            ITransport trolleybuss2 = new Trolleybuss(35, "Trololobus");
            transports.Add(buss1);
            transports.Add(trolleybuss1);
            transports.Add(tram1);
            transports.Add(buss2);
            transports.Add(trolleybuss2);

            Depot<ITransport> depot = new Depot<ITransport>(routes, transports);
            depot.Distribute();
            Console.WriteLine($"Муршрут {buss1.Model} автобуса №{depot.Distribute()[buss1].Number} " +
                $"с вместимостью = {buss1.PassengerCapacity} и маршрутом с потоком = {depot.Distribute()[buss1].flow}\n");
            depot.Distribute()[buss1].PrintStops();
            Console.WriteLine($"Муршрут {trolleybuss1.Model} троллейбуса №{depot.Distribute()[trolleybuss1].Number} " +
                $"с вместимостью = {trolleybuss1.PassengerCapacity} и маршрутом с потоком = {depot.Distribute()[trolleybuss1].flow}\n");
            depot.Distribute()[trolleybuss1].PrintStops();
            Console.WriteLine($"Муршрут {tram1.Model} трамвая №{depot.Distribute()[tram1].Number} " +
                $"с вместимостью = {tram1.PassengerCapacity} и маршрутом с потоком = {depot.Distribute()[tram1].flow}\n");
            depot.Distribute()[tram1].PrintStops();
            Console.WriteLine($"Муршрут {buss2.Model} автобуса №{depot.Distribute()[buss2].Number} " +
                $"с вместимостью = {buss2.PassengerCapacity} и маршрутом с потоком = {depot.Distribute()[buss2].flow}\n");
            depot.Distribute()[buss2].PrintStops();
            Console.WriteLine($"Муршрут {trolleybuss2.Model} троллейбуса №{depot.Distribute()[trolleybuss2].Number} " +
                $"с вместимостью = {trolleybuss2.PassengerCapacity} и маршрутом с потоком = {depot.Distribute()[trolleybuss2].flow}\n");
            depot.Distribute()[trolleybuss2].PrintStops();
        }
    }
}
