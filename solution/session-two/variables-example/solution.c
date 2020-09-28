#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdint.h>

int main() {
	char *key = "KeYpress";
	int64_t xor_me = 0xdeadbeeffacecafe;
	for(int i = 0; i <= 7; i += 1) {
		printf("%c", (char)((char)(xor_me >> ((i << 3) & 0x3f)) + key[i] + 1) );
	}
	return 0;
}
