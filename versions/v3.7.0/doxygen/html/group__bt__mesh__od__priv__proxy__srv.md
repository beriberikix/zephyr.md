---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__od__priv__proxy__srv.html
original_path: doxygen/html/group__bt__mesh__od__priv__proxy__srv.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh On-Demand Private GATT Proxy Server

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_SRV](#gaa3c6451144f696ef9e67494165283c41) |
|  | On-Demand Private Proxy Server model composition data entry. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaa3c6451144f696ef9e67494165283c41)BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_SRV

| #define BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_SRV |
| --- |

`#include <[od_priv_proxy_srv.h](od__priv__proxy__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_SRV](group__bt__mesh__sol__pdu__rpl__srv.md#gab32d54a2d8e7020107063b292a70f7b6), \

BT\_MESH\_MODEL\_CB([BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV](group__bt__mesh__access.md#gaddc0bd645180a57cb9cd36745b84f7a1), \

\_bt\_mesh\_od\_priv\_proxy\_srv\_op, NULL, NULL, \

&\_bt\_mesh\_od\_priv\_proxy\_srv\_cb)

[BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV](group__bt__mesh__access.md#gaddc0bd645180a57cb9cd36745b84f7a1)

#define BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV

Private Proxy Server.

**Definition** access.h:211

[BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_SRV](group__bt__mesh__sol__pdu__rpl__srv.md#gab32d54a2d8e7020107063b292a70f7b6)

#define BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_SRV

Solicitation PDU RPL Server model composition data entry.

**Definition** sol\_pdu\_rpl\_srv.h:23

On-Demand Private Proxy Server model composition data entry.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
