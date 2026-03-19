---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsigaction.html
original_path: doxygen/html/structsigaction.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sigaction Struct Reference

`#include <[signal.h](include_2zephyr_2posix_2signal_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [sa\_handler](#a02261e69c38b387de4c6b96a26e26199) )(int signno) |
| [sigset\_t](structsigset__t.md) | [sa\_mask](#a684e70081d03d46ce70af097ea5cfd49) |
| int | [sa\_flags](#aea0dabe7a03641c8b426521f4406b425) |
| void(\* | [sa\_sigaction](#a068409137809e8e6e4a522d29daa65af) )(int signo, [siginfo\_t](structsiginfo__t.md) \*info, void \*context) |

## Field Documentation

## [◆ ](#aea0dabe7a03641c8b426521f4406b425)sa\_flags

| int sigaction::sa\_flags |
| --- |

## [◆ ](#a02261e69c38b387de4c6b96a26e26199)sa\_handler

| void(\* sigaction::sa\_handler) (int signno) |
| --- |

## [◆ ](#a684e70081d03d46ce70af097ea5cfd49)sa\_mask

| [sigset\_t](structsigset__t.md) sigaction::sa\_mask |
| --- |

## [◆ ](#a068409137809e8e6e4a522d29daa65af)sa\_sigaction

| void(\* sigaction::sa\_sigaction) (int signo, [siginfo\_t](structsiginfo__t.md) \*info, void \*context) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/posix/[signal.h](include_2zephyr_2posix_2signal_8h_source.md)

- [sigaction](structsigaction.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
