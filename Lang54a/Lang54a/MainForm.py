import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(35, 69)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(111, 198)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(7, 20)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(98, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "radioButton1"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(7, 51)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(98, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "radioButton2"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(7, 83)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(98, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "radioButton3"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(7, 113)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(98, 24)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "radioButton4"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 286)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(110, 286)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(209, 286)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(151, 102)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(153, 76)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "Miles"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(153, 139)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "Gallons"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(151, 165)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 7
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(153, 203)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 8
		self._label3.Text = "MPG"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Location = System.Drawing.Point(151, 226)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 9
		self._label4.Text = "label4"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(35, 13)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(216, 42)
		self._label5.TabIndex = 10
		self._label5.Text = "Cars MPG"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(297, 340)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Lang54a"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()

