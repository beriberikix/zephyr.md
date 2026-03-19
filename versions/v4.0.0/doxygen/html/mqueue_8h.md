---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mqueue_8h.html
original_path: doxygen/html/mqueue_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqueue.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/posix/time.h](include_2zephyr_2posix_2time_8h_source.md)>`  
`#include <[zephyr/posix/fcntl.h](fcntl_8h_source.md)>`  
`#include <[zephyr/posix/signal.h](include_2zephyr_2posix_2signal_8h_source.md)>`  
`#include <[zephyr/posix/sys/stat.h](stat_8h_source.md)>`  
`#include <[zephyr/posix/posix_types.h](posix__types_8h_source.md)>`

[Go to the source code of this file.](mqueue_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mq\_attr](structmq__attr.md) |

| Typedefs | |
| --- | --- |
| typedef void \* | [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) |

| Functions | |
| --- | --- |
| [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) | [mq\_open](#a6e6c4881ac0fd3ad18d733b96d088b8b) (const char \*name, int oflags,...) |
| int | [mq\_close](#a3fbd3906296be63451c64d69be2bc371) ([mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) mqdes) |
| int | [mq\_unlink](#accd8c5ee36e60d990963e1d544ef4140) (const char \*name) |
| int | [mq\_getattr](#a5a55ce03d8466a53a36601aaca9ee328) ([mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) mqdes, struct [mq\_attr](structmq__attr.md) \*mqstat) |
| int | [mq\_receive](#ae0ff0175064ab31858eff0669b7e745b) ([mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) mqdes, char \*msg\_ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_len, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \*msg\_prio) |
| int | [mq\_send](#af13b6f0b3b15e14624b0c50050d062a4) ([mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) mqdes, const char \*msg\_ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_len, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int msg\_prio) |
| int | [mq\_setattr](#a83b7aa93cb6f1f5a4fd938baea5579a6) ([mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) mqdes, const struct [mq\_attr](structmq__attr.md) \*mqstat, struct [mq\_attr](structmq__attr.md) \*omqstat) |
| int | [mq\_timedreceive](#aaf2e88ac75eac32eb5a3672fd56759b7) ([mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) mqdes, char \*msg\_ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_len, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \*msg\_prio, const struct [timespec](structtimespec.md) \*abstime) |
| int | [mq\_timedsend](#ac19939c8157d7ef9033a5be97a7ca6a1) ([mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) mqdes, const char \*msg\_ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_len, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int msg\_prio, const struct [timespec](structtimespec.md) \*abstime) |
| int | [mq\_notify](#a5eadbb82e0b9702d77f384a27827b334) ([mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) mqdes, const struct [sigevent](structsigevent.md) \*notification) |

## Typedef Documentation

## [◆ ](#aa03ac56b19aba70879b7e2934da6a507)mqd\_t

| typedef void\* [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) |
| --- |

## Function Documentation

## [◆ ](#a3fbd3906296be63451c64d69be2bc371)mq\_close()

| int mq\_close | ( | [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) | *mqdes* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5a55ce03d8466a53a36601aaca9ee328)mq\_getattr()

| int mq\_getattr | ( | [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) | *mqdes*, |
| --- | --- | --- | --- |
|  |  | struct [mq\_attr](structmq__attr.md) \* | *mqstat* ) |

## [◆ ](#a5eadbb82e0b9702d77f384a27827b334)mq\_notify()

| int mq\_notify | ( | [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) | *mqdes*, |
| --- | --- | --- | --- |
|  |  | const struct [sigevent](structsigevent.md) \* | *notification* ) |

## [◆ ](#a6e6c4881ac0fd3ad18d733b96d088b8b)mq\_open()

| [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) mq\_open | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | int | *oflags*, |
|  |  |  | *...* ) |

## [◆ ](#ae0ff0175064ab31858eff0669b7e745b)mq\_receive()

| int mq\_receive | ( | [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) | *mqdes*, |
| --- | --- | --- | --- |
|  |  | char \* | *msg\_ptr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *msg\_len*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \* | *msg\_prio* ) |

## [◆ ](#af13b6f0b3b15e14624b0c50050d062a4)mq\_send()

| int mq\_send | ( | [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) | *mqdes*, |
| --- | --- | --- | --- |
|  |  | const char \* | *msg\_ptr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *msg\_len*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *msg\_prio* ) |

## [◆ ](#a83b7aa93cb6f1f5a4fd938baea5579a6)mq\_setattr()

| int mq\_setattr | ( | [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) | *mqdes*, |
| --- | --- | --- | --- |
|  |  | const struct [mq\_attr](structmq__attr.md) \* | *mqstat*, |
|  |  | struct [mq\_attr](structmq__attr.md) \* | *omqstat* ) |

## [◆ ](#aaf2e88ac75eac32eb5a3672fd56759b7)mq\_timedreceive()

| int mq\_timedreceive | ( | [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) | *mqdes*, |
| --- | --- | --- | --- |
|  |  | char \* | *msg\_ptr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *msg\_len*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \* | *msg\_prio*, |
|  |  | const struct [timespec](structtimespec.md) \* | *abstime* ) |

## [◆ ](#ac19939c8157d7ef9033a5be97a7ca6a1)mq\_timedsend()

| int mq\_timedsend | ( | [mqd\_t](#aa03ac56b19aba70879b7e2934da6a507) | *mqdes*, |
| --- | --- | --- | --- |
|  |  | const char \* | *msg\_ptr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *msg\_len*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *msg\_prio*, |
|  |  | const struct [timespec](structtimespec.md) \* | *abstime* ) |

## [◆ ](#accd8c5ee36e60d990963e1d544ef4140)mq\_unlink()

| int mq\_unlink | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [mqueue.h](mqueue_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
