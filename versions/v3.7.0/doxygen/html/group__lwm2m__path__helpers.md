---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__lwm2m__path__helpers.html
original_path: doxygen/html/group__lwm2m__path__helpers.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LwM2M path helper macros

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [LwM2M high-level API](group__lwm2m__api.md)

| Macros | |
| --- | --- |
| #define | [LWM2M\_PATH](#ga0ac92ffa4a22bcd407a19e768a5720bd)(...) |
|  | Generate LwM2M string paths using numeric components. |
| #define | [LWM2M\_OBJ](#gac3c46145eae19f8c8608429e5b4e9250)(...) |
|  | Initialize LwM2M object structure. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gac3c46145eae19f8c8608429e5b4e9250)LWM2M\_OBJ

| #define LWM2M\_OBJ | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m_path.h](lwm2m__path_8h.md)>`

**Value:**

GET\_OBJ\_MACRO(\_\_VA\_ARGS\_\_, LWM2M\_OBJ4, LWM2M\_OBJ3, LWM2M\_OBJ2, LWM2M\_OBJ1)(\_\_VA\_ARGS\_\_)

Initialize LwM2M object structure.

Accepts at least one and up to four arguments. Fill up [lwm2m\_obj\_path](structlwm2m__obj__path.md "lwm2m_obj_path") structure and sets the level.

For example:

struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) p = [LWM2M\_OBJ](#gac3c46145eae19f8c8608429e5b4e9250)(MY\_OBJ, 0, RESOURCE);

[LWM2M\_OBJ](#gac3c46145eae19f8c8608429e5b4e9250)

#define LWM2M\_OBJ(...)

Initialize LwM2M object structure.

**Definition** lwm2m\_path.h:81

[lwm2m\_obj\_path](structlwm2m__obj__path.md)

LwM2M object path structure.

**Definition** lwm2m.h:96

Can also be used in place of function argument to return the structure allocated from stack

lwm2m\_notify\_observer\_path(&[LWM2M\_OBJ](#gac3c46145eae19f8c8608429e5b4e9250)(MY\_OBJ, inst\_id, RESOURCE));

## [◆ ](#ga0ac92ffa4a22bcd407a19e768a5720bd)LWM2M\_PATH

| #define LWM2M\_PATH | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m_path.h](lwm2m__path_8h.md)>`

**Value:**

LWM2M\_PATH\_MACRO(\_\_VA\_ARGS\_\_, LWM2M\_PATH4, LWM2M\_PATH3, \

LWM2M\_PATH2, LWM2M\_PATH1)(\_\_VA\_ARGS\_\_)

Generate LwM2M string paths using numeric components.

Accepts at least one and up to four arguments. Each argument will be stringified by the pre-processor, so calling this with non-literals will likely not do what you want.

For example:

#define MY\_OBJ\_ID 3

[LWM2M\_PATH](#ga0ac92ffa4a22bcd407a19e768a5720bd)(MY\_OBJ\_ID, 0, 1)

[LWM2M\_PATH](#ga0ac92ffa4a22bcd407a19e768a5720bd)

#define LWM2M\_PATH(...)

Generate LwM2M string paths using numeric components.

**Definition** lwm2m\_path.h:43

would evaluate to "3/0/1", while

int x = 3;

[LWM2M\_PATH](#ga0ac92ffa4a22bcd407a19e768a5720bd)(x, 0, 1)

evaluates to "x/0/1".

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
