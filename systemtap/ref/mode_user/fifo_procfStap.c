#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[])
{
  char *MODNAME = argv[1];

  int client_to_server;
  int checkfs;
  //char *procStap = "/proc/systemtap/";
  char *procFs = "/bully";
  char buf[BUFSIZ];
  char myfifo[128];
  char *flag = "no_event";
  snprintf(myfifo, sizeof(myfifo), "%s%s",MODNAME,procFs);
  printf("%s\n",myfifo);

  client_to_server = open(myfifo, O_RDONLY);

  printf("Server ON bufsize=%d.\n", BUFSIZ);

  while (1)
  {
    checkfs = read(client_to_server, buf, sizeof(buf));
    if(checkfs<0)
    {
	printf("---check %d\n",checkfs);
	break;
    }else{
	printf("%s\n",buf);
}
   

    if (strcmp("exit",buf)==0)
    {
      printf("Server OFF.\n");
      break;
    }
    else if (strcmp("",buf)!=0)
    {
      printf("Received: %s %d\n", buf,sizeof(buf));  
      
 //     close(client_to_server);
  //    client_to_server = open(myfifo, O_RDONLY);
/*
      printf("Received: %s %d\n", buf,sizeof(buf));
      write(client_to_server, flag, sizeof(flag) );
      printf("----Sending fin---- \n");

      close(client_to_server);
      client_to_server = open(myfifo, O_RDONLY);
  */
    }

    /* clean buf from any data */
    memset(buf, 0, sizeof(buf));
    //break;
  }

  close(client_to_server);
  unlink(myfifo);
  return 0;
}
