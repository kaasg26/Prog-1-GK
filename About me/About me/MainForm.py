import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Navy
		self._label1.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Location = System.Drawing.Point(66, 42)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(465, 89)
		self._label1.TabIndex = 0
		self._label1.Text = " "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Navy
		self._button1.ForeColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button1.Location = System.Drawing.Point(66, 151)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(175, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "About Me"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Navy
		self._button2.ForeColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button2.Location = System.Drawing.Point(219, 180)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(175, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Navy
		self._button3.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._button3.Location = System.Drawing.Point(356, 209)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(175, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self.ClientSize = System.Drawing.Size(630, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "About me"
		self.ResumeLayout(False)



	

	def Label1Click(self, sender, e):
		pass
	
	def Button1Click(self, sender, e):
		self._label1.Text = "My names Gavin Kaas, I play Hockey and like to do Metal arts"

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()