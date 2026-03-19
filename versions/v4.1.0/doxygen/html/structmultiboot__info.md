---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmultiboot__info.html
original_path: doxygen/html/structmultiboot__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

multiboot\_info Struct Reference

`#include <[multiboot_info.h](multiboot__info_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a33c78eb1aec2573f8293acf9a42fe2a8) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mem\_lower](#a8c88b721d871cb57a51feb5cd5fbdb6c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mem\_upper](#a8ecb8953e55d1f6b75a3892cdc82a0b5) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [unused0](#a769182fd546a2231c7cec58ea1a77789) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cmdline](#aac1e78293233aa63654d4c0161820201) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [unused1](#a2fda76c274faccbc23a2b1e1155be45d) [6] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mmap\_length](#a65bfac8b5152c771a4b8eadd408ca0d6) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mmap\_addr](#ac977f37274093fd9874d68dfb038e143) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [unused2](#a44d645d01d52f7ad6fc82c37b7a66e37) [9] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fb\_addr\_lo](#a4470854aa62c829c5ada578876a68944) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fb\_addr\_hi](#a51ec099821903ee057a8163272da2760) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fb\_pitch](#a1a412fb3d3f792b173787a65f32450d6) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fb\_width](#ac0d58fbf588108f6f0109db47efeae37) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fb\_height](#a2a23c846d241bbb1469ec8565e8b3cef) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fb\_bpp](#a0a5bc6718a8cae87416553fa6100b013) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fb\_type](#a33735d95e34f7fc9588cea69efbb5075) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fb\_color\_info](#a7ddf1b8d00568efa22fbc11074d6fc98) [6] |

## Field Documentation

## [◆ ](#aac1e78293233aa63654d4c0161820201)cmdline

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::cmdline |
| --- |

## [◆ ](#a51ec099821903ee057a8163272da2760)fb\_addr\_hi

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::fb\_addr\_hi |
| --- |

## [◆ ](#a4470854aa62c829c5ada578876a68944)fb\_addr\_lo

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::fb\_addr\_lo |
| --- |

## [◆ ](#a0a5bc6718a8cae87416553fa6100b013)fb\_bpp

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) multiboot\_info::fb\_bpp |
| --- |

## [◆ ](#a7ddf1b8d00568efa22fbc11074d6fc98)fb\_color\_info

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) multiboot\_info::fb\_color\_info[6] |
| --- |

## [◆ ](#a2a23c846d241bbb1469ec8565e8b3cef)fb\_height

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::fb\_height |
| --- |

## [◆ ](#a1a412fb3d3f792b173787a65f32450d6)fb\_pitch

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::fb\_pitch |
| --- |

## [◆ ](#a33735d95e34f7fc9588cea69efbb5075)fb\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) multiboot\_info::fb\_type |
| --- |

## [◆ ](#ac0d58fbf588108f6f0109db47efeae37)fb\_width

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::fb\_width |
| --- |

## [◆ ](#a33c78eb1aec2573f8293acf9a42fe2a8)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::flags |
| --- |

## [◆ ](#a8c88b721d871cb57a51feb5cd5fbdb6c)mem\_lower

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::mem\_lower |
| --- |

## [◆ ](#a8ecb8953e55d1f6b75a3892cdc82a0b5)mem\_upper

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::mem\_upper |
| --- |

## [◆ ](#ac977f37274093fd9874d68dfb038e143)mmap\_addr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::mmap\_addr |
| --- |

## [◆ ](#a65bfac8b5152c771a4b8eadd408ca0d6)mmap\_length

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::mmap\_length |
| --- |

## [◆ ](#a769182fd546a2231c7cec58ea1a77789)unused0

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::unused0 |
| --- |

## [◆ ](#a2fda76c274faccbc23a2b1e1155be45d)unused1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::unused1[6] |
| --- |

## [◆ ](#a44d645d01d52f7ad6fc82c37b7a66e37)unused2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) multiboot\_info::unused2[9] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/arch/x86/[multiboot\_info.h](multiboot__info_8h_source.md)

- [multiboot\_info](structmultiboot__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
