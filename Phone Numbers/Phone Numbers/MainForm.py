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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self._button4 = System.Windows.Forms.Button()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Location = System.Drawing.Point(12, 66)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(134, 23)
		self._label1.TabIndex = 0
		self._label1.Text = " "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Location = System.Drawing.Point(166, 89)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(129, 23)
		self._label2.TabIndex = 1
		self._label2.Text = " "
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Location = System.Drawing.Point(12, 112)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(134, 23)
		self._label3.TabIndex = 3
		self._label3.Text = " "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.Location = System.Drawing.Point(166, 135)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(129, 23)
		self._label4.TabIndex = 4
		self._label4.Text = " "
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label5.Location = System.Drawing.Point(12, 158)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(134, 24)
		self._label5.TabIndex = 5
		self._label5.Text = " "
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label5.Click += self.Label5Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button1.Location = System.Drawing.Point(12, 199)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(78, 23)
		self._button1.TabIndex = 6
		self._button1.Text = "Place"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.Info
		self._button2.Location = System.Drawing.Point(114, 199)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Number"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.InfoText
		self._button3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button3.Location = System.Drawing.Point(217, 199)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(78, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "Clear All"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label6.Location = System.Drawing.Point(38, 9)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(214, 43)
		self._label6.TabIndex = 9
		self._label6.Text = "Phone #'s"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Click += self.Label6Click
		# 
		# button4
		# 
		self._button4.ForeColor = System.Drawing.Color.Red
		self._button4.Location = System.Drawing.Point(12, 228)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(283, 23)
		self._button4.TabIndex = 10
		self._button4.Text = "Exit"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.Info
		self._label7.Location = System.Drawing.Point(166, 66)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(129, 23)
		self._label7.TabIndex = 11
		self._label7.Click += self.Label7Click
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.Info
		self._label8.Location = System.Drawing.Point(12, 89)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(134, 23)
		self._label8.TabIndex = 12
		self._label8.Click += self.Label8Click
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.Info
		self._label9.Location = System.Drawing.Point(166, 112)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(129, 23)
		self._label9.TabIndex = 13
		self._label9.Click += self.Label9Click
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.Info
		self._label10.Location = System.Drawing.Point(12, 135)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(134, 23)
		self._label10.TabIndex = 14
		self._label10.Click += self.Label10Click
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.Info
		self._label11.Location = System.Drawing.Point(166, 159)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(129, 23)
		self._label11.TabIndex = 15
		self._label11.Click += self.Label11Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.HotTrack
		self.ClientSize = System.Drawing.Size(306, 261)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Phone Numbers"
		self.ResumeLayout(False)


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

	def Label5Click(self, sender, e):
		pass

	def Label7Click(self, sender, e):
		pass

	def Label8Click(self, sender, e):
		pass

	def Label9Click(self, sender, e):
		pass

	def Label10Click(self, sender, e):
		pass

	def Label11Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text = "Rocky Rococo Pizza"
		self._label2.Text = "Sam's Pizza"
		self._label3.Text = "Italian House"
		self._label4.Text = "Culvers"
		self._label5.Text = "My Apartment"

	def Button2Click(self, sender, e):
		self._label7.Text = "(262) 473-2105"
		self._label8.Text = "(608) 757-1999"
		self._label9.Text = "(608) 754-2226"
		self._label10.Text = "(608) 758-8916"
		self._label11.Text = "(608) 752-9908"

	def Button3Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""

	def Button4Click(self, sender, e):
		Application.Exit()