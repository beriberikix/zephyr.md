---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/parser__url_8h.html
original_path: doxygen/html/parser__url_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

parser\_url.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/net/http/parser_state.h](parser__state_8h_source.md)>`

[Go to the source code of this file.](parser__url_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [http\_parser\_url](structhttp__parser__url.md) |

| Enumerations | |
| --- | --- |
| enum | [http\_parser\_url\_fields](#a9ca1f91c2958091e2ac9e9b2f903d4eb) {     [UF\_SCHEMA](#a9ca1f91c2958091e2ac9e9b2f903d4ebab2b8b31b30d6bc897dde653f6cc9f06c) = 0 , [UF\_HOST](#a9ca1f91c2958091e2ac9e9b2f903d4ebaf2aeb0b896645bd8100ca0f1e263a12f) = 1 , [UF\_PORT](#a9ca1f91c2958091e2ac9e9b2f903d4eba357b6dc1326ed55be377b0d839e8ca0f) = 2 , [UF\_PATH](#a9ca1f91c2958091e2ac9e9b2f903d4eba86b9abfa220db7b834490d8b36e915af) = 3 ,     [UF\_QUERY](#a9ca1f91c2958091e2ac9e9b2f903d4ebabc8500a49ccad1cd91d66d1eefb503cc) = 4 , [UF\_FRAGMENT](#a9ca1f91c2958091e2ac9e9b2f903d4eba32fb35461b96b6872f1427b2d51d1c30) = 5 , [UF\_USERINFO](#a9ca1f91c2958091e2ac9e9b2f903d4ebacb4a85c6a7d6cd0b64ec6e91e7ba8689) = 6 , [UF\_MAX](#a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd) = 7   } |

| Functions | |
| --- | --- |
| enum [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | [parse\_url\_char](#a9f477f452dcabd0d22f4a96ce0bfda57) (enum [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), const char ch) |
| void | [http\_parser\_url\_init](#a64e907d36fbcc883033c6bbe5a78b1b3) (struct [http\_parser\_url](structhttp__parser__url.md) \*u) |
| int | [http\_parser\_parse\_url](#aeb269310a348fd68fd001b30b690fc83) (const char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen, int is\_connect, struct [http\_parser\_url](structhttp__parser__url.md) \*u) |

## Enumeration Type Documentation

## [◆ ](#a9ca1f91c2958091e2ac9e9b2f903d4eb)http\_parser\_url\_fields

| enum [http\_parser\_url\_fields](#a9ca1f91c2958091e2ac9e9b2f903d4eb) |
| --- |

| Enumerator | |
| --- | --- |
| UF\_SCHEMA |  |
| UF\_HOST |  |
| UF\_PORT |  |
| UF\_PATH |  |
| UF\_QUERY |  |
| UF\_FRAGMENT |  |
| UF\_USERINFO |  |
| UF\_MAX |  |

## Function Documentation

## [◆ ](#aeb269310a348fd68fd001b30b690fc83)http\_parser\_parse\_url()

| int http\_parser\_parse\_url | ( | const char \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buflen*, |
|  |  | int | *is\_connect*, |
|  |  | struct [http\_parser\_url](structhttp__parser__url.md) \* | *u* ) |

## [◆ ](#a64e907d36fbcc883033c6bbe5a78b1b3)http\_parser\_url\_init()

| void http\_parser\_url\_init | ( | struct [http\_parser\_url](structhttp__parser__url.md) \* | *u* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a9f477f452dcabd0d22f4a96ce0bfda57)parse\_url\_char()

| enum [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) parse\_url\_char | ( | enum [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | *s*, |
| --- | --- | --- | --- |
|  |  | const char | *ch* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [parser\_url.h](parser__url_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
