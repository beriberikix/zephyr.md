---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__l2cap__br__endpoint.html
original_path: doxygen/html/structbt__l2cap__br__endpoint.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_l2cap\_br\_endpoint Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [L2CAP](group__bt__l2cap.md)

BREDR L2CAP Endpoint structure.
[More...](#details)

`#include <[zephyr/bluetooth/l2cap.h](l2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cid](#acbe4f6cc15bb20703fca53e7084b2ea7) |
|  | Endpoint Channel Identifier (CID). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mtu](#aaeb46128990fe08c926d34049bbc2d6a) |
|  | Endpoint Maximum Transmission Unit. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mode](#af49eacd8794e580adc285d95613547f6) |
|  | Endpoint Link Mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [optional](#af64e45ea279960b3db213c9ad3e1828c) |
|  | Whether Endpoint Link Mode is optional If the [optional](#af64e45ea279960b3db213c9ad3e1828c) is true, the [mode](#af49eacd8794e580adc285d95613547f6) could be changed according to the extended feature and peer configuration from L2CAP configuration response and request. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_transmit](#a8c66377adf1681079fa446b05eff7e8a) |
|  | Endpoint Maximum Transmit The field is used to set the max retransmission count. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ret\_timeout](#ae5cdb992cd40ce925863e05c7f647f5e) |
|  | Endpoint Retransmission Timeout The field is configured by @kconfig{BT\_L2CAP\_BR\_RET\_TIMEOUT} The field should be no more than the field [monitor\_timeout](#a4f272e96d31b00a3e50d8dcbc2303c57). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [monitor\_timeout](#a4f272e96d31b00a3e50d8dcbc2303c57) |
|  | Endpoint Monitor Timeout The field is configured by @kconfig{BT\_L2CAP\_BR\_MONITOR\_TIMEOUT}. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mps](#ab5789c43d09f18f89bffdd829af90a7b) |
|  | Endpoint Maximum PDU payload Size. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_window](#a2b27b7017ddc68d5b8a597d4be45074c) |
|  | Endpoint Maximum Window Size MAX supported window size is configured by @kconfig{BT\_L2CAP\_MAX\_WINDOW\_SIZE}. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fcs](#ac63ef5c2ae54fbcce9380a379a551595) |
|  | Endpoint FCS Type The value is defined as BT\_L2CAP\_BR\_FCS\_\* The default setting should be BT\_L2CAP\_BR\_FCS\_16BIT. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [extended\_control](#aba3184618ab6e8a3db1808041d3a0f8d) |
|  | Endpoint Extended Control. |

## Detailed Description

BREDR L2CAP Endpoint structure.

## Field Documentation

## [◆ ](#acbe4f6cc15bb20703fca53e7084b2ea7)cid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_endpoint::cid |
| --- |

Endpoint Channel Identifier (CID).

## [◆ ](#aba3184618ab6e8a3db1808041d3a0f8d)extended\_control

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_l2cap\_br\_endpoint::extended\_control |
| --- |

Endpoint Extended Control.

If this field is true, and both side support Extended Window size feature, the local will include extended window size option in configuration request packet.

## [◆ ](#ac63ef5c2ae54fbcce9380a379a551595)fcs

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_l2cap\_br\_endpoint::fcs |
| --- |

Endpoint FCS Type The value is defined as BT\_L2CAP\_BR\_FCS\_\* The default setting should be BT\_L2CAP\_BR\_FCS\_16BIT.

For FC and RET, the FCS type should be BT\_L2CAP\_BR\_FCS\_16BIT. For ERET and STREAM, the FCS type is optional. If the field is not default value, the local will include FCS option in configuration request packet if both side support FCS Option.

## [◆ ](#a8c66377adf1681079fa446b05eff7e8a)max\_transmit

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_l2cap\_br\_endpoint::max\_transmit |
| --- |

Endpoint Maximum Transmit The field is used to set the max retransmission count.

For RET, FC, and ERET, it should be not less 1. For STREAM, it should be 0.

## [◆ ](#a2b27b7017ddc68d5b8a597d4be45074c)max\_window

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_endpoint::max\_window |
| --- |

Endpoint Maximum Window Size MAX supported window size is configured by @kconfig{BT\_L2CAP\_MAX\_WINDOW\_SIZE}.

The field should be no more then CONFIG\_BT\_L2CAP\_MAX\_WINDOW\_SIZE.

## [◆ ](#af49eacd8794e580adc285d95613547f6)mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_l2cap\_br\_endpoint::mode |
| --- |

Endpoint Link Mode.

The value is defined as BT\_L2CAP\_BR\_LINK\_MODE\_\*

## [◆ ](#a4f272e96d31b00a3e50d8dcbc2303c57)monitor\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_endpoint::monitor\_timeout |
| --- |

Endpoint Monitor Timeout The field is configured by @kconfig{BT\_L2CAP\_BR\_MONITOR\_TIMEOUT}.

## [◆ ](#ab5789c43d09f18f89bffdd829af90a7b)mps

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_endpoint::mps |
| --- |

Endpoint Maximum PDU payload Size.

## [◆ ](#aaeb46128990fe08c926d34049bbc2d6a)mtu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_endpoint::mtu |
| --- |

Endpoint Maximum Transmission Unit.

## [◆ ](#af64e45ea279960b3db213c9ad3e1828c)optional

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_l2cap\_br\_endpoint::optional |
| --- |

Whether Endpoint Link Mode is optional If the [optional](#af64e45ea279960b3db213c9ad3e1828c) is true, the [mode](#af49eacd8794e580adc285d95613547f6) could be changed according to the extended feature and peer configuration from L2CAP configuration response and request.

Otherwise, if the channel configuration process does not meet the set mode, the L2CAP channel will be disconnected.

## [◆ ](#ae5cdb992cd40ce925863e05c7f647f5e)ret\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_endpoint::ret\_timeout |
| --- |

Endpoint Retransmission Timeout The field is configured by @kconfig{BT\_L2CAP\_BR\_RET\_TIMEOUT} The field should be no more than the field [monitor\_timeout](#a4f272e96d31b00a3e50d8dcbc2303c57).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[l2cap.h](l2cap_8h_source.md)

- [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
