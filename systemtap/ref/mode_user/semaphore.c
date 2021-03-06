#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>


sem_t bin_sem;
void *thread_function1(void *arg)
{
printf("thread_function1--------------sem_wait\n");
sem_wait(&bin_sem);
printf("sem_wait\n");
while (1)
{
}
}


void *thread_function2(void *arg)
{
printf("thread_function2--------------sem_post\n");
sem_post(&bin_sem);
printf("sem_post\n");
while (1)
{
}
}

 


int main()
{
int res = 0;
pthread_t a_thread;
void *thread_result;


res = sem_init(&bin_sem, 0, 0);
if (res != 0)
{
perror("Semaphore initialization failed");
}
printf("sem_init\n");
res = pthread_create(&a_thread, NULL, thread_function1, NULL);
if (res != 0)
{
perror("Thread creation failure");
}
printf("thread_function1\n");
sleep (5);
printf("sleep\n");
res = pthread_create(&a_thread, NULL, thread_function2, NULL);
if (res != 0)
{
perror("Thread creation failure");
}
while (1)
{
}
}
