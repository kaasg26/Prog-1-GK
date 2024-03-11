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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(7, 193)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Solve"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(83, 193)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(7, 222)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(151, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(58, 37)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Location = System.Drawing.Point(57, 128)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 4
		self._label1.Click += self.Label1Click
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(58, 63)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(58, 89)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		self._textBox3.TextChanged += self.TextBox3TextChanged
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(7, 40)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(45, 17)
		self._label2.TabIndex = 7
		self._label2.Text = "A"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(7, 63)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(45, 20)
		self._label3.TabIndex = 8
		self._label3.Text = "B"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(7, 89)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(45, 20)
		self._label4.TabIndex = 9
		self._label4.Text = "C"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 123)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(39, 23)
		self._label5.TabIndex = 10
		self._label5.Text = "Roots"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label6.Location = System.Drawing.Point(57, 155)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 11
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label7.ForeColor = System.Drawing.SystemColors.HighlightText
		self._label7.Location = System.Drawing.Point(7, 9)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(151, 23)
		self._label7.TabIndex = 12
		self._label7.Text = "Roots Calculator"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self.ClientSize = System.Drawing.Size(166, 261)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang58b"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox3TextChanged(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		
		a = float(self._textBox1.Text)
		b = float(self._textBox2.Text)
		c = float(self._textBox3.Text)
		ac = a * c
		
		Root1 = -b + math.sqrt(b ** 2 - 4 * ac)
		Rt1 = Root1 / 2 * a
		Root2 = -b - math.sqrt(b ** 2 - 4 * ac)
		Rt2 = Root2 / 2 * a
		
		self._label1.Text = str(Rt1)
		self._label6.Text = str(Rt2)
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label1.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass