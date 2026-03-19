---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__frontend_8h_source.html
original_path: doxygen/html/log__frontend_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend.h

[Go to the documentation of this file.](log__frontend_8h.md)

1/\*

2 \* Copyright (c) 2019 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef LOG\_FRONTEND\_H\_

7#define LOG\_FRONTEND\_H\_

8

9#include <[zephyr/logging/log\_core.h](log__core_8h.md)>

10

[ 13](log__frontend_8h.md#a10b0e6f2dd38be09465b6356586f6745)void [log\_frontend\_init](log__frontend_8h.md#a10b0e6f2dd38be09465b6356586f6745)(void);

14

[ 31](log__frontend_8h.md#a81d90e2daca1f6c16f948c6a725803ba)void [log\_frontend\_msg](log__frontend_8h.md#a81d90e2daca1f6c16f948c6a725803ba)(const void \*source,

32 const struct [log\_msg\_desc](structlog__msg__desc.md) desc,

33 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*package, const void \*data);

34

[ 47](log__frontend_8h.md#a19e07719a21e8d2138d8e5932b1e7c68)void [log\_frontend\_simple\_0](log__frontend_8h.md#a19e07719a21e8d2138d8e5932b1e7c68)(const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level, const char \*fmt);

48

[ 62](log__frontend_8h.md#a6a4875ae710dc7e14c93b9225d2496d2)void [log\_frontend\_simple\_1](log__frontend_8h.md#a6a4875ae710dc7e14c93b9225d2496d2)(const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level, const char \*fmt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg);

63

[ 78](log__frontend_8h.md#a13ea68c36a760c2da64d164d8b79c1db)void [log\_frontend\_simple\_2](log__frontend_8h.md#a13ea68c36a760c2da64d164d8b79c1db)(const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level,

79 const char \*fmt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg0, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1);

80

[ 82](log__frontend_8h.md#a3ef25b9e13a89b566c507fcf14d7fb91)void [log\_frontend\_panic](log__frontend_8h.md#a3ef25b9e13a89b566c507fcf14d7fb91)(void);

83

84#endif /\* LOG\_FRONTEND\_H\_ \*/

[log\_core.h](log__core_8h.md)

[log\_frontend\_init](log__frontend_8h.md#a10b0e6f2dd38be09465b6356586f6745)

void log\_frontend\_init(void)

Initialize frontend.

[log\_frontend\_simple\_2](log__frontend_8h.md#a13ea68c36a760c2da64d164d8b79c1db)

void log\_frontend\_simple\_2(const void \*source, uint32\_t level, const char \*fmt, uint32\_t arg0, uint32\_t arg1)

Log message with 2 arguments.

[log\_frontend\_simple\_0](log__frontend_8h.md#a19e07719a21e8d2138d8e5932b1e7c68)

void log\_frontend\_simple\_0(const void \*source, uint32\_t level, const char \*fmt)

Log message with 0 arguments.

[log\_frontend\_panic](log__frontend_8h.md#a3ef25b9e13a89b566c507fcf14d7fb91)

void log\_frontend\_panic(void)

Panic state notification.

[log\_frontend\_simple\_1](log__frontend_8h.md#a6a4875ae710dc7e14c93b9225d2496d2)

void log\_frontend\_simple\_1(const void \*source, uint32\_t level, const char \*fmt, uint32\_t arg)

Log message with 1 argument.

[log\_frontend\_msg](log__frontend_8h.md#a81d90e2daca1f6c16f948c6a725803ba)

void log\_frontend\_msg(const void \*source, const struct log\_msg\_desc desc, uint8\_t \*package, const void \*data)

Log generic message.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[log\_msg\_desc](structlog__msg__desc.md)

**Definition** log\_msg.h:56

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_frontend.h](log__frontend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
