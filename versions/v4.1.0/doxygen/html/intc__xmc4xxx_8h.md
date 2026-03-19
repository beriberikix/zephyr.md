---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__xmc4xxx_8h.html
original_path: doxygen/html/intc__xmc4xxx_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_xmc4xxx.h File Reference

[Go to the source code of this file.](intc__xmc4xxx_8h_source.md)

| Functions | |
| --- | --- |
| int | [intc\_xmc4xxx\_gpio\_enable\_interrupt](#a0410ccf1ca439b7a70eb796292e8ef6c) (int port\_id, int pin, enum gpio\_int\_mode mode, enum gpio\_int\_trig trig, void(\*fn)(const struct [device](structdevice.md) \*, int), void \*user\_data) |
|  | Enable interrupt for specific port\_id and pin combination. |
| int | [intc\_xmc4xxx\_gpio\_disable\_interrupt](#a1583d09e4b260c07763e5419ca3411d1) (int port\_id, int pin) |
|  | Disable interrupt for specific port\_id and pin combination. |

## Function Documentation

## [◆ ](#a1583d09e4b260c07763e5419ca3411d1)intc\_xmc4xxx\_gpio\_disable\_interrupt()

| int intc\_xmc4xxx\_gpio\_disable\_interrupt | ( | int | *port\_id*, |
| --- | --- | --- | --- |
|  |  | int | *pin* ) |

Disable interrupt for specific port\_id and pin combination.

Parameters
:   | port\_id | Port index |
    | --- | --- |
    | pin | pin Pin the port |

Return values
:   | 0 | On susccess |
    | --- | --- |
    | -EINVAL | If the specific port\_id and pin combination has no interrupt enabled |

## [◆ ](#a0410ccf1ca439b7a70eb796292e8ef6c)intc\_xmc4xxx\_gpio\_enable\_interrupt()

| int intc\_xmc4xxx\_gpio\_enable\_interrupt | ( | int | *port\_id*, |
| --- | --- | --- | --- |
|  |  | int | *pin*, |
|  |  | enum gpio\_int\_mode | *mode*, |
|  |  | enum gpio\_int\_trig | *trig*, |
|  |  | void(\* | *fn*)(const struct [device](structdevice.md) \*, int), |
|  |  | void \* | *user\_data* ) |

Enable interrupt for specific port\_id and pin combination.

Parameters
:   | port\_id | Port index |
    | --- | --- |
    | pin | pin Pin the port |
    | mode | Level or edge interrupt |
    | trig | Trigger edge type (falling, rising or both) |
    | fn | Callback function |
    | user\_data | Parameter to the interrupt callback |

Return values
:   | 0 | On success |
    | --- | --- |
    | -ENOTSUP | If the specific port\_id/pin combination is not supported or not defined in the dts |
    | -EBUSY | If the interrupt line is already used by a different port\_id/pin |
    | -EINVAL | If the trigger combination is invalid |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_xmc4xxx.h](intc__xmc4xxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
