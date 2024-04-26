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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(87, 36)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(87, 71)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(68, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "First Name:"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 71)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(68, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Last Name:"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SeaShell
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(13, 128)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(174, 69)
		self._label3.TabIndex = 4
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 105)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(109, 23)
		self._label4.TabIndex = 5
		self._label4.Text = "This is your full name:"
		self._label4.Click += self.Label4Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(19, 206)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(48, 23)
		self._button1.TabIndex = 6
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(73, 206)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(48, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Erase"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(127, 206)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(48, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Silver
		self.ClientSize = System.Drawing.Size(199, 241)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Pg119FullName"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label4Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass