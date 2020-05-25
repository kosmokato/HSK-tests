def test(dict_array):
	test_answer = 5
	test_opciones = []
	while(test_answer not in [0,1,2,3]):
		try:
			print("\nTEST-0\n------\n")
			print("What does it means \"" + dict_array[0]["chinese"] + "\" (" + dict_array[0]["pinyin"] + ")?")
			
			test_opciones = []
			test_opciones.append(dict_array[1]["translation"])
			test_opciones.append(dict_array[2]["translation"])
			test_opciones.append(dict_array[0]["translation"])
			test_opciones.append(dict_array[3]["translation"])

			for i in range(len(test_opciones)):
				print("\t[" + str(i) + "] " + test_opciones[i])
			test_answer = int(input("Choose an option:"))

			if test_opciones[test_answer] == dict_array[0]["translation"]: print("[+] 溜溜溜!")
			else: print("[-] Wrong answer! :_(\n\n")

			if test_answer in [0,1,2,3]: break  # valid option
			else: print("[i] Invalid answer! try again ;)\n\n")	
		except KeyboardInterrupt:
			exit()
		except: test_answer = 5  # Don't cry to me, just loop on