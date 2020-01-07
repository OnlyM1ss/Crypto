import base64

class Base:
	def base16_encode(msg):
		ret = ''
		ret = base64.b16encode(bytes(msg,'utf-8'))
		return ret
	def base32_encode(msg):
		ret = ''
		ret = base64.b32encode(bytes(msg,'utf-8'))
		return ret 
	def base64_encode(msg):
		ret = ''
		ret = base64.b64encode(bytes(msg, 'utf-8'))
		return ret
	def base16_decode(msg):
		ret = ''
		ret = base64.b16decode(msg)
		return ret
	def base16_decode(msg):
		ret = ''
		ret = base64.b32decode(msg)
		return ret
	def base16_decode(msg):
		ret = ''
		ret = base64.b64decode(msg)
		return ret