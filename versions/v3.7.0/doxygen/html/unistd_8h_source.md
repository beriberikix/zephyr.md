---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/unistd_8h_source.html
original_path: doxygen/html/unistd_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

unistd.h

[Go to the documentation of this file.](unistd_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_UNISTD\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_UNISTD\_H\_

8

9#include "[posix\_types.h](posix__types_8h.md)"

10

11#ifdef CONFIG\_POSIX\_API

12#include <[zephyr/fs/fs.h](fs_8h.md)>

13#endif

14#ifdef CONFIG\_NETWORKING

15/\* For zsock\_gethostname() \*/

16#include <[zephyr/net/socket.h](net_2socket_8h.md)>

17#include <[zephyr/net/hostname.h](hostname_8h.md)>

18#endif

19#include <[zephyr/posix/sys/confstr.h](confstr_8h.md)>

20#include <[zephyr/posix/sys/stat.h](stat_8h.md)>

21#include <[zephyr/posix/sys/sysconf.h](sysconf_8h.md)>

22

23#include "[posix\_features.h](posix__features_8h.md)"

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

29#ifdef CONFIG\_POSIX\_API

30/\* File related operations \*/

31int [close](group__bsd__sockets.md#ga3c78073ab26ad78a7a1f715ba3580086)(int file);

32[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) write(int file, const void \*buffer, size\_t count);

33[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) read(int file, void \*buffer, size\_t count);

34[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) lseek(int file, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, int whence);

35int fsync(int fd);

36int ftruncate(int fd, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) length);

37

38/\* File System related operations \*/

39int rename(const char \*old, const char \*newp);

40int unlink(const char \*path);

41int [stat](stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)(const char \*path, struct [stat](structstat.md) \*buf);

42int [mkdir](stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)(const char \*path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) mode);

43

44FUNC\_NORETURN void \_exit(int status);

45

46#ifdef CONFIG\_NETWORKING

47static inline int [gethostname](group__bsd__sockets.md#ga14fe74115e6133e1be596c327047b0ca)(char \*buf, size\_t len)

48{

49 return [zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)(buf, len);

50}

51#endif /\* CONFIG\_NETWORKING \*/

52

53#endif /\* CONFIG\_POSIX\_API \*/

54

55#ifdef CONFIG\_POSIX\_C\_LIB\_EXT

56int getopt(int argc, char \*const argv[], const char \*optstring);

57extern char \*optarg;

58extern int opterr, optind, optopt;

59#endif

60

[ 61](unistd_8h.md#a5d88641f86c8a447fefd1e531758a3c0)int [getentropy](unistd_8h.md#a5d88641f86c8a447fefd1e531758a3c0)(void \*buffer, size\_t length);

[ 62](unistd_8h.md#ac61b207337ca21b3b309593fd1a0cb82)[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) [getpid](unistd_8h.md#ac61b207337ca21b3b309593fd1a0cb82)(void);

[ 63](unistd_8h.md#aaa1de6debea33c41fbfaa909e813c2f4)unsigned [sleep](unistd_8h.md#aaa1de6debea33c41fbfaa909e813c2f4)(unsigned int seconds);

[ 64](unistd_8h.md#a59715f1a0a2ee4dc75e8343aca15c1dd)int [usleep](unistd_8h.md#a59715f1a0a2ee4dc75e8343aca15c1dd)([useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342) useconds);

65#if \_POSIX\_C\_SOURCE >= 2

66size\_t confstr(int name, char \*buf, size\_t len);

67#endif

68

69#ifdef CONFIG\_POSIX\_SYSCONF\_IMPL\_MACRO

70#define sysconf(x) (long)CONCAT(\_\_z\_posix\_sysconf, x)

71#else

[ 72](unistd_8h.md#a599f55d9eaa01b6921367233437b9b13)long [sysconf](unistd_8h.md#a599f55d9eaa01b6921367233437b9b13)(int opt);

73#endif /\* CONFIG\_POSIX\_SYSCONF\_IMPL\_FULL \*/

74

75#ifdef \_\_cplusplus

76}

77#endif

78

79#endif /\* ZEPHYR\_INCLUDE\_POSIX\_UNISTD\_H\_ \*/

[confstr.h](confstr_8h.md)

[fs.h](fs_8h.md)

[gethostname](group__bsd__sockets.md#ga14fe74115e6133e1be596c327047b0ca)

static int gethostname(char \*buf, size\_t len)

POSIX wrapper for zsock\_gethostname.

**Definition** socket.h:1022

[close](group__bsd__sockets.md#ga3c78073ab26ad78a7a1f715ba3580086)

static int close(int sock)

POSIX wrapper for zsock\_close.

**Definition** socket.h:879

[zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)

int zsock\_gethostname(char \*buf, size\_t len)

Get local host name.

[hostname.h](hostname_8h.md)

Hostname configuration definitions.

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00)

unsigned int mode\_t

**Definition** types.h:14

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[posix\_features.h](posix__features_8h.md)

[posix\_types.h](posix__types_8h.md)

[useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342)

unsigned long useconds\_t

**Definition** posix\_types.h:29

[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)

int pid\_t

**Definition** posix\_types.h:25

[stat.h](stat_8h.md)

[stat](stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)

int stat(const char \*\_\_restrict \_\_path, struct stat \*\_\_restrict \_\_sbuf)

[mkdir](stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)

int mkdir(const char \*\_path, mode\_t \_\_mode)

[stat](structstat.md)

**Definition** stat.h:92

[sysconf.h](sysconf_8h.md)

[usleep](unistd_8h.md#a59715f1a0a2ee4dc75e8343aca15c1dd)

int usleep(useconds\_t useconds)

[sysconf](unistd_8h.md#a599f55d9eaa01b6921367233437b9b13)

long sysconf(int opt)

[getentropy](unistd_8h.md#a5d88641f86c8a447fefd1e531758a3c0)

int getentropy(void \*buffer, size\_t length)

[sleep](unistd_8h.md#aaa1de6debea33c41fbfaa909e813c2f4)

unsigned sleep(unsigned int seconds)

[getpid](unistd_8h.md#ac61b207337ca21b3b309593fd1a0cb82)

pid\_t getpid(void)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [unistd.h](unistd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
