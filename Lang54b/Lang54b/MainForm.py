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
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.Window
		self._textBox1.Location = System.Drawing.Point(112, 71)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(112, 97)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(112, 123)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 2
		self._textBox3.TextChanged += self.TextBox3TextChanged
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(112, 149)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 3
		self._textBox4.TextChanged += self.TextBox4TextChanged
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(6, 217)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(83, 23)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(129, 217)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(83, 23)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(6, 246)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(206, 23)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label1.Location = System.Drawing.Point(6, 71)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 7
		self._label1.Text = "Number One"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label2.Location = System.Drawing.Point(6, 97)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 8
		self._label2.Text = "Number Two"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label3.Location = System.Drawing.Point(6, 123)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 9
		self._label3.Text = "Number Three"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label4.Location = System.Drawing.Point(6, 149)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 10
		self._label4.Text = "Number Four"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ScrollBar
		self._label5.Location = System.Drawing.Point(112, 176)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 11
		self._label5.Text = "Sum"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label6.Location = System.Drawing.Point(12, 9)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(203, 48)
		self._label6.TabIndex = 12
		self._label6.Text = "Sum Calculator"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlText
		self.ClientSize = System.Drawing.Size(217, 289)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass
	
	def Label2Click(self, sender, e):
		pass
	
	def TextBox2TextChanged(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox3TextChanged(self, sender, e):
		pass

	def TextBox4TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		One = int(self._textBox1.Text)
		Two = int(self._textBox2.Text)
		Three = int(self._textBox3.Text)
		Four = int(self._textBox4.Text)
		Sum = One + Two + Three + Four
		self._label5.Text = str(Sum)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label5.Text = "Sum"

	def Button3Click(self, sender, e):
		Application.Exit()