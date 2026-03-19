---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ipm_8h.html
original_path: doxygen/html/ipm_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipm.h File Reference

Generic low-level inter-processor mailbox communication API.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/ipm.h>`

[Go to the source code of this file.](ipm_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ipm\_driver\_api](structipm__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa)) (const struct [device](structdevice.md) \*ipmdev, void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, volatile void \*data) |
|  | Callback API for incoming IPM messages. |
| typedef int(\* | [ipm\_send\_t](group__ipm__interface.md#ga45fb35e92b26b04ed4c665d50912ff3b)) (const struct [device](structdevice.md) \*ipmdev, int wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const void \*data, int size) |
|  | Callback API to send IPM messages. |
| typedef int(\* | [ipm\_max\_data\_size\_get\_t](group__ipm__interface.md#ga34c3a4782175068eda6443c521094a03)) (const struct [device](structdevice.md) \*ipmdev) |
|  | Callback API to get maximum data size. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [ipm\_max\_id\_val\_get\_t](group__ipm__interface.md#gaa50f765662f9d1dbea75902211de7000)) (const struct [device](structdevice.md) \*ipmdev) |
|  | Callback API to get the ID's maximum value. |
| typedef void(\* | [ipm\_register\_callback\_t](group__ipm__interface.md#ga8f7b338aa9f5d4aa1c218db412da562b)) (const struct [device](structdevice.md) \*port, [ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa) cb, void \*user\_data) |
|  | Callback API upon registration. |
| typedef int(\* | [ipm\_set\_enabled\_t](group__ipm__interface.md#gab1faa1ebf47e2c12286bac0ce8be7784)) (const struct [device](structdevice.md) \*ipmdev, int enable) |
|  | Callback API upon enablement of interrupts. |
| typedef void(\* | [ipm\_complete\_t](group__ipm__interface.md#ga1aff2b36a9b7712a1fa743052282d440)) (const struct [device](structdevice.md) \*ipmdev) |
|  | Callback API upon command completion. |

| Functions | |
| --- | --- |
| int | [ipm\_send](group__ipm__interface.md#ga8f3fe21c1a4ffd3c38b67f81749af043) (const struct [device](structdevice.md) \*ipmdev, int wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const void \*data, int size) |
|  | Try to send a message over the IPM device. |
| static void | [ipm\_register\_callback](group__ipm__interface.md#ga557b15bc8a353483ca55888dba27493b) (const struct [device](structdevice.md) \*ipmdev, [ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa) cb, void \*user\_data) |
|  | Register a callback function for incoming messages. |
| int | [ipm\_max\_data\_size\_get](group__ipm__interface.md#ga0a11eecaa7254575ab6baf0783a18b5e) (const struct [device](structdevice.md) \*ipmdev) |
|  | Return the maximum number of bytes possible in an outbound message. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ipm\_max\_id\_val\_get](group__ipm__interface.md#ga168fd277b7819b639baa4e630c596a7f) (const struct [device](structdevice.md) \*ipmdev) |
|  | Return the maximum id value possible in an outbound message. |
| int | [ipm\_set\_enabled](group__ipm__interface.md#ga5884fa95cb38ddfe4493eb70dafebe8b) (const struct [device](structdevice.md) \*ipmdev, int enable) |
|  | Enable interrupts and callbacks for inbound channels. |
| void | [ipm\_complete](group__ipm__interface.md#ga53f785ecfac17b9fb2e5f3a9505c7fd2) (const struct [device](structdevice.md) \*ipmdev) |
|  | Signal asynchronous command completion. |

## Detailed Description

Generic low-level inter-processor mailbox communication API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ipm.h](ipm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
