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
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(25, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Paid"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(25, 42)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Price"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(131, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(131, 39)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 3
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(25, 65)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Change"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label4.Location = System.Drawing.Point(145, 99)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(72, 23)
		self._label4.TabIndex = 5
		self._label4.Text = " "
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label5.Location = System.Drawing.Point(145, 126)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(72, 23)
		self._label5.TabIndex = 6
		self._label5.Text = " "
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label6.Location = System.Drawing.Point(145, 153)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(72, 23)
		self._label6.TabIndex = 7
		self._label6.Text = " "
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label7.Location = System.Drawing.Point(145, 180)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(72, 23)
		self._label7.TabIndex = 8
		self._label7.Text = " "
		self._label7.Click += self.Label7Click
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label8.Location = System.Drawing.Point(145, 206)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(72, 23)
		self._label8.TabIndex = 9
		self._label8.Text = " "
		self._label8.Click += self.Label8Click
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label9.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label9.Location = System.Drawing.Point(131, 65)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 10
		self._label9.Click += self.Label9Click
		# 
		# label10
		# 
		self._label10.Location = System.Drawing.Point(29, 103)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 11
		self._label10.Text = "Dollars"
		# 
		# label11
		# 
		self._label11.Location = System.Drawing.Point(29, 126)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 12
		self._label11.Text = "Quarters"
		# 
		# label12
		# 
		self._label12.Location = System.Drawing.Point(29, 153)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 13
		self._label12.Text = "Dimes"
		# 
		# label13
		# 
		self._label13.Location = System.Drawing.Point(29, 180)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 14
		self._label13.Text = "Nickels"
		# 
		# label14
		# 
		self._label14.Location = System.Drawing.Point(29, 206)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 15
		self._label14.Text = "Pennies"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 242)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 16
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(93, 242)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 17
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(174, 242)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 18
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self.ClientSize = System.Drawing.Size(263, 301)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
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
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lanf58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def Label9Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass

	def Label7Click(self, sender, e):
		pass

	def Label8Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		price = float(self._textBox1.Text)
		paid = float(self._textBox2.Text)
		change = paid - price
		dollars = change // 1
		quarters = (change - dollars) // 0.25
		dimes = (change - (dollars + quarters * 0.25)) // 0.1
		nickels = (change - (dollars + quarters * 0.25 + (dimes * 0.1))) // 0.05
		pennies = (change - (dollars + quarters * 0.25 + (dimes * 0.1) + (nickels * 0.05))) // 0.01

		self._label9.Text = str(change)
		self._label4.Text = str(dollars)
		self._label5.Text = str(quarters)
		self._label6.Text = str(dimes)
		self._label7.Text = str(nickels)
		self._label8.Text = str(pennies)

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()