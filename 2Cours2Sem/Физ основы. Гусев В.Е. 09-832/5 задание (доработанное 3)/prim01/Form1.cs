using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace prim01
{
    public partial class Form1 : Form
    {
        public String s1;
        public String s2;
        public char c0;
        public String Y1, Y2;
        public bool Y1empty, Y2empty;
        public int time;
        public double chisloTime;
        public Form1()
        {
            InitializeComponent();
            Y1 = "0";
            Y2 = "0";
            Y1empty = true;
            Y2empty = true;
            time = 0;
            chisloTime = 0;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            serialPort1.Open();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            s1 = "$046" + '\r';
            serialPort1.Write(s1);
            s2 = "";
            while ((c0 = (char)serialPort1.ReadChar()) != '\r')
            {
                s2 += c0;
            }
            label1.Text = s2;
        }
        
        private void Click_Button(String num, String binnum)
        {
            if (Y1empty == true)
            {
                label2.Text = $"Y={num}";
                label6.Text = binnum;
                Y1 = num;
                Y1empty = false;
            }
            else
            {
                if (Y2empty == true)
                {
                    label3.Text = $"Y={num}";
                    label7.Text = binnum;
                    Y2 = num;
                    Y2empty = false;
                }
                else
                {
                    label2.Text = $"Y={num}";
                    label6.Text = binnum;
                    Y1 = num;
                    Y1empty = false;
                    Y2empty = true;
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Click_Button("1", "0001");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Click_Button("2", "0010");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Click_Button("3", "0011");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Click_Button("4", "0100");
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Click_Button("5", "0101");
        }

        private void button9_Click(object sender, EventArgs e)
        {
            Click_Button("6", "0110");
        }

        private void button10_Click(object sender, EventArgs e)
        {
            Click_Button("7", "0111");
        }

        private void button11_Click(object sender, EventArgs e)
        {
            Click_Button("8", "1000");
        }

        private void button12_Click(object sender, EventArgs e)
        {
            Click_Button("9", "1001");
        }

        private void button13_Click(object sender, EventArgs e)
        {
            Click_Button("A", "1010");
        }

        private void button14_Click(object sender, EventArgs e)
        {
            Click_Button("B", "1011");
        }

        private void button15_Click(object sender, EventArgs e)
        {
            Click_Button("C", "1100");
        }

        private void button16_Click(object sender, EventArgs e)
        {
            Click_Button("D", "1101");
        }

        private void button17_Click(object sender, EventArgs e)
        {
            Click_Button("E", "1110");
        }

        private void button18_Click(object sender, EventArgs e)
        {
            Click_Button("F", "1111");
        }

        private void button19_Click(object sender, EventArgs e)
        {
            label2.Text = "Y=";
            label3.Text = "Y=";
            label6.Text = "";
            label7.Text = "";
            Y1empty = true;
            Y2empty = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            s1 = "#0400" + Y1 + Y2 + '\r';
            serialPort1.Write(s1);
            s2 = "";
            while ((c0 = (char)serialPort1.ReadChar()) != '\r')
            {
                s2 += c0;
            }
            label1.Text = s2;
            time += timer1.Interval;
            chisloTime = Convert.ToInt32(Convert.ToDouble(time)/1000);
            label5.Text = "Time " + Convert.ToString(chisloTime) + " (sec)";
            if (Convert.ToInt32(textBox1.Text)*1000 == time)
            {
                time = 0;
                timer1.Enabled = false;
            }
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            char number = e.KeyChar;
            if (!Char.IsDigit(number))
            {
                e.Handled = true;
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            time = 0;
            timer1.Enabled = true;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Click_Button("0", "0000");
        }
    }
}