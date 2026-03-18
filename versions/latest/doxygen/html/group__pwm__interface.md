---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__pwm__interface.html
original_path: doxygen/html/group__pwm__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PWM Interface

[Device Driver APIs](group__io__interfaces.md)

PWM Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [pwm\_dt\_spec](structpwm__dt__spec.md) |
|  | Container for PWM information specified in devicetree. [More...](structpwm__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [PWM\_DT\_SPEC\_GET\_BY\_NAME](#ga88b92c580860441c83d1b03db25fc4f1)(node\_id, name) |
|  | Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree."). |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME](#ga104a81a3481362d2da9046c0e93a8cd0)(inst, name) |
|  | Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") from a DT\_DRV\_COMPAT instance. |
| #define | [PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR](#ga5557add2123a7138b64997cd070e0ee6)(node\_id, name, default\_value) |
|  | Like [PWM\_DT\_SPEC\_GET\_BY\_NAME()](#ga88b92c580860441c83d1b03db25fc4f1), with a fallback to a default value. |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME\_OR](#gac00e53eccaf9eb515aed0921404adb31)(inst, name, default\_value) |
|  | Like [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME()](#ga104a81a3481362d2da9046c0e93a8cd0), with a fallback to a default value. |
| #define | [PWM\_DT\_SPEC\_GET\_BY\_IDX](#ga7e8375bcf95ae6a9500ce3aba4586de4)(node\_id, idx) |
|  | Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree."). |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX](#ga3c1c557fa4461e61f4a147fc72f87f8d)(inst, idx) |
|  | Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") from a DT\_DRV\_COMPAT instance. |
| #define | [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](#gaf5808fd88b101208681820b53bca33e1)(node\_id, idx, default\_value) |
|  | Like [PWM\_DT\_SPEC\_GET\_BY\_IDX()](#ga7e8375bcf95ae6a9500ce3aba4586de4), with a fallback to a default value. |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#ga7eeef648c3142fced48b7ab52c9c1ead)(inst, idx, default\_value) |
|  | Like [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX()](#ga3c1c557fa4461e61f4a147fc72f87f8d), with a fallback to a default value. |
| #define | [PWM\_DT\_SPEC\_GET](#ga59a79f0b77c5b71252bde126f333a84b)(node\_id) |
|  | Equivalent to [PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](#ga7e8375bcf95ae6a9500ce3aba4586de4). |
| #define | [PWM\_DT\_SPEC\_INST\_GET](#gaa346428c6cb1f11aafaa6306486e8a4b)(inst) |
|  | Equivalent to [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](#ga3c1c557fa4461e61f4a147fc72f87f8d). |
| #define | [PWM\_DT\_SPEC\_GET\_OR](#ga82f8efe8f0bc088fdda58c09dd4be4ff)(node\_id, default\_value) |
|  | Equivalent to [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)](#gaf5808fd88b101208681820b53bca33e1). |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_OR](#ga6bd84121715beb62a3ca2672dfae0630)(inst, default\_value) |
|  | Equivalent to [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, 0, default\_value)](#ga7eeef648c3142fced48b7ab52c9c1ead). |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) |
|  | Provides a type to hold PWM configuration flags. |
| typedef void(\* | [pwm\_capture\_callback\_handler\_t](#ga2395ef29b77674d9f1b56d8091b8695a)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles, int status, void \*user\_data) |
|  | PWM capture callback handler function signature. |

| Functions | |
| --- | --- |
| int | [pwm\_set\_cycles](#gaff280789f7b45fdefc354b3f841fe3ef) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse, [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set the period and pulse width for a single PWM output. |
| int | [pwm\_get\_cycles\_per\_sec](#ga310d416087a619f90e946222668135af) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles) |
|  | Get the clock rate (cycles per second) for a single PWM output. |
| static int | [pwm\_set](#gadd9049c9a56cd9419736b3514e42dc01) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse, [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set the period and pulse width in nanoseconds for a single PWM output. |
| static int | [pwm\_set\_dt](#ga225ce58ceb3de3d76df3e03439d655b9) (const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse) |
|  | Set the period and pulse width in nanoseconds from a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") (with custom period). |
| static int | [pwm\_set\_pulse\_dt](#ga8ff263177143d33c6d0a284b837bc4da) (const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse) |
|  | Set the period and pulse width in nanoseconds from a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree."). |
| static int | [pwm\_cycles\_to\_usec](#gae57fb205e43dde82d96abe79966539a9) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycles, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*usec) |
|  | Convert from PWM cycles to microseconds. |
| static int | [pwm\_cycles\_to\_nsec](#ga6f0281398611dd876386c66a63373a2e) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycles, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*nsec) |
|  | Convert from PWM cycles to nanoseconds. |
| static int | [pwm\_configure\_capture](#ga9603146d7f9c2690c1e1983113d6c6bb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [pwm\_capture\_callback\_handler\_t](#ga2395ef29b77674d9f1b56d8091b8695a) cb, void \*user\_data) |
|  | Configure PWM period/pulse width capture for a single PWM input. |
| int | [pwm\_enable\_capture](#gad14ca53862a465d1789e8936ce394f9a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Enable PWM period/pulse width capture for a single PWM input. |
| int | [pwm\_disable\_capture](#ga1df2bb40af2fa3ce945cc9cd67edc2bf) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Disable PWM period/pulse width capture for a single PWM input. |
| int | [pwm\_capture\_cycles](#ga09767ae3c8d970675dbf9e3e50291743) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Capture a single PWM period/pulse width in clock cycles for a single PWM input. |
| static int | [pwm\_capture\_usec](#ga3a1552ea924eeec21477396da6d3890b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*period, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Capture a single PWM period/pulse width in microseconds for a single PWM input. |
| static int | [pwm\_capture\_nsec](#ga6489095d890224d23c5ed05bc884d24a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*period, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Capture a single PWM period/pulse width in nanoseconds for a single PWM input. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pwm\_is\_ready\_dt](#ga70aad0d88e8041c880499e7cdaa9ae57) (const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec) |
|  | Validate that the PWM device is ready. |

| PWM capture configuration flags | |
| --- | --- |
|  | |
| #define | [PWM\_CAPTURE\_TYPE\_PERIOD](#ga5b4b41ccdf8810a77f71c2155a521f44)   (1U << PWM\_CAPTURE\_TYPE\_SHIFT) |
|  | PWM pin capture captures period. |
| #define | [PWM\_CAPTURE\_TYPE\_PULSE](#gab883b83cc5418555a437ce128f32ab01)   (2U << PWM\_CAPTURE\_TYPE\_SHIFT) |
|  | PWM pin capture captures pulse width. |
| #define | [PWM\_CAPTURE\_TYPE\_BOTH](#ga76175b0c2d5187ded5bbd314dc798bd5) |
|  | PWM pin capture captures both period and pulse width. |
| #define | [PWM\_CAPTURE\_MODE\_SINGLE](#gad59fe75340facda843cad06993cf1814)   (0U << PWM\_CAPTURE\_MODE\_SHIFT) |
|  | PWM pin capture captures a single period/pulse width. |
| #define | [PWM\_CAPTURE\_MODE\_CONTINUOUS](#gabe9bbff9832b4fa40faa057fad8fdaa9)   (1U << PWM\_CAPTURE\_MODE\_SHIFT) |
|  | PWM pin capture captures period/pulse width continuously. |

| PWM period set helpers | |
| --- | --- |
| The period cell in the PWM specifier needs to be provided in nanoseconds.  However, in some applications it is more convenient to use another scale. | |
| #define | [PWM\_NSEC](#ga17f20d628bcc81d5023c39e4cdfad405)(x) |
|  | Specify PWM period in nanoseconds. |
| #define | [PWM\_USEC](#ga368f28c8daaee25e546484bd908e675e)(x) |
|  | Specify PWM period in microseconds. |
| #define | [PWM\_MSEC](#ga1cccc226a23866dd2dcac9467ff3af0e)(x) |
|  | Specify PWM period in milliseconds. |
| #define | [PWM\_SEC](#ga4da4565d4dbded0efb640bd538cba3c2)(x) |
|  | Specify PWM period in seconds. |
| #define | [PWM\_HZ](#ga4a5edbee48c4a5706cf75524aef2364a)(x) |
|  | Specify PWM frequency in hertz. |
| #define | [PWM\_KHZ](#gaf846cf23d31d14296e0cbc1f82a530f4)(x) |
|  | Specify PWM frequency in kilohertz. |

| PWM polarity flags | |
| --- | --- |
| The PWM\_POLARITY\_\* flags are used with [pwm\_set\_cycles()](#gaff280789f7b45fdefc354b3f841fe3ef), [pwm\_set()](#gadd9049c9a56cd9419736b3514e42dc01) or [pwm\_configure\_capture()](#ga9603146d7f9c2690c1e1983113d6c6bb) to specify the polarity of a PWM channel.  The flags are on the lower 8bits of the [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) | |
| #define | [PWM\_POLARITY\_NORMAL](#ga2c706bbada711f383d7b42f09dace861)   (0 << 0) |
|  | PWM pin normal polarity (active-high pulse). |
| #define | [PWM\_POLARITY\_INVERTED](#ga930c0ab50f81aeb571af9747947d7fae)   (1 << 0) |
|  | PWM pin inverted polarity (active-low pulse). |

## Detailed Description

PWM Interface.

## Macro Definition Documentation

## [◆ ](#gabe9bbff9832b4fa40faa057fad8fdaa9)PWM\_CAPTURE\_MODE\_CONTINUOUS

| #define PWM\_CAPTURE\_MODE\_CONTINUOUS   (1U << PWM\_CAPTURE\_MODE\_SHIFT) |
| --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

PWM pin capture captures period/pulse width continuously.

## [◆ ](#gad59fe75340facda843cad06993cf1814)PWM\_CAPTURE\_MODE\_SINGLE

| #define PWM\_CAPTURE\_MODE\_SINGLE   (0U << PWM\_CAPTURE\_MODE\_SHIFT) |
| --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

PWM pin capture captures a single period/pulse width.

## [◆ ](#ga76175b0c2d5187ded5bbd314dc798bd5)PWM\_CAPTURE\_TYPE\_BOTH

| #define PWM\_CAPTURE\_TYPE\_BOTH |
| --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

([PWM\_CAPTURE\_TYPE\_PERIOD](#ga5b4b41ccdf8810a77f71c2155a521f44) | \

[PWM\_CAPTURE\_TYPE\_PULSE](#gab883b83cc5418555a437ce128f32ab01))

[PWM\_CAPTURE\_TYPE\_PERIOD](#ga5b4b41ccdf8810a77f71c2155a521f44)

#define PWM\_CAPTURE\_TYPE\_PERIOD

PWM pin capture captures period.

**Definition** pwm.h:53

[PWM\_CAPTURE\_TYPE\_PULSE](#gab883b83cc5418555a437ce128f32ab01)

#define PWM\_CAPTURE\_TYPE\_PULSE

PWM pin capture captures pulse width.

**Definition** pwm.h:56

PWM pin capture captures both period and pulse width.

## [◆ ](#ga5b4b41ccdf8810a77f71c2155a521f44)PWM\_CAPTURE\_TYPE\_PERIOD

| #define PWM\_CAPTURE\_TYPE\_PERIOD   (1U << PWM\_CAPTURE\_TYPE\_SHIFT) |
| --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

PWM pin capture captures period.

## [◆ ](#gab883b83cc5418555a437ce128f32ab01)PWM\_CAPTURE\_TYPE\_PULSE

| #define PWM\_CAPTURE\_TYPE\_PULSE   (2U << PWM\_CAPTURE\_TYPE\_SHIFT) |
| --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

PWM pin capture captures pulse width.

## [◆ ](#ga59a79f0b77c5b71252bde126f333a84b)PWM\_DT\_SPEC\_GET

| #define PWM\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[PWM\_DT\_SPEC\_GET\_BY\_IDX](#ga7e8375bcf95ae6a9500ce3aba4586de4)(node\_id, 0)

[PWM\_DT\_SPEC\_GET\_BY\_IDX](#ga7e8375bcf95ae6a9500ce3aba4586de4)

#define PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)

Static initializer for a struct pwm\_dt\_spec.

**Definition** pwm.h:256

Equivalent to [PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](#ga7e8375bcf95ae6a9500ce3aba4586de4).

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property.

See also
:   [PWM\_DT\_SPEC\_GET\_BY\_IDX](#ga7e8375bcf95ae6a9500ce3aba4586de4)
:   [PWM\_DT\_SPEC\_INST\_GET](#gaa346428c6cb1f11aafaa6306486e8a4b)

## [◆ ](#ga7e8375bcf95ae6a9500ce3aba4586de4)PWM\_DT\_SPEC\_GET\_BY\_IDX

| #define PWM\_DT\_SPEC\_GET\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

{ \

.dev = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_PWMS\_CTLR\_BY\_IDX](group__devicetree-pwms.md#ga2f16d00a53717a66668fb8bc967acce5)(node\_id, idx)), \

.channel = [DT\_PWMS\_CHANNEL\_BY\_IDX](group__devicetree-pwms.md#ga10a372e44c7e3feb551ca996c6ca5a8f)(node\_id, idx), \

.period = [DT\_PWMS\_PERIOD\_BY\_IDX](group__devicetree-pwms.md#ga9456f65777e6fc7c057c6e0709c9245f)(node\_id, idx), \

.flags = [DT\_PWMS\_FLAGS\_BY\_IDX](group__devicetree-pwms.md#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)(node\_id, idx), \

}

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:233

[DT\_PWMS\_CHANNEL\_BY\_IDX](group__devicetree-pwms.md#ga10a372e44c7e3feb551ca996c6ca5a8f)

#define DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, idx)

Get a PWM specifier's channel cell value at an index.

**Definition** pwms.h:207

[DT\_PWMS\_CTLR\_BY\_IDX](group__devicetree-pwms.md#ga2f16d00a53717a66668fb8bc967acce5)

#define DT\_PWMS\_CTLR\_BY\_IDX(node\_id, idx)

Get the node identifier for the PWM controller from a pwms property at an index.

**Definition** pwms.h:51

[DT\_PWMS\_PERIOD\_BY\_IDX](group__devicetree-pwms.md#ga9456f65777e6fc7c057c6e0709c9245f)

#define DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, idx)

Get PWM specifier's period cell value at an index.

**Definition** pwms.h:248

[DT\_PWMS\_FLAGS\_BY\_IDX](group__devicetree-pwms.md#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)

#define DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, idx)

Get a PWM specifier's flags cell value at an index.

**Definition** pwms.h:290

Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.").

This returns a static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") given a devicetree node identifier and an index.

Example devicetree fragment:

n: node {

pwms = <&pwm1 1 1000 PWM\_POLARITY\_NORMAL>,

<&pwm2 3 2000 PWM\_POLARITY\_INVERTED>;

};

Example usage:

const struct [pwm\_dt\_spec](structpwm__dt__spec.md) spec =

[PWM\_DT\_SPEC\_GET\_BY\_IDX](#ga7e8375bcf95ae6a9500ce3aba4586de4)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), 1);

// Initializes 'spec' to:

// {

// .dev = DEVICE\_DT\_GET(DT\_NODELABEL(pwm2)),

// .channel = 3,

// .period = 2000,

// .flags = PWM\_POLARITY\_INVERTED,

// }

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:198

[pwm\_dt\_spec](structpwm__dt__spec.md)

Container for PWM information specified in devicetree.

**Definition** pwm.h:96

The device (dev) must still be checked for readiness, e.g. using [device\_is\_ready()](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb "Verify that a device is ready for use."). It is an error to use this macro unless the node exists, has the 'pwms' property, and that 'pwms' property specifies a PWM controller, a channel, a period in nanoseconds and optionally flags.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | idx | Logical index into 'pwms' property. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property.

See also
:   [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX](#ga3c1c557fa4461e61f4a147fc72f87f8d)

## [◆ ](#gaf5808fd88b101208681820b53bca33e1)PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR

| #define PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, pwms), \

([PWM\_DT\_SPEC\_GET\_BY\_IDX](#ga7e8375bcf95ae6a9500ce3aba4586de4)(node\_id, idx)), \

(default\_value))

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3285

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

Like [PWM\_DT\_SPEC\_GET\_BY\_IDX()](#ga7e8375bcf95ae6a9500ce3aba4586de4), with a fallback to a default value.

If the devicetree node identifier 'node\_id' refers to a node with a property 'pwms', this expands to [PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)](#ga7e8375bcf95ae6a9500ce3aba4586de4). The `default_value` parameter is not expanded in this case. Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | idx | Logical index into 'pwms' property. |
    | default\_value | Fallback value to expand to. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property, or `default_value` if the node or property do not exist.

See also
:   [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#ga7eeef648c3142fced48b7ab52c9c1ead)

## [◆ ](#ga88b92c580860441c83d1b03db25fc4f1)PWM\_DT\_SPEC\_GET\_BY\_NAME

| #define PWM\_DT\_SPEC\_GET\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

{ \

.dev = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_PWMS\_CTLR\_BY\_NAME](group__devicetree-pwms.md#ga6922e69c707219cd766fe317484dac8a)(node\_id, name)), \

.channel = [DT\_PWMS\_CHANNEL\_BY\_NAME](group__devicetree-pwms.md#ga59a4b9884e9620eac04c3808a3a6d164)(node\_id, name), \

.period = [DT\_PWMS\_PERIOD\_BY\_NAME](group__devicetree-pwms.md#ga74af83d31fc38f331808dedfaecf4c74)(node\_id, name), \

.flags = [DT\_PWMS\_FLAGS\_BY\_NAME](group__devicetree-pwms.md#ga7a1621bfb223da23aa030b64fc0c0bcd)(node\_id, name), \

}

[DT\_PWMS\_CHANNEL\_BY\_NAME](group__devicetree-pwms.md#ga59a4b9884e9620eac04c3808a3a6d164)

#define DT\_PWMS\_CHANNEL\_BY\_NAME(node\_id, name)

Get a PWM specifier's channel cell value by name.

**Definition** pwms.h:224

[DT\_PWMS\_CTLR\_BY\_NAME](group__devicetree-pwms.md#ga6922e69c707219cd766fe317484dac8a)

#define DT\_PWMS\_CTLR\_BY\_NAME(node\_id, name)

Get the node identifier for the PWM controller from a pwms property by name.

**Definition** pwms.h:81

[DT\_PWMS\_PERIOD\_BY\_NAME](group__devicetree-pwms.md#ga74af83d31fc38f331808dedfaecf4c74)

#define DT\_PWMS\_PERIOD\_BY\_NAME(node\_id, name)

Get a PWM specifier's period cell value by name.

**Definition** pwms.h:265

[DT\_PWMS\_FLAGS\_BY\_NAME](group__devicetree-pwms.md#ga7a1621bfb223da23aa030b64fc0c0bcd)

#define DT\_PWMS\_FLAGS\_BY\_NAME(node\_id, name)

Get a PWM specifier's flags cell value by name.

**Definition** pwms.h:310

Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.").

This returns a static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") given a devicetree node identifier and an index.

Example devicetree fragment:

n: node {

pwms = <&pwm1 1 1000 PWM\_POLARITY\_NORMAL>,

<&pwm2 3 2000 PWM\_POLARITY\_INVERTED>;

pwm-names = "alpha", "beta";

};

Example usage:

const struct [pwm\_dt\_spec](structpwm__dt__spec.md) spec =

[PWM\_DT\_SPEC\_GET\_BY\_NAME](#ga88b92c580860441c83d1b03db25fc4f1)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), alpha);

// Initializes 'spec' to:

// {

// .dev = DEVICE\_DT\_GET(DT\_NODELABEL(pwm1)),

// .channel = 1,

// .period = 1000,

// .flags = PWM\_POLARITY\_NORMAL,

// }

[PWM\_DT\_SPEC\_GET\_BY\_NAME](#ga88b92c580860441c83d1b03db25fc4f1)

#define PWM\_DT\_SPEC\_GET\_BY\_NAME(node\_id, name)

Static initializer for a struct pwm\_dt\_spec.

**Definition** pwm.h:151

The device (dev) must still be checked for readiness, e.g. using [device\_is\_ready()](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb "Verify that a device is ready for use."). It is an error to use this macro unless the node exists, has the 'pwms' property, and that 'pwms' property specifies a PWM controller, a channel, a period in nanoseconds and optionally flags.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | name | Lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property.

See also
:   [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME](#ga104a81a3481362d2da9046c0e93a8cd0)

## [◆ ](#ga5557add2123a7138b64997cd070e0ee6)PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR

| #define PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, pwms), \

([PWM\_DT\_SPEC\_GET\_BY\_NAME](#ga88b92c580860441c83d1b03db25fc4f1)(node\_id, name)), \

(default\_value))

Like [PWM\_DT\_SPEC\_GET\_BY\_NAME()](#ga88b92c580860441c83d1b03db25fc4f1), with a fallback to a default value.

If the devicetree node identifier 'node\_id' refers to a node with a property 'pwms', this expands to [PWM\_DT\_SPEC\_GET\_BY\_NAME(node\_id, name)](#ga88b92c580860441c83d1b03db25fc4f1). The `default_value` parameter is not expanded in this case. Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | name | Lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |
    | default\_value | Fallback value to expand to. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property, or `default_value` if the node or property do not exist.

See also
:   [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME\_OR](#gac00e53eccaf9eb515aed0921404adb31)

## [◆ ](#ga82f8efe8f0bc088fdda58c09dd4be4ff)PWM\_DT\_SPEC\_GET\_OR

| #define PWM\_DT\_SPEC\_GET\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *default\_value* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](#gaf5808fd88b101208681820b53bca33e1)(node\_id, 0, default\_value)

[PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](#gaf5808fd88b101208681820b53bca33e1)

#define PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value)

Like PWM\_DT\_SPEC\_GET\_BY\_IDX(), with a fallback to a default value.

**Definition** pwm.h:295

Equivalent to [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)](#gaf5808fd88b101208681820b53bca33e1).

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | default\_value | Fallback value to expand to. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property.

See also
:   [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](#gaf5808fd88b101208681820b53bca33e1)
:   [PWM\_DT\_SPEC\_INST\_GET\_OR](#ga6bd84121715beb62a3ca2672dfae0630)

## [◆ ](#gaa346428c6cb1f11aafaa6306486e8a4b)PWM\_DT\_SPEC\_INST\_GET

| #define PWM\_DT\_SPEC\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[PWM\_DT\_SPEC\_GET](#ga59a79f0b77c5b71252bde126f333a84b)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

[PWM\_DT\_SPEC\_GET](#ga59a79f0b77c5b71252bde126f333a84b)

#define PWM\_DT\_SPEC\_GET(node\_id)

Equivalent to PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0).

**Definition** pwm.h:326

Equivalent to [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](#ga3c1c557fa4461e61f4a147fc72f87f8d).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property.

See also
:   [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX](#ga3c1c557fa4461e61f4a147fc72f87f8d)
:   [PWM\_DT\_SPEC\_GET](#ga59a79f0b77c5b71252bde126f333a84b)

## [◆ ](#ga3c1c557fa4461e61f4a147fc72f87f8d)PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX

| #define PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[PWM\_DT\_SPEC\_GET\_BY\_IDX](#ga7e8375bcf95ae6a9500ce3aba4586de4)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") from a DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | Logical index into 'pwms' property. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property.

See also
:   [PWM\_DT\_SPEC\_GET\_BY\_IDX](#ga7e8375bcf95ae6a9500ce3aba4586de4)

## [◆ ](#ga7eeef648c3142fced48b7ab52c9c1ead)PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR

| #define PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](#gaf5808fd88b101208681820b53bca33e1)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx, default\_value)

Like [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX()](#ga3c1c557fa4461e61f4a147fc72f87f8d), with a fallback to a default value.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | Logical index into 'pwms' property. |
    | default\_value | Fallback value to expand to. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property, or `default_value` if the node or property do not exist.

See also
:   [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](#gaf5808fd88b101208681820b53bca33e1)

## [◆ ](#ga104a81a3481362d2da9046c0e93a8cd0)PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME

| #define PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[PWM\_DT\_SPEC\_GET\_BY\_NAME](#ga88b92c580860441c83d1b03db25fc4f1)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") from a DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | Lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property.

See also
:   [PWM\_DT\_SPEC\_GET\_BY\_NAME](#ga88b92c580860441c83d1b03db25fc4f1)

## [◆ ](#gac00e53eccaf9eb515aed0921404adb31)PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME\_OR

| #define PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR](#ga5557add2123a7138b64997cd070e0ee6)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, default\_value)

[PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR](#ga5557add2123a7138b64997cd070e0ee6)

#define PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR(node\_id, name, default\_value)

Like PWM\_DT\_SPEC\_GET\_BY\_NAME(), with a fallback to a default value.

**Definition** pwm.h:192

Like [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME()](#ga104a81a3481362d2da9046c0e93a8cd0), with a fallback to a default value.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | Lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property. |
    | default\_value | Fallback value to expand to. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property, or `default_value` if the node or property do not exist.

See also
:   [PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR](#ga5557add2123a7138b64997cd070e0ee6)

## [◆ ](#ga6bd84121715beb62a3ca2672dfae0630)PWM\_DT\_SPEC\_INST\_GET\_OR

| #define PWM\_DT\_SPEC\_INST\_GET\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *default\_value* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

**Value:**

[PWM\_DT\_SPEC\_GET\_OR](#ga82f8efe8f0bc088fdda58c09dd4be4ff)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), default\_value)

[PWM\_DT\_SPEC\_GET\_OR](#ga82f8efe8f0bc088fdda58c09dd4be4ff)

#define PWM\_DT\_SPEC\_GET\_OR(node\_id, default\_value)

Equivalent to PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value).

**Definition** pwm.h:352

Equivalent to [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, 0, default\_value)](#ga7eeef648c3142fced48b7ab52c9c1ead).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | default\_value | Fallback value to expand to. |

Returns
:   Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") for the property.

See also
:   [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#ga7eeef648c3142fced48b7ab52c9c1ead)
:   [PWM\_DT\_SPEC\_GET\_OR](#ga82f8efe8f0bc088fdda58c09dd4be4ff)

## [◆ ](#ga4a5edbee48c4a5706cf75524aef2364a)PWM\_HZ

| #define PWM\_HZ | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](dt-bindings_2pwm_2pwm_8h.md)>`

**Value:**

([PWM\_SEC](#ga4da4565d4dbded0efb640bd538cba3c2)(1UL) / (x))

[PWM\_SEC](#ga4da4565d4dbded0efb640bd538cba3c2)

#define PWM\_SEC(x)

Specify PWM period in seconds.

**Definition** pwm.h:30

Specify PWM frequency in hertz.

## [◆ ](#gaf846cf23d31d14296e0cbc1f82a530f4)PWM\_KHZ

| #define PWM\_KHZ | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](dt-bindings_2pwm_2pwm_8h.md)>`

**Value:**

([PWM\_HZ](#ga4a5edbee48c4a5706cf75524aef2364a)((x) \* 1000UL))

[PWM\_HZ](#ga4a5edbee48c4a5706cf75524aef2364a)

#define PWM\_HZ(x)

Specify PWM frequency in hertz.

**Definition** pwm.h:32

Specify PWM frequency in kilohertz.

## [◆ ](#ga1cccc226a23866dd2dcac9467ff3af0e)PWM\_MSEC

| #define PWM\_MSEC | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](dt-bindings_2pwm_2pwm_8h.md)>`

**Value:**

([PWM\_USEC](#ga368f28c8daaee25e546484bd908e675e)(x) \* 1000UL)

[PWM\_USEC](#ga368f28c8daaee25e546484bd908e675e)

#define PWM\_USEC(x)

Specify PWM period in microseconds.

**Definition** pwm.h:26

Specify PWM period in milliseconds.

## [◆ ](#ga17f20d628bcc81d5023c39e4cdfad405)PWM\_NSEC

| #define PWM\_NSEC | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](dt-bindings_2pwm_2pwm_8h.md)>`

**Value:**

(x)

Specify PWM period in nanoseconds.

## [◆ ](#ga930c0ab50f81aeb571af9747947d7fae)PWM\_POLARITY\_INVERTED

| #define PWM\_POLARITY\_INVERTED   (1 << 0) |
| --- |

`#include <[pwm.h](dt-bindings_2pwm_2pwm_8h.md)>`

PWM pin inverted polarity (active-low pulse).

## [◆ ](#ga2c706bbada711f383d7b42f09dace861)PWM\_POLARITY\_NORMAL

| #define PWM\_POLARITY\_NORMAL   (0 << 0) |
| --- |

`#include <[pwm.h](dt-bindings_2pwm_2pwm_8h.md)>`

PWM pin normal polarity (active-high pulse).

## [◆ ](#ga4da4565d4dbded0efb640bd538cba3c2)PWM\_SEC

| #define PWM\_SEC | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](dt-bindings_2pwm_2pwm_8h.md)>`

**Value:**

([PWM\_MSEC](#ga1cccc226a23866dd2dcac9467ff3af0e)(x) \* 1000UL)

[PWM\_MSEC](#ga1cccc226a23866dd2dcac9467ff3af0e)

#define PWM\_MSEC(x)

Specify PWM period in milliseconds.

**Definition** pwm.h:28

Specify PWM period in seconds.

## [◆ ](#ga368f28c8daaee25e546484bd908e675e)PWM\_USEC

| #define PWM\_USEC | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](dt-bindings_2pwm_2pwm_8h.md)>`

**Value:**

([PWM\_NSEC](#ga17f20d628bcc81d5023c39e4cdfad405)(x) \* 1000UL)

[PWM\_NSEC](#ga17f20d628bcc81d5023c39e4cdfad405)

#define PWM\_NSEC(x)

Specify PWM period in nanoseconds.

**Definition** pwm.h:24

Specify PWM period in microseconds.

## Typedef Documentation

## [◆ ](#ga2395ef29b77674d9f1b56d8091b8695a)pwm\_capture\_callback\_handler\_t

| typedef void(\* pwm\_capture\_callback\_handler\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles, int status, void \*user\_data) |
| --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

PWM capture callback handler function signature.

Note
:   The callback handler will be called in interrupt context.
:   `CONFIG_PWM_CAPTURE` must be selected to enable PWM capture support.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    |  | period\_cycles | Captured PWM period width (in clock cycles). HW specific. |
    |  | pulse\_cycles | Captured PWM pulse width (in clock cycles). HW specific. |
    |  | status | Status for the PWM capture (0 if no error, negative errno otherwise. See [pwm\_capture\_cycles()](#ga09767ae3c8d970675dbf9e3e50291743) return value descriptions for details). |
    |  | user\_data | User data passed to [pwm\_configure\_capture()](#ga9603146d7f9c2690c1e1983113d6c6bb) |

## [◆ ](#gae1dcfb878163da76041efcedf0960fa0)pwm\_flags\_t

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) |
| --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Provides a type to hold PWM configuration flags.

The lower 8 bits are used for standard flags. The upper 8 bits are reserved for SoC specific flags.

See also
:   [PWM\_CAPTURE\_FLAGS](#PWM_CAPTURE_FLAGS).

## Function Documentation

## [◆ ](#ga09767ae3c8d970675dbf9e3e50291743)pwm\_capture\_cycles()

| int pwm\_capture\_cycles | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, |
|  |  | [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) | *flags*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *period*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *pulse*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Capture a single PWM period/pulse width in clock cycles for a single PWM input.

This API function wraps calls to [pwm\_configure\_capture()](#ga9603146d7f9c2690c1e1983113d6c6bb), [pwm\_enable\_capture()](#gad14ca53862a465d1789e8936ce394f9a), and [pwm\_disable\_capture()](#ga1df2bb40af2fa3ce945cc9cd67edc2bf) and passes the capture result to the caller. The function is blocking until either the PWM capture is completed or a timeout occurs.

Note
:   `CONFIG_PWM_CAPTURE` must be selected for this function to be available.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    |  | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | PWM capture flags. |
    | [out] | period | Pointer to the memory to store the captured PWM period width (in clock cycles). HW specific. |
    | [out] | pulse | Pointer to the memory to store the captured PWM pulse width (in clock cycles). HW specific. |
    |  | timeout | Waiting period for the capture to complete. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | PWM capture already in progress. |
    | -EAGAIN | Waiting period timed out. |
    | -EIO | IO error while capturing. |
    | -ERANGE | If result is too large. |

## [◆ ](#ga6489095d890224d23c5ed05bc884d24a)pwm\_capture\_nsec()

| | int pwm\_capture\_nsec | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, | |  |  | [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) | *flags*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *period*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *pulse*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Capture a single PWM period/pulse width in nanoseconds for a single PWM input.

This API function wraps calls to [pwm\_capture\_cycles()](#ga09767ae3c8d970675dbf9e3e50291743) and [pwm\_cycles\_to\_nsec()](#ga6f0281398611dd876386c66a63373a2e) and passes the capture result to the caller. The function is blocking until either the PWM capture is completed or a timeout occurs.

Note
:   `CONFIG_PWM_CAPTURE` must be selected for this function to be available.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    |  | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | PWM capture flags. |
    | [out] | period | Pointer to the memory to store the captured PWM period width (in nsec). |
    | [out] | pulse | Pointer to the memory to store the captured PWM pulse width (in nsec). |
    |  | timeout | Waiting period for the capture to complete. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | PWM capture already in progress. |
    | -EAGAIN | Waiting period timed out. |
    | -EIO | IO error while capturing. |
    | -ERANGE | If result is too large. |
    | -errno | Other negative errno code on failure. |

## [◆ ](#ga3a1552ea924eeec21477396da6d3890b)pwm\_capture\_usec()

| | int pwm\_capture\_usec | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, | |  |  | [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) | *flags*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *period*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *pulse*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Capture a single PWM period/pulse width in microseconds for a single PWM input.

This API function wraps calls to [pwm\_capture\_cycles()](#ga09767ae3c8d970675dbf9e3e50291743) and [pwm\_cycles\_to\_usec()](#gae57fb205e43dde82d96abe79966539a9) and passes the capture result to the caller. The function is blocking until either the PWM capture is completed or a timeout occurs.

Note
:   `CONFIG_PWM_CAPTURE` must be selected for this function to be available.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    |  | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | PWM capture flags. |
    | [out] | period | Pointer to the memory to store the captured PWM period width (in usec). |
    | [out] | pulse | Pointer to the memory to store the captured PWM pulse width (in usec). |
    |  | timeout | Waiting period for the capture to complete. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | PWM capture already in progress. |
    | -EAGAIN | Waiting period timed out. |
    | -EIO | IO error while capturing. |
    | -ERANGE | If result is too large. |
    | -errno | Other negative errno code on failure. |

## [◆ ](#ga9603146d7f9c2690c1e1983113d6c6bb)pwm\_configure\_capture()

| | int pwm\_configure\_capture | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, | |  |  | [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) | *flags*, | |  |  | [pwm\_capture\_callback\_handler\_t](#ga2395ef29b77674d9f1b56d8091b8695a) | *cb*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Configure PWM period/pulse width capture for a single PWM input.

After configuring PWM capture using this function, the capture can be enabled/disabled using [pwm\_enable\_capture()](#gad14ca53862a465d1789e8936ce394f9a) and [pwm\_disable\_capture()](#ga1df2bb40af2fa3ce945cc9cd67edc2bf).

Note
:   This API function cannot be invoked from user space due to the use of a function callback. In user space, one of the simpler API functions ([pwm\_capture\_cycles()](#ga09767ae3c8d970675dbf9e3e50291743), [pwm\_capture\_usec()](#ga3a1552ea924eeec21477396da6d3890b), or [pwm\_capture\_nsec()](#ga6489095d890224d23c5ed05bc884d24a)) can be used instead.
:   `CONFIG_PWM_CAPTURE` must be selected for this function to be available.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    |  | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | PWM capture flags |
    | [in] | cb | Application callback handler function to be called upon capture |
    | [in] | user\_data | User data to pass to the application callback handler function |

Return values
:   | -EINVAL | if invalid function parameters were given |
    | --- | --- |
    | -ENOSYS | if PWM capture is not supported or the given flags are not supported |
    | -EIO | if IO error occurred while configuring |
    | -EBUSY | if PWM capture is already in progress |

## [◆ ](#ga6f0281398611dd876386c66a63373a2e)pwm\_cycles\_to\_nsec()

| | int pwm\_cycles\_to\_nsec | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cycles*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *nsec* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Convert from PWM cycles to nanoseconds.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    |  | cycles | Cycles to be converted. |
    | [out] | nsec | Pointer to the memory to store the calculated nsec. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ERANGE | If result is too large. |
    | -errno | Other negative errno code on failure. |

## [◆ ](#gae57fb205e43dde82d96abe79966539a9)pwm\_cycles\_to\_usec()

| | int pwm\_cycles\_to\_usec | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cycles*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *usec* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Convert from PWM cycles to microseconds.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    |  | cycles | Cycles to be converted. |
    | [out] | usec | Pointer to the memory to store calculated usec. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ERANGE | If result is too large. |
    | -errno | Other negative errno code on failure. |

## [◆ ](#ga1df2bb40af2fa3ce945cc9cd67edc2bf)pwm\_disable\_capture()

| int pwm\_disable\_capture | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Disable PWM period/pulse width capture for a single PWM input.

Note
:   `CONFIG_PWM_CAPTURE` must be selected for this function to be available.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | if invalid function parameters were given |
    | -ENOSYS | if PWM capture is not supported |
    | -EIO | if IO error occurred while disabling PWM capture |

## [◆ ](#gad14ca53862a465d1789e8936ce394f9a)pwm\_enable\_capture()

| int pwm\_enable\_capture | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Enable PWM period/pulse width capture for a single PWM input.

The PWM pin must be configured using [pwm\_configure\_capture()](#ga9603146d7f9c2690c1e1983113d6c6bb) prior to calling this function.

Note
:   `CONFIG_PWM_CAPTURE` must be selected for this function to be available.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | if invalid function parameters were given |
    | -ENOSYS | if PWM capture is not supported |
    | -EIO | if IO error occurred while enabling PWM capture |
    | -EBUSY | if PWM capture is already in progress |

## [◆ ](#ga310d416087a619f90e946222668135af)pwm\_get\_cycles\_per\_sec()

| int pwm\_get\_cycles\_per\_sec | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *cycles* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Get the clock rate (cycles per second) for a single PWM output.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    | [out] | cycles | Pointer to the memory to store clock rate (cycles per sec). HW specific. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative errno code on failure. |

## [◆ ](#ga70aad0d88e8041c880499e7cdaa9ae57)pwm\_is\_ready\_dt()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pwm\_is\_ready\_dt | ( | const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Validate that the PWM device is ready.

Parameters
:   | spec | PWM specification from devicetree |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If the PWM device is ready for use |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If the PWM device is not ready for use |

## [◆ ](#gadd9049c9a56cd9419736b3514e42dc01)pwm\_set()

| | int pwm\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *period*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pulse*, | |  |  | [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Set the period and pulse width in nanoseconds for a single PWM output.

Note
:   Utility macros such as [PWM\_MSEC()](#ga1cccc226a23866dd2dcac9467ff3af0e) can be used to convert from other scales or units to nanoseconds, the units used by this function.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    |  | period | Period (in nanoseconds) set to the PWM. |
    |  | pulse | Pulse width (in nanoseconds) set to the PWM. |
    |  | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for pin configuration (polarity). |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If requested period or pulse cycles are not supported. |
    | -errno | Other negative errno code on failure. |

## [◆ ](#gaff280789f7b45fdefc354b3f841fe3ef)pwm\_set\_cycles()

| int pwm\_set\_cycles | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *period*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pulse*, |
|  |  | [pwm\_flags\_t](#gae1dcfb878163da76041efcedf0960fa0) | *flags* ) |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Set the period and pulse width for a single PWM output.

The PWM period and pulse width will synchronously be set to the new values without glitches in the PWM signal, but the call will not block for the change to take effect.

Note
:   Not all PWM controllers support synchronous, glitch-free updates of the PWM period and pulse width. Depending on the hardware, changing the PWM period and/or pulse width may cause a glitch in the generated PWM signal.
:   Some multi-channel PWM controllers share the PWM period across all channels. Depending on the hardware, changing the PWM period for one channel may affect the PWM period for the other channels of the same PWM controller.

Passing 0 as `pulse` will cause the pin to be driven to a constant inactive level. Passing a non-zero `pulse` equal to `period` will cause the pin to be driven to a constant active level.

Parameters
:   | [in] | dev | PWM device instance. |
    | --- | --- | --- |
    |  | channel | PWM channel. |
    |  | period | Period (in clock cycles) set to the PWM. HW specific. |
    |  | pulse | Pulse width (in clock cycles) set to the PWM. HW specific. |
    |  | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for pin configuration. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If pulse > period. |
    | -errno | Negative errno code on failure. |

## [◆ ](#ga225ce58ceb3de3d76df3e03439d655b9)pwm\_set\_dt()

| | int pwm\_set\_dt | ( | const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *period*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pulse* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Set the period and pulse width in nanoseconds from a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") (with custom period).

This is equivalent to:

```
pwm_set(spec->dev, spec->channel, period, pulse, spec->flags)
```

The period specified in `spec` is ignored. This API call can be used when the period specified in Devicetree needs to be changed at runtime.

Parameters
:   | [in] | spec | PWM specification from devicetree. |
    | --- | --- | --- |
    |  | period | Period (in nanoseconds) set to the PWM. |
    |  | pulse | Pulse width (in nanoseconds) set to the PWM. |

Returns
:   A value from [pwm\_set()](#gadd9049c9a56cd9419736b3514e42dc01).

See also
:   [pwm\_set\_pulse\_dt()](#ga8ff263177143d33c6d0a284b837bc4da)

## [◆ ](#ga8ff263177143d33c6d0a284b837bc4da)pwm\_set\_pulse\_dt()

| | int pwm\_set\_pulse\_dt | ( | const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pulse* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pwm.h](drivers_2pwm_8h.md)>`

Set the period and pulse width in nanoseconds from a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.").

This is equivalent to:

```
pwm_set(spec->dev, spec->channel, spec->period, pulse, spec->flags)
```

Parameters
:   | [in] | spec | PWM specification from devicetree. |
    | --- | --- | --- |
    |  | pulse | Pulse width (in nanoseconds) set to the PWM. |

Returns
:   A value from [pwm\_set()](#gadd9049c9a56cd9419736b3514e42dc01).

See also
:   [pwm\_set\_pulse\_dt()](#ga8ff263177143d33c6d0a284b837bc4da)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
