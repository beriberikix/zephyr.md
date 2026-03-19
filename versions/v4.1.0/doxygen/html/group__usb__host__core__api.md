---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__usb__host__core__api.html
original_path: doxygen/html/group__usb__host__core__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB Host Core API

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

USB HOST Core Layer API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [usbh\_contex](structusbh__contex.md) |
|  | USB host support runtime context. [More...](structusbh__contex.md#details) |
| struct | [usbh\_code\_triple](structusbh__code__triple.md) |
|  | USB Class Code triple. [More...](structusbh__code__triple.md#details) |
| struct | [usbh\_class\_data](structusbh__class__data.md) |
|  | USB host class data and class instance API. [More...](structusbh__class__data.md#details) |

| Macros | |
| --- | --- |
| #define | [USBH\_CONTROLLER\_DEFINE](#ga0a8885f9c6e8371ccc02ce191d010010)(device\_name, uhc\_dev) |
| #define | [USBH\_DEFINE\_CLASS](#ga21693790725ac6df7033e2edf67cfa29)(name) |

| Functions | |
| --- | --- |
| int | [usbh\_init](#gaaacb8627f0aae8f8965f923d1d1c786e) (struct [usbh\_contex](structusbh__contex.md) \*uhs\_ctx) |
|  | Initialize the USB host support;. |
| int | [usbh\_enable](#gab77ebba887ffd903de530a587e177a86) (struct [usbh\_contex](structusbh__contex.md) \*uhs\_ctx) |
|  | Enable the USB host support and class instances. |
| int | [usbh\_disable](#ga96ef9b1614874a1ed0e4c9f75bf815ec) (struct [usbh\_contex](structusbh__contex.md) \*uhs\_ctx) |
|  | Disable the USB host support. |
| int | [usbh\_shutdown](#ga4b2581d4e2c5350486ddb8483cd83de9) (struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
|  | Shutdown the USB host support. |

## Detailed Description

USB HOST Core Layer API.

## Macro Definition Documentation

## [◆ ](#ga0a8885f9c6e8371ccc02ce191d010010)USBH\_CONTROLLER\_DEFINE

| #define USBH\_CONTROLLER\_DEFINE | ( |  | *device\_name*, |
| --- | --- | --- | --- |
|  |  |  | *uhc\_dev* ) |

`#include <[usbh.h](usbh_8h.md)>`

**Value:**

[SYS\_BITARRAY\_DEFINE\_STATIC](group__bitarray__apis.md#ga2c55680355b67fc25125299a35f604d1)(ba\_##device\_name, 128); \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([usbh\_contex](structusbh__contex.md), device\_name) = { \

.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(device\_name), \

.mutex = Z\_MUTEX\_INITIALIZER(device\_name.mutex), \

.dev = uhc\_dev, \

.addr\_ba = &ba\_##device\_name, \

}

[SYS\_BITARRAY\_DEFINE\_STATIC](group__bitarray__apis.md#ga2c55680355b67fc25125299a35f604d1)

#define SYS\_BITARRAY\_DEFINE\_STATIC(name, total\_bits)

Create a static bitarray object.

**Definition** bitarray.h:83

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[usbh\_contex](structusbh__contex.md)

USB host support runtime context.

**Definition** usbh.h:39

## [◆ ](#ga21693790725ac6df7033e2edf67cfa29)USBH\_DEFINE\_CLASS

| #define USBH\_DEFINE\_CLASS | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbh.h](usbh_8h.md)>`

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([usbh\_class\_data](structusbh__class__data.md), name)

[usbh\_class\_data](structusbh__class__data.md)

USB host class data and class instance API.

**Definition** usbh.h:78

## Function Documentation

## [◆ ](#ga96ef9b1614874a1ed0e4c9f75bf815ec)usbh\_disable()

| int usbh\_disable | ( | struct [usbh\_contex](structusbh__contex.md) \* | *uhs\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbh.h](usbh_8h.md)>`

Disable the USB host support.

This function disables the USB host support.

Parameters
:   | [in] | uhs\_ctx | Pointer to USB host support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#gab77ebba887ffd903de530a587e177a86)usbh\_enable()

| int usbh\_enable | ( | struct [usbh\_contex](structusbh__contex.md) \* | *uhs\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbh.h](usbh_8h.md)>`

Enable the USB host support and class instances.

This function enables the USB host support.

Parameters
:   | [in] | uhs\_ctx | Pointer to USB host support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#gaaacb8627f0aae8f8965f923d1d1c786e)usbh\_init()

| int usbh\_init | ( | struct [usbh\_contex](structusbh__contex.md) \* | *uhs\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbh.h](usbh_8h.md)>`

Initialize the USB host support;.

Parameters
:   | [in] | uhs\_ctx | Pointer to USB host support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga4b2581d4e2c5350486ddb8483cd83de9)usbh\_shutdown()

| int usbh\_shutdown | ( | struct [usbh\_contex](structusbh__contex.md) \*const | *uhs\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbh.h](usbh_8h.md)>`

Shutdown the USB host support.

This function completely disables the USB host support.

Parameters
:   | [in] | uhs\_ctx | Pointer to USB host support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
