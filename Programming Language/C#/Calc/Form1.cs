using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator
{
    public partial class Form1 : Form
    {
        int su1, su2;
        float result;
        string oper;
        bool isOper;
        const int DEFAULT_VALUE = 0;

        public Form1()
        {
            InitializeComponent();
            Init();
        }

        private void Init()
        {
            tb_Result.Text = DEFAULT_VALUE.ToString();
            isOper = true;
        }

        private void BtnClick(object sender, EventArgs e)
        {
            if (isOper)
                tb_Result.Text = "";
            isOper = false;
            tb_Result.Text += ((Button)sender).Text;
        }

        private void BtnClear_Click(object sender, EventArgs e)
        {
            tb_Result.Text = "";
            Init();
        }

        private void BtnOper_Click(object sender, EventArgs e)
        {
            su2 = int.Parse(tb_Result.Text);
            oper = ((Button)sender).Text;
        }

        private void BtnResult_Click(object sender, EventArgs e)
        {
            su2 = int.Parse(tb_Result.Text);

            switch (oper)
            {
                case "+":
                    result = su1 + su2;
                    break;
                case "-":
                    result = su1 - su2;
                    break;
                case "*":
                    result = su1 * su2;
                    break;
                case "/":
                    result = (float)su1 / (float)su2;
                    break;
            }
            tb_Result.Text = result.ToString();
            isOper = true;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
