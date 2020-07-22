#include<windows.h>
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<math.h>
#define M 1000 //产生1000个点
#define N_perpoint 1000  //每产生1000个高斯点中的一个点需要50个均匀分布的随机数。这个数越大越精确
#define MeanNeed 1   //MeanNeed  : the expected value of mean of generated gauss series
#define SigmaNeed sqrt(2.0)  //SigmaNeed : the expected value of sigma of generated gauss series

//void main (){
//	float    x[N_perpoint],gauss[M],mean=0,sigma=0;
//	int      n,i,stime;
//	long     ltime;
//	for(i=0;i<M;i++)
//		gauss[i]=0;
//	for(i=0;i<M;i++)
//	{
//		ltime=time(NULL);
//		stime=(unsigned int)ltime;
//		stime=stime+i;
//		srand(stime);
//		for(n=0;n<N_perpoint;n++)
//			x[n]=0;
//		for(n=0;n<N_perpoint;n++)
//		{  x[n]=(float)rand()/RAND_MAX;
//		gauss[i]=gauss[i]+(float)sqrt((float)12/N_perpoint)*x[n];
//		}
//		gauss[i]=gauss[i]-(float)sqrt((float)12/N_perpoint)*(N_perpoint/2);
//		gauss[i]=(float)(MeanNeed+SigmaNeed*gauss[i]);
//		mean=mean+gauss[i]/M;
//	}
//	for(i=0;i<M;i++)
//		sigma=sigma+(gauss[i]-mean)*(gauss[i]-mean)/M;
//	printf("%lf , %lf ", mean , sigma) ;
//}
