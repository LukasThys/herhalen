b=1
def actie():
	text=input("Welke tekst moet ik herhalen?: ")
	a=input("hoe vaak moet ik deze tekst herhalen?: ")
	a=int(a)
	print('\n')
	def prtn():
		print(text)

	while a>=1:
		a=a-1
		prtn()

actie()