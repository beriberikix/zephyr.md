---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__setup__params.html
original_path: doxygen/html/structbt__hci__setup__params.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_setup\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth HCI APIs](group__bt__hci__api.md)

`#include <[bluetooth.h](drivers_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_t](structbt__addr__t.md) | [public\_addr](#a6aea62826eeab39e6af40f9005548f3f) |
|  | The public identity address to give to the controller. |

## Field Documentation

## [◆ ](#a6aea62826eeab39e6af40f9005548f3f)public\_addr

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_setup\_params::public\_addr |
| --- |

The public identity address to give to the controller.

This field is used when the driver selects `CONFIG_BT_HCI_SET_PUBLIC_ADDR` to indicate that it supports setting the controller's public address.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[bluetooth.h](drivers_2bluetooth_8h_source.md)

- [bt\_hci\_setup\_params](structbt__hci__setup__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
