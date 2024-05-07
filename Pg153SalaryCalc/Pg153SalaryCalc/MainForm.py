import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(101, 208)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DimGray
		self._label1.Location = System.Drawing.Point(18, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(113, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Annual Pay:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DimGray
		self._label2.Location = System.Drawing.Point(18, 102)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(113, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Pay periods per year:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DimGray
		self._label3.Location = System.Drawing.Point(18, 137)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(113, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Salery per pay period:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg153SalaryCalc"
		self.ResumeLayout(False)

