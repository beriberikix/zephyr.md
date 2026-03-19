---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structxen__domctl.html
original_path: doxygen/html/structxen__domctl.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen\_domctl Struct Reference

`#include <[domctl.h](public_2domctl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cmd](#a833a895a5cd7ccaf368eb93cdcb1256b) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interface\_version](#a5bf335484906644f2c19d74c751ce1c4) |
| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | [domain](#a329ec329aec68c0faa2fa7e5d98c19ba) |
| union { |  |
| struct [xen\_domctl\_createdomain](structxen__domctl__createdomain.md)   [createdomain](#a111bee61edfc780955a58994fb3ba060) |  |
| struct [xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md)   [getdomaininfo](#aa6f45bbd91fb3d4283918f2ed374776d) |  |
| struct [xen\_domctl\_max\_mem](structxen__domctl__max__mem.md)   [max\_mem](#abc809477a658a0eb0a027b3606856c05) |  |
| struct [xen\_domctl\_vcpucontext](structxen__domctl__vcpucontext.md)   [vcpucontext](#a8bed0bb93553afca175a4fb897fae394) |  |
| struct [xen\_domctl\_max\_vcpus](structxen__domctl__max__vcpus.md)   [max\_vcpus](#ac464216bbb0403acef0e2c47e82b7731) |  |
| struct [xen\_domctl\_scheduler\_op](structxen__domctl__scheduler__op.md)   [scheduler\_op](#a412d944e92980210af7faf2686871793) |  |
| struct [xen\_domctl\_iomem\_permission](structxen__domctl__iomem__permission.md)   [iomem\_permission](#a41c0d47a8d5764d900d17a93ac1bd0e8) |  |
| struct [xen\_domctl\_address\_size](structxen__domctl__address__size.md)   [address\_size](#acf33e4ac5d83e482ded6d0fbaae75e19) |  |
| struct [xen\_domctl\_assign\_device](structxen__domctl__assign__device.md)   [assign\_device](#a2897a77b7aafa6bb91e8390a53027b00) |  |
| struct [xen\_domctl\_bind\_pt\_irq](structxen__domctl__bind__pt__irq.md)   [bind\_pt\_irq](#a07d169fc24c634686e986b9dc2ed0079) |  |
| struct [xen\_domctl\_memory\_mapping](structxen__domctl__memory__mapping.md)   [memory\_mapping](#a1baa090dcccc38080bb15b2643228972) |  |
| struct [xen\_domctl\_cacheflush](structxen__domctl__cacheflush.md)   [cacheflush](#a2b552007fb7ccfac707f3450ea1f6ae8) |  |
| struct [xen\_domctl\_paging\_mempool](structxen__domctl__paging__mempool.md)   [paging\_mempool](#a625a6b2e8ec8632898615588dba1090a) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [pad](#aee525828504105fcafbcc01ef08eff18) [128] |  |
| } | [u](#af36b8da93f1e4f58a4f079088ac982ec) |

## Field Documentation

## [◆ ](#acf33e4ac5d83e482ded6d0fbaae75e19)address\_size

| struct [xen\_domctl\_address\_size](structxen__domctl__address__size.md) xen\_domctl::address\_size |
| --- |

## [◆ ](#a2897a77b7aafa6bb91e8390a53027b00)assign\_device

| struct [xen\_domctl\_assign\_device](structxen__domctl__assign__device.md) xen\_domctl::assign\_device |
| --- |

## [◆ ](#a07d169fc24c634686e986b9dc2ed0079)bind\_pt\_irq

| struct [xen\_domctl\_bind\_pt\_irq](structxen__domctl__bind__pt__irq.md) xen\_domctl::bind\_pt\_irq |
| --- |

## [◆ ](#a2b552007fb7ccfac707f3450ea1f6ae8)cacheflush

| struct [xen\_domctl\_cacheflush](structxen__domctl__cacheflush.md) xen\_domctl::cacheflush |
| --- |

## [◆ ](#a833a895a5cd7ccaf368eb93cdcb1256b)cmd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl::cmd |
| --- |

## [◆ ](#a111bee61edfc780955a58994fb3ba060)createdomain

| struct [xen\_domctl\_createdomain](structxen__domctl__createdomain.md) xen\_domctl::createdomain |
| --- |

## [◆ ](#a329ec329aec68c0faa2fa7e5d98c19ba)domain

| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) xen\_domctl::domain |
| --- |

## [◆ ](#aa6f45bbd91fb3d4283918f2ed374776d)getdomaininfo

| struct [xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md) xen\_domctl::getdomaininfo |
| --- |

## [◆ ](#a5bf335484906644f2c19d74c751ce1c4)interface\_version

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl::interface\_version |
| --- |

## [◆ ](#a41c0d47a8d5764d900d17a93ac1bd0e8)iomem\_permission

| struct [xen\_domctl\_iomem\_permission](structxen__domctl__iomem__permission.md) xen\_domctl::iomem\_permission |
| --- |

## [◆ ](#abc809477a658a0eb0a027b3606856c05)max\_mem

| struct [xen\_domctl\_max\_mem](structxen__domctl__max__mem.md) xen\_domctl::max\_mem |
| --- |

## [◆ ](#ac464216bbb0403acef0e2c47e82b7731)max\_vcpus

| struct [xen\_domctl\_max\_vcpus](structxen__domctl__max__vcpus.md) xen\_domctl::max\_vcpus |
| --- |

## [◆ ](#a1baa090dcccc38080bb15b2643228972)memory\_mapping

| struct [xen\_domctl\_memory\_mapping](structxen__domctl__memory__mapping.md) xen\_domctl::memory\_mapping |
| --- |

## [◆ ](#aee525828504105fcafbcc01ef08eff18)pad

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xen\_domctl::pad[128] |
| --- |

## [◆ ](#a625a6b2e8ec8632898615588dba1090a)paging\_mempool

| struct [xen\_domctl\_paging\_mempool](structxen__domctl__paging__mempool.md) xen\_domctl::paging\_mempool |
| --- |

## [◆ ](#a412d944e92980210af7faf2686871793)scheduler\_op

| struct [xen\_domctl\_scheduler\_op](structxen__domctl__scheduler__op.md) xen\_domctl::scheduler\_op |
| --- |

## [◆ ](#af36b8da93f1e4f58a4f079088ac982ec)[union]

| union { ... } xen\_domctl::u |
| --- |

## [◆ ](#a8bed0bb93553afca175a4fb897fae394)vcpucontext

| struct [xen\_domctl\_vcpucontext](structxen__domctl__vcpucontext.md) xen\_domctl::vcpucontext |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[domctl.h](public_2domctl_8h_source.md)

- [xen\_domctl](structxen__domctl.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
