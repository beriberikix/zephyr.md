---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__version__apis.html
original_path: doxygen/html/group__version__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Version APIs

[Kernel APIs](group__kernel__apis.md)

The kernel version has been converted from a string to a four-byte quantity that is divided into two parts.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [SYS\_KERNEL\_VER\_MAJOR](#ga607e6596eedd6b15e52d707dfd886cb1)(ver) |
| #define | [SYS\_KERNEL\_VER\_MINOR](#ga8074ea738e2f8aa7ab5e3e75b411286f)(ver) |
| #define | [SYS\_KERNEL\_VER\_PATCHLEVEL](#ga59bdad0b6a5ab7b36b3abdccfc6aec5f)(ver) |

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_kernel\_version\_get](#ga7979b71e0ee58ec1951b675a29368374) (void) |
|  | Return the kernel version of the present build. |

## Detailed Description

The kernel version has been converted from a string to a four-byte quantity that is divided into two parts.

Part 1: The three most significant bytes represent the kernel's numeric version, x.y.z. These fields denote: x – major release y – minor release z – patchlevel release Each of these elements must therefore be in the range 0 to 255, inclusive.

Part 2: The least significant byte is reserved for future use.

## Macro Definition Documentation

## [◆ ](#ga607e6596eedd6b15e52d707dfd886cb1)SYS\_KERNEL\_VER\_MAJOR

| #define SYS\_KERNEL\_VER\_MAJOR | ( |  | *ver* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_version.h](kernel__version_8h.md)>`

**Value:**

(((ver) >> 24) & 0xFF)

## [◆ ](#ga8074ea738e2f8aa7ab5e3e75b411286f)SYS\_KERNEL\_VER\_MINOR

| #define SYS\_KERNEL\_VER\_MINOR | ( |  | *ver* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_version.h](kernel__version_8h.md)>`

**Value:**

(((ver) >> 16) & 0xFF)

## [◆ ](#ga59bdad0b6a5ab7b36b3abdccfc6aec5f)SYS\_KERNEL\_VER\_PATCHLEVEL

| #define SYS\_KERNEL\_VER\_PATCHLEVEL | ( |  | *ver* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_version.h](kernel__version_8h.md)>`

**Value:**

(((ver) >> 8) & 0xFF)

## Function Documentation

## [◆ ](#ga7979b71e0ee58ec1951b675a29368374)sys\_kernel\_version\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_kernel\_version\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_version.h](kernel__version_8h.md)>`

Return the kernel version of the present build.

The kernel version is a four-byte value, whose format is described in the file "kernel\_version.h".

Returns
:   kernel version

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
