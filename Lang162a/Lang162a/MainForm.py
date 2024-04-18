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
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(261, 155)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(261, 185)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(261, 215)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(31, 30)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(31, 53)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "label1"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(31, 76)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "label2"
		self._label2.Click += self.Label2Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(353, 260)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		n = int(self._textBox1.Text)
		def factorial(n):
			if (n==1 or n==0):
  				return 1

			else:
  				n * factorial(n - 1)

		num = n
		N = ("Factorial of",num,"is",factorial(num))
		self._label2.Text = str(N)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()