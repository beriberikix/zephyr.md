---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ztest__mock.html
original_path: doxygen/html/group__ztest__mock.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ztest mocking support

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md)

This module provides simple mocking functions for unit testing.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [ztest\_expect\_value](#ga58c2f0c0e628e73a2268a3d18b0440d6)(func, param, value) |
|  | Tell function *func* to expect the value *value* for *param*. |
| #define | [ztest\_check\_expected\_value](#gae9af6ba8e51738e938763c896f17ea8f)(param) |
|  | If *param* doesn't match the value set by [ztest\_expect\_value()](#ga58c2f0c0e628e73a2268a3d18b0440d6), fail the test. |
| #define | [ztest\_expect\_data](#gac1a64d8bf9c877e8666e0c6d93b0dbab)(func, param, data) |
|  | Tell function *func* to expect the data *data* for *param*. |
| #define | [ztest\_check\_expected\_data](#ga805cf99272f147beeeee5ad6ca2553f5)(param, length) |
|  | If data pointed by *param* don't match the data set by [ztest\_expect\_data()](#gac1a64d8bf9c877e8666e0c6d93b0dbab), fail the test. |
| #define | [ztest\_return\_data](#gac79d097a6b274b25286f2b0e80fbd6e9)(func, param, data) |
|  | Tell function *func* to return the data *data* for *param*. |
| #define | [ztest\_copy\_return\_data](#ga12872a3d783d53d564ed94583bc490b0)(param, length) |
|  | Copy the data set by ztest\_return\_data to the memory pointed by *param*. |
| #define | [ztest\_returns\_value](#ga2ec539b4c0f3e4efb695213b4fd08c2c)(func, value) |
|  | Tell *func* that it should return *value*. |
| #define | [ztest\_get\_return\_value](#ga31dcd5b5a3596a7404a771a2d32f3a39)() |
|  | Get the return value for current function. |
| #define | [ztest\_get\_return\_value\_ptr](#gaa2df2eaeba49019b7a83ac769ea95968)() |
|  | Get the return value as a pointer for current function. |

## Detailed Description

This module provides simple mocking functions for unit testing.

These need CONFIG\_ZTEST\_MOCKING=y.

## Macro Definition Documentation

## [◆ ](#ga805cf99272f147beeeee5ad6ca2553f5)ztest\_check\_expected\_data

| #define ztest\_check\_expected\_data | ( |  | *param*, |
| --- | --- | --- | --- |
|  |  |  | *length* ) |

`#include <[ztest_mock.h](ztest__mock_8h.md)>`

**Value:**

