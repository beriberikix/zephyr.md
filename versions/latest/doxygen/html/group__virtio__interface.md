---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__virtio__interface.html
original_path: doxygen/html/group__virtio__interface.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Virtio Interface

[Device Driver APIs](group__io__interfaces.md)

Virtio Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Virtqueue Interface](group__virtqueue__interface.md) |
|  | Virtqueue Interface. |

| Data Structures | |
| --- | --- |
| struct | [virtio\_driver\_api](structvirtio__driver__api.md) |
|  | Virtio api structure. [More...](structvirtio__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* | [virtio\_enumerate\_queues](#gac66779305009c3896eff113f680c29c4)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_queue\_size, void \*opaque) |
|  | Callback used during virtqueue enumeration. |

| Functions | |
| --- | --- |
| static struct [virtq](structvirtq.md) \* | [virtio\_get\_virtqueue](#ga4c1e58e5e34cb40f0a420a52767bff27) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx) |
|  | Returns virtqueue at given idx. |
| static void | [virtio\_notify\_virtqueue](#gada51c40981fcdf232b571e1a11dc3cee) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx) |
|  | Notifies virtqueue. |
| static void \* | [virtio\_get\_device\_specific\_config](#ga24987fd9a7603824baed470e4b0ef4d0) (const struct [device](structdevice.md) \*dev) |
|  | Returns device specific config. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [virtio\_read\_device\_feature\_bit](#ga55be5a1c2dc457bb1d44b0c302bfb7a8) (const struct [device](structdevice.md) \*dev, int bit) |
|  | Returns feature bit offered by virtio device. |
| static int | [virtio\_write\_driver\_feature\_bit](#gab920f8dfee1139585f6af6b22c340912) (const struct [device](structdevice.md) \*dev, int bit, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
|  | Sets feature bit. |
| static int | [virtio\_commit\_feature\_bits](#ga7d29735da898548661844356fef966e9) (const struct [device](structdevice.md) \*dev) |
|  | Commits feature bits. |
| static int | [virtio\_init\_virtqueues](#gaf8fde0107ed6da7eb621f334f478666e) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_queues, [virtio\_enumerate\_queues](#gac66779305009c3896eff113f680c29c4) cb, void \*opaque) |
|  | Initializes virtqueues. |
| static void | [virtio\_finalize\_init](#ga3ce7e3833b19210d47e563995c39087d) (const struct [device](structdevice.md) \*dev) |
|  | Finalizes initialization of the virtio device. |

## Detailed Description

Virtio Interface.

## Typedef Documentation

## [◆ ](#gac66779305009c3896eff113f680c29c4)virtio\_enumerate\_queues

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* virtio\_enumerate\_queues) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_queue\_size, void \*opaque) |
| --- |

`#include <[zephyr/drivers/virtio.h](virtio_8h.md)>`

Callback used during virtqueue enumeration.

Parameters
:   | queue\_idx | index of currently inspected queue |
    | --- | --- |
    | max\_queue\_size | maximum permitted size of currently inspected queue |
    | opaque | pointer to user provided data |

Returns
:   the size of currently inspected virtqueue we want to set

## Function Documentation

## [◆ ](#ga7d29735da898548661844356fef966e9)virtio\_commit\_feature\_bits()

| | int virtio\_commit\_feature\_bits | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/virtio.h](virtio_8h.md)>`

Commits feature bits.

Parameters
:   | dev | virtio device it operates on |
    | --- | --- |

Returns
:   0 on success or negative error code on failure

## [◆ ](#ga3ce7e3833b19210d47e563995c39087d)virtio\_finalize\_init()

| | void virtio\_finalize\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/virtio.h](virtio_8h.md)>`

Finalizes initialization of the virtio device.

Parameters
:   | dev | virtio device it operates on |
    | --- | --- |

## [◆ ](#ga24987fd9a7603824baed470e4b0ef4d0)virtio\_get\_device\_specific\_config()

| | void \* virtio\_get\_device\_specific\_config | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/virtio.h](virtio_8h.md)>`

Returns device specific config.

Parameters
:   | dev | virtio device it operates on |
    | --- | --- |

Returns
:   pointer to the device specific config or NULL if its not present

## [◆ ](#ga4c1e58e5e34cb40f0a420a52767bff27)virtio\_get\_virtqueue()

| | struct [virtq](structvirtq.md) \* virtio\_get\_virtqueue | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *queue\_idx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/virtio.h](virtio_8h.md)>`

Returns virtqueue at given idx.

Parameters
:   | dev | virtio device it operates on |
    | --- | --- |
    | queue\_idx | index of virtqueue to get |

Returns
:   pointer to virtqueue or NULL if not present

## [◆ ](#gaf8fde0107ed6da7eb621f334f478666e)virtio\_init\_virtqueues()

| | int virtio\_init\_virtqueues | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_queues*, | |  |  | [virtio\_enumerate\_queues](#gac66779305009c3896eff113f680c29c4) | *cb*, | |  |  | void \* | *opaque* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/virtio.h](virtio_8h.md)>`

Initializes virtqueues.

Parameters
:   | dev | virtio device it operates on |
    | --- | --- |
    | num\_queues | number of queues to initialize |
    | cb | callback called for each available virtqueue |
    | opaque | pointer to user provided data that will be passed to the callback |

Returns
:   0 on success or negative error code on failure

## [◆ ](#gada51c40981fcdf232b571e1a11dc3cee)virtio\_notify\_virtqueue()

| | void virtio\_notify\_virtqueue | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *queue\_idx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/virtio.h](virtio_8h.md)>`

Notifies virtqueue.

Note that according to spec 2.7.13.3 the device may access the buffers as soon as the avail->idx is increased, which is done by virtq\_add\_buffer\_chain, so the device may access the buffers even without notifying it with virtio\_notify\_virtqueue

Parameters
:   | dev | virtio device it operates on |
    | --- | --- |
    | queue\_idx | virtqueue to be notified |

## [◆ ](#ga55be5a1c2dc457bb1d44b0c302bfb7a8)virtio\_read\_device\_feature\_bit()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) virtio\_read\_device\_feature\_bit | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | int | *bit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/virtio.h](virtio_8h.md)>`

Returns feature bit offered by virtio device.

Parameters
:   | dev | virtio device it operates on |
    | --- | --- |
    | bit | selected bit |

Returns
:   value of the offered feature bit

## [◆ ](#gab920f8dfee1139585f6af6b22c340912)virtio\_write\_driver\_feature\_bit()

| | int virtio\_write\_driver\_feature\_bit | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | int | *bit*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/virtio.h](virtio_8h.md)>`

Sets feature bit.

Parameters
:   | dev | virtio device it operates on |
    | --- | --- |
    | bit | selected bit |
    | value | bit value to write |

Returns
:   0 on success or negative error code on failure

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
