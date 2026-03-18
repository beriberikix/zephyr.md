---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/signal_8h_source.html
original_path: doxygen/html/signal_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

signal.h

[Go to the documentation of this file.](signal_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SIGNAL\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SIGNAL\_H\_

8

9#include "[posix\_types.h](posix__types_8h.md)"

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

[ 15](signal_8h.md#a136c64ec2d1306de745e39d6aee362ca)#define SIGHUP 1

[ 16](signal_8h.md#a487309e3e9e0527535644115204a639a)#define SIGINT 2

[ 17](signal_8h.md#a62045b465be11891160d53c10861b16c)#define SIGQUIT 3

[ 18](signal_8h.md#a4c9c5284f8c8d146bd7a93d25017fc62)#define SIGILL 4

[ 19](signal_8h.md#aa2beb906ab1b46676e63823f4e773c38)#define SIGTRAP 5

[ 20](signal_8h.md#aa86c630133e5b5174ac970227b273446)#define SIGABRT 6

[ 21](signal_8h.md#aead3d488474201acf18c4b63d91edc3c)#define SIGBUS 7

[ 22](signal_8h.md#a7fbba29aec3e4a8daae12935299df92d)#define SIGFPE 8

[ 23](signal_8h.md#addd8dcd406ce514ab3b4f576a5343d42)#define SIGKILL 9

[ 24](signal_8h.md#a944a8250e34bfd7991123abd3436d8c0)#define SIGUSR1 10

[ 25](signal_8h.md#ae20b4f7171a09516ea73c9d2745bd596)#define SIGSEGV 11

[ 26](signal_8h.md#abaaa61abe503c43481e35e21b0b5a031)#define SIGUSR2 12

[ 27](signal_8h.md#a57e9c8c5fa13bf86bc779a9f6f408b7c)#define SIGPIPE 13

[ 28](signal_8h.md#aa6946723c6b7a86ec3c33caaf832840b)#define SIGALRM 14

[ 29](signal_8h.md#a682182a5e5f38fd61f4311501e9dac5d)#define SIGTERM 15

30/\* 16 not used \*/

[ 31](signal_8h.md#a0e63521a64cc8bc2b91d36a87d32c9f8)#define SIGCHLD 17

[ 32](signal_8h.md#a024f43063003e753afc6cca1acd6e104)#define SIGCONT 18

[ 33](signal_8h.md#a069e358bc9a864b7dc4fed2440eda14c)#define SIGSTOP 19

[ 34](signal_8h.md#abe65c086e01f0d286b7a785a7e3cdd1a)#define SIGTSTP 20

[ 35](signal_8h.md#a2c146e34a6b5a78dfba41cded3331181)#define SIGTTIN 21

[ 36](signal_8h.md#a782864287613e2c5c030411fa9c5e9b1)#define SIGTTOU 22

[ 37](signal_8h.md#ad9ff13149e36144a4ea28788948c34dd)#define SIGURG 23

[ 38](signal_8h.md#a7265cbba4972503c1c30a2e52a929874)#define SIGXCPU 24

[ 39](signal_8h.md#a75440a7aa885a1052dfd3b4393fd9baa)#define SIGXFSZ 25

[ 40](signal_8h.md#a71403d2f5240e409e213060ea3301851)#define SIGVTALRM 26

[ 41](signal_8h.md#ab6bd2a2ff7e58d45965ef257f96dfe65)#define SIGPROF 27

42/\* 28 not used \*/

[ 43](signal_8h.md#a1614264a836d6a5642554775ef0134d0)#define SIGPOLL 29

44/\* 30 not used \*/

[ 45](signal_8h.md#a8bacf9eb18fd539099c1bb4666c45d60)#define SIGSYS 31

46

[ 47](signal_8h.md#ad7f754398cdc81462f3d626e74a41b69)#define RTSIG\_MAX CONFIG\_POSIX\_RTSIG\_MAX

[ 48](signal_8h.md#ae89f9a1282bd2d1b2a2b310c12ea16a5)#define SIGRTMIN 32

[ 49](signal_8h.md#a5336d2c76af22b10373e3dd28fb3b0f0)#define SIGRTMAX (SIGRTMIN + RTSIG\_MAX)

50#define \_NSIG (SIGRTMAX + 1)

51

52BUILD\_ASSERT([RTSIG\_MAX](signal_8h.md#ad7f754398cdc81462f3d626e74a41b69) >= 0);

53

[ 54](structsigset__t.md)typedef struct {

[ 55](structsigset__t.md#a28eafd4a022848d48f3c466e2106f2e3) unsigned long [sig](structsigset__t.md#a28eafd4a022848d48f3c466e2106f2e3)[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(\_NSIG, [BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3))];

56} [sigset\_t](structsigset__t.md);

57

58#ifndef SIGEV\_NONE

[ 59](signal_8h.md#aced9a66610d9d61756999ce4f103740e)#define SIGEV\_NONE 1

60#endif

61

62#ifndef SIGEV\_SIGNAL

[ 63](signal_8h.md#a06d5881eeb84e6ac35f5b801c380dbb6)#define SIGEV\_SIGNAL 2

64#endif

65

66#ifndef SIGEV\_THREAD

[ 67](signal_8h.md#a29ccb6a17fa90a1357b478f62af7fca0)#define SIGEV\_THREAD 3

68#endif

69

70#ifndef SIG\_BLOCK

[ 71](signal_8h.md#a927f6ae16379576d638006c7498ac5d7)#define SIG\_BLOCK 0

72#endif

73#ifndef SIG\_SETMASK

[ 74](signal_8h.md#a37750b78b7ae75fe02ad26e70f6cc845)#define SIG\_SETMASK 1

75#endif

76#ifndef SIG\_UNBLOCK

[ 77](signal_8h.md#a5fcd73313a63dac2cc7eb3b654215250)#define SIG\_UNBLOCK 2

78#endif

79

[ 80](signal_8h.md#a5d486213aa4f744f497959af6917e2a0)typedef int [sig\_atomic\_t](signal_8h.md#a5d486213aa4f744f497959af6917e2a0); /\* Atomic entity type (ANSI) \*/

81

[ 82](unionsigval.md)union [sigval](unionsigval.md) {

[ 83](unionsigval.md#a4668f1bd7463de7b70bd0022207e26ac) void \*[sival\_ptr](unionsigval.md#a4668f1bd7463de7b70bd0022207e26ac);

[ 84](unionsigval.md#a560393252ee7edc37df44bf1c11bdbdd) int [sival\_int](unionsigval.md#a560393252ee7edc37df44bf1c11bdbdd);

85};

86

[ 87](structsigevent.md)struct [sigevent](structsigevent.md) {

[ 88](structsigevent.md#ae3636bc03a98e9f92bf154dfefaa9b43) void (\*[sigev\_notify\_function](structsigevent.md#ae3636bc03a98e9f92bf154dfefaa9b43))(union [sigval](unionsigval.md) val);

[ 89](structsigevent.md#a5a687d2092b237d76eb08e2d46a5115f) pthread\_attr\_t \*[sigev\_notify\_attributes](structsigevent.md#a5a687d2092b237d76eb08e2d46a5115f);

[ 90](structsigevent.md#a757af1e34b87e3f66bbc08c514017a2c) union [sigval](unionsigval.md) [sigev\_value](structsigevent.md#a757af1e34b87e3f66bbc08c514017a2c);

[ 91](structsigevent.md#aae9a19d879c38e0c4e8a9bf738c5081e) int [sigev\_notify](structsigevent.md#aae9a19d879c38e0c4e8a9bf738c5081e);

[ 92](structsigevent.md#a5c645ec1d12bb46efc3f4097c52b665d) int [sigev\_signo](structsigevent.md#a5c645ec1d12bb46efc3f4097c52b665d);

93};

94

95#ifdef CONFIG\_POSIX\_SIGNAL

96char \*strsignal(int signum);

97int sigemptyset([sigset\_t](structsigset__t.md) \*set);

98int sigfillset([sigset\_t](structsigset__t.md) \*set);

99int sigaddset([sigset\_t](structsigset__t.md) \*set, int signo);

100int sigdelset([sigset\_t](structsigset__t.md) \*set, int signo);

101int sigismember(const [sigset\_t](structsigset__t.md) \*set, int signo);

102int sigprocmask(int how, const [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) set, [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) oset);

103

104int pthread\_sigmask(int how, const [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) set, [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) oset);

105#endif /\* CONFIG\_POSIX\_SIGNAL \*/

106

107#ifdef \_\_cplusplus

108}

109#endif

110

111#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SIGNAL\_H\_ \*/

[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)

#define BITS\_PER\_LONG

Number of bits in a long int.

**Definition** util.h:58

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:318

[posix\_types.h](posix__types_8h.md)

[sig\_atomic\_t](signal_8h.md#a5d486213aa4f744f497959af6917e2a0)

int sig\_atomic\_t

**Definition** signal.h:80

[RTSIG\_MAX](signal_8h.md#ad7f754398cdc81462f3d626e74a41b69)

#define RTSIG\_MAX

**Definition** signal.h:47

[sigevent](structsigevent.md)

**Definition** signal.h:87

[sigevent::sigev\_notify\_attributes](structsigevent.md#a5a687d2092b237d76eb08e2d46a5115f)

pthread\_attr\_t \* sigev\_notify\_attributes

**Definition** signal.h:89

[sigevent::sigev\_signo](structsigevent.md#a5c645ec1d12bb46efc3f4097c52b665d)

int sigev\_signo

**Definition** signal.h:92

[sigevent::sigev\_value](structsigevent.md#a757af1e34b87e3f66bbc08c514017a2c)

union sigval sigev\_value

**Definition** signal.h:90

[sigevent::sigev\_notify](structsigevent.md#aae9a19d879c38e0c4e8a9bf738c5081e)

int sigev\_notify

**Definition** signal.h:91

[sigevent::sigev\_notify\_function](structsigevent.md#ae3636bc03a98e9f92bf154dfefaa9b43)

void(\* sigev\_notify\_function)(union sigval val)

**Definition** signal.h:88

[sigset\_t](structsigset__t.md)

**Definition** signal.h:54

[sigset\_t::sig](structsigset__t.md#a28eafd4a022848d48f3c466e2106f2e3)

unsigned long sig[DIV\_ROUND\_UP(((32+CONFIG\_POSIX\_RTSIG\_MAX)+1), BITS\_PER\_LONG)]

**Definition** signal.h:55

[sigval](unionsigval.md)

**Definition** signal.h:82

[sigval::sival\_ptr](unionsigval.md#a4668f1bd7463de7b70bd0022207e26ac)

void \* sival\_ptr

**Definition** signal.h:83

[sigval::sival\_int](unionsigval.md#a560393252ee7edc37df44bf1c11bdbdd)

int sival\_int

**Definition** signal.h:84

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [signal.h](signal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
