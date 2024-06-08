class Turtles:
	x=0
	y=0
	s=1
	def __init__(self,startX,startY,step):
		self.x=startX
		self.y=startY
		self.s=step
	def go_up(self):
		self.y+=self.s
	def go_down(self):
		self.y-=self.s
	def go_left(self):
		self.x-=self.s
	def go_right(self):
		self.x+=self.s
	def evolve(self):
		self.s+=1
	def degrade(self):
		if self.s-1>0:
			self.s-= 1
		else:
			raise ValueError('шаг не может быть меньше 1')
	def count_moves(self,x2,y2):
			ax=abs(self.x-x2)
			ay=abs(self.y-y2)
			if ax==ay:# движемся по диагонали
				if ax%self.s==0:
					return ax//self.s
				else:
					return (ax//self.s)+1
			else:#идем отдельно по осям
				v=(abs(self.x-x2)+abs(self.y-y2))
				if v%self.s==0:
					return v//self.s
				else:#неполный шаг
					return (v//self.s)+1
