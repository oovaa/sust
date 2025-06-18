#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "employee.dat"

typedef struct employee
{
    char name[30];
    char ssn[9];
    int salary;
    char department[20];
    int job_code;
} Employee;

void initialize()
{
    FILE *pf = fopen(FILENAME, "w");
    if (pf)
        fclose(pf);
    printf("File initialized.\n");
}

void insert()
{
    Employee emp, temp;
    printf("Enter employee details (name ssn salary department job_code): ");
    scanf("%s %s %d %s %d", emp.name, emp.ssn, &emp.salary, emp.department, &emp.job_code);

    FILE *pf = fopen(FILENAME, "rb");
    FILE *tempf = fopen("temp.dat", "wb");
    if (!tempf)
    {
        printf("Error opening temp file.\n");
        if (pf)
            fclose(pf);
        return;
    }
    int inserted = 0;
    if (pf)
    {
        while (fread(&temp, sizeof(Employee), 1, pf))
        {
            if (!inserted && strcmp(emp.ssn, temp.ssn) < 0)
            {
                fwrite(&emp, sizeof(Employee), 1, tempf);
                inserted = 1;
            }
            fwrite(&temp, sizeof(Employee), 1, tempf);
        }
        fclose(pf);
    }
    if (!inserted)
    {
        fwrite(&emp, sizeof(Employee), 1, tempf);
    }
    fclose(tempf);
    remove(FILENAME);
    rename("temp.dat", FILENAME);
    printf("Employee inserted in order.\n");
}

void display()
{
    FILE *pf = fopen(FILENAME, "rb");
    if (!pf)
    {
        printf("Error opening file.\n");
        return;
    }
    Employee emp;
    printf("\n%-30s %-9s %-10s %-20s %-8s\n", "Name", "SSN", "Salary", "Department", "JobCode");
    while (fread(&emp, sizeof(Employee), 1, pf))
        printf("%-30s %-9s %-10d %-20s %-8d\n", emp.name, emp.ssn, emp.salary, emp.department, emp.job_code);

    fclose(pf);
}

void search()
{
    char ssn[9];
    printf("Enter SSN to search: ");
    scanf("%s", ssn);
    FILE *pf = fopen(FILENAME, "rb");
    if (!pf)
    {
        printf("Error opening file.\n");
        return;
    }
    Employee emp;
    int found = 0;
    while (fread(&emp, sizeof(Employee), 1, pf))
    {
        if (strcmp(emp.ssn, ssn) == 0)
        {
            printf("Found: %s %s %d %s %d\n", emp.name, emp.ssn, emp.salary, emp.department, emp.job_code);
            found = 1;
            break;
        }
    }
    if (!found)
        printf("Employee not found.\n");
    fclose(pf);
}

void delete()
{
    char ssn[9];
    printf("Enter SSN to delete: ");
    scanf("%s", ssn);
    FILE *pf = fopen(FILENAME, "rb");
    FILE *temp = fopen("temp.dat", "wb");
    if (!pf || !temp)
    {
        printf("Error opening file.\n");
        return;
    }
    Employee emp;
    int found = 0;
    while (fread(&emp, sizeof(Employee), 1, pf))
    {
        if (strcmp(emp.ssn, ssn) == 0)
        {
            found = 1;
            continue;
        }
        fwrite(&emp, sizeof(Employee), 1, temp);
    }
    fclose(pf);
    fclose(temp);
    remove(FILENAME);
    rename("temp.dat", FILENAME);
    if (found)
        printf("Employee deleted.\n");
    else
        printf("Employee not found.\n");
}

int main()
{
    int choice;
    while (1)
    {
        printf("\nMenu:\n1. Initialize\n2. Insert\n3. Delete\n4. Search\n5. Display\n6. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            initialize();
            break;
        case 2:
            insert();
            break;
        case 3:
            delete();
            break;
        case 4:
            search();
            break;
        case 5:
            display();
            break;
        case 6:
            printf("Exiting...\n");
            return 0;
        default:
            printf("Invalid choice.\n");
        }
    }
    return 0;
}