z\_ztest\_check\_expected\_data(\_\_func\_\_, [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(param), \

(void \*)(param), (length))

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

If data pointed by *param* don't match the data set by [ztest\_expect\_data()](#gac1a64d8bf9c877e8666e0c6d93b0dbab), fail the test.

This will first check that *param* is expected to be null or non-null and then check whether the data pointed by parameter is equal to expected data. If either of these checks fail, the current test will fail. This must be called from the called function.

Parameters
:   | param | Parameter to check |
    | --- | --- |
    | length | Length of the data to compare |

## [◆ ](#gae9af6ba8e51738e938763c896f17ea8f)ztest\_check\_expected\_value

| #define ztest\_check\_expected\_value | ( |  | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_mock.h](ztest__mock_8h.md)>`

**Value:**

z\_ztest\_check\_expected\_value(\_\_func\_\_, [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(param), \

([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))(param))

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

If *param* doesn't match the value set by [ztest\_expect\_value()](#ga58c2f0c0e628e73a2268a3d18b0440d6), fail the test.

This will first check that does *param* have a value to be expected, and then checks whether the value of the parameter is equal to the expected value. If either of these checks fail, the current test will fail. This must be called from the called function.

Parameters
:   | param | Parameter to check |
    | --- | --- |

## [◆ ](#ga12872a3d783d53d564ed94583bc490b0)ztest\_copy\_return\_data

| #define ztest\_copy\_return\_data | ( |  | *param*, |
| --- | --- | --- | --- |
|  |  |  | *length* ) |

`#include <[ztest_mock.h](ztest__mock_8h.md)>`

**Value:**

z\_ztest\_copy\_return\_data(\_\_func\_\_, [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(param), \

(void \*)(param), (length))

Copy the data set by ztest\_return\_data to the memory pointed by *param*.

This will first check that *param* is not null and then copy the data. This must be called from the called function.

Parameters
:   | param | Parameter to return data for |
    | --- | --- |
    | length | Length of the data to return |

## [◆ ](#gac1a64d8bf9c877e8666e0c6d93b0dbab)ztest\_expect\_data

| #define ztest\_expect\_data | ( |  | *func*, |
| --- | --- | --- | --- |
|  |  |  | *param*, |
|  |  |  | *data* ) |

`#include <[ztest_mock.h](ztest__mock_8h.md)>`

**Value:**

z\_ztest\_expect\_data([STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(func), [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(param), (void \*)(data))

Tell function *func* to expect the data *data* for *param*.

When using [ztest\_check\_expected\_data()](#ga805cf99272f147beeeee5ad6ca2553f5), the data pointed to by *param* should be same *data* in this function. Only data pointer is stored by this function, so it must still be valid when ztest\_check\_expected\_data is called.

Parameters
:   | func | Function in question |
    | --- | --- |
    | param | Parameter for which the data should be set |
    | data | pointer for the data for parameter *param* |

## [◆ ](#ga58c2f0c0e628e73a2268a3d18b0440d6)ztest\_expect\_value

| #define ztest\_expect\_value | ( |  | *func*, |
| --- | --- | --- | --- |
|  |  |  | *param*, |
|  |  |  | *value* ) |

`#include <[ztest_mock.h](ztest__mock_8h.md)>`

**Value:**

z\_ztest\_expect\_value([STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(func), [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(param), \

([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))(value))

Tell function *func* to expect the value *value* for *param*.

When using [ztest\_check\_expected\_value()](#gae9af6ba8e51738e938763c896f17ea8f), tell that the value of *param* should be *value*. The value will internally be stored as an [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808).

Parameters
:   | func | Function in question |
    | --- | --- |
    | param | Parameter for which the value should be set |
    | value | Value for *param* |

## [◆ ](#ga31dcd5b5a3596a7404a771a2d32f3a39)ztest\_get\_return\_value

| #define ztest\_get\_return\_value | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[ztest_mock.h](ztest__mock_8h.md)>`

**Value:**

z\_ztest\_get\_return\_value(\_\_func\_\_)

Get the return value for current function.

The return value must have been set previously with [ztest\_returns\_value()](#ga2ec539b4c0f3e4efb695213b4fd08c2c). If no return value exists, the current test will fail.

Returns
:   The value the current function should return

## [◆ ](#gaa2df2eaeba49019b7a83ac769ea95968)ztest\_get\_return\_value\_ptr

| #define ztest\_get\_return\_value\_ptr | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[ztest_mock.h](ztest__mock_8h.md)>`

**Value:**

((void \*)z\_ztest\_get\_return\_value(\_\_func\_\_))

Get the return value as a pointer for current function.

The return value must have been set previously with [ztest\_returns\_value()](#ga2ec539b4c0f3e4efb695213b4fd08c2c). If no return value exists, the current test will fail.

Returns
:   The value the current function should return as a void \*

## [◆ ](#gac79d097a6b274b25286f2b0e80fbd6e9)ztest\_return\_data

| #define ztest\_return\_data | ( |  | *func*, |
| --- | --- | --- | --- |
|  |  |  | *param*, |
|  |  |  | *data* ) |

`#include <[ztest_mock.h](ztest__mock_8h.md)>`

**Value:**

z\_ztest\_return\_data([STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(func), [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(param), (void \*)(data))

Tell function *func* to return the data *data* for *param*.

When using [ztest\_return\_data()](#gac79d097a6b274b25286f2b0e80fbd6e9), the data pointed to by *param* should be same *data* in this function. Only data pointer is stored by this function, so it must still be valid when ztest\_copy\_return\_data is called.

Parameters
:   | func | Function in question |
    | --- | --- |
    | param | Parameter for which the data should be set |
    | data | pointer for the data for parameter *param* |

## [◆ ](#ga2ec539b4c0f3e4efb695213b4fd08c2c)ztest\_returns\_value

| #define ztest\_returns\_value | ( |  | *func*, |
| --- | --- | --- | --- |
|  |  |  | *value* ) |

`#include <[ztest_mock.h](ztest__mock_8h.md)>`

**Value:**

z\_ztest\_returns\_value([STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(func), ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))(value))

Tell *func* that it should return *value*.

Parameters
:   | func | Function that should return *value* |
    | --- | --- |
    | value | Value to return from *func* |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
