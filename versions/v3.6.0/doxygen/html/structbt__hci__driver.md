---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__hci__driver.html
original_path: doxygen/html/structbt__hci__driver.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_driver Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [HCI drivers](group__bt__hci__driver.md)

Abstraction which represents the HCI transport to the controller.
[More...](#details)

`#include <[hci_driver.h](hci__driver_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#a4036d2609565058a46b1a677fc7ec93e) |
|  | Name of the driver. |
| enum [bt\_hci\_driver\_bus](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) | [bus](#acd9a4d631da22b4638afd4593cff7d0c) |
|  | Bus of the transport (BT\_HCI\_DRIVER\_BUS\_\*). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [quirks](#a0dd8d706ee7ded476a90b19a946226b8) |
|  | Specific controller quirks. |
| int(\* | [open](#aabacc7c98a08a8a53f6aca436fac87d0) )(void) |
|  | Open the HCI transport. |
| int(\* | [close](#ae76bda7ebee44966554ba7b58da30e87) )(void) |
|  | Close the HCI transport. |
| int(\* | [send](#abcfc79474fc44aae260d61ff99fdb666) )(struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send HCI buffer to controller. |
| int(\* | [setup](#af2dd8b2817aab56738e7f447987efd2b) )(const struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*params) |
|  | HCI vendor-specific setup. |

## Detailed Description

Abstraction which represents the HCI transport to the controller.

This struct is used to represent the HCI transport to the Bluetooth controller.

## Field Documentation

## [◆ ](#acd9a4d631da22b4638afd4593cff7d0c)bus

| enum [bt\_hci\_driver\_bus](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) bt\_hci\_driver::bus |
| --- |

Bus of the transport (BT\_HCI\_DRIVER\_BUS\_\*).

## [◆ ](#ae76bda7ebee44966554ba7b58da30e87)close

| int(\* bt\_hci\_driver::close) (void) |
| --- |

Close the HCI transport.

Closes the HCI transport. This function must not return until the transport is closed.

If the driver uses its own RX thread, i.e. `CONFIG_BT_RECV_BLOCKING` is set, then this function is expected to abort that thread.

Returns
:   0 on success or negative error number on failure.

## [◆ ](#a4036d2609565058a46b1a677fc7ec93e)name

| const char\* bt\_hci\_driver::name |
| --- |

Name of the driver.

## [◆ ](#aabacc7c98a08a8a53f6aca436fac87d0)open

| int(\* bt\_hci\_driver::open) (void) |
| --- |

Open the HCI transport.

Opens the HCI transport for operation. This function must not return until the transport is ready for operation, meaning it is safe to start calling the [send()](#abcfc79474fc44aae260d61ff99fdb666) handler.

If the driver uses its own RX thread, i.e. `CONFIG_BT_RECV_BLOCKING` is set, then this function is expected to start that thread.

Returns
:   0 on success or negative error number on failure.

## [◆ ](#a0dd8d706ee7ded476a90b19a946226b8)quirks

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_hci\_driver::quirks |
| --- |

Specific controller quirks.

These are set by the HCI driver and acted upon by the host. They can either be statically set at buildtime, or set at runtime before the HCI driver's [open()](#aabacc7c98a08a8a53f6aca436fac87d0) callback returns.

## [◆ ](#abcfc79474fc44aae260d61ff99fdb666)send

| int(\* bt\_hci\_driver::send) (struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

Send HCI buffer to controller.

Send an HCI command or ACL data to the controller. The exact type of the data can be checked with the help of [bt\_buf\_get\_type()](group__bt__buf.md#ga2e35f0593e54d28bad62d6b8933f1599 "Get the buffer type.").

Note
:   This function must only be called from a cooperative thread.

Parameters
:   | buf | Buffer containing data to be sent to the controller. |
    | --- | --- |

Returns
:   0 on success or negative error number on failure.

## [◆ ](#af2dd8b2817aab56738e7f447987efd2b)setup

| int(\* bt\_hci\_driver::setup) (const struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*params) |
| --- |

HCI vendor-specific setup.

Executes vendor-specific commands sequence to initialize BT Controller before BT Host executes Reset sequence.

Note
:   `CONFIG_BT_HCI_SETUP` must be selected for this field to be available.

Returns
:   0 on success or negative error number on failure.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/bluetooth/[hci\_driver.h](hci__driver_8h_source.md)

- [bt\_hci\_driver](structbt__hci__driver.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
