---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pinctrl__rcar__common_8h.html
original_path: doxygen/html/pinctrl__rcar__common_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_rcar\_common.h File Reference

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h](pinctrl-rcar-common_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](pinctrl__rcar__common_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [rcar\_pin\_func](structrcar__pin__func.md) |
| struct | [pinctrl\_soc\_pin](structpinctrl__soc__pin.md) |
|  | Type for R-Car pin. [More...](structpinctrl__soc__pin.md#details) |
| struct | [pfc\_drive\_reg\_field](structpfc__drive__reg__field.md) |
| struct | [pfc\_drive\_reg](structpfc__drive__reg.md) |
| struct | [pfc\_bias\_reg](structpfc__bias__reg.md) |

| Macros | |
| --- | --- |
| #define | [RCAR\_PIN\_FLAGS\_PULL\_SET](#a8ac73177e56465acd4376645a2fd89b1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Pull-up, pull-down, or bias disable is requested. |
| #define | [RCAR\_PIN\_FLAGS\_PUEN](#acdaea04a569eaec56c706bd311e1cadd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Performs on/off control of the pull resistors. |
| #define | [RCAR\_PIN\_FLAGS\_PUD](#a6df27aa417055266a299e964bb92fd44)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Select pull-up resistor if set pull-down otherwise. |
| #define | [RCAR\_PIN\_FLAGS\_FUNC\_SET](#aabcc781206d861b19d24bd82ad1150b0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Alternate function for the pin is requested. |
| #define | [RCAR\_PIN\_FLAGS\_FUNC\_DUMMY](#a44b7efa931db5d11e5b7c9cb8a94bbf9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Ignore IPSR settings for alternate function pin. |
| #define | [RCAR\_PIN\_PULL\_UP](#a5ac9cbd536534bf5e4edb3b76f0a2f60)   ([RCAR\_PIN\_FLAGS\_PULL\_SET](#a8ac73177e56465acd4376645a2fd89b1) | [RCAR\_PIN\_FLAGS\_PUEN](#acdaea04a569eaec56c706bd311e1cadd) | [RCAR\_PIN\_FLAGS\_PUD](#a6df27aa417055266a299e964bb92fd44)) |
| #define | [RCAR\_PIN\_PULL\_DOWN](#a53d33b579bb9c498fdd09ed9bb35c0e1)   ([RCAR\_PIN\_FLAGS\_PULL\_SET](#a8ac73177e56465acd4376645a2fd89b1) | [RCAR\_PIN\_FLAGS\_PUEN](#acdaea04a569eaec56c706bd311e1cadd)) |
| #define | [RCAR\_PIN\_PULL\_DISABLE](#a6d4c259adbd0cd5fd6065fdd4a57cda7)   [RCAR\_PIN\_FLAGS\_PULL\_SET](#a8ac73177e56465acd4376645a2fd89b1) |
| #define | [RCAR\_IPSR](#af89135625acaec60f328c703a7d1823b)(node\_id) |
| #define | [RCAR\_HAS\_IPSR](#a2c260d5b989251d6dc533f835df76772)(node\_id) |
| #define | [RCAR\_PIN\_FUNC](#a7f0e2d8e2d84035326685c1e2c56d181)(node\_id) |
| #define | [RCAR\_PIN\_IS\_FUNC\_DUMMY](#a718e93760aba13e5c883ce133760e197)(node\_id) |
| #define | [RCAR\_PIN\_FLAGS](#ab94ca6630b8bddbf7325b5ae01ee969d)(node\_id) |
| #define | [RCAR\_DT\_PIN](#a3f524c2e190008ea866d3e9e114a5f18)(node\_id) |
| #define | [RCAR\_IS\_GP\_PIN](#af231b8fe5b02c023bf068b8c7565d4c4)(pin) |
|  | Utility macro to check if a pin is GPIO capable. |

| Typedefs | |
| --- | --- |
| typedef struct [pinctrl\_soc\_pin](structpinctrl__soc__pin.md) | [pinctrl\_soc\_pin\_t](#a022eeb1c811e7ef94d3a7a99cbda0e2d) |
|  | Type for R-Car pin. |

## Macro Definition Documentation

## [◆ ](#a3f524c2e190008ea866d3e9e114a5f18)RCAR\_DT\_PIN

| #define RCAR\_DT\_PIN | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

.pin = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, pin, 0), \

.func = [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([RCAR\_HAS\_IPSR](#a2c260d5b989251d6dc533f835df76772)(node\_id), \

([RCAR\_PIN\_FUNC](#a7f0e2d8e2d84035326685c1e2c56d181)(node\_id)), {0}), \

.[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = [RCAR\_PIN\_FLAGS](#ab94ca6630b8bddbf7325b5ae01ee969d)(node\_id), \

.drive\_strength = \

COND\_CODE\_1([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, drive\_strength), \

([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, drive\_strength)), (0)), \

.voltage = [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, \

power\_source), \

([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, power\_source)), \

([PIN\_VOLTAGE\_NONE](pinctrl-rcar-common_8h.md#a866ef498674c60a51c56decc15421e25))), \

},

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3677

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:891

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:745

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[PIN\_VOLTAGE\_NONE](pinctrl-rcar-common_8h.md#a866ef498674c60a51c56decc15421e25)

#define PIN\_VOLTAGE\_NONE

**Definition** pinctrl-rcar-common.h:97

[RCAR\_HAS\_IPSR](#a2c260d5b989251d6dc533f835df76772)

#define RCAR\_HAS\_IPSR(node\_id)

**Definition** pinctrl\_rcar\_common.h:47

[RCAR\_PIN\_FUNC](#a7f0e2d8e2d84035326685c1e2c56d181)

#define RCAR\_PIN\_FUNC(node\_id)

**Definition** pinctrl\_rcar\_common.h:50

[RCAR\_PIN\_FLAGS](#ab94ca6630b8bddbf7325b5ae01ee969d)

#define RCAR\_PIN\_FLAGS(node\_id)

**Definition** pinctrl\_rcar\_common.h:62

## [◆ ](#a2c260d5b989251d6dc533f835df76772)RCAR\_HAS\_IPSR

| #define RCAR\_HAS\_IPSR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)(node\_id, pin, 1)

[DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)

#define DT\_PROP\_HAS\_IDX(node\_id, prop, idx)

Is index idx valid for an array type property?

**Definition** devicetree.h:819

## [◆ ](#af89135625acaec60f328c703a7d1823b)RCAR\_IPSR

| #define RCAR\_IPSR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, pin, 1)

## [◆ ](#af231b8fe5b02c023bf068b8c7565d4c4)RCAR\_IS\_GP\_PIN

| #define RCAR\_IS\_GP\_PIN | ( |  | *pin* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(pin < [PIN\_NOGPSR\_START](pinctrl-rcar-common_8h.md#a165cdeba11c616c3c14e1d02e6c4d552))

[PIN\_NOGPSR\_START](pinctrl-rcar-common_8h.md#a165cdeba11c616c3c14e1d02e6c4d552)

#define PIN\_NOGPSR\_START

**Definition** pinctrl-rcar-common.h:28

Utility macro to check if a pin is GPIO capable.

Parameters
:   | pin |  |
    | --- | --- |

Returns
:   true if pin is GPIO capable false otherwise

## [◆ ](#ab94ca6630b8bddbf7325b5ae01ee969d)RCAR\_PIN\_FLAGS

| #define RCAR\_PIN\_FLAGS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, bias\_pull\_up) \* [RCAR\_PIN\_PULL\_UP](#a5ac9cbd536534bf5e4edb3b76f0a2f60) | \

DT\_PROP(node\_id, bias\_pull\_down) \* [RCAR\_PIN\_PULL\_DOWN](#a53d33b579bb9c498fdd09ed9bb35c0e1) | \

DT\_PROP(node\_id, bias\_disable) \* [RCAR\_PIN\_PULL\_DISABLE](#a6d4c259adbd0cd5fd6065fdd4a57cda7) | \

RCAR\_HAS\_IPSR(node\_id) \* [RCAR\_PIN\_FLAGS\_FUNC\_SET](#aabcc781206d861b19d24bd82ad1150b0) | \

RCAR\_PIN\_IS\_FUNC\_DUMMY(node\_id) \* [RCAR\_PIN\_FLAGS\_FUNC\_DUMMY](#a44b7efa931db5d11e5b7c9cb8a94bbf9)

[RCAR\_PIN\_FLAGS\_FUNC\_DUMMY](#a44b7efa931db5d11e5b7c9cb8a94bbf9)

#define RCAR\_PIN\_FLAGS\_FUNC\_DUMMY

Ignore IPSR settings for alternate function pin.

**Definition** pinctrl\_rcar\_common.h:31

[RCAR\_PIN\_PULL\_DOWN](#a53d33b579bb9c498fdd09ed9bb35c0e1)

#define RCAR\_PIN\_PULL\_DOWN

**Definition** pinctrl\_rcar\_common.h:34

[RCAR\_PIN\_PULL\_UP](#a5ac9cbd536534bf5e4edb3b76f0a2f60)

#define RCAR\_PIN\_PULL\_UP

**Definition** pinctrl\_rcar\_common.h:33

[RCAR\_PIN\_PULL\_DISABLE](#a6d4c259adbd0cd5fd6065fdd4a57cda7)

#define RCAR\_PIN\_PULL\_DISABLE

**Definition** pinctrl\_rcar\_common.h:35

[RCAR\_PIN\_FLAGS\_FUNC\_SET](#aabcc781206d861b19d24bd82ad1150b0)

#define RCAR\_PIN\_FLAGS\_FUNC\_SET

Alternate function for the pin is requested.

**Definition** pinctrl\_rcar\_common.h:29

## [◆ ](#a44b7efa931db5d11e5b7c9cb8a94bbf9)RCAR\_PIN\_FLAGS\_FUNC\_DUMMY

| #define RCAR\_PIN\_FLAGS\_FUNC\_DUMMY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Ignore IPSR settings for alternate function pin.

## [◆ ](#aabcc781206d861b19d24bd82ad1150b0)RCAR\_PIN\_FLAGS\_FUNC\_SET

| #define RCAR\_PIN\_FLAGS\_FUNC\_SET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Alternate function for the pin is requested.

## [◆ ](#a6df27aa417055266a299e964bb92fd44)RCAR\_PIN\_FLAGS\_PUD

| #define RCAR\_PIN\_FLAGS\_PUD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Select pull-up resistor if set pull-down otherwise.

## [◆ ](#acdaea04a569eaec56c706bd311e1cadd)RCAR\_PIN\_FLAGS\_PUEN

| #define RCAR\_PIN\_FLAGS\_PUEN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Performs on/off control of the pull resistors.

## [◆ ](#a8ac73177e56465acd4376645a2fd89b1)RCAR\_PIN\_FLAGS\_PULL\_SET

| #define RCAR\_PIN\_FLAGS\_PULL\_SET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Pull-up, pull-down, or bias disable is requested.

## [◆ ](#a7f0e2d8e2d84035326685c1e2c56d181)RCAR\_PIN\_FUNC

| #define RCAR\_PIN\_FUNC | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

(([RCAR\_IPSR](#af89135625acaec60f328c703a7d1823b)(node\_id) >> 10U) & 0x1FU), \

(([RCAR\_IPSR](#af89135625acaec60f328c703a7d1823b)(node\_id) >> 4U) & 0x1FU), \

(([RCAR\_IPSR](#af89135625acaec60f328c703a7d1823b)(node\_id) & 0xFU)) \

}

[RCAR\_IPSR](#af89135625acaec60f328c703a7d1823b)

#define RCAR\_IPSR(node\_id)

**Definition** pinctrl\_rcar\_common.h:46

## [◆ ](#a718e93760aba13e5c883ce133760e197)RCAR\_PIN\_IS\_FUNC\_DUMMY

| #define RCAR\_PIN\_IS\_FUNC\_DUMMY | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((([RCAR\_IPSR](#af89135625acaec60f328c703a7d1823b)(node\_id) >> 10U) & 0x1FU) == 0x1F) && \

((([RCAR\_IPSR](#af89135625acaec60f328c703a7d1823b)(node\_id) >> 4U) & 0x1FU) == 0x1F) && \

(([RCAR\_IPSR](#af89135625acaec60f328c703a7d1823b)(node\_id) & 0xFU) == 0xF))

## [◆ ](#a6d4c259adbd0cd5fd6065fdd4a57cda7)RCAR\_PIN\_PULL\_DISABLE

| #define RCAR\_PIN\_PULL\_DISABLE   [RCAR\_PIN\_FLAGS\_PULL\_SET](#a8ac73177e56465acd4376645a2fd89b1) |
| --- |

## [◆ ](#a53d33b579bb9c498fdd09ed9bb35c0e1)RCAR\_PIN\_PULL\_DOWN

| #define RCAR\_PIN\_PULL\_DOWN   ([RCAR\_PIN\_FLAGS\_PULL\_SET](#a8ac73177e56465acd4376645a2fd89b1) | [RCAR\_PIN\_FLAGS\_PUEN](#acdaea04a569eaec56c706bd311e1cadd)) |
| --- |

## [◆ ](#a5ac9cbd536534bf5e4edb3b76f0a2f60)RCAR\_PIN\_PULL\_UP

| #define RCAR\_PIN\_PULL\_UP   ([RCAR\_PIN\_FLAGS\_PULL\_SET](#a8ac73177e56465acd4376645a2fd89b1) | [RCAR\_PIN\_FLAGS\_PUEN](#acdaea04a569eaec56c706bd311e1cadd) | [RCAR\_PIN\_FLAGS\_PUD](#a6df27aa417055266a299e964bb92fd44)) |
| --- |

## Typedef Documentation

## [◆ ](#a022eeb1c811e7ef94d3a7a99cbda0e2d)pinctrl\_soc\_pin\_t

| typedef struct [pinctrl\_soc\_pin](structpinctrl__soc__pin.md) [pinctrl\_soc\_pin\_t](#a022eeb1c811e7ef94d3a7a99cbda0e2d) |
| --- |

Type for R-Car pin.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl](dir_c0bb3bf986f9412b3a6b9d85dc06c157.md)
- [pinctrl\_rcar\_common.h](pinctrl__rcar__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
