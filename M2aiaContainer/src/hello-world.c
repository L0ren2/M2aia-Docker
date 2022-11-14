#include <stdio.h>

int main(int argc, char* argv[])
{
	FILE* out = fopen("/m2aia-share/hello-world-out.txt", "w+");
	fprintf(out, "Hello, ");
	if (argc > 1)
		fprintf(out, "%s!\n", argv[1]);
	else 
		fprintf(out, "World!\n");
	fclose(out);
	return 0;
}

