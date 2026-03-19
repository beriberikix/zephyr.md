---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__hwspinlock__interface.html
original_path: doxygen/html/group__hwspinlock__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HW spinlock Interface

[Device Driver APIs](group__io__interfaces.md)

HW spinlock Interface.
[More...](#details)

| Functions | |
| --- | --- |
| int | [hwspinlock\_trylock](#ga7b7efadefb9e0810c462ee38c669ef99) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Try to lock HW spinlock. |
| void | [hwspinlock\_lock](#ga5b4edd18441bb51012801e15447e860a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Lock HW spinlock. |
| void | [hwspinlock\_unlock](#ga997a5bd42875e09c671960be9535bcc9) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Try to unlock HW spinlock. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hwspinlock\_get\_max\_id](#gaac02b3349210f467641161dffd6dc363) (const struct [device](structdevice.md) \*dev) |
|  | Get HW spinlock max ID. |

## Detailed Description

HW spinlock Interface.

## Function Documentation

## [◆ ](#gaac02b3349210f467641161dffd6dc363)hwspinlock\_get\_max\_id()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) hwspinlock\_get\_max\_id | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hwspinlock.h](hwspinlock_8h.md)>`

Get HW spinlock max ID.

This function is used to get the HW spinlock maximum ID. It should be called before attempting to lock/unlock a specific HW spinlock.

Parameters
:   | dev | HW spinlock device instance. |
    | --- | --- |

Return values
:   | HW | spinlock max ID. |
    | --- | --- |
    | 0 | if the function is not implemented by the driver. |

## [◆ ](#ga5b4edd18441bb51012801e15447e860a)hwspinlock\_lock()

| void hwspinlock\_lock | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* ) |

`#include <[hwspinlock.h](hwspinlock_8h.md)>`

Lock HW spinlock.

This function is used to lock specific HW spinlock. It should be called before a critical section that we want to protect.

Parameters
:   | dev | HW spinlock device instance. |
    | --- | --- |
    | id | Spinlock identifier. |

## [◆ ](#ga7b7efadefb9e0810c462ee38c669ef99)hwspinlock\_trylock()

| int hwspinlock\_trylock | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* ) |

`#include <[hwspinlock.h](hwspinlock_8h.md)>`

Try to lock HW spinlock.

This function is used for try to lock specific HW spinlock. It should be called before a critical section that we want to protect.

Parameters
:   | dev | HW spinlock device instance. |
    | --- | --- |
    | id | Spinlock identifier. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | In case of any failure. |

## [◆ ](#ga997a5bd42875e09c671960be9535bcc9)hwspinlock\_unlock()

| void hwspinlock\_unlock | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* ) |

`#include <[hwspinlock.h](hwspinlock_8h.md)>`

Try to unlock HW spinlock.

This function is used for try to unlock specific HW spinlock. It should be called after a critical section that we want to protect.

Parameters
:   | dev | HW spinlock device instance. |
    | --- | --- |
    | id | Spinlock identifier. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
