---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dsa_8h.html
original_path: doxygen/html/dsa_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dsa.h File Reference

DSA definitions and handlers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`

[Go to the source code of this file.](dsa_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [dsa\_slave\_config](structdsa__slave__config.md) |
|  | Structure to provide mac address for each LAN interface. [More...](structdsa__slave__config.md#details) |

| Typedefs | |
| --- | --- |
| typedef enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* | [dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | DSA (MGMT) Receive packet callback. |
| typedef int(\* | [dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b)) (const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Pointer to master interface send function. |

| Functions | |
| --- | --- |
| int | [dsa\_tx](group__DSA.md#ga381fae2a3cf652db81db6e64d9aea62a) (const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | DSA generic transmit function. |
| int | [dsa\_register\_recv\_callback](group__DSA.md#gaee78adf88b0598611097e42ff94e9c52) (struct [net\_if](structnet__if.md) \*iface, [dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa) cb) |
|  | Register DSA Rx callback functions. |
| struct [net\_if](structnet__if.md) \* | [dsa\_net\_recv](group__DSA.md#ga01a24efc07ef0aa4125b91781c3039f3) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*\*pkt) |
|  | Set DSA interface to packet. |
| int | [dsa\_register\_master\_tx](group__DSA.md#ga676bff9b468696e2158bf5b14211fd27) (struct [net\_if](structnet__if.md) \*iface, [dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b) fn) |
|  | DSA helper function to register transmit function for master. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [dsa\_is\_port\_master](group__DSA.md#ga06ef38794a9ca3f7b8d3a32d2e1b2212) (struct [net\_if](structnet__if.md) \*iface) |
|  | DSA helper function to check if port is master. |
| struct [net\_if](structnet__if.md) \* | [dsa\_get\_slave\_port](group__DSA.md#ga6ee72f05ee1192ceb3f691d0fe007e13) (struct [net\_if](structnet__if.md) \*iface, int slave\_num) |
|  | Get network interface of a slave port. |
| int | [dsa\_switch\_read](group__DSA.md#ga131e095ddf546471952663e0ce836c59) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read from DSA switch register. |
| int | [dsa\_switch\_write](group__DSA.md#gad6464601dcfccc77f06a0fed9ce80b0f) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write to DSA switch. |
| int | [dsa\_switch\_set\_mac\_table\_entry](group__DSA.md#ga742d4531fc59bfd37a229c2f25c84239) (struct [net\_if](structnet__if.md) \*iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fw\_port, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Write static MAC table entry. |
| int | [dsa\_switch\_get\_mac\_table\_entry](group__DSA.md#ga16767d0b80c684b32c33bbcc74d54488) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx) |
|  | Read static MAC table entry. |

## Detailed Description

DSA definitions and handlers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dsa.h](dsa_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
