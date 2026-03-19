---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fdtable_8h.html
original_path: doxygen/html/fdtable_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fdtable.h File Reference

`#include <stdarg.h>`  
`#include <time.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <zephyr/syscalls/fdtable.h>`

[Go to the source code of this file.](fdtable_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [fd\_op\_vtable](structfd__op__vtable.md) |
|  | File descriptor virtual method table. [More...](structfd__op__vtable.md#details) |
| struct | [zvfs\_pollfd](structzvfs__pollfd.md) |
| struct | [zvfs\_fd\_set](structzvfs__fd__set.md) |

| Macros | |
| --- | --- |
| #define | [ZVFS\_MODE\_IFMT](#a1a7eb223a64cc8df1d236ad9d4373c04)   0170000 |
| #define | [ZVFS\_MODE\_UNSPEC](#a4696b5a4cecb531946d2f5b2ecd8b8ff)   0000000 |
| #define | [ZVFS\_MODE\_IFIFO](#a6af8ed654a6cc5e0b21b2374ab56d4ae)   0010000 |
| #define | [ZVFS\_MODE\_IFCHR](#a02b35555e5ea7d2a577daa2b14ca7c6b)   0020000 |
| #define | [ZVFS\_MODE\_IMSGQ](#a2bdc08321b707a710c4fc3f755638954)   0030000 |
| #define | [ZVFS\_MODE\_IFDIR](#a44cd1a7ec98550ba895b0906ffbcb52d)   0040000 |
| #define | [ZVFS\_MODE\_IFSEM](#a22ed252f154ab0a11edfedd2c1468647)   0050000 |
| #define | [ZVFS\_MODE\_IFBLK](#a0da8fae58fe76c88d5701e5c0683da91)   0060000 |
| #define | [ZVFS\_MODE\_IFSHM](#aa6c681e545a9ab1644c47d83d375697c)   0070000 |
| #define | [ZVFS\_MODE\_IFREG](#ad0bb04c7688eb917fa06939f277cc8c0)   0100000 |
| #define | [ZVFS\_MODE\_IFLNK](#a66443b8d46b4f32cf1a17a3d0a0a1486)   0120000 |
| #define | [ZVFS\_MODE\_IFSOCK](#a2b0c1987c6ab087dd6cd91e7af2fb883)   0140000 |
| #define | [ZVFS\_POLLIN](#abacd664acb7f265a70011864e7ba9b0f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ZVFS\_POLLPRI](#adf798c33fb9da067a17ffd68514791af)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ZVFS\_POLLOUT](#ac1938ed509009a549d0eee1c8a9ffe80)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [ZVFS\_POLLERR](#acddab9e57408c2b5800c60be120f1101)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [ZVFS\_POLLHUP](#a510aeed3c8541e8f48db1c3241c85aab)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [ZVFS\_POLLNVAL](#a25568088715f7eacbd673a896f38caf2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [ZVFS\_FD\_SETSIZE](#ae8d10dc8bd02e619f8c384c493f53709)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(((struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*)0)->bitset) \* 8) |
|  | Number of file descriptors which can be added [zvfs\_fd\_set](structzvfs__fd__set.md "zvfs_fd_set"). |

| Enumerations | |
| --- | --- |
| enum | {     [ZFD\_IOCTL\_FSYNC](#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4) = 0x100 , [ZFD\_IOCTL\_LSEEK](#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072) , [ZFD\_IOCTL\_POLL\_PREPARE](#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e) , [ZFD\_IOCTL\_POLL\_UPDATE](#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa) ,     [ZFD\_IOCTL\_POLL\_OFFLOAD](#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe) , [ZFD\_IOCTL\_SET\_LOCK](#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62) , [ZFD\_IOCTL\_STAT](#aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c) , [ZFD\_IOCTL\_TRUNCATE](#aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5) ,     [ZFD\_IOCTL\_MMAP](#aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f) , [ZFD\_IOCTL\_FIONREAD](#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) = 0x541B , [ZFD\_IOCTL\_FIONBIO](#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) = 0x5421   } |
|  | Request codes for [fd\_op\_vtable.ioctl()](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298). [More...](#aac8cb8bde69d227a7a8e9edf2980bd20) |

| Functions | |
| --- | --- |
| int | [zvfs\_reserve\_fd](#a0805f751464ff9a51a463841ce35ff5f) (void) |
|  | Reserve file descriptor. |
| void | [zvfs\_finalize\_typed\_fd](#a448172e130af96c11af2fe6511e6b262) (int fd, void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode) |
|  | Finalize creation of file descriptor, with type. |
| static void | [zvfs\_finalize\_fd](#a0bb7c530d69c9e5b1cfc61e7a11441af) (int fd, void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable) |
|  | Finalize creation of file descriptor. |
| int | [zvfs\_alloc\_fd](#a0248f37e9b8cfc0a76ced956b75a3ed2) (void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable) |
|  | Allocate file descriptor for underlying I/O object. |
| void | [zvfs\_free\_fd](#a5cedc4a2f8375d103238d611f6ed3422) (int fd) |
|  | Release reserved file descriptor. |
| void \* | [zvfs\_get\_fd\_obj](#a8655ab5d3b0776f27eb67d53ef8a431b) (int fd, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, int err) |
|  | Get underlying object pointer from file descriptor. |
| void \* | [zvfs\_get\_fd\_obj\_and\_vtable](#a0b8c1eeb3ff253e45d45752b77679e17) (int fd, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*\*vtable, struct [k\_mutex](structk__mutex.md) \*\*lock) |
|  | Get underlying object pointer and vtable pointer from file descriptor. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [zvfs\_get\_obj\_lock\_and\_cond](#a54e1f1cbd983631903757a93997c3fab) (void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, struct [k\_mutex](structk__mutex.md) \*\*lock, struct [k\_condvar](structk__condvar.md) \*\*cond) |
|  | Get the mutex and condition variable associated with the given object and vtable. |
| static int | [zvfs\_fdtable\_call\_ioctl](#a78c25e35ddacd2d4287cc24acf4126cc) (const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, void \*obj, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long request,...) |
|  | Call ioctl vmethod on an object using varargs. |
| int | [zvfs\_poll](#a1a758fb84d99d0390b6a8d51ec7cda34) (struct [zvfs\_pollfd](structzvfs__pollfd.md) \*fds, int nfds, int poll\_timeout) |
| void | [ZVFS\_FD\_CLR](#a029809dfde96846d9e7871e252d74546) (int fd, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*fdset) |
| int | [ZVFS\_FD\_ISSET](#a84f63f19ea89e5711725f4d753b5484c) (int fd, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*fdset) |
| void | [ZVFS\_FD\_SET](#afa48d92e5f545412139f567a19e01f71) (int fd, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*fdset) |
| void | [ZVFS\_FD\_ZERO](#a46ae4a3ac3d192de02fb1b6c4a4e95ac) (struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*fdset) |
| int | [zvfs\_select](#a8ced1fc0adbdf35b71ec486a8ec68665) (int nfds, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) readfds, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) writefds, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) errorfds, const struct [timespec](structtimespec.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) timeout, const void \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) sigmask) |

## Macro Definition Documentation

## [◆ ](#ae8d10dc8bd02e619f8c384c493f53709)ZVFS\_FD\_SETSIZE

| #define ZVFS\_FD\_SETSIZE   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(((struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*)0)->bitset) \* 8) |
| --- |

Number of file descriptors which can be added [zvfs\_fd\_set](structzvfs__fd__set.md "zvfs_fd_set").

## [◆ ](#a0da8fae58fe76c88d5701e5c0683da91)ZVFS\_MODE\_IFBLK

| #define ZVFS\_MODE\_IFBLK   0060000 |
| --- |

## [◆ ](#a02b35555e5ea7d2a577daa2b14ca7c6b)ZVFS\_MODE\_IFCHR

| #define ZVFS\_MODE\_IFCHR   0020000 |
| --- |

## [◆ ](#a44cd1a7ec98550ba895b0906ffbcb52d)ZVFS\_MODE\_IFDIR

| #define ZVFS\_MODE\_IFDIR   0040000 |
| --- |

## [◆ ](#a6af8ed654a6cc5e0b21b2374ab56d4ae)ZVFS\_MODE\_IFIFO

| #define ZVFS\_MODE\_IFIFO   0010000 |
| --- |

## [◆ ](#a66443b8d46b4f32cf1a17a3d0a0a1486)ZVFS\_MODE\_IFLNK

| #define ZVFS\_MODE\_IFLNK   0120000 |
| --- |

## [◆ ](#a1a7eb223a64cc8df1d236ad9d4373c04)ZVFS\_MODE\_IFMT

| #define ZVFS\_MODE\_IFMT   0170000 |
| --- |

## [◆ ](#ad0bb04c7688eb917fa06939f277cc8c0)ZVFS\_MODE\_IFREG

| #define ZVFS\_MODE\_IFREG   0100000 |
| --- |

## [◆ ](#a22ed252f154ab0a11edfedd2c1468647)ZVFS\_MODE\_IFSEM

| #define ZVFS\_MODE\_IFSEM   0050000 |
| --- |

## [◆ ](#aa6c681e545a9ab1644c47d83d375697c)ZVFS\_MODE\_IFSHM

| #define ZVFS\_MODE\_IFSHM   0070000 |
| --- |

## [◆ ](#a2b0c1987c6ab087dd6cd91e7af2fb883)ZVFS\_MODE\_IFSOCK

| #define ZVFS\_MODE\_IFSOCK   0140000 |
| --- |

## [◆ ](#a2bdc08321b707a710c4fc3f755638954)ZVFS\_MODE\_IMSGQ

| #define ZVFS\_MODE\_IMSGQ   0030000 |
| --- |

## [◆ ](#a4696b5a4cecb531946d2f5b2ecd8b8ff)ZVFS\_MODE\_UNSPEC

| #define ZVFS\_MODE\_UNSPEC   0000000 |
| --- |

## [◆ ](#acddab9e57408c2b5800c60be120f1101)ZVFS\_POLLERR

| #define ZVFS\_POLLERR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a510aeed3c8541e8f48db1c3241c85aab)ZVFS\_POLLHUP

| #define ZVFS\_POLLHUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#abacd664acb7f265a70011864e7ba9b0f)ZVFS\_POLLIN

| #define ZVFS\_POLLIN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a25568088715f7eacbd673a896f38caf2)ZVFS\_POLLNVAL

| #define ZVFS\_POLLNVAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#ac1938ed509009a549d0eee1c8a9ffe80)ZVFS\_POLLOUT

| #define ZVFS\_POLLOUT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#adf798c33fb9da067a17ffd68514791af)ZVFS\_POLLPRI

| #define ZVFS\_POLLPRI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## Enumeration Type Documentation

## [◆ ](#aac8cb8bde69d227a7a8e9edf2980bd20)anonymous enum

| anonymous enum |
| --- |

Request codes for [fd\_op\_vtable.ioctl()](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298).

Note that these codes are internal Zephyr numbers, for internal Zephyr operations (and subject to change without notice, not part of "stable ABI"). These are however expected to co-exist with "well-known" POSIX/Linux ioctl numbers, and not clash with them.

| Enumerator | |
| --- | --- |
| ZFD\_IOCTL\_FSYNC |  |
| ZFD\_IOCTL\_LSEEK |  |
| ZFD\_IOCTL\_POLL\_PREPARE |  |
| ZFD\_IOCTL\_POLL\_UPDATE |  |
| ZFD\_IOCTL\_POLL\_OFFLOAD |  |
| ZFD\_IOCTL\_SET\_LOCK |  |
| ZFD\_IOCTL\_STAT |  |
| ZFD\_IOCTL\_TRUNCATE |  |
| ZFD\_IOCTL\_MMAP |  |
| ZFD\_IOCTL\_FIONREAD |  |
| ZFD\_IOCTL\_FIONBIO |  |

## Function Documentation

## [◆ ](#a0248f37e9b8cfc0a76ced956b75a3ed2)zvfs\_alloc\_fd()

| int zvfs\_alloc\_fd | ( | void \* | *obj*, |
| --- | --- | --- | --- |
|  |  | const struct [fd\_op\_vtable](structfd__op__vtable.md) \* | *vtable* ) |

Allocate file descriptor for underlying I/O object.

This function combines operations of [zvfs\_reserve\_fd()](#a0805f751464ff9a51a463841ce35ff5f) and [zvfs\_finalize\_fd()](#a0bb7c530d69c9e5b1cfc61e7a11441af) in one step, and provided for convenience.

Parameters
:   | obj | pointer to I/O object structure |
    | --- | --- |
    | vtable | pointer to I/O operation implementations for the object |

Returns
:   Allocated file descriptor, or -1 in case of error (errno is set)

## [◆ ](#a029809dfde96846d9e7871e252d74546)ZVFS\_FD\_CLR()

| void ZVFS\_FD\_CLR | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | struct [zvfs\_fd\_set](structzvfs__fd__set.md) \* | *fdset* ) |

## [◆ ](#a84f63f19ea89e5711725f4d753b5484c)ZVFS\_FD\_ISSET()

| int ZVFS\_FD\_ISSET | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | struct [zvfs\_fd\_set](structzvfs__fd__set.md) \* | *fdset* ) |

## [◆ ](#afa48d92e5f545412139f567a19e01f71)ZVFS\_FD\_SET()

| void ZVFS\_FD\_SET | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | struct [zvfs\_fd\_set](structzvfs__fd__set.md) \* | *fdset* ) |

## [◆ ](#a46ae4a3ac3d192de02fb1b6c4a4e95ac)ZVFS\_FD\_ZERO()

| void ZVFS\_FD\_ZERO | ( | struct [zvfs\_fd\_set](structzvfs__fd__set.md) \* | *fdset* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a78c25e35ddacd2d4287cc24acf4126cc)zvfs\_fdtable\_call\_ioctl()

| | int zvfs\_fdtable\_call\_ioctl | ( | const struct [fd\_op\_vtable](structfd__op__vtable.md) \* | *vtable*, | | --- | --- | --- | --- | |  |  | void \* | *obj*, | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *request*, | |  |  |  | *...* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Call ioctl vmethod on an object using varargs.

We need this helper function because ioctl vmethod is declared to take va\_list and the only portable way to construct va\_list is from function's ... parameters.

Parameters
:   | vtable | vtable containing ioctl function pointer |
    | --- | --- |
    | obj | Object to call ioctl on |
    | request | ioctl request number |
    | ... | Variadic arguments to ioctl |

## [◆ ](#a0bb7c530d69c9e5b1cfc61e7a11441af)zvfs\_finalize\_fd()

| | void zvfs\_finalize\_fd | ( | int | *fd*, | | --- | --- | --- | --- | |  |  | void \* | *obj*, | |  |  | const struct [fd\_op\_vtable](structfd__op__vtable.md) \* | *vtable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Finalize creation of file descriptor.

This function should be called exactly once after [zvfs\_reserve\_fd()](#a0805f751464ff9a51a463841ce35ff5f), and should not be called in any other case.

Parameters
:   | fd | File descriptor previously returned by [zvfs\_reserve\_fd()](#a0805f751464ff9a51a463841ce35ff5f) |
    | --- | --- |
    | obj | pointer to I/O object structure |
    | vtable | pointer to I/O operation implementations for the object |

## [◆ ](#a448172e130af96c11af2fe6511e6b262)zvfs\_finalize\_typed\_fd()

| void zvfs\_finalize\_typed\_fd | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | void \* | *obj*, |
|  |  | const struct [fd\_op\_vtable](structfd__op__vtable.md) \* | *vtable*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mode* ) |

Finalize creation of file descriptor, with type.

This function should be called exactly once after [zvfs\_reserve\_fd()](#a0805f751464ff9a51a463841ce35ff5f), and should not be called in any other case.

The difference between this function and [zvfs\_finalize\_fd](#a0bb7c530d69c9e5b1cfc61e7a11441af) is that the latter does not relay type information of the created file descriptor.

Values permitted for *mode* are one of ZVFS\_MODE\_...

Parameters
:   | fd | File descriptor previously returned by [zvfs\_reserve\_fd()](#a0805f751464ff9a51a463841ce35ff5f) |
    | --- | --- |
    | obj | pointer to I/O object structure |
    | vtable | pointer to I/O operation implementations for the object |
    | mode | File type as specified above. |

## [◆ ](#a5cedc4a2f8375d103238d611f6ed3422)zvfs\_free\_fd()

| void zvfs\_free\_fd | ( | int | *fd* | ) |  |
| --- | --- | --- | --- | --- | --- |

Release reserved file descriptor.

This function may be called once after [zvfs\_reserve\_fd()](#a0805f751464ff9a51a463841ce35ff5f), and should not be called in any other case.

Parameters
:   | fd | File descriptor previously returned by [zvfs\_reserve\_fd()](#a0805f751464ff9a51a463841ce35ff5f) |
    | --- | --- |

## [◆ ](#a8655ab5d3b0776f27eb67d53ef8a431b)zvfs\_get\_fd\_obj()

| void \* zvfs\_get\_fd\_obj | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | const struct [fd\_op\_vtable](structfd__op__vtable.md) \* | *vtable*, |
|  |  | int | *err* ) |

Get underlying object pointer from file descriptor.

This function is useful for functions other than read/write/ioctl to look up underlying I/O object by fd, optionally checking its type (using vtable reference). If fd refers to invalid entry, NULL will be returned with errno set to EBADF. If fd is valid, but vtable param is not NULL and doesn't match object's vtable, NULL is returned and errno set to err param.

Parameters
:   | fd | File descriptor previously returned by [zvfs\_reserve\_fd()](#a0805f751464ff9a51a463841ce35ff5f) |
    | --- | --- |
    | vtable | Expected object vtable or NULL |
    | err | errno value to set if object vtable doesn't match |

Returns
:   Object pointer or NULL, with errno set

## [◆ ](#a0b8c1eeb3ff253e45d45752b77679e17)zvfs\_get\_fd\_obj\_and\_vtable()

| void \* zvfs\_get\_fd\_obj\_and\_vtable | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | const struct [fd\_op\_vtable](structfd__op__vtable.md) \*\* | *vtable*, |
|  |  | struct [k\_mutex](structk__mutex.md) \*\* | *lock* ) |

Get underlying object pointer and vtable pointer from file descriptor.

Parameters
:   | fd | File descriptor previously returned by [zvfs\_reserve\_fd()](#a0805f751464ff9a51a463841ce35ff5f) |
    | --- | --- |
    | vtable | A pointer to a pointer variable to store the vtable |
    | lock | An optional pointer to a pointer variable to store the mutex preventing concurrent descriptor access. The lock is not taken, it is just returned for the caller to use if necessary. Pass NULL if the lock is not needed by the caller. |

Returns
:   Object pointer or NULL, with errno set

## [◆ ](#a54e1f1cbd983631903757a93997c3fab)zvfs\_get\_obj\_lock\_and\_cond()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) zvfs\_get\_obj\_lock\_and\_cond | ( | void \* | *obj*, |
| --- | --- | --- | --- |
|  |  | const struct [fd\_op\_vtable](structfd__op__vtable.md) \* | *vtable*, |
|  |  | struct [k\_mutex](structk__mutex.md) \*\* | *lock*, |
|  |  | struct [k\_condvar](structk__condvar.md) \*\* | *cond* ) |

Get the mutex and condition variable associated with the given object and vtable.

Parameters
:   | obj | Object previously returned by a call to e.g. [zvfs\_get\_fd\_obj](#a8655ab5d3b0776f27eb67d53ef8a431b). |
    | --- | --- |
    | vtable | A pointer the vtable associated with `obj`. |
    | lock | An optional pointer to a pointer variable to store the mutex preventing concurrent descriptor access. The lock is not taken, it is just returned for the caller to use if necessary. Pass NULL if the lock is not needed by the caller. |
    | cond | An optional pointer to a pointer variable to store the condition variable to notify waiting threads in the case of concurrent descriptor access. Pass NULL if the condition variable is not needed by the caller. |

Returns
:   [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) on success, [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) otherwise.

## [◆ ](#a1a758fb84d99d0390b6a8d51ec7cda34)zvfs\_poll()

| int zvfs\_poll | ( | struct [zvfs\_pollfd](structzvfs__pollfd.md) \* | *fds*, |
| --- | --- | --- | --- |
|  |  | int | *nfds*, |
|  |  | int | *poll\_timeout* ) |

## [◆ ](#a0805f751464ff9a51a463841ce35ff5f)zvfs\_reserve\_fd()

| int zvfs\_reserve\_fd | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Reserve file descriptor.

This function allows to reserve a space for file descriptor entry in the underlying table, and thus allows caller to fail fast if no free descriptor is available. If this function succeeds, [zvfs\_finalize\_fd()](#a0bb7c530d69c9e5b1cfc61e7a11441af) or [zvfs\_free\_fd()](#a5cedc4a2f8375d103238d611f6ed3422) must be called mandatorily.

Returns
:   Allocated file descriptor, or -1 in case of error (errno is set)

## [◆ ](#a8ced1fc0adbdf35b71ec486a8ec68665)zvfs\_select()

| int zvfs\_select | ( | int | *nfds*, |
| --- | --- | --- | --- |
|  |  | struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *readfds*, |
|  |  | struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *writefds*, |
|  |  | struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *errorfds*, |
|  |  | const struct [timespec](structtimespec.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *timeout*, |
|  |  | const void \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *sigmask* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [fdtable.h](fdtable_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
