#include <stdio.h>
#include <stdlib.h>

//function, list inputs, first before function declaration say type returning, void is none
int addNumbers(int num1, int num2){
    return num1 + num2;
}

 //structure
struct Student{
    int age;
    double gpa;
    char grade;
    };

int main()
{
    int sum = addNumbers(4,60);
    printf("%d \n", sum);

    int isStudent = 1;
    int isSmart = 1;

    if (isStudent != 0 && isSmart != 0) {
        printf("You are a student \n");
    } else if (isStudent != 0 && isSmart == 0) {
        printf("You are not a smart student \n");
    } else {
        printf("You are not a student and are not smart\n");
    }
    // <, >, >=, <=, !=, ==
    if (1>3){
        printf("number comparison was true\n");
    }

    char myGrade = 'A';
    switch(myGrade){
        case 'A':
            printf("You pass with an %c \n", myGrade);
            break;
        case 'F':
            printf("You fail with an %c \n", myGrade);
            break;
        default:
            printf("You did alright with a %c\n");
            break;
    }

    //While loop
    int index = 1;
    while (index <= 5) {
        printf("%d \n", index);
        index ++;
    }

    //for loop
    for(int i = 0; i < 5; i++){
        printf("%d is the index \n", i);
    }
    struct Student student1;
    student1.age = 19;
    student1.gpa = 3.4;
    student1.grade = 'B';
    
   
    return 0;
}