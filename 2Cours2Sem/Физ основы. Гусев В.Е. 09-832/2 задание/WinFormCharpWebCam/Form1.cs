using System;
using System.Linq;
using System.Text;
using System.Data;
using System.Drawing;
using System.Windows.Forms;
using System.ComponentModel;
using System.Collections.Generic;
using System.Threading;



namespace WinFormCharpWebCam
{
    //Design by Pongsakorn Poosankam
    public partial class mainWinForm : Form
    {
        public mainWinForm()
        {
            InitializeComponent();
        }
        WebCam webcam;
        public int time1 = 0;
        public int count = 0;
        public string location = AppDomain.CurrentDomain.BaseDirectory;
        
        private void mainWinForm_Load(object sender, EventArgs e)
        {
            webcam = new WebCam();
            webcam.InitializeWebCam(ref imgVideo);
        }

        private void bntStart_Click(object sender, EventArgs e)
        {
            webcam.Start();
        }

        private void bntStop_Click(object sender, EventArgs e)
        {
            webcam.Stop();
        }

        private void bntContinue_Click(object sender, EventArgs e)
        {
            webcam.Continue();
        }

        private void bntCapture_Click(object sender, EventArgs e)
        {
            imgCapture.Image = imgVideo.Image;
        }

        private void bntSave_Click(object sender, EventArgs e)
        {
            Helper.SaveImageCapture(imgCapture.Image);
        }

        private void bntVideoFormat_Click(object sender, EventArgs e)
        {
            webcam.ResolutionSetting();
        }

        private void bntVideoSource_Click(object sender, EventArgs e)
        {
            webcam.AdvanceSetting();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            time1 += 1;
            label1.Text = Convert.ToString(time1);
            if (time1 % 5 == 0)
            {
                SavePhoto();
            }
        }
        public void SavePhoto()
        {
            while(count<5)
            {
                imgVideo.Image.Save(location + "\\photos\\" + "\\" + DateTime.Now.Ticks + ".jpg");
                count += 1;
            }
            count = 0;
        }

        private void btnStopCapture_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
        }

        private void btnStartCapture_Click(object sender, EventArgs e)
        {
            webcam.Start();
            timer1.Enabled = true;
            time1 = 0;
        }
    }
}
