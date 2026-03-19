---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__futex.html
original_path: doxygen/html/structk__futex.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_futex Struct Reference

futex structure
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [val](#a454ad1b595b899306c8e9c8e1431e7a7) |

## Detailed Description

futex structure

A [k\_futex](structk__futex.md "futex structure") is a lightweight mutual exclusion primitive designed to minimize kernel involvement. Uncontended operation relies only on atomic access to shared memory. [k\_futex](structk__futex.md "futex structure") are tracked as kernel objects and can live in user memory so that any access bypasses the kernel object permission management mechanism.

## Field Documentation

## [◆ ](#a454ad1b595b899306c8e9c8e1431e7a7)val

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) k\_futex::val |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_futex](structk__futex.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
