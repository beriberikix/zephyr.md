---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hwspinlock_8h.html
original_path: doxygen/html/hwspinlock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hwspinlock.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/hwspinlock.h>`

[Go to the source code of this file.](hwspinlock_8h_source.md)

| Functions | |
| --- | --- |
| int | [hwspinlock\_trylock](group__hwspinlock__interface.md#ga7b7efadefb9e0810c462ee38c669ef99) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Try to lock HW spinlock. |
| void | [hwspinlock\_lock](group__hwspinlock__interface.md#ga5b4edd18441bb51012801e15447e860a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Lock HW spinlock. |
| void | [hwspinlock\_unlock](group__hwspinlock__interface.md#ga997a5bd42875e09c671960be9535bcc9) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Try to unlock HW spinlock. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hwspinlock\_get\_max\_id](group__hwspinlock__interface.md#gaac02b3349210f467641161dffd6dc363) (const struct [device](structdevice.md) \*dev) |
|  | Get HW spinlock max ID. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [hwspinlock.h](hwspinlock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
