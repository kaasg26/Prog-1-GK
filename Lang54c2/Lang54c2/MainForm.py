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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 47)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(236, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate "
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 76)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(236, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(12, 105)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(236, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(148, 153)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label2.Location = System.Drawing.Point(148, 196)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label3.Location = System.Drawing.Point(148, 239)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 6
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(13, 156)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Radius"
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(13, 196)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "Area"
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(13, 239)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "Circumference "
		self._label6.Click += self.Label6Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self.ClientSize = System.Drawing.Size(259, 318)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang54c2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		
		pi = int(3.14159)
		
		radius = float(self._textBox1.Text)
		# calculate area here ...
		
		area = pi * radius ** 2
		area = round(area, 3)
		# round area to 3 decimal places
		circ = 2 * pi * radius
		
		self._label2.Text = str(area)
		self._label3.Text = str(circ)
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def TextBox1TextChanged(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass