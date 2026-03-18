---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pio__rpi__pico_8h.html
original_path: doxygen/html/pio__rpi__pico_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pio\_rpi\_pico.h File Reference

`#include <[zephyr/devicetree/gpio.h](devicetree_2gpio_8h_source.md)>`  
`#include <hardware/pio.h>`

[Go to the source code of this file.](pio__rpi__pico_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RPI\_PICO\_PIO\_DEFINE\_PROGRAM](#a744449bb6c1a409a9d8677c66667ea9b)(name, wrap\_target, wrap, ...) |
|  | Utility macro to define a PIO program. |
| #define | [RPI\_PICO\_PIO\_GET\_WRAP\_TARGET](#a0d74a21471e301563224d4673ca1a738)(name) |
|  | Utility macro to get the wrap target of a program. |
| #define | [RPI\_PICO\_PIO\_GET\_WRAP](#a5cc3f015332a73cba6141e94b8fbe67e)(name) |
|  | Utility macro to get the wrap source of a program. |
| #define | [RPI\_PICO\_PIO\_GET\_PROGRAM](#a989341427ba2e681aba5c4d702d91927)(name) |
|  | Utility macro to get a pointer to a PIO program. |
| #define | [DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME](#a482acc1e13f4b6ef96f55a2c9e3b7a07)(node\_id, p\_name, p\_idx, g\_name, g\_idx) |
|  | Get a pin number from a pinctrl / group name and index. |
| #define | [DT\_INST\_RPI\_PICO\_PIO\_PIN\_BY\_NAME](#aa3620b14a4d34eed3302048d58a86893)(inst, p\_name, p\_idx, g\_name, g\_idx) |
|  | Get a pin number from a pinctrl / group name and index. |
| #define | [DT\_INST\_PIO\_PIN\_BY\_NAME](#ad2aef23ab08361004bba9209f9e612c1)(inst, name) |
|  | Get the pin number of a pin by its name. |

| Functions | |
| --- | --- |
| PIO | [pio\_rpi\_pico\_get\_pio](#af8e5b65f61711314c4c2a4f6a510209d) (const struct [device](structdevice.md) \*dev) |
|  | Get PIO object. |
| int | [pio\_rpi\_pico\_allocate\_sm](#ac3c70836b493b3fd535ea073c1f7d55b) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*sm) |
|  | Allocate a state machine. |

## Macro Definition Documentation

## [◆ ](#ad2aef23ab08361004bba9209f9e612c1)DT\_INST\_PIO\_PIN\_BY\_NAME

| #define DT\_INST\_PIO\_PIN\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

**Value:**

DT\_PIO\_PIN\_BY\_NAME([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

Get the pin number of a pin by its name.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | name of the pin (e.g. tx, rx, sck). |

## [◆ ](#aa3620b14a4d34eed3302048d58a86893)DT\_INST\_RPI\_PICO\_PIO\_PIN\_BY\_NAME

| #define DT\_INST\_RPI\_PICO\_PIO\_PIN\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *p\_name*, |
|  |  |  | *p\_idx*, |
|  |  |  | *g\_name*, |
|  |  |  | *g\_idx* ) |

**Value:**

[DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME](#a482acc1e13f4b6ef96f55a2c9e3b7a07)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), p\_name, p\_idx, g\_name, g\_idx)

[DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME](#a482acc1e13f4b6ef96f55a2c9e3b7a07)

#define DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME(node\_id, p\_name, p\_idx, g\_name, g\_idx)

Get a pin number from a pinctrl / group name and index.

**Definition** pio\_rpi\_pico.h:103

Get a pin number from a pinctrl / group name and index.

Parameters
:   | inst | instance number |
    | --- | --- |
    | p\_name | pinctrl name |
    | p\_idx | pinctrl index |
    | g\_name | group name |
    | g\_idx | group index |

Returns
:   pin number

See also
:   [DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME](#a482acc1e13f4b6ef96f55a2c9e3b7a07)

## [◆ ](#a482acc1e13f4b6ef96f55a2c9e3b7a07)DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME

| #define DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *p\_name*, |
|  |  |  | *p\_idx*, |
|  |  |  | *g\_name*, |
|  |  |  | *g\_idx* ) |

**Value:**

RP2\_GET\_PIN\_NUM([DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)( \

[DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)([DT\_PINCTRL\_BY\_NAME](group__devicetree-pinctrl.md#ga1cd336f902738fd684f3d81b3fb6caae)(node\_id, p\_name, p\_idx), g\_name), pinmux, g\_idx))

[DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)

#define DT\_CHILD(node\_id, child)

Get a node identifier for a child node.

**Definition** devicetree.h:421

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:761

[DT\_PINCTRL\_BY\_NAME](group__devicetree-pinctrl.md#ga1cd336f902738fd684f3d81b3fb6caae)

#define DT\_PINCTRL\_BY\_NAME(node\_id, name, idx)

Get a node identifier for a phandle inside a pinctrl node by name.

**Definition** pinctrl.h:81

Get a pin number from a pinctrl / group name and index.

Example devicetree fragment(s):

pinctrl {

pio\_child\_default: pio\_child\_default {

tx\_gpio {

pinmux = <PIO0\_P0>, <PIO0\_P2>;

};

rx\_gpio {

pinmux = <PIO0\_P1>;

input-enable;

};

};

};

pio {

status = "okay";

c: child {

pinctrl-0 = <&pio\_child\_default>;

pinctrl-names = "default";

};

};

Example usage:

[DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME](#a482acc1e13f4b6ef96f55a2c9e3b7a07)(node, default, 0, tx\_gpio, 0) // 0

[DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME](#a482acc1e13f4b6ef96f55a2c9e3b7a07)(node, default, 0, tx\_gpio, 1) // 2

[DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME](#a482acc1e13f4b6ef96f55a2c9e3b7a07)(node, default, 0, rx\_gpio, 0) // 1

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | p\_name | pinctrl name |
    | p\_idx | pinctrl index |
    | g\_name | group name |
    | g\_idx | group index |

Returns
:   pin number

## [◆ ](#a744449bb6c1a409a9d8677c66667ea9b)RPI\_PICO\_PIO\_DEFINE\_PROGRAM

| #define RPI\_PICO\_PIO\_DEFINE\_PROGRAM | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *wrap\_target*, |
|  |  |  | *wrap*, |
|  |  |  | ... ) |

**Value:**

static const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) name ## \_wrap\_target = wrap\_target; \

static const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) name ## \_wrap = wrap; \

static const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) name ## \_program\_instructions[] = { \

\_\_VA\_ARGS\_\_ \

}; \

static const struct pio\_program name ## \_program = { \

.instructions = name ## \_program\_instructions, \

.length = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(name ## \_program\_instructions), \

.origin = -1, \

}

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:124

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

Utility macro to define a PIO program.

The program is a list of 16 bit instructions, generated by the pioasm tool.

Parameters
:   | name | Name of the program. |
    | --- | --- |
    | wrap\_target | Wrap target as specified by the PIO program. |
    | wrap | Wrap source as specified by the PIO program. |
    | ... | Comma separated list of PIO instructions. |

## [◆ ](#a989341427ba2e681aba5c4d702d91927)RPI\_PICO\_PIO\_GET\_PROGRAM

| #define RPI\_PICO\_PIO\_GET\_PROGRAM | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

&name ## \_program

Utility macro to get a pointer to a PIO program.

Parameters
:   | name | Name of the program. |
    | --- | --- |

## [◆ ](#a5cc3f015332a73cba6141e94b8fbe67e)RPI\_PICO\_PIO\_GET\_WRAP

| #define RPI\_PICO\_PIO\_GET\_WRAP | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

name ## \_wrap

Utility macro to get the wrap source of a program.

Parameters
:   | name | Name of the program. |
    | --- | --- |

## [◆ ](#a0d74a21471e301563224d4673ca1a738)RPI\_PICO\_PIO\_GET\_WRAP\_TARGET

| #define RPI\_PICO\_PIO\_GET\_WRAP\_TARGET | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

name ## \_wrap\_target

Utility macro to get the wrap target of a program.

Parameters
:   | name | Name of the program. |
    | --- | --- |

## Function Documentation

## [◆ ](#ac3c70836b493b3fd535ea073c1f7d55b)pio\_rpi\_pico\_allocate\_sm()

| int pio\_rpi\_pico\_allocate\_sm | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *sm* ) |

Allocate a state machine.

Parameters
:   | dev | Pointer to device structure for rpi\_pio device instance |
    | --- | --- |
    | sm | Pointer to store allocated state machine |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EBUSY | if no state machines were available |

## [◆ ](#af8e5b65f61711314c4c2a4f6a510209d)pio\_rpi\_pico\_get\_pio()

| PIO pio\_rpi\_pico\_get\_pio | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get PIO object.

Parameters
:   | dev | Pointer to device structure for rpi\_pio device instance |
    | --- | --- |

Returns
:   PIO object

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [pio\_rpi\_pico](dir_226c323191fcba4fde21e80cdf6d98df.md)
- [pio\_rpi\_pico.h](pio__rpi__pico_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
