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
		self._label9 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._label17 = System.Windows.Forms.Label()
		self._label18 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._label1.ForeColor = System.Drawing.Color.MediumSpringGreen
		self._label1.Location = System.Drawing.Point(22, 69)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = " "
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label2.ForeColor = System.Drawing.Color.MediumSpringGreen
		self._label2.Location = System.Drawing.Point(22, 92)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = " "
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label3.ForeColor = System.Drawing.Color.MediumSpringGreen
		self._label3.Location = System.Drawing.Point(22, 115)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = " "
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(192, 64, 0)
		self._label4.ForeColor = System.Drawing.Color.MediumSpringGreen
		self._label4.Location = System.Drawing.Point(22, 138)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = " "
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._label5.ForeColor = System.Drawing.Color.MediumSpringGreen
		self._label5.Location = System.Drawing.Point(22, 161)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		self._label5.Text = " "
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(128, 64, 64)
		self._label6.ForeColor = System.Drawing.Color.MediumSpringGreen
		self._label6.Location = System.Drawing.Point(22, 184)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 5
		self._label6.Text = " "
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.FromArgb(64, 0, 64)
		self._label7.ForeColor = System.Drawing.Color.MediumSpringGreen
		self._label7.Location = System.Drawing.Point(22, 207)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 6
		self._label7.Text = " "
		self._label7.Click += self.Label7Click
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Purple
		self._label8.ForeColor = System.Drawing.Color.MediumSpringGreen
		self._label8.Location = System.Drawing.Point(22, 230)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 7
		self._label8.Text = " "
		self._label8.Click += self.Label8Click
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Black
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.SystemColors.Control
		self._label9.Location = System.Drawing.Point(22, 13)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(236, 46)
		self._label9.TabIndex = 8
		self._label9.Text = "Schedule"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label9.Click += self.Label9Click
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(152, 69)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(106, 70)
		self._button1.TabIndex = 9
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(152, 138)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(106, 69)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(152, 207)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(106, 46)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(152, 46)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(104, 69)
		self._button4.TabIndex = 0
		self._button4.Text = "Show"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(152, 115)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(104, 69)
		self._button5.TabIndex = 1
		self._button5.Text = "Clear"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.ForeColor = System.Drawing.Color.Red
		self._button6.Location = System.Drawing.Point(152, 184)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(104, 46)
		self._button6.TabIndex = 2
		self._button6.Text = "Exit"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label10.ForeColor = System.Drawing.Color.MintCream
		self._label10.Location = System.Drawing.Point(32, 46)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 3
		self._label10.Text = " "
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label11.ForeColor = System.Drawing.Color.MintCream
		self._label11.Location = System.Drawing.Point(32, 69)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 4
		self._label11.Text = " "
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label12.ForeColor = System.Drawing.Color.MintCream
		self._label12.Location = System.Drawing.Point(32, 92)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 5
		self._label12.Text = " "
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.FromArgb(192, 64, 0)
		self._label13.ForeColor = System.Drawing.Color.MintCream
		self._label13.Location = System.Drawing.Point(32, 115)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 6
		self._label13.Text = " "
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._label14.ForeColor = System.Drawing.Color.MintCream
		self._label14.Location = System.Drawing.Point(32, 138)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 7
		self._label14.Text = " "
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.FromArgb(128, 64, 64)
		self._label15.ForeColor = System.Drawing.Color.MintCream
		self._label15.Location = System.Drawing.Point(32, 161)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(100, 23)
		self._label15.TabIndex = 8
		self._label15.Text = " "
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.FromArgb(64, 0, 64)
		self._label16.ForeColor = System.Drawing.Color.MintCream
		self._label16.Location = System.Drawing.Point(32, 184)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(100, 23)
		self._label16.TabIndex = 9
		self._label16.Text = " "
		# 
		# label17
		# 
		self._label17.BackColor = System.Drawing.Color.Purple
		self._label17.ForeColor = System.Drawing.Color.MintCream
		self._label17.Location = System.Drawing.Point(32, 207)
		self._label17.Name = "label17"
		self._label17.Size = System.Drawing.Size(100, 23)
		self._label17.TabIndex = 10
		self._label17.Text = " "
		# 
		# label18
		# 
		self._label18.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label18.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label18.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label18.Location = System.Drawing.Point(32, 13)
		self._label18.Name = "label18"
		self._label18.Size = System.Drawing.Size(224, 30)
		self._label18.TabIndex = 11
		self._label18.Text = "Schedule"
		self._label18.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDark
		self.ClientSize = System.Drawing.Size(284, 243)
		self.Controls.Add(self._label18)
		self.Controls.Add(self._label17)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Name = "MainForm"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)



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

	def Label6Click(self, sender, e):
		pass

	def Label7Click(self, sender, e):
		pass

	def Label8Click(self, sender, e):
		pass
	
	def Label9Click(self, sender, e):
		pass
	
	def Button1Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Button4Click(self, sender, e):
		self._label10.Text = "Adv Art Metals"
		self._label11.Text = "Symphonic Band"
		self._label12.Text = "Computer Prog"
		self._label13.Text = "Algabra 2"
		self._label14.Text = "Ap US History"
		self._label15.Text = "English 10"
		self._label16.Text = "Health"
		self._label17.Text = "Chemistry"

	def Button5Click(self, sender, e):
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""
		self._label15.Text = ""
		self._label16.Text = ""
		self._label17.Text = ""


	def Button6Click(self, sender, e):
		Application.Exit()