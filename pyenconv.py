import sys, getopt, cchardet
def pyenconv(string, f = None, t = 'utf-8'):
	if f == None:
		f = cchardet.detect(string)['encoding']
	return string.decode(f).encode(t)
if __name__ == '__main__':
	opts, args = getopt.gnu_getopt(sys.argv, "hi:o:f:t:rw", ["help", "input=", "output=", "from=", "to=", "rewrite", "write"])
	i = ""
	o = ""
	f = None
	t = 'utf-8'
	r = False
	w = False
	for opt, arg in opts:
		if opt in ('-h', "--help"):
			print("""Python Encoding Converter\n
Usage: pyenconv [-h | --help] [-i inputfile | --input=inputfile] [-o outputfile | --output=outputfile] [-f encoding | --from=encoding] [-t encoding | --to=encoding] [-r | --rewrite] [-w | --write]\n
-h | --help\tDisplay help. 显示帮助。
-i | --input\tSet the input file. 设置输入文件。
-o | --output\tSet the output file. 设置输出文件。
-f | --from\tSet the encoding of the input file. 设置输入文件编码。
-t | --to\tSet the encoding of the output file. 设置输出文件编码。
-r | --rewrite\tRewrite the content to the original file. 将内容重写到原文件。
-w | --write\tWrite the content to the screen. 将内容输出到屏幕。""")
			sys.exit()
		elif opt in ('-i', '--input'):
			i = arg
		elif opt in ('-o', '--output'):
			o = arg
		elif opt in ('-f', '--from'):
			f = arg
		elif opt in ('-t', '--to'):
			t = arg
		elif opt in ('-r', '--rewrite'):
			r = True
		elif opt in ('-w', '--write'):
			w = True
	if i == "":
		sys.stderr.write("Insufficient parameters. 参数不足。")
		sys.exit(1)
	res = pyenconv(open(i, 'rb').read(), f, t)
	if o != "":
		open(o, 'wb').write(res)
	elif r != False:
		open(i, 'wb').write(res)
	elif w != False:
		print(res.decode(t))
	else:
		sys.stderr.write("Insufficient parameters. 参数不足。")
		sys.exit(1)
