---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/threads/system_threads.html
original_path: kernel/services/threads/system_threads.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# System Threads

A *system thread* is a thread that the kernel spawns automatically
during system initialization.

The kernel spawns the following system threads:

**Main thread**
:   This thread performs kernel initialization, then calls the application’s
    `main()` function (if one is defined).

    By default, the main thread uses the highest configured preemptible thread
    priority (i.e. 0). If the kernel is not configured to support preemptible
    threads, the main thread uses the lowest configured cooperative thread
    priority (i.e. -1).

    The main thread is an essential thread while it is performing kernel
    initialization or executing the application’s `main()` function;
    this means a fatal system error is raised if the thread aborts. If
    `main()` is not defined, or if it executes and then does a normal
    return, the main thread terminates normally and no error is raised.

**Idle thread**
:   This thread executes when there is no other work for the system to do.
    If possible, the idle thread activates the board’s power management support
    to save power; otherwise, the idle thread simply performs a “do nothing”
    loop. The idle thread remains in existence as long as the system is running
    and never terminates.

    The idle thread always uses the lowest configured thread priority.
    If this makes it a cooperative thread, the idle thread repeatedly
    yields the CPU to allow the application’s other threads to run when
    they need to.

    The idle thread is an essential thread, which means a fatal system error
    is raised if the thread aborts.

Additional system threads may also be spawned, depending on the kernel
and board configuration options specified by the application. For example,
enabling the system workqueue spawns a system thread
that services the work items submitted to it. (See [Workqueue Threads](workqueue.md#workqueues-v2).)

## [Implementation](#id1)

### [Writing a main() function](#id2)

An application-supplied `main()` function begins executing once
kernel initialization is complete. The kernel does not pass any arguments
to the function.

The following code outlines a trivial `main()` function.
The function used by a real application can be as complex as needed.

```c
int main(void)
{
    /* initialize a semaphore */
    ...

    /* register an ISR that gives the semaphore */
    ...

    /* monitor the semaphore forever */
    while (1) {
        /* wait for the semaphore to be given by the ISR */
        ...
        /* do whatever processing is now needed */
        ...
    }
}
```

## [Suggested Uses](#id3)

Use the main thread to perform thread-based processing in an application
that only requires a single thread, rather than defining an additional
application-specific thread.
