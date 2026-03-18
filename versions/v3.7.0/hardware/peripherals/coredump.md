---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/coredump.html
original_path: hardware/peripherals/coredump.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Coredump Device

## Overview

The coredump device is a pseudo-device driver with two types.A COREDUMP\_TYPE\_MEMCPY
type exposes device tree bindings for memory address/size values to be included in
any dump. And the driver exposes an API to add/remove dump memory regions at runtime.
A COREDUMP\_TYPE\_CALLBACK device requires exactly one entry in the memory-regions
array with a size of 0 and a desired size. The driver will statically allocate memory
of the desired size and provide an API to register a callback function to fill that
memory when a dump occurs.

## Configuration Options

Related configuration options:

- [`CONFIG_COREDUMP_DEVICE`](../../kconfig.md#CONFIG_COREDUMP_DEVICE "CONFIG_COREDUMP_DEVICE")

## API Reference

*group* Coredump pseudo-device driver APIs
:   Coredump pseudo-device driver APIs.

    Typedefs

    typedef void (\*coredump\_dump\_callback\_t)(uintptr\_t dump\_area, size\_t dump\_area\_size)
    :   Callback that occurs at dump time, data copied into dump\_area will be included in the dump that is generated.

        Param dump\_area:
        :   Pointer to area to copy data into for inclusion in dump

        Param dump\_area\_size:
        :   Size of available memory at dump\_area

    Functions

    static inline bool coredump\_device\_register\_memory(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [coredump\_mem\_region\_node](#c.coredump_mem_region_node) \*region)
    :   Register a region of memory to be stored in core dump at the time it is generated.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **region** – Struct describing memory to be collected

        Returns:
        :   true if registration succeeded

        Returns:
        :   false if registration failed

    static inline bool coredump\_device\_unregister\_memory(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [coredump\_mem\_region\_node](#c.coredump_mem_region_node) \*region)
    :   Unregister a region of memory to be stored in core dump at the time it is generated.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **region** – Struct describing memory to be collected

        Returns:
        :   true if unregistration succeeded

        Returns:
        :   false if unregistration failed

    static inline bool coredump\_device\_register\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [coredump\_dump\_callback\_t](#c.coredump_dump_callback_t) callback)
    :   Register a callback to be invoked at dump time.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **callback** – Callback to be invoked at dump time

        Returns:
        :   true if registration succeeded

        Returns:
        :   false if registration failed

    struct coredump\_mem\_region\_node
    :   *#include <coredump.h>*

        Structure describing a region in memory that may be stored in core dump at the time it is generated.

        Instances of this are passed to the [coredump\_device\_register\_memory()](#group__coredump__device__interface_1ga14ccecab2b077a32a0bc3bf4ec5df909) and [coredump\_device\_unregister\_memory()](#group__coredump__device__interface_1gafd4e43696175eeb3ad1a2894df945530) functions to indicate addition and removal of memory regions to be captured

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Node of single-linked list, do not modify.

        uintptr\_t start
        :   Address of start of memory region.

        size\_t size
        :   Size of memory region.
