---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/string_8h_source.html
original_path: doxygen/html/string_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

string.h

[Go to the documentation of this file.](string_8h.md)

1/\* string.h \*/

2

3/\*

4 \* Copyright (c) 2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STRING\_H\_

10#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STRING\_H\_

11

12#include <stddef.h>

13#include <[zephyr/toolchain.h](toolchain_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 19](string_8h.md#a6d729a7b6396b8508060821c56f4adbc)extern char \*[strcpy](string_8h.md#a6d729a7b6396b8508060821c56f4adbc)(char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

[ 20](string_8h.md#a4bc5f273980fb0e81e0fc7a4dd3de87e)extern char \*[strerror](string_8h.md#a4bc5f273980fb0e81e0fc7a4dd3de87e)(int errnum);

[ 21](string_8h.md#a080c6052ea267026d0baa316f8610b46)extern int [strerror\_r](string_8h.md#a080c6052ea267026d0baa316f8610b46)(int errnum, char \*strerrbuf, size\_t buflen);

[ 22](string_8h.md#aa7003ae2e637e6eb92a4c5e7523848a5)extern char \*[strncpy](string_8h.md#aa7003ae2e637e6eb92a4c5e7523848a5)(char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d),

23 size\_t n);

[ 24](string_8h.md#ad7c16a2447154107d5ecd28434993443)extern char \*[strchr](string_8h.md#ad7c16a2447154107d5ecd28434993443)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), int c);

[ 25](string_8h.md#af87bb1cdc3d71abcd9aa0bd6d36e50a8)extern char \*[strrchr](string_8h.md#af87bb1cdc3d71abcd9aa0bd6d36e50a8)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), int c);

[ 26](string_8h.md#aa383452fe445bfae989358c9d7d96f4f)extern size\_t [strlen](string_8h.md#aa383452fe445bfae989358c9d7d96f4f)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

[ 27](string_8h.md#afc92d2231e45d19988c7894aa2a07f0c)extern size\_t [strnlen](string_8h.md#afc92d2231e45d19988c7894aa2a07f0c)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), size\_t maxlen);

[ 28](string_8h.md#a11bd144d7d44914099a3aeddf1c8567d)extern int [strcmp](string_8h.md#a11bd144d7d44914099a3aeddf1c8567d)(const char \*s1, const char \*s2);

[ 29](string_8h.md#a07f4a84c11c106e95c32b6ab509346ef)extern int [strncmp](string_8h.md#a07f4a84c11c106e95c32b6ab509346ef)(const char \*s1, const char \*s2, size\_t n);

[ 30](string_8h.md#a22af6fcfed68749460181f2077c34813)extern char \*[strtok\_r](string_8h.md#a22af6fcfed68749460181f2077c34813)(char \*str, const char \*sep, char \*\*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

[ 31](string_8h.md#a85c0f130f91a3121ee06207f42554572)extern char \*[strcat](string_8h.md#a85c0f130f91a3121ee06207f42554572)(char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) dest,

32 const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) src);

[ 33](string_8h.md#a32dff100d3a0806b158b13bbe60710af)extern char \*[strncat](string_8h.md#a32dff100d3a0806b158b13bbe60710af)(char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) dest, const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) src,

34 size\_t n);

[ 35](string_8h.md#adef2d6284e392701fd4149b344188ceb)extern char \*[strstr](string_8h.md#adef2d6284e392701fd4149b344188ceb)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), const char \*find);

36

[ 37](string_8h.md#a900a0edfa51f601d479244f7451cedd1)extern size\_t [strspn](string_8h.md#a900a0edfa51f601d479244f7451cedd1)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), const char \*[accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb));

[ 38](string_8h.md#aeb6c449e5d77477c057abf00eaaf88fe)extern size\_t [strcspn](string_8h.md#aeb6c449e5d77477c057abf00eaaf88fe)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), const char \*reject);

39

[ 40](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)extern int [memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(const void \*m1, const void \*m2, size\_t n);

[ 41](string_8h.md#a71a1afb093b0af8298df8a745b1b1f5c)extern void \*[memmove](string_8h.md#a71a1afb093b0af8298df8a745b1b1f5c)(void \*[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), const void \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), size\_t n);

[ 42](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)extern void \*[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(void \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), const void \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d),

43 size\_t n);

[ 44](string_8h.md#a4137694174d4ca2fad886a1db355015c)extern void \*[memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(void \*buf, int c, size\_t n);

[ 45](string_8h.md#a0a3e4af1b88f5d51a32fe7dcbf753b38)extern void \*[memchr](string_8h.md#a0a3e4af1b88f5d51a32fe7dcbf753b38)(const void \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), int c, size\_t n);

46

47#ifdef \_\_cplusplus

48}

49#endif

50

51#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STRING\_H\_ \*/

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)

static int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_accept.

**Definition** socket.h:910

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[strncmp](string_8h.md#a07f4a84c11c106e95c32b6ab509346ef)

int strncmp(const char \*s1, const char \*s2, size\_t n)

[strerror\_r](string_8h.md#a080c6052ea267026d0baa316f8610b46)

int strerror\_r(int errnum, char \*strerrbuf, size\_t buflen)

[memchr](string_8h.md#a0a3e4af1b88f5d51a32fe7dcbf753b38)

void \* memchr(const void \*s, int c, size\_t n)

[strcmp](string_8h.md#a11bd144d7d44914099a3aeddf1c8567d)

int strcmp(const char \*s1, const char \*s2)

[strtok\_r](string_8h.md#a22af6fcfed68749460181f2077c34813)

char \* strtok\_r(char \*str, const char \*sep, char \*\*state)

[strncat](string_8h.md#a32dff100d3a0806b158b13bbe60710af)

char \* strncat(char \*ZRESTRICT dest, const char \*ZRESTRICT src, size\_t n)

[memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)

void \* memset(void \*buf, int c, size\_t n)

[strerror](string_8h.md#a4bc5f273980fb0e81e0fc7a4dd3de87e)

char \* strerror(int errnum)

[strcpy](string_8h.md#a6d729a7b6396b8508060821c56f4adbc)

char \* strcpy(char \*ZRESTRICT d, const char \*ZRESTRICT s)

[memmove](string_8h.md#a71a1afb093b0af8298df8a745b1b1f5c)

void \* memmove(void \*d, const void \*s, size\_t n)

[strcat](string_8h.md#a85c0f130f91a3121ee06207f42554572)

char \* strcat(char \*ZRESTRICT dest, const char \*ZRESTRICT src)

[strspn](string_8h.md#a900a0edfa51f601d479244f7451cedd1)

size\_t strspn(const char \*s, const char \*accept)

[strlen](string_8h.md#aa383452fe445bfae989358c9d7d96f4f)

size\_t strlen(const char \*s)

[strncpy](string_8h.md#aa7003ae2e637e6eb92a4c5e7523848a5)

char \* strncpy(char \*ZRESTRICT d, const char \*ZRESTRICT s, size\_t n)

[strchr](string_8h.md#ad7c16a2447154107d5ecd28434993443)

char \* strchr(const char \*s, int c)

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

[strstr](string_8h.md#adef2d6284e392701fd4149b344188ceb)

char \* strstr(const char \*s, const char \*find)

[strcspn](string_8h.md#aeb6c449e5d77477c057abf00eaaf88fe)

size\_t strcspn(const char \*s, const char \*reject)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[strrchr](string_8h.md#af87bb1cdc3d71abcd9aa0bd6d36e50a8)

char \* strrchr(const char \*s, int c)

[strnlen](string_8h.md#afc92d2231e45d19988c7894aa2a07f0c)

size\_t strnlen(const char \*s, size\_t maxlen)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [string.h](string_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
