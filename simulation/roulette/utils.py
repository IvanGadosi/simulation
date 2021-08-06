import random


class Player:
	def __init__(self, num_turns, money, bet, name):
		self.num_turns=num_turns
		self.money=money
		self.bet=bet
		self.name=name

		self.turns=[]
		self.data_dict={}

	def __str__(self):
		return self.name
		
	def create_turns(self):
		roulette_nums=[num for num in range(15)]
		for _ in range(self.num_turns):
			turn_color=''
			turn_num=random.choice(roulette_nums)

			if turn_num==0:
				turn_color='green'
			elif turn_num % 2 ==0:
				turn_color='red'
			elif turn_num % 2 ==1:
				turn_color='black'

			self.turns.append(turn_color)

	def play(self):
		turn_list=[]
		m_list=[]
		for i in range(len(self.turns)-1):
			if i%(self.num_turns//50)==0:
				turn_list.append(i)
				m_list.append(self.money)
			if self.turns[i]=='black':
				if self.turns[i+1]=='red':
					self.money+=self.bet
				else:
					self.money-=self.bet
			elif self.turns[i]=='red':
				if self.turns[i+1]=='black':
					self.money+=self.bet
				else:
					self.money-=self.bet

		self.data_dict=dict(zip(turn_list,m_list))