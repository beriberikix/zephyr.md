---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mspi__devicetree.html
original_path: doxygen/html/group__mspi__devicetree.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MSPI Devicetree related macros

[Device Driver APIs](group__io__interfaces.md)

MSPI Devicetree related macros.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [MSPI\_DEVICE\_CONFIG\_DT](#gaa8e730d85dede3d1e5dc9f69f30098b2)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") from devicetree. |
| #define | [MSPI\_DEVICE\_CONFIG\_DT\_INST](#ga52ebf325f9a1eb7d9fda6736ac8188f1)(inst) |
|  | Structure initializer for struct [mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") from devicetree instance. |
| #define | [MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK](#ga01a618fadb0147bf5abf42972a17f594)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") from devicetree. |
| #define | [MSPI\_XIP\_CONFIG\_DT](#ga24a88651c634c5ab5630e7844ff98e4b)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") from devicetree. |
| #define | [MSPI\_XIP\_CONFIG\_DT\_INST](#gafe739210f9f5cab4ab71bd61ec5af03f)(inst) |
|  | Structure initializer for struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") from devicetree instance. |
| #define | [MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK](#gad1f36df770167384cc4e3f2c9be07d34)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") from devicetree. |
| #define | [MSPI\_SCRAMBLE\_CONFIG\_DT](#ga10ee161794b5c7986a4411b8fc90ea7d)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") from devicetree. |
| #define | [MSPI\_SCRAMBLE\_CONFIG\_DT\_INST](#gaa9b32a8f6984468b5198524bea42ed8c)(inst) |
|  | Structure initializer for struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") from devicetree instance. |
| #define | [MSPI\_DEVICE\_ID\_DT](#gafa7c0d76c85a31004d72392016da1246)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_dev\_id](structmspi__dev__id.md "MSPI device ID The controller can identify its devices and determine whether the access is allowed in...") from devicetree. |
| #define | [MSPI\_DEVICE\_ID\_DT\_INST](#gabfd0d3beb91762e939636c87a91a6673)(inst) |
|  | Structure initializer for struct [mspi\_dev\_id](structmspi__dev__id.md "MSPI device ID The controller can identify its devices and determine whether the access is allowed in...") from devicetree instance. |
| #define | [MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET](#ga0a91ef9392be4493ede6cea607ee8728)(mspi\_dev) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a MSPI device's chip enable pin. |
| #define | [MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_INST\_GET](#ga0b98f7a625324abce90933cb2395fb17)(inst) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a MSPI device's chip enable pin. |
| #define | [MSPI\_CE\_GPIOS\_DT\_SPEC\_GET](#ga1ca28d7ead69cd3a5e26198bc6815b54)(node\_id) |
|  | Get an array of struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") from devicetree for a MSPI controller. |
| #define | [MSPI\_CE\_GPIOS\_DT\_SPEC\_INST\_GET](#ga5ae4bd8071da4babd0bdf9767e9542e4)(inst) |
|  | Get an array of struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a MSPI controller. |
| #define | [MSPI\_CE\_CONTROL\_INIT](#ga501b2e19e358083f2b47838cde58a676)(node\_id, delay\_) |
|  | Initialize and get a pointer to a `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` from a devicetree node identifier. |
| #define | [MSPI\_CE\_CONTROL\_INIT\_INST](#gacec91c9080052adf96aa5d36c6301d8c)(inst, delay\_) |
|  | Get a pointer to a `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` from a devicetree node. |

## Detailed Description

MSPI Devicetree related macros.

## Macro Definition Documentation

## [◆ ](#ga501b2e19e358083f2b47838cde58a676)MSPI\_CE\_CONTROL\_INIT

| #define MSPI\_CE\_CONTROL\_INIT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *delay\_* ) |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

{ \

.gpio = [MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET](#ga0a91ef9392be4493ede6cea607ee8728)(node\_id), .delay = (delay\_), \

}

[MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET](#ga0a91ef9392be4493ede6cea607ee8728)

#define MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET(mspi\_dev)

Get a struct gpio\_dt\_spec for a MSPI device's chip enable pin.

**Definition** devicetree.h:214

Initialize and get a pointer to a `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` from a devicetree node identifier.

This helper is useful for initializing a device on a MSPI bus. It initializes a struct [mspi\_ce\_control](structmspi__ce__control.md "MSPI Chip Select control structure.") and returns a pointer to it. Here, `node_id` is a node identifier for a MSPI device, not a MSPI controller.

Example devicetree fragment:

mspi@abcd0001 {

ce-gpios = <&gpio0 1 GPIO\_ACTIVE\_LOW>;

mspidev: mspi-device@0 { ... };

};

Example usage:

struct [mspi\_ce\_control](structmspi__ce__control.md) ctrl =

[MSPI\_CE\_CONTROL\_INIT](#ga501b2e19e358083f2b47838cde58a676)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(mspidev), 2);

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[MSPI\_CE\_CONTROL\_INIT](#ga501b2e19e358083f2b47838cde58a676)

#define MSPI\_CE\_CONTROL\_INIT(node\_id, delay\_)

Initialize and get a pointer to a mspi\_ce\_control from a devicetree node identifier.

**Definition** devicetree.h:298

[mspi\_ce\_control](structmspi__ce__control.md)

MSPI Chip Select control structure.

**Definition** mspi.h:348

This example is equivalent to:

struct [mspi\_ce\_control](structmspi__ce__control.md) ctrl = {

.gpio = [MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET](#ga0a91ef9392be4493ede6cea607ee8728)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(mspidev)),

.delay = 2,

};

Parameters
:   | node\_id | Devicetree node identifier for a device on a MSPI bus |
    | --- | --- |
    | delay\_ | The `delay` field to set in the `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` |

Returns
:   a pointer to the `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` structure

## [◆ ](#gacec91c9080052adf96aa5d36c6301d8c)MSPI\_CE\_CONTROL\_INIT\_INST

| #define MSPI\_CE\_CONTROL\_INIT\_INST | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *delay\_* ) |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[MSPI\_CE\_CONTROL\_INIT](#ga501b2e19e358083f2b47838cde58a676)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), delay\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

Get a pointer to a `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` from a devicetree node.

This is equivalent to [MSPI\_CE\_CONTROL\_INIT(DT\_DRV\_INST(inst), delay)](#ga501b2e19e358083f2b47838cde58a676).

Therefore, `DT_DRV_COMPAT` must already be defined before using this macro.

Parameters
:   | inst | Devicetree node instance number |
    | --- | --- |
    | delay\_ | The `delay` field to set in the `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` |

Returns
:   a pointer to the `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` structure

## [◆ ](#ga1ca28d7ead69cd3a5e26198bc6815b54)MSPI\_CE\_GPIOS\_DT\_SPEC\_GET

| #define MSPI\_CE\_GPIOS\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

{ \

COND\_CODE\_1([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, ce\_gpios), \

([DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)(node\_id, ce\_gpios, [GPIO\_DT\_SPEC\_GET\_BY\_IDX](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf), (,))), \

()) \

}

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3784

[DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)

#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep)

Invokes fn for each element in the value of property prop with separator.

**Definition** devicetree.h:3367

[GPIO\_DT\_SPEC\_GET\_BY\_IDX](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf)

#define GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx)

Static initializer for a gpio\_dt\_spec.

**Definition** gpio.h:332

Get an array of struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") from devicetree for a MSPI controller.

This helper macro check whether ce\_gpios binding exist first before calling [GPIO\_DT\_SPEC\_GET\_BY\_IDX](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf "Static initializer for a gpio_dt_spec.") and expand to an array of [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.").

Parameters
:   | node\_id | Devicetree node identifier for the MSPI controller |
    | --- | --- |

Returns
:   an array of [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") struct corresponding with mspi\_dev's chip enables

## [◆ ](#ga5ae4bd8071da4babd0bdf9767e9542e4)MSPI\_CE\_GPIOS\_DT\_SPEC\_INST\_GET

| #define MSPI\_CE\_GPIOS\_DT\_SPEC\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[MSPI\_CE\_GPIOS\_DT\_SPEC\_GET](#ga1ca28d7ead69cd3a5e26198bc6815b54)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[MSPI\_CE\_GPIOS\_DT\_SPEC\_GET](#ga1ca28d7ead69cd3a5e26198bc6815b54)

#define MSPI\_CE\_GPIOS\_DT\_SPEC\_GET(node\_id)

Get an array of struct gpio\_dt\_spec from devicetree for a MSPI controller.

**Definition** devicetree.h:241

Get an array of struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a MSPI controller.

This is equivalent to [MSPI\_CE\_GPIOS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))](#ga1ca28d7ead69cd3a5e26198bc6815b54).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

Returns
:   an array of [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") struct corresponding with mspi\_dev's chip enables

## [◆ ](#ga0a91ef9392be4493ede6cea607ee8728)MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET

| #define MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET | ( |  | *mspi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(mspi\_dev), ce\_gpios, \

[DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(mspi\_dev), {})

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3861

[DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)

#define DT\_REG\_ADDR\_RAW(node\_id)

Get a node's (only) register block raw address.

**Definition** devicetree.h:2428

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)

#define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value)

Like GPIO\_DT\_SPEC\_GET\_BY\_IDX(), with a fallback to a default value.

**Definition** gpio.h:356

Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a MSPI device's chip enable pin.

Example devicetree fragment:

gpio1: gpio@abcd0001 { ... };

gpio2: gpio@abcd0002 { ... };

mspi@abcd0003 {

compatible = "ambiq,mspi";

ce-gpios = <&gpio1 10 GPIO\_ACTIVE\_LOW>,

<&gpio2 20 GPIO\_ACTIVE\_LOW>;

a: mspi-dev-a@0 {

reg = <0>;

};

b: mspi-dev-b@1 {

reg = <1>;

};

};

Example usage:

[MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET](#ga0a91ef9392be4493ede6cea607ee8728)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(a)) \

// { DEVICE\_DT\_GET(DT\_NODELABEL(gpio1)), 10, GPIO\_ACTIVE\_LOW }

[MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET](#ga0a91ef9392be4493ede6cea607ee8728)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(b)) \

// { DEVICE\_DT\_GET(DT\_NODELABEL(gpio2)), 20, GPIO\_ACTIVE\_LOW }

Parameters
:   | mspi\_dev | a MSPI device node identifier |
    | --- | --- |

Returns
:   [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") struct corresponding with mspi\_dev's chip enable

## [◆ ](#ga0b98f7a625324abce90933cb2395fb17)MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_INST\_GET

| #define MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET](#ga0a91ef9392be4493ede6cea607ee8728)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a MSPI device's chip enable pin.

This is equivalent to [MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))](#ga0a91ef9392be4493ede6cea607ee8728).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

Returns
:   [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") struct corresponding with mspi\_dev's chip enable

## [◆ ](#gaa8e730d85dede3d1e5dc9f69f30098b2)MSPI\_DEVICE\_CONFIG\_DT

| #define MSPI\_DEVICE\_CONFIG\_DT | ( |  | *mspi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

{ \

.ce\_num = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(mspi\_dev, mspi\_hardware\_ce\_num, 0), \

.freq = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(mspi\_dev, mspi\_max\_frequency), \

.io\_mode = [DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)(mspi\_dev, [mspi\_io\_mode](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5), \

[MSPI\_IO\_MODE\_SINGLE](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd)), \

.data\_rate = [DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)(mspi\_dev, [mspi\_data\_rate](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68), \

[MSPI\_DATA\_RATE\_SINGLE](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0)), \

.cpp = [DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)(mspi\_dev, [mspi\_cpp\_mode](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c), [MSPI\_CPP\_MODE\_0](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90)), \

.endian = [DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)(mspi\_dev, [mspi\_endian](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44), \

[MSPI\_XFER\_LITTLE\_ENDIAN](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345)), \

.ce\_polarity = [DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)(mspi\_dev, [mspi\_ce\_polarity](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b), \

[MSPI\_CE\_ACTIVE\_LOW](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae)), \

.dqs\_enable = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(mspi\_dev, mspi\_dqs\_enable), \

.rx\_dummy = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(mspi\_dev, rx\_dummy, 0), \

.tx\_dummy = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(mspi\_dev, tx\_dummy, 0), \

.read\_cmd = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(mspi\_dev, read\_command, 0), \

.write\_cmd = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(mspi\_dev, write\_command, 0), \

.cmd\_length = [DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)(mspi\_dev, command\_length, 0), \

.addr\_length = [DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)(mspi\_dev, address\_length, 0), \

.mem\_boundary = [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(mspi\_dev, ce\_break\_config), \

([DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(mspi\_dev, ce\_break\_config, 0)), \

(0)), \

.time\_to\_break = [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(mspi\_dev, ce\_break\_config), \

([DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(mspi\_dev, ce\_break\_config, 1)), \

(0)), \

}

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:908

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:935

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

[DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)

#define DT\_ENUM\_IDX\_OR(node\_id, prop, default\_idx\_value)

Equivalent to DT\_ENUM\_IDX\_BY\_IDX\_OR(node\_id, prop, 0, default\_idx\_value).

**Definition** devicetree.h:1032

[mspi\_ce\_polarity](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b)

mspi\_ce\_polarity

MSPI chip enable polarity.

**Definition** mspi.h:113

[mspi\_endian](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44)

mspi\_endian

MSPI Endian.

**Definition** mspi.h:105

[mspi\_cpp\_mode](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c)

mspi\_cpp\_mode

MSPI Polarity & Phase Modes.

**Definition** mspi.h:95

[mspi\_io\_mode](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5)

mspi\_io\_mode

MSPI I/O mode capabilities Postfix like 1\_4\_4 stands for the number of lines used for command,...

**Definition** mspi.h:58

[mspi\_data\_rate](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68)

mspi\_data\_rate

MSPI data rate capabilities SINGLE stands for single data rate for all phases.

**Definition** mspi.h:84

[MSPI\_CE\_ACTIVE\_LOW](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae)

@ MSPI\_CE\_ACTIVE\_LOW

**Definition** mspi.h:114

[MSPI\_XFER\_LITTLE\_ENDIAN](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345)

@ MSPI\_XFER\_LITTLE\_ENDIAN

**Definition** mspi.h:106

[MSPI\_CPP\_MODE\_0](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90)

@ MSPI\_CPP\_MODE\_0

**Definition** mspi.h:96

[MSPI\_IO\_MODE\_SINGLE](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd)

@ MSPI\_IO\_MODE\_SINGLE

**Definition** mspi.h:59

[MSPI\_DATA\_RATE\_SINGLE](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0)

@ MSPI\_DATA\_RATE\_SINGLE

**Definition** mspi.h:85

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

Structure initializer for struct [mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") from devicetree.

This helper macro expands to a static initializer for a struct
[mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") by reading the relevant data from the devicetree.

Parameters
:   | mspi\_dev | Devicetree node identifier for the MSPI device whose struct [mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") to create an initializer for |
    | --- | --- |

## [◆ ](#ga52ebf325f9a1eb7d9fda6736ac8188f1)MSPI\_DEVICE\_CONFIG\_DT\_INST

| #define MSPI\_DEVICE\_CONFIG\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[MSPI\_DEVICE\_CONFIG\_DT](#gaa8e730d85dede3d1e5dc9f69f30098b2)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[MSPI\_DEVICE\_CONFIG\_DT](#gaa8e730d85dede3d1e5dc9f69f30098b2)

#define MSPI\_DEVICE\_CONFIG\_DT(mspi\_dev)

Structure initializer for struct mspi\_dev\_cfg from devicetree.

**Definition** devicetree.h:32

Structure initializer for struct [mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") from devicetree instance.

This is equivalent to [MSPI\_DEVICE\_CONFIG\_DT(DT\_DRV\_INST(inst))](#gaa8e730d85dede3d1e5dc9f69f30098b2).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

## [◆ ](#gafa7c0d76c85a31004d72392016da1246)MSPI\_DEVICE\_ID\_DT

| #define MSPI\_DEVICE\_ID\_DT | ( |  | *mspi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

{ \

.ce = [MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET](#ga0a91ef9392be4493ede6cea607ee8728)(mspi\_dev), \

.dev\_idx = [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(mspi\_dev), \

}

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2461

Structure initializer for struct [mspi\_dev\_id](structmspi__dev__id.md "MSPI device ID The controller can identify its devices and determine whether the access is allowed in...") from devicetree.

This helper macro expands to a static initializer for a struct
[mspi\_dev\_id](structmspi__dev__id.md "MSPI device ID The controller can identify its devices and determine whether the access is allowed in...") by reading the relevant data from the devicetree.

Parameters
:   | mspi\_dev | Devicetree node identifier for the MSPI device whose struct [mspi\_dev\_id](structmspi__dev__id.md "MSPI device ID The controller can identify its devices and determine whether the access is allowed in...") to create an initializer for |
    | --- | --- |

## [◆ ](#gabfd0d3beb91762e939636c87a91a6673)MSPI\_DEVICE\_ID\_DT\_INST

| #define MSPI\_DEVICE\_ID\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[MSPI\_DEVICE\_ID\_DT](#gafa7c0d76c85a31004d72392016da1246)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[MSPI\_DEVICE\_ID\_DT](#gafa7c0d76c85a31004d72392016da1246)

#define MSPI\_DEVICE\_ID\_DT(mspi\_dev)

Structure initializer for struct mspi\_dev\_id from devicetree.

**Definition** devicetree.h:160

Structure initializer for struct [mspi\_dev\_id](structmspi__dev__id.md "MSPI device ID The controller can identify its devices and determine whether the access is allowed in...") from devicetree instance.

This is equivalent to [MSPI\_DEVICE\_ID\_DT(DT\_DRV\_INST(inst))](#gafa7c0d76c85a31004d72392016da1246).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

## [◆ ](#ga10ee161794b5c7986a4411b8fc90ea7d)MSPI\_SCRAMBLE\_CONFIG\_DT

| #define MSPI\_SCRAMBLE\_CONFIG\_DT | ( |  | *mspi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(mspi\_dev, scramble\_config), \

([MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK](#gad1f36df770167384cc4e3f2c9be07d34)(mspi\_dev)), \

({}))

[MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK](#gad1f36df770167384cc4e3f2c9be07d34)

#define MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK(mspi\_dev)

Structure initializer for struct mspi\_scramble\_cfg from devicetree.

**Definition** devicetree.h:120

Structure initializer for struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") from devicetree.

This helper macro check whether scramble\_config binding exist first before calling [MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK](#gad1f36df770167384cc4e3f2c9be07d34).

Parameters
:   | mspi\_dev | Devicetree node identifier for the MSPI device whose struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") to create an initializer for |
    | --- | --- |

## [◆ ](#gaa9b32a8f6984468b5198524bea42ed8c)MSPI\_SCRAMBLE\_CONFIG\_DT\_INST

| #define MSPI\_SCRAMBLE\_CONFIG\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[MSPI\_SCRAMBLE\_CONFIG\_DT](#ga10ee161794b5c7986a4411b8fc90ea7d)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[MSPI\_SCRAMBLE\_CONFIG\_DT](#ga10ee161794b5c7986a4411b8fc90ea7d)

#define MSPI\_SCRAMBLE\_CONFIG\_DT(mspi\_dev)

Structure initializer for struct mspi\_scramble\_cfg from devicetree.

**Definition** devicetree.h:136

Structure initializer for struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") from devicetree instance.

This is equivalent to [MSPI\_SCRAMBLE\_CONFIG\_DT(DT\_DRV\_INST(inst))](#ga10ee161794b5c7986a4411b8fc90ea7d).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

## [◆ ](#gad1f36df770167384cc4e3f2c9be07d34)MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK

| #define MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK | ( |  | *mspi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

{ \

.enable = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(mspi\_dev, scramble\_config, 0), \

.address\_offset = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(mspi\_dev, scramble\_config, 1), \

.size = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(mspi\_dev, scramble\_config, 2), \

}

Structure initializer for struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") from devicetree.

This helper macro expands to a static initializer for a struct
[mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") by reading the relevant data from the devicetree.

Parameters
:   | mspi\_dev | Devicetree node identifier for the MSPI device whose struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") to create an initializer for |
    | --- | --- |

## [◆ ](#ga24a88651c634c5ab5630e7844ff98e4b)MSPI\_XIP\_CONFIG\_DT

| #define MSPI\_XIP\_CONFIG\_DT | ( |  | *mspi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(mspi\_dev, xip\_config), \

([MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK](#ga01a618fadb0147bf5abf42972a17f594)(mspi\_dev)), \

({}))

[MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK](#ga01a618fadb0147bf5abf42972a17f594)

#define MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK(mspi\_dev)

Structure initializer for struct mspi\_xip\_cfg from devicetree.

**Definition** devicetree.h:79

Structure initializer for struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") from devicetree.

This helper macro check whether xip\_config binding exist first before calling [MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK](#ga01a618fadb0147bf5abf42972a17f594).

Parameters
:   | mspi\_dev | Devicetree node identifier for the MSPI device whose struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") to create an initializer for |
    | --- | --- |

## [◆ ](#gafe739210f9f5cab4ab71bd61ec5af03f)MSPI\_XIP\_CONFIG\_DT\_INST

| #define MSPI\_XIP\_CONFIG\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

[MSPI\_XIP\_CONFIG\_DT](#ga24a88651c634c5ab5630e7844ff98e4b)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[MSPI\_XIP\_CONFIG\_DT](#ga24a88651c634c5ab5630e7844ff98e4b)

#define MSPI\_XIP\_CONFIG\_DT(mspi\_dev)

Structure initializer for struct mspi\_xip\_cfg from devicetree.

**Definition** devicetree.h:96

Structure initializer for struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") from devicetree instance.

This is equivalent to [MSPI\_XIP\_CONFIG\_DT(DT\_DRV\_INST(inst))](#ga24a88651c634c5ab5630e7844ff98e4b).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

## [◆ ](#ga01a618fadb0147bf5abf42972a17f594)MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK

| #define MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK | ( |  | *mspi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2mspi_2devicetree_8h.md)>`

**Value:**

{ \

.enable = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(mspi\_dev, xip\_config, 0), \

.address\_offset = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(mspi\_dev, xip\_config, 1), \

.size = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(mspi\_dev, xip\_config, 2), \

.permission = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(mspi\_dev, xip\_config, 3), \

}

Structure initializer for struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") from devicetree.

This helper macro expands to a static initializer for a struct
[mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") by reading the relevant data from the devicetree.

Parameters
:   | mspi\_dev | Devicetree node identifier for the MSPI device whose struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") to create an initializer for |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
