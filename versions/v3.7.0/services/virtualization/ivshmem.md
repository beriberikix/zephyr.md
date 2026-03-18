---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/virtualization/ivshmem.html
original_path: services/virtualization/ivshmem.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Inter-VM Shared Memory

## [Overview](#id1)

As Zephyr is enabled to run as a guest OS on Qemu and
[ACRN](https://projectacrn.github.io/latest/tutorials/using_zephyr_as_uos.html)
it might be necessary to make VMs aware of each other, or aware of the host.
This is made possible by exposing a shared memory among parties via a feature
called ivshmem, which stands for inter-VM Shared Memory.

The two types are supported: a plain shared memory (ivshmem-plain) or a shared
memory with the ability for a VM to generate an interruption on another, and
thus to be interrupted as well itself (ivshmem-doorbell).

Please refer to the official [Qemu ivshmem documentation](https://www.qemu.org/docs/master/system/devices/ivshmem.html) for more information.

## [Support](#id2)

Zephyr supports both versions: plain and doorbell. Ivshmem driver can be built
by enabling [`CONFIG_IVSHMEM`](../../kconfig.md#CONFIG_IVSHMEM "CONFIG_IVSHMEM"). By default, this will expose the plain
version. [`CONFIG_IVSHMEM_DOORBELL`](../../kconfig.md#CONFIG_IVSHMEM_DOORBELL "CONFIG_IVSHMEM_DOORBELL") needs to be enabled to get the
doorbell version.

Because the doorbell version uses MSI-X vectors to support notification vectors,
the [`CONFIG_IVSHMEM_MSI_X_VECTORS`](../../kconfig.md#CONFIG_IVSHMEM_MSI_X_VECTORS "CONFIG_IVSHMEM_MSI_X_VECTORS") has to be tweaked to the number of
vectors that will be needed.

Note that a tiny shell module can be exposed to test the ivshmem feature by
enabling [`CONFIG_IVSHMEM_SHELL`](../../kconfig.md#CONFIG_IVSHMEM_SHELL "CONFIG_IVSHMEM_SHELL").

## [ivshmem-v2](#id3)

Zephyr also supports ivshmem-v2:

[https://github.com/siemens/jailhouse/blob/master/Documentation/ivshmem-v2-specification.md](https://github.com/siemens/jailhouse/blob/master/Documentation/ivshmem-v2-specification.md)

This is primarily used for IPC in the Jailhouse hypervisor
(e.g. [Inter-VM Shared Memory (ivshmem) Ethernet](../../samples/drivers/ethernet/eth_ivshmem/README.md#eth-ivshmem "Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.")). It is also possible to use ivshmem-v2 without
Jailhouse by building the Siemens fork of QEMU, and modifying the QEMU launch flags:

[https://github.com/siemens/qemu/tree/wip/ivshmem2](https://github.com/siemens/qemu/tree/wip/ivshmem2)

## [API Reference](#id4)

Related code samples

[IVSHMEM doorbell](../../samples/drivers/virtualization/ivshmem/doorbell/README.md#ivshmem-doorbell "Use Inter-VM Shared Memory to exchange messages between two processes running on different operating systems.")
:   Use Inter-VM Shared Memory to exchange messages between two processes running on different
    operating systems.

[Inter-VM Shared Memory (ivshmem) Ethernet](../../samples/drivers/ethernet/eth_ivshmem/README.md#eth-ivshmem "Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.")
:   Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.

*group* Inter-VM Shared Memory (ivshmem) reference API
:   Inter-VM Shared Memory (ivshmem) reference API.

    Defines

    IVSHMEM\_V2\_PROTO\_UNDEFINED

    IVSHMEM\_V2\_PROTO\_NET

    Typedefs

    typedef size\_t (\*ivshmem\_get\_mem\_f)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uintptr\_t \*memmap)

    typedef uint32\_t (\*ivshmem\_get\_id\_f)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)

    typedef uint16\_t (\*ivshmem\_get\_vectors\_f)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)

    typedef int (\*ivshmem\_int\_peer\_f)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t peer\_id, uint16\_t vector)

    typedef int (\*ivshmem\_register\_handler\_f)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*signal, uint16\_t vector)

    Functions

    size\_t ivshmem\_get\_mem(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uintptr\_t \*memmap)
    :   Get the inter-VM shared memory.

        Note: This API is not supported for ivshmem-v2, as the R/W and R/O areas may not be mapped contiguously. For ivshmem-v2, use the ivshmem\_get\_rw\_mem\_section, ivshmem\_get\_output\_mem\_section and ivshmem\_get\_state APIs to access the shared memory.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **memmap** – A pointer to fill in with the memory address

        Returns:
        :   the size of the memory mapped, or 0

    uint32\_t ivshmem\_get\_id(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get our VM ID.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance

        Returns:
        :   our VM ID or 0 if we are not running on doorbell version

    uint16\_t ivshmem\_get\_vectors(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the number of interrupt vectors we can use.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance

        Returns:
        :   the number of available interrupt vectors

    int ivshmem\_int\_peer(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t peer\_id, uint16\_t vector)
    :   Interrupt another VM.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **peer\_id** – The VM ID to interrupt
            - **vector** – The interrupt vector to use

        Returns:
        :   0 on success, a negative errno otherwise

    int ivshmem\_register\_handler(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*signal, uint16\_t vector)
    :   Register a vector notification (interrupt) handler.

        Note: The returned status, if positive, to a raised signal is the vector that generated the signal. This lets the possibility to the user to have one signal for all vectors, or one per-vector.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **signal** – A pointer to a valid and ready to be signaled struct [k\_poll\_signal](../../kernel/services/polling.md#structk__poll__signal). Or NULL to unregister any handler registered for the given vector.
            - **vector** – The interrupt vector to get notification from

        Returns:
        :   0 on success, a negative errno otherwise

    struct ivshmem\_driver\_api
    :   *#include <ivshmem.h>*
