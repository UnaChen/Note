KVERSION := $(shell uname -r)
KERNEL_DIR = /lib/modules/$(KVERSION)/build

obj-m := signal_kernel.o

all:
	make -C $(KERNEL_DIR) M=$(PWD) modules
clean:
	make -C $(KERNEL_DIR) M=$(PWD) clean
