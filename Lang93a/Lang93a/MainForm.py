import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(31, 69)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Kilowatts Used:"
		self._label1.Click += self.Label1Click
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(31, 120)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Base Rate:"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(171, 120)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(66, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "label4"
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(31, 143)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "Surcharge:"
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(171, 143)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(66, 23)
		self._label6.TabIndex = 5
		self._label6.Text = "label6"
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(31, 169)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 6
		self._label7.Text = "CityTax:"
		self._label7.Click += self.Label7Click
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(171, 169)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(66, 23)
		self._label8.TabIndex = 7
		self._label8.Text = "label8"
		self._label8.Click += self.Label8Click
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(31, 224)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 8
		self._label9.Text = "Amount In Total:"
		self._label9.Click += self.Label9Click
		# 
		# label10
		# 
		self._label10.Location = System.Drawing.Point(171, 224)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(66, 23)
		self._label10.TabIndex = 9
		self._label10.Text = "label10"
		self._label10.Click += self.Label10Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(137, 69)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 10
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 297)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 11
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(94, 297)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 12
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(175, 297)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 13
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(153, 120)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(12, 23)
		self._label2.TabIndex = 14
		self._label2.Text = "$"
		# 
		# label11
		# 
		self._label11.Location = System.Drawing.Point(153, 143)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(12, 23)
		self._label11.TabIndex = 15
		self._label11.Text = "$"
		# 
		# label12
		# 
		self._label12.Location = System.Drawing.Point(153, 169)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(12, 23)
		self._label12.TabIndex = 16
		self._label12.Text = "$"
		# 
		# label13
		# 
		self._label13.Location = System.Drawing.Point(31, 251)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 17
		self._label13.Text = "After Due Date:"
		# 
		# label14
		# 
		self._label14.Location = System.Drawing.Point(171, 251)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(66, 23)
		self._label14.TabIndex = 18
		self._label14.Text = "label14"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(262, 351)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass

	def Label7Click(self, sender, e):
		pass

	def Label9Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass

	def Label8Click(self, sender, e):
		pass

	def Label10Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		Used = float(self._textBox1.Text)
		
		Base = Used * 0.0475
		Base = round(Base, 2)
		Surc = Base * 0.10
		Surc = round(Surc, 2)
		CitT = Base * 0.03
		CitT = round(CitT, 2)
		
		Total = Base + Surc + CitT
		Total = round(Total, 2)
		After = Total + (Total * 0.04)
		After = round(After, 2)
		
		self._label4.Text = str(Base)
		self._label6.Text = str(Surc)
		self._label8.Text = str(CitT)
		self._label10.Text = str(Total)
		self._label14.Text = str(After)

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._label6.Text = ""
		self._label8.Text = ""
		self._label10.Text = ""
		self._label14.Text = ""


	def Button3Click(self, sender, e):
		Application.Exit()
		
		