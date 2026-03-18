---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/ipm.html
original_path: hardware/peripherals/ipm.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Inter-Processor Mailbox (IPM)

## Overview

## API Reference

Related code samples

[IPM on ESP32](../../samples/drivers/ipm/ipm_esp32/README.md#ipm-esp32 "Implement inter-processor mailbox (IPM) between ESP32 APP and PRO CPUs.")
:   Implement inter-processor mailbox (IPM) between ESP32 APP and PRO CPUs.

[IPM on NXP LPC](../../samples/drivers/ipm/ipm_mcux/README.md#ipm-mcux "Implement inter-processor mailbox (IPM) on NXP LPC family.")
:   Implement inter-processor mailbox (IPM) on NXP LPC family.

[IPM on NXP i.MX](../../samples/drivers/ipm/ipm_imx/README.md#ipm-imx "Implement inter-processor mailbox (IPM) on i.MX SoCs containing a Messaging Unit peripheral.")
:   Implement inter-processor mailbox (IPM) on i.MX SoCs containing a Messaging Unit peripheral.

[IPM over IVSHMEM](../../samples/drivers/ipm/ipm_ivshmem/README.md#ipm-ivshmem "Implement inter-processor mailbox (IPM) over IVSHMEM (Inter-VM shared memory)")
:   Implement inter-processor mailbox (IPM) over IVSHMEM (Inter-VM shared memory)

[IPM with ARM MHU](../../samples/drivers/ipm/ipm_mhu_dual_core/README.md#ipm-mhu-dual-core "Implement inter-processor mailbox (IPM) using an MHU (Message Handling Unit)")
:   Implement inter-processor mailbox (IPM) using an MHU (Message Handling Unit)

[OpenAMP](../../samples/subsys/ipc/openamp/README.md#openamp "Send messages between two cores using OpenAMP.")
:   Send messages between two cores using OpenAMP.

[OpenAMP using resource table](../../samples/subsys/ipc/openamp_rsc_table/README.md#openamp-rsc-table "Send messages between two cores using OpenAMP and a resource table.")
:   Send messages between two cores using OpenAMP and a resource table.

*group* ipm\_interface
:   IPM Interface.

    Typedefs

    typedef void (\*ipm\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev, void \*user\_data, uint32\_t id, volatile void \*data)
    :   Callback API for incoming IPM messages.

        These callbacks execute in interrupt context. Therefore, use only interrupt-safe APIS. Registration of callbacks is done via *ipm\_register\_callback*

        Param ipmdev:
        :   Driver instance

        Param user\_data:
        :   Pointer to some private data provided at registration time.

        Param id:
        :   Message type identifier.

        Param data:
        :   Message data pointer. The correct amount of data to read out must be inferred using the message id/upper level protocol.

    typedef int (\*ipm\_send\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev, int wait, uint32\_t id, const void \*data, int size)
    :   Callback API to send IPM messages.

        See *[ipm\_send()](#group__ipm__interface_1ga8f3fe21c1a4ffd3c38b67f81749af043)* for argument definitions.

    typedef int (\*ipm\_max\_data\_size\_get\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev)
    :   Callback API to get maximum data size.

        See *[ipm\_max\_data\_size\_get()](#group__ipm__interface_1ga0a11eecaa7254575ab6baf0783a18b5e)* for argument definitions.

    typedef uint32\_t (\*ipm\_max\_id\_val\_get\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev)
    :   Callback API to get the ID’s maximum value.

        See *[ipm\_max\_id\_val\_get()](#group__ipm__interface_1ga168fd277b7819b639baa4e630c596a7f)* for argument definitions.

    typedef void (\*ipm\_register\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [ipm\_callback\_t](#c.ipm_callback_t) cb, void \*user\_data)
    :   Callback API upon registration.

        See *[ipm\_register\_callback()](#group__ipm__interface_1ga557b15bc8a353483ca55888dba27493b)* for argument definitions.

    typedef int (\*ipm\_set\_enabled\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev, int enable)
    :   Callback API upon enablement of interrupts.

        See *[ipm\_set\_enabled()](#group__ipm__interface_1ga5884fa95cb38ddfe4493eb70dafebe8b)* for argument definitions.

    typedef void (\*ipm\_complete\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev)
    :   Callback API upon command completion.

        See *[ipm\_complete()](#group__ipm__interface_1ga53f785ecfac17b9fb2e5f3a9505c7fd2)* for argument definitions.

    Functions

    int ipm\_send(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev, int wait, uint32\_t id, const void \*data, int size)
    :   Try to send a message over the IPM device.

        A message is considered consumed once the remote interrupt handler finishes. If there is deferred processing on the remote side, or if outgoing messages must be queued and wait on an event/semaphore, a high-level driver can implement that.

        There are constraints on how much data can be sent or the maximum value of id. Use the *ipm\_max\_data\_size\_get* and *ipm\_max\_id\_val\_get* routines to determine them.

        The *size* parameter is used only on the sending side to determine the amount of data to put in the message registers. It is not passed along to the receiving side. The upper-level protocol dictates the amount of data read back.

        Parameters:
        :   - **ipmdev** – Driver instance
            - **wait** – If nonzero, busy-wait for remote to consume the message. The message is considered consumed once the remote interrupt handler finishes. If there is deferred processing on the remote side, or you would like to queue outgoing messages and wait on an event/semaphore, you can implement that in a high-level driver
            - **id** – Message identifier. Values are constrained by *ipm\_max\_data\_size\_get* since many boards only allow for a subset of bits in a 32-bit register to store the ID.
            - **data** – Pointer to the data sent in the message.
            - **size** – Size of the data.

        Return values:
        :   - **-EBUSY** – If the remote hasn’t yet read the last data sent.
            - **-EMSGSIZE** – If the supplied data size is unsupported by the driver.
            - **-EINVAL** – If there was a bad parameter, such as: too-large id value. or the device isn’t an outbound IPM channel.
            - **0** – On success.

    static inline void ipm\_register\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev, [ipm\_callback\_t](#c.ipm_callback_t) cb, void \*user\_data)
    :   Register a callback function for incoming messages.

        Parameters:
        :   - **ipmdev** – Driver instance pointer.
            - **cb** – Callback function to execute on incoming message interrupts.
            - **user\_data** – Application-specific data pointer which will be passed to the callback function when executed.

    int ipm\_max\_data\_size\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev)
    :   Return the maximum number of bytes possible in an outbound message.

        IPM implementations vary on the amount of data that can be sent in a single message since the data payload is typically stored in registers.

        Parameters:
        :   - **ipmdev** – Driver instance pointer.

        Returns:
        :   Maximum possible size of a message in bytes.

    uint32\_t ipm\_max\_id\_val\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev)
    :   Return the maximum id value possible in an outbound message.

        Many IPM implementations store the message’s ID in a register with some bits reserved for other uses.

        Parameters:
        :   - **ipmdev** – Driver instance pointer.

        Returns:
        :   Maximum possible value of a message ID.

    int ipm\_set\_enabled(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev, int enable)
    :   Enable interrupts and callbacks for inbound channels.

        Parameters:
        :   - **ipmdev** – Driver instance pointer.
            - **enable** – Set to 0 to disable and to nonzero to enable.

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If it isn’t an inbound channel.

    void ipm\_complete(const struct [device](../../kernel/drivers/index.md#c.device "device") \*ipmdev)
    :   Signal asynchronous command completion.

        Some IPM backends have an ability to deliver a command asynchronously. The callback will be invoked in interrupt context, but the message (including the provided data pointer) will stay “active” and unacknowledged until later code (presumably in thread mode) calls [ipm\_complete()](#group__ipm__interface_1ga53f785ecfac17b9fb2e5f3a9505c7fd2).

        This function is, obviously, a noop on drivers without async support.

        Parameters:
        :   - **ipmdev** – Driver instance pointer.

    struct ipm\_driver\_api
    :   *#include <ipm.h>*
