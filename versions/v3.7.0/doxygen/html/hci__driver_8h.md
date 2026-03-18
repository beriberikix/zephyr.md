---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hci__driver_8h.html
original_path: doxygen/html/hci__driver_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_driver.h File Reference

Bluetooth HCI driver API.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci_vs.h](hci__vs_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](hci__driver_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_hci\_setup\_params](structbt__hci__setup__params.md) |
| struct | [bt\_hci\_driver](structbt__hci__driver.md) |
|  | Abstraction which represents the HCI transport to the controller. [More...](structbt__hci__driver.md#details) |

| Enumerations | |
| --- | --- |
| enum | { [BT\_QUIRK\_NO\_RESET](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea18274691e4c0129f945e88304778a241) = BIT(0) , [BT\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea7b8e6d2f5604015c92c623193b9fe1e4) = BIT(1) } |
| enum | [bt\_hci\_driver\_bus](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) {     [BT\_HCI\_DRIVER\_BUS\_VIRTUAL](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa885401f44dae9e39caf4a4838b547db9) = 0 , [BT\_HCI\_DRIVER\_BUS\_USB](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efac2b08e3e52f795deabffd3638a421b68) = 1 , [BT\_HCI\_DRIVER\_BUS\_PCCARD](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa08bc821327d571bf9659eda7e06a5129) = 2 , [BT\_HCI\_DRIVER\_BUS\_UART](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa39c5fca0c61c99db6541d01fb55e41f4) = 3 ,     [BT\_HCI\_DRIVER\_BUS\_RS232](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa5790e933f10773e30da6c7b922a443fa) = 4 , [BT\_HCI\_DRIVER\_BUS\_PCI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab4c130c7862cbbd6be7827b6462dab90) = 5 , [BT\_HCI\_DRIVER\_BUS\_SDIO](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab572fbb186634bc08a3bce457cf38c74) = 6 , [BT\_HCI\_DRIVER\_BUS\_SPI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa49f2ba9eeaafa266d905a30b2caf015a) = 7 ,     [BT\_HCI\_DRIVER\_BUS\_I2C](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa0d8c310b05d2c982e8de720dbdc2d742) = 8 , [BT\_HCI\_DRIVER\_BUS\_IPM](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa8473c5abdf2f5839c9df54fc00ee3800) = 9   } |
|  | Possible values for the 'bus' member of the [bt\_hci\_driver](structbt__hci__driver.md "Abstraction which represents the HCI transport to the controller.") struct. [More...](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) |

| Functions | |
| --- | --- |
| int | [bt\_recv](group__bt__hci__driver.md#gaca80bc9dacc4fa44416bd545bd185ef7) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Receive data from the controller/HCI driver. |
| int | [bt\_hci\_driver\_register](group__bt__hci__driver.md#ga642d226772448dccbd14f2c287d687f0) (const struct [bt\_hci\_driver](structbt__hci__driver.md) \*drv) |
|  | Register a new HCI driver to the Bluetooth stack. |
| int | [bt\_hci\_transport\_setup](group__bt__hci__driver.md#gadd813c1343955a7bb95135eb0fbe9cd5) (const struct [device](structdevice.md) \*dev) |
|  | Setup the HCI transport, which usually means to reset the Bluetooth IC. |
| int | [bt\_hci\_transport\_teardown](group__bt__hci__driver.md#gae29dbf165252ddf9085c7387706fd09c) (const struct [device](structdevice.md) \*dev) |
|  | Teardown the HCI transport. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_evt\_create](group__bt__hci__driver.md#ga362df79e2f782159f7e85d63817421bb) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len) |
|  | Allocate an HCI event buffer. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_cmd\_complete\_create](group__bt__hci__driver.md#ga8ab7dc7d38f3bc7be72e34d7a9f14212) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plen) |
|  | Allocate an HCI Command Complete event buffer. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_cmd\_status\_create](group__bt__hci__driver.md#gab6b790e6dd0e8251d6cf10b0a7cce5f7) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Allocate an HCI Command Status event buffer. |

## Detailed Description

Bluetooth HCI driver API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [bluetooth](dir_95992648d5602e5c89adafd44bf19e08.md)
- [hci\_driver.h](hci__driver_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
