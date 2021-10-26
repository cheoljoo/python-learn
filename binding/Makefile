all:
	g++ -c -fPIC foo.cpp -o foo.o
	g++ -shared -Wl,-soname,libfoo.so -o libfoo.so  foo.o 
	python3 foo.py
	g++ -c -fPIC cmult.c -o cmult.o
	g++ -shared -Wl,-soname,libcmult.so -o libcmult.so  cmult.o 
	python3 cmult.py
