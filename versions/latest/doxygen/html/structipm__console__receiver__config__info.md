---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structipm__console__receiver__config__info.html
original_path: doxygen/html/structipm__console__receiver__config__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipm\_console\_receiver\_config\_info Struct Reference

`#include <[ipm_console.h](ipm__console_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char \* | [bind\_to](#ac57741917d3d869680bb4b78446ed269) |
|  | Name of the low-level IPM driver to bind to. |
| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | [thread\_stack](#a924802d5b239f37b25f519c4c9e0be5f) |
|  | Stack for the receiver's thread, which prints out messages as they come in. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [ring\_buf\_data](#aab7bf2a943d620d3fe4a85a08423335b) |
|  | Ring buffer data area for stashing characters from the interrupt callback. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [rb\_size32](#a2ba6b50f7f949b21eb25031ad74699e6) |
|  | Size of ring\_buf\_data in 32-bit chunks. |
| char \* | [line\_buf](#a340991c90102acee70fc7ca3fdcf932f) |
|  | Line buffer for incoming messages, characters accumulate here and then are sent to [printk()](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54 "Print kernel debugging message.") once full (including a trailing NULL) or a carriage return seen. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [lb\_size](#ac7456fac5c924586f2a7f9ffa55f7d82) |
|  | Size in bytes of the line buffer. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [flags](#ab41bc0fddbb023f7269be72864084e61) |
|  | Destination for received console messages, one of IPM\_CONSOLE\_STDOUT or IPM\_CONSOLE\_PRINTK. |

## Field Documentation

## [◆ ](#ac57741917d3d869680bb4b78446ed269)bind\_to

| char\* ipm\_console\_receiver\_config\_info::bind\_to |
| --- |

Name of the low-level IPM driver to bind to.

## [◆ ](#ab41bc0fddbb023f7269be72864084e61)flags

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ipm\_console\_receiver\_config\_info::flags |
| --- |

Destination for received console messages, one of IPM\_CONSOLE\_STDOUT or IPM\_CONSOLE\_PRINTK.

## [◆ ](#ac7456fac5c924586f2a7f9ffa55f7d82)lb\_size

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ipm\_console\_receiver\_config\_info::lb\_size |
| --- |

Size in bytes of the line buffer.

Must be at least 2

## [◆ ](#a340991c90102acee70fc7ca3fdcf932f)line\_buf

| char\* ipm\_console\_receiver\_config\_info::line\_buf |
| --- |

Line buffer for incoming messages, characters accumulate here and then are sent to [printk()](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54 "Print kernel debugging message.") once full (including a trailing NULL) or a carriage return seen.

## [◆ ](#a2ba6b50f7f949b21eb25031ad74699e6)rb\_size32

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ipm\_console\_receiver\_config\_info::rb\_size32 |
| --- |

Size of ring\_buf\_data in 32-bit chunks.

## [◆ ](#aab7bf2a943d620d3fe4a85a08423335b)ring\_buf\_data

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* ipm\_console\_receiver\_config\_info::ring\_buf\_data |
| --- |

Ring buffer data area for stashing characters from the interrupt callback.

## [◆ ](#a924802d5b239f37b25f519c4c9e0be5f)thread\_stack

| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)\* ipm\_console\_receiver\_config\_info::thread\_stack |
| --- |

Stack for the receiver's thread, which prints out messages as they come in.

Should be sized CONFIG\_IPM\_CONSOLE\_STACK\_SIZE

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/console/[ipm\_console.h](ipm__console_8h_source.md)

- [ipm\_console\_receiver\_config\_info](structipm__console__receiver__config__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
