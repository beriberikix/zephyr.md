---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2bluetooth_8h.html
original_path: doxygen/html/drivers_2bluetooth_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bluetooth.h File Reference

Bluetooth HCI driver API.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/addr.h](addr_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci_vs.h](hci__vs_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](drivers_2bluetooth_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_hci\_setup\_params](structbt__hci__setup__params.md) |
| struct | [bt\_hci\_driver\_api](structbt__hci__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [BT\_DT\_HCI\_QUIRK\_OR](group__bt__hci__api.md#ga5e61116282ab2555f1dcd93c2858157e)(node\_id, prop, idx) |
| #define | [BT\_DT\_HCI\_QUIRKS\_GET](group__bt__hci__api.md#ga73fc76e779a3dd45a680b09063471887)(node\_id) |
| #define | [BT\_DT\_HCI\_QUIRKS\_INST\_GET](group__bt__hci__api.md#ga9e97337a538670bbc2dde4b35a6c8a25)(inst) |
| #define | [BT\_DT\_HCI\_NAME\_GET](group__bt__hci__api.md#gaf66891071ade556e5906e71f0f0d2678)(node\_id) |
| #define | [BT\_DT\_HCI\_NAME\_INST\_GET](group__bt__hci__api.md#gae14d26da17a9b761226f9c68537d4161)(inst) |
| #define | [BT\_DT\_HCI\_BUS\_GET](group__bt__hci__api.md#ga766eaafe5d88d9d1efa0b3f09a334fc8)(node\_id) |
| #define | [BT\_DT\_HCI\_BUS\_INST\_GET](group__bt__hci__api.md#gafb7922cf9937229bb75ab7b4fd7c37bb)(inst) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed)) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf) |

| Enumerations | |
| --- | --- |
| enum | { [BT\_HCI\_QUIRK\_NO\_RESET](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1) = BIT(0) , [BT\_HCI\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2) = BIT(1) } |
| enum | [bt\_hci\_bus](group__bt__hci__api.md#ga82f70de5f5df8c14fea7440410431a49) {     [BT\_HCI\_BUS\_VIRTUAL](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab) = 0 , [BT\_HCI\_BUS\_USB](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a34115533231b4abe577c75e9e308ef7f) = 1 , [BT\_HCI\_BUS\_PCCARD](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a67e2e3bbbcbc08ea57819dd8c83bae61) = 2 , [BT\_HCI\_BUS\_UART](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a9318109c873bfc7411ac35c87042c604) = 3 ,     [BT\_HCI\_BUS\_RS232](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49accd587417c6e531be0c6f2b3cfe4b4fe) = 4 , [BT\_HCI\_BUS\_PCI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aba69a4fa7ba0d2ce97a193ef80bc7196) = 5 , [BT\_HCI\_BUS\_SDIO](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49ae0ff096a7460128bc97195faf3fab0c4) = 6 , [BT\_HCI\_BUS\_SPI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a8959ae675c1362e10d0125116f691530) = 7 ,     [BT\_HCI\_BUS\_I2C](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aeba46b1b3c164a6ac5b6ca71ba448a98) = 8 , [BT\_HCI\_BUS\_IPM](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a42bdfecd1d9941977338d6b4d8a5a86b) = 9   } |
|  | Possible values for the 'bus' member of the [bt\_hci\_driver](structbt__hci__driver.md "Abstraction which represents the HCI transport to the controller.") struct. [More...](group__bt__hci__api.md#ga82f70de5f5df8c14fea7440410431a49) |

| Functions | |
| --- | --- |
| static int | [bt\_hci\_open](group__bt__hci__api.md#gac744c98801cea5afd13d6774154e71c8) (const struct [device](structdevice.md) \*dev, [bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)) |
|  | Open the HCI transport. |
| static int | [bt\_hci\_close](group__bt__hci__api.md#gad187f0aff959a4756b281aa33d1b4394) (const struct [device](structdevice.md) \*dev) |
|  | Close the HCI transport. |
| static int | [bt\_hci\_send](group__bt__hci__api.md#ga64079b6f03479561c1c7d09b3af81ede) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send HCI buffer to controller. |
| static int | [bt\_hci\_setup](group__bt__hci__api.md#ga45ce7bf5fe86f5fff3d8838d247b1d47) (const struct [device](structdevice.md) \*dev, struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*params) |
|  | HCI vendor-specific setup. |
| int | [bt\_hci\_transport\_setup](#add813c1343955a7bb95135eb0fbe9cd5) (const struct [device](structdevice.md) \*dev) |
|  | Setup the HCI transport, which usually means to reset the Bluetooth IC. |
| int | [bt\_hci\_transport\_teardown](#ae29dbf165252ddf9085c7387706fd09c) (const struct [device](structdevice.md) \*dev) |
|  | Teardown the HCI transport. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_evt\_create](#a362df79e2f782159f7e85d63817421bb) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len) |
|  | Allocate an HCI event buffer. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_cmd\_complete\_create](#a8ab7dc7d38f3bc7be72e34d7a9f14212) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plen) |
|  | Allocate an HCI Command Complete event buffer. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_cmd\_status\_create](#ab6b790e6dd0e8251d6cf10b0a7cce5f7) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Allocate an HCI Command Status event buffer. |

## Detailed Description

Bluetooth HCI driver API.

Copyright (c) 2024 Johan Hedberg

SPDX-License-Identifier: Apache-2.0

## Function Documentation

## [◆ ](#a8ab7dc7d38f3bc7be72e34d7a9f14212)bt\_hci\_cmd\_complete\_create()

| struct [net\_buf](structnet__buf.md) \* bt\_hci\_cmd\_complete\_create | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *op*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *plen* ) |

Allocate an HCI Command Complete event buffer.

This function allocates a new buffer for HCI Command Complete event. It is given the OpCode (encoded e.g. using the BT\_OP macro) and the total length of the parameters. Upon successful return the buffer is ready to have the parameters encoded into it.

Parameters
:   | op | HCI command OpCode. |
    | --- | --- |
    | plen | Length of command parameters. |

Returns
:   Newly allocated buffer.

## [◆ ](#ab6b790e6dd0e8251d6cf10b0a7cce5f7)bt\_hci\_cmd\_status\_create()

| struct [net\_buf](structnet__buf.md) \* bt\_hci\_cmd\_status\_create | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *op*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *status* ) |

Allocate an HCI Command Status event buffer.

This function allocates a new buffer for HCI Command Status event. It is given the OpCode (encoded e.g. using the BT\_OP macro) and the status code. Upon successful return the buffer is ready to have the parameters encoded into it.

Parameters
:   | op | HCI command OpCode. |
    | --- | --- |
    | status | Status code. |

Returns
:   Newly allocated buffer.

## [◆ ](#a362df79e2f782159f7e85d63817421bb)bt\_hci\_evt\_create()

| struct [net\_buf](structnet__buf.md) \* bt\_hci\_evt\_create | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *evt*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len* ) |

Allocate an HCI event buffer.

This function allocates a new buffer for an HCI event. It is given the event code and the total length of the parameters. Upon successful return the buffer is ready to have the parameters encoded into it.

Parameters
:   | evt | HCI event OpCode. |
    | --- | --- |
    | len | Length of event parameters. |

Returns
:   Newly allocated buffer.

## [◆ ](#add813c1343955a7bb95135eb0fbe9cd5)bt\_hci\_transport\_setup()

| int bt\_hci\_transport\_setup | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Setup the HCI transport, which usually means to reset the Bluetooth IC.

Note
:   A weak version of this function is included in the H4 driver, so defining it is optional per board.

Parameters
:   | dev | The device structure for the bus connecting to the IC |
    | --- | --- |

Returns
:   0 on success, negative error value on failure

## [◆ ](#ae29dbf165252ddf9085c7387706fd09c)bt\_hci\_transport\_teardown()

| int bt\_hci\_transport\_teardown | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Teardown the HCI transport.

Note
:   A weak version of this function is included in the IPC driver, so defining it is optional. NRF5340 includes support to put network core in reset state.

Parameters
:   | dev | The device structure for the bus connecting to the IC |
    | --- | --- |

Returns
:   0 on success, negative error value on failure

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [bluetooth.h](drivers_2bluetooth_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
