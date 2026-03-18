---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__hci__setup__params.html
original_path: doxygen/html/structbt__hci__setup__params.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_setup\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [HCI drivers](group__bt__hci__driver.md)

`#include <[hci_driver.h](hci__driver_8h_source.md)>`

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

- zephyr/drivers/bluetooth/[hci\_driver.h](hci__driver_8h_source.md)

- [bt\_hci\_setup\_params](structbt__hci__setup__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
