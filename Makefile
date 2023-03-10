all: runexe runpy
mydll.dll: mydll.c
	gcc -Wall -shared mydll.c -o mydll.dll
test_mydll: test_mydll.c mydll.dll
	gcc test_mydll.c mydll.dll -o test_mydll
runexe: test_mydll 
	echo "Running test_mydll.exe"
	./test_mydll
runpy: test_mydll.py
	echo "Running test_mydll.py"
	python test_mydll.py
clean:
	rm mydll.dll
	rm test_mydll
