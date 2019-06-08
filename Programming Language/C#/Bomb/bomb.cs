using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
	public partial class Form1 : Form
	{
		public int count = 9;
		
		public Form1()
		{
			InitializeComponent();
		}
		private void button1_Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
		private void timer1_Tick(object sender, EventArgs e)
		{
			count = count - 1;
			progressBar1.PerformStep();
			label1.Text = count.ToString();
			if (count == 0)
			{
				timer1.Stop();
				pictureBox1.Show();
				return;
			}
		}
		
		private void button2_Click(object sender, EventArgs e)
		{
			timer1.Start();
		}
		private void button3_Click(object sender, EventArgs e)
		{
			pictureBox1.Hide();
			timer1.Stop();
			count = 9;
			progressBar1.Value = 0;
			label1.Text = count.ToString();
		}
	}
}