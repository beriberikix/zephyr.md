---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/intc__rz__ext__irq_8h.html
original_path: doxygen/html/intc__rz__ext__irq_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_rz\_ext\_irq.h File Reference

[Go to the source code of this file.](intc__rz__ext__irq_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZ\_EXT\_IRQ\_TRIG\_FALLING](#a17f720465c2865fd41086d7529b58065)   0 |
| #define | [RZ\_EXT\_IRQ\_TRIG\_RISING](#ae86170a06f383179bee5d69b37021205)   1 |
| #define | [RZ\_EXT\_IRQ\_TRIG\_BOTH\_EDGE](#acde0f849883aa9b57e93b056754d4dbb)   2 |
| #define | [RZ\_EXT\_IRQ\_TRIG\_LEVEL\_LOW](#a2ac25bcef358c7dad3620ba42ff0fc2c)   3 |

| Typedefs | |
| --- | --- |
| typedef void(\* | [intc\_rz\_ext\_irq\_callback\_t](#a1c6d9f3910b3d82378ab40219828184a)) (void \*arg) |
|  | RZ external interrupt callback. |

| Functions | |
| --- | --- |
| int | [intc\_rz\_ext\_irq\_enable](#a08eb727b662be3e71d70c5fa88e95b7a) (const struct [device](structdevice.md) \*dev) |
|  | Enable external interrupt for specified channel. |
| int | [intc\_rz\_ext\_irq\_disable](#a9a372d975e6507a4d34c0766f22a368a) (const struct [device](structdevice.md) \*dev) |
|  | Disable external interrupt for specified channel. |
| int | [intc\_rz\_ext\_irq\_set\_callback](#af40022fc3bb2e30df6513c4172672235) (const struct [device](structdevice.md) \*dev, [intc\_rz\_ext\_irq\_callback\_t](#a1c6d9f3910b3d82378ab40219828184a) cb, void \*arg) |
|  | Updates the user callback. |
| int | [intc\_rz\_ext\_irq\_set\_type](#a913bfcbf3ff2161da4c2a45a77781452) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) trig) |
|  | Change trigger external interrupt type for specified channel. |

## Macro Definition Documentation

## [◆ ](#acde0f849883aa9b57e93b056754d4dbb)RZ\_EXT\_IRQ\_TRIG\_BOTH\_EDGE

| #define RZ\_EXT\_IRQ\_TRIG\_BOTH\_EDGE   2 |
| --- |

## [◆ ](#a17f720465c2865fd41086d7529b58065)RZ\_EXT\_IRQ\_TRIG\_FALLING

| #define RZ\_EXT\_IRQ\_TRIG\_FALLING   0 |
| --- |

## [◆ ](#a2ac25bcef358c7dad3620ba42ff0fc2c)RZ\_EXT\_IRQ\_TRIG\_LEVEL\_LOW

| #define RZ\_EXT\_IRQ\_TRIG\_LEVEL\_LOW   3 |
| --- |

## [◆ ](#ae86170a06f383179bee5d69b37021205)RZ\_EXT\_IRQ\_TRIG\_RISING

| #define RZ\_EXT\_IRQ\_TRIG\_RISING   1 |
| --- |

## Typedef Documentation

## [◆ ](#a1c6d9f3910b3d82378ab40219828184a)intc\_rz\_ext\_irq\_callback\_t

| typedef void(\* intc\_rz\_ext\_irq\_callback\_t) (void \*arg) |
| --- |

RZ external interrupt callback.

## Function Documentation

## [◆ ](#a9a372d975e6507a4d34c0766f22a368a)intc\_rz\_ext\_irq\_disable()

| int intc\_rz\_ext\_irq\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable external interrupt for specified channel.

Parameters
:   | dev | pointer to interrupt controller instance |
    | --- | --- |

Returns
:   0 on success, or negative value on error

## [◆ ](#a08eb727b662be3e71d70c5fa88e95b7a)intc\_rz\_ext\_irq\_enable()

| int intc\_rz\_ext\_irq\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable external interrupt for specified channel.

Parameters
:   | dev | pointer to interrupt controller instance |
    | --- | --- |

Returns
:   0 on success, or negative value on error

## [◆ ](#af40022fc3bb2e30df6513c4172672235)intc\_rz\_ext\_irq\_set\_callback()

| int intc\_rz\_ext\_irq\_set\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [intc\_rz\_ext\_irq\_callback\_t](#a1c6d9f3910b3d82378ab40219828184a) | *cb*, |
|  |  | void \* | *arg* ) |

Updates the user callback.

Parameters
:   | dev | pointer to interrupt controller instance |
    | --- | --- |
    | cb | callback to set |
    | arg | user data passed to callback |

Returns
:   0 on success, or negative value on error

## [◆ ](#a913bfcbf3ff2161da4c2a45a77781452)intc\_rz\_ext\_irq\_set\_type()

| int intc\_rz\_ext\_irq\_set\_type | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *trig* ) |

Change trigger external interrupt type for specified channel.

Parameters
:   | dev | pointer to interrupt controller instance |
    | --- | --- |
    | trig | trigger type to be changed |

Returns
:   0 on success, or negative value on error

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_rz\_ext\_irq.h](intc__rz__ext__irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
