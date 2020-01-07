import string

uper_list = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
low_list = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
string_upercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
string_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

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
	def encrypteng(msg,shift):
		ret = ''
		for x in msg:
			if x in string_upercase:
				ind = string_upercase.index(x)
				ret += string_upercase[ind + shift]
			if x in string_lowercase:
				ind = string_lowercase.index(x)
				ret += string_lowercase[ind + shift]
			else:
				ret +=x
			return ret
	def decrypteng(msg,shift):
		ret = ''
		for x in msg:
			if x in string_upercase:
				ind = string_upercase.index(x)
				ret += string_upercase[ind - shift]
			if x in string_lowercase:
				ind = string_lowercase.index(x)
				ret += string_lowercase[ind - shift]
			else:
				ret +=x
			return ret