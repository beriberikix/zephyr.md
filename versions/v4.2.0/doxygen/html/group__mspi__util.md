---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__mspi__util.html
original_path: doxygen/html/group__mspi__util.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Mspi\_util

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md)

| Macros | |
| --- | --- |
| #define | [MSPI\_XIP\_CFG\_STRUCT\_DECLARE](#gaee7a74e9fbe2ec3d646ac3e1b422d9f6)(\_name) |
|  | Declare the optional XIP config in peripheral driver. |
| #define | [MSPI\_XIP\_BASE\_ADDR\_DECLARE](#ga073d056b234445b9b65a35df108c7c06)(\_name) |
|  | Declare the optional XIP base address in peripheral driver. |
| #define | [MSPI\_SCRAMBLE\_CFG\_STRUCT\_DECLARE](#ga8c55eacfe36f484bb5b3f82f8918aa79)(\_name) |
|  | Declare the optional scramble config in peripheral driver. |
| #define | [MSPI\_TIMING\_CFG\_STRUCT\_DECLARE](#ga118cb8d67bde11040aa8369ff88e4b6b)(\_name) |
|  | Declare the optional timing config in peripheral driver. |
| #define | [MSPI\_TIMING\_PARAM\_DECLARE](#ga4c88adce60d915c85972fa2cfaf7177e)(\_name) |
|  | Declare the optional timing parameter in peripheral driver. |
| #define | [MSPI\_OPTIONAL\_CFG\_STRUCT\_INIT](#ga7b2c02a81ae6d670680b86088624dc17)(code, \_name, \_object) |
|  | Initialize the optional config structure in peripheral driver. |
| #define | [MSPI\_XIP\_BASE\_ADDR\_INIT](#gae363a99025470afc6be5a501869b58d4)(\_name, \_bus) |
|  | Initialize the optional XIP base address in peripheral driver. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga7b2c02a81ae6d670680b86088624dc17)MSPI\_OPTIONAL\_CFG\_STRUCT\_INIT

| #define MSPI\_OPTIONAL\_CFG\_STRUCT\_INIT | ( |  | *code*, |
| --- | --- | --- | --- |
|  |  |  | *\_name*, |
|  |  |  | *\_object* ) |

`#include <[zephyr/drivers/mspi.h](mspi_8h.md)>`

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(code, (.\_name = \_object,))

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:247

Initialize the optional config structure in peripheral driver.

## [◆ ](#ga8c55eacfe36f484bb5b3f82f8918aa79)MSPI\_SCRAMBLE\_CFG\_STRUCT\_DECLARE

| #define MSPI\_SCRAMBLE\_CFG\_STRUCT\_DECLARE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/mspi.h](mspi_8h.md)>`

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_MSPI\_SCRAMBLE, (struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \_name;))

[mspi\_scramble\_cfg](structmspi__scramble__cfg.md)

MSPI controller scramble configuration.

**Definition** mspi.h:332

Declare the optional scramble config in peripheral driver.

## [◆ ](#ga118cb8d67bde11040aa8369ff88e4b6b)MSPI\_TIMING\_CFG\_STRUCT\_DECLARE

| #define MSPI\_TIMING\_CFG\_STRUCT\_DECLARE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/mspi.h](mspi_8h.md)>`

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_MSPI\_TIMING, ([mspi\_timing\_cfg](structmspi__timing__cfg.md) \_name;))

[mspi\_timing\_cfg](structmspi__timing__cfg.md)

Stub for struct timing\_cfg.

**Definition** mspi.h:216

Declare the optional timing config in peripheral driver.

## [◆ ](#ga4c88adce60d915c85972fa2cfaf7177e)MSPI\_TIMING\_PARAM\_DECLARE

| #define MSPI\_TIMING\_PARAM\_DECLARE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/mspi.h](mspi_8h.md)>`

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_MSPI\_TIMING, ([mspi\_timing\_param](group__mspi__configure__api.md#gaa25a7f97ab3437d4544832a0e7474f4a) \_name;))

[mspi\_timing\_param](group__mspi__configure__api.md#gaa25a7f97ab3437d4544832a0e7474f4a)

mspi\_timing\_param

Stub for timing parameter.

**Definition** mspi.h:209

Declare the optional timing parameter in peripheral driver.

## [◆ ](#ga073d056b234445b9b65a35df108c7c06)MSPI\_XIP\_BASE\_ADDR\_DECLARE

| #define MSPI\_XIP\_BASE\_ADDR\_DECLARE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/mspi.h](mspi_8h.md)>`

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_MSPI\_XIP, ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_name;))

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Declare the optional XIP base address in peripheral driver.

## [◆ ](#gae363a99025470afc6be5a501869b58d4)MSPI\_XIP\_BASE\_ADDR\_INIT

| #define MSPI\_XIP\_BASE\_ADDR\_INIT | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_bus* ) |

`#include <[zephyr/drivers/mspi.h](mspi_8h.md)>`

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_MSPI\_XIP, (.\_name = [DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)(\_bus, 1),))

[DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)

#define DT\_REG\_ADDR\_BY\_IDX(node\_id, idx)

Get the base address of the register block at index idx.

**Definition** devicetree.h:2437

Initialize the optional XIP base address in peripheral driver.

## [◆ ](#gaee7a74e9fbe2ec3d646ac3e1b422d9f6)MSPI\_XIP\_CFG\_STRUCT\_DECLARE

| #define MSPI\_XIP\_CFG\_STRUCT\_DECLARE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/mspi.h](mspi_8h.md)>`

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_MSPI\_XIP, (struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \_name;))

[mspi\_xip\_cfg](structmspi__xip__cfg.md)

MSPI controller XIP configuration.

**Definition** mspi.h:316

Declare the optional XIP config in peripheral driver.

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
