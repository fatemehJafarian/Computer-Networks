import math
import sys

try:
	f = open('public.key', 'r')
	e = int(f.readline())
	n = int(f.readline())
finally:
	f.close()
try:
	pass
except:
	print('Key file does not exist or the path is wrong!')
try:
	fi = open("input.txt", 'rb')
	fo = open("input.txt.enc", 'wb')
except:
	print('Input file does not exist or the path is wrong!')
finally:
	enc_msg = []
	byte = fi.read(1)
	l = math.ceil(math.log(n, 256))
	sys.stdout.write(str(l))
	while len(byte) != 0:
		M = ord(byte)
		C = pow(M, e) % n
		tmp = (bin(C))[2:]
		for i in range(8*l - len(tmp)):
			tmp = '0' + tmp
		for i in range(l):
			enc_msg.append(int(tmp[i*8:(i+1)*8], 2))
		byte = fi.read(1)
	enc_msg = bytes(enc_msg)
	fo.write(enc_msg)
	fi.close()
	fo.close()