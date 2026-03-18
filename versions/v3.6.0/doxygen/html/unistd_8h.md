---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/unistd_8h.html
original_path: doxygen/html/unistd_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

unistd.h File Reference

`#include "[posix_types.h](posix__types_8h_source.md)"`  
`#include <[zephyr/posix/sys/stat.h](include_2zephyr_2posix_2sys_2stat_8h_source.md)>`

[Go to the source code of this file.](unistd_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NL\_LANGMAX](#a82c429c39d68f08d56e4bfdb050fe54a)   (14) |
| #define | [NL\_MSGMAX](#a7e7a512ab4395a4bb0be4ff872764e45)   (32767) |
| #define | [NL\_SETMAX](#a5dd5a06bde8cda4edb4dfda129375a1a)   (255) |
| #define | [NL\_TEXTMAX](#a934658c7b37ed12672f76ec304a5b460)   (\_POSIX2\_LINE\_MAX) |
| #define | [NZERO](#a3b04cc1d4ce6930b578eede1f1c6ebfc)   (20) |
| #define | [AIO\_LISTIO\_MAX](#a0b4029afb1dcaf401c08b7b147d00cec)   \_POSIX\_AIO\_LISTIO\_MAX |
| #define | [AIO\_MAX](#a0889d4ed1489519e1e8a83ca6f212c5a)   \_POSIX\_AIO\_MAX |
| #define | [AIO\_PRIO\_DELTA\_MAX](#aa9d8b79923c4fc549c074fc387ef65c9)   (0) |
| #define | [DELAYTIMER\_MAX](#a86025bd0a07f29a6ae97f310ff9c701c)   \_POSIX\_DELAYTIMER\_MAX |
| #define | [HOST\_NAME\_MAX](#ac956117a90023ec0971b8f9fce9dec75) |
| #define | [LOGIN\_NAME\_MAX](#af3b7f7833ae69cac7adf84f5973715fe)   \_POSIX\_LOGIN\_NAME\_MAX |
| #define | [MQ\_OPEN\_MAX](#abea867e23b4ca9316a0a7511f1b783d3)   \_POSIX\_MQ\_OPEN\_MAX |
| #define | [MQ\_PRIO\_MAX](#ad1516b4f64b6dc890b1fa3bf576bfef9)   \_POSIX\_MQ\_PRIO\_MAX |
| #define | [PAGE\_SIZE](#a7d467c1d283fdfa1f2081ba1e0d01b6e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(CONFIG\_POSIX\_PAGE\_SIZE\_BITS) |
| #define | [PAGESIZE](#a519adc2af3ba06a8f0548b6690050a89)   [PAGE\_SIZE](#a7d467c1d283fdfa1f2081ba1e0d01b6e) |
| #define | [PTHREAD\_DESTRUCTOR\_ITERATIONS](#a1d96b13a4ba5975d724c5fe13788a957)   \_POSIX\_THREAD\_DESTRUCTOR\_ITERATIONS |
| #define | [PTHREAD\_KEYS\_MAX](#a0a23e66e087bcf5c253b9b2746f19a64) |
| #define | [PTHREAD\_THREADS\_MAX](#ab8f25dec585d6255fcf40b67db66c1c5) |
| #define | [SEM\_NSEMS\_MAX](#a829c888ff8820c37384a5531577cea33)   \_POSIX\_SEM\_NSEMS\_MAX |
| #define | [SEM\_VALUE\_MAX](#a2961bb23950351c6b10976674c27ddaf)   CONFIG\_SEM\_VALUE\_MAX |
| #define | [SIGQUEUE\_MAX](#a649781c35d0360b7d68ef6d55f2aa668)   \_POSIX\_SIGQUEUE\_MAX |
| #define | [STREAM\_MAX](#a238bb3d2a0e88f9ff3e46a6affd7f61d)   \_POSIX\_STREAM\_MAX |
| #define | [SYMLOOP\_MAX](#a41170bbc4e205b3bc9c2b06033aecc17)   \_POSIX\_SYMLOOP\_MAX |
| #define | [TIMER\_MAX](#a9cb39fc9fca65abcf086c5b293db3772)   CONFIG\_MAX\_TIMER\_COUNT |
| #define | [TTY\_NAME\_MAX](#a8e87ff1f5de326c7161ef933ff2fb0f1)   \_POSIX\_TTY\_NAME\_MAX |
| #define | [TZNAME\_MAX](#afb3fe48998f8d32cfb7047b917a8039e)   \_POSIX\_TZNAME\_MAX |
| #define | [FILESIZEBITS](#a34ef6afc1709d5686f1353804aa03e88)   (32) |
| #define | [POSIX\_ALLOC\_SIZE\_MIN](#aa9c42ba60b7eac67360d9804a99e8bba)   (256) |
| #define | [POSIX\_REC\_INCR\_XFER\_SIZE](#a9d04829540462d79aa8751d230987d8b)   (1024) |
| #define | [POSIX\_REC\_MAX\_XFER\_SIZE](#a17269b771b87209b99c9698c782f0d9b)   (32767) |
| #define | [POSIX\_REC\_MIN\_XFER\_SIZE](#a3dae40a21514758cfd61dfb8f159c6f4)   (1) |
| #define | [POSIX\_REC\_XFER\_ALIGN](#a40069c33a92e401df7b3b09d1e65ce55)   (4) |
| #define | [SYMLINK\_MAX](#af552b1b86caac064b8d74f73ac9d3f0c)   \_POSIX\_SYMLINK\_MAX |

| Functions | |
| --- | --- |
| [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) | [getpid](#ac61b207337ca21b3b309593fd1a0cb82) (void) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) | [sleep](#aaa1de6debea33c41fbfaa909e813c2f4) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int seconds) |
| int | [usleep](#a59715f1a0a2ee4dc75e8343aca15c1dd) ([useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342) useconds) |

## Macro Definition Documentation

## [◆ ](#a0b4029afb1dcaf401c08b7b147d00cec)AIO\_LISTIO\_MAX

| #define AIO\_LISTIO\_MAX   \_POSIX\_AIO\_LISTIO\_MAX |
| --- |

## [◆ ](#a0889d4ed1489519e1e8a83ca6f212c5a)AIO\_MAX

| #define AIO\_MAX   \_POSIX\_AIO\_MAX |
| --- |

## [◆ ](#aa9d8b79923c4fc549c074fc387ef65c9)AIO\_PRIO\_DELTA\_MAX

| #define AIO\_PRIO\_DELTA\_MAX   (0) |
| --- |

## [◆ ](#a86025bd0a07f29a6ae97f310ff9c701c)DELAYTIMER\_MAX

| #define DELAYTIMER\_MAX   \_POSIX\_DELAYTIMER\_MAX |
| --- |

## [◆ ](#a34ef6afc1709d5686f1353804aa03e88)FILESIZEBITS

| #define FILESIZEBITS   (32) |
| --- |

## [◆ ](#ac956117a90023ec0971b8f9fce9dec75)HOST\_NAME\_MAX

| #define HOST\_NAME\_MAX |
| --- |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_NETWORKING, \

([NET\_HOSTNAME\_MAX\_LEN](group__net__hostname.md#ga9dda37a09616f2eb1bcdcb76cd868a0f)), \

(\_POSIX\_HOST\_NAME\_MAX))

[NET\_HOSTNAME\_MAX\_LEN](group__net__hostname.md#ga9dda37a09616f2eb1bcdcb76cd868a0f)

#define NET\_HOSTNAME\_MAX\_LEN

**Definition** hostname.h:31

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

## [◆ ](#af3b7f7833ae69cac7adf84f5973715fe)LOGIN\_NAME\_MAX

| #define LOGIN\_NAME\_MAX   \_POSIX\_LOGIN\_NAME\_MAX |
| --- |

## [◆ ](#abea867e23b4ca9316a0a7511f1b783d3)MQ\_OPEN\_MAX

| #define MQ\_OPEN\_MAX   \_POSIX\_MQ\_OPEN\_MAX |
| --- |

## [◆ ](#ad1516b4f64b6dc890b1fa3bf576bfef9)MQ\_PRIO\_MAX

| #define MQ\_PRIO\_MAX   \_POSIX\_MQ\_PRIO\_MAX |
| --- |

## [◆ ](#a82c429c39d68f08d56e4bfdb050fe54a)NL\_LANGMAX

| #define NL\_LANGMAX   (14) |
| --- |

## [◆ ](#a7e7a512ab4395a4bb0be4ff872764e45)NL\_MSGMAX

| #define NL\_MSGMAX   (32767) |
| --- |

## [◆ ](#a5dd5a06bde8cda4edb4dfda129375a1a)NL\_SETMAX

| #define NL\_SETMAX   (255) |
| --- |

## [◆ ](#a934658c7b37ed12672f76ec304a5b460)NL\_TEXTMAX

| #define NL\_TEXTMAX   (\_POSIX2\_LINE\_MAX) |
| --- |

## [◆ ](#a3b04cc1d4ce6930b578eede1f1c6ebfc)NZERO

| #define NZERO   (20) |
| --- |

## [◆ ](#a7d467c1d283fdfa1f2081ba1e0d01b6e)PAGE\_SIZE

| #define PAGE\_SIZE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(CONFIG\_POSIX\_PAGE\_SIZE\_BITS) |
| --- |

## [◆ ](#a519adc2af3ba06a8f0548b6690050a89)PAGESIZE

| #define PAGESIZE   [PAGE\_SIZE](#a7d467c1d283fdfa1f2081ba1e0d01b6e) |
| --- |

## [◆ ](#aa9c42ba60b7eac67360d9804a99e8bba)POSIX\_ALLOC\_SIZE\_MIN

| #define POSIX\_ALLOC\_SIZE\_MIN   (256) |
| --- |

## [◆ ](#a9d04829540462d79aa8751d230987d8b)POSIX\_REC\_INCR\_XFER\_SIZE

| #define POSIX\_REC\_INCR\_XFER\_SIZE   (1024) |
| --- |

## [◆ ](#a17269b771b87209b99c9698c782f0d9b)POSIX\_REC\_MAX\_XFER\_SIZE

| #define POSIX\_REC\_MAX\_XFER\_SIZE   (32767) |
| --- |

## [◆ ](#a3dae40a21514758cfd61dfb8f159c6f4)POSIX\_REC\_MIN\_XFER\_SIZE

| #define POSIX\_REC\_MIN\_XFER\_SIZE   (1) |
| --- |

## [◆ ](#a40069c33a92e401df7b3b09d1e65ce55)POSIX\_REC\_XFER\_ALIGN

| #define POSIX\_REC\_XFER\_ALIGN   (4) |
| --- |

## [◆ ](#a1d96b13a4ba5975d724c5fe13788a957)PTHREAD\_DESTRUCTOR\_ITERATIONS

| #define PTHREAD\_DESTRUCTOR\_ITERATIONS   \_POSIX\_THREAD\_DESTRUCTOR\_ITERATIONS |
| --- |

## [◆ ](#a0a23e66e087bcf5c253b9b2746f19a64)PTHREAD\_KEYS\_MAX

| #define PTHREAD\_KEYS\_MAX |
| --- |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_PTHREAD\_IPC, \

(CONFIG\_MAX\_PTHREAD\_KEY\_COUNT), \

(\_POSIX\_THREAD\_KEYS\_MAX))

## [◆ ](#ab8f25dec585d6255fcf40b67db66c1c5)PTHREAD\_THREADS\_MAX

| #define PTHREAD\_THREADS\_MAX |
| --- |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_PTHREAD\_IPC, \

(CONFIG\_MAX\_PTHREAD\_COUNT), \

(0))

## [◆ ](#a829c888ff8820c37384a5531577cea33)SEM\_NSEMS\_MAX

| #define SEM\_NSEMS\_MAX   \_POSIX\_SEM\_NSEMS\_MAX |
| --- |

## [◆ ](#a2961bb23950351c6b10976674c27ddaf)SEM\_VALUE\_MAX

| #define SEM\_VALUE\_MAX   CONFIG\_SEM\_VALUE\_MAX |
| --- |

## [◆ ](#a649781c35d0360b7d68ef6d55f2aa668)SIGQUEUE\_MAX

| #define SIGQUEUE\_MAX   \_POSIX\_SIGQUEUE\_MAX |
| --- |

## [◆ ](#a238bb3d2a0e88f9ff3e46a6affd7f61d)STREAM\_MAX

| #define STREAM\_MAX   \_POSIX\_STREAM\_MAX |
| --- |

## [◆ ](#af552b1b86caac064b8d74f73ac9d3f0c)SYMLINK\_MAX

| #define SYMLINK\_MAX   \_POSIX\_SYMLINK\_MAX |
| --- |

## [◆ ](#a41170bbc4e205b3bc9c2b06033aecc17)SYMLOOP\_MAX

| #define SYMLOOP\_MAX   \_POSIX\_SYMLOOP\_MAX |
| --- |

## [◆ ](#a9cb39fc9fca65abcf086c5b293db3772)TIMER\_MAX

| #define TIMER\_MAX   CONFIG\_MAX\_TIMER\_COUNT |
| --- |

## [◆ ](#a8e87ff1f5de326c7161ef933ff2fb0f1)TTY\_NAME\_MAX

| #define TTY\_NAME\_MAX   \_POSIX\_TTY\_NAME\_MAX |
| --- |

## [◆ ](#afb3fe48998f8d32cfb7047b917a8039e)TZNAME\_MAX

| #define TZNAME\_MAX   \_POSIX\_TZNAME\_MAX |
| --- |

## Function Documentation

## [◆ ](#ac61b207337ca21b3b309593fd1a0cb82)getpid()

| [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) getpid | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aaa1de6debea33c41fbfaa909e813c2f4)sleep()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) sleep | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *seconds* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a59715f1a0a2ee4dc75e8343aca15c1dd)usleep()

| int usleep | ( | [useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342) | *useconds* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [unistd.h](unistd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
