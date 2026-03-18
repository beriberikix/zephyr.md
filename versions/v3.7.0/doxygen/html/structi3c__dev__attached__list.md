---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structi3c__dev__attached__list.html
original_path: doxygen/html/structi3c__dev__attached__list.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_dev\_attached\_list Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

Structure for describing attached devices for a controller.
[More...](#details)

`#include <[i3c.h](i3c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [i3c\_addr\_slots](structi3c__addr__slots.md) | [addr\_slots](#ab5aba9e4e47d3acedc88754946e21474) |
|  | Address slots: |
| struct { |  |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)   [i3c](#a4cb8e85cf103f7368c2a16004baf1bad) |  |
|  | Linked list of attached I3C devices. [More...](#a4cb8e85cf103f7368c2a16004baf1bad) |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)   [i2c](#ab2688288f1ab550e4181ed4dc3dd057a) |  |
|  | Linked list of attached I2C devices. [More...](#ab2688288f1ab550e4181ed4dc3dd057a) |
| } | [devices](#ad539b98ce41e781da53f1fd46b03df63) |

## Detailed Description

Structure for describing attached devices for a controller.

This contains slists of attached I3C and I2C devices.

This is a helper struct that can be used by controller device driver to aid in device management.

## Field Documentation

## [◆ ](#ab5aba9e4e47d3acedc88754946e21474)addr\_slots

| struct [i3c\_addr\_slots](structi3c__addr__slots.md) i3c\_dev\_attached\_list::addr\_slots |
| --- |

Address slots:

- Aid in dynamic address assignment.
- Quick way to find out if a target address is a I3C or I2C device.

## [◆ ](#ad539b98ce41e781da53f1fd46b03df63)[struct]

| struct { ... } i3c\_dev\_attached\_list::devices |
| --- |

## [◆ ](#ab2688288f1ab550e4181ed4dc3dd057a)i2c

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) i3c\_dev\_attached\_list::i2c |
| --- |

Linked list of attached I2C devices.

## [◆ ](#a4cb8e85cf103f7368c2a16004baf1bad)i3c

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) i3c\_dev\_attached\_list::i3c |
| --- |

Linked list of attached I3C devices.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
