---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/xen_2public_2io_2console_8h.html
original_path: doxygen/html/xen_2public_2io_2console_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

console.h File Reference

[Go to the source code of this file.](xen_2public_2io_2console_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [xencons\_interface](structxencons__interface.md) |

| Macros | |
| --- | --- |
| #define | [MASK\_XENCONS\_IDX](#a19ac5a1c26856ccdfbba6e6cbe86430a)(idx, ring) |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [XENCONS\_RING\_IDX](#aa49f8668886bc6a29fee54402474f068) |

## Macro Definition Documentation

## [◆ ](#a19ac5a1c26856ccdfbba6e6cbe86430a)MASK\_XENCONS\_IDX

| #define MASK\_XENCONS\_IDX | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *ring* ) |

**Value:**

((idx) & (sizeof(ring)-1))

## Typedef Documentation

## [◆ ](#aa49f8668886bc6a29fee54402474f068)XENCONS\_RING\_IDX

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [XENCONS\_RING\_IDX](#aa49f8668886bc6a29fee54402474f068) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [io](dir_78ec230a751ffdc5d7d32748ed18d356.md)
- [console.h](xen_2public_2io_2console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
