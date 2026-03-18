---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structxen__domctl__bind__pt__irq.html
original_path: doxygen/html/structxen__domctl__bind__pt__irq.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen\_domctl\_bind\_pt\_irq Struct Reference

`#include <[domctl.h](public_2domctl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [machine\_irq](#ac7e169794a1268053698ea63689fb953) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [irq\_type](#aa1085a60b7c25661b85f7c9524b754d7) |
| union { |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [isa\_irq](#a53e7af42e7181983b80fcfedd8d709ab) |  |
| }   [isa](#a50399e43aa64a2294e134cb3db16b6a0) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [bus](#aa73344f449c2f794c1b07d81bc5e2613) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [device](#a7f1d36a2965de0d35e9e86f3825218af) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [intx](#aac07dc02b436ae553cd73503baa4372c) |  |
| }   [pci](#afd2db2c0861d6098c7ff94aa094450cc) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [gvec](#a571d737fec6ba58131b433643edc8a70) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [gflags](#abd99cec39f010ebbdf6e5cd0ba3c3676) |  |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)   [gtable](#a4fb5cf50743c77a22b7fe95acef43129) |  |
| }   [msi](#aa489bd4eedf57431c4fbff4aa80255c8) |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [spi](#a6502c409d05ea42bbf0544602c1c140f) |  |
| }   [spi](#a42e318f72ca9810f5f34b8671ffad088) |
| } | [u](#a57facd116b7981a353636a698b821062) |

## Field Documentation

## [◆ ](#aa73344f449c2f794c1b07d81bc5e2613)bus

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xen\_domctl\_bind\_pt\_irq::bus |
| --- |

## [◆ ](#a7f1d36a2965de0d35e9e86f3825218af)device

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xen\_domctl\_bind\_pt\_irq::device |
| --- |

## [◆ ](#abd99cec39f010ebbdf6e5cd0ba3c3676)gflags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_bind\_pt\_irq::gflags |
| --- |

## [◆ ](#a4fb5cf50743c77a22b7fe95acef43129)gtable

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) xen\_domctl\_bind\_pt\_irq::gtable |
| --- |

## [◆ ](#a571d737fec6ba58131b433643edc8a70)gvec

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xen\_domctl\_bind\_pt\_irq::gvec |
| --- |

## [◆ ](#aac07dc02b436ae553cd73503baa4372c)intx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xen\_domctl\_bind\_pt\_irq::intx |
| --- |

## [◆ ](#aa1085a60b7c25661b85f7c9524b754d7)irq\_type

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_bind\_pt\_irq::irq\_type |
| --- |

## [◆ ](#a50399e43aa64a2294e134cb3db16b6a0)[struct]

| struct { ... } xen\_domctl\_bind\_pt\_irq::isa |
| --- |

## [◆ ](#a53e7af42e7181983b80fcfedd8d709ab)isa\_irq

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xen\_domctl\_bind\_pt\_irq::isa\_irq |
| --- |

## [◆ ](#ac7e169794a1268053698ea63689fb953)machine\_irq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_bind\_pt\_irq::machine\_irq |
| --- |

## [◆ ](#aa489bd4eedf57431c4fbff4aa80255c8)[struct]

| struct { ... } xen\_domctl\_bind\_pt\_irq::msi |
| --- |

## [◆ ](#afd2db2c0861d6098c7ff94aa094450cc)[struct]

| struct { ... } xen\_domctl\_bind\_pt\_irq::pci |
| --- |

## [◆ ](#a42e318f72ca9810f5f34b8671ffad088)[struct] [1/2]

| struct { ... } xen\_domctl\_bind\_pt\_irq::spi |
| --- |

## [◆ ](#a6502c409d05ea42bbf0544602c1c140f)spi [2/2]

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) xen\_domctl\_bind\_pt\_irq::spi |
| --- |

## [◆ ](#a57facd116b7981a353636a698b821062)[union]

| union { ... } xen\_domctl\_bind\_pt\_irq::u |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[domctl.h](public_2domctl_8h_source.md)

- [xen\_domctl\_bind\_pt\_irq](structxen__domctl__bind__pt__irq.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
