---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__led__interface.html
original_path: doxygen/html/group__led__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LED Interface

[Device Driver APIs](group__io__interfaces.md)

LED Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [led\_info](structled__info.md) |
|  | LED information structure. [More...](structled__info.md#details) |
| struct | [led\_driver\_api](structled__driver__api.md) |
|  | LED driver API. [More...](structled__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [led\_api\_blink](#gad3c655794f58045459cbd910592d2cdd)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off) |
|  | Callback API for blinking an LED. |
| typedef int(\* | [led\_api\_get\_info](#ga3828b1e544a2f64378d5c3bfbbaa0c77)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, const struct [led\_info](structled__info.md) \*\*info) |
|  | Optional API callback to get LED information. |
| typedef int(\* | [led\_api\_set\_brightness](#gae24caa14f6aa41c2a509d2eaf468463f)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Callback API for setting brightness of an LED. |
| typedef int(\* | [led\_api\_set\_color](#ga977317f3208d5336463edf9979def4ae)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color) |
|  | Optional API callback to set the colors of a LED. |
| typedef int(\* | [led\_api\_on](#gad13f55702668133575658d2ccc295339)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
|  | Callback API for turning on an LED. |
| typedef int(\* | [led\_api\_off](#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
|  | Callback API for turning off an LED. |
| typedef int(\* | [led\_api\_write\_channels](#ga66dac12510c3a2281378d532ba6db2ae)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
|  | Callback API for writing a strip of LED channels. |

| Functions | |
| --- | --- |
| int | [led\_blink](#ga4f31fecd215e5597999be4d16b0d2dd5) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off) |
|  | Blink an LED. |
| int | [led\_get\_info](#ga9925483b97073354f7be6b40aa2dad1a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, const struct [led\_info](structled__info.md) \*\*info) |
|  | Get LED information. |
| int | [led\_set\_brightness](#gaca479fd77518331f4fc84f788e345882) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Set LED brightness. |
| int | [led\_write\_channels](#ga24d4007f81483d0fe8b9988288adf59a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
|  | Write/update a strip of LED channels. |
| int | [led\_set\_channel](#ga717bdbe76331b6286c58feb6e3e214dd) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Set a single LED channel. |
| int | [led\_set\_color](#ga94dd46cc96f6ade5cebaa46a5f7ca5ea) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color) |
|  | Set LED color. |
| int | [led\_on](#gad4daafd7fcab22d1d68745b7264d0f73) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
|  | Turn on an LED. |
| int | [led\_off](#ga22c9dbe76f06fec327aebe06448d1542) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
|  | Turn off an LED. |

## Detailed Description

LED Interface.

Since
:   1.12

Version
:   1.0.0

## Typedef Documentation

## [◆ ](#gad3c655794f58045459cbd910592d2cdd)led\_api\_blink

| typedef int(\* led\_api\_blink) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off) |
| --- |

`#include <[led.h](drivers_2led_8h.md)>`

Callback API for blinking an LED.

See also
:   [led\_blink()](#ga4f31fecd215e5597999be4d16b0d2dd5) for argument descriptions.

## [◆ ](#ga3828b1e544a2f64378d5c3bfbbaa0c77)led\_api\_get\_info

| typedef int(\* led\_api\_get\_info) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, const struct [led\_info](structled__info.md) \*\*info) |
| --- |

`#include <[led.h](drivers_2led_8h.md)>`

Optional API callback to get LED information.

See also
:   [led\_get\_info()](#ga9925483b97073354f7be6b40aa2dad1a) for argument descriptions.

## [◆ ](#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)led\_api\_off

| typedef int(\* led\_api\_off) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
| --- |

`#include <[led.h](drivers_2led_8h.md)>`

Callback API for turning off an LED.

See also
:   [led\_off()](#ga22c9dbe76f06fec327aebe06448d1542) for argument descriptions.

## [◆ ](#gad13f55702668133575658d2ccc295339)led\_api\_on

| typedef int(\* led\_api\_on) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
| --- |

`#include <[led.h](drivers_2led_8h.md)>`

Callback API for turning on an LED.

See also
:   [led\_on()](#gad4daafd7fcab22d1d68745b7264d0f73) for argument descriptions.

## [◆ ](#gae24caa14f6aa41c2a509d2eaf468463f)led\_api\_set\_brightness

| typedef int(\* led\_api\_set\_brightness) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
| --- |

`#include <[led.h](drivers_2led_8h.md)>`

Callback API for setting brightness of an LED.

See also
:   [led\_set\_brightness()](#gaca479fd77518331f4fc84f788e345882) for argument descriptions.

## [◆ ](#ga977317f3208d5336463edf9979def4ae)led\_api\_set\_color

| typedef int(\* led\_api\_set\_color) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color) |
| --- |

`#include <[led.h](drivers_2led_8h.md)>`

Optional API callback to set the colors of a LED.

See also
:   [led\_set\_color()](#ga94dd46cc96f6ade5cebaa46a5f7ca5ea) for argument descriptions.

## [◆ ](#ga66dac12510c3a2281378d532ba6db2ae)led\_api\_write\_channels

| typedef int(\* led\_api\_write\_channels) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
| --- |

`#include <[led.h](drivers_2led_8h.md)>`

Callback API for writing a strip of LED channels.

See also
:   [led\_api\_write\_channels()](#ga66dac12510c3a2281378d532ba6db2ae) for arguments descriptions.

## Function Documentation

## [◆ ](#ga4f31fecd215e5597999be4d16b0d2dd5)led\_blink()

| int led\_blink | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *led*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *delay\_on*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *delay\_off* ) |

`#include <[led.h](drivers_2led_8h.md)>`

Blink an LED.

This optional routine starts blinking a LED forever with the given time period.

Parameters
:   | dev | LED device |
    | --- | --- |
    | led | LED number |
    | delay\_on | Time period (in milliseconds) an LED should be ON |
    | delay\_off | Time period (in milliseconds) an LED should be OFF |

Returns
:   0 on success, negative on error

## [◆ ](#ga9925483b97073354f7be6b40aa2dad1a)led\_get\_info()

| int led\_get\_info | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *led*, |
|  |  | const struct [led\_info](structled__info.md) \*\* | *info* ) |

`#include <[led.h](drivers_2led_8h.md)>`

Get LED information.

This optional routine provides information about a LED.

Parameters
:   | dev | LED device |
    | --- | --- |
    | led | LED number |
    | info | Pointer to a pointer filled with LED information |

Returns
:   0 on success, negative on error

## [◆ ](#ga22c9dbe76f06fec327aebe06448d1542)led\_off()

| int led\_off | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *led* ) |

`#include <[led.h](drivers_2led_8h.md)>`

Turn off an LED.

This routine turns off an LED

Parameters
:   | dev | LED device |
    | --- | --- |
    | led | LED number |

Returns
:   0 on success, negative on error

## [◆ ](#gad4daafd7fcab22d1d68745b7264d0f73)led\_on()

| int led\_on | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *led* ) |

`#include <[led.h](drivers_2led_8h.md)>`

Turn on an LED.

This routine turns on an LED

Parameters
:   | dev | LED device |
    | --- | --- |
    | led | LED number |

Returns
:   0 on success, negative on error

## [◆ ](#gaca479fd77518331f4fc84f788e345882)led\_set\_brightness()

| int led\_set\_brightness | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *led*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

`#include <[led.h](drivers_2led_8h.md)>`

Set LED brightness.

This optional routine sets the brightness of a LED to the given value. Calling this function after [led\_blink()](#ga4f31fecd215e5597999be4d16b0d2dd5) won't affect blinking.

LEDs which can only be turned on or off may provide this function. These should simply turn the LED on if `value` is nonzero, and off if `value` is zero.

Parameters
:   | dev | LED device |
    | --- | --- |
    | led | LED number |
    | value | Brightness value to set in percent |

Returns
:   0 on success, negative on error

## [◆ ](#ga717bdbe76331b6286c58feb6e3e214dd)led\_set\_channel()

| int led\_set\_channel | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

`#include <[led.h](drivers_2led_8h.md)>`

Set a single LED channel.

This optional routine sets a single LED channel to the given value.

Calling this function after [led\_blink()](#ga4f31fecd215e5597999be4d16b0d2dd5) won't affect blinking.

Parameters
:   | dev | LED device |
    | --- | --- |
    | channel | Absolute channel number (i.e. not relative to a LED) |
    | value | Value to configure the channel with |

Returns
:   0 on success, negative on error

## [◆ ](#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)led\_set\_color()

| int led\_set\_color | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *led*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_colors*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *color* ) |

`#include <[led.h](drivers_2led_8h.md)>`

Set LED color.

This routine configures all the color channels of a LED with the given color array.

Calling this function after [led\_blink()](#ga4f31fecd215e5597999be4d16b0d2dd5) won't affect blinking.

Parameters
:   | dev | LED device |
    | --- | --- |
    | led | LED number |
    | num\_colors | Number of colors in the array. |
    | color | Array of colors. It must be ordered following the color mapping of the LED controller. See the color\_mapping member in struct [led\_info](structled__info.md "LED information structure."). |

Returns
:   0 on success, negative on error

## [◆ ](#ga24d4007f81483d0fe8b9988288adf59a)led\_write\_channels()

| int led\_write\_channels | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *start\_channel*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_channels*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf* ) |

`#include <[led.h](drivers_2led_8h.md)>`

Write/update a strip of LED channels.

This optional routine writes a strip of LED channels to the given array of levels. Therefore it can be used to configure several LEDs at the same time.

Calling this function after [led\_blink()](#ga4f31fecd215e5597999be4d16b0d2dd5) won't affect blinking.

Parameters
:   | dev | LED device |
    | --- | --- |
    | start\_channel | Absolute number (i.e. not relative to a LED) of the first channel to update. |
    | num\_channels | The number of channels to write/update. |
    | buf | array of values to configure the channels with. num\_channels entries must be provided. |

Returns
:   0 on success, negative on error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
