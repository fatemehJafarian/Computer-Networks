import math
import sys

def Zero_Padd(var):
	l = len(var)
	for i in range(8 - l):
		var = '0' + var
	return var

try:
	f = open('private.key', 'r')
	d = int(f.readline())
	n = int(f.readline())
finally:
	f.close()
try:
	pass
except:
	print('Key file does not exist or the path is wrong!')
try:
	fi = open("input.txt.enc", 'rb')
	fo = open("output.txt", 'wb')
except:
	print('Input file does not exist or the path is wrong!')
finally:
	dyc_msg = []
	l = math.ceil(math.log(n, 256))
	tmp = fi.read(1)
	l_byte = bin(ord(tmp))[2:]
	l_byte = Zero_Padd(l_byte)
	for i in range(l-1):
		t = bin(ord(fi.read(1)))[2:]
		t = Zero_Padd(t)
		l_byte = l_byte + t 
	C = int(l_byte, 2)
	sys.stdout.write(str(l))
	while len(tmp) != 0:
		M = pow(C, d) % n
		dyc_msg.append(M)
		tmp = fi.read(1)
		if len(tmp) == 0:
			continue
		l_byte = bin(ord(tmp))[2:]
		l_byte = Zero_Padd(l_byte)
		for i in range(l-1):
			t = bin(ord(fi.read(1)))[2:]
			t = Zero_Padd(t)
			l_byte = l_byte + t
		C = int(l_byte, 2)
	dyc_msg = bytes(dyc_msg)
	fo.write(dyc_msg)
	fi.close()
	fo.close()