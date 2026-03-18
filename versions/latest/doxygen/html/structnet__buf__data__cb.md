---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__buf__data__cb.html
original_path: doxygen/html/structnet__buf__data__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_buf\_data\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Buffer Library](group__net__buf.md)

`#include <[buf.h](net_2buf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*(\* | [alloc](#a34bf941a262975eef4ff1c6e14a0c78f) )(struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*(\* | [ref](#a099e08c1dc2a48c821e381a8ce20cd51) )(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| void(\* | [unref](#a80c307edcf878bde8d43813854185575) )(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |

## Field Documentation

## [◆ ](#a34bf941a262975eef4ff1c6e14a0c78f)alloc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*(\* net\_buf\_data\_cb::alloc) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
| --- |

## [◆ ](#a099e08c1dc2a48c821e381a8ce20cd51)ref

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*(\* net\_buf\_data\_cb::ref) (struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| --- |

## [◆ ](#a80c307edcf878bde8d43813854185575)unref

| void(\* net\_buf\_data\_cb::unref) (struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[buf.h](net_2buf_8h_source.md)

- [net\_buf\_data\_cb](structnet__buf__data__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
