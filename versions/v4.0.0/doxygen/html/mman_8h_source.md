---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mman_8h_source.html
original_path: doxygen/html/mman_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mman.h

[Go to the documentation of this file.](mman_8h.md)

1/\*

2 \* Copyright (c) 2024, Tenstorrent AI ULC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_POSIX\_SYS\_MMAN\_H\_

8#define ZEPHYR\_INCLUDE\_ZEPHYR\_POSIX\_SYS\_MMAN\_H\_

9

10#include <stddef.h>

11#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

12

[ 13](mman_8h.md#a6a982b48b8d3eb8eccd17e0d54ee5379)#define PROT\_NONE 0x0

[ 14](mman_8h.md#a15bf68ce8b590838b3a5c0b639d8d519)#define PROT\_READ 0x1

[ 15](mman_8h.md#a2a79c8ceefb8fc25a940ae07a3d94429)#define PROT\_WRITE 0x2

[ 16](mman_8h.md#a77848f068638e916c72cd543f5ecb815)#define PROT\_EXEC 0x4

17

[ 18](mman_8h.md#a57028962c2a7c0c802ca6613492f2ef3)#define MAP\_SHARED 0x1

[ 19](mman_8h.md#a398ef47a991a44389aa9818c98a28d24)#define MAP\_PRIVATE 0x2

[ 20](mman_8h.md#a387ec707b30c5e78cf20a14517a63b96)#define MAP\_FIXED 0x4

21

22/\* for Linux compatibility \*/

[ 23](mman_8h.md#ae4f86bff73414c5fc08c058f957212f0)#define MAP\_ANONYMOUS 0x20

24

[ 25](mman_8h.md#aee74e153705852ce48dca911f1b94d72)#define MS\_SYNC 0x0

[ 26](mman_8h.md#a98930d8c4137a6cf3f9e21b2b7c84c24)#define MS\_ASYNC 0x1

[ 27](mman_8h.md#ad094236c94cb5fcfd6a663b646782bc8)#define MS\_INVALIDATE 0x2

28

[ 29](mman_8h.md#a8523dcf952f6ff059a3bed717e4f1296)#define MAP\_FAILED ((void \*)-1)

30

[ 31](mman_8h.md#a22408a60244fd4662ed07d8afd74f8d0)#define MCL\_CURRENT 0

[ 32](mman_8h.md#a403c070913f388ac8d97521f949533ae)#define MCL\_FUTURE 1

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 38](mman_8h.md#a49da9349d68e3ced27b73c1b2e88ebf3)int [mlock](mman_8h.md#a49da9349d68e3ced27b73c1b2e88ebf3)(const void \*addr, size\_t len);

[ 39](mman_8h.md#ad4697a198c5b65f462dc77e3699a4f03)int [mlockall](mman_8h.md#ad4697a198c5b65f462dc77e3699a4f03)(int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 40](mman_8h.md#ac2e7d057b16f0c959ffb39d8719eb1ed)void \*[mmap](mman_8h.md#ac2e7d057b16f0c959ffb39d8719eb1ed)(void \*addr, size\_t len, int prot, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), int fildes, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394));

[ 41](mman_8h.md#abef113c04cdf88b279b9d4204a63d448)int [msync](mman_8h.md#abef113c04cdf88b279b9d4204a63d448)(void \*addr, size\_t length, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 42](mman_8h.md#ad3cfd73f8180a1a364cb57dc909bcb69)int [munlock](mman_8h.md#ad3cfd73f8180a1a364cb57dc909bcb69)(const void \*addr, size\_t len);

[ 43](mman_8h.md#a03b30383879c5b943ac4d4f9077aeb66)int [munlockall](mman_8h.md#a03b30383879c5b943ac4d4f9077aeb66)(void);

[ 44](mman_8h.md#a01ff21bc70401bee9b80c350763087f7)int [munmap](mman_8h.md#a01ff21bc70401bee9b80c350763087f7)(void \*addr, size\_t len);

[ 45](mman_8h.md#a14d35ac0e791a20d8773bfa13c456c2b)int [shm\_open](mman_8h.md#a14d35ac0e791a20d8773bfa13c456c2b)(const char \*name, int oflag, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) mode);

[ 46](mman_8h.md#a4037e49e9537e24edd610bd1acf090da)int [shm\_unlink](mman_8h.md#a4037e49e9537e24edd610bd1acf090da)(const char \*name);

47

48#ifdef \_\_cplusplus

49}

50#endif

51

52#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_POSIX\_SYS\_MMAN\_H\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00)

unsigned int mode\_t

**Definition** types.h:14

[munmap](mman_8h.md#a01ff21bc70401bee9b80c350763087f7)

int munmap(void \*addr, size\_t len)

[munlockall](mman_8h.md#a03b30383879c5b943ac4d4f9077aeb66)

int munlockall(void)

[shm\_open](mman_8h.md#a14d35ac0e791a20d8773bfa13c456c2b)

int shm\_open(const char \*name, int oflag, mode\_t mode)

[shm\_unlink](mman_8h.md#a4037e49e9537e24edd610bd1acf090da)

int shm\_unlink(const char \*name)

[mlock](mman_8h.md#a49da9349d68e3ced27b73c1b2e88ebf3)

int mlock(const void \*addr, size\_t len)

[msync](mman_8h.md#abef113c04cdf88b279b9d4204a63d448)

int msync(void \*addr, size\_t length, int flags)

[mmap](mman_8h.md#ac2e7d057b16f0c959ffb39d8719eb1ed)

void \* mmap(void \*addr, size\_t len, int prot, int flags, int fildes, off\_t off)

[munlock](mman_8h.md#ad3cfd73f8180a1a364cb57dc909bcb69)

int munlock(const void \*addr, size\_t len)

[mlockall](mman_8h.md#ad4697a198c5b65f462dc77e3699a4f03)

int mlockall(int flags)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [mman.h](mman_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
