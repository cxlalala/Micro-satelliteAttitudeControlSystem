#include <stdio.h>
#include <stdlib.h>

typedef float          		FP32;                      /* single precision floating point variable (32bits) 单精度浮点数（32位长度） */
typedef int   				SINT32;                    /* defined for signed 32-bits integer variable 		有符号32位整型变量 */

//#define N 5
//FP32 gaussian[N];
//FILE *fpread;

void read_noise(FILE *fpread, SINT32 n, FP32 gaussian[])
{

	if (fpread == NULL)
	{
		printf("file is error.");
		return -1;
	}
	for (int i = 0; i < n; i++)
    {
        fscanf(fpread, "%f", &gaussian[i]);
    }
	fclose(fpread);
//	for (int i = 0; i < n; i++)
//	{
//        printf("%f\n",gaussian[i]);
//	}
}

//int main(void)
//{
//    fpread = fopen("guassian_noise.txt", "r");
//    read_noise(fpread, N, gaussian);
//    return 0;
//}

