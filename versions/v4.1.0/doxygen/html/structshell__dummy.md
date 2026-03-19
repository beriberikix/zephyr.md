---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structshell__dummy.html
original_path: doxygen/html/structshell__dummy.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_dummy Struct Reference

`#include <[shell_dummy.h](shell__dummy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [initialized](#a18b0aa67864bbb1bedb0af574d433cc8) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#a2eb3c3976f7d0d22318ba376ca3617c9) |
|  | current number of bytes in buffer (0 if no output) |
| char | [buf](#a3d227470504d3c565cdd5ff3408b69d3) [CONFIG\_SHELL\_BACKEND\_DUMMY\_BUF\_SIZE] |
|  | output buffer to collect shell output |

## Field Documentation

## [◆ ](#a3d227470504d3c565cdd5ff3408b69d3)buf

| char shell\_dummy::buf[CONFIG\_SHELL\_BACKEND\_DUMMY\_BUF\_SIZE] |
| --- |

output buffer to collect shell output

## [◆ ](#a18b0aa67864bbb1bedb0af574d433cc8)initialized

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shell\_dummy::initialized |
| --- |

## [◆ ](#a2eb3c3976f7d0d22318ba376ca3617c9)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) shell\_dummy::len |
| --- |

current number of bytes in buffer (0 if no output)

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_dummy.h](shell__dummy_8h_source.md)

- [shell\_dummy](structshell__dummy.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
