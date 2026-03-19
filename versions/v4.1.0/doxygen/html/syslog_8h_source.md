---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/syslog_8h_source.html
original_path: doxygen/html/syslog_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syslog.h

[Go to the documentation of this file.](syslog_8h.md)

1/\*

2 \* Copyright (c) 2024, Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYSLOG\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SYSLOG\_H\_

8

9#include <stdarg.h>

10

11/\* option \*/

[ 12](syslog_8h.md#a7b264572ee428bb73548226ba5bbe88a)#define LOG\_PID 1

[ 13](syslog_8h.md#aeccd30c76c44f407cd9d5441318b6aba)#define LOG\_CONS 2

[ 14](syslog_8h.md#a446430791b21a34e7308046826759d25)#define LOG\_NDELAY 4

[ 15](syslog_8h.md#aed1240a0e0d7f574a09ea915d4e1af85)#define LOG\_ODELAY 8

[ 16](syslog_8h.md#a9dff0ca45769bfa276ce3f0080acc397)#define LOG\_NOWAIT 16

[ 17](syslog_8h.md#a542160b84335cc94dfb75604fd40d341)#define LOG\_PERROR 32

18

19/\* facility \*/

[ 20](syslog_8h.md#a3782c789d7d0eeab593758f80e436da4)#define LOG\_KERN 0

[ 21](syslog_8h.md#ac8b1ae5666bff93a5db0bb45f99f5832)#define LOG\_USER 1

[ 22](syslog_8h.md#a135a6127cf9b508b4361594e842eefc0)#define LOG\_MAIL 2

[ 23](syslog_8h.md#aeae7c4754f60a7931ce0141bac37e798)#define LOG\_NEWS 3

[ 24](syslog_8h.md#ab0db5f3df16ec19a5897b852930bca54)#define LOG\_UUCP 4

[ 25](syslog_8h.md#a9961fc94ec213d970dc7c8d9608e1d42)#define LOG\_DAEMON 5

[ 26](syslog_8h.md#a22b8a93c6a27426f9a8ad4ce9407e86d)#define LOG\_AUTH 6

[ 27](syslog_8h.md#a285963d2ea1986d2f31ae7c6c0b5dc4e)#define LOG\_CRON 7

[ 28](syslog_8h.md#a3c6927ac15f5eaa92ee6d79b2837b68e)#define LOG\_LPR 8

[ 29](syslog_8h.md#a25eab08bcadd790ad09db8ab1391d7b4)#define LOG\_LOCAL0 9

[ 30](syslog_8h.md#ae2702880c720b92d9b133a394536fc55)#define LOG\_LOCAL1 10

[ 31](syslog_8h.md#a3bba702c131c9a343f43cefe9dc54806)#define LOG\_LOCAL2 11

[ 32](syslog_8h.md#adc43741bf59af027c44c46f6c4692592)#define LOG\_LOCAL3 12

[ 33](syslog_8h.md#a7c96c20eb0501c681dea19b78c36e475)#define LOG\_LOCAL4 13

[ 34](syslog_8h.md#ac19bfe79880b74eb63d406c218c89350)#define LOG\_LOCAL5 14

[ 35](syslog_8h.md#a71d48fd009db4d4e57019903d372347a)#define LOG\_LOCAL6 15

[ 36](syslog_8h.md#aea1efd5b3880503ca94c623d0517e497)#define LOG\_LOCAL7 16

37

38/\* priority \*/

[ 39](syslog_8h.md#a5c6e8b60c2512dfc0e0224d25a61cb2c)#define LOG\_EMERG 0

[ 40](syslog_8h.md#a12b2a3bb9e3adfeb35b4e5514e7d9043)#define LOG\_ALERT 1

[ 41](syslog_8h.md#aaa731313f5c63e855fefb5f6519c3283)#define LOG\_CRIT 2

[ 42](syslog_8h.md#a96fad55b3f5adf08c39e4c877cf185e3)#define LOG\_ERR 3

[ 43](syslog_8h.md#adf4476a6a4ea6c74231c826e899d7189)#define LOG\_WARNING 4

[ 44](syslog_8h.md#ad89ee324d180cdcd7defcc709ff9ca42)#define LOG\_NOTICE 5

[ 45](syslog_8h.md#aeb4f36db01bd128c7afeac5889dac311)#define LOG\_INFO 6

[ 46](syslog_8h.md#a6ff63e8955665c4a58b1598f2b07c51a)#define LOG\_DEBUG 7

47

48/\* generate a valid log mask \*/

[ 49](syslog_8h.md#a8e1c2d42597b3dd0eeda52ed444b1d4a)#define LOG\_MASK(mask) ((mask) & BIT\_MASK(LOG\_DEBUG + 1))

50

51#ifdef \_\_cplusplus

52extern "C" {

53#endif

54

[ 55](syslog_8h.md#ae1e4e53707d8c3fbc36bbc523fbbcda3)void [closelog](syslog_8h.md#ae1e4e53707d8c3fbc36bbc523fbbcda3)(void);

[ 56](syslog_8h.md#a0dc773e0b62cd9b9e42addd25592a50e)void [openlog](syslog_8h.md#a0dc773e0b62cd9b9e42addd25592a50e)(const char \*ident, int logopt, int facility);

[ 57](syslog_8h.md#aca20103a73ae93ed63b2a1a94b93f53b)int [setlogmask](syslog_8h.md#aca20103a73ae93ed63b2a1a94b93f53b)(int maskpri);

[ 58](syslog_8h.md#a7b3a37aea8e8f9fe12fe0340eaccb838)void [syslog](syslog_8h.md#a7b3a37aea8e8f9fe12fe0340eaccb838)(int priority, const char \*message, ...);

[ 59](syslog_8h.md#a9722b4c868bed8d78283a4202a6f21d6)void [vsyslog](syslog_8h.md#a9722b4c868bed8d78283a4202a6f21d6)(int priority, const char \*format, va\_list ap);

60

61#ifdef \_\_cplusplus

62}

63#endif

64

65#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYSLOG\_H\_ \*/

[openlog](syslog_8h.md#a0dc773e0b62cd9b9e42addd25592a50e)

void openlog(const char \*ident, int logopt, int facility)

[syslog](syslog_8h.md#a7b3a37aea8e8f9fe12fe0340eaccb838)

void syslog(int priority, const char \*message,...)

[vsyslog](syslog_8h.md#a9722b4c868bed8d78283a4202a6f21d6)

void vsyslog(int priority, const char \*format, va\_list ap)

[setlogmask](syslog_8h.md#aca20103a73ae93ed63b2a1a94b93f53b)

int setlogmask(int maskpri)

[closelog](syslog_8h.md#ae1e4e53707d8c3fbc36bbc523fbbcda3)

void closelog(void)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [syslog.h](syslog_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
