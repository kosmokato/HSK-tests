import random
import os, sys

def quiz(dict_array, language):
	right_ones = 0
	quiz_answer = 5

	# STRINGS
	if language == 2:
		what_does_it_mean = "\nWhat does it means \""
		choose_an_option = "Choose an option:"
		you_won_5_pts = "    You won 5 points! ["
		wrong_answer = "[-] Wrong answer! :_("
		the_right_answer_was = "    The right answer was \""
		you_made_x_points_1 = "You made "
		you_made_x_points_2 = " points!"
		invalid_answer = "[i] Invalid answer! try again ;)\n\n"
		msg_error = "[-] Error: "
	elif language == 3:
		what_does_it_mean = "\n¿Qué significa \""
		choose_an_option = "Escoge una opción:"
		you_won_5_pts = "    ¡Has ganado 5 puntos! ["
		wrong_answer = "[-] ¡Respuesta incorrecta! :_("
		the_right_answer_was = "    La respuesta correcta era \""
		you_made_x_points_1 = "¡Lograste "
		you_made_x_points_2 = " puntos!"
		invalid_answer = "[i] ¡Respuesta no válida! Prueba de nuevo ;)\n\n"
		msg_error = "[-] Error: "
	elif language == 4:
		what_does_it_mean = "\nЧто это значит \""
		choose_an_option = "Выберите опцию:"
		you_won_5_pts = "    Вы выиграли 5 очков! ["
		wrong_answer = "[-] Неверный ответ! :_("
		the_right_answer_was = "    Правильный ответ был \""
		you_made_x_points_1 = "Вы достигли "
		you_made_x_points_2 = " очков!"
		invalid_answer = "[i] Неверный ответ! Попробуйте еще раз ;)\n\n"
		msg_error = "[-] Oшибка: "
	else:
		print('[-] Error: language not found')
		exit()

	print("\nQUIZ\n-----\n")
	while(quiz_answer not in [0,1,2,3]):
		i = random.randint(0,len(dict_array)-1)
		try:
			print(what_does_it_mean + dict_array[i]["chinese"] + "\" (" + dict_array[i]["pinyin"] + ")?")

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
			quiz_answer = int(input(choose_an_option))

			if quiz_options[quiz_answer] == dict_array[i]["translation"]: 
				print("[+] 六六六!")
				right_ones += 1
				print(you_won_5_pts + str(right_ones * 5) + "]\n")
			else: 
				print(wrong_answer)
				print(the_right_answer_was + dict_array[i]["translation"] + "\"\n")
				print(you_made_x_points_1 + str(right_ones * 5) + you_made_x_points_2)
				print("祝您下次运气更好 ^_^")
				exit()  # <---- THIS MUST BE CHANGED

			if quiz_answer in [0,1,2,3]: quiz_answer = 5  # <---- THIS MUST BE CHANGED
			else: 
				print(invalid_answer)
				
		except KeyboardInterrupt: exit()  # if Ctrl+C, abort
		except ValueError: pass
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(msg_error + str(e))
			print(exc_type, fname, exc_tb.tb_lineno)
			break #quiz_answer = 5  # Don't cry to me, just loop on