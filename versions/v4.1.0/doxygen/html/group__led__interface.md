---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__led__interface.html
original_path: doxygen/html/group__led__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| struct | [led\_dt\_spec](structled__dt__spec.md) |
|  | Container for an LED information specified in devicetree. [More...](structled__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [LED\_DT\_SPEC\_GET](#ga537f733ae3070fbe279834c76cda35ae)(node\_id) |
|  | Static initializer for a struct [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree."). |
| #define | [LED\_DT\_SPEC\_GET\_OR](#gade3059194ce428783ea3e9900ed0be52)(node\_id, default\_value) |
|  | Like [LED\_DT\_SPEC\_GET()](#ga537f733ae3070fbe279834c76cda35ae), with a fallback value if the node does not exist. |

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
| static int | [led\_set\_brightness\_dt](#gaecc33acfc2b1dde870b411d7f30eed82) (const struct [led\_dt\_spec](structled__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Set LED brightness from a [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree."). |
| static int | [led\_on\_dt](#gaa2b262a309e4ede4cb5715c69d900804) (const struct [led\_dt\_spec](structled__dt__spec.md) \*spec) |
|  | Turn on an LED from a struct [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree."). |
| static int | [led\_off\_dt](#ga8b6618e4fea4f44f218f95fd16abc16b) (const struct [led\_dt\_spec](structled__dt__spec.md) \*spec) |
|  | Turn off an LED from a struct [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree."). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [led\_is\_ready\_dt](#gaa2994b959c730dad3432481bba278497) (const struct [led\_dt\_spec](structled__dt__spec.md) \*spec) |
|  | Validate that the LED device is ready. |

## Detailed Description

LED Interface.

Since
:   1.12

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga537f733ae3070fbe279834c76cda35ae)LED\_DT\_SPEC\_GET

| #define LED\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[led.h](drivers_2led_8h.md)>`

**Value:**

{ \

.dev = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)(node\_id)), \

.index = [DT\_NODE\_CHILD\_IDX](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)(node\_id), \

}

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:280

[DT\_NODE\_CHILD\_IDX](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)

#define DT\_NODE\_CHILD\_IDX(node\_id)

Get a devicetree node's index into its parent's list of children.

**Definition** devicetree.h:651

[DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)

#define DT\_PARENT(node\_id)

Get a node identifier for a parent node.

**Definition** devicetree.h:374

Static initializer for a struct [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree.").

This returns a static initializer for a struct [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree.") given a devicetree node identifier.

Example devicetree fragment:

leds {

compatible = "gpio-leds";

led0: led\_0 {

...

};

};

Example usage:

const struct [led\_dt\_spec](structled__dt__spec.md) spec = [LED\_DT\_SPEC\_GET](#ga537f733ae3070fbe279834c76cda35ae)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(led0));

// Initializes 'spec' to:

// {

// .dev = DEVICE\_DT\_GET(DT\_PARENT(led0)),

// .index = 0,

// }

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[LED\_DT\_SPEC\_GET](#ga537f733ae3070fbe279834c76cda35ae)

#define LED\_DT\_SPEC\_GET(node\_id)

Static initializer for a struct led\_dt\_spec.

**Definition** led.h:442

[led\_dt\_spec](structled__dt__spec.md)

Container for an LED information specified in devicetree.

**Definition** led.h:345

The device (dev) must still be checked for readiness, e.g. using [device\_is\_ready()](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb "Verify that a device is ready for use.").

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |

Returns
:   Static initializer for a struct [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree.") for the property.

## [◆ ](#gade3059194ce428783ea3e9900ed0be52)LED\_DT\_SPEC\_GET\_OR

| #define LED\_DT\_SPEC\_GET\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *default\_value* ) |

`#include <[led.h](drivers_2led_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_EXISTS](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)(node\_id), \

([LED\_DT\_SPEC\_GET](#ga537f733ae3070fbe279834c76cda35ae)(node\_id)), \

(default\_value))

[DT\_NODE\_EXISTS](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)

#define DT\_NODE\_EXISTS(node\_id)

Does a node identifier refer to a node?

**Definition** devicetree.h:3644

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

Like [LED\_DT\_SPEC\_GET()](#ga537f733ae3070fbe279834c76cda35ae), with a fallback value if the node does not exist.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |

Returns
:   Static initializer for a struct [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree.") for the property.

See also
:   [LED\_DT\_SPEC\_GET](#ga537f733ae3070fbe279834c76cda35ae)

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

## [◆ ](#gaa2994b959c730dad3432481bba278497)led\_is\_ready\_dt()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) led\_is\_ready\_dt | ( | const struct [led\_dt\_spec](structled__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[led.h](drivers_2led_8h.md)>`

Validate that the LED device is ready.

Parameters
:   | spec | LED specification from devicetree. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If the LED device is ready for use. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If the LED device is not ready for use. |

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

## [◆ ](#ga8b6618e4fea4f44f218f95fd16abc16b)led\_off\_dt()

| | int led\_off\_dt | ( | const struct [led\_dt\_spec](structled__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[led.h](drivers_2led_8h.md)>`

Turn off an LED from a struct [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree.").

Parameters
:   | spec | LED device specification from devicetree. |
    | --- | --- |

Returns
:   0 on success, negative on error.

See also
:   [led\_off()](#ga22c9dbe76f06fec327aebe06448d1542)

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

## [◆ ](#gaa2b262a309e4ede4cb5715c69d900804)led\_on\_dt()

| | int led\_on\_dt | ( | const struct [led\_dt\_spec](structled__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[led.h](drivers_2led_8h.md)>`

Turn on an LED from a struct [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree.").

Parameters
:   | spec | LED device specification from devicetree. |
    | --- | --- |

Returns
:   0 on success, negative on error.

See also
:   [led\_on()](#gad4daafd7fcab22d1d68745b7264d0f73)

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

## [◆ ](#gaecc33acfc2b1dde870b411d7f30eed82)led\_set\_brightness\_dt()

| | int led\_set\_brightness\_dt | ( | const struct [led\_dt\_spec](structled__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[led.h](drivers_2led_8h.md)>`

Set LED brightness from a [led\_dt\_spec](structled__dt__spec.md "Container for an LED information specified in devicetree.").

Parameters
:   | spec | LED device specification from devicetree. |
    | --- | --- |
    | value | Brightness value to set in percent. |

Returns
:   0 on success, negative on error.

See also
:   [led\_set\_brightness()](#gaca479fd77518331f4fc84f788e345882)

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
