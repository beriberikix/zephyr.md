---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/testing_8h.html
original_path: doxygen/html/testing_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

testing.h File Reference

Internal testing interfaces for Bluetooth.
[More...](#details)

`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`

[Go to the source code of this file.](testing_8h_source.md)

| Functions | |
| --- | --- |
| void | [bt\_testing\_trace\_event\_acl\_pool\_destroy](#ad881c44e84d8ba4650a33ef6bae19c4c) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Hook for acl\_in\_pool.destroy. |

## Detailed Description

Internal testing interfaces for Bluetooth.

## Function Documentation

## [◆ ](#ad881c44e84d8ba4650a33ef6bae19c4c)bt\_testing\_trace\_event\_acl\_pool\_destroy()

| void bt\_testing\_trace\_event\_acl\_pool\_destroy | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

Hook for acl\_in\_pool.destroy.

Weak-function interface. The user can simply define this function, and it will automatically become the event listener.

Attention
:   Available only when the following Kconfig option is enabled: `CONFIG_BT_TESTING`.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [testing.h](testing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
