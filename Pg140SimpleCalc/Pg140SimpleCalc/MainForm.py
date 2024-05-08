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
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(167, 26)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(25, 31)
		self._button1.TabIndex = 0
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(198, 26)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(25, 31)
		self._button2.TabIndex = 6
		self._button2.Text = "-"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(229, 26)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(25, 31)
		self._button3.TabIndex = 7
		self._button3.Text = "x"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(167, 63)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(25, 31)
		self._button4.TabIndex = 8
		self._button4.Text = "^"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(198, 63)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(25, 31)
		self._button5.TabIndex = 9
		self._button5.Text = "/"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(229, 63)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(25, 31)
		self._button6.TabIndex = 10
		self._button6.Text = "//"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(167, 100)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(87, 23)
		self._button7.TabIndex = 11
		self._button7.Text = "MOD"
		self._button7.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self._button7.UseVisualStyleBackColor = True
		# 
		# button8
		# 
		self._button8.Location = System.Drawing.Point(167, 156)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(87, 23)
		self._button8.TabIndex = 12
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.ForeColor = System.Drawing.Color.Red
		self._button9.Location = System.Drawing.Point(167, 185)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(87, 23)
		self._button9.TabIndex = 13
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Aquamarine
		self._label1.Font = System.Drawing.Font("Mistral", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Red
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 29)
		self._label1.TabIndex = 14
		self._label1.Text = "It's Simple"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 63)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(60, 37)
		self._label2.TabIndex = 15
		self._label2.Text = "First Number"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 106)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(60, 23)
		self._label3.TabIndex = 16
		self._label3.Text = "Operation"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 141)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(74, 34)
		self._label4.TabIndex = 17
		self._label4.Text = "Second Number"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.SpringGreen
		self._label6.Location = System.Drawing.Point(79, 102)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(82, 21)
		self._label6.TabIndex = 19
		self._label6.Text = " "
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Click += self.Label6Click
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.LightBlue
		self._label8.Location = System.Drawing.Point(12, 176)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(149, 41)
		self._label8.TabIndex = 21
		self._label8.Text = " "
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label8.Click += self.Label8Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Goldenrod
		self._textBox1.Location = System.Drawing.Point(79, 63)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(82, 20)
		self._textBox1.TabIndex = 22
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Goldenrod
		self._textBox2.Location = System.Drawing.Point(79, 141)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(82, 20)
		self._textBox2.TabIndex = 23
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Teal
		self.ClientSize = System.Drawing.Size(269, 226)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg140SimpleCalc"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		dblResult = 0.0
		self._label6.Text = "+"
		dblResult = float(self._textBox1.Text) + float(self._textBox2.Text)
		self._label8.Text = str(dblResult)

	def Button2Click(self, sender, e):
		dblResult = 0.0
		self._label6.Text = "-"
		dblResult = float(self._textBox1.Text) - float(self._textBox2.Text)
		self._label8.Text = str(dblResult)

	def Button3Click(self, sender, e):
		dblResult = 0.0
		self._label6.Text = "x"
		dblResult = float(self._textBox1.Text) * float(self._textBox2.Text)
		self._label8.Text = str(dblResult)

	def Button4Click(self, sender, e):
		dblResult = 0.0
		self._label6.Text = "^"
		dblResult = int(self._textBox1.Text) ** (int(self._textBox2.Text))
		self._label8.Text = str(dblResult)

	def Button5Click(self, sender, e):
		dblResult = 0.0
		self._label6.Text = "/"
		dblResult = float(self._textBox1.Text) / int(self._textBox2.Text)
		self._label8.Text = str(dblResult)

	def Button6Click(self, sender, e):
		dblResult = 0.0
		self._label6.Text = "//"
		dblResult = float(self._textBox1.Text) // int(self._textBox2.Text)
		self._label8.Text = str(dblResult)

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass

	def Label8Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Button8Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label6.Text = ""
		self._label8.Text = ""

	def Button9Click(self, sender, e):
		Application.Exit()