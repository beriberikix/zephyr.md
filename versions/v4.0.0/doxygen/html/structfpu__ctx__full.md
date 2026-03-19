---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfpu__ctx__full.html
original_path: doxygen/html/structfpu__ctx__full.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fpu\_ctx\_full Struct Reference

`#include <[fpu.h](fpu_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [caller\_saved](#af4654001584aa8606c7c2bd3a20bb74f) [16] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [callee\_saved](#ad50e1fc3ec931979f9c3f6508fec259b) [16] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fpscr](#a66ea3fea6f0209273e960831bfab09c6) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ctx\_saved](#a6866578483d0340161bb84231ceee120) |

## Field Documentation

## [◆ ](#ad50e1fc3ec931979f9c3f6508fec259b)callee\_saved

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fpu\_ctx\_full::callee\_saved[16] |
| --- |

## [◆ ](#af4654001584aa8606c7c2bd3a20bb74f)caller\_saved

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fpu\_ctx\_full::caller\_saved[16] |
| --- |

## [◆ ](#a6866578483d0340161bb84231ceee120)ctx\_saved

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fpu\_ctx\_full::ctx\_saved |
| --- |

## [◆ ](#a66ea3fea6f0209273e960831bfab09c6)fpscr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fpu\_ctx\_full::fpscr |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/arch/arm/cortex\_m/[fpu.h](fpu_8h_source.md)

- [fpu\_ctx\_full](structfpu__ctx__full.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
