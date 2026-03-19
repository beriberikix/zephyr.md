---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__spinlock__apis.html
original_path: doxygen/html/group__spinlock__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Spinlock APIs

[Kernel APIs](group__kernel__apis.md)

Spinlock APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [k\_spinlock](structk__spinlock.md) |
|  | Kernel Spin Lock. [More...](structk__spinlock.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_SPINLOCK\_BREAK](#ga7b16542003f7eca7f5bcae5ba494f823)   continue |
|  | Leaves a code block guarded with [K\_SPINLOCK](#ga6d0db300193464dc4e603110e891f856) after releasing the lock. |
| #define | [K\_SPINLOCK](#ga6d0db300193464dc4e603110e891f856)(lck) |
|  | Guards a code block with the given spinlock, automatically acquiring the lock before executing the code block. |

| Typedefs | |
| --- | --- |
| typedef struct z\_spinlock\_key | [k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) |
|  | Spinlock key type. |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) | [k\_spin\_lock](#gaac60da4347f5b29ff8c4e5f24c99b3bf) (struct [k\_spinlock](structk__spinlock.md) \*l) |
|  | Lock a spinlock. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [k\_spin\_trylock](#ga680d878eaa0e7a2f10c6e992791855ee) (struct [k\_spinlock](structk__spinlock.md) \*l, [k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) \*k) |
|  | Attempt to lock a spinlock. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [k\_spin\_unlock](#gaa54fc60d17d1033276aed4605671ed8e) (struct [k\_spinlock](structk__spinlock.md) \*l, [k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) key) |
|  | Unlock a spin lock. |

## Detailed Description

Spinlock APIs.

## Macro Definition Documentation

## [◆ ](#ga6d0db300193464dc4e603110e891f856)K\_SPINLOCK

| #define K\_SPINLOCK | ( |  | *lck* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spinlock.h](spinlock_8h.md)>`

**Value:**

for ([k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) \_\_i K\_SPINLOCK\_ONEXIT = {}, \_\_key = [k\_spin\_lock](#gaac60da4347f5b29ff8c4e5f24c99b3bf)(lck); !\_\_i.key; \

k\_spin\_unlock((lck), \_\_key), \_\_i.key = 1)

[k\_spin\_lock](#gaac60da4347f5b29ff8c4e5f24c99b3bf)

static ALWAYS\_INLINE k\_spinlock\_key\_t k\_spin\_lock(struct k\_spinlock \*l)

Lock a spinlock.

**Definition** spinlock.h:182

[k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0)

struct z\_spinlock\_key k\_spinlock\_key\_t

Spinlock key type.

**Definition** spinlock.h:130

Guards a code block with the given spinlock, automatically acquiring the lock before executing the code block.

The lock will be released either when reaching the end of the code block or when leaving the block with [K\_SPINLOCK\_BREAK](#ga7b16542003f7eca7f5bcae5ba494f823).

Example usage:

[K\_SPINLOCK](#ga6d0db300193464dc4e603110e891f856)(&mylock) {

...execute statements with the lock held...

if (some\_condition) {

...release the lock and leave the guarded section prematurely:

[K\_SPINLOCK\_BREAK](#ga7b16542003f7eca7f5bcae5ba494f823);

}

...execute statements with the lock held...

}

[K\_SPINLOCK](#ga6d0db300193464dc4e603110e891f856)

#define K\_SPINLOCK(lck)

Guards a code block with the given spinlock, automatically acquiring the lock before executing the co...

**Definition** spinlock.h:438

[K\_SPINLOCK\_BREAK](#ga7b16542003f7eca7f5bcae5ba494f823)

#define K\_SPINLOCK\_BREAK

Leaves a code block guarded with K\_SPINLOCK after releasing the lock.

**Definition** spinlock.h:395

Behind the scenes this pattern expands to a for-loop whose body is executed exactly once:

for ([k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) key = [k\_spin\_lock](#gaac60da4347f5b29ff8c4e5f24c99b3bf)(&mylock); ...; [k\_spin\_unlock](#gaa54fc60d17d1033276aed4605671ed8e)(&mylock, key)) {

...

}

[k\_spin\_unlock](#gaa54fc60d17d1033276aed4605671ed8e)

static ALWAYS\_INLINE void k\_spin\_unlock(struct k\_spinlock \*l, k\_spinlock\_key\_t key)

Unlock a spin lock.

**Definition** spinlock.h:300

Warning
:   The code block must execute to its end or be left by calling [K\_SPINLOCK\_BREAK](#ga7b16542003f7eca7f5bcae5ba494f823). Otherwise, e.g. if exiting the block with a break, goto or return statement, the spinlock will not be released on exit.

Note
:   In user mode the spinlock must be placed in memory accessible to the application, see [K\_APP\_DMEM](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6 "K_APP_DMEM") and [K\_APP\_BMEM](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881 "K_APP_BMEM") macros for details.

Parameters
:   | lck | Spinlock used to guard the enclosed code block. |
    | --- | --- |

## [◆ ](#ga7b16542003f7eca7f5bcae5ba494f823)K\_SPINLOCK\_BREAK

| #define K\_SPINLOCK\_BREAK   continue |
| --- |

`#include <[spinlock.h](spinlock_8h.md)>`

Leaves a code block guarded with [K\_SPINLOCK](#ga6d0db300193464dc4e603110e891f856) after releasing the lock.

See [K\_SPINLOCK](#ga6d0db300193464dc4e603110e891f856) for details.

## Typedef Documentation

## [◆ ](#gacacd3d3bbd31416dbbf6a0239be82ef0)k\_spinlock\_key\_t

| typedef struct z\_spinlock\_key [k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) |
| --- |

`#include <[spinlock.h](spinlock_8h.md)>`

Spinlock key type.

This type defines a "key" value used by a spinlock implementation to store the system interrupt state at the time of a call to [k\_spin\_lock()](#gaac60da4347f5b29ff8c4e5f24c99b3bf). It is expected to be passed to a matching [k\_spin\_unlock()](#gaa54fc60d17d1033276aed4605671ed8e).

This type is opaque and should not be inspected by application code.

## Function Documentation

## [◆ ](#gaac60da4347f5b29ff8c4e5f24c99b3bf)k\_spin\_lock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) k\_spin\_lock | ( | struct [k\_spinlock](structk__spinlock.md) \* | *l* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spinlock.h](spinlock_8h.md)>`

Lock a spinlock.

This routine locks the specified spinlock, returning a key handle representing interrupt state needed at unlock time. Upon returning, the calling thread is guaranteed not to be suspended or interrupted on its current CPU until it calls [k\_spin\_unlock()](#gaa54fc60d17d1033276aed4605671ed8e). The implementation guarantees mutual exclusion: exactly one thread on one CPU will return from [k\_spin\_lock()](#gaac60da4347f5b29ff8c4e5f24c99b3bf) at a time. Other CPUs trying to acquire a lock already held by another CPU will enter an implementation-defined busy loop ("spinning") until the lock is released.

Separate spin locks may be nested. It is legal to lock an (unlocked) spin lock while holding a different lock. Spin locks are not recursive, however: an attempt to acquire a spin lock that the CPU already holds will deadlock.

In circumstances where only one CPU exists, the behavior of [k\_spin\_lock()](#gaac60da4347f5b29ff8c4e5f24c99b3bf) remains as specified above, though obviously no spinning will take place. Implementations may be free to optimize in uniprocessor contexts such that the locking reduces to an interrupt mask operation.

Parameters
:   | l | A pointer to the spinlock to lock |
    | --- | --- |

Returns
:   A key value that must be passed to [k\_spin\_unlock()](#gaa54fc60d17d1033276aed4605671ed8e) when the lock is released.

## [◆ ](#ga680d878eaa0e7a2f10c6e992791855ee)k\_spin\_trylock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int k\_spin\_trylock | ( | struct [k\_spinlock](structk__spinlock.md) \* | *l*, | | --- | --- | --- | --- | |  |  | [k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) \* | *k* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spinlock.h](spinlock_8h.md)>`

Attempt to lock a spinlock.

This routine makes one attempt to lock `l`. If it is successful, then it will store the key into `k`.

Parameters
:   | [in] | l | A pointer to the spinlock to lock |
    | --- | --- | --- |
    | [out] | k | A pointer to the spinlock key |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EBUSY | if another thread holds the lock |

See also
:   [k\_spin\_lock](#gaac60da4347f5b29ff8c4e5f24c99b3bf)
:   [k\_spin\_unlock](#gaa54fc60d17d1033276aed4605671ed8e)

## [◆ ](#gaa54fc60d17d1033276aed4605671ed8e)k\_spin\_unlock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void k\_spin\_unlock | ( | struct [k\_spinlock](structk__spinlock.md) \* | *l*, | | --- | --- | --- | --- | |  |  | [k\_spinlock\_key\_t](#gacacd3d3bbd31416dbbf6a0239be82ef0) | *key* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spinlock.h](spinlock_8h.md)>`

Unlock a spin lock.

This releases a lock acquired by [k\_spin\_lock()](#gaac60da4347f5b29ff8c4e5f24c99b3bf). After this function is called, any CPU will be able to acquire the lock. If other CPUs are currently spinning inside [k\_spin\_lock()](#gaac60da4347f5b29ff8c4e5f24c99b3bf) waiting for this lock, exactly one of them will return synchronously with the lock held.

Spin locks must be properly nested. A call to [k\_spin\_unlock()](#gaa54fc60d17d1033276aed4605671ed8e) must be made on the lock object most recently locked using [k\_spin\_lock()](#gaac60da4347f5b29ff8c4e5f24c99b3bf), using the key value that it returned. Attempts to unlock mis-nested locks, or to unlock locks that are not held, or to passing a key parameter other than the one returned from [k\_spin\_lock()](#gaac60da4347f5b29ff8c4e5f24c99b3bf), are illegal. When CONFIG\_SPIN\_VALIDATE is set, some of these errors can be detected by the framework.

Parameters
:   | l | A pointer to the spinlock to release |
    | --- | --- |
    | key | The value returned from [k\_spin\_lock()](#gaac60da4347f5b29ff8c4e5f24c99b3bf) when this lock was acquired |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
