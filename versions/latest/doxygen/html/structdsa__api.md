---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structdsa__api.html
original_path: doxygen/html/structdsa__api.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dsa\_api Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Distributed Switch Architecture (DSA)](group__dsa__core.md)

Structure to provide DSA switch api callbacks - it is an augmented struct [ethernet\_api](structethernet__api.md "Ethernet L2 API operations.").
[More...](#details)

`#include <[zephyr/net/dsa_core.h](dsa__core_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_if](structnet__if.md) \*(\* | [recv](#af715363f30777917905a6e0b94059a8d) )(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | DSA helper callbacks. |
| struct [net\_pkt](structnet__pkt.md) \*(\* | [xmit](#aae906b6ec5bff5a7fbba1bf43312e71d) )(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Transmit packet on the user port with tagging. |
| int(\* | [port\_init](#a5117a72ebe047a23f18e168282b74a30) )(const struct [device](structdevice.md) \*dev) |
|  | Port init. |
| void(\* | [port\_phylink\_change](#a170af07de55d93fbdf82c89d2976d9ea) )(const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
|  | Port link change. |
| void(\* | [port\_generate\_random\_mac](#a40cc66f48a287011ef61a0767eceda5c) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac\_addr) |
|  | Port generates random mac address. |
| int(\* | [switch\_setup](#a3ad664182c5cee8786600d4dcd9bae1a) )(const struct [dsa\_switch\_context](structdsa__switch__context.md) \*dsa\_switch\_ctx) |
|  | Switch setup. |

## Detailed Description

Structure to provide DSA switch api callbacks - it is an augmented struct [ethernet\_api](structethernet__api.md "Ethernet L2 API operations.").

## Field Documentation

## [◆ ](#a40cc66f48a287011ef61a0767eceda5c)port\_generate\_random\_mac

| void(\* dsa\_api::port\_generate\_random\_mac) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac\_addr) |
| --- |

Port generates random mac address.

## [◆ ](#a5117a72ebe047a23f18e168282b74a30)port\_init

| int(\* dsa\_api::port\_init) (const struct [device](structdevice.md) \*dev) |
| --- |

Port init.

## [◆ ](#a170af07de55d93fbdf82c89d2976d9ea)port\_phylink\_change

| void(\* dsa\_api::port\_phylink\_change) (const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
| --- |

Port link change.

## [◆ ](#af715363f30777917905a6e0b94059a8d)recv

| struct [net\_if](structnet__if.md) \*(\* dsa\_api::recv) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

DSA helper callbacks.

Handle receive packet on conduit port for untagging and redirection

## [◆ ](#a3ad664182c5cee8786600d4dcd9bae1a)switch\_setup

| int(\* dsa\_api::switch\_setup) (const struct [dsa\_switch\_context](structdsa__switch__context.md) \*dsa\_switch\_ctx) |
| --- |

Switch setup.

## [◆ ](#aae906b6ec5bff5a7fbba1bf43312e71d)xmit

| struct [net\_pkt](structnet__pkt.md) \*(\* dsa\_api::xmit) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

Transmit packet on the user port with tagging.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dsa\_core.h](dsa__core_8h_source.md)

- [dsa\_api](structdsa__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
