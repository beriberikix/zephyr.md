---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/include_2zephyr_2posix_2signal_8h.html
original_path: doxygen/html/include_2zephyr_2posix_2signal_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

signal.h File Reference

`#include "[posix_types.h](posix__types_8h_source.md)"`  
`#include "[posix_features.h](posix__features_8h_source.md)"`

[Go to the source code of this file.](include_2zephyr_2posix_2signal_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sigset\_t](structsigset__t.md) |
| union | [sigval](unionsigval.md) |
| struct | [sigevent](structsigevent.md) |

| Macros | |
| --- | --- |
| #define | [SIGHUP](#a136c64ec2d1306de745e39d6aee362ca)   1 |
|  | Hangup. |
| #define | [SIGINT](#a487309e3e9e0527535644115204a639a)   2 |
|  | Interrupt. |
| #define | [SIGQUIT](#a62045b465be11891160d53c10861b16c)   3 |
|  | Quit. |
| #define | [SIGILL](#a4c9c5284f8c8d146bd7a93d25017fc62)   4 |
|  | Illegal instruction. |
| #define | [SIGTRAP](#aa2beb906ab1b46676e63823f4e773c38)   5 |
|  | Trace/breakpoint trap. |
| #define | [SIGABRT](#aa86c630133e5b5174ac970227b273446)   6 |
|  | Aborted. |
| #define | [SIGBUS](#aead3d488474201acf18c4b63d91edc3c)   7 |
|  | Bus error. |
| #define | [SIGFPE](#a7fbba29aec3e4a8daae12935299df92d)   8 |
|  | Arithmetic exception. |
| #define | [SIGKILL](#addd8dcd406ce514ab3b4f576a5343d42)   9 |
|  | Killed. |
| #define | [SIGUSR1](#a944a8250e34bfd7991123abd3436d8c0)   10 |
|  | User-defined signal 1. |
| #define | [SIGSEGV](#ae20b4f7171a09516ea73c9d2745bd596)   11 |
|  | Invalid memory reference. |
| #define | [SIGUSR2](#abaaa61abe503c43481e35e21b0b5a031)   12 |
|  | User-defined signal 2. |
| #define | [SIGPIPE](#a57e9c8c5fa13bf86bc779a9f6f408b7c)   13 |
|  | Broken pipe. |
| #define | [SIGALRM](#aa6946723c6b7a86ec3c33caaf832840b)   14 |
|  | Alarm clock. |
| #define | [SIGTERM](#a682182a5e5f38fd61f4311501e9dac5d)   15 |
|  | Terminated. |
| #define | [SIGCHLD](#a0e63521a64cc8bc2b91d36a87d32c9f8)   17 |
|  | Child status changed. |
| #define | [SIGCONT](#a024f43063003e753afc6cca1acd6e104)   18 |
|  | Continued. |
| #define | [SIGSTOP](#a069e358bc9a864b7dc4fed2440eda14c)   19 |
|  | Stop executing. |
| #define | [SIGTSTP](#abe65c086e01f0d286b7a785a7e3cdd1a)   20 |
|  | Stopped. |
| #define | [SIGTTIN](#a2c146e34a6b5a78dfba41cded3331181)   21 |
|  | Stopped (read). |
| #define | [SIGTTOU](#a782864287613e2c5c030411fa9c5e9b1)   22 |
|  | Stopped (write). |
| #define | [SIGURG](#ad9ff13149e36144a4ea28788948c34dd)   23 |
|  | Urgent I/O condition. |
| #define | [SIGXCPU](#a7265cbba4972503c1c30a2e52a929874)   24 |
|  | CPU time limit exceeded. |
| #define | [SIGXFSZ](#a75440a7aa885a1052dfd3b4393fd9baa)   25 |
|  | File size limit exceeded. |
| #define | [SIGVTALRM](#a71403d2f5240e409e213060ea3301851)   26 |
|  | Virtual timer expired. |
| #define | [SIGPROF](#ab6bd2a2ff7e58d45965ef257f96dfe65)   27 |
|  | Profiling timer expired. |
| #define | [SIGPOLL](#a1614264a836d6a5642554775ef0134d0)   29 |
|  | Pollable event occurred. |
| #define | [SIGSYS](#a8bacf9eb18fd539099c1bb4666c45d60)   31 |
|  | Bad system call. |
| #define | [SIGRTMIN](#ae89f9a1282bd2d1b2a2b310c12ea16a5)   32 |
| #define | [SIGRTMAX](#a5336d2c76af22b10373e3dd28fb3b0f0)   ([SIGRTMIN](#ae89f9a1282bd2d1b2a2b310c12ea16a5) + [RTSIG\_MAX](posix__features_8h.md#ad7f754398cdc81462f3d626e74a41b69)) |
| #define | [SIGEV\_NONE](#aced9a66610d9d61756999ce4f103740e)   1 |
| #define | [SIGEV\_SIGNAL](#a06d5881eeb84e6ac35f5b801c380dbb6)   2 |
| #define | [SIGEV\_THREAD](#a29ccb6a17fa90a1357b478f62af7fca0)   3 |
| #define | [SIG\_BLOCK](#a927f6ae16379576d638006c7498ac5d7)   0 |
| #define | [SIG\_SETMASK](#a37750b78b7ae75fe02ad26e70f6cc845)   1 |
| #define | [SIG\_UNBLOCK](#a5fcd73313a63dac2cc7eb3b654215250)   2 |

