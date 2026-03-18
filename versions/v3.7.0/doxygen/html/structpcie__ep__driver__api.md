---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpcie__ep__driver__api.html
original_path: doxygen/html/structpcie__ep__driver__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie\_ep\_driver\_api Struct Reference

`#include <[pcie_ep.h](pcie__ep_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [conf\_read](#aa5f508a7ab546c862f3aa65b480a45cc) )(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
| void(\* | [conf\_write](#acc1262a07dd079842c9c95708a2c6004) )(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
| int(\* | [map\_addr](#a444198e899d6a1353a7f8e3828f76643) )(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pcie\_addr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*mapped\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, enum [pcie\_ob\_mem\_type](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510b) ob\_mem\_type) |
| void(\* | [unmap\_addr](#a82d9766067a066d83b25390ad5903534) )(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr) |
| int(\* | [raise\_irq](#a83ef7d357174e55364660b53924b0017) )(const struct [device](structdevice.md) \*dev, enum [pci\_ep\_irq\_type](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800) irq\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num) |
| int(\* | [register\_reset\_cb](#adb5f2ea78cc5e9b0f61461a036c746eb) )(const struct [device](structdevice.md) \*dev, enum [pcie\_reset](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cd) reset, [pcie\_ep\_reset\_callback\_t](pcie__ep_8h.md#afcde72dd6977ee7de9ebf4146113f912) cb, void \*arg) |
| int(\* | [dma\_xfer](#ab816f2aad307f0b4a8181a7711d565bc) )(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) local\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, enum [xfer\_direction](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458) dir) |

## Field Documentation

## [◆ ](#aa5f508a7ab546c862f3aa65b480a45cc)conf\_read

| int(\* pcie\_ep\_driver\_api::conf\_read) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
| --- |

## [◆ ](#acc1262a07dd079842c9c95708a2c6004)conf\_write

| void(\* pcie\_ep\_driver\_api::conf\_write) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
| --- |

## [◆ ](#ab816f2aad307f0b4a8181a7711d565bc)dma\_xfer

| int(\* pcie\_ep\_driver\_api::dma\_xfer) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) local\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, enum [xfer\_direction](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458) dir) |
| --- |

## [◆ ](#a444198e899d6a1353a7f8e3828f76643)map\_addr

| int(\* pcie\_ep\_driver\_api::map\_addr) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pcie\_addr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*mapped\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, enum [pcie\_ob\_mem\_type](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510b) ob\_mem\_type) |
| --- |

## [◆ ](#a83ef7d357174e55364660b53924b0017)raise\_irq

| int(\* pcie\_ep\_driver\_api::raise\_irq) (const struct [device](structdevice.md) \*dev, enum [pci\_ep\_irq\_type](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800) irq\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num) |
| --- |

## [◆ ](#adb5f2ea78cc5e9b0f61461a036c746eb)register\_reset\_cb

| int(\* pcie\_ep\_driver\_api::register\_reset\_cb) (const struct [device](structdevice.md) \*dev, enum [pcie\_reset](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cd) reset, [pcie\_ep\_reset\_callback\_t](pcie__ep_8h.md#afcde72dd6977ee7de9ebf4146113f912) cb, void \*arg) |
| --- |

## [◆ ](#a82d9766067a066d83b25390ad5903534)unmap\_addr

| void(\* pcie\_ep\_driver\_api::unmap\_addr) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/pcie/endpoint/[pcie\_ep.h](pcie__ep_8h_source.md)

- [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
