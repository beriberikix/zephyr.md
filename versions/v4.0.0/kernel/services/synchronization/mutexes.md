---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/services/synchronization/mutexes.html
original_path: kernel/services/synchronization/mutexes.html
---

# Mutexes

A *mutex* is a kernel object that implements a traditional
reentrant mutex. A mutex allows multiple threads to safely share
an associated hardware or software resource by ensuring mutually exclusive
access to the resource.

## [Concepts](#id1)

Any number of mutexes can be defined (limited only by available RAM). Each mutex
is referenced by its memory address.

A mutex has the following key properties:

- A **lock count** that indicates the number of times the mutex has been locked
  by the thread that has locked it. A count of zero indicates that the mutex
  is unlocked.
- An **owning thread** that identifies the thread that has locked the mutex,
  when it is locked.

A mutex must be initialized before it can be used. This sets its lock count
to zero.

A thread that needs to use a shared resource must first gain exclusive rights
to access it by **locking** the associated mutex. If the mutex is already locked
by another thread, the requesting thread may choose to wait for the mutex
to be unlocked.

After locking a mutex, the thread may safely use the associated resource
for as long as needed; however, it is considered good practice to hold the lock
for as short a time as possible to avoid negatively impacting other threads
that want to use the resource. When the thread no longer needs the resource
it must **unlock** the mutex to allow other threads to use the resource.

Any number of threads may wait on a locked mutex simultaneously.
When the mutex becomes unlocked it is then locked by the highest-priority
thread that has waited the longest.

Note

Mutex objects are *not* designed for use by ISRs.

### [Reentrant Locking](#id2)

A thread is permitted to lock a mutex it has already locked.
This allows the thread to access the associated resource at a point
in its execution when the mutex may or may not already be locked.

A mutex that is repeatedly locked by a thread must be unlocked an equal number
of times before the mutex becomes fully unlocked so it can be claimed
by another thread.

### [Priority Inheritance](#id3)

The thread that has locked a mutex is eligible for *priority inheritance*.
This means the kernel will *temporarily* elevate the thread’s priority
if a higher priority thread begins waiting on the mutex. This allows the owning
thread to complete its work and release the mutex more rapidly by executing
at the same priority as the waiting thread. Once the mutex has been unlocked,
the unlocking thread resets its priority to the level it had before locking
that mutex.

Note

The [`CONFIG_PRIORITY_CEILING`](../../../kconfig.md#CONFIG_PRIORITY_CEILING "CONFIG_PRIORITY_CEILING") configuration option limits
how high the kernel can raise a thread’s priority due to priority
inheritance. The default value of 0 permits unlimited elevation.

The owning thread’s base priority is saved in the mutex when it obtains the
lock. Each time a higher priority thread waits on a mutex, the kernel adjusts
the owning thread’s priority. When the owning thread releases the lock (or if
the high priority waiting thread times out), the kernel restores the thread’s
base priority from the value saved in the mutex.

This works well for priority inheritance as long as only one locked mutex is
involved. However, if multiple mutexes are involved, sub-optimal behavior will
be observed if the mutexes are not unlocked in the reverse order to which the
owning thread’s priority was previously raised. Consequently it is recommended
that a thread lock only a single mutex at a time when multiple mutexes are
shared between threads of different priorities.

## [Implementation](#id4)

### [Defining a Mutex](#id5)

A mutex is defined using a variable of type [`k_mutex`](../../../doxygen/html/structk__mutex.md).
It must then be initialized by calling [`k_mutex_init()`](../../../doxygen/html/group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480).

The following code defines and initializes a mutex.

```c
struct k_mutex my_mutex;

k_mutex_init(&my_mutex);
```

Alternatively, a mutex can be defined and initialized at compile time
by calling [`K_MUTEX_DEFINE`](../../../doxygen/html/group__mutex__apis.md#gab6f3d98fabbdc0918bbc9934d61d63f3).

The following code has the same effect as the code segment above.

```c
K_MUTEX_DEFINE(my_mutex);
```

### [Locking a Mutex](#id6)

A mutex is locked by calling [`k_mutex_lock()`](../../../doxygen/html/group__mutex__apis.md#ga850549358645249c285669baa49c33b0).

The following code builds on the example above, and waits indefinitely
for the mutex to become available if it is already locked by another thread.

```c
k_mutex_lock(&my_mutex, K_FOREVER);
```

The following code waits up to 100 milliseconds for the mutex to become
available, and gives a warning if the mutex does not become available.

```c
if (k_mutex_lock(&my_mutex, K_MSEC(100)) == 0) {
    /* mutex successfully locked */
} else {
    printf("Cannot lock XYZ display\n");
}
```

### [Unlocking a Mutex](#id7)

A mutex is unlocked by calling [`k_mutex_unlock()`](../../../doxygen/html/group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31).

The following code builds on the example above,
and unlocks the mutex that was previously locked by the thread.

```c
k_mutex_unlock(&my_mutex);
```

## [Suggested Uses](#id8)

Use a mutex to provide exclusive access to a resource, such as a physical
device.

## [Configuration Options](#id9)

Related configuration options:

- [`CONFIG_PRIORITY_CEILING`](../../../kconfig.md#CONFIG_PRIORITY_CEILING "CONFIG_PRIORITY_CEILING")

## [API Reference](#id10)

[Mutex APIs](../../../doxygen/html/group__mutex__apis.md)

Related code samples

- [Dining Philosophers](../../../samples/philosophers/README.md#dining-philosophers "Implement a solution to the Dining Philosophers problem using Zephyr kernel services.")Implement a solution to the Dining Philosophers problem using Zephyr kernel services.

## [Futex API Reference](#id11)

k\_futex is a lightweight mutual exclusion primitive designed to minimize
kernel involvement. Uncontended operation relies only on atomic access
to shared memory. k\_futex are tracked as kernel objects and can live in
user memory so that any access bypasses the kernel object permission
management mechanism.

[FUTEX APIs](../../../doxygen/html/group__futex__apis.md)

## [User Mode Mutex API Reference](#id12)

sys\_mutex behaves almost exactly like k\_mutex, with the added advantage
that a sys\_mutex instance can reside in user memory. When user mode isn’t
enabled, sys\_mutex behaves like k\_mutex.

[User mode mutex APIs](../../../doxygen/html/group__user__mutex__apis.md)
