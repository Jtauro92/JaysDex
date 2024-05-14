using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Dex_Editor
{
    public partial class mainForm : Form
    {
        public mainForm()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void outputbutton_Click(object sender, EventArgs e)
        {
            StringBuilder sb = new StringBuilder(outputBox.Text);

            sb.Append($"Hi {nameMaskedTextBox.Text} \nIt is nice to meet you");

            outputBox.Text = sb.ToString();
        }
    }
}
