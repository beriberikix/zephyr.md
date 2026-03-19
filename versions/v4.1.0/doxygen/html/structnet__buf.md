---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__buf.html
original_path: doxygen/html/structnet__buf.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_buf Struct Reference

[Operating System Services](group__os__services.md) » [Network Buffer Library](group__net__buf.md)

Network buffer representation.
[More...](#details)

`#include <[net_buf.h](net__buf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a5cc70f57e5b776cfa12b2d556e5958f3) |
|  | Allow placing the buffer into [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8 "Single-linked list structure."). |
| struct [net\_buf](structnet__buf.md) \* | [frags](#a1fa032cc23854c35eae013020823fa88) |
|  | Fragments associated with this buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ref](#a42da518a82f4c37c45814b4f8c5f2731) |
|  | Reference count. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#aa4fcce2e2894fc5dbd9cc74fc020647e) |
|  | Bit-field of buffer flags. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pool\_id](#a45f294bac054d64034bddcc4c6574d29) |
|  | Where the buffer should go when freed up. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [user\_data\_size](#a65db7bed62d7211114767e6ce58dad75) |
|  | Size of user data on this buffer. |
| union { |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [data](#ac6eef59915e7ce167442fdacbbfb5e56) |  |
|  | Pointer to the start of data in the buffer. [More...](#ac6eef59915e7ce167442fdacbbfb5e56) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [len](#ae75b7ca728fb7440ea483be8bf88bc38) |  |
|  | Length of the data behind the data pointer. [More...](#ae75b7ca728fb7440ea483be8bf88bc38) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [size](#a1522d81a002804223e25300a6961f527) |  |
|  | Amount of data that this buffer can store. [More...](#a1522d81a002804223e25300a6961f527) |
| } |  |
| }; |  |
|  | Union for convenience access to the [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") members, also preserving the old API. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [user\_data](#ade8055f804d5a1fea13e55d71d92a5e7) [] |
|  | System metadata for this buffer. |

## Detailed Description

Network buffer representation.

This struct is used to represent network buffers. Such buffers are normally defined through the NET\_BUF\_POOL\_\*\_DEFINE() APIs and allocated using the [net\_buf\_alloc()](group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005) API.

## Field Documentation

## [◆ ](#acd1c7c21fe5b7a1e0f7ea10140200a1b)[union]

| union { ... } [net\_buf](structnet__buf.md) |
| --- |

Union for convenience access to the [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") members, also preserving the old API.

## [◆ ](#ac6eef59915e7ce167442fdacbbfb5e56)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* net\_buf::data |
| --- |

Pointer to the start of data in the buffer.

## [◆ ](#aa4fcce2e2894fc5dbd9cc74fc020647e)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf::flags |
| --- |

Bit-field of buffer flags.

## [◆ ](#a1fa032cc23854c35eae013020823fa88)frags

| struct [net\_buf](structnet__buf.md)\* net\_buf::frags |
| --- |

Fragments associated with this buffer.

## [◆ ](#ae75b7ca728fb7440ea483be8bf88bc38)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf::len |
| --- |

Length of the data behind the data pointer.

## [◆ ](#a5cc70f57e5b776cfa12b2d556e5958f3)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) net\_buf::node |
| --- |

Allow placing the buffer into [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8 "Single-linked list structure.").

## [◆ ](#a45f294bac054d64034bddcc4c6574d29)pool\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf::pool\_id |
| --- |

Where the buffer should go when freed up.

## [◆ ](#a42da518a82f4c37c45814b4f8c5f2731)ref

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf::ref |
| --- |

Reference count.

## [◆ ](#a1522d81a002804223e25300a6961f527)size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf::size |
| --- |

Amount of data that this buffer can store.

## [◆ ](#ade8055f804d5a1fea13e55d71d92a5e7)user\_data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf::user\_data[] |
| --- |

System metadata for this buffer.

Cleared on allocation.

## [◆ ](#a65db7bed62d7211114767e6ce58dad75)user\_data\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf::user\_data\_size |
| --- |

Size of user data on this buffer.

---

The documentation for this struct was generated from the following file:

- zephyr/[net\_buf.h](net__buf_8h_source.md)

- [net\_buf](structnet__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
