---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/include_2zephyr_2posix_2signal_8h_source.html
original_path: doxygen/html/include_2zephyr_2posix_2signal_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

signal.h

[Go to the documentation of this file.](include_2zephyr_2posix_2signal_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SIGNAL\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SIGNAL\_H\_

8

9/\* include posix\_types.h before posix\_features.h (here) to avoid build errors against newlib \*/

10#include <[zephyr/posix/posix\_types.h](posix__types_8h.md)>

11#include "[posix\_features.h](posix__features_8h.md)"

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 17](include_2zephyr_2posix_2signal_8h.md#a136c64ec2d1306de745e39d6aee362ca)#define SIGHUP 1

[ 18](include_2zephyr_2posix_2signal_8h.md#a487309e3e9e0527535644115204a639a)#define SIGINT 2

[ 19](include_2zephyr_2posix_2signal_8h.md#a62045b465be11891160d53c10861b16c)#define SIGQUIT 3

[ 20](include_2zephyr_2posix_2signal_8h.md#a4c9c5284f8c8d146bd7a93d25017fc62)#define SIGILL 4

[ 21](include_2zephyr_2posix_2signal_8h.md#aa2beb906ab1b46676e63823f4e773c38)#define SIGTRAP 5

[ 22](include_2zephyr_2posix_2signal_8h.md#aa86c630133e5b5174ac970227b273446)#define SIGABRT 6

[ 23](include_2zephyr_2posix_2signal_8h.md#aead3d488474201acf18c4b63d91edc3c)#define SIGBUS 7

[ 24](include_2zephyr_2posix_2signal_8h.md#a7fbba29aec3e4a8daae12935299df92d)#define SIGFPE 8

[ 25](include_2zephyr_2posix_2signal_8h.md#addd8dcd406ce514ab3b4f576a5343d42)#define SIGKILL 9

[ 26](include_2zephyr_2posix_2signal_8h.md#a944a8250e34bfd7991123abd3436d8c0)#define SIGUSR1 10

[ 27](include_2zephyr_2posix_2signal_8h.md#ae20b4f7171a09516ea73c9d2745bd596)#define SIGSEGV 11

[ 28](include_2zephyr_2posix_2signal_8h.md#abaaa61abe503c43481e35e21b0b5a031)#define SIGUSR2 12

[ 29](include_2zephyr_2posix_2signal_8h.md#a57e9c8c5fa13bf86bc779a9f6f408b7c)#define SIGPIPE 13

[ 30](include_2zephyr_2posix_2signal_8h.md#aa6946723c6b7a86ec3c33caaf832840b)#define SIGALRM 14

[ 31](include_2zephyr_2posix_2signal_8h.md#a682182a5e5f38fd61f4311501e9dac5d)#define SIGTERM 15

32/\* 16 not used \*/

[ 33](include_2zephyr_2posix_2signal_8h.md#a0e63521a64cc8bc2b91d36a87d32c9f8)#define SIGCHLD 17

[ 34](include_2zephyr_2posix_2signal_8h.md#a024f43063003e753afc6cca1acd6e104)#define SIGCONT 18

[ 35](include_2zephyr_2posix_2signal_8h.md#a069e358bc9a864b7dc4fed2440eda14c)#define SIGSTOP 19

[ 36](include_2zephyr_2posix_2signal_8h.md#abe65c086e01f0d286b7a785a7e3cdd1a)#define SIGTSTP 20

[ 37](include_2zephyr_2posix_2signal_8h.md#a2c146e34a6b5a78dfba41cded3331181)#define SIGTTIN 21

[ 38](include_2zephyr_2posix_2signal_8h.md#a782864287613e2c5c030411fa9c5e9b1)#define SIGTTOU 22

[ 39](include_2zephyr_2posix_2signal_8h.md#ad9ff13149e36144a4ea28788948c34dd)#define SIGURG 23

[ 40](include_2zephyr_2posix_2signal_8h.md#a7265cbba4972503c1c30a2e52a929874)#define SIGXCPU 24

[ 41](include_2zephyr_2posix_2signal_8h.md#a75440a7aa885a1052dfd3b4393fd9baa)#define SIGXFSZ 25

[ 42](include_2zephyr_2posix_2signal_8h.md#a71403d2f5240e409e213060ea3301851)#define SIGVTALRM 26

[ 43](include_2zephyr_2posix_2signal_8h.md#ab6bd2a2ff7e58d45965ef257f96dfe65)#define SIGPROF 27

44/\* 28 not used \*/

[ 45](include_2zephyr_2posix_2signal_8h.md#a1614264a836d6a5642554775ef0134d0)#define SIGPOLL 29

46/\* 30 not used \*/

[ 47](include_2zephyr_2posix_2signal_8h.md#a8bacf9eb18fd539099c1bb4666c45d60)#define SIGSYS 31

48

[ 49](include_2zephyr_2posix_2signal_8h.md#ae89f9a1282bd2d1b2a2b310c12ea16a5)#define SIGRTMIN 32

[ 50](include_2zephyr_2posix_2signal_8h.md#a5336d2c76af22b10373e3dd28fb3b0f0)#define SIGRTMAX (SIGRTMIN + RTSIG\_MAX)

51#define \_NSIG (SIGRTMAX + 1)

52

53BUILD\_ASSERT([RTSIG\_MAX](posix__features_8h.md#ad7f754398cdc81462f3d626e74a41b69) >= 0);

54

[ 55](structsigset__t.md)typedef struct {

[ 56](structsigset__t.md#ac970376511e3a440d413666a0998d69e) unsigned long [sig](structsigset__t.md#ac970376511e3a440d413666a0998d69e)[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(\_NSIG, [BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3))];

57} [sigset\_t](structsigset__t.md);

58

59#ifndef SIGEV\_NONE

[ 60](include_2zephyr_2posix_2signal_8h.md#aced9a66610d9d61756999ce4f103740e)#define SIGEV\_NONE 1

61#endif

62

63#ifndef SIGEV\_SIGNAL

[ 64](include_2zephyr_2posix_2signal_8h.md#a06d5881eeb84e6ac35f5b801c380dbb6)#define SIGEV\_SIGNAL 2

65#endif

66

67#ifndef SIGEV\_THREAD

[ 68](include_2zephyr_2posix_2signal_8h.md#a29ccb6a17fa90a1357b478f62af7fca0)#define SIGEV\_THREAD 3

69#endif

70

71#ifndef SIG\_BLOCK

[ 72](include_2zephyr_2posix_2signal_8h.md#a927f6ae16379576d638006c7498ac5d7)#define SIG\_BLOCK 0

73#endif

74#ifndef SIG\_SETMASK

[ 75](include_2zephyr_2posix_2signal_8h.md#a37750b78b7ae75fe02ad26e70f6cc845)#define SIG\_SETMASK 1

76#endif

77#ifndef SIG\_UNBLOCK

[ 78](include_2zephyr_2posix_2signal_8h.md#a5fcd73313a63dac2cc7eb3b654215250)#define SIG\_UNBLOCK 2

79#endif

80

[ 81](include_2zephyr_2posix_2signal_8h.md#a27d5dc561093d6243542e6a2465bc0f8)#define SIG\_DFL ((void \*)0)

[ 82](include_2zephyr_2posix_2signal_8h.md#acf0e499b0ac946b366b4f47a3b3e8b9e)#define SIG\_IGN ((void \*)1)

[ 83](include_2zephyr_2posix_2signal_8h.md#a3c330fbddd84bf34e65af370b11998d6)#define SIG\_ERR ((void \*)-1)

84

[ 85](include_2zephyr_2posix_2signal_8h.md#af9e4986b4f6bb9bd932b2fc8166301b9)#define SI\_USER 1

[ 86](include_2zephyr_2posix_2signal_8h.md#a4f23f53a46f88a96a0f28e23f7a9bad6)#define SI\_QUEUE 2

[ 87](include_2zephyr_2posix_2signal_8h.md#ab57ec52e57fbb49071f96f255bc7c31b)#define SI\_TIMER 3

[ 88](include_2zephyr_2posix_2signal_8h.md#aa8ff6c6d4af21cf9380de1e8fef9db4c)#define SI\_ASYNCIO 4

[ 89](include_2zephyr_2posix_2signal_8h.md#afdf808efb3ebd166f67910156146c8fc)#define SI\_MESGQ 5

90

[ 91](include_2zephyr_2posix_2signal_8h.md#a5d486213aa4f744f497959af6917e2a0)typedef int [sig\_atomic\_t](include_2zephyr_2posix_2signal_8h.md#a5d486213aa4f744f497959af6917e2a0); /\* Atomic entity type (ANSI) \*/

92

[ 93](unionsigval.md)union [sigval](unionsigval.md) {

[ 94](unionsigval.md#a4668f1bd7463de7b70bd0022207e26ac) void \*[sival\_ptr](unionsigval.md#a4668f1bd7463de7b70bd0022207e26ac);

[ 95](unionsigval.md#a560393252ee7edc37df44bf1c11bdbdd) int [sival\_int](unionsigval.md#a560393252ee7edc37df44bf1c11bdbdd);

96};

97

[ 98](structsigevent.md)struct [sigevent](structsigevent.md) {

[ 99](structsigevent.md#ae3636bc03a98e9f92bf154dfefaa9b43) void (\*[sigev\_notify\_function](structsigevent.md#ae3636bc03a98e9f92bf154dfefaa9b43))(union [sigval](unionsigval.md) val);

[ 100](structsigevent.md#a5a687d2092b237d76eb08e2d46a5115f) [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*[sigev\_notify\_attributes](structsigevent.md#a5a687d2092b237d76eb08e2d46a5115f);

[ 101](structsigevent.md#a757af1e34b87e3f66bbc08c514017a2c) union [sigval](unionsigval.md) [sigev\_value](structsigevent.md#a757af1e34b87e3f66bbc08c514017a2c);

[ 102](structsigevent.md#aae9a19d879c38e0c4e8a9bf738c5081e) int [sigev\_notify](structsigevent.md#aae9a19d879c38e0c4e8a9bf738c5081e);

[ 103](structsigevent.md#a5c645ec1d12bb46efc3f4097c52b665d) int [sigev\_signo](structsigevent.md#a5c645ec1d12bb46efc3f4097c52b665d);

104};

105

[ 106](structsiginfo__t.md)typedef struct {

[ 107](structsiginfo__t.md#a238821f6eb15317d3d7b10efef80b9c7) int [si\_signo](structsiginfo__t.md#a238821f6eb15317d3d7b10efef80b9c7);

[ 108](structsiginfo__t.md#a0dd36ae3e9df589f5755f88c93671c2d) int [si\_code](structsiginfo__t.md#a0dd36ae3e9df589f5755f88c93671c2d);

[ 109](structsiginfo__t.md#aea6512792c4af9f46ba221e454b6e0a7) union [sigval](unionsigval.md) [si\_value](structsiginfo__t.md#aea6512792c4af9f46ba221e454b6e0a7);

110} [siginfo\_t](structsiginfo__t.md);

111

[ 112](structsigaction.md)struct [sigaction](structsigaction.md) {

[ 113](structsigaction.md#a02261e69c38b387de4c6b96a26e26199) void (\*[sa\_handler](structsigaction.md#a02261e69c38b387de4c6b96a26e26199))(int signno);

[ 114](structsigaction.md#a684e70081d03d46ce70af097ea5cfd49) [sigset\_t](structsigset__t.md) [sa\_mask](structsigaction.md#a684e70081d03d46ce70af097ea5cfd49);

[ 115](structsigaction.md#aea0dabe7a03641c8b426521f4406b425) int [sa\_flags](structsigaction.md#aea0dabe7a03641c8b426521f4406b425);

[ 116](structsigaction.md#a068409137809e8e6e4a522d29daa65af) void (\*[sa\_sigaction](structsigaction.md#a068409137809e8e6e4a522d29daa65af))(int signo, [siginfo\_t](structsiginfo__t.md) \*info, void \*context);

117};

118

[ 119](include_2zephyr_2posix_2signal_8h.md#a9b897a32dbc17d103b01b6e54c2a6430)typedef void (\*[sighandler\_t](include_2zephyr_2posix_2signal_8h.md#a9b897a32dbc17d103b01b6e54c2a6430))(int signo);

120

[ 121](include_2zephyr_2posix_2signal_8h.md#a8c476685d78ea93ee343f8a0580c79fe)unsigned int [alarm](include_2zephyr_2posix_2signal_8h.md#a8c476685d78ea93ee343f8a0580c79fe)(unsigned int seconds);

[ 122](include_2zephyr_2posix_2signal_8h.md#a4539db972bcf3dd8c8b429af0dc3789d)int [kill](include_2zephyr_2posix_2signal_8h.md#a4539db972bcf3dd8c8b429af0dc3789d)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, int sig);

[ 123](include_2zephyr_2posix_2signal_8h.md#a47a6ff5872f457ee230458137f2b2409)int [pause](include_2zephyr_2posix_2signal_8h.md#a47a6ff5872f457ee230458137f2b2409)(void);

[ 124](include_2zephyr_2posix_2signal_8h.md#a59fe78a089520953775195912c6d923a)int [raise](include_2zephyr_2posix_2signal_8h.md#a59fe78a089520953775195912c6d923a)(int signo);

[ 125](include_2zephyr_2posix_2signal_8h.md#a5dabd0b7783afd0e4cab78446436e25c)int [sigaction](include_2zephyr_2posix_2signal_8h.md#a5dabd0b7783afd0e4cab78446436e25c)(int sig, const struct [sigaction](structsigaction.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) act, struct [sigaction](structsigaction.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) oact);

[ 126](include_2zephyr_2posix_2signal_8h.md#a7b91eecad5998acd6162fde3ab530d7a)int [sigpending](include_2zephyr_2posix_2signal_8h.md#a7b91eecad5998acd6162fde3ab530d7a)([sigset\_t](structsigset__t.md) \*set);

[ 127](include_2zephyr_2posix_2signal_8h.md#a20d9f879bbe69c79f62bd3813fcc1e63)int [sigsuspend](include_2zephyr_2posix_2signal_8h.md#a20d9f879bbe69c79f62bd3813fcc1e63)(const [sigset\_t](structsigset__t.md) \*sigmask);

[ 128](include_2zephyr_2posix_2signal_8h.md#a328385f8347e4f287220fd6a867bde23)int [sigwait](include_2zephyr_2posix_2signal_8h.md#a328385f8347e4f287220fd6a867bde23)(const [sigset\_t](structsigset__t.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) set, int \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) signo);

[ 129](include_2zephyr_2posix_2signal_8h.md#a8b856eee87a225f697f1b264ebd6a47b)char \*[strsignal](include_2zephyr_2posix_2signal_8h.md#a8b856eee87a225f697f1b264ebd6a47b)(int signum);

[ 130](include_2zephyr_2posix_2signal_8h.md#a5925352f90eb589393274fa0376d7def)int [sigemptyset](include_2zephyr_2posix_2signal_8h.md#a5925352f90eb589393274fa0376d7def)([sigset\_t](structsigset__t.md) \*set);

[ 131](include_2zephyr_2posix_2signal_8h.md#a88d7bbc77ea1569ee21c90db549ea023)int [sigfillset](include_2zephyr_2posix_2signal_8h.md#a88d7bbc77ea1569ee21c90db549ea023)([sigset\_t](structsigset__t.md) \*set);

[ 132](include_2zephyr_2posix_2signal_8h.md#acab58ba1dfe2108f96d9f28e249a8c7d)int [sigaddset](include_2zephyr_2posix_2signal_8h.md#acab58ba1dfe2108f96d9f28e249a8c7d)([sigset\_t](structsigset__t.md) \*set, int signo);

[ 133](include_2zephyr_2posix_2signal_8h.md#ac3471f7a860cdfb70afe89a90a074c69)int [sigdelset](include_2zephyr_2posix_2signal_8h.md#ac3471f7a860cdfb70afe89a90a074c69)([sigset\_t](structsigset__t.md) \*set, int signo);

[ 134](include_2zephyr_2posix_2signal_8h.md#a2bd11ded490df632440aa08f320aad17)int [sigismember](include_2zephyr_2posix_2signal_8h.md#a2bd11ded490df632440aa08f320aad17)(const [sigset\_t](structsigset__t.md) \*set, int signo);

[ 135](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)[sighandler\_t](include_2zephyr_2posix_2signal_8h.md#a9b897a32dbc17d103b01b6e54c2a6430) [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)(int signo, [sighandler\_t](include_2zephyr_2posix_2signal_8h.md#a9b897a32dbc17d103b01b6e54c2a6430) handler);

[ 136](include_2zephyr_2posix_2signal_8h.md#a6e6b04897703c43b2ad10013041ad152)int [sigprocmask](include_2zephyr_2posix_2signal_8h.md#a6e6b04897703c43b2ad10013041ad152)(int how, const [sigset\_t](structsigset__t.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) set, [sigset\_t](structsigset__t.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) oset);

137

[ 138](include_2zephyr_2posix_2signal_8h.md#a16972ede9065cb2709fcfc6a84272116)int [pthread\_sigmask](include_2zephyr_2posix_2signal_8h.md#a16972ede9065cb2709fcfc6a84272116)(int how, const [sigset\_t](structsigset__t.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) set, [sigset\_t](structsigset__t.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) oset);

139

140#ifdef \_\_cplusplus

141}

142#endif

143

144#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SIGNAL\_H\_ \*/

[BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)

#define BITS\_PER\_LONG

Number of bits in a long int.

**Definition** util.h:70

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:352

[pthread\_sigmask](include_2zephyr_2posix_2signal_8h.md#a16972ede9065cb2709fcfc6a84272116)

int pthread\_sigmask(int how, const sigset\_t \*ZRESTRICT set, sigset\_t \*ZRESTRICT oset)

[sigsuspend](include_2zephyr_2posix_2signal_8h.md#a20d9f879bbe69c79f62bd3813fcc1e63)

int sigsuspend(const sigset\_t \*sigmask)

[sigismember](include_2zephyr_2posix_2signal_8h.md#a2bd11ded490df632440aa08f320aad17)

int sigismember(const sigset\_t \*set, int signo)

[sigwait](include_2zephyr_2posix_2signal_8h.md#a328385f8347e4f287220fd6a867bde23)

int sigwait(const sigset\_t \*ZRESTRICT set, int \*ZRESTRICT signo)

[kill](include_2zephyr_2posix_2signal_8h.md#a4539db972bcf3dd8c8b429af0dc3789d)

int kill(pid\_t pid, int sig)

[pause](include_2zephyr_2posix_2signal_8h.md#a47a6ff5872f457ee230458137f2b2409)

int pause(void)

[sigemptyset](include_2zephyr_2posix_2signal_8h.md#a5925352f90eb589393274fa0376d7def)

int sigemptyset(sigset\_t \*set)

[raise](include_2zephyr_2posix_2signal_8h.md#a59fe78a089520953775195912c6d923a)

int raise(int signo)

[sig\_atomic\_t](include_2zephyr_2posix_2signal_8h.md#a5d486213aa4f744f497959af6917e2a0)

int sig\_atomic\_t

**Definition** signal.h:91

[sigaction](include_2zephyr_2posix_2signal_8h.md#a5dabd0b7783afd0e4cab78446436e25c)

int sigaction(int sig, const struct sigaction \*ZRESTRICT act, struct sigaction \*ZRESTRICT oact)

[sigprocmask](include_2zephyr_2posix_2signal_8h.md#a6e6b04897703c43b2ad10013041ad152)

int sigprocmask(int how, const sigset\_t \*ZRESTRICT set, sigset\_t \*ZRESTRICT oset)

[sigpending](include_2zephyr_2posix_2signal_8h.md#a7b91eecad5998acd6162fde3ab530d7a)

int sigpending(sigset\_t \*set)

[sigfillset](include_2zephyr_2posix_2signal_8h.md#a88d7bbc77ea1569ee21c90db549ea023)

int sigfillset(sigset\_t \*set)

[strsignal](include_2zephyr_2posix_2signal_8h.md#a8b856eee87a225f697f1b264ebd6a47b)

char \* strsignal(int signum)

[alarm](include_2zephyr_2posix_2signal_8h.md#a8c476685d78ea93ee343f8a0580c79fe)

unsigned int alarm(unsigned int seconds)

[sighandler\_t](include_2zephyr_2posix_2signal_8h.md#a9b897a32dbc17d103b01b6e54c2a6430)

void(\* sighandler\_t)(int signo)

**Definition** signal.h:119

[sigdelset](include_2zephyr_2posix_2signal_8h.md#ac3471f7a860cdfb70afe89a90a074c69)

int sigdelset(sigset\_t \*set, int signo)

[sigaddset](include_2zephyr_2posix_2signal_8h.md#acab58ba1dfe2108f96d9f28e249a8c7d)

int sigaddset(sigset\_t \*set, int signo)

[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)

sighandler\_t signal(int signo, sighandler\_t handler)

[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[posix\_features.h](posix__features_8h.md)

[RTSIG\_MAX](posix__features_8h.md#ad7f754398cdc81462f3d626e74a41b69)

#define RTSIG\_MAX

**Definition** posix\_features.h:326

[posix\_types.h](posix__types_8h.md)

[pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a)

struct pthread\_attr pthread\_attr\_t

**Definition** posix\_types.h:103

[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)

int pid\_t

**Definition** posix\_types.h:79

[sigaction](structsigaction.md)

**Definition** signal.h:112

[sigaction::sa\_handler](structsigaction.md#a02261e69c38b387de4c6b96a26e26199)

void(\* sa\_handler)(int signno)

**Definition** signal.h:113

[sigaction::sa\_sigaction](structsigaction.md#a068409137809e8e6e4a522d29daa65af)

void(\* sa\_sigaction)(int signo, siginfo\_t \*info, void \*context)

**Definition** signal.h:116

[sigaction::sa\_mask](structsigaction.md#a684e70081d03d46ce70af097ea5cfd49)

sigset\_t sa\_mask

**Definition** signal.h:114

[sigaction::sa\_flags](structsigaction.md#aea0dabe7a03641c8b426521f4406b425)

int sa\_flags

**Definition** signal.h:115

[sigevent](structsigevent.md)

**Definition** signal.h:98

[sigevent::sigev\_notify\_attributes](structsigevent.md#a5a687d2092b237d76eb08e2d46a5115f)

pthread\_attr\_t \* sigev\_notify\_attributes

**Definition** signal.h:100

[sigevent::sigev\_signo](structsigevent.md#a5c645ec1d12bb46efc3f4097c52b665d)

int sigev\_signo

**Definition** signal.h:103

[sigevent::sigev\_value](structsigevent.md#a757af1e34b87e3f66bbc08c514017a2c)

union sigval sigev\_value

**Definition** signal.h:101

[sigevent::sigev\_notify](structsigevent.md#aae9a19d879c38e0c4e8a9bf738c5081e)

int sigev\_notify

**Definition** signal.h:102

[sigevent::sigev\_notify\_function](structsigevent.md#ae3636bc03a98e9f92bf154dfefaa9b43)

void(\* sigev\_notify\_function)(union sigval val)

**Definition** signal.h:99

[siginfo\_t](structsiginfo__t.md)

**Definition** signal.h:106

[siginfo\_t::si\_code](structsiginfo__t.md#a0dd36ae3e9df589f5755f88c93671c2d)

int si\_code

**Definition** signal.h:108

[siginfo\_t::si\_signo](structsiginfo__t.md#a238821f6eb15317d3d7b10efef80b9c7)

int si\_signo

**Definition** signal.h:107

[siginfo\_t::si\_value](structsiginfo__t.md#aea6512792c4af9f46ba221e454b6e0a7)

union sigval si\_value

**Definition** signal.h:109

[sigset\_t](structsigset__t.md)

**Definition** signal.h:55

[sigset\_t::sig](structsigset__t.md#ac970376511e3a440d413666a0998d69e)

unsigned long sig[DIV\_ROUND\_UP(((32+COND\_CODE\_1(CONFIG\_POSIX\_REALTIME\_SIGNALS,(CONFIG\_POSIX\_RTSIG\_MAX),(0)))+1), BITS\_PER\_LONG)]

**Definition** signal.h:56

[sigval](unionsigval.md)

**Definition** signal.h:93

[sigval::sival\_ptr](unionsigval.md#a4668f1bd7463de7b70bd0022207e26ac)

void \* sival\_ptr

**Definition** signal.h:94

[sigval::sival\_int](unionsigval.md#a560393252ee7edc37df44bf1c11bdbdd)

int sival\_int

**Definition** signal.h:95

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [signal.h](include_2zephyr_2posix_2signal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
