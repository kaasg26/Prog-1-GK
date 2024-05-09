import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 212)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DimGray
		self._label1.Location = System.Drawing.Point(18, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(113, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Annual Pay:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DimGray
		self._label2.Location = System.Drawing.Point(18, 70)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(113, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Pay periods per year:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DimGray
		self._label3.Location = System.Drawing.Point(18, 137)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(113, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Salery per pay period:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._label4.Location = System.Drawing.Point(137, 137)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "label4"
		self._label4.Click += self.Label4Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(137, 38)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(138, 72)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 6
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(93, 212)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(174, 212)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self.ClientSize = System.Drawing.Size(255, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg153SalaryCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		AnnualSal = 0.0
		PayPer = 0
		SPP = 0.0
		
		AnnualSal = float(self._textBox1.Text)
		PayPer = int(self._textBox2.Text)
		SPP = AnnualSal / PayPer
		self._label4.Text = str(SPP)
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""
		
	def Button3Click(self, sender, e):
		Application.Exit()