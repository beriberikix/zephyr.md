---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/spinlock_8h.html
original_path: doxygen/html/spinlock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spinlock.h File Reference

Public interface for spinlocks.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/arch/cpu.h](cpu_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/time_units.h](time__units_8h_source.md)>`

[Go to the source code of this file.](spinlock_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [k\_spinlock](structk__spinlock.md) |
|  | Kernel Spin Lock. [More...](structk__spinlock.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_SPINLOCK\_BREAK](group__spinlock__apis.md#ga7b16542003f7eca7f5bcae5ba494f823)   continue |
|  | Leaves a code block guarded with [K\_SPINLOCK](group__spinlock__apis.md#ga6d0db300193464dc4e603110e891f856 "K_SPINLOCK") after releasing the lock. |
| #define | [K\_SPINLOCK](group__spinlock__apis.md#ga6d0db300193464dc4e603110e891f856)(lck) |
|  | Guards a code block with the given spinlock, automatically acquiring the lock before executing the code block. |

| Typedefs | |
| --- | --- |
| typedef struct z\_spinlock\_key | [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) |
|  | Spinlock key type. |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) | [k\_spin\_lock](group__spinlock__apis.md#gaac60da4347f5b29ff8c4e5f24c99b3bf) (struct [k\_spinlock](structk__spinlock.md) \*l) |
|  | Lock a spinlock. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [k\_spin\_trylock](group__spinlock__apis.md#ga680d878eaa0e7a2f10c6e992791855ee) (struct [k\_spinlock](structk__spinlock.md) \*l, [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) \*k) |
|  | Attempt to lock a spinlock. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [k\_spin\_unlock](group__spinlock__apis.md#gaa54fc60d17d1033276aed4605671ed8e) (struct [k\_spinlock](structk__spinlock.md) \*l, [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) key) |
|  | Unlock a spin lock. |

## Detailed Description

Public interface for spinlocks.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [spinlock.h](spinlock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
