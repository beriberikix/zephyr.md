---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2riscv_2thread_8h.html
original_path: doxygen/html/arch_2riscv_2thread_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h File Reference

Per-arch thread definition.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](arch_2riscv_2thread_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RV\_FP\_TYPE](#a94fb796ff93ddd2633c9cc48d9bc1214)   [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) |
| #define | [PMP\_M\_MODE\_SLOTS](#ad37c7fba59f9d64bc2b4d154c274e007)   8 /\* 8 is plenty enough for m-mode \*/ |

## Detailed Description

Per-arch thread definition.

This file contains definitions for

struct \_thread\_arch struct \_callee\_saved

necessary to instantiate instances of struct [k\_thread](structk__thread.md "Thread Structure.").

## Macro Definition Documentation

## [◆ ](#ad37c7fba59f9d64bc2b4d154c274e007)PMP\_M\_MODE\_SLOTS

| #define PMP\_M\_MODE\_SLOTS   8 /\* 8 is plenty enough for m-mode \*/ |
| --- |

## [◆ ](#a94fb796ff93ddd2633c9cc48d9bc1214)RV\_FP\_TYPE

| #define RV\_FP\_TYPE   [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [thread.h](arch_2riscv_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
