---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__source__callbacks.html
original_path: doxygen/html/group__source__callbacks.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Source\_callbacks

[USB-C Device API](group____usbc__device__api.md)

| Typedefs | |
| --- | --- |
| typedef int(\* | [policy\_cb\_get\_src\_caps\_t](#ga4bbf78bd752d38d915412dd942d3aab8)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*pdos, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*num\_pdos) |
|  | Callback type used to get the Source Capabilities from the Device Policy Manager. |
| typedef enum [usbc\_snk\_req\_reply\_t](group____usbc__device__api.md#ga4c4f0592a034b4e49eee85e95af33f94)(\* | [policy\_cb\_check\_sink\_request\_t](#gaeeda677224456f685137e4b345c0e173)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) request\_msg) |
|  | Callback type used to check if Sink request is valid. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_is\_ps\_ready\_t](#gae7391e858485e44a74e5fcdbb7931ca7)) (const struct [device](structdevice.md) \*dev) |
|  | Callback type used to check if Source Power Supply is ready. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_present\_contract\_is\_valid\_t](#ga2925e462140a700920251d92ae5a3aa4)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) present\_contract) |
|  | Callback type used to check if present Contract is still valid. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_change\_src\_caps\_t](#ga699811c862990b31ec0126dd3a4c3e4d)) (const struct [device](structdevice.md) \*dev) |
|  | Callback type used to request that a different set of Source Caps be sent to the Sink. |
| typedef void(\* | [policy\_cb\_set\_port\_partner\_snk\_cap\_t](#gae903c8108e8d1563cb0b1ccdd901c925)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pdos, const int num\_pdos) |
|  | Callback type used to report the Capabilities received from a Sink Port Partner. |
| typedef int(\* | [policy\_cb\_get\_src\_rp\_t](#ga7c75f8192001179f20bf1fe48316f3c6)) (const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp) |
|  | Callback type used to get the Rp value that should be placed on the CC lines. |
| typedef int(\* | [policy\_cb\_src\_en\_t](#gaaecac7683d7092c0a477e8d9ca0e5a33)) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) en) |
|  | Callback type used to enable VBUS. |

## Detailed Description

## Typedef Documentation

## [◆ ](#ga699811c862990b31ec0126dd3a4c3e4d)policy\_cb\_change\_src\_caps\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* policy\_cb\_change\_src\_caps\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to request that a different set of Source Caps be sent to the Sink.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |

Returns
:   true if a different set of Cource Caps is available

## [◆ ](#gaeeda677224456f685137e4b345c0e173)policy\_cb\_check\_sink\_request\_t

| typedef enum [usbc\_snk\_req\_reply\_t](group____usbc__device__api.md#ga4c4f0592a034b4e49eee85e95af33f94)(\* policy\_cb\_check\_sink\_request\_t) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) request\_msg) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to check if Sink request is valid.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | request\_msg | request message to check |

Returns
:   sink request reply

## [◆ ](#ga4bbf78bd752d38d915412dd942d3aab8)policy\_cb\_get\_src\_caps\_t

| typedef int(\* policy\_cb\_get\_src\_caps\_t) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*pdos, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*num\_pdos) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to get the Source Capabilities from the Device Policy Manager.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | pdos | pointer to source capability pdos |
    | num\_pdos | pointer to number of source capability pdos |

Returns
:   0 on success

## [◆ ](#ga7c75f8192001179f20bf1fe48316f3c6)policy\_cb\_get\_src\_rp\_t

| typedef int(\* policy\_cb\_get\_src\_rp\_t) (const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to get the Rp value that should be placed on the CC lines.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | rp | rp value |

Returns
:   0 on success

## [◆ ](#gae7391e858485e44a74e5fcdbb7931ca7)policy\_cb\_is\_ps\_ready\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* policy\_cb\_is\_ps\_ready\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to check if Source Power Supply is ready.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |

Returns
:   true if power supply is ready, else false

## [◆ ](#ga2925e462140a700920251d92ae5a3aa4)policy\_cb\_present\_contract\_is\_valid\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* policy\_cb\_present\_contract\_is\_valid\_t) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) present\_contract) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to check if present Contract is still valid.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | present\_contract | present contract |

Returns
:   true if present contract is still valid

## [◆ ](#gae903c8108e8d1563cb0b1ccdd901c925)policy\_cb\_set\_port\_partner\_snk\_cap\_t

| typedef void(\* policy\_cb\_set\_port\_partner\_snk\_cap\_t) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pdos, const int num\_pdos) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to report the Capabilities received from a Sink Port Partner.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | pdos | pointer to sink cap pdos |
    | num\_pdos | number of sink cap pdos |

## [◆ ](#gaaecac7683d7092c0a477e8d9ca0e5a33)policy\_cb\_src\_en\_t

| typedef int(\* policy\_cb\_src\_en\_t) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) en) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to enable VBUS.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | en | true if VBUS should be enabled, else false to disable it |

Returns
:   0 on success

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
