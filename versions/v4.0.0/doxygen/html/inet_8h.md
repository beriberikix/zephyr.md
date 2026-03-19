---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/inet_8h.html
original_path: doxygen/html/inet_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

inet.h File Reference

`#include <stddef.h>`  
`#include <[zephyr/posix/netinet/in.h](in_8h_source.md)>`  
`#include <[zephyr/posix/sys/socket.h](posix_2sys_2socket_8h_source.md)>`  
`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](inet_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [in\_addr\_t](#a98b38134a62f24554da0ffcabde8062c) |

| Functions | |
| --- | --- |
| [in\_addr\_t](#a98b38134a62f24554da0ffcabde8062c) | [inet\_addr](#a3e3b8f43e05dc3b87977b6a7a2ed09ca) (const char \*cp) |
| char \* | [inet\_ntoa](#ab1d195e3682f88d1cea726e8c1de08d2) (struct [in\_addr](structin__addr.md) in) |
| char \* | [inet\_ntop](#ae93e32740fb355baef0cab02133e7ff4) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src, char \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| int | [inet\_pton](#aabfaede889b4bc47241ab0c49a7a3cab) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst) |

## Typedef Documentation

## [◆ ](#a98b38134a62f24554da0ffcabde8062c)in\_addr\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [in\_addr\_t](#a98b38134a62f24554da0ffcabde8062c) |
| --- |

## Function Documentation

## [◆ ](#a3e3b8f43e05dc3b87977b6a7a2ed09ca)inet\_addr()

| [in\_addr\_t](#a98b38134a62f24554da0ffcabde8062c) inet\_addr | ( | const char \* | *cp* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ab1d195e3682f88d1cea726e8c1de08d2)inet\_ntoa()

| char \* inet\_ntoa | ( | struct [in\_addr](structin__addr.md) | *in* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae93e32740fb355baef0cab02133e7ff4)inet\_ntop()

| char \* inet\_ntop | ( | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, |
| --- | --- | --- | --- |
|  |  | const void \* | *src*, |
|  |  | char \* | *dst*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

## [◆ ](#aabfaede889b4bc47241ab0c49a7a3cab)inet\_pton()

| int inet\_pton | ( | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, |
| --- | --- | --- | --- |
|  |  | const char \* | *src*, |
|  |  | void \* | *dst* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [arpa](dir_600f14fff2b86b8fd0090e7f273e0e80.md)
- [inet.h](inet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
