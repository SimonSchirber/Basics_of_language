#include <stdio.h>
#include <stdlib.h>

int main()
{
    //array
    int luckyNumbers[] = {4,8,15,16,23,42};
    // indexes            0 1 2  3  4  5
    luckyNumbers[0] = 90;
    printf("%d \n", luckyNumbers[0]);

    //multi dimensional arrays
    int numberGrid[2][3] = { {1,2,3}, {4,5,6}};
    numberGrid[0][1] = 99;
    
    return 0;
}