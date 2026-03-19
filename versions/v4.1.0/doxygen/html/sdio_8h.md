---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sdio_8h.html
original_path: doxygen/html/sdio_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdio.h File Reference

Public API for SDIO subsystem.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/sdhc.h](sdhc_8h_source.md)>`  
`#include <[zephyr/sd/sd.h](sd_8h_source.md)>`

[Go to the source code of this file.](sdio_8h_source.md)

| Functions | |
| --- | --- |
| int | [sdio\_init\_func](#aae010680d9035116f503d7ddc1cf8590) (struct [sd\_card](structsd__card.md) \*card, struct [sdio\_func](structsdio__func.md) \*func, enum [sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6) num) |
|  | Initialize SDIO function. |
| int | [sdio\_enable\_func](#aa3e60d2c643cd054af56cb44d193074b) (struct [sdio\_func](structsdio__func.md) \*func) |
|  | Enable SDIO function. |
| int | [sdio\_set\_block\_size](#a417829a0558b236465b70ff637a7ca38) (struct [sdio\_func](structsdio__func.md) \*func, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bsize) |
|  | Set block size of SDIO function. |
| int | [sdio\_read\_byte](#a2ac93072041651597b9027156706f0d0) (struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
|  | Read byte from SDIO register. |
| int | [sdio\_write\_byte](#a9bfb4970e28830151d2a293475b98435) (struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) write\_val) |
|  | Write byte to SDIO register. |
| int | [sdio\_rw\_byte](#a8fbc927607a156abc4c47bc551f72b11) (struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) write\_val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*read\_val) |
|  | Write byte to SDIO register, and read result. |
| int | [sdio\_read\_fifo](#a8cf3af67ef909dd93cdfec29250d76c6) (struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len) |
|  | Read bytes from SDIO fifo. |
| int | [sdio\_write\_fifo](#a5beb64599a265b117a42858e8087ae4a) (struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len) |
|  | Write bytes to SDIO fifo. |
| int | [sdio\_read\_blocks\_fifo](#ab7ec658d92672acfa36d073191d0369f) (struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) blocks) |
|  | Read blocks from SDIO fifo. |
| int | [sdio\_write\_blocks\_fifo](#a68f75f10ea65cef4bc650b6e2ec4001d) (struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) blocks) |
|  | Write blocks to SDIO fifo. |
| int | [sdio\_read\_addr](#a341c846c55adf512a4c3397f38d4bbf9) (struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len) |
|  | Copy bytes from an SDIO card. |
| int | [sdio\_write\_addr](#a55bd42c4d41643444890227ee6cbbfc5) (struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len) |
|  | Copy bytes to an SDIO card. |

## Detailed Description

Public API for SDIO subsystem.

## Function Documentation

## [◆ ](#aa3e60d2c643cd054af56cb44d193074b)sdio\_enable\_func()

| int sdio\_enable\_func | ( | struct [sdio\_func](structsdio__func.md) \* | *func* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable SDIO function.

Enables SDIO card function. [sdio\_init\_func](#aae010680d9035116f503d7ddc1cf8590) must be called to initialized the function structure before enabling it in the card.

Parameters
:   | func | function to enable |
    | --- | --- |

Return values
:   | 0 | function was enabled successfully |
    | --- | --- |
    | -ETIMEDOUT | card I/O timed out |
    | -EIO | I/O error |

## [◆ ](#aae010680d9035116f503d7ddc1cf8590)sdio\_init\_func()

| int sdio\_init\_func | ( | struct [sd\_card](structsd__card.md) \* | *card*, |
| --- | --- | --- | --- |
|  |  | struct [sdio\_func](structsdio__func.md) \* | *func*, |
|  |  | enum [sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6) | *num* ) |

Initialize SDIO function.

Initializes SDIO card function. The card function will not be enabled, but after this call returns the SDIO function structure can be used to read and write data from the card.

Parameters
:   | func | function structure to initialize |
    | --- | --- |
    | card | SD card to enable function on |
    | num | function number to initialize |

Return values
:   | 0 | function was initialized successfully |
    | --- | --- |
    | -EIO | I/O error |

## [◆ ](#a341c846c55adf512a4c3397f38d4bbf9)sdio\_read\_addr()

| int sdio\_read\_addr | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *len* ) |

Copy bytes from an SDIO card.

Copies bytes from an SDIO card, starting from provided address.

Parameters
:   | func | function to read from |
    | --- | --- |
    | reg | register address to start copy at |
    | data | buffer to copy data into |
    | len | length of data to read |

Return values
:   | 0 | read succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card read timed out |
    | -EIO | I/O error |

## [◆ ](#ab7ec658d92672acfa36d073191d0369f)sdio\_read\_blocks\_fifo()

| int sdio\_read\_blocks\_fifo | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *blocks* ) |

Read blocks from SDIO fifo.

Reads blocks from SDIO register, treating it as a fifo. Reads will all be done from same address.

Parameters
:   | func | function to read from |
    | --- | --- |
    | reg | register address of fifo |
    | data | filled with data read from fifo |
    | blocks | number of blocks to read from fifo |

Return values
:   | 0 | read succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card read timed out |
    | -EIO | I/O error |

## [◆ ](#a2ac93072041651597b9027156706f0d0)sdio\_read\_byte()

| int sdio\_read\_byte | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *val* ) |

Read byte from SDIO register.

Reads byte from SDIO register

Parameters
:   | func | function to read from |
    | --- | --- |
    | reg | register address to read from |
    | val | filled with byte value read from register |

Return values
:   | 0 | read succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card read timed out |
    | -EIO | I/O error |

## [◆ ](#a8cf3af67ef909dd93cdfec29250d76c6)sdio\_read\_fifo()

| int sdio\_read\_fifo | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *len* ) |

Read bytes from SDIO fifo.

Reads bytes from SDIO register, treating it as a fifo. Reads will all be done from same address.

Parameters
:   | func | function to read from |
    | --- | --- |
    | reg | register address of fifo |
    | data | filled with data read from fifo |
    | len | length of data to read from card |

Return values
:   | 0 | read succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card read timed out |
    | -EIO | I/O error |

## [◆ ](#a8fbc927607a156abc4c47bc551f72b11)sdio\_rw\_byte()

| int sdio\_rw\_byte | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *write\_val*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *read\_val* ) |

Write byte to SDIO register, and read result.

Writes byte to SDIO register, and reads the register after write

Parameters
:   | func | function to write to |
    | --- | --- |
    | reg | register address to write to |
    | write\_val | value to write to register |
    | read\_val | filled with value read from register |

Return values
:   | 0 | write succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card write timed out |
    | -EIO | I/O error |

## [◆ ](#a417829a0558b236465b70ff637a7ca38)sdio\_set\_block\_size()

| int sdio\_set\_block\_size | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *bsize* ) |

Set block size of SDIO function.

Set desired block size for SDIO function, used by block transfers to SDIO registers.

Parameters
:   | func | function to set block size for |
    | --- | --- |
    | bsize | block size |

Return values
:   | 0 | block size was set |
    | --- | --- |
    | -EINVAL | unsupported/invalid block size |
    | -EIO | I/O error |

## [◆ ](#a55bd42c4d41643444890227ee6cbbfc5)sdio\_write\_addr()

| int sdio\_write\_addr | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *len* ) |

Copy bytes to an SDIO card.

Copies bytes to an SDIO card, starting from provided address.

Parameters
:   | func | function to write to |
    | --- | --- |
    | reg | register address to start copy at |
    | data | buffer to copy data from |
    | len | length of data to write |

Return values
:   | 0 | write succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card write timed out |
    | -EIO | I/O error |

## [◆ ](#a68f75f10ea65cef4bc650b6e2ec4001d)sdio\_write\_blocks\_fifo()

| int sdio\_write\_blocks\_fifo | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *blocks* ) |

Write blocks to SDIO fifo.

Writes blocks from SDIO register, treating it as a fifo. Writes will all be done to same address.

Parameters
:   | func | function to write to |
    | --- | --- |
    | reg | register address of fifo |
    | data | data to write to fifo |
    | blocks | number of blocks to write to fifo |

Return values
:   | 0 | write succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card write timed out |
    | -EIO | I/O error |

## [◆ ](#a9bfb4970e28830151d2a293475b98435)sdio\_write\_byte()

| int sdio\_write\_byte | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *write\_val* ) |

Write byte to SDIO register.

Writes byte to SDIO register

Parameters
:   | func | function to write to |
    | --- | --- |
    | reg | register address to write to |
    | write\_val | value to write to register |

Return values
:   | 0 | write succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card write timed out |
    | -EIO | I/O error |

## [◆ ](#a5beb64599a265b117a42858e8087ae4a)sdio\_write\_fifo()

| int sdio\_write\_fifo | ( | struct [sdio\_func](structsdio__func.md) \* | *func*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *len* ) |

Write bytes to SDIO fifo.

Writes bytes to SDIO register, treating it as a fifo. Writes will all be done to same address.

Parameters
:   | func | function to write to |
    | --- | --- |
    | reg | register address of fifo |
    | data | data to write to fifo |
    | len | length of data to write to card |

Return values
:   | 0 | write succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card write timed out |
    | -EIO | I/O error |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sd](dir_ff091b3f4b9505cc58dad89321d1c232.md)
- [sdio.h](sdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
