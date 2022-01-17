#include <stdio.h> // define the header file  
#include <stdlib.h>

int main()   // define the main function  
{  
    printf("Hello World\n");
    printf("This is a newline\n");
    char mychar = 'C';
    char name[] = "Simon";

    int age1 = 20; //at least 16 bit integer
    long age2 = 30; //at least 64 bit signed integer

    float gpa0 = 3.7; //single precision floating poit
    double gpa2 = 5.7; //double precision floating point

    //boolean is just int, youi can make it an int
    int isTall = 1;
    const int isShort = 0;

    printf("%s, your grade is %d \n", name, gpa2); //the percent sign followed by letter denotes string s,, etc
    return 0; // print the statement.  
}  