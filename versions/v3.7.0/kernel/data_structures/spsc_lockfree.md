---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/data_structures/spsc_lockfree.html
original_path: kernel/data_structures/spsc_lockfree.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Single Producer Single Consumer Lock Free Queue

A *Single Producer Single Consumer Lock Free Queue (SPSC)* is a lock free
atomic ring buffer based queue.

## API Reference

*group* SPSC API
:   Single Producer Single Consumer (SPSC) Lockfree Queue API.

    Defines

    SPSC\_INITIALIZER(sz, buf)
    :   Statically initialize an spsc.

        Parameters:
        :   - **sz** – Size of the spsc, must be power of 2 (ex: 2, 4, 8)
            - **buf** – Buffer pointer

    SPSC\_DECLARE(name, type)
    :   Declare an anonymous struct type for an spsc.

        Parameters:
        :   - **name** – Name of the spsc symbol to be provided
            - **type** – Type stored in the spsc

    SPSC\_DEFINE(name, type, sz)
    :   Define an spsc with a fixed size.

        Parameters:
        :   - **name** – Name of the spsc symbol to be provided
            - **type** – Type stored in the spsc
            - **sz** – Size of the spsc, must be power of 2 (ex: 2, 4, 8)

    spsc\_size(spsc)
    :   Size of the SPSC queue.

        Parameters:
        :   - **spsc** – SPSC reference

    spsc\_reset(spsc)
    :   Initialize/reset a spsc such that its empty.

        Note that this is not safe to do while being used in a producer/consumer situation with multiple calling contexts (isrs/threads).

        Parameters:
        :   - **spsc** – SPSC to initialize/reset

    spsc\_acquire(spsc)
    :   Acquire an element to produce from the SPSC.

        Parameters:
        :   - **spsc** – SPSC to acquire an element from for producing

        Returns:
        :   A pointer to the acquired element or null if the spsc is full

    spsc\_produce(spsc)
    :   Produce one previously acquired element to the SPSC.

        This makes one element available to the consumer immediately

        Parameters:
        :   - **spsc** – SPSC to produce the previously acquired element or do nothing

    spsc\_produce\_all(spsc)
    :   Produce all previously acquired elements to the SPSC.

        This makes all previous acquired elements available to the consumer immediately

        Parameters:
        :   - **spsc** – SPSC to produce all previously acquired elements or do nothing

    spsc\_drop\_all(spsc)
    :   Drop all previously acquired elements.

        This makes all previous acquired elements available to be acquired again

        Parameters:
        :   - **spsc** – SPSC to drop all previously acquired elements or do nothing

    spsc\_consume(spsc)
    :   Consume an element from the spsc.

        Parameters:
        :   - **spsc** – Spsc to consume from

        Returns:
        :   Pointer to element or null if no consumable elements left

    spsc\_release(spsc)
    :   Release a consumed element.

        Parameters:
        :   - **spsc** – SPSC to release consumed element or do nothing

    spsc\_release\_all(spsc)
    :   Release all consumed elements.

        Parameters:
        :   - **spsc** – SPSC to release consumed elements or do nothing

    spsc\_acquirable(spsc)
    :   Count of acquirable in spsc.

        Parameters:
        :   - **spsc** – SPSC to get item count for

    spsc\_consumable(spsc)
    :   Count of consumables in spsc.

        Parameters:
        :   - **spsc** – SPSC to get item count for

    spsc\_peek(spsc)
    :   Peek at the first available item in queue.

        Parameters:
        :   - **spsc** – Spsc to peek into

        Returns:
        :   Pointer to element or null if no consumable elements left

    spsc\_next(spsc, item)
    :   Peek at the next item in the queue from a given one.

        Parameters:
        :   - **spsc** – SPSC to peek at
            - **item** – Pointer to an item in the queue

        Returns:
        :   Pointer to element or null if none left

    spsc\_prev(spsc, item)
    :   Get the previous item in the queue from a given one.

        Parameters:
        :   - **spsc** – SPSC to peek at
            - **item** – Pointer to an item in the queue

        Returns:
        :   Pointer to element or null if none left

    struct spsc
    :   Common SPSC attributes.

        Warning

        Not to be manipulated without the macros!
