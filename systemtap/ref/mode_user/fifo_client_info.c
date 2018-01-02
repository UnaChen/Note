#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include<string.h>

int main(int argc, char *argv[])
{
    int client_to_server;
    char *myfifo = "/tmp/client_to_server_fifo";
    int server_to_client;
    char *myfifo2 = "/tmp/server_to_client_fifo";

    char str[BUFSIZ];
    ssize_t check;

    /* write str to the FIFO */
    client_to_server = open(myfifo, O_WRONLY);
    server_to_client = open(myfifo2, O_RDONLY);

    char buf1[1024] ;
    //char *buf1;
   
    while(1){
        //printf("input：");
        //scanf("%s", buf1);
        strcpy(buf1,argv[1]);
	
	printf("--%s %d\n",buf1,sizeof(buf1));

	if (strcmp("bye", buf1)==0)
	    break;
	else
            check = write(client_to_server, buf1, sizeof(buf1));
		
        if (check < 0){
            printf("write error!!\n");
	}
        if (strcmp("exit",buf1)!=0){
            check = read(server_to_client,str,sizeof(str));
            if (check < 0){
                printf("read error!!\n");
            }
            printf("...received from the server: %s\n",str);
            memset(str, '\0', sizeof(str));
            memset(buf1, '\0', sizeof(buf1));
	    printf("------------\n");
        }
        else {
            printf("Exit!!!!\n");
            break;
        }
	break;

    }

    close(client_to_server);
    close(server_to_client);
    return 0;
}
