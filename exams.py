import random
import os, sys

def quiz(dict_array):
	right_ones = 0
	quiz_answer = 5
	quiz_options = []
	print("\nQUIZ\n-----\n")
	while(quiz_answer not in [0,1,2,3]):
		i = random.randint(0,len(dict_array)-1)
		try:
			print("\nWhat does it means \"" + dict_array[i]["chinese"] + "\" (" + dict_array[i]["pinyin"] + ")?")
			
			quiz_options = []
			
			answers = set()
			answers.add(i)  # the right one
			while len(answers) < 4:
				answers.add(random.randint(0, len(dict_array)-1))

			for x in answers:
				quiz_options.append(dict_array[x]["translation"])  

			random.shuffle(quiz_options)

			for x in range(len(quiz_options)):
				print("\t[" + str(x) + "] " + quiz_options[x])
			quiz_answer = int(input("Choose an option:"))

			if quiz_options[quiz_answer] == dict_array[i]["translation"]: 
				print("[+] 六六六!")
				right_ones += 1
				print("    You won 5 points! [" + str(right_ones * 5) + "]\n")
			else: 
				print("[-] Wrong answer! :_(")
				print("    The right answer was \"" + dict_array[i]["translation"] + "\"\n")
				print("You made " + str(right_ones * 5) + " points!")
				print("祝您下次运气更好 ^_^")
				exit()  # <---- THIS MUST BE CHANGED

			if quiz_answer in [0,1,2,3]: quiz_answer = 5  # <---- THIS MUST BE CHANGED
			else: 
				print("[i] Invalid answer! try again ;)\n\n")
				
		except KeyboardInterrupt: exit()  # if Ctrl+C, abort
		except ValueError: pass
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print("[-] Error: " + str(e))
			print(exc_type, fname, exc_tb.tb_lineno)
			break #quiz_answer = 5  # Don't cry to me, just loop on