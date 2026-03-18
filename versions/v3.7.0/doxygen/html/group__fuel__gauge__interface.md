---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__fuel__gauge__interface.html
original_path: doxygen/html/group__fuel__gauge__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Fuel Gauge Interface

[Device Driver APIs](group__io__interfaces.md)

Fuel Gauge Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| union | [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) |
|  | Property field to value/type union. [More...](unionfuel__gauge__prop__val.md#details) |
| struct | [sbs\_gauge\_manufacturer\_name](structsbs__gauge__manufacturer__name.md) |
| struct | [sbs\_gauge\_device\_name](structsbs__gauge__device__name.md) |
| struct | [sbs\_gauge\_device\_chemistry](structsbs__gauge__device__chemistry.md) |
| struct | [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE](#ga824e00f1d607cdfe2598625f154636f1)   20 |
|  | Data structures for reading SBS buffer properties. |
| #define | [SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE](#ga41b8379542b9cbd0b3ee9e1bbe4bc599)   20 |
| #define | [SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE](#gafe9bdc00d856d4cc787265edb7eb0ed2)   4 |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) |
| typedef int(\* | [fuel\_gauge\_get\_property\_t](#gaed940ae925236ad2f25cf05d78304568)) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val) |
|  | Callback API for getting a fuel\_gauge property. |
| typedef int(\* | [fuel\_gauge\_set\_property\_t](#gae87a20a20f4f1fbb74d72afb2bcee4c9)) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val) |
|  | Callback API for setting a fuel\_gauge property. |
| typedef int(\* | [fuel\_gauge\_get\_buffer\_property\_t](#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) prop\_type, void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dst\_len) |
|  | Callback API for getting a fuel\_gauge buffer property. |
| typedef int(\* | [fuel\_gauge\_battery\_cutoff\_t](#ga698c8f84da7d1cbe7db1fc024e2388b7)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API for doing a battery cutoff. |

| Enumerations | |
| --- | --- |
| enum | [fuel\_gauge\_prop\_type](#gae49908857800bdd010d59895cfad9171) {     [FUEL\_GAUGE\_AVG\_CURRENT](#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396) = 0 , [FUEL\_GAUGE\_BATTERY\_CUTOFF](#ggae49908857800bdd010d59895cfad9171ad431ab05b79f942dd500ce84980cf81f) , [FUEL\_GAUGE\_CURRENT](#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354) , [FUEL\_GAUGE\_CHARGE\_CUTOFF](#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f) ,     [FUEL\_GAUGE\_CYCLE\_COUNT](#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984) , [FUEL\_GAUGE\_CONNECT\_STATE](#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d) , [FUEL\_GAUGE\_FLAGS](#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c) , [FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY](#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9) ,     [FUEL\_GAUGE\_PRESENT\_STATE](#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b) , [FUEL\_GAUGE\_REMAINING\_CAPACITY](#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4) , [FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY](#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd) , [FUEL\_GAUGE\_RUNTIME\_TO\_FULL](#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399) ,     [FUEL\_GAUGE\_SBS\_MFR\_ACCESS](#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd) , [FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE](#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee) , [FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE](#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b) , [FUEL\_GAUGE\_TEMPERATURE](#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009) ,     [FUEL\_GAUGE\_VOLTAGE](#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71) , [FUEL\_GAUGE\_SBS\_MODE](#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae) , [FUEL\_GAUGE\_CHARGE\_CURRENT](#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e) , [FUEL\_GAUGE\_CHARGE\_VOLTAGE](#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920) ,     [FUEL\_GAUGE\_STATUS](#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40) , [FUEL\_GAUGE\_DESIGN\_CAPACITY](#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67) , [FUEL\_GAUGE\_DESIGN\_VOLTAGE](#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf) , [FUEL\_GAUGE\_SBS\_ATRATE](#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58) ,     [FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL](#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70) , [FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY](#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0) , [FUEL\_GAUGE\_SBS\_ATRATE\_OK](#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec) , [FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM](#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2) ,     [FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM](#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a) , [FUEL\_GAUGE\_MANUFACTURER\_NAME](#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8) , [FUEL\_GAUGE\_DEVICE\_NAME](#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10) , [FUEL\_GAUGE\_DEVICE\_CHEMISTRY](#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9) ,     [FUEL\_GAUGE\_COMMON\_COUNT](#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815) , [FUEL\_GAUGE\_CUSTOM\_BEGIN](#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584) , [FUEL\_GAUGE\_PROP\_MAX](#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81) = UINT16\_MAX   } |

| Functions | |
| --- | --- |
| int | [fuel\_gauge\_get\_prop](#gab84999beab9a43241992945a3b2d37e1) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val) |
|  | Fetch a battery fuel-gauge property. |
| int | [fuel\_gauge\_get\_props](#gac721c19bc2c9714c11ede5e6d86fd0b0) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) \*props, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fetch multiple battery fuel-gauge properties. |
| int | [fuel\_gauge\_set\_prop](#ga936be681a82f173b664ae2187bc5a73d) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val) |
|  | Set a battery fuel-gauge property. |
| int | [fuel\_gauge\_set\_props](#ga55bb2be9c9eae7c3a8d01df051178d01) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) \*props, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set a battery fuel-gauge property. |
| int | [fuel\_gauge\_get\_buffer\_prop](#ga7e6cb77d2d4dd7a0feb25c92d031614c) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) prop\_type, void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dst\_len) |
|  | Fetch a battery fuel-gauge buffer property. |
| int | [fuel\_gauge\_battery\_cutoff](#ga763a40688dc8fc6a0ba85fdc79178ebc) (const struct [device](structdevice.md) \*dev) |
|  | Have fuel gauge cutoff its associated battery. |

## Detailed Description

Fuel Gauge Interface.

Since
:   3.3

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#gafe9bdc00d856d4cc787265edb7eb0ed2)SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE

| #define SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE   4 |
| --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

## [◆ ](#ga41b8379542b9cbd0b3ee9e1bbe4bc599)SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE

| #define SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE   20 |
| --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

## [◆ ](#ga824e00f1d607cdfe2598625f154636f1)SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE

| #define SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE   20 |
| --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Data structures for reading SBS buffer properties.

## Typedef Documentation

## [◆ ](#ga698c8f84da7d1cbe7db1fc024e2388b7)fuel\_gauge\_battery\_cutoff\_t

| typedef int(\* fuel\_gauge\_battery\_cutoff\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Callback API for doing a battery cutoff.

See [fuel\_gauge\_battery\_cutoff()](#ga763a40688dc8fc6a0ba85fdc79178ebc) for argument description

## [◆ ](#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)fuel\_gauge\_get\_buffer\_property\_t

| typedef int(\* fuel\_gauge\_get\_buffer\_property\_t) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) prop\_type, void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dst\_len) |
| --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Callback API for getting a fuel\_gauge buffer property.

See fuel\_gauge\_get\_buffer\_property() for argument description

## [◆ ](#gaed940ae925236ad2f25cf05d78304568)fuel\_gauge\_get\_property\_t

| typedef int(\* fuel\_gauge\_get\_property\_t) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val) |
| --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Callback API for getting a fuel\_gauge property.

See fuel\_gauge\_get\_property() for argument description

## [◆ ](#ga633eb1cb8dd64123252634b833b2f806)fuel\_gauge\_prop\_t

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) |
| --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

## [◆ ](#gae87a20a20f4f1fbb74d72afb2bcee4c9)fuel\_gauge\_set\_property\_t

| typedef int(\* fuel\_gauge\_set\_property\_t) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val) |
| --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Callback API for setting a fuel\_gauge property.

See fuel\_gauge\_set\_property() for argument description

## Enumeration Type Documentation

## [◆ ](#gae49908857800bdd010d59895cfad9171)fuel\_gauge\_prop\_type

| enum [fuel\_gauge\_prop\_type](#gae49908857800bdd010d59895cfad9171) |
| --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

| Enumerator | |
| --- | --- |
| FUEL\_GAUGE\_AVG\_CURRENT | Runtime Dynamic Battery Parameters.  Provide a 1 minute average of the current on the battery. Does not check for flags or whether those values are bad readings. See driver instance header for details on implementation and how the average is calculated. Units in uA negative=discharging |
| FUEL\_GAUGE\_BATTERY\_CUTOFF | Used to cutoff the battery from the system - useful for storage/shipping of devices. |
| FUEL\_GAUGE\_CURRENT | Battery current (uA); negative=discharging. |
| FUEL\_GAUGE\_CHARGE\_CUTOFF | Whether the battery underlying the fuel-gauge is cut off from charge. |
| FUEL\_GAUGE\_CYCLE\_COUNT | Cycle count in 1/100ths (number of charge/discharge cycles). |
| FUEL\_GAUGE\_CONNECT\_STATE | Connect state of battery. |
| FUEL\_GAUGE\_FLAGS | General Error/Runtime Flags. |
| FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY | Full Charge Capacity in uAh (might change in some implementations to determine wear). |
| FUEL\_GAUGE\_PRESENT\_STATE | Is the battery physically present. |
| FUEL\_GAUGE\_REMAINING\_CAPACITY | Remaining capacity in uAh. |
| FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY | Remaining battery life time in minutes. |
| FUEL\_GAUGE\_RUNTIME\_TO\_FULL | Remaining time in minutes until battery reaches full charge. |
| FUEL\_GAUGE\_SBS\_MFR\_ACCESS | Retrieve word from SBS1.1 ManufactuerAccess. |
| FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE | Absolute state of charge (percent, 0-100) - expressed as % of design capacity. |
| FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE | Relative state of charge (percent, 0-100) - expressed as % of full charge capacity. |
| FUEL\_GAUGE\_TEMPERATURE | Temperature in 0.1 K. |
| FUEL\_GAUGE\_VOLTAGE | Battery voltage (uV). |
| FUEL\_GAUGE\_SBS\_MODE | Battery Mode (flags). |
| FUEL\_GAUGE\_CHARGE\_CURRENT | Battery desired Max Charging Current (uA). |
| FUEL\_GAUGE\_CHARGE\_VOLTAGE | Battery desired Max Charging Voltage (uV). |
| FUEL\_GAUGE\_STATUS | Alarm, Status and Error codes (flags). |
| FUEL\_GAUGE\_DESIGN\_CAPACITY | Design Capacity (mAh or 10mWh). |
| FUEL\_GAUGE\_DESIGN\_VOLTAGE | Design Voltage (mV). |
| FUEL\_GAUGE\_SBS\_ATRATE | AtRate (mA or 10 mW). |
| FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL | AtRateTimeToFull (minutes). |
| FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY | AtRateTimeToEmpty (minutes). |
| FUEL\_GAUGE\_SBS\_ATRATE\_OK | AtRateOK (boolean). |
| FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM | Remaining Capacity Alarm (mAh or 10mWh). |
| FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM | Remaining Time Alarm (minutes). |
| FUEL\_GAUGE\_MANUFACTURER\_NAME | Manufacturer of pack (1 byte length + 20 bytes data). |
| FUEL\_GAUGE\_DEVICE\_NAME | Name of pack (1 byte length + 20 bytes data). |
| FUEL\_GAUGE\_DEVICE\_CHEMISTRY | Chemistry (1 byte length + 4 bytes data). |
| FUEL\_GAUGE\_COMMON\_COUNT | Reserved to demark end of common fuel gauge properties. |
| FUEL\_GAUGE\_CUSTOM\_BEGIN | Reserved to demark downstream custom properties - use this value as the actual value may change over future versions of this API. |
| FUEL\_GAUGE\_PROP\_MAX | Reserved to demark end of valid enum properties. |

## Function Documentation

## [◆ ](#ga763a40688dc8fc6a0ba85fdc79178ebc)fuel\_gauge\_battery\_cutoff()

| int fuel\_gauge\_battery\_cutoff | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Have fuel gauge cutoff its associated battery.

Parameters
:   | dev | Pointer to the battery fuel-gauge device |
    | --- | --- |

Returns
:   return=0 if successful and battery cutoff is now in process, return < 0 if failed to do battery cutoff.

## [◆ ](#ga7e6cb77d2d4dd7a0feb25c92d031614c)fuel\_gauge\_get\_buffer\_prop()

| int fuel\_gauge\_get\_buffer\_prop | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) | *prop\_type*, |
|  |  | void \* | *dst*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *dst\_len* ) |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Fetch a battery fuel-gauge buffer property.

Parameters
:   | dev | Pointer to the battery fuel-gauge device |
    | --- | --- |
    | prop\_type | Type of property to be fetched from device |
    | dst | byte array or struct that will hold the buffer data that is read from the fuel gauge |
    | dst\_len | the length of the destination array in bytes |

Returns
:   return=0 if successful, return < 0 if getting property failed, return 0 on success

## [◆ ](#gab84999beab9a43241992945a3b2d37e1)fuel\_gauge\_get\_prop()

| int fuel\_gauge\_get\_prop | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) | *prop*, |
|  |  | union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \* | *val* ) |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Fetch a battery fuel-gauge property.

Parameters
:   | dev | Pointer to the battery fuel-gauge device |
    | --- | --- |
    | prop | Type of property to be fetched from device |
    | val | pointer to a union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md "Property field to value/type union.") where the property is read into from the fuel gauge device. |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#gac721c19bc2c9714c11ede5e6d86fd0b0)fuel\_gauge\_get\_props()

| int fuel\_gauge\_get\_props | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) \* | *props*, |
|  |  | union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \* | *vals*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Fetch multiple battery fuel-gauge properties.

The default implementation is the same as calling [fuel\_gauge\_get\_prop()](#gab84999beab9a43241992945a3b2d37e1) multiple times. A driver may implement the get\_properties field of the fuel gauge driver APIs struct to override this implementation.

Parameters
:   | dev | Pointer to the battery fuel-gauge device |
    | --- | --- |
    | props | Array of the type of property to be fetched from device, each index corresponds to the same index of the vals input array. |
    | vals | Pointer to array of union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md "Property field to value/type union.") where the property is read into from the fuel gauge device. The vals array is not permuted. |
    | len | number of properties in props & vals array |

Returns
:   0 if successful, negative errno code of first failing property

## [◆ ](#ga936be681a82f173b664ae2187bc5a73d)fuel\_gauge\_set\_prop()

| int fuel\_gauge\_set\_prop | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) | *prop*, |
|  |  | union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) | *val* ) |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Set a battery fuel-gauge property.

Parameters
:   | dev | Pointer to the battery fuel-gauge device |
    | --- | --- |
    | prop | Type of property that's being set |
    | val | Value to set associated prop property. |

Returns
:   0 if successful, negative errno code of first failing property

## [◆ ](#ga55bb2be9c9eae7c3a8d01df051178d01)fuel\_gauge\_set\_props()

| int fuel\_gauge\_set\_props | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [fuel\_gauge\_prop\_t](#ga633eb1cb8dd64123252634b833b2f806) \* | *props*, |
|  |  | union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \* | *vals*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[fuel_gauge.h](fuel__gauge_8h.md)>`

Set a battery fuel-gauge property.

Parameters
:   | dev | Pointer to the battery fuel-gauge device |
    | --- | --- |
    | props | Array of the type of property to be set, each index corresponds to the same index of the vals input array. |
    | vals | Pointer to array of union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md "Property field to value/type union.") where the property is written the fuel gauge device. The vals array is not permuted. |
    | len | number of properties in props array |

Returns
:   return=0 if successful. Otherwise, return array index of failing property.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
