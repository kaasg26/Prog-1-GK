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
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(28, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(460, 86)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(28, 164)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(126, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Quote"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(28, 193)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(126, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(28, 222)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(126, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(246, 115)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(194, 23)
		self._label2.TabIndex = 4
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label2.Click += self.Label2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ScrollBar
		self.ClientSize = System.Drawing.Size(520, 261)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Favorite Quote"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text = "Nobody makes mistakes, just happy little accidents."
		self._label2.Text = "- Bob Ross"

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()