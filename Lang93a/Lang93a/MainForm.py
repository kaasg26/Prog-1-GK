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
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(57, 171)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(164, 171)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(57, 207)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "label3"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(164, 207)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "label4"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(57, 243)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "label5"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(164, 243)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 5
		self._label6.Text = "label6"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(57, 303)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 6
		self._label7.Text = "label7"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(164, 303)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 7
		self._label8.Text = "label8"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(330, 362)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang93a"
		self.ResumeLayout(False)

