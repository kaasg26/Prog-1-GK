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
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(167, 26)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(25, 31)
		self._button1.TabIndex = 0
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(198, 26)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(25, 31)
		self._button2.TabIndex = 6
		self._button2.Text = "-"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(229, 26)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(25, 31)
		self._button3.TabIndex = 7
		self._button3.Text = "="
		self._button3.UseVisualStyleBackColor = True
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(167, 63)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(25, 31)
		self._button4.TabIndex = 8
		self._button4.Text = "+"
		self._button4.UseVisualStyleBackColor = True
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(198, 63)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(25, 31)
		self._button5.TabIndex = 9
		self._button5.Text = "+"
		self._button5.UseVisualStyleBackColor = True
		# 
		# button6
		# 
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(229, 63)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(25, 31)
		self._button6.TabIndex = 10
		self._button6.Text = "+"
		self._button6.UseVisualStyleBackColor = True
		# 
		# button7
		# 
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(167, 100)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(87, 23)
		self._button7.TabIndex = 11
		self._button7.Text = "MOD"
		self._button7.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self._button7.UseVisualStyleBackColor = True
		# 
		# button8
		# 
		self._button8.Location = System.Drawing.Point(167, 141)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(87, 23)
		self._button8.TabIndex = 12
		self._button8.Text = "Calculate"
		self._button8.UseVisualStyleBackColor = True
		# 
		# button9
		# 
		self._button9.Location = System.Drawing.Point(167, 171)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(87, 23)
		self._button9.TabIndex = 13
		self._button9.Text = "Clear"
		self._button9.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Aquamarine
		self._label1.Font = System.Drawing.Font("Mistral", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Red
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 29)
		self._label1.TabIndex = 14
		self._label1.Text = "It's Simple"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(29, 63)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 15
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(29, 100)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 16
		self._label3.Text = "label3"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(29, 140)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 17
		self._label4.Text = "label4"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Teal
		self.ClientSize = System.Drawing.Size(284, 226)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg140SimpleCalc"
		self.ResumeLayout(False)

