using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Threading;

namespace prim02
{
    public partial class Form1 : Form
    {
        public Thread myThread;
        public Thread sendThread;
        public String zapros;
        public String sendzapros;
        public String s2;
        public char c0;
        public bool started;
        public bool sendstarted;
        public String helpsend;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            serialPort1.Open();
            started = false;
            sendstarted = false;
            sendzapros = "";
        }
        public void ThreadSendZapros()
        {
            while (true)
            {
                sendzapros = textBox1.Text + '\r';
                serialPort1.Write(sendzapros);
            }
        }
        public void ThreadProc()
        {
            while (true)
            {
                //zapros = "GP111011" + '\r';
                while ((c0 = (char)serialPort1.ReadChar()) != '\r')
                {
                    zapros += c0;
                }
            }
        }

        public bool RequestVeridication(String zapros) //проверка запроса
        {
            if (zapros.Length!=8)
            {
                return false;
            }
            if (zapros[0]!='G' || zapros[1]!='P')
            {
                return false;
            }
            for (int i=2;i<8;i++)
            {
                if (zapros[i]!='0' && zapros[i]!='1')
                {
                    return false;
                }
            }
            return true;
        }

        public void ChangeColor(String zapros)
        {
            if (zapros[2] == '0')
            {
                pictureBox3.BackColor = Color.Red;
            }
            else
            {
                pictureBox3.BackColor = Color.Green;
            }
            if (zapros[3] == '0')
            {
                pictureBox4.BackColor = Color.Red;
            }
            else
            {
                pictureBox4.BackColor = Color.Green;
            }
            if (zapros[4] == '0')
            {
                pictureBox5.BackColor = Color.Red;
            }
            else
            {
                pictureBox5.BackColor = Color.Green;
            }
            if (zapros[5] == '0')
            {
                pictureBox10.BackColor = Color.Red;
            }
            else
            {
                pictureBox10.BackColor = Color.Green;
            }
            if (zapros[6] == '0')
            {
                pictureBox8.BackColor = Color.Red;
            }
            else
            {
                pictureBox8.BackColor = Color.Green;
            }
            if (zapros[7] == '0')
            {
                pictureBox7.BackColor = Color.Red;
            }
            else
            {
                pictureBox7.BackColor = Color.Green;
            }
        }


        private void button2_Click(object sender, EventArgs e)
        {
            if (started == true)
            {
                timer1.Enabled = false;
                label1.Text = "Принимаемый запрос";
                myThread.Abort();
                pictureBox2.BackColor = Color.Gray;
                pictureBox3.BackColor = Color.Gray;
                pictureBox4.BackColor = Color.Gray;
                pictureBox5.BackColor = Color.Gray;
                pictureBox6.BackColor = Color.Gray;
                pictureBox7.BackColor = Color.Gray;
                pictureBox8.BackColor = Color.Gray;
                pictureBox10.BackColor = Color.Gray;
                started = false;
            }
        }


        private void button4_Click(object sender, EventArgs e)
        {
            if (started == false)
            {
                timer1.Enabled = true;
                myThread = new Thread(this.ThreadProc);
                myThread.Start();
                started = true;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (sendstarted == false)
            {
                sendThread = new Thread(this.ThreadSendZapros);
                sendThread.Start();
                sendstarted = true;
                timer2.Enabled = true;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (sendstarted == true)
            {
                sendThread.Abort();
                sendstarted = false;
                timer2.Enabled = false;
                label3.Text = "Правильность отправляемого запроса";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (RequestVeridication(zapros) == true)
            {
                ChangeColor(zapros);
                label1.Text = zapros;
            }
            else
            {
                label1.Text = "Неправильный запрос";
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            helpsend = sendzapros.TrimEnd('\r');
            if (RequestVeridication(helpsend) == true)
            {
                label3.Text = textBox1.Text;
            }
            else
            {
                label3.Text = "Неправильный запрос";
            }
        }
    }
}