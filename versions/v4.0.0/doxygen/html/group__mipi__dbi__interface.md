---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mipi__dbi__interface.html
original_path: doxygen/html/group__mipi__dbi__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| #define | [MIPI\_DBI\_SPI\_CONFIG\_DT](#ga9e05938ce1cd2b647cb00a77b773ad1d)(node\_id, operation\_, delay\_) |
|  | initialize a MIPI DBI SPI configuration struct from devicetree |
| #define | [MIPI\_DBI\_SPI\_CONFIG\_DT\_INST](#ga93d0c043dc9022bbe42c21a13bc46091)(inst, operation\_, delay\_) |
|  | Initialize a MIPI DBI SPI configuration from devicetree instance. |
| #define | [MIPI\_DBI\_CONFIG\_DT](#ga94aed5adf0dc393556b2c8c9976aeddf)(node\_id, operation\_, delay\_) |
|  | Initialize a MIPI DBI configuration from devicetree. |
| #define | [MIPI\_DBI\_CONFIG\_DT\_INST](#ga658456683f895d3b44ea44d9bf8b0558)(inst, operation\_, delay\_) |
|  | Initialize a MIPI DBI configuration from device instance. |
| #define | [MIPI\_DBI\_MODE\_SPI\_3WIRE](#ga9aeeeef78898e1d649f96feccae2fcac)   0x1 |
|  | SPI 3 wire (Type C1). |
| #define | [MIPI\_DBI\_MODE\_SPI\_4WIRE](#ga5c27ef3aa3256e60495a7c511cbaf7a5)   0x2 |
|  | SPI 4 wire (Type C3). |
| #define | [MIPI\_DBI\_MODE\_6800\_BUS\_16\_BIT](#ga4e59f3d57007cea38ae04aac74c2b5dc)   0x3 |
|  | Parallel Bus protocol for MIPI DBI Type A based on Motorola 6800 bus. |
| #define | [MIPI\_DBI\_MODE\_6800\_BUS\_9\_BIT](#gaa89b584bc5bf5a153926ba808de49131)   0x4 |
| #define | [MIPI\_DBI\_MODE\_6800\_BUS\_8\_BIT](#gab9b80bb367e7bd084ae490bbff9034b9)   0x5 |
| #define | [MIPI\_DBI\_MODE\_8080\_BUS\_16\_BIT](#ga3c3d1c379c4bc07847412b3bd5b76cb1)   0x6 |
|  | Parallel Bus protocol for MIPI DBI Type B based on Intel 8080 bus. |
| #define | [MIPI\_DBI\_MODE\_8080\_BUS\_9\_BIT](#gad4c61d48021f38c0759daf9a401f24c7)   0x7 |
| #define | [MIPI\_DBI\_MODE\_8080\_BUS\_8\_BIT](#ga3d26bb4556822d12567c62c7ff2c3bb9)   0x8 |

