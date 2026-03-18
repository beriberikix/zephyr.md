---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__tgpio__interface.html
original_path: doxygen/html/group__tgpio__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Time-aware GPIO Interface

[Device Driver APIs](group__io__interfaces.md)

Time-aware GPIO Interface.
[More...](#details)

| Enumerations | |
| --- | --- |
| enum | [tgpio\_pin\_polarity](#gae05efc7d3232c308ae614b73688aa92c) { [TGPIO\_RISING\_EDGE](#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df) = 0 , [TGPIO\_FALLING\_EDGE](#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98) , [TGPIO\_TOGGLE\_EDGE](#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9) } |
|  | Event polarity. [More...](#gae05efc7d3232c308ae614b73688aa92c) |

| Functions | |
| --- | --- |
| int | [tgpio\_port\_get\_time](#gaa40a3fef2a4e4e1326a25cc832ff2fb3) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*current\_time) |
|  | Get time from ART timer. |
| int | [tgpio\_port\_get\_cycles\_per\_second](#gaccc8c2ed61ffabed71d5a410f10992da) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cycles) |
|  | Get current running rate. |
| int | [tgpio\_pin\_disable](#ga724d1410e73eba65c5d343b534424879) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin) |
|  | Disable operation on pin. |
| int | [tgpio\_pin\_config\_ext\_timestamp](#ga4c35c5941848a1b060366e6ccb9e655e) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_polarity) |
|  | Enable/Continue operation on pin. |
| int | [tgpio\_pin\_periodic\_output](#gaec3b6161e701b9f2124470da9c202301) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) start\_time, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) repeat\_interval, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) periodic\_enable) |
|  | Enable periodic pulse generation on a pin. |
| int | [tgpio\_pin\_read\_ts\_ec](#ga2f351d5d09b1f5bc7d71bce18979a0c2) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*timestamp, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*event\_count) |
|  | Read timestamp and event counter from TGPIO. |

## Detailed Description

Time-aware GPIO Interface.

## Enumeration Type Documentation

## [◆ ](#gae05efc7d3232c308ae614b73688aa92c)tgpio\_pin\_polarity

| enum [tgpio\_pin\_polarity](#gae05efc7d3232c308ae614b73688aa92c) |
| --- |

`#include <[timeaware_gpio.h](timeaware__gpio_8h.md)>`

Event polarity.

| Enumerator | |
| --- | --- |
| TGPIO\_RISING\_EDGE |  |
| TGPIO\_FALLING\_EDGE |  |
| TGPIO\_TOGGLE\_EDGE |  |

## Function Documentation

## [◆ ](#ga4c35c5941848a1b060366e6ccb9e655e)tgpio\_pin\_config\_ext\_timestamp()

| int tgpio\_pin\_config\_ext\_timestamp | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pin*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *event\_polarity* ) |

`#include <[timeaware_gpio.h](timeaware__gpio_8h.md)>`

Enable/Continue operation on pin.

Parameters
:   | dev | TGPIO device |
    | --- | --- |
    | pin | TGPIO pin |
    | event\_polarity | TGPIO pin event polarity |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#ga724d1410e73eba65c5d343b534424879)tgpio\_pin\_disable()

| int tgpio\_pin\_disable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pin* ) |

`#include <[timeaware_gpio.h](timeaware__gpio_8h.md)>`

Disable operation on pin.

Parameters
:   | dev | TGPIO device |
    | --- | --- |
    | pin | TGPIO pin |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#gaec3b6161e701b9f2124470da9c202301)tgpio\_pin\_periodic\_output()

| int tgpio\_pin\_periodic\_output | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pin*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *start\_time*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *repeat\_interval*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *periodic\_enable* ) |

`#include <[timeaware_gpio.h](timeaware__gpio_8h.md)>`

Enable periodic pulse generation on a pin.

Parameters
:   | dev | TGPIO device |
    | --- | --- |
    | pin | TGPIO pin |
    | start\_time | start\_time of first pulse in hw cycles |
    | repeat\_interval | repeat interval between two pulses in hw cycles |
    | periodic\_enable | enables periodic mode if 'true' is passed. |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#ga2f351d5d09b1f5bc7d71bce18979a0c2)tgpio\_pin\_read\_ts\_ec()

| int tgpio\_pin\_read\_ts\_ec | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pin*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *timestamp*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *event\_count* ) |

`#include <[timeaware_gpio.h](timeaware__gpio_8h.md)>`

Read timestamp and event counter from TGPIO.

Parameters
:   | dev | TGPIO device |
    | --- | --- |
    | pin | TGPIO pin |
    | timestamp | timestamp of the last pulse received |
    | event\_count | number of pulses received since the pin is enabled |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#gaccc8c2ed61ffabed71d5a410f10992da)tgpio\_port\_get\_cycles\_per\_second()

| int tgpio\_port\_get\_cycles\_per\_second | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *cycles* ) |

`#include <[timeaware_gpio.h](timeaware__gpio_8h.md)>`

Get current running rate.

Parameters
:   | dev | TGPIO device |
    | --- | --- |
    | cycles | pointer to store current running requency |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#gaa40a3fef2a4e4e1326a25cc832ff2fb3)tgpio\_port\_get\_time()

| int tgpio\_port\_get\_time | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *current\_time* ) |

`#include <[timeaware_gpio.h](timeaware__gpio_8h.md)>`

Get time from ART timer.

Parameters
:   | dev | TGPIO device |
    | --- | --- |
    | current\_time | Pointer to store timer value in cycles |

Returns
:   0 if successful
:   negative errno code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
