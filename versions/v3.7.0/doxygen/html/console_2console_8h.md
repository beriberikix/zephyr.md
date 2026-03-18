---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/console_2console_8h.html
original_path: doxygen/html/console_2console_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

console.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](console_2console_8h_source.md)

| Functions | |
| --- | --- |
| int | [console\_init](group__console__api.md#ga0bf949437e32d17992435003cf8b46b5) (void) |
|  | Initialize console device. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [console\_read](group__console__api.md#ga27785534c14d4098822db2b870b7d81d) (void \*dummy, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Read data from console. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [console\_write](group__console__api.md#ga204fd795daf9ef6b1f2803547747545e) (void \*dummy, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write data to console. |
| int | [console\_getchar](group__console__api.md#ga2ba36eb1081cd0b98aa43216ccd6fbd5) (void) |
|  | Get next char from console input buffer. |
| int | [console\_putchar](group__console__api.md#ga7bd842f1cda6c8218cb1d41420e4de49) (char c) |
|  | Output a char to console (buffered). |
| void | [console\_getline\_init](group__console__api.md#gacd13267df8567c63f2285ce0e1cbbc20) (void) |
|  | Initialize [console\_getline()](group__console__api.md#ga3454f5b84d38d46a6c2bbf7fd6baa815 "Get next line from console input buffer.") call. |
| char \* | [console\_getline](group__console__api.md#ga3454f5b84d38d46a6c2bbf7fd6baa815) (void) |
|  | Get next line from console input buffer. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [console](dir_2f086bf88c9e3ffd4c7c065f4bf7757c.md)
- [console.h](console_2console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
