#include <sys/socket.h>
#include <linux/netlink.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "netlink_hello_user_so.h"

#define NETLINK_USER 31

#define MAX_PAYLOAD 1024 /* maximum payload size*/
struct sockaddr_nl src_addr, dest_addr;
struct nlmsghdr *nlh = NULL;
struct iovec iov;
int sock_fd;
struct msghdr msg;

void netlink_initMsg()
{
    nlh = (struct nlmsghdr *)malloc(NLMSG_SPACE(MAX_PAYLOAD));
    memset(nlh, 0, NLMSG_SPACE(MAX_PAYLOAD));
    nlh->nlmsg_len = NLMSG_SPACE(MAX_PAYLOAD);
    nlh->nlmsg_pid = getpid();
    nlh->nlmsg_flags = 0;

    strcpy(NLMSG_DATA(nlh), "H");

    iov.iov_base = (void *)nlh;
    iov.iov_len = nlh->nlmsg_len;
    msg.msg_name = (void *)&dest_addr;
    msg.msg_namelen = sizeof(dest_addr);
    msg.msg_iov = &iov;
    msg.msg_iovlen = 1;  
}
int netlink_isExit()
{
    if (strcmp("Hello",NLMSG_DATA(nlh))==0)
	return 1;
    return 0;
}

char* netlink_recvMsg()
{
    recvmsg(sock_fd, &msg, 0);
    //printf("Received message payload: %s\n", NLMSG_DATA(nlh));
    return NLMSG_DATA(nlh);  
}

void netlink_sendMsg()
{
    sendmsg(sock_fd, &msg, 0);    
}

void netlink_exit()
{
    close(sock_fd);
}

int netlink_init()
//int main()
{
    sock_fd = socket(PF_NETLINK, SOCK_RAW, NETLINK_USER);
    if (sock_fd < 0)
        return -1;

    memset(&src_addr, 0, sizeof(src_addr));
    src_addr.nl_family = AF_NETLINK;
    src_addr.nl_pid = getpid(); /* self pid */

    bind(sock_fd, (struct sockaddr *)&src_addr, sizeof(src_addr));

    memset(&dest_addr, 0, sizeof(dest_addr));
    memset(&dest_addr, 0, sizeof(dest_addr));
    dest_addr.nl_family = AF_NETLINK;
    dest_addr.nl_pid = 0; /* For Linux Kernel */
    dest_addr.nl_groups = 0; /* unicast */

    netlink_initMsg();
  //  printf("Sending message to kernel\n");
//    netlink_sendMsg();
//    printf("Waiting for message from kernel\n");
    return 0;
/*    while (1){
	netlink_recvMsg();
        if (netlink_isExit())
		break;	
        netlink_initMsg();
        netlink_sendMsg();
    }
    netlink_exit();
*/
}
