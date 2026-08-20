#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char name[20];
    char buffer[20];
    char cmd[100];

    printf("Enter your name: ");

    gets(name);

    strcpy(buffer, name);

    sprintf(cmd, "echo Hello %s", buffer);

    system(cmd);

    return 0;
}
