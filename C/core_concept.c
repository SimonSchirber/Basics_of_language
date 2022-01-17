#include <stdio.h> //header (standard io)
#include <stdlib.h>

int main()
{
    printf("Hello\n");
    printf("World");
    printf("!\n");

    char testGrade = 'A'; //character (%c)
    char name[] = "Mike"; //string (%s), double quotes needed
    printf("%s, your grade is %c \n", name, testGrade);
    /* print letters
    %c character
    %d integer
    %e exponential floating point
    %f floating point
    %i integer
    %s string of characters
    %u unsigned decimal integer
    */

    int age1 = 20; //integer
    float gpa0 = 3.5; //float
    double  dub = 3.44;//double that is lin
    int isTall = 1; //Boolean

    printf("%d \n", 2 * 3);
    printf("%d \n", (1 + 2) * 3);
    printf("%f \n", 10/3.0);
    int num = 10;
    num += 100; //increment 100
    printf("%d \n", num);
    num ++ ; //increment 1, -- is decrement 1

    char nameLast[10]; //declaring how large string is

    //change data type
    printf("%d, \n", (int)3.14);
    return 0;
}
