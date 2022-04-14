#include <iostream>
#include <math.h>

//add function for two arrays
//*x means point to memory address of x
//Global represents that available to do on GPU
void add(int n, float *x, float *y)
{
    for (int i =0; i < n; i++)
        y[i] = x[i] + y[i];
}

int main(void){
    int N = 1<<20; //1M (1,048,576) elements, shift 1 over 20 times in binary
    //to print (std::cout << ""<<) 
    std::cout << "N value:" << N << std::endl;
    
    //Define length of array
    float *x = new float[N];
    float *y = new float[N];

    //initialize arrays
    for (int i = 0; i < N; i++){
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    //run kernal on elemants on CPU
    add(N,x,y);


    //check for errors, all should be 3 (1.0 + 2.0)
    float maxError = 0.0f;
    for (int i = 0; i < N; i++){
        maxError = fmax(maxError, fabs(y[i]-3.0f));
    }
    std::cout << "Max Error: " << maxError << std::endl;

 

    //Free up  cpu memory
    delete [] x;
    delete [] y;

    return 0;

}