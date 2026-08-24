---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvirtio__driver__api.html
original_path: doxygen/html/structvirtio__driver__api.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtio\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Virtio Interface](group__virtio__interface.md)

Virtio api structure.
[More...](#details)

`#include <[zephyr/drivers/virtio.h](virtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [virtq](structvirtq.md) \*(\* | [get\_virtqueue](#a49fb281829e12fc226e6e2e3cdf47b36) )(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx) |
| void(\* | [notify\_virtqueue](#a22eb11370ec5ea6a0f91334ae1ccff02) )(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx) |
| void \*(\* | [get\_device\_specific\_config](#a7add58b2a488e662443d99b5ef12aace) )(const struct [device](structdevice.md) \*dev) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [read\_device\_feature\_bit](#a6f324b95d6edcd044bf44734ec6897b9) )(const struct [device](structdevice.md) \*dev, int bit) |
| int(\* | [write\_driver\_feature\_bit](#af6683e8641684e1cc206d1fde6bdb727) )(const struct [device](structdevice.md) \*dev, int bit, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
| int(\* | [commit\_feature\_bits](#a8f39c335de27446a54ca2bea8d822546) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [init\_virtqueues](#aeffc9d53ed7bca3ffd7467d3bcbfaf65) )(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_queues, [virtio\_enumerate\_queues](group__virtio__interface.md#gac66779305009c3896eff113f680c29c4) cb, void \*opaque) |
| void(\* | [finalize\_init](#a1f9e9ce08443a6ea748ed52bc457bce4) )(const struct [device](structdevice.md) \*dev) |

## Detailed Description

Virtio api structure.

## Field Documentation

## [◆ ](#a8f39c335de27446a54ca2bea8d822546)commit\_feature\_bits

| int(\* virtio\_driver\_api::commit\_feature\_bits) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a1f9e9ce08443a6ea748ed52bc457bce4)finalize\_init

| void(\* virtio\_driver\_api::finalize\_init) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a7add58b2a488e662443d99b5ef12aace)get\_device\_specific\_config

| void \*(\* virtio\_driver\_api::get\_device\_specific\_config) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a49fb281829e12fc226e6e2e3cdf47b36)get\_virtqueue

| struct [virtq](structvirtq.md) \*(\* virtio\_driver\_api::get\_virtqueue) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx) |
| --- |

## [◆ ](#aeffc9d53ed7bca3ffd7467d3bcbfaf65)init\_virtqueues

| int(\* virtio\_driver\_api::init\_virtqueues) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_queues, [virtio\_enumerate\_queues](group__virtio__interface.md#gac66779305009c3896eff113f680c29c4) cb, void \*opaque) |
| --- |

## [◆ ](#a22eb11370ec5ea6a0f91334ae1ccff02)notify\_virtqueue

| void(\* virtio\_driver\_api::notify\_virtqueue) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx) |
| --- |

## [◆ ](#a6f324b95d6edcd044bf44734ec6897b9)read\_device\_feature\_bit

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* virtio\_driver\_api::read\_device\_feature\_bit) (const struct [device](structdevice.md) \*dev, int bit) |
| --- |

## [◆ ](#af6683e8641684e1cc206d1fde6bdb727)write\_driver\_feature\_bit

| int(\* virtio\_driver\_api::write\_driver\_feature\_bit) (const struct [device](structdevice.md) \*dev, int bit, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[virtio.h](virtio_8h_source.md)

- [virtio\_driver\_api](structvirtio__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
