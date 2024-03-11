import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label17 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(115, 111)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(115, 143)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.Control
		self._label1.Location = System.Drawing.Point(11, 108)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "Num 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.Control
		self._label2.Location = System.Drawing.Point(11, 140)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Num 2:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.Control
		self._label3.Location = System.Drawing.Point(246, 68)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Difference"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.Control
		self._label4.Location = System.Drawing.Point(246, 108)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 5
		self._label4.Text = "Product"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.Control
		self._label5.Location = System.Drawing.Point(246, 146)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 6
		self._label5.Text = "Average"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.Control
		self._label6.Location = System.Drawing.Point(246, 182)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 7
		self._label6.Text = "Distance"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.Control
		self._label7.Location = System.Drawing.Point(246, 30)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 8
		self._label7.Text = "Sum"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.Control
		self._label8.Location = System.Drawing.Point(246, 216)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 9
		self._label8.Text = "Max"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.Control
		self._label9.Location = System.Drawing.Point(246, 251)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 10
		self._label9.Text = "Min"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.Control
		self._label10.Location = System.Drawing.Point(352, 30)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 11
		self._label10.Text = "10"
		self._label10.Click += self.Label10Click
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.Control
		self._label11.Location = System.Drawing.Point(352, 68)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 12
		self._label11.Text = "11"
		self._label11.Click += self.Label11Click
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.Control
		self._label12.Location = System.Drawing.Point(352, 108)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 13
		self._label12.Text = "12"
		self._label12.Click += self.Label12Click
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.Control
		self._label13.Location = System.Drawing.Point(352, 146)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 14
		self._label13.Text = "13"
		self._label13.Click += self.Label13Click
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.SystemColors.Control
		self._label14.Location = System.Drawing.Point(352, 182)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 15
		self._label14.Text = "14"
		self._label14.Click += self.Label14Click
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.SystemColors.Control
		self._label15.Location = System.Drawing.Point(352, 216)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(100, 23)
		self._label15.TabIndex = 16
		self._label15.Text = "15"
		self._label15.Click += self.Label15Click
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.SystemColors.Control
		self._label16.Location = System.Drawing.Point(352, 251)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(100, 23)
		self._label16.TabIndex = 17
		self._label16.Text = "16"
		self._label16.Click += self.Label16Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 186)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(202, 23)
		self._button1.TabIndex = 18
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(13, 216)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(202, 23)
		self._button2.TabIndex = 19
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(13, 246)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(202, 23)
		self._button3.TabIndex = 20
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label17
		# 
		self._label17.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label17.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label17.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label17.Location = System.Drawing.Point(13, 26)
		self._label17.Name = "label17"
		self._label17.Size = System.Drawing.Size(202, 65)
		self._label17.TabIndex = 21
		self._label17.Text = "Smart Calculator"
		self._label17.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self.ClientSize = System.Drawing.Size(464, 300)
		self.Controls.Add(self._label17)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label10Click(self, sender, e):
		pass

	def Label11Click(self, sender, e):
		pass

	def Label12Click(self, sender, e):
		pass

	def Label13Click(self, sender, e):
		pass

	def Label14Click(self, sender, e):
		pass

	def Label15Click(self, sender, e):
		pass

	def Label16Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Diff = num1 - num2
		Prod = num1 * num2
		Aver = num1 / num2
		AbsDiff = abs(Diff)
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:
			Max = num2
			
		if Max == num1:
			min = num2
		else:
			min = num1
		self._label10.Text = str(Sum)
		self._label11.Text = str(Diff)
		self._label12.Text = str(Prod)
		self._label13.Text = str(Aver)
		self._label14.Text = str(AbsDiff)
		self._label15.Text = str(Max)
		self._label16.Text = str(Min)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""
		self._label15.Text = ""
		self._label16.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()