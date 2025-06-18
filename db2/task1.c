#include <stdio.h>

int main()
{
    // Print "Hello, World!" to the console
    FILE *pf = fopen("sust.txt", "w");
    if (pf == NULL)
    {
        perror("Failed to open file");
        return 1;
    }
    fprintf(pf, "- Sudan University of Science and Technology\n"
                "- College of Computer Science and Information Technology\n"
                "- Department of Computer Science\n"
                "- Course: C Programming\n"
                "- Lab: 2\n"
                "- Task: 1\n"
                "- Student ID: 1234567890\n");

    fclose(pf);
    return 0;
}