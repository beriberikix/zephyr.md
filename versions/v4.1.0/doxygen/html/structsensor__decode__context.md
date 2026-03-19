---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensor__decode__context.html
original_path: doxygen/html/structsensor__decode__context.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_decode\_context Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Sensor Interface](group__sensor__interface.md)

Used for iterating over the data frames via the [sensor\_decoder\_api](structsensor__decoder__api.md "Decodes a single raw data buffer.").
[More...](#details)

`#include <[sensor.h](sensor_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \* | [decoder](#a1ac0773e83a086455371d108264ef4f6) |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buffer](#a23e27eb0687d722be78e1b89278613d1) |
| struct [sensor\_chan\_spec](structsensor__chan__spec.md) | [channel](#a1c051bd8d0030f81cc561e32b2897d74) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fit](#ada9e40625829093087886c41f2fb7350) |

## Detailed Description

Used for iterating over the data frames via the [sensor\_decoder\_api](structsensor__decoder__api.md "Decodes a single raw data buffer.").

Example usage:

(.c)

struct [sensor\_decode\_context](structsensor__decode__context.md) ctx = [SENSOR\_DECODE\_CONTEXT\_INIT](group__sensor__interface.md#gae69ec503df53d2d5ee417e481f9ac9ea)(

[decoder](#a1ac0773e83a086455371d108264ef4f6), [buffer](#a23e27eb0687d722be78e1b89278613d1), [SENSOR\_CHAN\_ACCEL\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9), 0);

while (true) {

struct [sensor\_three\_axis\_data](structsensor__three__axis__data.md) accel\_out\_data;

num\_decoded\_channels = [sensor\_decode](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)(ctx, &accel\_out\_data, 1);

if (num\_decoded\_channels <= 0) {

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Done decoding buffer\n");

break;

}

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Decoded (%" [PRId32](inttypes_8h.md#a6d94d1417e1b35c53aee6306590de72b) ", %" [PRId32](inttypes_8h.md#a6d94d1417e1b35c53aee6306590de72b) ", %" [PRId32](inttypes_8h.md#a6d94d1417e1b35c53aee6306590de72b) ")\n", accel\_out\_data.readings[0].x,

accel\_out\_data.readings[0].y, accel\_out\_data.readings[0].z);

}

[sensor\_decode](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)

static int sensor\_decode(struct sensor\_decode\_context \*ctx, void \*out, uint16\_t max\_count)

Decode N frames using a sensor\_decode\_context.

**Definition** sensor.h:591

[SENSOR\_DECODE\_CONTEXT\_INIT](group__sensor__interface.md#gae69ec503df53d2d5ee417e481f9ac9ea)

#define SENSOR\_DECODE\_CONTEXT\_INIT(decoder\_, buffer\_, channel\_type\_, channel\_index\_)

Initialize a sensor\_decode\_context.

**Definition** sensor.h:575

[SENSOR\_CHAN\_ACCEL\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)

@ SENSOR\_CHAN\_ACCEL\_XYZ

Acceleration on the X, Y and Z axes.

**Definition** sensor.h:69

[PRId32](inttypes_8h.md#a6d94d1417e1b35c53aee6306590de72b)

#define PRId32

**Definition** inttypes.h:15

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)

static void printk(const char \*fmt,...)

Print kernel debugging message.

**Definition** printk.h:51

[sensor\_decode\_context](structsensor__decode__context.md)

Used for iterating over the data frames via the sensor\_decoder\_api.

**Definition** sensor.h:565

[sensor\_decode\_context::decoder](#a1ac0773e83a086455371d108264ef4f6)

const struct sensor\_decoder\_api \* decoder

**Definition** sensor.h:566

[sensor\_decode\_context::buffer](#a23e27eb0687d722be78e1b89278613d1)

const uint8\_t \* buffer

**Definition** sensor.h:567

[sensor\_three\_axis\_data](structsensor__three__axis__data.md)

Data for a sensor channel which reports on three axes.

**Definition** sensor\_data\_types.h:52

## Field Documentation

## [◆ ](#a23e27eb0687d722be78e1b89278613d1)buffer

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* sensor\_decode\_context::buffer |
| --- |

## [◆ ](#a1c051bd8d0030f81cc561e32b2897d74)channel

| struct [sensor\_chan\_spec](structsensor__chan__spec.md) sensor\_decode\_context::channel |
| --- |

## [◆ ](#a1ac0773e83a086455371d108264ef4f6)decoder

| const struct [sensor\_decoder\_api](structsensor__decoder__api.md)\* sensor\_decode\_context::decoder |
| --- |

## [◆ ](#ada9e40625829093087886c41f2fb7350)fit

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensor\_decode\_context::fit |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor.h](sensor_8h_source.md)

- [sensor\_decode\_context](structsensor__decode__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
