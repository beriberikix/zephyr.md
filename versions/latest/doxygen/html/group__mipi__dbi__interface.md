---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mipi__dbi__interface.html
original_path: doxygen/html/group__mipi__dbi__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MIPI-DBI driver APIs

[Device Driver APIs](group__io__interfaces.md)

MIPI-DBI driver APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mipi\_dbi\_config](structmipi__dbi__config.md) |
|  | MIPI DBI controller configuration. [More...](structmipi__dbi__config.md#details) |
| struct | [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) |
|  | MIPI-DBI host driver API. [More...](structmipi__dbi__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [MIPI\_DBI\_MODE\_SPI\_3WIRE](#ga9aeeeef78898e1d649f96feccae2fcac)   0x1 |
|  | SPI 3 wire (Type C1). |
| #define | [MIPI\_DBI\_MODE\_SPI\_4WIRE](#ga5c27ef3aa3256e60495a7c511cbaf7a5)   0x2 |
|  | SPI 4 wire (Type C3). |
| #define | [MIPI\_DBI\_SPI\_CONFIG\_DT](#ga9e05938ce1cd2b647cb00a77b773ad1d)(node\_id, operation\_, delay\_) |
|  | initialize a MIPI DBI SPI configuration struct from devicetree |

| Functions | |
| --- | --- |
| static int | [mipi\_dbi\_command\_write](#gad36e3d57fd931236c4ed4e58dfef1cca) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write a command to the display controller. |
| static int | [mipi\_dbi\_command\_read](#gafac64feca9fdee3803154bacb58e8e47) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*cmds, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_cmd, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read a command response from the display controller. |
| static int | [mipi\_dbi\_write\_display](#ga62aa7b9677da010a678580d956f7d0e3) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*framebuf, struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixfmt) |
|  | Write a display buffer to the display controller. |
| static int | [mipi\_dbi\_reset](#ga2d04bcd271ba2fd6338f8ac9e787e114) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay) |
|  | Resets attached display controller. |

## Detailed Description

MIPI-DBI driver APIs.

## Macro Definition Documentation

## [◆ ](#ga9aeeeef78898e1d649f96feccae2fcac)MIPI\_DBI\_MODE\_SPI\_3WIRE

| #define MIPI\_DBI\_MODE\_SPI\_3WIRE   0x1 |
| --- |

`#include <[mipi_dbi.h](mipi__dbi_8h.md)>`

SPI 3 wire (Type C1).

Uses 9 write clocks to send a byte of data. The bit sent on the 9th clock indicates whether the byte is a command or data byte

```
      .---.   .---.   .---.   .---.   .---.   .---.   .---.   .---.
SCK  -'   '---'   '---'   '---'   '---'   '---'   '---'   '---'   '---

     -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.
DOUT  |D/C| D7| D6| D5| D4| D3| D2| D1| D0|D/C| D7| D6| D5| D4|...|
     -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'
      | Word 1                            | Word n

     -.                                                              .--
CS    '-----------------------------------------------------------'
```

## [◆ ](#ga5c27ef3aa3256e60495a7c511cbaf7a5)MIPI\_DBI\_MODE\_SPI\_4WIRE

| #define MIPI\_DBI\_MODE\_SPI\_4WIRE   0x2 |
| --- |

`#include <[mipi_dbi.h](mipi__dbi_8h.md)>`

SPI 4 wire (Type C3).

Uses 8 write clocks to send a byte of data. an additional C/D pin will be use to indicate whether the byte is a command or data byte

```
      .---.   .---.   .---.   .---.   .---.   .---.   .---.   .---.
SCK  -'   '---'   '---'   '---'   '---'   '---'   '---'   '---'   '---

     -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.
DOUT  | D7| D6| D5| D4| D3| D2| D1| D0| D7| D6| D5| D4| D3| D2| D1| D0|
     -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'
      | Word 1                        | Word n

     -.                                                                  .--
CS    '---------------------------------------------------------------'

     -.-------------------------------.-------------------------------.-
CD    |             D/C               |             D/C               |
     -'-------------------------------'-------------------------------'-
```

## [◆ ](#ga9e05938ce1cd2b647cb00a77b773ad1d)MIPI\_DBI\_SPI\_CONFIG\_DT

| #define MIPI\_DBI\_SPI\_CONFIG\_DT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[mipi_dbi.h](mipi__dbi_8h.md)>`

**Value:**

{ \

.frequency = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, mipi\_max\_frequency), \

.operation = (operation\_) | \

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, duplex), \

COND\_CODE\_1([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, mipi\_cpol), [SPI\_MODE\_CPOL](group__spi__interface.md#ga5a2be1003873beaa0ade10e7218d67d5), (0)) | \

COND\_CODE\_1([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, mipi\_cpha), [SPI\_MODE\_CPHA](group__spi__interface.md#ga35e98b37e3ec4889a90100abe884590f), (0)) | \

COND\_CODE\_1([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, mipi\_hold\_cs), [SPI\_HOLD\_ON\_CS](group__spi__interface.md#gae917312adef283b4bf67cdb53566e4bb), (0)), \

.slave = [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id), \

.cs = { \

.gpio = [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)([DT\_PHANDLE](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)([DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)(node\_id), \

spi\_dev), cs\_gpios, \

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id), \

{}), \

.delay = (delay\_), \

}, \

}

[DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)

#define DT\_PARENT(node\_id)

Get a node identifier for a parent node.

**Definition** devicetree.h:359

[DT\_PHANDLE](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)

#define DT\_PHANDLE(node\_id, prop)

Get a node identifier for a phandle property's value.

**Definition** devicetree.h:1594

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:615

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2214

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)

#define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value)

Like GPIO\_DT\_SPEC\_GET\_BY\_IDX(), with a fallback to a default value.

**Definition** gpio.h:353

[SPI\_MODE\_CPHA](group__spi__interface.md#ga35e98b37e3ec4889a90100abe884590f)

#define SPI\_MODE\_CPHA

Clock Phase: this dictates when is the data captured, and depends clock's polarity.

**Definition** spi.h:68

[SPI\_MODE\_CPOL](group__spi__interface.md#ga5a2be1003873beaa0ade10e7218d67d5)

#define SPI\_MODE\_CPOL

Clock Polarity: if set, clock idle state will be 1 and active state will be 0.

**Definition** spi.h:59

[SPI\_HOLD\_ON\_CS](group__spi__interface.md#gae917312adef283b4bf67cdb53566e4bb)

#define SPI\_HOLD\_ON\_CS

Requests - if possible - to keep CS asserted after the transaction.

**Definition** spi.h:114

initialize a MIPI DBI SPI configuration struct from devicetree

This helper allows drivers to initialize a MIPI DBI SPI configuration structure using devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the MIPI DBI device whose struct [spi\_config](structspi__config.md "SPI controller configuration structure.") to create an initializer for |
    | --- | --- |
    | operation\_ | the desired operation field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.") |
    | delay\_ | the desired delay field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.")'s [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure."), if there is one |

## Function Documentation

## [◆ ](#gafac64feca9fdee3803154bacb58e8e47)mipi\_dbi\_command\_read()

| | int mipi\_dbi\_command\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \* | *config*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *cmds*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_cmd*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *response*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dbi.h](mipi__dbi_8h.md)>`

Read a command response from the display controller.

Reads a command response from the display controller.

Parameters
:   | dev | mipi dbi controller |
    | --- | --- |
    | config | MIPI DBI configuration |
    | cmds | array of one byte commands to send to display controller |
    | num\_cmd | number of commands to write to display controller |
    | response | response buffer, filled with display controller response |
    | len | size of response buffer in bytes. |

Return values
:   | 0 | command read succeeded |
    | --- | --- |
    | -EIO | I/O error |
    | -ETIMEDOUT | transfer timed out |
    | -EBUSY | controller is busy |
    | -ENOSYS | not implemented |

## [◆ ](#gad36e3d57fd931236c4ed4e58dfef1cca)mipi\_dbi\_command\_write()

| | int mipi\_dbi\_command\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \* | *config*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dbi.h](mipi__dbi_8h.md)>`

Write a command to the display controller.

Writes a command, along with an optional data buffer to the display. If data buffer and buffer length are NULL and 0 respectively, then only a command will be sent.

Parameters
:   | dev | mipi dbi controller |
    | --- | --- |
    | config | MIPI DBI configuration |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | command to write to display controller |
    | data | optional data buffer to write after command |
    | len | size of data buffer in bytes. Set to 0 to skip sending data. |

Return values
:   | 0 | command write succeeded |
    | --- | --- |
    | -EIO | I/O error |
    | -ETIMEDOUT | transfer timed out |
    | -EBUSY | controller is busy |
    | -ENOSYS | not implemented |

## [◆ ](#ga2d04bcd271ba2fd6338f8ac9e787e114)mipi\_dbi\_reset()

| | int mipi\_dbi\_reset | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *delay* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dbi.h](mipi__dbi_8h.md)>`

Resets attached display controller.

Resets the attached display controller.

Parameters
:   | dev | mipi dbi controller |
    | --- | --- |
    | delay | duration to set reset signal for, in milliseconds |

Return values
:   | 0 | reset succeeded |
    | --- | --- |
    | -EIO | I/O error |
    | -ENOSYS | not implemented |
    | -ENOTSUP | not supported |

## [◆ ](#ga62aa7b9677da010a678580d956f7d0e3)mipi\_dbi\_write\_display()

| | int mipi\_dbi\_write\_display | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \* | *config*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *framebuf*, | |  |  | struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \* | *desc*, | |  |  | enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) | *pixfmt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dbi.h](mipi__dbi_8h.md)>`

Write a display buffer to the display controller.

Writes a display buffer to the controller. If the controller requires a "Write memory" command before writing display data, this should be sent with [mipi\_dbi\_command\_write](#gad36e3d57fd931236c4ed4e58dfef1cca)

Parameters
:   | dev | mipi dbi controller |
    | --- | --- |
    | config | MIPI DBI configuration |
    | framebuf | framebuffer to write to display |
    | desc | descriptor of framebuffer to write. Note that the pitch must be equal to width. "buf\_size" field determines how many bytes will be written. |
    | pixfmt | pixel format of framebuffer data |

Return values
:   | 0 | buffer write succeeded. |
    | --- | --- |
    | -EIO | I/O error |
    | -ETIMEDOUT | transfer timed out |
    | -EBUSY | controller is busy |
    | -ENOSYS | not implemented |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
