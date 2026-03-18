---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__gpio__emul.html
original_path: doxygen/html/group__gpio__emul.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Emulated GPIO

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

Emulated GPIO backend API.
[More...](#details)

| Functions | |
| --- | --- |
| int | [gpio\_emul\_input\_set\_masked](#gaa7eae6a0f85d0f0fb6a8aa41329f4709) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) values) |
|  | Modify the values of one or more emulated GPIO input `pins`. |
| static int | [gpio\_emul\_input\_set](#ga3962e337bc22e532f2c181724621fcf8) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, int value) |
|  | Modify the value of one emulated GPIO input `pin`. |
| int | [gpio\_emul\_output\_get\_masked](#gaa6e4c5c2c53d421e9635c0a977172205) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*values) |
|  | Read the value of one or more emulated GPIO output `pins`. |
| static int | [gpio\_emul\_output\_get](#gaa62613aa6eb442d2c4e436893316124f) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Read the value of one emulated GPIO output `pin`. |
| int | [gpio\_emul\_flags\_get](#ga86bd5ff4f557e4d520a4f760fb74cdd5) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get `flags` for a given emulated GPIO `pin`. |

## Detailed Description

Emulated GPIO backend API.

Behaviour of emulated GPIO is application-defined. As-such, each application may

- define a Device Tree overlay file to indicate the number of GPIO controllers as well as the number of pins for each controller
- register a callback with the GPIO controller using [gpio\_add\_callback](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca "gpio_add_callback") to emulate "wiring"
- asynchronously call [gpio\_emul\_input\_set](#ga3962e337bc22e532f2c181724621fcf8) and / or [gpio\_emul\_input\_set\_masked](#gaa7eae6a0f85d0f0fb6a8aa41329f4709) in order to emulate GPIO events

An example of an appropriate Device Tree overlay file is in tests/drivers/gpio/gpio\_basic\_api/boards/native\_sim.overlay.

An example of registering a callback to emulate "wiring" as well as an example of calling [gpio\_emul\_input\_set](#ga3962e337bc22e532f2c181724621fcf8) is in the file tests/drivers/gpio/gpio\_basic\_api/src/main.c .

## Function Documentation

## [◆ ](#ga86bd5ff4f557e4d520a4f760fb74cdd5)gpio\_emul\_flags\_get()

| int gpio\_emul\_flags\_get | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) | *pin*, |
|  |  | [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \* | *flags* ) |

`#include <[gpio_emul.h](gpio__emul_8h.md)>`

Get `flags` for a given emulated GPIO `pin`.

For more information on available flags, see [GPIO Driver APIs](group__gpio__interface.md "GPIO Driver APIs").

Parameters
:   | port | The emulated GPIO port |
    | --- | --- |
    | pin | The pin to retrieve `flags` for |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | a pointer to where the flags for `pin` will be stored |

Returns
:   0 on success
:   -EINVAL if an invalid argument is provided

## [◆ ](#ga3962e337bc22e532f2c181724621fcf8)gpio\_emul\_input\_set()

| | int gpio\_emul\_input\_set | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) | *pin*, | |  |  | int | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio_emul.h](gpio__emul_8h.md)>`

Modify the value of one emulated GPIO input `pin`.

Parameters
:   | port | The emulated GPIO port |
    | --- | --- |
    | pin | The pin to modify |
    | value | New values to assign to `pin` |

Returns
:   0 on success
:   -EINVAL if an invalid argument is provided

## [◆ ](#gaa7eae6a0f85d0f0fb6a8aa41329f4709)gpio\_emul\_input\_set\_masked()

| int gpio\_emul\_input\_set\_masked | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins*, |
|  |  | [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) | *values* ) |

`#include <[gpio_emul.h](gpio__emul_8h.md)>`

Modify the values of one or more emulated GPIO input `pins`.

Parameters
:   | port | The emulated GPIO port |
    | --- | --- |
    | pins | The mask of pins that have changed |
    | values | New values to assign to `pins` |

Returns
:   0 on success
:   -EINVAL if an invalid argument is provided

## [◆ ](#gaa62613aa6eb442d2c4e436893316124f)gpio\_emul\_output\_get()

| | int gpio\_emul\_output\_get | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) | *pin* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio_emul.h](gpio__emul_8h.md)>`

Read the value of one emulated GPIO output `pin`.

Parameters
:   | port | The emulated GPIO port |
    | --- | --- |
    | pin | The pin to read |

Returns
:   0 or 1 on success
:   -EINVAL if an invalid argument is provided

## [◆ ](#gaa6e4c5c2c53d421e9635c0a977172205)gpio\_emul\_output\_get\_masked()

| int gpio\_emul\_output\_get\_masked | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins*, |
|  |  | [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \* | *values* ) |

`#include <[gpio_emul.h](gpio__emul_8h.md)>`

Read the value of one or more emulated GPIO output `pins`.

Parameters
:   | port | The emulated GPIO port |
    | --- | --- |
    | pins | The mask of pins that have changed |
    | values | A pointer to where the value of `pins` will be stored |

Returns
:   0 on success
:   -EINVAL if an invalid argument is provided

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