| Functions | |
| --- | --- |
| static int | [mipi\_dbi\_command\_write](#gad36e3d57fd931236c4ed4e58dfef1cca) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write a command to the display controller. |
| static int | [mipi\_dbi\_command\_read](#gafac64feca9fdee3803154bacb58e8e47) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*cmds, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_cmd, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read a command response from the display controller. |
| static int | [mipi\_dbi\_write\_display](#ga62aa7b9677da010a678580d956f7d0e3) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*framebuf, struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixfmt) |
|  | Write a display buffer to the display controller. |
| static int | [mipi\_dbi\_reset](#ga1c1a117ae5db5f7508f302d48dc72013) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_ms) |
|  | Resets attached display controller. |
| static int | [mipi\_dbi\_release](#gade0b635bcd4f16fb3ec5d122d1b09161) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config) |
|  | Releases a locked MIPI DBI device. |

## Detailed Description

MIPI-DBI driver APIs.

Since
:   3.6

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga94aed5adf0dc393556b2c8c9976aeddf)MIPI\_DBI\_CONFIG\_DT

| #define MIPI\_DBI\_CONFIG\_DT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h.md)>`

**Value:**

{ \

.mode = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, mipi\_mode), \

.config = [MIPI\_DBI\_SPI\_CONFIG\_DT](#ga9e05938ce1cd2b647cb00a77b773ad1d)(node\_id, operation\_, delay\_), \

}

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:745

[MIPI\_DBI\_SPI\_CONFIG\_DT](#ga9e05938ce1cd2b647cb00a77b773ad1d)

#define MIPI\_DBI\_SPI\_CONFIG\_DT(node\_id, operation\_, delay\_)

initialize a MIPI DBI SPI configuration struct from devicetree

**Definition** mipi\_dbi.h:54

Initialize a MIPI DBI configuration from devicetree.

This helper allows drivers to initialize a MIPI DBI configuration structure from devicetree. It sets the MIPI DBI mode, as well as configuration fields in the SPI configuration structure

Parameters
:   | node\_id | Devicetree node identifier for the MIPI DBI device to initialize |
    | --- | --- |
    | operation\_ | the desired operation field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.") |
    | delay\_ | the desired delay field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.")'s [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure."), if there is one |

## [◆ ](#ga658456683f895d3b44ea44d9bf8b0558)MIPI\_DBI\_CONFIG\_DT\_INST

| #define MIPI\_DBI\_CONFIG\_DT\_INST | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h.md)>`

**Value:**

[MIPI\_DBI\_CONFIG\_DT](#ga94aed5adf0dc393556b2c8c9976aeddf)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), operation\_, delay\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

[MIPI\_DBI\_CONFIG\_DT](#ga94aed5adf0dc393556b2c8c9976aeddf)

#define MIPI\_DBI\_CONFIG\_DT(node\_id, operation\_, delay\_)

Initialize a MIPI DBI configuration from devicetree.

**Definition** mipi\_dbi.h:97

Initialize a MIPI DBI configuration from device instance.

Equivalent to [MIPI\_DBI\_CONFIG\_DT(DT\_DRV\_INST(inst), operation\_, delay\_)](#ga94aed5adf0dc393556b2c8c9976aeddf)

Parameters
:   | inst | Instance of the device to initialize a MIPI DBI configuration for |
    | --- | --- |
    | operation\_ | the desired operation field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.") |
    | delay\_ | the desired delay field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.")'s [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure."), if there is one |

## [◆ ](#ga4e59f3d57007cea38ae04aac74c2b5dc)MIPI\_DBI\_MODE\_6800\_BUS\_16\_BIT

| #define MIPI\_DBI\_MODE\_6800\_BUS\_16\_BIT   0x3 |
| --- |

`#include <[mipi_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)>`

Parallel Bus protocol for MIPI DBI Type A based on Motorola 6800 bus.

```
         -.   .--------.      .------------------------
CS        '---'        '---'

         -------------------------------------------
RESX

              .--------------------------------
D/CX     ----------'

R/WX     -------------------------------------------

         -------------------------------------------
E

          .--------.   .--------------------------.
D[15:0]/ -| COMMAND|---|  DATA                    |
D[8:0]/   '--------'   '--------------------------'
D[7:0]
```

Please refer to the MIPI DBI specification for a detailed cycle diagram.

## [◆ ](#gab9b80bb367e7bd084ae490bbff9034b9)MIPI\_DBI\_MODE\_6800\_BUS\_8\_BIT

| #define MIPI\_DBI\_MODE\_6800\_BUS\_8\_BIT   0x5 |
| --- |

`#include <[mipi_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)>`

## [◆ ](#gaa89b584bc5bf5a153926ba808de49131)MIPI\_DBI\_MODE\_6800\_BUS\_9\_BIT

| #define MIPI\_DBI\_MODE\_6800\_BUS\_9\_BIT   0x4 |
| --- |

`#include <[mipi_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)>`

## [◆ ](#ga3c3d1c379c4bc07847412b3bd5b76cb1)MIPI\_DBI\_MODE\_8080\_BUS\_16\_BIT

| #define MIPI\_DBI\_MODE\_8080\_BUS\_16\_BIT   0x6 |
| --- |

`#include <[mipi_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)>`

Parallel Bus protocol for MIPI DBI Type B based on Intel 8080 bus.

```
         -.                                  .-
CS        '---------------------------------------'

         -------------------------------------------
RESX

         --.              .----------------------------
D/CX       '-----------'

         ---.   .--------.   .----------------------
WRX         '---'   '---'

         -------------------------------------------
RDX

            .--------.   .--------------------------.
D[15:0]/ ---| COMMAND|---|  DATA                    |
D[8:0]/     '--------'   '--------------------------'
D[7:0]
```

Please refer to the MIPI DBI specification for a detailed cycle diagram.

## [◆ ](#ga3d26bb4556822d12567c62c7ff2c3bb9)MIPI\_DBI\_MODE\_8080\_BUS\_8\_BIT

| #define MIPI\_DBI\_MODE\_8080\_BUS\_8\_BIT   0x8 |
| --- |

`#include <[mipi_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)>`

## [◆ ](#gad4c61d48021f38c0759daf9a401f24c7)MIPI\_DBI\_MODE\_8080\_BUS\_9\_BIT

| #define MIPI\_DBI\_MODE\_8080\_BUS\_9\_BIT   0x7 |
| --- |

`#include <[mipi_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)>`

## [◆ ](#ga9aeeeef78898e1d649f96feccae2fcac)MIPI\_DBI\_MODE\_SPI\_3WIRE

| #define MIPI\_DBI\_MODE\_SPI\_3WIRE   0x1 |
| --- |

`#include <[mipi_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)>`

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

`#include <[mipi_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)>`

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

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h.md)>`

**Value:**

{ \

.frequency = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, mipi\_max\_frequency), \

.operation = (operation\_) | \

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, duplex, 0) | \

COND\_CODE\_1([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, mipi\_cpol), [SPI\_MODE\_CPOL](group__spi__interface.md#ga5a2be1003873beaa0ade10e7218d67d5), (0)) | \

COND\_CODE\_1([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, mipi\_cpha), [SPI\_MODE\_CPHA](group__spi__interface.md#ga35e98b37e3ec4889a90100abe884590f), (0)) | \

COND\_CODE\_1([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, mipi\_hold\_cs), [SPI\_HOLD\_ON\_CS](group__spi__interface.md#gae917312adef283b4bf67cdb53566e4bb), (0)), \

.slave = [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id), \

.cs = { \

.gpio = [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)([DT\_PHANDLE](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)([DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)(node\_id), \

spi\_dev), cs\_gpios, \

[DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(node\_id), \

{}), \

.delay = (delay\_), \

}, \

}

[DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)

#define DT\_PARENT(node\_id)

Get a node identifier for a parent node.

**Definition** devicetree.h:357

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:907

[DT\_PHANDLE](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)

#define DT\_PHANDLE(node\_id, prop)

Get a node identifier for a phandle property's value.

**Definition** devicetree.h:1771

[DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)

#define DT\_REG\_ADDR\_RAW(node\_id)

Get a node's (only) register block raw address.

**Definition** devicetree.h:2400

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2433

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)

#define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value)

Like GPIO\_DT\_SPEC\_GET\_BY\_IDX(), with a fallback to a default value.

**Definition** gpio.h:355

[SPI\_MODE\_CPHA](group__spi__interface.md#ga35e98b37e3ec4889a90100abe884590f)

#define SPI\_MODE\_CPHA

Clock Phase: this dictates when is the data captured, and depends clock's polarity.

**Definition** spi.h:70

[SPI\_MODE\_CPOL](group__spi__interface.md#ga5a2be1003873beaa0ade10e7218d67d5)

#define SPI\_MODE\_CPOL

Clock Polarity: if set, clock idle state will be 1 and active state will be 0.

**Definition** spi.h:61

[SPI\_HOLD\_ON\_CS](group__spi__interface.md#gae917312adef283b4bf67cdb53566e4bb)

#define SPI\_HOLD\_ON\_CS

Requests - if possible - to keep CS asserted after the transaction.

**Definition** spi.h:116

initialize a MIPI DBI SPI configuration struct from devicetree

This helper allows drivers to initialize a MIPI DBI SPI configuration structure using devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the MIPI DBI device whose struct [spi\_config](structspi__config.md "SPI controller configuration structure.") to create an initializer for |
    | --- | --- |
    | operation\_ | the desired operation field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.") |
    | delay\_ | the desired delay field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.")'s [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure."), if there is one |

## [◆ ](#ga93d0c043dc9022bbe42c21a13bc46091)MIPI\_DBI\_SPI\_CONFIG\_DT\_INST

| #define MIPI\_DBI\_SPI\_CONFIG\_DT\_INST | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h.md)>`

**Value:**

[MIPI\_DBI\_SPI\_CONFIG\_DT](#ga9e05938ce1cd2b647cb00a77b773ad1d)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), operation\_, delay\_)

Initialize a MIPI DBI SPI configuration from devicetree instance.

This helper initializes a MIPI DBI SPI configuration from a devicetree instance. It is equivalent to [MIPI\_DBI\_SPI\_CONFIG\_DT(DT\_DRV\_INST(inst))](#ga9e05938ce1cd2b647cb00a77b773ad1d)

Parameters
:   | inst | Instance number to initialize configuration from |
    | --- | --- |
    | operation\_ | the desired operation field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.") |
    | delay\_ | the desired delay field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.")'s [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure."), if there is one |

## Function Documentation

## [◆ ](#gafac64feca9fdee3803154bacb58e8e47)mipi\_dbi\_command\_read()

| | int mipi\_dbi\_command\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \* | *config*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *cmds*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_cmd*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *response*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h.md)>`

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

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h.md)>`

Write a command to the display controller.

Writes a command, along with an optional data buffer to the display. If data buffer and buffer length are NULL and 0 respectively, then only a command will be sent. Note that if the SPI configuration passed to this function locks the SPI bus, it is the caller's responsibility to release it with [mipi\_dbi\_release()](#gade0b635bcd4f16fb3ec5d122d1b09161)

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

## [◆ ](#gade0b635bcd4f16fb3ec5d122d1b09161)mipi\_dbi\_release()

| | int mipi\_dbi\_release | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \* | *config* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h.md)>`

Releases a locked MIPI DBI device.

Releases a lock on a MIPI DBI device and/or the device's CS line if and only if the given config parameter was the last one to be used in any of the above functions, and if it has the SPI\_LOCK\_ON bit set and/or the SPI\_HOLD\_ON\_CS bit set into its operation bits field. This lock functions exactly like the SPI lock, and can be used if the caller needs to keep CS asserted for multiple transactions, or the MIPI DBI device locked.

Parameters
:   | dev | mipi dbi controller |
    | --- | --- |
    | config | MIPI DBI configuration |

Return values
:   | 0 | reset succeeded |
    | --- | --- |
    | -EIO | I/O error |
    | -ENOSYS | not implemented |
    | -ENOTSUP | not supported |

## [◆ ](#ga1c1a117ae5db5f7508f302d48dc72013)mipi\_dbi\_reset()

| | int mipi\_dbi\_reset | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *delay\_ms* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h.md)>`

Resets attached display controller.

Resets the attached display controller.

Parameters
:   | dev | mipi dbi controller |
    | --- | --- |
    | delay\_ms | duration to set reset signal for, in milliseconds |

Return values
:   | 0 | reset succeeded |
    | --- | --- |
    | -EIO | I/O error |
    | -ENOSYS | not implemented |
    | -ENOTSUP | not supported |

## [◆ ](#ga62aa7b9677da010a678580d956f7d0e3)mipi\_dbi\_write\_display()

| | int mipi\_dbi\_write\_display | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \* | *config*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *framebuf*, | |  |  | struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \* | *desc*, | |  |  | enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) | *pixfmt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h.md)>`

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
