---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structhid__ops.html
original_path: doxygen/html/structhid__ops.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hid\_ops Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB HID class API](group__usb__hid__class.md) » [HID class USB specific definitions](group__usb__hid__device__api.md)

USB HID device interface.
[More...](#details)

`#include <[usb_hid.h](usb__hid_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [hid\_cb\_t](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee) | [get\_report](#a4ec029d8a0bc2acb1dd89a4ccdc4d652) |
| [hid\_cb\_t](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee) | [set\_report](#a5ab9c3bbb1d42b7557682ce4f9fc5de5) |
| [hid\_protocol\_cb\_t](group__usb__hid__device__api.md#gae3d308c55f5594cc0c926b52aaa28fc7) | [protocol\_change](#acc04ebec1deb335ef60bd3a01c6058d6) |
| [hid\_idle\_cb\_t](group__usb__hid__device__api.md#ga61b4facfbfb729159135f5c7534ca593) | [on\_idle](#a1acc7f77f6896d2925e63402f1b9ffdd) |
| [hid\_int\_ready\_callback](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0) | [int\_in\_ready](#af1eda81d93e935f9560a26344076f65e) |
| [hid\_int\_ready\_callback](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0) | [int\_out\_ready](#a42f454cc1ea1e7ae75e6fa4073111f48) |

## Detailed Description

USB HID device interface.

## Field Documentation

## [◆ ](#a4ec029d8a0bc2acb1dd89a4ccdc4d652)get\_report

| [hid\_cb\_t](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee) hid\_ops::get\_report |
| --- |

## [◆ ](#af1eda81d93e935f9560a26344076f65e)int\_in\_ready

| [hid\_int\_ready\_callback](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0) hid\_ops::int\_in\_ready |
| --- |

## [◆ ](#a42f454cc1ea1e7ae75e6fa4073111f48)int\_out\_ready

| [hid\_int\_ready\_callback](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0) hid\_ops::int\_out\_ready |
| --- |

## [◆ ](#a1acc7f77f6896d2925e63402f1b9ffdd)on\_idle

| [hid\_idle\_cb\_t](group__usb__hid__device__api.md#ga61b4facfbfb729159135f5c7534ca593) hid\_ops::on\_idle |
| --- |

## [◆ ](#acc04ebec1deb335ef60bd3a01c6058d6)protocol\_change

| [hid\_protocol\_cb\_t](group__usb__hid__device__api.md#gae3d308c55f5594cc0c926b52aaa28fc7) hid\_ops::protocol\_change |
| --- |

## [◆ ](#a5ab9c3bbb1d42b7557682ce4f9fc5de5)set\_report

| [hid\_cb\_t](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee) hid\_ops::set\_report |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usb\_hid.h](usb__hid_8h_source.md)

- [hid\_ops](structhid__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
