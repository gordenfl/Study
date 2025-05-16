# Resize Disk Space

Here in the AWS Linux system does not have so much space to store data, I just change the space from 8G to 16G. How can we add all the spaces to the file system.

```shell
[ec2-user@ip-172-31-47-252 /]$  df -h

Filesystem        Size  Used Avail Use% Mounted on
devtmpfs          4.0M     0  4.0M   0% /dev
tmpfs             1.9G     0  1.9G   0% /dev/shm
tmpfs             766M  444K  766M   1% /run
/dev/nvme0n1p1    8.0G  5.8G  2.2G  73% /
tmpfs             1.9G     0  1.9G   0% /tmp
/dev/nvme0n1p128   10M  1.3M  8.7M  13% /boot/efi
tmpfs             383M     0  383M   0% /run/user/1000
```

I just want to add all the extra space into /dev/nvme0n1p1 which is /
how can I do it?

1. first to see what is the satuation of the disk:

```shell
[ec2-user@ip-172-31-47-252 /]$ lsblk
NAME          MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
nvme0n1       259:0    0  16G  0 disk 
├─nvme0n1p1   259:1    0   8G  0 part /
├─nvme0n1p127 259:2    0   1M  0 part 
└─nvme0n1p128 259:3    0  10M  0 part /boot/efi
```

all the defice have 16G, but only 8G used and assigned to /, we need increase the space of /.

2. the first step to check what kind of the partition is:

```shell
[ec2-user@ip-172-31-47-252 /]$ lsblk -f
NAME          FSTYPE FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
nvme0n1                                                                              
├─nvme0n1p1   xfs          /     f0b93573-be85-4f02-8666-58d87d890c30    2.1G    73% /
├─nvme0n1p127                                                                        
└─nvme0n1p128 vfat   FAT16       3CBA-2494                               8.7M    13% /boot/efi
```

that indicate that nvme0n1p1 is an xfs type partition.

3. resize the partition with gdisk command.

```shell
[ec2-user@ip-172-31-47-252 /]$ sudo gdisk /dev/nvme0n1

Command (? for help):
```

then show all partition we have with:

```shell
Command (? for help): p

Disk /dev/nvme0n1: 33554432 sectors, 16.0 GiB
Model: Amazon Elastic Block Store              
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 6903FC47-8F98-4422-B42E-CC8DB8BAB2A6
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 33554398
Partitions will be aligned on 2048-sector boundaries
Total free space is 16779230 sectors (8.0 GiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1           24576        16777182   8.0 GiB     8300  Linux filesystem
 127           22528           24575   1024.0 KiB  EF02  BIOS Boot Partition
 128            2048           22527   10.0 MiB    EF00  EFI System Partition

```

then delete the first one of the disk. (it will not delete the data on your disk), we are only change the partition table. It will not effect all the data in the disk.

```shell
Command (? for help): d
Partition number (1-128): 1

```

next, I just create a new disk with command n:

```shell
Command (? for help): n
Partition number (1-128, default 1): 
First sector (34-33554398, default = 24576) or {+-}size{KMGTP}: 24576
Last sector (24576-33554398, default = 33554398) or {+-}size{KMGTP}: 33554398
Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): 
Changed type of partition to 'Linux filesystem'

```

please notice the First is still 24576, but the end becomes to 33554398 not 16777182.
after that, we need save our change, with command w

outside of gdisk command line, we need execute the command to apply this change to system with partprobe  and sfs_growfs :

```shell
[ec2-user@ip-172-31-47-252 /]$ sudo partprobe
[ec2-user@ip-172-31-47-252 /]$ sudo xfs_growfs /
meta-data=/dev/nvme0n1p1         isize=512    agcount=2, agsize=1047040 blks
         =                       sectsz=4096  attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1    bigtime=1 inobtcount=1
data     =                       bsize=4096   blocks=2094075, imaxpct=25
         =                       sunit=128    swidth=128 blks
naming   =version 2              bsize=16384  ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=16384, version=2
         =                       sectsz=4096  sunit=4 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 2094075 to 4191227
```

after all we change the space of our disk. check with that:

```shell
[ec2-user@ip-172-31-47-252 /]$ df -h
Filesystem        Size  Used Avail Use% Mounted on
devtmpfs          4.0M     0  4.0M   0% /dev
tmpfs             1.9G     0  1.9G   0% /dev/shm
tmpfs             766M  444K  766M   1% /run
/dev/nvme0n1p1     16G  5.9G   11G  37% /
tmpfs             1.9G     0  1.9G   0% /tmp
/dev/nvme0n1p128   10M  1.3M  8.7M  13% /boot/efi
tmpfs             383M     0  383M   0% /run/user/1000
```

the space change success: /dev/nvme0n1p1 becomes 16G 
