using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Graphs
{
    interface IGraph
    {
        void Add(Edge edge);
        void Remove(Edge edge);
        int Contains(Edge edge);
        int EdgeCount();
        int VertexCount(); //вершина
    }
    class Edge //ребро
    {
        public int From { get; set; }
        public int To { get; set; }
        public int Weight { get; set; }
        public Edge(int a,int b,int с)
        {
            this.From = a;
            this.To = b;
            this.Weight = с;
        }
    }
    class GraphsArray : IGraph
    {
        public int[,] array = new int[20, 20];
        public GraphsArray(List<Edge> list)
        {
            for (int i=0;i<list.Count;i++)
            {
                this.Add(list[i]);
            }
        }
        public void Add(Edge edge)
        {
            array[edge.From, edge.To] = edge.Weight;
        }
        public int Contains(Edge edge)
        {
            return array[edge.From, edge.To];
        }

        public int VertexCount()
        {
            bool[] help = new bool[20];
            int sum=0;
            for (int i=0;i<20;i++)
            {
                for (int j=0;j<20;j++)
                {
                    if (array[i, j] != 0)
                    {
                        help[i] = true;
                        help[j] = true;
                    }
                }
            }
            for (int i=0;i<20;i++)
            {
                if (help[i]==true)
                {
                    sum++;
                }
            }
            return sum;
        }

        public void Remove(Edge edge)
        {
            array[edge.From, edge.To] = 0;
        }

        public int EdgeCount()
        {
            int sum = 0;
            bool prov = true;
            for (int i=0;i<20;i++)
            {
                for (int j=0;j<20; j++)
                {
                    if (array[i,j]!=0)
                    {
                        if (prov==true)
                        {
                            sum++;
                            prov = false;
                        }
                    }
                }
                prov = true;
            }
            return sum;
        }
    }
    class GraphsList : IGraph
    {
        List<Edge> list = new List<Edge>();
        public GraphsList(List<Edge> list)
        {
            for (int i = 0; i < list.Count; i++)
            {
                this.Add(list[i]);
            }
        }
        public void Add(Edge edge)
        {
            list.Add(edge);
        }

        public int Contains(Edge edge)
        {
            int num = 0;
            for(int i=0;i<list.Count;i++)
            {
                if (list[i].From == edge.From && list[i].To == edge.To)
                {
                    num = list[i].Weight;
                }
            }
            return num;
        }

        public int EdgeCount()
        {
            return list.Count;
        }

        public void Remove(Edge edge)
        {
            for (int i=0;i<list.Count;i++)
            {
                if (list[i].From==edge.From && list[i].To==edge.To)
                {
                    list.RemoveAt(i);
                }
            }
        }

        public int VertexCount()
        {
            List<int> sum = new List<int>();
            bool provfrom = true;
            bool provto = true;
            for(int i=0;i<list.Count;i++)
            {
                for(int j=0;j<sum.Count;j++)
                {
                    if(list[i].From==sum[j])
                    {
                        provfrom = false;
                    }
                    if (list[i].To == sum[j])
                    {
                        provto = false;
                    }
                }
                if (provfrom==true)
                {
                    sum.Add(list[i].From);
                }
                if (provto == true)
                {
                    sum.Add(list[i].To);
                }
                provfrom = true;
                provto = true;
            }
            return sum.Count;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            //int[,] array = new int[20, 30];
            //array[5, 8] = 123;
            //List<int> list = new List<int>();
            //list.Add(13);

            //GraphsArray grap = new GraphsArray();
            //grap.Add(new Edge(1, 2, 10));
            //grap.Add(new Edge(3, 3, 20));
            //grap.Add(new Edge(1, 5, 30));
            //grap.Add(new Edge(4, 3, 40));
            //Console.WriteLine(grap.Contains(new Edge(3, 5, 0)));
            //Console.WriteLine(grap.Contains(new Edge(3, 3, 0)));
            //grap.Remove(new Edge(1, 5, 0));
            //Console.WriteLine(grap.EdgeCount());
            //Console.WriteLine(grap.VertexCount()+"\n");

            //GraphsList grli = new GraphsList();
            //grli.Add(new Edge(1, 2, 10));
            //grli.Add(new Edge(3, 5, 20));
            //grli.Add(new Edge(1, 4, 30));
            //grli.Add(new Edge(8, 5, 40));
            //grli.Add(new Edge(6, 4, 50));
            //Console.WriteLine(grli.Contains(new Edge(2, 5, 0)));
            //Console.WriteLine(grli.Contains(new Edge(3, 5, 0)));
            //Console.WriteLine(grli.EdgeCount());
            //grli.Remove(new Edge(3, 5, 0));
            //Console.WriteLine(grli.EdgeCount());
            //Console.WriteLine(grli.VertexCount()+"\n");

            List<Edge> list = new List<Edge>();
            list.Add(new Edge(1, 2, 10));
            list.Add(new Edge(1, 5, 20));
            list.Add(new Edge(3, 4, 30));

            GraphsArray grar = new GraphsArray(list);
            Console.WriteLine(grar.Contains(new Edge(3, 5, 0)));
            Console.WriteLine(grar.Contains(new Edge(1, 2, 10)));
            grar.Remove(new Edge(1, 5, 0));
            Console.WriteLine(grar.EdgeCount());
            Console.WriteLine(grar.VertexCount() + "\n");

            GraphsList grli = new GraphsList(list);
            Console.WriteLine(grli.Contains(new Edge(3, 5, 0)));
            Console.WriteLine(grli.Contains(new Edge(1, 2, 10)));
            grli.Remove(new Edge(1, 5, 0));
            Console.WriteLine(grli.EdgeCount());
            Console.WriteLine(grli.VertexCount() + "\n");
        }
    }
}

//граф доработать до взешенного
//добавить в конструкторы листы, содержащие координаты ребер (в каждом ребре листа координаты ребер)