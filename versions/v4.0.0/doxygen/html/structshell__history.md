---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structshell__history.html
original_path: doxygen/html/structshell__history.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_history Struct Reference

`#include <[shell_history.h](shell__history_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [ring\_buf](structring__buf.md) \* | [ring\_buf](#a8e9fbd6e179a1a8063eb80df04b86395) |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [list](#af3b256c6fdb29eddedadcc2720e0b2c3) |
| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [current](#a3f7d85e4e3123048e5a7d758d54a8602) |

## Field Documentation

## [◆ ](#a3f7d85e4e3123048e5a7d758d54a8602)current

| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)\* shell\_history::current |
| --- |

## [◆ ](#af3b256c6fdb29eddedadcc2720e0b2c3)list

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) shell\_history::list |
| --- |

## [◆ ](#a8e9fbd6e179a1a8063eb80df04b86395)ring\_buf

| struct [ring\_buf](structring__buf.md)\* shell\_history::ring\_buf |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_history.h](shell__history_8h_source.md)

- [shell\_history](structshell__history.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
