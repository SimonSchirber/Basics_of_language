
#include <cstdio>
#include <iostream>

//Right Click > runcode to execute

int step_function(int x){
    /*
        Multi line comment
    */
    int result = 0;
    if (x<0){
        result = -1;
    } else if (x >0){
        result = 1;
    }
    return result;
}

int main(){
    int x = 0;
    if (x > 0){
        printf("Positive");
    }else if (x < 0){
        printf("Negative");
    }else{
        printf("Zero\n");
    }

    int value1 = step_function(100);
    int value2 = step_function(-2);
    int value3 = step_function(0);
    
    printf("The result was %d, but I didnt expect it above %d", value1, 5);

    return 0; //function returns 0 if no bugs, one if error along the way
}

