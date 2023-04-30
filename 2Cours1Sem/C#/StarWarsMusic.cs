using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace ConsoleApp6
{
    class StarWarsMusic
    {
        public delegate void MusicDelegate();
        public event MusicDelegate Music;
        static void Sound300_500()
        {
            Console.Beep(300, 500);
        }
        static void Sound250_500()
        {
            Console.Beep(250, 500);
        }
        static void Sound350_250()
        {
            Console.Beep(350, 250);
        }
        static void Sound37_50()
        {
            Console.Beep(37, 50);
        }
        static void Main(string[] args)
        {
            StarWarsMusic music = new StarWarsMusic();
            music.Music += Sound300_500;
            music.Music += Sound37_50;
            music.Music += Sound300_500;
            music.Music += Sound37_50;
            music.Music += Sound300_500;
            music.Music += Sound37_50;
            music.Music += Sound250_500;
            music.Music += Sound37_50;
            music.Music += Sound350_250;
            music.Music += Sound300_500;
            music.Music += Sound37_50;
            music.Music += Sound250_500;
            music.Music += Sound37_50;
            music.Music += Sound350_250;
            music.Music += Sound300_500;
            music.Music += Sound37_50;
            music.Music();
        }
    }
}
