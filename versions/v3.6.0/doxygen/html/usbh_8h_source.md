---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbh_8h_source.html
original_path: doxygen/html/usbh_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbh.h

[Go to the documentation of this file.](usbh_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_USBH\_H\_

15#define ZEPHYR\_INCLUDE\_USBH\_H\_

16

17#include <[stdint.h](stdint_8h.md)>

18#include <[zephyr/device.h](device_8h.md)>

19#include <[zephyr/net/buf.h](net_2buf_8h.md)>

20#include <[zephyr/sys/dlist.h](dlist_8h.md)>

21#include <[zephyr/drivers/usb/uhc.h](uhc_8h.md)>

22#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

34

[ 38](structusbh__contex.md)struct [usbh\_contex](structusbh__contex.md) {

[ 40](structusbh__contex.md#aa2e6c8e95ddf1942fda07ed6bf49b8a9) const char \*[name](structusbh__contex.md#aa2e6c8e95ddf1942fda07ed6bf49b8a9);

[ 42](structusbh__contex.md#aa8264dd792ac5c9e99f35c182d80e7f8) struct [k\_mutex](structk__mutex.md) [mutex](structusbh__contex.md#aa8264dd792ac5c9e99f35c182d80e7f8);

[ 44](structusbh__contex.md#a08fd4b998cc4db5781caeb62f06a5028) const struct [device](structdevice.md) \*[dev](structusbh__contex.md#a08fd4b998cc4db5781caeb62f06a5028);

[ 46](structusbh__contex.md#a4cc8b4d571e6c74f65cdf9889e68b0f7) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [peripherals](structusbh__contex.md#a4cc8b4d571e6c74f65cdf9889e68b0f7);

47};

48

[ 49](group__usb__host__core__api.md#ga0a8885f9c6e8371ccc02ce191d010010)#define USBH\_CONTROLLER\_DEFINE(device\_name, uhc\_dev) \

50 static STRUCT\_SECTION\_ITERABLE(usbh\_contex, device\_name) = { \

51 .name = STRINGIFY(device\_name), \

52 .mutex = Z\_MUTEX\_INITIALIZER(device\_name.mutex), \

53 .dev = uhc\_dev, \

54 }

55

[ 59](structusbh__code__triple.md)struct [usbh\_code\_triple](structusbh__code__triple.md) {

[ 61](structusbh__code__triple.md#a7948eedb27e5353f5fcb3d1bf2c63887) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dclass](structusbh__code__triple.md#a7948eedb27e5353f5fcb3d1bf2c63887);

[ 63](structusbh__code__triple.md#aaa5f3d7d43eb606327b8c7bfde4fb128) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sub](structusbh__code__triple.md#aaa5f3d7d43eb606327b8c7bfde4fb128);

[ 65](structusbh__code__triple.md#a168889fd628aa7fe86bf638fac5874a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [proto](structusbh__code__triple.md#a168889fd628aa7fe86bf638fac5874a9);

66};

67

[ 71](structusbh__class__data.md)struct [usbh\_class\_data](structusbh__class__data.md) {

[ 73](structusbh__class__data.md#a3db5ee91a0ecb31f12bb46e6f93d1291) struct [usbh\_code\_triple](structusbh__code__triple.md) [code](structusbh__class__data.md#a3db5ee91a0ecb31f12bb46e6f93d1291);

74

76 /\* int (\*init)(struct usbh\_contex \*const uhs\_ctx); \*/

[ 78](structusbh__class__data.md#a0818ed7ce3c9a1444140158dcd276927) int (\*[request](structusbh__class__data.md#a0818ed7ce3c9a1444140158dcd276927))(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx,

79 struct [uhc\_transfer](structuhc__transfer.md) \*const xfer, int err);

[ 81](structusbh__class__data.md#a6c2fbedf9882e4a7d8e5b65aa3fe1734) int (\*[connected](structusbh__class__data.md#a6c2fbedf9882e4a7d8e5b65aa3fe1734))(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx);

[ 83](structusbh__class__data.md#ad80163e078fd59b29a45f24a6c7df8e5) int (\*[removed](structusbh__class__data.md#ad80163e078fd59b29a45f24a6c7df8e5))(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx);

[ 85](structusbh__class__data.md#a167b3103b6bc3bb9ab4ffbca0e9ad9d4) int (\*[rwup](structusbh__class__data.md#a167b3103b6bc3bb9ab4ffbca0e9ad9d4))(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx);

[ 87](structusbh__class__data.md#abf773a53750a44d418cef64b1e14dabe) int (\*[suspended](structusbh__class__data.md#abf773a53750a44d418cef64b1e14dabe))(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx);

[ 89](structusbh__class__data.md#aa23cbff522562c4974ade761474c65d7) int (\*[resumed](structusbh__class__data.md#aa23cbff522562c4974ade761474c65d7))(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx);

90};

91

[ 94](group__usb__host__core__api.md#ga21693790725ac6df7033e2edf67cfa29)#define USBH\_DEFINE\_CLASS(name) \

95 static STRUCT\_SECTION\_ITERABLE(usbh\_class\_data, name)

96

97

[ 105](group__usb__host__core__api.md#gaaacb8627f0aae8f8965f923d1d1c786e)int [usbh\_init](group__usb__host__core__api.md#gaaacb8627f0aae8f8965f923d1d1c786e)(struct [usbh\_contex](structusbh__contex.md) \*uhs\_ctx);

106

[ 116](group__usb__host__core__api.md#gab77ebba887ffd903de530a587e177a86)int [usbh\_enable](group__usb__host__core__api.md#gab77ebba887ffd903de530a587e177a86)(struct [usbh\_contex](structusbh__contex.md) \*uhs\_ctx);

117

[ 127](group__usb__host__core__api.md#ga96ef9b1614874a1ed0e4c9f75bf815ec)int [usbh\_disable](group__usb__host__core__api.md#ga96ef9b1614874a1ed0e4c9f75bf815ec)(struct [usbh\_contex](structusbh__contex.md) \*uhs\_ctx);

128

[ 138](group__usb__host__core__api.md#ga4b2581d4e2c5350486ddb8483cd83de9)int [usbh\_shutdown](group__usb__host__core__api.md#ga4b2581d4e2c5350486ddb8483cd83de9)(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx);

139

143

144#ifdef \_\_cplusplus

145}

146#endif

147

148#endif /\* ZEPHYR\_INCLUDE\_USBH\_H\_ \*/

[device.h](device_8h.md)

[dlist.h](dlist_8h.md)

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:51

[usbh\_shutdown](group__usb__host__core__api.md#ga4b2581d4e2c5350486ddb8483cd83de9)

int usbh\_shutdown(struct usbh\_contex \*const uhs\_ctx)

Shutdown the USB host support.

[usbh\_disable](group__usb__host__core__api.md#ga96ef9b1614874a1ed0e4c9f75bf815ec)

int usbh\_disable(struct usbh\_contex \*uhs\_ctx)

Disable the USB host support.

[usbh\_init](group__usb__host__core__api.md#gaaacb8627f0aae8f8965f923d1d1c786e)

int usbh\_init(struct usbh\_contex \*uhs\_ctx)

Initialize the USB host support;.

[usbh\_enable](group__usb__host__core__api.md#gab77ebba887ffd903de530a587e177a86)

int usbh\_enable(struct usbh\_contex \*uhs\_ctx)

Enable the USB host support and class instances.

[buf.h](net_2buf_8h.md)

Buffer management.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[uhc\_transfer](structuhc__transfer.md)

UHC endpoint buffer info.

**Definition** uhc.h:47

[usbh\_class\_data](structusbh__class__data.md)

USB host class data and class instance API.

**Definition** usbh.h:71

[usbh\_class\_data::request](structusbh__class__data.md#a0818ed7ce3c9a1444140158dcd276927)

int(\* request)(struct usbh\_contex \*const uhs\_ctx, struct uhc\_transfer \*const xfer, int err)

Initialization of the class implementation.

**Definition** usbh.h:78

[usbh\_class\_data::rwup](structusbh__class__data.md#a167b3103b6bc3bb9ab4ffbca0e9ad9d4)

int(\* rwup)(struct usbh\_contex \*const uhs\_ctx)

Bus remote wakeup handler.

**Definition** usbh.h:85

[usbh\_class\_data::code](structusbh__class__data.md#a3db5ee91a0ecb31f12bb46e6f93d1291)

struct usbh\_code\_triple code

Class code supported by this instance.

**Definition** usbh.h:73

[usbh\_class\_data::connected](structusbh__class__data.md#a6c2fbedf9882e4a7d8e5b65aa3fe1734)

int(\* connected)(struct usbh\_contex \*const uhs\_ctx)

Device connected handler.

**Definition** usbh.h:81

[usbh\_class\_data::resumed](structusbh__class__data.md#aa23cbff522562c4974ade761474c65d7)

int(\* resumed)(struct usbh\_contex \*const uhs\_ctx)

Bus resumed handler.

**Definition** usbh.h:89

[usbh\_class\_data::suspended](structusbh__class__data.md#abf773a53750a44d418cef64b1e14dabe)

int(\* suspended)(struct usbh\_contex \*const uhs\_ctx)

Bus suspended handler.

**Definition** usbh.h:87

[usbh\_class\_data::removed](structusbh__class__data.md#ad80163e078fd59b29a45f24a6c7df8e5)

int(\* removed)(struct usbh\_contex \*const uhs\_ctx)

Device removed handler.

**Definition** usbh.h:83

[usbh\_code\_triple](structusbh__code__triple.md)

USB Class Code triple.

**Definition** usbh.h:59

[usbh\_code\_triple::proto](structusbh__code__triple.md#a168889fd628aa7fe86bf638fac5874a9)

uint8\_t proto

Class Protocol Code.

**Definition** usbh.h:65

[usbh\_code\_triple::dclass](structusbh__code__triple.md#a7948eedb27e5353f5fcb3d1bf2c63887)

uint8\_t dclass

Device Class Code.

**Definition** usbh.h:61

[usbh\_code\_triple::sub](structusbh__code__triple.md#aaa5f3d7d43eb606327b8c7bfde4fb128)

uint8\_t sub

Class Subclass Code.

**Definition** usbh.h:63

[usbh\_contex](structusbh__contex.md)

USB host support runtime context.

**Definition** usbh.h:38

[usbh\_contex::dev](structusbh__contex.md#a08fd4b998cc4db5781caeb62f06a5028)

const struct device \* dev

Pointer to UHC device struct.

**Definition** usbh.h:44

[usbh\_contex::peripherals](structusbh__contex.md#a4cc8b4d571e6c74f65cdf9889e68b0f7)

sys\_dlist\_t peripherals

peripheral list

**Definition** usbh.h:46

[usbh\_contex::name](structusbh__contex.md#aa2e6c8e95ddf1942fda07ed6bf49b8a9)

const char \* name

Name of the USB device.

**Definition** usbh.h:40

[usbh\_contex::mutex](structusbh__contex.md#aa8264dd792ac5c9e99f35c182d80e7f8)

struct k\_mutex mutex

Access mutex.

**Definition** usbh.h:42

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[uhc.h](uhc_8h.md)

USB host controller (UHC) driver API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usbh.h](usbh_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
