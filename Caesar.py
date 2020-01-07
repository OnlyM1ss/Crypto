uper_list = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
low_list = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
class Caesar: 
	def encryptCaesar(msg,shift): 
		ret = '' 
		for x in msg: 
			if x in low_list:
				ind = low_list.index(x)
				ret += low_list[ind + shift]
			if x in uper_list: 
				ind = uper_list.index(x)
				ret += uper_list[ind + shift]
			else: 
				ret+=x
		return ret
	def decryptCaesar(msg,shift):
		ret = ''
		for x in msg:
			if x in low_list:
				ind = low_list.index(x)
				ret +=low_list[ind - shift]
			if x in uper_list:
				ind = uper_list
				ret = uper_list[ind - shift]
			else:
				ret+=x
		return ret