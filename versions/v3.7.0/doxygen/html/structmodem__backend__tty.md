---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmodem__backend__tty.html
original_path: doxygen/html/structmodem__backend__tty.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_backend\_tty Struct Reference

`#include <[tty.h](modem_2backend_2tty_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [tty\_path](#af6a76d369957f01f9d44c7f4bba67642) |
| int | [tty\_fd](#abf93189b2640afa8bad440089bb1a863) |
| struct modem\_pipe | [pipe](#abe654bb7b24f23417e60bc8af7b73d36) |
| struct [k\_thread](structk__thread.md) | [thread](#ad454321f08f334b028bb63cbb0d8e8f6) |
| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | [stack](#a23afe812c5951bfa41251610056aa3aa) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [stack\_size](#a2ea8d323973de8423f558a7a2e6b8984) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [state](#a7f85f1f41fbcdf69ad1846a3af1b0b1e) |

## Field Documentation

## [◆ ](#abe654bb7b24f23417e60bc8af7b73d36)pipe

| struct modem\_pipe modem\_backend\_tty::pipe |
| --- |

## [◆ ](#a23afe812c5951bfa41251610056aa3aa)stack

| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)\* modem\_backend\_tty::stack |
| --- |

## [◆ ](#a2ea8d323973de8423f558a7a2e6b8984)stack\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) modem\_backend\_tty::stack\_size |
| --- |

## [◆ ](#a7f85f1f41fbcdf69ad1846a3af1b0b1e)state

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) modem\_backend\_tty::state |
| --- |

## [◆ ](#ad454321f08f334b028bb63cbb0d8e8f6)thread

| struct [k\_thread](structk__thread.md) modem\_backend\_tty::thread |
| --- |

## [◆ ](#abf93189b2640afa8bad440089bb1a863)tty\_fd

| int modem\_backend\_tty::tty\_fd |
| --- |

## [◆ ](#af6a76d369957f01f9d44c7f4bba67642)tty\_path

| const char\* modem\_backend\_tty::tty\_path |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/backend/[tty.h](modem_2backend_2tty_8h_source.md)

- [modem\_backend\_tty](structmodem__backend__tty.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
