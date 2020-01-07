import basem
import Caesar

class Interface:
	def main_print():
		print('1: Шифр Цезаря')
		print('1: Base(до 64)')

Interface.main_print()
value = input()
if value == '1':
	print('1:расшифровать')
	print('2:зашифровать')
	value = input()
	if value == 1:
		Caesar.decryptCaesar()