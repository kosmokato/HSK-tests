import random
import os, sys

def quiz(dict_array):
	quiz_answer = 5
	quiz_options = []
	i = random.randint(0,len(dict_array)-1)
	while(quiz_answer not in [0,1,2,3]):
		try:
			print("\nQUIZ\n-----\n")
			print("What does it means \"" + dict_array[i]["chinese"] + "\" (" + dict_array[i]["pinyin"] + ")?")
			
			quiz_options = []
			
			answers = set()
			answers.add(i)  # the right one
			while len(answers) < 4:
				answers.add(random.randint(0, len(dict_array)-1))

			for x in answers:  # add the answers to the quiz
				quiz_options.append(dict_array[x]["translation"])  

			random.shuffle(quiz_options)

			for x in range(len(quiz_options)):
				print("\t[" + str(x) + "] " + quiz_options[x])
			quiz_answer = int(input("Choose an option:"))

			if quiz_options[quiz_answer] == dict_array[i]["translation"]: print("[+] 六六六!")
			else: 
				print("[-] Wrong answer! :_(")
				print("    The right answer was \"" + dict_array[i]["translation"] + "\"\n\n")

			if quiz_answer in [0,1,2,3]: break  # valid option, end for now  <---- THIS MUST BE CHANGED
			else: 
				print("[i] Invalid answer! try again ;)\n\n")	
		except KeyboardInterrupt:
			exit()  # if Ctrl+C, abort
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print("[-] Error: " + str(e))
			print(exc_type, fname, exc_tb.tb_lineno)
			break #quiz_answer = 5  # Don't cry to me, just loop on