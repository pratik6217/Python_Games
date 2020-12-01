import random

def left():
	l = ["You went to the river...Do you want to go across it or walk along the banks of the river (across/walk) ?", 
	"You saw a butterfly...follow it or leave it (follow/leave) ?",
	"You saw your friend trapped Help him/her or leave it (help/leave) ?",
	]

	return random.choice(l)

def right():
	r = ["You fell from a cliff and died :( ",
	"Jungle or a beach (jungle/beach) ?",
	"You met a Bear....run or pretend to be dead (run/dead) ?",
	]

	return random.choice(r)


name = input("Please enter your name:")
age = int(input(("Please enter your age:")))

if age < 18:
	print("You are not eligible to play the game :(")

elif age >= 18:
	print("You are Eligible :)")
	ch = input("Do You want to play ?").lower()
	if ch == "yes":
		right_or_left = input("Enter your first choice: right or left ?").lower()
		if right_or_left == "left":
			l1 = left()
			if "river" in l1:
				print(l1)
				choice = input()
				if choice == "across":
					across = ["You went across and found an abandoned house.... go inside or leave it (in/leave) ?",
					"You met your soulmate and you lived happily after :)",
					"You got hyperthermia while swimming across the river and you died :(",
					]
					l2 = random.choice(across)
					if "abandoned" in l2:
						choice = input().lower()
						if choice == "in":
							print("You went inside a witch's house and she ate you !\n" + "Better Luck next time....")
							
						elif choice == "leave":
							print("A wild animal suddenly appeared Run to the abanoned house or stand there (run/stand) ?")
							choice = input().lower()
							if choice == "run":
								print("You went inside a witch's house and she ate you !\n" + "Better Luck next time....")
								
							elif choice == "stand":
								print("The animal ate you !\n"+ "Better Luck next time.....")
						else:
							print(l2)
							
				elif choice == "walk":
					print("There was a family of corocodiles waiting for you along the banks of the river :(")
								
					
				


			elif "butterfly" in l1:
				print(l1)
				choice = input().lower()
				if choice == "follow":
					b = ["You followed it into the deep jungle and you got lost :(",
					"While following it you fell into a trap :(",
					]
					l2 = random.choice(b)
					print(l2)
					
				elif choice == "leave":
					b = ["You saw a tree and you feel tired rest under it or keep walking (rest/walk) ?"]
					print(b[0])
					choice = input().lower()
					if choice == "rest":
						print("While you were resting a snike bit you and you died :(")
						
					elif choice == "walk":
						w = ["You died due to intensive walking for a long period....",
						"You finally reached your destination....Congractulations You won !!!"
						]
						l2 = random.choice(w)
						print(l2)
						

			elif "friend" in l1:
				print(l1)
				choice = input().lower()
				if choice == "help":
					print("When you went to help your friend you found out it was god in disguise testing you and granted you eternal peace :)")
					
				elif choice == "leave":
					print("Your friend was just pretending to be trapped to test you and you failed in that :(")
					


		elif right_or_left == "right":
			r1 = right()
			print(r1)
			if "fell" in r1:
				print("Better Luck next time !!!")
				
			elif "jungle" in r1:
				choice = input().lower()
				if choice == "jungle":
					print(random.choice(["You went inside the jungle and got eaten up by wild animals", "Due to high humidity of the jungle you died :(", "You found a tree house there and lived happily after :)"]))
					
				elif choice == "beach":
					print("There was lighting at the beach which caused tsunami and you died !!!" )
					
			elif "Bear" in r1:
				choice = input().lower()
				if choice == "run":
					print("The bear caught you and ate you !!")
				elif choice == "dead":
					print("You fooled the bear, Congractulations")
					

	else:
		print("Bye, Have a great day !")
