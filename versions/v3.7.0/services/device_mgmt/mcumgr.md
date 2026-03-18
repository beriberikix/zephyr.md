---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/device_mgmt/mcumgr.html
original_path: services/device_mgmt/mcumgr.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# MCUmgr

## Overview

The management subsystem allows remote management of Zephyr-enabled devices.
The following management operations are available:

- Image management
- File System management
- OS management
- Settings (config) management
- Shell management
- Statistic management
- Zephyr management

over the following transports:

- BLE (Bluetooth Low Energy)
- Serial (UART)
- UDP over IP

The management subsystem is based on the Simple Management Protocol (SMP)
provided by [MCUmgr](https://github.com/apache/mynewt-mcumgr), an open source project that provides a
management subsystem that is portable across multiple real-time operating
systems.

The management subsystem is located in [subsys/mgmt/](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/) inside of
the Zephyr tree.

Additionally, there is a [sample](../../samples/subsys/mgmt/mcumgr/smp_svr/README.md#smp-svr "Implement a Simple Management Protocol (SMP) server.") server that provides
management functionality over BLE and serial.

## Tools/libraries

There are various tools and libraries available which enable usage of MCUmgr functionality on a
device which are listed below. Note that these tools are not part of or related to the Zephyr
project.

Tools and Libraries for MCUmgr

| Name | OS support | | | | | Transports | | | Groups | | | | | | | Type | Language | License |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Windows | Linux | mac | Mobile | Embedded | Serial | Bluetooth | UDP | OS | IMG | Stat | Settings | FS | Shell | Zephyr |
| [AuTerm](https://github.com/thedjnK/AuTerm/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Application | C++ (Qt) | GPLv3 |
| [mcumgr-client](https://github.com/vouch-opensource/mcumgr-client/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | Application | Rust | BSD |
| [mcumgr-web](https://github.com/boogie/mcumgr-web/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✓ | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | Web page (chrome only) | Javascript | MIT |
| nRF Connect Device Manager:   [Android](https://github.com/NordicSemiconductor/Android-nRF-Connect-Device-Manager/) and [iOS](https://github.com/NordicSemiconductor/IOS-nRF-Connect-Device-Manager) | ✕ | ✕ | ✕ | ✓ | ✕ | ✕ | ✓ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Library and application | Java, Kotlin, Swift | Apache |
| Zephyr MCUmgr client (in-tree) | ✕ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | Library | C | Apache |

Note that a tick for a particular group indicates basic support for that group in the code, it is
possible that not all commands/features of a group are supported by the implementation.

## J-Link Virtual MSD Interaction Note

On boards where a J-Link OB is present which has both CDC and MSC (virtual Mass
Storage Device, also known as drag-and-drop) support, the MSD functionality can
prevent MCUmgr commands over the CDC UART port from working due to how USB
endpoints are configured in the J-Link firmware (for example on the
[Nordic nrf52840dk/nrf52840 board](../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840)) because of
limiting the maximum packet size (most likely to occur when using image
management commands for updating firmware). This issue can be
resolved by disabling MSD functionality on the J-Link device, follow the
instructions on [Disabling the Mass Storage Device functionality](../../develop/flash_debug/nordic_segger.md#nordic-segger-msd) to disable MSD support.

## Bootloader Integration

The [Device Firmware Upgrade](dfu.md#dfu) subsystem integrates the management subsystem with the
bootloader, providing the ability to send and upgrade a Zephyr image to a
device.

Currently only the MCUboot bootloader is supported. See [MCUboot](dfu.md#mcuboot) for more
information.

## Discord channel

Developers welcome!

- Discord mcumgr channel: [https://discord.com/invite/Ck7jw53nU2](https://discord.com/invite/Ck7jw53nU2)

## API Reference

*group* MCUmgr mgmt API
:   MCUmgr mgmt API.

    **Since**
    :   1.11

    **Version**
    :   1.0.0

    Defines

    MGMT\_CTXT\_SET\_RC\_RSN(mc, rsn)

    MGMT\_CTXT\_RC\_RSN(mc)

    MGMT\_RETURN\_CHECK(ok)
    :   Used at end of MCUmgr handlers to return an error if the message size limit was reached, or OK if it was not.

    MGMT\_HDR\_SIZE

    Typedefs

    typedef void \*(\*mgmt\_alloc\_rsp\_fn)(const void \*src\_buf, void \*arg)
    :   Allocates a buffer suitable for holding a response.

        If a source buf is provided, its user data is copied into the new buffer.

        Param src\_buf:
        :   An optional source buffer to copy user data from.

        Param arg:
        :   Optional streamer argument.

        Return:
        :   Newly-allocated buffer on success NULL on failure.

    typedef void (\*mgmt\_reset\_buf\_fn)(void \*buf, void \*arg)
    :   Resets a buffer to a length of 0.

        The buffer’s user data remains, but its payload is cleared.

        Param buf:
        :   The buffer to reset.

        Param arg:
        :   Optional streamer argument.

    typedef int (\*mgmt\_handler\_fn)(struct smp\_streamer \*ctxt)
    :   Processes a request and writes the corresponding response.

        A separate handler is required for each supported op-ID pair.

        Param ctxt:
        :   The mcumgr context to use.

        Return:
        :   0 if a response was successfully encoded, [mcumgr\_err\_t](#group__mcumgr__mgmt__api_1gac5d8757a7ca945c77f405764b85ad5c5) code on failure.

    Enums

    enum mcumgr\_op\_t
    :   Opcodes; encoded in first byte of header.

        *Values:*

        enumerator MGMT\_OP\_READ = 0
        :   Read op-code.

        enumerator MGMT\_OP\_READ\_RSP
        :   Read response op-code.

        enumerator MGMT\_OP\_WRITE
        :   Write op-code.

        enumerator MGMT\_OP\_WRITE\_RSP
        :   Write response op-code.

    enum mcumgr\_group\_t
    :   MCUmgr groups.

        The first 64 groups are reserved for system level mcumgr commands. Per-user commands are then defined after group 64.

        *Values:*

        enumerator MGMT\_GROUP\_ID\_OS = 0
        :   OS (operating system) group.

        enumerator MGMT\_GROUP\_ID\_IMAGE
        :   Image management group, used for uploading firmware images.

        enumerator MGMT\_GROUP\_ID\_STAT
        :   Statistic management group, used for retrieving statistics.

        enumerator MGMT\_GROUP\_ID\_SETTINGS
        :   Settings management (config) group, used for reading/writing settings.

        enumerator MGMT\_GROUP\_ID\_LOG
        :   Log management group (unused).

        enumerator MGMT\_GROUP\_ID\_CRASH
        :   Crash group (unused).

        enumerator MGMT\_GROUP\_ID\_SPLIT
        :   Split image management group (unused).

        enumerator MGMT\_GROUP\_ID\_RUN
        :   Run group (unused).

        enumerator MGMT\_GROUP\_ID\_FS
        :   FS (file system) group, used for performing file IO operations.

        enumerator MGMT\_GROUP\_ID\_SHELL
        :   Shell management group, used for executing shell commands.

        enumerator MGMT\_GROUP\_ID\_PERUSER = 64
        :   User groups defined from 64 onwards.

        enumerator ZEPHYR\_MGMT\_GRP\_BASIC = ([MGMT\_GROUP\_ID\_PERUSER](#c.mcumgr_group_t.MGMT_GROUP_ID_PERUSER) - 1)
        :   Zephyr-specific groups decrease from PERUSER to avoid collision with upstream and user-defined groups.

            Zephyr-specific: Basic group

    enum mcumgr\_err\_t
    :   MCUmgr error codes.

        *Values:*

        enumerator MGMT\_ERR\_EOK = 0
        :   No error (success).

        enumerator MGMT\_ERR\_EUNKNOWN
        :   Unknown error.

        enumerator MGMT\_ERR\_ENOMEM
        :   Insufficient memory (likely not enough space for CBOR object).

        enumerator MGMT\_ERR\_EINVAL
        :   Error in input value.

        enumerator MGMT\_ERR\_ETIMEOUT
        :   Operation timed out.

        enumerator MGMT\_ERR\_ENOENT
        :   No such file/entry.

        enumerator MGMT\_ERR\_EBADSTATE
        :   Current state disallows command.

        enumerator MGMT\_ERR\_EMSGSIZE
        :   Response too large.

        enumerator MGMT\_ERR\_ENOTSUP
        :   Command not supported.

        enumerator MGMT\_ERR\_ECORRUPT
        :   Corrupt.

        enumerator MGMT\_ERR\_EBUSY
        :   Command blocked by processing of other command.

        enumerator MGMT\_ERR\_EACCESSDENIED
        :   Access to specific function, command or resource denied.

        enumerator MGMT\_ERR\_UNSUPPORTED\_TOO\_OLD
        :   Requested SMP MCUmgr protocol version is not supported (too old).

        enumerator MGMT\_ERR\_UNSUPPORTED\_TOO\_NEW
        :   Requested SMP MCUmgr protocol version is not supported (too new).

        enumerator MGMT\_ERR\_EPERUSER = 256
        :   User errors defined from 256 onwards.

    Functions

    void mgmt\_register\_group(struct [mgmt\_group](#c.mgmt_group) \*group)
    :   Registers a full command group.

        Parameters:
        :   - **group** – The group to register.

    void mgmt\_unregister\_group(struct [mgmt\_group](#c.mgmt_group) \*group)
    :   Unregisters a full command group.

        Parameters:
        :   - **group** – The group to register.

    const struct [mgmt\_handler](#c.mgmt_handler) \*mgmt\_find\_handler(uint16\_t group\_id, uint16\_t command\_id)
    :   Finds a registered command handler.

        Parameters:
        :   - **group\_id** – The group of the command to find.
            - **command\_id** – The ID of the command to find.

        Returns:
        :   The requested command handler on success; NULL on failure.

    const struct [mgmt\_group](#c.mgmt_group) \*mgmt\_find\_group(uint16\_t group\_id)
    :   Finds a registered command group.

        Parameters:
        :   - **group\_id** – The group id of the command group to find.

        Returns:
        :   The requested group on success; NULL on failure.

    const struct [mgmt\_handler](#c.mgmt_handler) \*mgmt\_get\_handler(const struct [mgmt\_group](#c.mgmt_group) \*group, uint16\_t command\_id)
    :   Finds a registered command handler.

        Parameters:
        :   - **group** – The group of the command to find.
            - **command\_id** – The ID of the command to find.

        Returns:
        :   The requested command handler on success; NULL on failure.

    struct mgmt\_handler
    :   *#include <mgmt.h>*

        Read handler and write handler for a single command ID.

        Set use\_custom\_payload to true when using a user defined payload type

    struct mgmt\_group
    :   *#include <mgmt.h>*

        A collection of handlers for an entire command group.

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Entry list node.

        const struct [mgmt\_handler](#c.mgmt_handler) \*mg\_handlers
        :   Array of handlers; one entry per command ID.

        uint16\_t mg\_group\_id
        :   The numeric ID of this group.
