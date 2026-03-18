---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__hci__api.html
original_path: doxygen/html/group__bt__hci__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth HCI APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth HCI APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_hci\_setup\_params](structbt__hci__setup__params.md) |
| struct | [bt\_hci\_driver\_api](structbt__hci__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [BT\_DT\_HCI\_QUIRK\_OR](#ga5e61116282ab2555f1dcd93c2858157e)(node\_id, prop, idx) |
| #define | [BT\_DT\_HCI\_QUIRKS\_GET](#ga73fc76e779a3dd45a680b09063471887)(node\_id) |
| #define | [BT\_DT\_HCI\_QUIRKS\_INST\_GET](#ga9e97337a538670bbc2dde4b35a6c8a25)(inst) |
| #define | [BT\_DT\_HCI\_NAME\_GET](#gaf66891071ade556e5906e71f0f0d2678)(node\_id) |
| #define | [BT\_DT\_HCI\_NAME\_INST\_GET](#gae14d26da17a9b761226f9c68537d4161)(inst) |
| #define | [BT\_DT\_HCI\_BUS\_GET](#ga766eaafe5d88d9d1efa0b3f09a334fc8)(node\_id) |
| #define | [BT\_DT\_HCI\_BUS\_INST\_GET](#gafb7922cf9937229bb75ab7b4fd7c37bb)(inst) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [bt\_hci\_recv\_t](#ga79b12569871b2b6c8420c245e9505aed)) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf) |

| Enumerations | |
| --- | --- |
| enum | { [BT\_HCI\_QUIRK\_NO\_RESET](#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1) = BIT(0) , [BT\_HCI\_QUIRK\_NO\_AUTO\_DLE](#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2) = BIT(1) } |
| enum | [bt\_hci\_bus](#ga82f70de5f5df8c14fea7440410431a49) {     [BT\_HCI\_BUS\_VIRTUAL](#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab) = 0 , [BT\_HCI\_BUS\_USB](#gga82f70de5f5df8c14fea7440410431a49a34115533231b4abe577c75e9e308ef7f) = 1 , [BT\_HCI\_BUS\_PCCARD](#gga82f70de5f5df8c14fea7440410431a49a67e2e3bbbcbc08ea57819dd8c83bae61) = 2 , [BT\_HCI\_BUS\_UART](#gga82f70de5f5df8c14fea7440410431a49a9318109c873bfc7411ac35c87042c604) = 3 ,     [BT\_HCI\_BUS\_RS232](#gga82f70de5f5df8c14fea7440410431a49accd587417c6e531be0c6f2b3cfe4b4fe) = 4 , [BT\_HCI\_BUS\_PCI](#gga82f70de5f5df8c14fea7440410431a49aba69a4fa7ba0d2ce97a193ef80bc7196) = 5 , [BT\_HCI\_BUS\_SDIO](#gga82f70de5f5df8c14fea7440410431a49ae0ff096a7460128bc97195faf3fab0c4) = 6 , [BT\_HCI\_BUS\_SPI](#gga82f70de5f5df8c14fea7440410431a49a8959ae675c1362e10d0125116f691530) = 7 ,     [BT\_HCI\_BUS\_I2C](#gga82f70de5f5df8c14fea7440410431a49aeba46b1b3c164a6ac5b6ca71ba448a98) = 8 , [BT\_HCI\_BUS\_IPM](#gga82f70de5f5df8c14fea7440410431a49a42bdfecd1d9941977338d6b4d8a5a86b) = 9   } |
|  | Possible values for the 'bus' member of the [bt\_hci\_driver](structbt__hci__driver.md "Abstraction which represents the HCI transport to the controller.") struct. [More...](#ga82f70de5f5df8c14fea7440410431a49) |

| Functions | |
| --- | --- |
| static int | [bt\_hci\_open](#gac744c98801cea5afd13d6774154e71c8) (const struct [device](structdevice.md) \*dev, [bt\_hci\_recv\_t](#ga79b12569871b2b6c8420c245e9505aed) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)) |
|  | Open the HCI transport. |
| static int | [bt\_hci\_close](#gad187f0aff959a4756b281aa33d1b4394) (const struct [device](structdevice.md) \*dev) |
|  | Close the HCI transport. |
| static int | [bt\_hci\_send](#ga64079b6f03479561c1c7d09b3af81ede) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send HCI buffer to controller. |
| static int | [bt\_hci\_setup](#ga45ce7bf5fe86f5fff3d8838d247b1d47) (const struct [device](structdevice.md) \*dev, struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*params) |
|  | HCI vendor-specific setup. |

## Detailed Description

Bluetooth HCI APIs.

Since
:   3.7

Version
:   0.2.0

## Macro Definition Documentation

## [◆ ](#ga766eaafe5d88d9d1efa0b3f09a334fc8)BT\_DT\_HCI\_BUS\_GET

| #define BT\_DT\_HCI\_BUS\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

**Value:**

[DT\_STRING\_TOKEN\_OR](group__devicetree-generic-prop.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c)(node\_id, [bt\_hci\_bus](#ga82f70de5f5df8c14fea7440410431a49), [BT\_HCI\_BUS\_VIRTUAL](#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab))

[bt\_hci\_bus](#ga82f70de5f5df8c14fea7440410431a49)

bt\_hci\_bus

Possible values for the 'bus' member of the bt\_hci\_driver struct.

**Definition** bluetooth.h:54

[BT\_HCI\_BUS\_VIRTUAL](#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab)

@ BT\_HCI\_BUS\_VIRTUAL

**Definition** bluetooth.h:55

[DT\_STRING\_TOKEN\_OR](group__devicetree-generic-prop.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c)

#define DT\_STRING\_TOKEN\_OR(node\_id, prop, default\_value)

Like DT\_STRING\_TOKEN(), but with a fallback to default\_value.

**Definition** devicetree.h:975

## [◆ ](#gafb7922cf9937229bb75ab7b4fd7c37bb)BT\_DT\_HCI\_BUS\_INST\_GET

| #define BT\_DT\_HCI\_BUS\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

**Value:**

[BT\_DT\_HCI\_BUS\_GET](#ga766eaafe5d88d9d1efa0b3f09a334fc8)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[BT\_DT\_HCI\_BUS\_GET](#ga766eaafe5d88d9d1efa0b3f09a334fc8)

#define BT\_DT\_HCI\_BUS\_GET(node\_id)

**Definition** bluetooth.h:79

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

## [◆ ](#gaf66891071ade556e5906e71f0f0d2678)BT\_DT\_HCI\_NAME\_GET

| #define BT\_DT\_HCI\_NAME\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

**Value:**

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, bt\_hci\_name, "HCI")

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:825

## [◆ ](#gae14d26da17a9b761226f9c68537d4161)BT\_DT\_HCI\_NAME\_INST\_GET

| #define BT\_DT\_HCI\_NAME\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

**Value:**

[BT\_DT\_HCI\_NAME\_GET](#gaf66891071ade556e5906e71f0f0d2678)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[BT\_DT\_HCI\_NAME\_GET](#gaf66891071ade556e5906e71f0f0d2678)

#define BT\_DT\_HCI\_NAME\_GET(node\_id)

**Definition** bluetooth.h:76

## [◆ ](#ga5e61116282ab2555f1dcd93c2858157e)BT\_DT\_HCI\_QUIRK\_OR

| #define BT\_DT\_HCI\_QUIRK\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

**Value:**

[DT\_STRING\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)(node\_id, prop, idx)

[DT\_STRING\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)

#define DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx)

Get an element out of a string-array property as a token.

**Definition** devicetree.h:1165

## [◆ ](#ga73fc76e779a3dd45a680b09063471887)BT\_DT\_HCI\_QUIRKS\_GET

| #define BT\_DT\_HCI\_QUIRKS\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, bt\_hci\_quirks), \

([DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)(node\_id, \

bt\_hci\_quirks, \

[BT\_DT\_HCI\_QUIRK\_OR](#ga5e61116282ab2555f1dcd93c2858157e), \

(|))), \

(0))

[BT\_DT\_HCI\_QUIRK\_OR](#ga5e61116282ab2555f1dcd93c2858157e)

#define BT\_DT\_HCI\_QUIRK\_OR(node\_id, prop, idx)

**Definition** bluetooth.h:67

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3479

[DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)

#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep)

Invokes fn for each element in the value of property prop with separator.

**Definition** devicetree.h:3103

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

## [◆ ](#ga9e97337a538670bbc2dde4b35a6c8a25)BT\_DT\_HCI\_QUIRKS\_INST\_GET

| #define BT\_DT\_HCI\_QUIRKS\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

**Value:**

[BT\_DT\_HCI\_QUIRKS\_GET](#ga73fc76e779a3dd45a680b09063471887)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[BT\_DT\_HCI\_QUIRKS\_GET](#ga73fc76e779a3dd45a680b09063471887)

#define BT\_DT\_HCI\_QUIRKS\_GET(node\_id)

**Definition** bluetooth.h:68

## Typedef Documentation

## [◆ ](#ga79b12569871b2b6c8420c245e9505aed)bt\_hci\_recv\_t

| typedef int(\* bt\_hci\_recv\_t) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga687e88a53cddde1d7cbf3057678e66c5)anonymous enum

| anonymous enum |
| --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_HCI\_QUIRK\_NO\_RESET |  |
| BT\_HCI\_QUIRK\_NO\_AUTO\_DLE |  |

## [◆ ](#ga82f70de5f5df8c14fea7440410431a49)bt\_hci\_bus

| enum [bt\_hci\_bus](#ga82f70de5f5df8c14fea7440410431a49) |
| --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

Possible values for the 'bus' member of the [bt\_hci\_driver](structbt__hci__driver.md "Abstraction which represents the HCI transport to the controller.") struct.

| Enumerator | |
| --- | --- |
| BT\_HCI\_BUS\_VIRTUAL |  |
| BT\_HCI\_BUS\_USB |  |
| BT\_HCI\_BUS\_PCCARD |  |
| BT\_HCI\_BUS\_UART |  |
| BT\_HCI\_BUS\_RS232 |  |
| BT\_HCI\_BUS\_PCI |  |
| BT\_HCI\_BUS\_SDIO |  |
| BT\_HCI\_BUS\_SPI |  |
| BT\_HCI\_BUS\_I2C |  |
| BT\_HCI\_BUS\_IPM |  |

## Function Documentation

## [◆ ](#gad187f0aff959a4756b281aa33d1b4394)bt\_hci\_close()

| | int bt\_hci\_close | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

Close the HCI transport.

Closes the HCI transport. This function must not return until the transport is closed.

Parameters
:   | dev | HCI device |
    | --- | --- |

Returns
:   0 on success or negative POSIX error number on failure.

## [◆ ](#gac744c98801cea5afd13d6774154e71c8)bt\_hci\_open()

| | int bt\_hci\_open | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bt\_hci\_recv\_t](#ga79b12569871b2b6c8420c245e9505aed) | *recv* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

Open the HCI transport.

Opens the HCI transport for operation. This function must not return until the transport is ready for operation, meaning it is safe to start calling the [send()](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d "POSIX wrapper for zsock_send.") handler.

Parameters
:   | dev | HCI device |
    | --- | --- |
    | [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40 "POSIX wrapper for zsock_recv.") | This is callback through which the HCI driver provides the host with data from the controller. The buffer passed to the callback will have its type set with [bt\_buf\_set\_type()](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec "Set the buffer type."). The callback is expected to be called from thread context. |

Returns
:   0 on success or negative POSIX error number on failure.

## [◆ ](#ga64079b6f03479561c1c7d09b3af81ede)bt\_hci\_send()

| | int bt\_hci\_send | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [net\_buf](structnet__buf.md) \* | *buf* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

Send HCI buffer to controller.

Send an HCI packet to the controller. The packet type of the buffer must be set using [bt\_buf\_set\_type()](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec "Set the buffer type.").

Note
:   This function must only be called from a cooperative thread.

Parameters
:   | dev | HCI device |
    | --- | --- |
    | buf | Buffer containing data to be sent to the controller. |

Returns
:   0 on success or negative POSIX error number on failure.

## [◆ ](#ga45ce7bf5fe86f5fff3d8838d247b1d47)bt\_hci\_setup()

| | int bt\_hci\_setup | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \* | *params* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](drivers_2bluetooth_8h.md)>`

HCI vendor-specific setup.

Executes vendor-specific commands sequence to initialize BT Controller before BT Host executes Reset sequence. This is normally called directly after [bt\_hci\_open()](#gac744c98801cea5afd13d6774154e71c8).

Note
:   `CONFIG_BT_HCI_SETUP` must be selected for this field to be available.

Returns
:   0 on success or negative POSIX error number on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
