---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/entropy.html
original_path: hardware/peripherals/entropy.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Entropy

## Overview

The entropy API provides functions to retrieve entropy values from
entropy hardware present on the platform. The entropy APIs are provided
for use by the random subsystem and cryptographic services. They are not
suitable to be used as random number generation functions.

## API Reference

*group* Entropy Interface
:   Entropy Interface.

    **Since**
    :   1.10

    **Version**
    :   1.0.0

    Defines

    ENTROPY\_BUSYWAIT
    :   Driver is allowed to busy-wait for random data to be ready.

    Typedefs

    typedef int (\*entropy\_get\_entropy\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*buffer, uint16\_t length)
    :   Callback API to get entropy.

        See [entropy\_get\_entropy()](#group__entropy__interface_1ga54de6cd85d5c557ca91f425944e50ce6) for argument description

        Note

        This call has to be thread safe to satisfy requirements of the random subsystem.

    typedef int (\*entropy\_get\_entropy\_isr\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*buffer, uint16\_t length, uint32\_t flags)
    :   Callback API to get entropy from an ISR.

        See [entropy\_get\_entropy\_isr()](#group__entropy__interface_1ga71b99316bec395a7078b26e44f20fc9a) for argument description

    Functions

    int entropy\_get\_entropy(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*buffer, uint16\_t length)
    :   Fills a buffer with entropy.

        Blocks if required in order to generate the necessary random data.

        Parameters:
        :   - **dev** – Pointer to the entropy device.
            - **buffer** – Buffer to fill with entropy.
            - **length** – Buffer length.

        Return values:
        :   - **0** – on success.
            - **-ERRNO** – errno code on error.

    static inline int entropy\_get\_entropy\_isr(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*buffer, uint16\_t length, uint32\_t flags)
    :   Fills a buffer with entropy in a non-blocking or busy-wait manner.

        Callable from ISRs.

        Parameters:
        :   - **dev** – Pointer to the device structure.
            - **buffer** – Buffer to fill with entropy.
            - **length** – Buffer length.
            - **flags** – Flags to modify the behavior of the call.

        Return values:
        :   **number** – of bytes filled with entropy or -error.

    struct entropy\_driver\_api
    :   *#include <entropy.h>*

        Entropy driver API structure.

        This is the mandatory API any Entropy driver needs to expose.
