
class xor:
	cryptstr = [ ord(x) for x in \
			"\x78\x2E\x2F\x8F\x65\x8C\xD9\xD3\xD0\x33\x45\xED\x74\xBD\x8E\x5B\x6E\x9E\x2C\x71" \
			"\xAF\x72\x33\xF5\x84\x0C\xA9\xC7\x29\x85\xAE\xAD\x97\xEE\x0A\xD5\x4F\x2F\x5F\x60" \
			"\x18\x1A\x06\x90\xFF\xD5\x9E\x8E\xE0\xD0\x7B\x38\x71\x3F\x49\x3A\x0C\x1D\x1E\x29" \
			"\xB2\x96\xD2\x8C\x15\xF7\xB0\xEF\xA5\x26\x48\x36\xBE\x08\xE0\x16\x4D\x35\x1D\x30" \
			"\x22\x48\xDD\x11\xB5\x8E\x39\xCD\xF7\xDE\x70\x6E\xF8\x56\x03\x1F\xAD\x08\x4E\xFB" \
			"\x2A\x7C\x1E\x30\x19\xDF\x3F\x96\x8F\xE4\x54\x36\xC6\xBD\xA5\x42\xD0\xED\x5D\xD7" \
			"\xB5\x98\xF1\xE5\xBF\xB1\x9E\xE6\x48\x34\xC7\xDC\x1C\xFF\x6A\x08\xA7\x1B\x91\xFE" \
			"\x4A\x27\x5C\x2C\xA4\xB5\x06\x2E\xBB\xC5\xDB\x6F\x41\xD9\x15\x6E\xFD\xAD\x0E\xE7" \
			"\x63\x56\xB5\xCD\xD6\xE4\x28\x27\x8E\x46\x6E\x7F\x05\x8D\x5F\xFD\xC1\x6F\xD0\xBA" \
			"\x98\x80\x3A\x76\xBF\xC7\x0D\x53\x14\x63\x8B\xD7\x21\xA9\xB5\x3D\x05\xD4\x03\x9F" \
			"\x63\x25\xB8\x3C\xB9\x71\x12\xB7\x66\x7F\x5C\x9F\x32\x13\xCB\x36\x4E\x78\x10\xA3" \
			"\xFB\x3D\x8C\x5B\xD3\xC2\x39\x49\xD5\xEB\xEF\xCC\xEA\x38\xFA\x75\x4E\x09\x50\x30" \
			"\xDB\x71\xF0\x9C\x7A\x46\xF2\x92\xB4\x32\x9E\xD6\x66\xC9\xB6\x6D\x4F\xCF\x24\x6F" \
			"\x78\x3D\x6B\xF4\x72\x03\xA0\x19\x5F\x08\x22\x3B\xC9\x58\x9A\xA5\x92\xEA\xDA\x63" \
			"\x5D\xD8\x34\x54\x0C\xC4\xF0\x06\x93\x51\x4B\x60\xAF\xFE\x6C\x1D\xEB\x92\x66\x24" \
			"\x74\x3A\x57\xF3\x46\xE2\xF6\xA5\x08\x6E\x4F\xAE\xB4\x69\xA6\x8F\x3B\xDB\x95\x5B" \
			"\x65\xB3\x6F\x12\xFC\x0A\x23\x21\xE0\xDB\x2A\x5D\x83\xA4\xA7\x6A\xAF\x4C\x0B\xFF" \
			"\xFA\x24\x6F\x75\x86\x5B\xC8\xB9\xF6\x1F\x63\x62\x27\xC1\xF4\x73\xC4\x11\x05\x87" \
			"\x0B\x37\xAB\x23\x26\x53\xAA\xD9\x80\x33\x42\x64\xFA\x7F\x88\x58\x73\x40\x09\x93" \
			"\xAF\x7E\x6D\x1B\x78\x23\x5D\xD0\x9B\xC6\xFA\x89\x00\x8F\xAB\x16\x4D\x30\x7A\xC1" \
			"\xBF\x61\xD7\x2E\xE4\xF3\x53\xBE\xEC\x01\x59\x8A\xFA\x48\x29\x93\x44\x84\x77\x80" \
			"\x1F\x42\xBF\x01\xE0\x51\xE7\x67\x9F\xDF\x8D\xE5\xD5\xCD\x61\xAA\xE3\x07\xA9\x35" \
			"\x83\x01\x96\xAF\xB0\xE6\xBB\x8A\xEC\x3F\xE9\x1F\x69\xCE\x5D\x3A\xD4\x13\xDF\xA2" \
			"\x21\x71\x98\xC5\x12\x5B\x39\x4D\xDA\x30\x88\xD5\x19\x86\x01\x5A\x3E\x46\x7B\xB0" \
			"\xD0\xB9\x47\x81\x51\x83\x1F\xAD\x1C\xE7\xF9\xB7\xB0\x96\x99\xDA\x8D\x65\x6C\x5D" \
			"\x3B\xF2\xE8\x3E\xAA\x9F\x43\x31\xFD\xD3\x06\x2C\x15\x46\xA2\x95\x0C\x5B\x7B\xE7" \
			"\x55\x92\x8F\x36\xEE\x2E\x84\x87\x71\xFF\xE9\xD5\x52\x41\x09\x04\xD8\xA4\xF3\x43" \
			"\x77\xD0\xFC\xBB\x68\x01\xB8\x5D\xF2\xC5\xBD\xD2\xCA\xA1\x8A\xF1\xD7\x11\xC6\x8F" \
			"\xA4\x91\xEA\x4F\x9C\x82\xE7\xD5\x7F\x3E\x5E\x65\x4B\x73\x60\x02\x1E\x2F\x77\x5A" \
			"\x6D\xB6\x35\x6C\xE0\x60\x3F\xB5\x16\xB0\x93\x47\x67\xC8\xD8\x7B\xD1\xD9\xBD\x03" \
			"\x46\x3D\x95\xDB\xF6\x8D\xF3\x51\xBF\x88\x62\x4E\x84\x27\x53\xE2\x1C\xA4\x9C\x66" \
			"\x3D\x85\x29\x8F\xD8\x33\xB4\x42\x6B\xC0\x94\x98\x61\xB1\x58\xF8\x47\x11\x9E\x23" \
			"\x16\xE2\x50\x65\x13\x23\xDA\x4A\x2A\x38\x77\xBF\x08\x47\x1A\x61\xF2\xD8\xDC\xED" \
			"\xB4\x39\x49\x57\xB5\x5B\x06\x93\x73\x8A\xD9\x59\xAA\x6F\x15\x02\xE4\x1D\x88\xF3" \
			"\x04\x67\x1F\x68\x85\xCA\x8B\xDB\x1C\x76\x1A\x8E\x94\x62\x4F\xBC\x57\x00\xB0\xEF" \
			"\xA4\xD4\x54\x48\xA9\x8D\x2B\xA2\xE5\xEB\x85\xE1\xBC\x87\xB8\x67\xA5\xAE\x93\x02" \
			"\xF9\xB3\xD6\xAE\x91\x22\xF1\x39\x1B\x66\xC9\xA0\x9A\x3B\xDB\x68\xCA\x94\x03\x70" \
			"\xF1\x02\xB1" \
			]

	cryptlen=len(cryptstr)
	
	def __init__(self):
		self.crypt_idx=0
	
	def encode(self,msg):
		result=""
		length=len(msg)
		index=0
		while index<length:
			result+= chr(ord(msg[index:index+1]) ^ xor.cryptstr[self.crypt_idx])
			index+=1
			self.crypt_idx+=1
			if self.crypt_idx==xor.cryptlen:
				self.crypt_idx=0
		return result