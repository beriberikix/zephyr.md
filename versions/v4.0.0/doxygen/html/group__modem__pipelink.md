---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__modem__pipelink.html
original_path: doxygen/html/group__modem__pipelink.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Modem pipelink

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md)

Modem pipelink.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [MODEM\_PIPELINK\_DT\_DECLARE](#ga46d06461a5a465f4a73c135f721e3aa5)(node\_id, name) |
|  | Declare pipelink from devicetree node identifier and name. |
| #define | [MODEM\_PIPELINK\_DT\_DEFINE](#gac1010375931a7a5076d066e2c5ed9a14)(node\_id, name) |
|  | Define pipelink from devicetree node identifier and name. |
| #define | [MODEM\_PIPELINK\_DT\_GET](#gada75e5995e78c8c8daa5a16f5e5abb4a)(node\_id, name) |
|  | Get pointer to pipelink from devicetree node identifier and name. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_pipelink\_callback](#ga4f93732f1df6cab41cc352526d6a849e)) (struct modem\_pipelink \*link, enum [modem\_pipelink\_event](#ga399168cacd287e376df68c4cf221ba00) event, void \*user\_data) |
|  | Pipelink callback definition. |

| Enumerations | |
| --- | --- |
| enum | [modem\_pipelink\_event](#ga399168cacd287e376df68c4cf221ba00) { [MODEM\_PIPELINK\_EVENT\_CONNECTED](#gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f) = 0 , [MODEM\_PIPELINK\_EVENT\_DISCONNECTED](#gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d) } |
|  | Pipelink event. [More...](#ga399168cacd287e376df68c4cf221ba00) |

| Functions | |
| --- | --- |
| void | [modem\_pipelink\_attach](#ga7ee7b3454a9fe94c20855a893dd2b2a1) (struct modem\_pipelink \*link, [modem\_pipelink\_callback](#ga4f93732f1df6cab41cc352526d6a849e) callback, void \*user\_data) |
|  | Attach callback to pipelink. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [modem\_pipelink\_is\_connected](#ga7c7638ad3f22533f374e002b787b11ce) (struct modem\_pipelink \*link) |
|  | Check whether pipelink pipe is connected. |
| struct modem\_pipe \* | [modem\_pipelink\_get\_pipe](#gab09d76f7bd93a19b82a7d5e818b80d80) (struct modem\_pipelink \*link) |
|  | Get pipe from pipelink. |
| void | [modem\_pipelink\_release](#ga684ff47ddb0e0487022cea62052b32e2) (struct modem\_pipelink \*link) |
|  | Clear callback. |

| MODEM\_PIPELINK\_DT\_INST macros | |
| --- | --- |
| Device driver instance variants of MODEM\_PIPELINK\_DT macros | |
| #define | [MODEM\_PIPELINK\_DT\_INST\_DECLARE](#gaedc5b4665d541fe4d471a287177e6674)(inst, name) |
| #define | [MODEM\_PIPELINK\_DT\_INST\_DEFINE](#ga1ca071affbb19bfac4c2ef7f25bf9c65)(inst, name) |
| #define | [MODEM\_PIPELINK\_DT\_INST\_GET](#ga1c3a0ff1f1939e12fdefee85a7f5eeed)(inst, name) |

## Detailed Description

Modem pipelink.

## Macro Definition Documentation

## [◆ ](#ga46d06461a5a465f4a73c135f721e3aa5)MODEM\_PIPELINK\_DT\_DECLARE

| #define MODEM\_PIPELINK\_DT\_DECLARE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pipelink.h](pipelink_8h.md)>`

**Value:**

extern struct modem\_pipelink MODEM\_PIPELINK\_DT\_SYM(node\_id, name)

Declare pipelink from devicetree node identifier and name.

Parameters
:   | node\_id | Devicetree node identifier |
    | --- | --- |
    | name | Pipelink name |

## [◆ ](#gac1010375931a7a5076d066e2c5ed9a14)MODEM\_PIPELINK\_DT\_DEFINE

| #define MODEM\_PIPELINK\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pipelink.h](pipelink_8h.md)>`

**Value:**

struct modem\_pipelink MODEM\_PIPELINK\_DT\_SYM(node\_id, name)

Define pipelink from devicetree node identifier and name.

Parameters
:   | node\_id | Devicetree node identifier |
    | --- | --- |
    | name | Pipelink name |

## [◆ ](#gada75e5995e78c8c8daa5a16f5e5abb4a)MODEM\_PIPELINK\_DT\_GET

| #define MODEM\_PIPELINK\_DT\_GET | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pipelink.h](pipelink_8h.md)>`

**Value:**

(&MODEM\_PIPELINK\_DT\_SYM(node\_id, name))

Get pointer to pipelink from devicetree node identifier and name.

Parameters
:   | node\_id | Devicetree node identifier |
    | --- | --- |
    | name | Pipelink name |

## [◆ ](#gaedc5b4665d541fe4d471a287177e6674)MODEM\_PIPELINK\_DT\_INST\_DECLARE

| #define MODEM\_PIPELINK\_DT\_INST\_DECLARE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pipelink.h](pipelink_8h.md)>`

**Value:**

[MODEM\_PIPELINK\_DT\_DECLARE](#ga46d06461a5a465f4a73c135f721e3aa5)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

[MODEM\_PIPELINK\_DT\_DECLARE](#ga46d06461a5a465f4a73c135f721e3aa5)

#define MODEM\_PIPELINK\_DT\_DECLARE(node\_id, name)

Declare pipelink from devicetree node identifier and name.

**Definition** pipelink.h:125

## [◆ ](#ga1ca071affbb19bfac4c2ef7f25bf9c65)MODEM\_PIPELINK\_DT\_INST\_DEFINE

| #define MODEM\_PIPELINK\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pipelink.h](pipelink_8h.md)>`

**Value:**

[MODEM\_PIPELINK\_DT\_DEFINE](#gac1010375931a7a5076d066e2c5ed9a14)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[MODEM\_PIPELINK\_DT\_DEFINE](#gac1010375931a7a5076d066e2c5ed9a14)

#define MODEM\_PIPELINK\_DT\_DEFINE(node\_id, name)

Define pipelink from devicetree node identifier and name.

**Definition** pipelink.h:133

## [◆ ](#ga1c3a0ff1f1939e12fdefee85a7f5eeed)MODEM\_PIPELINK\_DT\_INST\_GET

| #define MODEM\_PIPELINK\_DT\_INST\_GET | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pipelink.h](pipelink_8h.md)>`

**Value:**

[MODEM\_PIPELINK\_DT\_GET](#gada75e5995e78c8c8daa5a16f5e5abb4a)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[MODEM\_PIPELINK\_DT\_GET](#gada75e5995e78c8c8daa5a16f5e5abb4a)

#define MODEM\_PIPELINK\_DT\_GET(node\_id, name)

Get pointer to pipelink from devicetree node identifier and name.

**Definition** pipelink.h:141

## Typedef Documentation

## [◆ ](#ga4f93732f1df6cab41cc352526d6a849e)modem\_pipelink\_callback

| typedef void(\* modem\_pipelink\_callback) (struct modem\_pipelink \*link, enum [modem\_pipelink\_event](#ga399168cacd287e376df68c4cf221ba00) event, void \*user\_data) |
| --- |

`#include <[pipelink.h](pipelink_8h.md)>`

Pipelink callback definition.

Parameters
:   | link | Modem pipelink instance |
    | --- | --- |
    | event | Modem pipelink event |
    | user\_data | User data passed to [modem\_pipelink\_attach()](#ga7ee7b3454a9fe94c20855a893dd2b2a1) |

## Enumeration Type Documentation

## [◆ ](#ga399168cacd287e376df68c4cf221ba00)modem\_pipelink\_event

| enum [modem\_pipelink\_event](#ga399168cacd287e376df68c4cf221ba00) |
| --- |

`#include <[pipelink.h](pipelink_8h.md)>`

Pipelink event.

| Enumerator | |
| --- | --- |
| MODEM\_PIPELINK\_EVENT\_CONNECTED | Modem pipe has been connected and can be opened. |
| MODEM\_PIPELINK\_EVENT\_DISCONNECTED | Modem pipe has been disconnected and can't be opened. |

## Function Documentation

## [◆ ](#ga7ee7b3454a9fe94c20855a893dd2b2a1)modem\_pipelink\_attach()

| void modem\_pipelink\_attach | ( | struct modem\_pipelink \* | *link*, |
| --- | --- | --- | --- |
|  |  | [modem\_pipelink\_callback](#ga4f93732f1df6cab41cc352526d6a849e) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[pipelink.h](pipelink_8h.md)>`

Attach callback to pipelink.

Parameters
:   | link | Pipelink instance |
    | --- | --- |
    | callback | Pipelink callback |
    | user\_data | User data passed to pipelink callback |

## [◆ ](#gab09d76f7bd93a19b82a7d5e818b80d80)modem\_pipelink\_get\_pipe()

| struct modem\_pipe \* modem\_pipelink\_get\_pipe | ( | struct modem\_pipelink \* | *link* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pipelink.h](pipelink_8h.md)>`

Get pipe from pipelink.

Parameters
:   | link | Pipelink instance |
    | --- | --- |

Return values
:   | Pointer | to pipe if pipelink has been initialized |
    | --- | --- |
    | NULL | if pipelink has not been initialized |

## [◆ ](#ga7c7638ad3f22533f374e002b787b11ce)modem\_pipelink\_is\_connected()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) modem\_pipelink\_is\_connected | ( | struct modem\_pipelink \* | *link* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pipelink.h](pipelink_8h.md)>`

Check whether pipelink pipe is connected.

Parameters
:   | link | Pipelink instance |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if pipe is connected |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if pipe is not connected |

## [◆ ](#ga684ff47ddb0e0487022cea62052b32e2)modem\_pipelink\_release()

| void modem\_pipelink\_release | ( | struct modem\_pipelink \* | *link* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pipelink.h](pipelink_8h.md)>`

Clear callback.

Parameters
:   | link | Pipelink instance |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
