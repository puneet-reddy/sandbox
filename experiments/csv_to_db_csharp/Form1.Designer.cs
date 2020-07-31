using System.Windows.Forms;
using System.Drawing;

namespace csv_to_db_csharp {
    partial class Form1 {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;
        private ListBox lstBox = new ListBox();
        private Button btnGet = new Button();

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose (bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose ();
            }
            base.Dispose (disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent () {
            this.components = new System.ComponentModel.Container ();
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size (800, 450);
            this.Text = "Dashboard";
            AddControls();
        }

        #endregion

        /// <summary>
        /// Building the form programatically instead of using the GUI designer.
        ///</summary>
        private void AddControls () {
            this.lstBox.Text = "Sample Text";
            this.lstBox.Location = new Point(10, 65);
            this.lstBox.Size = new Size(700, 375);

            this.btnGet.BackColor = Color.Gray;
            this.btnGet.Text = "Get Data";
            this.btnGet.Location = new Point(10, 25);
            this.btnGet.Size = new Size(100, 30);
            this.btnGet.Click += new System.EventHandler(btnGet_Click);

            this.Controls.Add(lstBox);
            this.Controls.Add(btnGet);
        }

        private void btnGet_Click(object sender, System.EventArgs e) {
            var access = new DataAccess();
            var items = access.GetSsqas(30);
            foreach (var item in items) {
                this.lstBox.Items.Add(item.FullInfo);
            }
        }
    }
}