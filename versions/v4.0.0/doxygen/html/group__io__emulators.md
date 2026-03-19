---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__io__emulators.html
original_path: doxygen/html/group__io__emulators.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Emulator interface

[Testing](group__testing.md)

Emulators used to test drivers and higher-level code that uses them.
[More...](#details)

| Topics | |
| --- | --- |
|  | [I2C Emulation Interface](group__i2c__emul__interface.md) |
|  | I2C Emulation Interface. |
|  | [MSPI Emulation Interface](group__mspi__emul__interface.md) |
|  | MSPI Emulation Interface. |
|  | [SPI Emulation Interface](group__spi__emul__interface.md) |
|  | SPI Emulation Interface. |
|  | [UART Emulation Interface](group__uart__emul__interface.md) |
|  | UART Emulation Interface. |
|  | [eSPI Emulation Interface](group__espi__emul__interface.md) |
|  | eSPI Emulation Interface |

| Data Structures | |
| --- | --- |
| struct | [emul\_link\_for\_bus](structemul__link__for__bus.md) |
|  | Structure uniquely identifying a device to be emulated. [More...](structemul__link__for__bus.md#details) |
| struct | [emul\_list\_for\_bus](structemul__list__for__bus.md) |
|  | List of emulators attached to a bus. [More...](structemul__list__for__bus.md#details) |
| struct | [no\_bus\_emul](structno__bus__emul.md) |
|  | Emulator API stub when an emulator is not actually placed on a bus. [More...](structno__bus__emul.md#details) |
| struct | [emul](structemul.md) |
|  | An emulator instance - represents the *target* emulated device/peripheral that is interacted with through an emulated bus. [More...](structemul.md#details) |

| Macros | |
| --- | --- |
| #define | [EMUL\_DT\_NAME\_GET](#gac1638c8cad48dab50f9ebc83592236db)(node\_id) |
|  | Use the devicetree node identifier as a unique name. |
| #define | [EMUL\_DT\_DEFINE](#gad6292e3cd7f17a3600be396777f304c8)(node\_id, init\_fn, data\_ptr, cfg\_ptr, bus\_api, \_backend\_api) |
|  | Define a new emulator. |
| #define | [EMUL\_DT\_INST\_DEFINE](#gafe7f4912bcffed1366ce07d024a4f977)(inst, ...) |
|  | Like [EMUL\_DT\_DEFINE()](#gad6292e3cd7f17a3600be396777f304c8), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier. |
| #define | [EMUL\_DT\_GET](#ga300d997df388118ae380e79b972f85cf)(node\_id) |
|  | Get a const struct emul\* from a devicetree node identifier. |
| #define | [EMUL\_DT\_GET\_OR\_NULL](#gab37b4f8b4c434ca38f523eb6391d4e3b)(node\_id) |
|  | Utility macro to obtain an optional reference to an emulator. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [emul\_init\_t](#gaa6129de6e0edef345242559a3dac3a50)) (const struct [emul](structemul.md) \*[emul](structemul.md), const struct [device](structdevice.md) \*parent) |
|  | Standard callback for emulator initialisation providing the initialiser record and the device that calls the emulator functions. |

| Enumerations | |
| --- | --- |
| enum | [emul\_bus\_type](#ga39b7a9438507b0be95038fe9464762aa) {     [EMUL\_BUS\_TYPE\_I2C](#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f) , [EMUL\_BUS\_TYPE\_ESPI](#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1) , [EMUL\_BUS\_TYPE\_SPI](#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a) , [EMUL\_BUS\_TYPE\_MSPI](#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46) ,     [EMUL\_BUS\_TYPE\_UART](#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6) , [EMUL\_BUS\_TYPE\_NONE](#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d)   } |
|  | The types of supported buses. [More...](#ga39b7a9438507b0be95038fe9464762aa) |

| Functions | |
| --- | --- |
| int | [emul\_init\_for\_bus](#gad587b2852a182e1a7fdcb3b056d898f1) (const struct [device](structdevice.md) \*dev) |
|  | Set up a list of emulators. |
| const struct [emul](structemul.md) \* | [emul\_get\_binding](#gaad94c1e07998417cb9aa06d03be3b280) (const char \*name) |
|  | Retrieve the emul structure for an emulator by name. |

## Detailed Description

Emulators used to test drivers and higher-level code that uses them.

## Macro Definition Documentation

## [◆ ](#gad6292e3cd7f17a3600be396777f304c8)EMUL\_DT\_DEFINE

| #define EMUL\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *data\_ptr*, |
|  |  |  | *cfg\_ptr*, |
|  |  |  | *bus\_api*, |
|  |  |  | *\_backend\_api* ) |

`#include <[emul.h](drivers_2emul_8h.md)>`

**Value:**

static struct Z\_EMUL\_BUS(node\_id, [i2c\_emul](structi2c__emul.md), [espi\_emul](structespi__emul.md), [spi\_emul](structspi__emul.md), [mspi\_emul](structmspi__emul.md), [uart\_emul](structuart__emul.md), \

[no\_bus\_emul](structno__bus__emul.md)) Z\_EMUL\_REG\_BUS\_IDENTIFIER(node\_id) = { \

.api = bus\_api, \

IF\_ENABLED([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, reg), \

(.Z\_EMUL\_BUS(node\_id, addr, chipsel, chipsel, dev\_idx, dummy, addr) = \

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id),))}; \

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([emul](structemul.md), [EMUL\_DT\_NAME\_GET](#gac1638c8cad48dab50f9ebc83592236db)(node\_id)) \_\_used = { \

.init = (init\_fn), \

.dev = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)(node\_id), \

.cfg = (cfg\_ptr), \

.data = (data\_ptr), \

.bus\_type = Z\_EMUL\_BUS(node\_id, [EMUL\_BUS\_TYPE\_I2C](#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f), [EMUL\_BUS\_TYPE\_ESPI](#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1), \

[EMUL\_BUS\_TYPE\_SPI](#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a), [EMUL\_BUS\_TYPE\_MSPI](#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46), [EMUL\_BUS\_TYPE\_UART](#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6), \

[EMUL\_BUS\_TYPE\_NONE](#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d)), \

.bus = {.Z\_EMUL\_BUS(node\_id, i2c, espi, spi, mspi, uart, none) = \

&(Z\_EMUL\_REG\_BUS\_IDENTIFIER(node\_id))}, \

.backend\_api = (\_backend\_api), \

};

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:255

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3677

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2433

[EMUL\_DT\_NAME\_GET](#gac1638c8cad48dab50f9ebc83592236db)

#define EMUL\_DT\_NAME\_GET(node\_id)

Use the devicetree node identifier as a unique name.

**Definition** emul.h:111

[EMUL\_BUS\_TYPE\_SPI](#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a)

@ EMUL\_BUS\_TYPE\_SPI

**Definition** emul.h:40

[EMUL\_BUS\_TYPE\_I2C](#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f)

@ EMUL\_BUS\_TYPE\_I2C

**Definition** emul.h:38

[EMUL\_BUS\_TYPE\_MSPI](#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46)

@ EMUL\_BUS\_TYPE\_MSPI

**Definition** emul.h:41

[EMUL\_BUS\_TYPE\_ESPI](#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1)

@ EMUL\_BUS\_TYPE\_ESPI

**Definition** emul.h:39

[EMUL\_BUS\_TYPE\_NONE](#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d)

@ EMUL\_BUS\_TYPE\_NONE

**Definition** emul.h:43

[EMUL\_BUS\_TYPE\_UART](#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6)

@ EMUL\_BUS\_TYPE\_UART

**Definition** emul.h:42

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:82

[espi\_emul](structespi__emul.md)

Node in a linked list of emulators for eSPI devices.

**Definition** espi\_emul.h:111

[i2c\_emul](structi2c__emul.md)

Node in a linked list of emulators for I2C devices.

**Definition** i2c\_emul.h:37

[mspi\_emul](structmspi__emul.md)

Node in a linked list of emulators for MSPI devices.

**Definition** mspi\_emul.h:87

[no\_bus\_emul](structno__bus__emul.md)

Emulator API stub when an emulator is not actually placed on a bus.

**Definition** emul.h:73

[spi\_emul](structspi__emul.md)

Node in a linked list of emulators for SPI devices.

**Definition** spi\_emul.h:37

[uart\_emul](structuart__emul.md)

Node in a linked list of emulators for UART devices.

**Definition** uart\_emul.h:46

Define a new emulator.

This adds a new struct emul to the linker list of emulations. This is typically used in your emulator's [DT\_INST\_FOREACH\_STATUS\_OKAY()](group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7 "Call fn on all nodes with compatible DT_DRV_COMPAT and status okay.") clause.

Parameters
:   | node\_id | Node ID of the driver to emulate (e.g. [DT\_DRV\_INST(n)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible.")); the node\_id *MUST* have a corresponding [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization."). |
    | --- | --- |
    | init\_fn | function to call to initialise the emulator (see emul\_init typedef) |
    | data\_ptr | emulator-specific data |
    | cfg\_ptr | emulator-specific configuration data |
    | bus\_api | emulator-specific bus api |
    | \_backend\_api | emulator-specific backend api |

## [◆ ](#ga300d997df388118ae380e79b972f85cf)EMUL\_DT\_GET

| #define EMUL\_DT\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[emul.h](drivers_2emul_8h.md)>`

**Value:**

(&[EMUL\_DT\_NAME\_GET](#gac1638c8cad48dab50f9ebc83592236db)(node\_id))

Get a const struct emul\* from a devicetree node identifier.

Returns a pointer to an emulator object created from a devicetree node, if any device was allocated by an emulator implementation.

If no such device was allocated, this will fail at linker time. If you get an error that looks like undefined reference to \_\_device\_dts\_ord\_<N>, that is what happened. Check to make sure your emulator implementation is being compiled, usually by enabling the Kconfig options it requires.

Parameters
:   | node\_id | A devicetree node identifier |
    | --- | --- |

Returns
:   A pointer to the emul object created for that node

## [◆ ](#gab37b4f8b4c434ca38f523eb6391d4e3b)EMUL\_DT\_GET\_OR\_NULL

| #define EMUL\_DT\_GET\_OR\_NULL | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[emul.h](drivers_2emul_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_STATUS\_OKAY](group__devicetree-generic-exist.md#gaed773a8782fe00db90e8599ff673e8ed)(node\_id), ([EMUL\_DT\_GET](#ga300d997df388118ae380e79b972f85cf)(node\_id)), (NULL))

[DT\_NODE\_HAS\_STATUS\_OKAY](group__devicetree-generic-exist.md#gaed773a8782fe00db90e8599ff673e8ed)

#define DT\_NODE\_HAS\_STATUS\_OKAY(node\_id)

Does a node identifier refer to a node with a status okay?

**Definition** devicetree.h:3583

[EMUL\_DT\_GET](#ga300d997df388118ae380e79b972f85cf)

#define EMUL\_DT\_GET(node\_id)

Get a const struct emul\* from a devicetree node identifier.

**Definition** emul.h:186

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

Utility macro to obtain an optional reference to an emulator.

If the node identifier refers to a node with status okay, this returns [EMUL\_DT\_GET(node\_id)](#ga300d997df388118ae380e79b972f85cf). Otherwise, it returns NULL.

Parameters
:   | node\_id | A devicetree node identifier |
    | --- | --- |

Returns
:   a [emul](structemul.md "emul") reference for the node identifier, which may be NULL.

## [◆ ](#gafe7f4912bcffed1366ce07d024a4f977)EMUL\_DT\_INST\_DEFINE

| #define EMUL\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[emul.h](drivers_2emul_8h.md)>`

**Value:**

[EMUL\_DT\_DEFINE](#gad6292e3cd7f17a3600be396777f304c8)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

[EMUL\_DT\_DEFINE](#gad6292e3cd7f17a3600be396777f304c8)

#define EMUL\_DT\_DEFINE(node\_id, init\_fn, data\_ptr, cfg\_ptr, bus\_api, \_backend\_api)

Define a new emulator.

**Definition** emul.h:142

Like [EMUL\_DT\_DEFINE()](#gad6292e3cd7f17a3600be396777f304c8), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier.

Parameters
:   | inst | instance number. The `node_id` argument to EMUL\_DT\_DEFINE is set to [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible."). |
    | --- | --- |
    | ... | other parameters as expected by EMUL\_DT\_DEFINE. |

## [◆ ](#gac1638c8cad48dab50f9ebc83592236db)EMUL\_DT\_NAME\_GET

| #define EMUL\_DT\_NAME\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[emul.h](drivers_2emul_8h.md)>`

**Value:**

\_CONCAT(\_\_emulreg\_, node\_id)

Use the devicetree node identifier as a unique name.

Parameters
:   | node\_id | A devicetree node identifier |
    | --- | --- |

## Typedef Documentation

## [◆ ](#gaa6129de6e0edef345242559a3dac3a50)emul\_init\_t

| typedef int(\* emul\_init\_t) (const struct [emul](structemul.md) \*[emul](structemul.md), const struct [device](structdevice.md) \*parent) |
| --- |

`#include <[emul.h](drivers_2emul_8h.md)>`

Standard callback for emulator initialisation providing the initialiser record and the device that calls the emulator functions.

Parameters
:   | [emul](structemul.md "An emulator instance - represents the target emulated device/peripheral that is interacted with throu...") | Emulator to init |
    | --- | --- |
    | parent | Parent device that is using the emulator |

## Enumeration Type Documentation

## [◆ ](#ga39b7a9438507b0be95038fe9464762aa)emul\_bus\_type

| enum [emul\_bus\_type](#ga39b7a9438507b0be95038fe9464762aa) |
| --- |

`#include <[emul.h](drivers_2emul_8h.md)>`

The types of supported buses.

| Enumerator | |
| --- | --- |
| EMUL\_BUS\_TYPE\_I2C |  |
| EMUL\_BUS\_TYPE\_ESPI |  |
| EMUL\_BUS\_TYPE\_SPI |  |
| EMUL\_BUS\_TYPE\_MSPI |  |
| EMUL\_BUS\_TYPE\_UART |  |
| EMUL\_BUS\_TYPE\_NONE |  |

## Function Documentation

## [◆ ](#gaad94c1e07998417cb9aa06d03be3b280)emul\_get\_binding()

| const struct [emul](structemul.md) \* emul\_get\_binding | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[emul.h](drivers_2emul_8h.md)>`

Retrieve the emul structure for an emulator by name.

Emulator objects are created via the [EMUL\_DT\_DEFINE()](#gad6292e3cd7f17a3600be396777f304c8) macro and placed in memory by the linker. If the emulator structure is needed for custom API calls, it can be retrieved by the name that the emulator exposes to the system (this is the devicetree node's label by default).

Parameters
:   | name | Emulator name to search for. A null pointer, or a pointer to an empty string, will cause NULL to be returned. |
    | --- | --- |

Returns
:   pointer to emulator structure; NULL if not found or cannot be used.

## [◆ ](#gad587b2852a182e1a7fdcb3b056d898f1)emul\_init\_for\_bus()

| int emul\_init\_for\_bus | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[emul.h](drivers_2emul_8h.md)>`

Set up a list of emulators.

Parameters
:   | dev | Device the emulators are attached to (e.g. an I2C controller) |
    | --- | --- |

Returns
:   0 if OK
:   negative value on error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
