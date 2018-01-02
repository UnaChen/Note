#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

int main()
{
  int client_to_server;
  char *myfifo = "/proc/record-fifo";
  int check;
  //int server_to_client;
  //char *myfifo2 = "/tmp/server_to_client_fifo";
  char buf[BUFSIZ];

  /* create the FIFO (named pipe) */
//  mkfifo(myfifo, 0666);
//  mkfifo(myfifo2, 0666);

  /* open, read, and display the message from the FIFO */
  client_to_server = open(myfifo, O_RDONLY);
//  server_to_client = open(myfifo2, O_WRONLY);

  printf("Server ON bufsize=%d.\n", BUFSIZ);

  while (1)
  {
    check = read(client_to_server, buf, sizeof(buf));
    printf("Received: %d %s %d\n", check, buf,sizeof(buf));
  /*  if (strcmp("exit",buf)==0)
    {
      printf("Server OFF.\n");
      break;
    }
    else if (strcmp("",buf)!=0)
    {
      printf("Received: %s %d\n", buf,sizeof(buf));
      printf("Sending back... %s %d\n", buf, sizeof(buf));
      sleep(3);
      write(server_to_client,buf,sizeof(buf));
      printf("----Sending fin---- \n");
    }
*/
    /* clean buf from any data */
      memset(buf, 0, sizeof(buf));
      break;
  }

  close(client_to_server);
//  close(server_to_client);
  unlink(myfifo);
//  unlink(myfifo2);
  return 0;
}
