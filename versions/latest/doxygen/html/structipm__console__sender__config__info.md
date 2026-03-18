---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structipm__console__sender__config__info.html
original_path: doxygen/html/structipm__console__sender__config__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipm\_console\_sender\_config\_info Struct Reference

`#include <[ipm_console.h](ipm__console_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char \* | [bind\_to](#aed3d8f396e858ddd9c4ea55e647feb34) |
|  | Name of the low-level driver to bind to. |
| int | [flags](#a95e4bf553f053ff389ae9e85f3d86ef3) |
|  | Source of messages to forward, hooks will be installed. |

## Field Documentation

## [◆ ](#aed3d8f396e858ddd9c4ea55e647feb34)bind\_to

| char\* ipm\_console\_sender\_config\_info::bind\_to |
| --- |

Name of the low-level driver to bind to.

## [◆ ](#a95e4bf553f053ff389ae9e85f3d86ef3)flags

| int ipm\_console\_sender\_config\_info::flags |
| --- |

Source of messages to forward, hooks will be installed.

Can be IPM\_CONSOLE\_STDOUT, IPM\_CONSOLE\_PRINTK, or both

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/console/[ipm\_console.h](ipm__console_8h_source.md)

- [ipm\_console\_sender\_config\_info](structipm__console__sender__config__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
