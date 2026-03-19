---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/string_8h.html
original_path: doxygen/html/string_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

string.h File Reference

`#include <stddef.h>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](string_8h_source.md)

| Functions | |
| --- | --- |
| char \* | [strcpy](#a6d729a7b6396b8508060821c56f4adbc) (char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), const char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| char \* | [strerror](#a4bc5f273980fb0e81e0fc7a4dd3de87e) (int errnum) |
| int | [strerror\_r](#a080c6052ea267026d0baa316f8610b46) (int errnum, char \*strerrbuf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen) |
| char \* | [strncpy](#aa7003ae2e637e6eb92a4c5e7523848a5) (char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), const char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
| char \* | [strchr](#ad7c16a2447154107d5ecd28434993443) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), int c) |
| char \* | [strrchr](#af87bb1cdc3d71abcd9aa0bd6d36e50a8) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), int c) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [strlen](#aa383452fe445bfae989358c9d7d96f4f) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [strnlen](#afc92d2231e45d19988c7894aa2a07f0c) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) maxlen) |
| int | [strcmp](#a11bd144d7d44914099a3aeddf1c8567d) (const char \*s1, const char \*s2) |
| int | [strncmp](#a07f4a84c11c106e95c32b6ab509346ef) (const char \*s1, const char \*s2, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
| char \* | [strtok\_r](#a22af6fcfed68749460181f2077c34813) (char \*str, const char \*sep, char \*\*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| char \* | [strcat](#a85c0f130f91a3121ee06207f42554572) (char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) dest, const char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) src) |
| char \* | [strncat](#a32dff100d3a0806b158b13bbe60710af) (char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) dest, const char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
| char \* | [strstr](#adef2d6284e392701fd4149b344188ceb) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), const char \*find) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [strspn](#a900a0edfa51f601d479244f7451cedd1) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), const char \*[accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [strcspn](#aeb6c449e5d77477c057abf00eaaf88fe) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), const char \*reject) |
| int | [memcmp](#ad8bfbfa1e4ad284ded921dd775735521) (const void \*m1, const void \*m2, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
| void \* | [memmove](#a71a1afb093b0af8298df8a745b1b1f5c) (void \*[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), const void \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
| void \* | [memcpy](#af0f01bffcd16daa9143f6014d10a25ad) (void \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), const void \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
| void \* | [memset](#a4137694174d4ca2fad886a1db355015c) (void \*buf, int c, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
| void \* | [memchr](#a0a3e4af1b88f5d51a32fe7dcbf753b38) (const void \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), int c, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |

## Function Documentation

## [◆ ](#a0a3e4af1b88f5d51a32fe7dcbf753b38)memchr()

| | void \* memchr | ( | const void \* | *s*, | | --- | --- | --- | --- | |  |  | int | *c*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad8bfbfa1e4ad284ded921dd775735521)memcmp()

| | int memcmp | ( | const void \* | *m1*, | | --- | --- | --- | --- | |  |  | const void \* | *m2*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af0f01bffcd16daa9143f6014d10a25ad)memcpy()

| | void \* memcpy | ( | void \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *d*, | | --- | --- | --- | --- | |  |  | const void \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *s*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a71a1afb093b0af8298df8a745b1b1f5c)memmove()

| | void \* memmove | ( | void \* | *d*, | | --- | --- | --- | --- | |  |  | const void \* | *s*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4137694174d4ca2fad886a1db355015c)memset()

| | void \* memset | ( | void \* | *buf*, | | --- | --- | --- | --- | |  |  | int | *c*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a85c0f130f91a3121ee06207f42554572)strcat()

| | char \* strcat | ( | char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *dest*, | | --- | --- | --- | --- | |  |  | const char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *src* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad7c16a2447154107d5ecd28434993443)strchr()

| | char \* strchr | ( | const char \* | *s*, | | --- | --- | --- | --- | |  |  | int | *c* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a11bd144d7d44914099a3aeddf1c8567d)strcmp()

| | int strcmp | ( | const char \* | *s1*, | | --- | --- | --- | --- | |  |  | const char \* | *s2* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a6d729a7b6396b8508060821c56f4adbc)strcpy()

| | char \* strcpy | ( | char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *d*, | | --- | --- | --- | --- | |  |  | const char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *s* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aeb6c449e5d77477c057abf00eaaf88fe)strcspn()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) strcspn | ( | const char \* | *s*, | | --- | --- | --- | --- | |  |  | const char \* | *reject* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4bc5f273980fb0e81e0fc7a4dd3de87e)strerror()

| | char \* strerror | ( | int | *errnum* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a080c6052ea267026d0baa316f8610b46)strerror\_r()

| | int strerror\_r | ( | int | *errnum*, | | --- | --- | --- | --- | |  |  | char \* | *strerrbuf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buflen* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa383452fe445bfae989358c9d7d96f4f)strlen()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) strlen | ( | const char \* | *s* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a32dff100d3a0806b158b13bbe60710af)strncat()

| | char \* strncat | ( | char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *dest*, | | --- | --- | --- | --- | |  |  | const char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *src*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a07f4a84c11c106e95c32b6ab509346ef)strncmp()

| | int strncmp | ( | const char \* | *s1*, | | --- | --- | --- | --- | |  |  | const char \* | *s2*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa7003ae2e637e6eb92a4c5e7523848a5)strncpy()

| | char \* strncpy | ( | char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *d*, | | --- | --- | --- | --- | |  |  | const char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *s*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#afc92d2231e45d19988c7894aa2a07f0c)strnlen()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) strnlen | ( | const char \* | *s*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *maxlen* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af87bb1cdc3d71abcd9aa0bd6d36e50a8)strrchr()

| | char \* strrchr | ( | const char \* | *s*, | | --- | --- | --- | --- | |  |  | int | *c* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a900a0edfa51f601d479244f7451cedd1)strspn()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) strspn | ( | const char \* | *s*, | | --- | --- | --- | --- | |  |  | const char \* | *accept* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adef2d6284e392701fd4149b344188ceb)strstr()

| | char \* strstr | ( | const char \* | *s*, | | --- | --- | --- | --- | |  |  | const char \* | *find* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a22af6fcfed68749460181f2077c34813)strtok\_r()

| | char \* strtok\_r | ( | char \* | *str*, | | --- | --- | --- | --- | |  |  | const char \* | *sep*, | |  |  | char \*\* | *state* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [string.h](string_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
