---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__hci__driver.html
original_path: doxygen/html/group__bt__hci__driver.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HCI drivers

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

HCI drivers.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_hci\_setup\_params](structbt__hci__setup__params.md) |
| struct | [bt\_hci\_driver](structbt__hci__driver.md) |
|  | Abstraction which represents the HCI transport to the controller. [More...](structbt__hci__driver.md#details) |

| Enumerations | |
| --- | --- |
| enum | { [BT\_QUIRK\_NO\_RESET](#gga8f5a83b514f6d2da7548c38f7c3c166ea18274691e4c0129f945e88304778a241) = BIT(0) , [BT\_QUIRK\_NO\_AUTO\_DLE](#gga8f5a83b514f6d2da7548c38f7c3c166ea7b8e6d2f5604015c92c623193b9fe1e4) = BIT(1) } |
| enum | [bt\_hci\_driver\_bus](#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) {     [BT\_HCI\_DRIVER\_BUS\_VIRTUAL](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa885401f44dae9e39caf4a4838b547db9) = 0 , [BT\_HCI\_DRIVER\_BUS\_USB](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efac2b08e3e52f795deabffd3638a421b68) = 1 , [BT\_HCI\_DRIVER\_BUS\_PCCARD](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa08bc821327d571bf9659eda7e06a5129) = 2 , [BT\_HCI\_DRIVER\_BUS\_UART](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa39c5fca0c61c99db6541d01fb55e41f4) = 3 ,     [BT\_HCI\_DRIVER\_BUS\_RS232](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa5790e933f10773e30da6c7b922a443fa) = 4 , [BT\_HCI\_DRIVER\_BUS\_PCI](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab4c130c7862cbbd6be7827b6462dab90) = 5 , [BT\_HCI\_DRIVER\_BUS\_SDIO](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab572fbb186634bc08a3bce457cf38c74) = 6 , [BT\_HCI\_DRIVER\_BUS\_SPI](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa49f2ba9eeaafa266d905a30b2caf015a) = 7 ,     [BT\_HCI\_DRIVER\_BUS\_I2C](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa0d8c310b05d2c982e8de720dbdc2d742) = 8 , [BT\_HCI\_DRIVER\_BUS\_IPM](#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa8473c5abdf2f5839c9df54fc00ee3800) = 9   } |
|  | Possible values for the 'bus' member of the [bt\_hci\_driver](structbt__hci__driver.md "Abstraction which represents the HCI transport to the controller.") struct. [More...](#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) |

| Functions | |
| --- | --- |
| int | [bt\_recv](#gaca80bc9dacc4fa44416bd545bd185ef7) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Receive data from the controller/HCI driver. |
| int | [bt\_hci\_driver\_register](#ga642d226772448dccbd14f2c287d687f0) (const struct [bt\_hci\_driver](structbt__hci__driver.md) \*drv) |
|  | Register a new HCI driver to the Bluetooth stack. |
| int | [bt\_hci\_transport\_setup](#gadd813c1343955a7bb95135eb0fbe9cd5) (const struct [device](structdevice.md) \*dev) |
|  | Setup the HCI transport, which usually means to reset the Bluetooth IC. |
| int | [bt\_hci\_transport\_teardown](#gae29dbf165252ddf9085c7387706fd09c) (const struct [device](structdevice.md) \*dev) |
|  | Teardown the HCI transport. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_evt\_create](#ga362df79e2f782159f7e85d63817421bb) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len) |
|  | Allocate an HCI event buffer. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_cmd\_complete\_create](#ga8ab7dc7d38f3bc7be72e34d7a9f14212) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plen) |
|  | Allocate an HCI Command Complete event buffer. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_cmd\_status\_create](#gab6b790e6dd0e8251d6cf10b0a7cce5f7) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Allocate an HCI Command Status event buffer. |

## Detailed Description

HCI drivers.

**[Deprecated](deprecated.md#_deprecated000010)**
:   This is the old HCI driver API. Drivers should use [Bluetooth HCI APIs](group__bt__hci__api.md "Bluetooth HCI APIs") instead.

## Enumeration Type Documentation

## [◆ ](#ga8f5a83b514f6d2da7548c38f7c3c166e)anonymous enum

| anonymous enum |
| --- |

`#include <[hci_driver.h](hci__driver_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_QUIRK\_NO\_RESET |  |
| BT\_QUIRK\_NO\_AUTO\_DLE |  |

## [◆ ](#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef)bt\_hci\_driver\_bus

| enum [bt\_hci\_driver\_bus](#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) |
| --- |

`#include <[hci_driver.h](hci__driver_8h.md)>`

Possible values for the 'bus' member of the [bt\_hci\_driver](structbt__hci__driver.md "Abstraction which represents the HCI transport to the controller.") struct.

| Enumerator | |
| --- | --- |
| BT\_HCI\_DRIVER\_BUS\_VIRTUAL |  |
| BT\_HCI\_DRIVER\_BUS\_USB |  |
| BT\_HCI\_DRIVER\_BUS\_PCCARD |  |
| BT\_HCI\_DRIVER\_BUS\_UART |  |
| BT\_HCI\_DRIVER\_BUS\_RS232 |  |
| BT\_HCI\_DRIVER\_BUS\_PCI |  |
| BT\_HCI\_DRIVER\_BUS\_SDIO |  |
| BT\_HCI\_DRIVER\_BUS\_SPI |  |
| BT\_HCI\_DRIVER\_BUS\_I2C |  |
| BT\_HCI\_DRIVER\_BUS\_IPM |  |

## Function Documentation

## [◆ ](#ga8ab7dc7d38f3bc7be72e34d7a9f14212)bt\_hci\_cmd\_complete\_create()

| struct [net\_buf](structnet__buf.md) \* bt\_hci\_cmd\_complete\_create | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *op*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *plen* ) |

`#include <[hci_driver.h](hci__driver_8h.md)>`

Allocate an HCI Command Complete event buffer.

This function allocates a new buffer for HCI Command Complete event. It is given the OpCode (encoded e.g. using the BT\_OP macro) and the total length of the parameters. Upon successful return the buffer is ready to have the parameters encoded into it.

Parameters
:   | op | Command OpCode. |
    | --- | --- |
    | plen | Length of command parameters. |

Returns
:   Newly allocated buffer.

## [◆ ](#gab6b790e6dd0e8251d6cf10b0a7cce5f7)bt\_hci\_cmd\_status\_create()

| struct [net\_buf](structnet__buf.md) \* bt\_hci\_cmd\_status\_create | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *op*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *status* ) |

`#include <[hci_driver.h](hci__driver_8h.md)>`

Allocate an HCI Command Status event buffer.

This function allocates a new buffer for HCI Command Status event. It is given the OpCode (encoded e.g. using the BT\_OP macro) and the status code. Upon successful return the buffer is ready to have the parameters encoded into it.

Parameters
:   | op | Command OpCode. |
    | --- | --- |
    | status | Status code. |

Returns
:   Newly allocated buffer.

## [◆ ](#ga642d226772448dccbd14f2c287d687f0)bt\_hci\_driver\_register()

| int bt\_hci\_driver\_register | ( | const struct [bt\_hci\_driver](structbt__hci__driver.md) \* | *drv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hci_driver.h](hci__driver_8h.md)>`

Register a new HCI driver to the Bluetooth stack.

This needs to be called before any application code runs. The [bt\_enable()](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b "Enable Bluetooth.") API will fail if there is no driver registered.

Parameters
:   | drv | A [bt\_hci\_driver](structbt__hci__driver.md "Abstraction which represents the HCI transport to the controller.") struct representing the driver. |
    | --- | --- |

Returns
:   0 on success or negative error number on failure.

**[Deprecated](deprecated.md#_deprecated000012)**
:   Use the new HCI driver interface instead: [Bluetooth HCI APIs](group__bt__hci__api.md "Bluetooth HCI APIs")

## [◆ ](#ga362df79e2f782159f7e85d63817421bb)bt\_hci\_evt\_create()

| struct [net\_buf](structnet__buf.md) \* bt\_hci\_evt\_create | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *evt*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len* ) |

`#include <[hci_driver.h](hci__driver_8h.md)>`

Allocate an HCI event buffer.

This function allocates a new buffer for an HCI event. It is given the event code and the total length of the parameters. Upon successful return the buffer is ready to have the parameters encoded into it.

Parameters
:   | evt | Event OpCode. |
    | --- | --- |
    | len | Length of event parameters. |

Returns
:   Newly allocated buffer.

## [◆ ](#gadd813c1343955a7bb95135eb0fbe9cd5)bt\_hci\_transport\_setup()

| int bt\_hci\_transport\_setup | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hci_driver.h](hci__driver_8h.md)>`

Setup the HCI transport, which usually means to reset the Bluetooth IC.

Note
:   A weak version of this function is included in the H4 driver, so defining it is optional per board.

Parameters
:   | dev | The device structure for the bus connecting to the IC |
    | --- | --- |

Returns
:   0 on success, negative error value on failure

## [◆ ](#gae29dbf165252ddf9085c7387706fd09c)bt\_hci\_transport\_teardown()

| int bt\_hci\_transport\_teardown | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hci_driver.h](hci__driver_8h.md)>`

Teardown the HCI transport.

Note
:   A weak version of this function is included in the IPC driver, so defining it is optional. NRF5340 includes support to put network core in reset state.

Parameters
:   | dev | The device structure for the bus connecting to the IC |
    | --- | --- |

Returns
:   0 on success, negative error value on failure

## [◆ ](#gaca80bc9dacc4fa44416bd545bd185ef7)bt\_recv()

| int bt\_recv | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hci_driver.h](hci__driver_8h.md)>`

Receive data from the controller/HCI driver.

This is the main function through which the HCI driver provides the host with data from the controller. The buffer needs to have its type set with the help of [bt\_buf\_set\_type()](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec "Set the buffer type.") before calling this API.

Parameters
:   | buf | Network buffer containing data from the controller. |
    | --- | --- |

Returns
:   0 on success or negative error number on failure.

**[Deprecated](deprecated.md#_deprecated000011)**
:   Use the new HCI driver interface instead: [Bluetooth HCI APIs](group__bt__hci__api.md "Bluetooth HCI APIs")

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