| Typedefs | |
| --- | --- |
| typedef int | [sig\_atomic\_t](#a5d486213aa4f744f497959af6917e2a0) |

| Functions | |
| --- | --- |
| char \* | [strsignal](#a8b856eee87a225f697f1b264ebd6a47b) (int signum) |
| int | [sigemptyset](#a5925352f90eb589393274fa0376d7def) ([sigset\_t](structsigset__t.md) \*set) |
| int | [sigfillset](#a88d7bbc77ea1569ee21c90db549ea023) ([sigset\_t](structsigset__t.md) \*set) |
| int | [sigaddset](#acab58ba1dfe2108f96d9f28e249a8c7d) ([sigset\_t](structsigset__t.md) \*set, int signo) |
| int | [sigdelset](#ac3471f7a860cdfb70afe89a90a074c69) ([sigset\_t](structsigset__t.md) \*set, int signo) |
| int | [sigismember](#a2bd11ded490df632440aa08f320aad17) (const [sigset\_t](structsigset__t.md) \*set, int signo) |
| int | [sigprocmask](#a6e6b04897703c43b2ad10013041ad152) (int how, const [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) set, [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) oset) |
| int | [pthread\_sigmask](#a16972ede9065cb2709fcfc6a84272116) (int how, const [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) set, [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) oset) |

## Macro Definition Documentation

## [◆ ](#a927f6ae16379576d638006c7498ac5d7)SIG\_BLOCK

| #define SIG\_BLOCK   0 |
| --- |

## [◆ ](#a37750b78b7ae75fe02ad26e70f6cc845)SIG\_SETMASK

| #define SIG\_SETMASK   1 |
| --- |

## [◆ ](#a5fcd73313a63dac2cc7eb3b654215250)SIG\_UNBLOCK

| #define SIG\_UNBLOCK   2 |
| --- |

## [◆ ](#aa86c630133e5b5174ac970227b273446)SIGABRT

| #define SIGABRT   6 |
| --- |

Aborted.

## [◆ ](#aa6946723c6b7a86ec3c33caaf832840b)SIGALRM

| #define SIGALRM   14 |
| --- |

Alarm clock.

## [◆ ](#aead3d488474201acf18c4b63d91edc3c)SIGBUS

| #define SIGBUS   7 |
| --- |

Bus error.

## [◆ ](#a0e63521a64cc8bc2b91d36a87d32c9f8)SIGCHLD

| #define SIGCHLD   17 |
| --- |

Child status changed.

## [◆ ](#a024f43063003e753afc6cca1acd6e104)SIGCONT

| #define SIGCONT   18 |
| --- |

Continued.

## [◆ ](#aced9a66610d9d61756999ce4f103740e)SIGEV\_NONE

| #define SIGEV\_NONE   1 |
| --- |

## [◆ ](#a06d5881eeb84e6ac35f5b801c380dbb6)SIGEV\_SIGNAL

| #define SIGEV\_SIGNAL   2 |
| --- |

## [◆ ](#a29ccb6a17fa90a1357b478f62af7fca0)SIGEV\_THREAD

| #define SIGEV\_THREAD   3 |
| --- |

## [◆ ](#a7fbba29aec3e4a8daae12935299df92d)SIGFPE

| #define SIGFPE   8 |
| --- |

Arithmetic exception.

## [◆ ](#a136c64ec2d1306de745e39d6aee362ca)SIGHUP

| #define SIGHUP   1 |
| --- |

Hangup.

## [◆ ](#a4c9c5284f8c8d146bd7a93d25017fc62)SIGILL

| #define SIGILL   4 |
| --- |

Illegal instruction.

## [◆ ](#a487309e3e9e0527535644115204a639a)SIGINT

| #define SIGINT   2 |
| --- |

Interrupt.

## [◆ ](#addd8dcd406ce514ab3b4f576a5343d42)SIGKILL

| #define SIGKILL   9 |
| --- |

Killed.

## [◆ ](#a57e9c8c5fa13bf86bc779a9f6f408b7c)SIGPIPE

| #define SIGPIPE   13 |
| --- |

Broken pipe.

## [◆ ](#a1614264a836d6a5642554775ef0134d0)SIGPOLL

| #define SIGPOLL   29 |
| --- |

Pollable event occurred.

## [◆ ](#ab6bd2a2ff7e58d45965ef257f96dfe65)SIGPROF

| #define SIGPROF   27 |
| --- |

Profiling timer expired.

## [◆ ](#a62045b465be11891160d53c10861b16c)SIGQUIT

| #define SIGQUIT   3 |
| --- |

Quit.

## [◆ ](#a5336d2c76af22b10373e3dd28fb3b0f0)SIGRTMAX

| #define SIGRTMAX   ([SIGRTMIN](#ae89f9a1282bd2d1b2a2b310c12ea16a5) + [RTSIG\_MAX](posix__features_8h.md#ad7f754398cdc81462f3d626e74a41b69)) |
| --- |

## [◆ ](#ae89f9a1282bd2d1b2a2b310c12ea16a5)SIGRTMIN

| #define SIGRTMIN   32 |
| --- |

## [◆ ](#ae20b4f7171a09516ea73c9d2745bd596)SIGSEGV

| #define SIGSEGV   11 |
| --- |

Invalid memory reference.

## [◆ ](#a069e358bc9a864b7dc4fed2440eda14c)SIGSTOP

| #define SIGSTOP   19 |
| --- |

Stop executing.

## [◆ ](#a8bacf9eb18fd539099c1bb4666c45d60)SIGSYS

| #define SIGSYS   31 |
| --- |

Bad system call.

## [◆ ](#a682182a5e5f38fd61f4311501e9dac5d)SIGTERM

| #define SIGTERM   15 |
| --- |

Terminated.

## [◆ ](#aa2beb906ab1b46676e63823f4e773c38)SIGTRAP

| #define SIGTRAP   5 |
| --- |

Trace/breakpoint trap.

## [◆ ](#abe65c086e01f0d286b7a785a7e3cdd1a)SIGTSTP

| #define SIGTSTP   20 |
| --- |

Stopped.

## [◆ ](#a2c146e34a6b5a78dfba41cded3331181)SIGTTIN

| #define SIGTTIN   21 |
| --- |

Stopped (read).

## [◆ ](#a782864287613e2c5c030411fa9c5e9b1)SIGTTOU

| #define SIGTTOU   22 |
| --- |

Stopped (write).

## [◆ ](#ad9ff13149e36144a4ea28788948c34dd)SIGURG

| #define SIGURG   23 |
| --- |

Urgent I/O condition.

## [◆ ](#a944a8250e34bfd7991123abd3436d8c0)SIGUSR1

| #define SIGUSR1   10 |
| --- |

User-defined signal 1.

## [◆ ](#abaaa61abe503c43481e35e21b0b5a031)SIGUSR2

| #define SIGUSR2   12 |
| --- |

User-defined signal 2.

## [◆ ](#a71403d2f5240e409e213060ea3301851)SIGVTALRM

| #define SIGVTALRM   26 |
| --- |

Virtual timer expired.

## [◆ ](#a7265cbba4972503c1c30a2e52a929874)SIGXCPU

| #define SIGXCPU   24 |
| --- |

CPU time limit exceeded.

## [◆ ](#a75440a7aa885a1052dfd3b4393fd9baa)SIGXFSZ

| #define SIGXFSZ   25 |
| --- |

File size limit exceeded.

## Typedef Documentation

## [◆ ](#a5d486213aa4f744f497959af6917e2a0)sig\_atomic\_t

| typedef int [sig\_atomic\_t](#a5d486213aa4f744f497959af6917e2a0) |
| --- |

## Function Documentation

## [◆ ](#a16972ede9065cb2709fcfc6a84272116)pthread\_sigmask()

| int pthread\_sigmask | ( | int | *how*, |
| --- | --- | --- | --- |
|  |  | const [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *set*, |
|  |  | [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *oset* ) |

## [◆ ](#acab58ba1dfe2108f96d9f28e249a8c7d)sigaddset()

| int sigaddset | ( | [sigset\_t](structsigset__t.md) \* | *set*, |
| --- | --- | --- | --- |
|  |  | int | *signo* ) |

## [◆ ](#ac3471f7a860cdfb70afe89a90a074c69)sigdelset()

| int sigdelset | ( | [sigset\_t](structsigset__t.md) \* | *set*, |
| --- | --- | --- | --- |
|  |  | int | *signo* ) |

## [◆ ](#a5925352f90eb589393274fa0376d7def)sigemptyset()

| int sigemptyset | ( | [sigset\_t](structsigset__t.md) \* | *set* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a88d7bbc77ea1569ee21c90db549ea023)sigfillset()

| int sigfillset | ( | [sigset\_t](structsigset__t.md) \* | *set* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a2bd11ded490df632440aa08f320aad17)sigismember()

| int sigismember | ( | const [sigset\_t](structsigset__t.md) \* | *set*, |
| --- | --- | --- | --- |
|  |  | int | *signo* ) |

## [◆ ](#a6e6b04897703c43b2ad10013041ad152)sigprocmask()

| int sigprocmask | ( | int | *how*, |
| --- | --- | --- | --- |
|  |  | const [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *set*, |
|  |  | [sigset\_t](structsigset__t.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *oset* ) |

## [◆ ](#a8b856eee87a225f697f1b264ebd6a47b)strsignal()

| char \* strsignal | ( | int | *signum* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [signal.h](include_2zephyr_2posix_2signal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
