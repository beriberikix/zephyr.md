---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/virtio_8h.html
original_path: doxygen/html/virtio_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtio.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include "[virtio/virtqueue.h](virtqueue_8h_source.md)"`

[Go to the source code of this file.](virtio_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [virtio\_driver\_api](structvirtio__driver__api.md) |
|  | Virtio api structure. [More...](structvirtio__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* | [virtio\_enumerate\_queues](group__virtio__interface.md#gac66779305009c3896eff113f680c29c4)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_queue\_size, void \*opaque) |
|  | Callback used during virtqueue enumeration. |

| Functions | |
| --- | --- |
| static struct [virtq](structvirtq.md) \* | [virtio\_get\_virtqueue](group__virtio__interface.md#ga4c1e58e5e34cb40f0a420a52767bff27) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx) |
|  | Returns virtqueue at given idx. |
| static void | [virtio\_notify\_virtqueue](group__virtio__interface.md#gada51c40981fcdf232b571e1a11dc3cee) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx) |
|  | Notifies virtqueue. |
| static void \* | [virtio\_get\_device\_specific\_config](group__virtio__interface.md#ga24987fd9a7603824baed470e4b0ef4d0) (const struct [device](structdevice.md) \*dev) |
|  | Returns device specific config. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [virtio\_read\_device\_feature\_bit](group__virtio__interface.md#ga55be5a1c2dc457bb1d44b0c302bfb7a8) (const struct [device](structdevice.md) \*dev, int bit) |
|  | Returns feature bit offered by virtio device. |
| static int | [virtio\_write\_driver\_feature\_bit](group__virtio__interface.md#gab920f8dfee1139585f6af6b22c340912) (const struct [device](structdevice.md) \*dev, int bit, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
|  | Sets feature bit. |
| static int | [virtio\_commit\_feature\_bits](group__virtio__interface.md#ga7d29735da898548661844356fef966e9) (const struct [device](structdevice.md) \*dev) |
|  | Commits feature bits. |
| static int | [virtio\_init\_virtqueues](group__virtio__interface.md#gaf8fde0107ed6da7eb621f334f478666e) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_queues, [virtio\_enumerate\_queues](group__virtio__interface.md#gac66779305009c3896eff113f680c29c4) cb, void \*opaque) |
|  | Initializes virtqueues. |
| static void | [virtio\_finalize\_init](group__virtio__interface.md#ga3ce7e3833b19210d47e563995c39087d) (const struct [device](structdevice.md) \*dev) |
|  | Finalizes initialization of the virtio device. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [virtio.h](virtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
