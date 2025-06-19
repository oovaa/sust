#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "employee.dat"
#define FA1 "Fa1.dat"
#define FA2 "Fa2.dat"
#define FB1 "Fb1.dat"
#define FB2 "Fb2.dat"

typedef struct employee
{
    char name[30];
    char ssn[9];
    int salary;
    char department[20];
    int job_code;
} Employee;

// Display all employees in a file
void display_file(const char *filename, const char *msg)
{
    FILE *pf = fopen(filename, "rb");
    if (!pf)
    {
        printf("Error opening %s\n", filename);
        return;
    }
    Employee emp;
    printf("%s\n", msg);
    printf("%-30s %-9s %-10s %-20s %-8s\n", "Name", "SSN", "Salary", "Department", "JobCode");
    while (fread(&emp, sizeof(Employee), 1, pf))
        printf("%-30s %-9s %-10d %-20s %-8d\n", emp.name, emp.ssn, emp.salary, emp.department, emp.job_code);
    fclose(pf);
}

// Split runs into Fa1 and Fa2
int split(const char *src, const char *fa1, const char *fa2, int run_size)
{
    FILE *in = fopen(src, "rb");
    FILE *out1 = fopen(fa1, "wb");
    FILE *out2 = fopen(fa2, "wb");
    if (!in || !out1 || !out2)
    {
        printf("Error opening files for splitting.\n");
        return 0;
    }
    Employee emp;
    int count = 0, toggle = 0;
    while (fread(&emp, sizeof(Employee), 1, in))
    {
        if (toggle == 0)
            fwrite(&emp, sizeof(Employee), 1, out1);
        else
            fwrite(&emp, sizeof(Employee), 1, out2);
        count++;
        if (count == run_size)
        {
            count = 0;
            toggle = 1 - toggle;
        }
    }
    fclose(in);
    fclose(out1);
    fclose(out2);
    return 1;
}

// Merge runs from Fa1 and Fa2 into Fb1 and Fb2
int merge(const char *fa1, const char *fa2, const char *fb1, const char *fb2, int run_size)
{
    FILE *in1 = fopen(fa1, "rb");
    FILE *in2 = fopen(fa2, "rb");
    FILE *out1 = fopen(fb1, "wb");
    FILE *out2 = fopen(fb2, "wb");
    if (!in1 || !in2 || !out1 || !out2)
    {
        printf("Error opening files for merging.\n");
        return 0;
    }
    Employee e1, e2;
    int read1 = fread(&e1, sizeof(Employee), 1, in1);
    int read2 = fread(&e2, sizeof(Employee), 1, in2);
    int out_toggle = 0;
    FILE *out = out1;
    while (read1 || read2)
    {
        int c1 = 0, c2 = 0;
        while ((c1 < run_size && read1) || (c2 < run_size && read2))
        {
            if (c1 < run_size && read1 && (c2 >= run_size || !read2 || strcmp(e1.ssn, e2.ssn) <= 0))
            {
                fwrite(&e1, sizeof(Employee), 1, out);
                read1 = fread(&e1, sizeof(Employee), 1, in1);
                c1++;
            }
            else if (c2 < run_size && read2)
            {
                fwrite(&e2, sizeof(Employee), 1, out);
                read2 = fread(&e2, sizeof(Employee), 1, in2);
                c2++;
            }
        }
        out_toggle = 1 - out_toggle;
        out = out_toggle ? out2 : out1;
    }
    fclose(in1);
    fclose(in2);
    fclose(out1);
    fclose(out2);
    return 1;
}

// Count number of records in a file
int count_records(const char *filename)
{
    FILE *pf = fopen(filename, "rb");
    if (!pf)
        return 0;
    fseek(pf, 0, SEEK_END);
    int n = ftell(pf) / sizeof(Employee);
    fclose(pf);
    return n;
}

// Copy file src to dest
void copy_file(const char *src, const char *dest)
{
    FILE *in = fopen(src, "rb");
    FILE *out = fopen(dest, "wb");
    Employee emp;
    while (fread(&emp, sizeof(Employee), 1, in))
        fwrite(&emp, sizeof(Employee), 1, out);
    fclose(in);
    fclose(out);
}

// Two-way external merge sort
void two_way_merge_sort(const char *filename)
{
    int n = count_records(filename);
    int run_size = 1;
    int toggle = 0;
    char *A1 = FA1, *A2 = FA2, *B1 = FB1, *B2 = FB2;
    while (run_size < n)
    {
        split(filename, A1, A2, run_size);
        merge(A1, A2, B1, B2, run_size);
        // Merge output is in B1 and B2, combine them into filename
        FILE *out = fopen(filename, "wb");
        FILE *in1 = fopen(B1, "rb");
        FILE *in2 = fopen(B2, "rb");
        Employee emp;
        while (fread(&emp, sizeof(Employee), 1, in1))
            fwrite(&emp, sizeof(Employee), 1, out);
        while (fread(&emp, sizeof(Employee), 1, in2))
            fwrite(&emp, sizeof(Employee), 1, out);
        fclose(out);
        fclose(in1);
        fclose(in2);
        run_size *= 2;
    }
}

int main()
{
    printf("Before sorting:\n");
    display_file(FILENAME, "Unsorted Employees:");
    two_way_merge_sort(FILENAME);
    printf("\nAfter sorting:\n");
    display_file(FILENAME, "Sorted Employees:");
    return 0;
}