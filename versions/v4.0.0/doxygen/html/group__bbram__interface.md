---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bbram__interface.html
original_path: doxygen/html/group__bbram__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BBRAM Interface

[Device Driver APIs](group__io__interfaces.md)

BBRAM Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bbram\_driver\_api](structbbram__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [bbram\_api\_check\_invalid\_t](#gac23658302662587043f3587080f798fe)) (const struct [device](structdevice.md) \*dev) |
|  | API template to check if the BBRAM is invalid. |
| typedef int(\* | [bbram\_api\_check\_standby\_power\_t](#ga99adefcb89ab80d8b5e24b8ffad8f43e)) (const struct [device](structdevice.md) \*dev) |
|  | API template to check for standby power failure. |
| typedef int(\* | [bbram\_api\_check\_power\_t](#gaa6edc8a61529edad90de2e6fff619fdf)) (const struct [device](structdevice.md) \*dev) |
|  | API template to check for V CC1 power failure. |
| typedef int(\* | [bbram\_api\_get\_size\_t](#gacfa586f705c520a6a05638a2e289fe50)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | API template to check the size of the BBRAM. |
| typedef int(\* | [bbram\_api\_read\_t](#ga8b06a1b3bb9b524597804dd268904881)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | API template to read from BBRAM. |
| typedef int(\* | [bbram\_api\_write\_t](#ga1b111ae421791b9544777c1bab5e2a02)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | API template to write to BBRAM. |

| Functions | |
| --- | --- |
| int | [bbram\_check\_invalid](#ga7164969f308616696a9ab71a4d19b70b) (const struct [device](structdevice.md) \*dev) |
|  | Check if BBRAM is invalid. |
| int | [bbram\_check\_standby\_power](#ga948ed0a7d3824f950ad46b99ba3d86f4) (const struct [device](structdevice.md) \*dev) |
|  | Check for standby (Volt SBY) power failure. |
| int | [bbram\_check\_power](#ga8fc2a647bda90e96f866514300180a96) (const struct [device](structdevice.md) \*dev) |
|  | Check for V CC1 power failure. |
| int | [bbram\_get\_size](#gab6bdb4a1cba88ca645c256366a696bdd) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Get the size of the BBRAM (in bytes). |
| int | [bbram\_read](#ga9ef786b0fbac3f8523be2bb87b7cff7b) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Read bytes from BBRAM. |
| int | [bbram\_write](#ga51007eed4820aed341d20e4562607564) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Write bytes to BBRAM. |
| int | [bbram\_emul\_set\_invalid](#gae2b89f8a44e38fe7df2219397bad139b) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_invalid) |
|  | Set the emulated BBRAM driver's invalid state. |
| int | [bbram\_emul\_set\_standby\_power\_state](#ga08a2c565ba0ec6ac5894a718a652eec2) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) failure) |
|  | Set the emulated BBRAM driver's standby power state. |
| int | [bbram\_emul\_set\_power\_state](#gadc0243187b853832b08af36c9baf9cb0) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) failure) |
|  | Set the emulated BBRAM driver's power state. |

## Detailed Description

BBRAM Interface.

## Typedef Documentation

## [◆ ](#gac23658302662587043f3587080f798fe)bbram\_api\_check\_invalid\_t

| typedef int(\* bbram\_api\_check\_invalid\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[bbram.h](bbram_8h.md)>`

API template to check if the BBRAM is invalid.

See also
:   [bbram\_check\_invalid](#ga7164969f308616696a9ab71a4d19b70b)

## [◆ ](#gaa6edc8a61529edad90de2e6fff619fdf)bbram\_api\_check\_power\_t

| typedef int(\* bbram\_api\_check\_power\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[bbram.h](bbram_8h.md)>`

API template to check for V CC1 power failure.

See also
:   [bbram\_check\_power](#ga8fc2a647bda90e96f866514300180a96)

## [◆ ](#ga99adefcb89ab80d8b5e24b8ffad8f43e)bbram\_api\_check\_standby\_power\_t

| typedef int(\* bbram\_api\_check\_standby\_power\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[bbram.h](bbram_8h.md)>`

API template to check for standby power failure.

See also
:   [bbram\_check\_standby\_power](#ga948ed0a7d3824f950ad46b99ba3d86f4)

## [◆ ](#gacfa586f705c520a6a05638a2e289fe50)bbram\_api\_get\_size\_t

| typedef int(\* bbram\_api\_get\_size\_t) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
| --- |

`#include <[bbram.h](bbram_8h.md)>`

API template to check the size of the BBRAM.

See also
:   [bbram\_get\_size](#gab6bdb4a1cba88ca645c256366a696bdd)

## [◆ ](#ga8b06a1b3bb9b524597804dd268904881)bbram\_api\_read\_t

| typedef int(\* bbram\_api\_read\_t) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| --- |

`#include <[bbram.h](bbram_8h.md)>`

API template to read from BBRAM.

See also
:   [bbram\_read](#ga9ef786b0fbac3f8523be2bb87b7cff7b)

## [◆ ](#ga1b111ae421791b9544777c1bab5e2a02)bbram\_api\_write\_t

| typedef int(\* bbram\_api\_write\_t) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| --- |

`#include <[bbram.h](bbram_8h.md)>`

API template to write to BBRAM.

See also
:   [bbram\_write](#ga51007eed4820aed341d20e4562607564)

## Function Documentation

## [◆ ](#ga7164969f308616696a9ab71a4d19b70b)bbram\_check\_invalid()

| int bbram\_check\_invalid | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bbram.h](bbram_8h.md)>`

Check if BBRAM is invalid.

Check if "Invalid Battery-Backed RAM" status is set then reset the status bit. This may occur as a result to low voltage at the VBAT pin.

Parameters
:   | [in] | dev | BBRAM device pointer. |
    | --- | --- | --- |

Returns
:   0 if the Battery-Backed RAM data is valid, -EFAULT otherwise.

## [◆ ](#ga8fc2a647bda90e96f866514300180a96)bbram\_check\_power()

| int bbram\_check\_power | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bbram.h](bbram_8h.md)>`

Check for V CC1 power failure.

This will return an error if the V CC1 power domain is turned on after it was off and reset the status bit.

Parameters
:   | [in] | dev | BBRAM device pointer. |
    | --- | --- | --- |

Returns
:   0 if the V CC1 power domain is in normal operation, -EFAULT otherwise.

## [◆ ](#ga948ed0a7d3824f950ad46b99ba3d86f4)bbram\_check\_standby\_power()

| int bbram\_check\_standby\_power | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bbram.h](bbram_8h.md)>`

Check for standby (Volt SBY) power failure.

Check if the V standby power domain is turned on after it was off then reset the status bit.

Parameters
:   | [in] | dev | BBRAM device pointer. |
    | --- | --- | --- |

Returns
:   0 if V SBY power domain is in normal operation.

## [◆ ](#gae2b89f8a44e38fe7df2219397bad139b)bbram\_emul\_set\_invalid()

| int bbram\_emul\_set\_invalid | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_invalid* ) |

`#include <[bbram.h](bbram_8h.md)>`

Set the emulated BBRAM driver's invalid state.

Calling this will affect the emulated behavior of [bbram\_check\_invalid()](#ga7164969f308616696a9ab71a4d19b70b).

Parameters
:   | [in] | dev | The emulated device to modify |
    | --- | --- | --- |
    | [in] | is\_invalid | The new invalid state |

Returns
:   0 on success, negative values on error.

## [◆ ](#gadc0243187b853832b08af36c9baf9cb0)bbram\_emul\_set\_power\_state()

| int bbram\_emul\_set\_power\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *failure* ) |

`#include <[bbram.h](bbram_8h.md)>`

Set the emulated BBRAM driver's power state.

Calling this will affect the emulated behavior of [bbram\_check\_power()](#ga8fc2a647bda90e96f866514300180a96).

Parameters
:   | [in] | dev | The emulated device to modify |
    | --- | --- | --- |
    | [in] | failure | Whether or not a power failure should be emulated |

Returns
:   0 on success, negative values on error.

## [◆ ](#ga08a2c565ba0ec6ac5894a718a652eec2)bbram\_emul\_set\_standby\_power\_state()

| int bbram\_emul\_set\_standby\_power\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *failure* ) |

`#include <[bbram.h](bbram_8h.md)>`

Set the emulated BBRAM driver's standby power state.

Calling this will affect the emulated behavior of [bbram\_check\_standby\_power()](#ga948ed0a7d3824f950ad46b99ba3d86f4).

Parameters
:   | [in] | dev | The emulated device to modify |
    | --- | --- | --- |
    | [in] | failure | Whether or not standby power failure should be emulated |

Returns
:   0 on success, negative values on error.

## [◆ ](#gab6bdb4a1cba88ca645c256366a696bdd)bbram\_get\_size()

| int bbram\_get\_size | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *size* ) |

`#include <[bbram.h](bbram_8h.md)>`

Get the size of the BBRAM (in bytes).

Parameters
:   | [in] | dev | BBRAM device pointer. |
    | --- | --- | --- |
    | [out] | size | Pointer to write the size to. |

Returns
:   0 for success, -EFAULT otherwise.

## [◆ ](#ga9ef786b0fbac3f8523be2bb87b7cff7b)bbram\_read()

| int bbram\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data* ) |

`#include <[bbram.h](bbram_8h.md)>`

Read bytes from BBRAM.

Parameters
:   | [in] | dev | The BBRAM device pointer to read from. |
    | --- | --- | --- |
    | [in] | offset | The offset into the RAM address to start reading from. |
    | [in] | size | The number of bytes to read. |
    | [out] | data | The buffer to load the data into. |

Returns
:   0 on success, -EFAULT if the address range is out of bounds.

## [◆ ](#ga51007eed4820aed341d20e4562607564)bbram\_write()

| int bbram\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data* ) |

`#include <[bbram.h](bbram_8h.md)>`

Write bytes to BBRAM.

Parameters
:   | [in] | dev | The BBRAM device pointer to write to. |
    | --- | --- | --- |
    | [in] | offset | The offset into the RAM address to start writing to. |
    | [in] | size | The number of bytes to write. |
    | [out] | data | Pointer to the start of data to write. |

Returns
:   0 on success, -EFAULT if the address range is out of bounds.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
