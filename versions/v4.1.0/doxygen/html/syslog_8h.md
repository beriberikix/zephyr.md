---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/syslog_8h.html
original_path: doxygen/html/syslog_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syslog.h File Reference

`#include <stdarg.h>`

[Go to the source code of this file.](syslog_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LOG\_PID](#a7b264572ee428bb73548226ba5bbe88a)   1 |
| #define | [LOG\_CONS](#aeccd30c76c44f407cd9d5441318b6aba)   2 |
| #define | [LOG\_NDELAY](#a446430791b21a34e7308046826759d25)   4 |
| #define | [LOG\_ODELAY](#aed1240a0e0d7f574a09ea915d4e1af85)   8 |
| #define | [LOG\_NOWAIT](#a9dff0ca45769bfa276ce3f0080acc397)   16 |
| #define | [LOG\_PERROR](#a542160b84335cc94dfb75604fd40d341)   32 |
| #define | [LOG\_KERN](#a3782c789d7d0eeab593758f80e436da4)   0 |
| #define | [LOG\_USER](#ac8b1ae5666bff93a5db0bb45f99f5832)   1 |
| #define | [LOG\_MAIL](#a135a6127cf9b508b4361594e842eefc0)   2 |
| #define | [LOG\_NEWS](#aeae7c4754f60a7931ce0141bac37e798)   3 |
| #define | [LOG\_UUCP](#ab0db5f3df16ec19a5897b852930bca54)   4 |
| #define | [LOG\_DAEMON](#a9961fc94ec213d970dc7c8d9608e1d42)   5 |
| #define | [LOG\_AUTH](#a22b8a93c6a27426f9a8ad4ce9407e86d)   6 |
| #define | [LOG\_CRON](#a285963d2ea1986d2f31ae7c6c0b5dc4e)   7 |
| #define | [LOG\_LPR](#a3c6927ac15f5eaa92ee6d79b2837b68e)   8 |
| #define | [LOG\_LOCAL0](#a25eab08bcadd790ad09db8ab1391d7b4)   9 |
| #define | [LOG\_LOCAL1](#ae2702880c720b92d9b133a394536fc55)   10 |
| #define | [LOG\_LOCAL2](#a3bba702c131c9a343f43cefe9dc54806)   11 |
| #define | [LOG\_LOCAL3](#adc43741bf59af027c44c46f6c4692592)   12 |
| #define | [LOG\_LOCAL4](#a7c96c20eb0501c681dea19b78c36e475)   13 |
| #define | [LOG\_LOCAL5](#ac19bfe79880b74eb63d406c218c89350)   14 |
| #define | [LOG\_LOCAL6](#a71d48fd009db4d4e57019903d372347a)   15 |
| #define | [LOG\_LOCAL7](#aea1efd5b3880503ca94c623d0517e497)   16 |
| #define | [LOG\_EMERG](#a5c6e8b60c2512dfc0e0224d25a61cb2c)   0 |
| #define | [LOG\_ALERT](#a12b2a3bb9e3adfeb35b4e5514e7d9043)   1 |
| #define | [LOG\_CRIT](#aaa731313f5c63e855fefb5f6519c3283)   2 |
| #define | [LOG\_ERR](#a96fad55b3f5adf08c39e4c877cf185e3)   3 |
| #define | [LOG\_WARNING](#adf4476a6a4ea6c74231c826e899d7189)   4 |
| #define | [LOG\_NOTICE](#ad89ee324d180cdcd7defcc709ff9ca42)   5 |
| #define | [LOG\_INFO](#aeb4f36db01bd128c7afeac5889dac311)   6 |
| #define | [LOG\_DEBUG](#a6ff63e8955665c4a58b1598f2b07c51a)   7 |
| #define | [LOG\_MASK](#a8e1c2d42597b3dd0eeda52ed444b1d4a)(mask) |

| Functions | |
| --- | --- |
| void | [closelog](#ae1e4e53707d8c3fbc36bbc523fbbcda3) (void) |
| void | [openlog](#a0dc773e0b62cd9b9e42addd25592a50e) (const char \*ident, int logopt, int facility) |
| int | [setlogmask](#aca20103a73ae93ed63b2a1a94b93f53b) (int maskpri) |
| void | [syslog](#a7b3a37aea8e8f9fe12fe0340eaccb838) (int priority, const char \*message,...) |
| void | [vsyslog](#a9722b4c868bed8d78283a4202a6f21d6) (int priority, const char \*format, va\_list ap) |

## Macro Definition Documentation

## [◆ ](#a12b2a3bb9e3adfeb35b4e5514e7d9043)LOG\_ALERT

| #define LOG\_ALERT   1 |
| --- |

## [◆ ](#a22b8a93c6a27426f9a8ad4ce9407e86d)LOG\_AUTH

| #define LOG\_AUTH   6 |
| --- |

## [◆ ](#aeccd30c76c44f407cd9d5441318b6aba)LOG\_CONS

| #define LOG\_CONS   2 |
| --- |

## [◆ ](#aaa731313f5c63e855fefb5f6519c3283)LOG\_CRIT

| #define LOG\_CRIT   2 |
| --- |

## [◆ ](#a285963d2ea1986d2f31ae7c6c0b5dc4e)LOG\_CRON

| #define LOG\_CRON   7 |
| --- |

## [◆ ](#a9961fc94ec213d970dc7c8d9608e1d42)LOG\_DAEMON

| #define LOG\_DAEMON   5 |
| --- |

## [◆ ](#a6ff63e8955665c4a58b1598f2b07c51a)LOG\_DEBUG

| #define LOG\_DEBUG   7 |
| --- |

## [◆ ](#a5c6e8b60c2512dfc0e0224d25a61cb2c)LOG\_EMERG

| #define LOG\_EMERG   0 |
| --- |

## [◆ ](#a96fad55b3f5adf08c39e4c877cf185e3)LOG\_ERR

| #define LOG\_ERR   3 |
| --- |

## [◆ ](#aeb4f36db01bd128c7afeac5889dac311)LOG\_INFO

| #define LOG\_INFO   6 |
| --- |

## [◆ ](#a3782c789d7d0eeab593758f80e436da4)LOG\_KERN

| #define LOG\_KERN   0 |
| --- |

## [◆ ](#a25eab08bcadd790ad09db8ab1391d7b4)LOG\_LOCAL0

| #define LOG\_LOCAL0   9 |
| --- |

## [◆ ](#ae2702880c720b92d9b133a394536fc55)LOG\_LOCAL1

| #define LOG\_LOCAL1   10 |
| --- |

## [◆ ](#a3bba702c131c9a343f43cefe9dc54806)LOG\_LOCAL2

| #define LOG\_LOCAL2   11 |
| --- |

## [◆ ](#adc43741bf59af027c44c46f6c4692592)LOG\_LOCAL3

| #define LOG\_LOCAL3   12 |
| --- |

## [◆ ](#a7c96c20eb0501c681dea19b78c36e475)LOG\_LOCAL4

| #define LOG\_LOCAL4   13 |
| --- |

## [◆ ](#ac19bfe79880b74eb63d406c218c89350)LOG\_LOCAL5

| #define LOG\_LOCAL5   14 |
| --- |

## [◆ ](#a71d48fd009db4d4e57019903d372347a)LOG\_LOCAL6

| #define LOG\_LOCAL6   15 |
| --- |

## [◆ ](#aea1efd5b3880503ca94c623d0517e497)LOG\_LOCAL7

| #define LOG\_LOCAL7   16 |
| --- |

## [◆ ](#a3c6927ac15f5eaa92ee6d79b2837b68e)LOG\_LPR

| #define LOG\_LPR   8 |
| --- |

## [◆ ](#a135a6127cf9b508b4361594e842eefc0)LOG\_MAIL

| #define LOG\_MAIL   2 |
| --- |

## [◆ ](#a8e1c2d42597b3dd0eeda52ed444b1d4a)LOG\_MASK

| #define LOG\_MASK | ( |  | *mask* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mask) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)([LOG\_DEBUG](#a6ff63e8955665c4a58b1598f2b07c51a) + 1))

[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

Bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:68

[LOG\_DEBUG](#a6ff63e8955665c4a58b1598f2b07c51a)

#define LOG\_DEBUG

**Definition** syslog.h:46

## [◆ ](#a446430791b21a34e7308046826759d25)LOG\_NDELAY

| #define LOG\_NDELAY   4 |
| --- |

## [◆ ](#aeae7c4754f60a7931ce0141bac37e798)LOG\_NEWS

| #define LOG\_NEWS   3 |
| --- |

## [◆ ](#ad89ee324d180cdcd7defcc709ff9ca42)LOG\_NOTICE

| #define LOG\_NOTICE   5 |
| --- |

## [◆ ](#a9dff0ca45769bfa276ce3f0080acc397)LOG\_NOWAIT

| #define LOG\_NOWAIT   16 |
| --- |

## [◆ ](#aed1240a0e0d7f574a09ea915d4e1af85)LOG\_ODELAY

| #define LOG\_ODELAY   8 |
| --- |

## [◆ ](#a542160b84335cc94dfb75604fd40d341)LOG\_PERROR

| #define LOG\_PERROR   32 |
| --- |

## [◆ ](#a7b264572ee428bb73548226ba5bbe88a)LOG\_PID

| #define LOG\_PID   1 |
| --- |

## [◆ ](#ac8b1ae5666bff93a5db0bb45f99f5832)LOG\_USER

| #define LOG\_USER   1 |
| --- |

## [◆ ](#ab0db5f3df16ec19a5897b852930bca54)LOG\_UUCP

| #define LOG\_UUCP   4 |
| --- |

## [◆ ](#adf4476a6a4ea6c74231c826e899d7189)LOG\_WARNING

| #define LOG\_WARNING   4 |
| --- |

## Function Documentation

## [◆ ](#ae1e4e53707d8c3fbc36bbc523fbbcda3)closelog()

| void closelog | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a0dc773e0b62cd9b9e42addd25592a50e)openlog()

| void openlog | ( | const char \* | *ident*, |
| --- | --- | --- | --- |
|  |  | int | *logopt*, |
|  |  | int | *facility* ) |

## [◆ ](#aca20103a73ae93ed63b2a1a94b93f53b)setlogmask()

| int setlogmask | ( | int | *maskpri* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a7b3a37aea8e8f9fe12fe0340eaccb838)syslog()

| void syslog | ( | int | *priority*, |
| --- | --- | --- | --- |
|  |  | const char \* | *message*, |
|  |  |  | *...* ) |

## [◆ ](#a9722b4c868bed8d78283a4202a6f21d6)vsyslog()

| void vsyslog | ( | int | *priority*, |
| --- | --- | --- | --- |
|  |  | const char \* | *format*, |
|  |  | va\_list | *ap* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [syslog.h](syslog_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
