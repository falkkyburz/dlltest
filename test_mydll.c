#include <stdio.h>
#include <stdlib.h>
#include "mydll.h"

// Compile DLL
// gcc -Wall -shared mydll.c -o mydll.dll
// Compile test_mydll.c
// gcc test_mydll.c mydll.dll -o test_mydll
// analyze DLL
// objdump --private-headers mydll.dll

int main() {
  char              str[21];
  struct STRUCT_DLL S;
  int               i;
  int               ret;

  S.count_int       = 10;
  S.ints            = malloc(sizeof(int) * 10);

  for (i=0; i<10; i++) {
    S.ints[i] = i;
  }


  ret = func_dll(42, str, &S);

  printf("str: %s, ret=%i\n", str, ret);

}