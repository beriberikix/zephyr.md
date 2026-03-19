---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2arm64_2sys__io_8h.html
original_path: doxygen/html/arch_2arm64_2sys__io_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_io.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/sys_io.h](sys_2sys__io_8h_source.md)>`  
`#include <[zephyr/sys/barrier.h](sys_2barrier_8h_source.md)>`

[Go to the source code of this file.](arch_2arm64_2sys__io_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_read8](#a51f9740fef1b1bb2abc93126ca2646ae) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_write8](#adf3b7a8a798d7497661d54d705a078fc) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sys\_read16](#ad8daa7da2671ca845272861859463567) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_write16](#a5cae8f8c0ea3749985e80f6ca85b1b13) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_read32](#a62f6066146f924b75015ae976b27866a) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_write32](#a2d04bb22b0aacb66c62b040ca36cb03f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_read64](#ae20bb8c275dcc157c1be9b232d00ff9d) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_write64](#a00285d93d1c8951641510e2071d46b40) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr) |

## Function Documentation

## [◆ ](#ad8daa7da2671ca845272861859463567)sys\_read16()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sys\_read16 | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a62f6066146f924b75015ae976b27866a)sys\_read32()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_read32 | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae20bb8c275dcc157c1be9b232d00ff9d)sys\_read64()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_read64 | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a51f9740fef1b1bb2abc93126ca2646ae)sys\_read8()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_read8 | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5cae8f8c0ea3749985e80f6ca85b1b13)sys\_write16()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_write16 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data*, | | --- | --- | --- | --- | |  |  | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2d04bb22b0aacb66c62b040ca36cb03f)sys\_write32()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_write32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data*, | | --- | --- | --- | --- | |  |  | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a00285d93d1c8951641510e2071d46b40)sys\_write64()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_write64 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *data*, | | --- | --- | --- | --- | |  |  | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adf3b7a8a798d7497661d54d705a078fc)sys\_write8()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_write8 | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data*, | | --- | --- | --- | --- | |  |  | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [sys\_io.h](arch_2arm64_2sys__io_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
