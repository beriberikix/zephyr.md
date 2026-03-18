---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ipc__service_8h.html
original_path: doxygen/html/ipc__service_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_service.h File Reference

`#include <[stdio.h](stdio_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](ipc__service_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ipc\_service\_cb](structipc__service__cb.md) |
|  | Event callback structure. [More...](structipc__service__cb.md#details) |
| struct | [ipc\_ept](structipc__ept.md) |
|  | Endpoint instance. [More...](structipc__ept.md#details) |
| struct | [ipc\_ept\_cfg](structipc__ept__cfg.md) |
|  | Endpoint configuration structure. [More...](structipc__ept__cfg.md#details) |

| Functions | |
| --- | --- |
| int | [ipc\_service\_open\_instance](group__ipc__service__api.md#gafef0b817299aedc870a004ab223bd20a) (const struct [device](structdevice.md) \*instance) |
|  | Open an instance. |
| int | [ipc\_service\_close\_instance](group__ipc__service__api.md#ga78c837d30cfd8989efe63e0a397148a7) (const struct [device](structdevice.md) \*instance) |
|  | Close an instance. |
| int | [ipc\_service\_register\_endpoint](group__ipc__service__api.md#gabfb8bab2e2e8cfe8908a050d4844666b) (const struct [device](structdevice.md) \*instance, struct [ipc\_ept](structipc__ept.md) \*ept, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*cfg) |
|  | Register IPC endpoint onto an instance. |
| int | [ipc\_service\_deregister\_endpoint](group__ipc__service__api.md#ga35c788240922fbca7b49af265100b68b) (struct [ipc\_ept](structipc__ept.md) \*ept) |
|  | Deregister an IPC endpoint from its instance. |
| int | [ipc\_service\_send](group__ipc__service__api.md#gac002253b7436902c6a3e0c93933d23fc) (struct [ipc\_ept](structipc__ept.md) \*ept, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send data using given IPC endpoint. |
| int | [ipc\_service\_get\_tx\_buffer\_size](group__ipc__service__api.md#ga5bcce96a208b4282e3eceb6e0ff451e4) (struct [ipc\_ept](structipc__ept.md) \*ept) |
|  | Get the TX buffer size. |
| int | [ipc\_service\_get\_tx\_buffer](group__ipc__service__api.md#gab2371bd26ad85b5dffac3b4000e51191) (struct [ipc\_ept](structipc__ept.md) \*ept, void \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*size, [k\_timeout\_t](structk__timeout__t.md) wait) |
|  | Get an empty TX buffer to be sent using [ipc\_service\_send\_nocopy](group__ipc__service__api.md#ga72aa5da1530908230478c49b5a012dc1 "ipc_service_send_nocopy"). |
| int | [ipc\_service\_drop\_tx\_buffer](group__ipc__service__api.md#ga3eb7168f73f5bc45fdced3af6d374860) (struct [ipc\_ept](structipc__ept.md) \*ept, const void \*data) |
|  | Drop and release a TX buffer. |
| int | [ipc\_service\_send\_nocopy](group__ipc__service__api.md#ga72aa5da1530908230478c49b5a012dc1) (struct [ipc\_ept](structipc__ept.md) \*ept, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send data in a TX buffer reserved by [ipc\_service\_get\_tx\_buffer](group__ipc__service__api.md#gab2371bd26ad85b5dffac3b4000e51191 "ipc_service_get_tx_buffer") using the given IPC endpoint. |
| int | [ipc\_service\_hold\_rx\_buffer](group__ipc__service__api.md#gadd957653c3e2bc32c494a9d643c0a0bd) (struct [ipc\_ept](structipc__ept.md) \*ept, void \*data) |
|  | Holds the RX buffer for usage outside the receive callback. |
| int | [ipc\_service\_release\_rx\_buffer](group__ipc__service__api.md#gaf4fd99716e7c83006a76f7f1bc85f228) (struct [ipc\_ept](structipc__ept.md) \*ept, void \*data) |
|  | Release the RX buffer for future reuse. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [ipc\_service.h](ipc__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
