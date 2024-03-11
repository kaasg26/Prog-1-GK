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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(22, 14)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Length:"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(22, 46)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Width:"
		self._label2.Click += self.Label2Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(176, 14)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(128, 20)
		self._textBox1.TabIndex = 2
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(176, 46)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(128, 20)
		self._textBox2.TabIndex = 3
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(22, 76)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Area:"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(22, 108)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 5
		self._label4.Text = "Perimeter:"
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(176, 76)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(128, 23)
		self._label5.TabIndex = 6
		self._label5.Text = " "
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(176, 108)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(128, 23)
		self._label6.TabIndex = 7
		self._label6.Text = " "
		self._label6.Click += self.Label6Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ScrollBar
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(22, 151)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(138, 49)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ScrollBar
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(166, 151)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(138, 49)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ScrollBar
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(22, 206)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(282, 33)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.InactiveCaption
		self.ClientSize = System.Drawing.Size(329, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog52a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()




	def Button1Click(self, sender, e):
		length = int(self._textBox1.Text)
		width = int(self._textBox2.Text)
		area = length * width
		perim = 2 * length + 2 * width
		self._label5.Text = str(area)
		self._label6.Text = str(perim)
		# + - * /   **pow   //divide round down
		#int (intiger): a whole number pos/neg
		#float (floating-point number): any number with a decimal
		#str (string): a string of text
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label5Click(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass