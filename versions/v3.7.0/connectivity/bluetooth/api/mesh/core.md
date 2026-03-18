---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/core.html
original_path: connectivity/bluetooth/api/mesh/core.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Core

The core provides functionality for managing the general Bluetooth Mesh
state.

## Low Power Node

The Low Power Node (LPN) role allows battery powered devices to participate in
a mesh network as a leaf node. An LPN interacts with the mesh network through
a Friend node, which is responsible for relaying any messages directed to the
LPN. The LPN saves power by keeping its radio turned off, and only wakes up to
either send messages or poll the Friend node for any incoming messages.

The radio control and polling is managed automatically by the mesh stack, but
the LPN API allows the application to trigger the polling at any time through
[`bt_mesh_lpn_poll()`](#c.bt_mesh_lpn_poll). The LPN operation parameters, including poll
interval, poll event timing and Friend requirements is controlled through the
[`CONFIG_BT_MESH_LOW_POWER`](../../../../kconfig.md#CONFIG_BT_MESH_LOW_POWER "CONFIG_BT_MESH_LOW_POWER") option and related configuration options.

When using the LPN feature with logging, it is strongly recommended to only use
the [`CONFIG_LOG_MODE_DEFERRED`](../../../../kconfig.md#CONFIG_LOG_MODE_DEFERRED "CONFIG_LOG_MODE_DEFERRED") option. Log modes other than the
deferred may cause unintended delays during processing of log messages. This in
turns will affect scheduling of the receive delay and receive window. The same
limitation applies for the [`CONFIG_BT_MESH_FRIEND`](../../../../kconfig.md#CONFIG_BT_MESH_FRIEND "CONFIG_BT_MESH_FRIEND") option.

## Replay Protection List

The Replay Protection List (RPL) is used to hold recently received sequence
numbers from elements within the mesh network to perform protection against
replay attacks.

To keep a node protected against replay attacks after reboot, it needs to store
the entire RPL in the persistent storage before it is powered off. Depending on
the amount of traffic in a mesh network, storing recently seen sequence numbers
can make flash wear out sooner or later. To mitigate this,
[`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_RPL_STORE_TIMEOUT "CONFIG_BT_MESH_RPL_STORE_TIMEOUT") can be used. This option postpones
storing of RPL entries in the persistent storage.

This option, however, doesn’t completely solve the issue as the node may
get powered off before the timer to store the RPL is fired. To ensure that
messages can not be replayed, the node can initiate storage of the pending
RPL entry (or entries) at any time (or sufficiently before power loss)
by calling [`bt_mesh_rpl_pending_store()`](#c.bt_mesh_rpl_pending_store). This is up to the node to decide,
which RPL entries are to be stored in this case.

Setting [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_RPL_STORE_TIMEOUT "CONFIG_BT_MESH_RPL_STORE_TIMEOUT") to -1 allows to completely
switch off the timer, which can help to significantly reduce flash wear out.
This moves the responsibility of storing RPL to the user application and
requires that sufficient power backup is available from the time this API
is called until all RPL entries are written to the flash.

Finding the right balance between [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_RPL_STORE_TIMEOUT "CONFIG_BT_MESH_RPL_STORE_TIMEOUT") and
calling [`bt_mesh_rpl_pending_store()`](#c.bt_mesh_rpl_pending_store) may reduce a risk of security
vulnerability and flash wear out.

## Persistent storage

The mesh stack uses the [Settings Subsystem](../../../../services/settings/index.md#settings-api) for storing the
device configuration persistently. When the stack configuration changes and
the change needs to be stored persistently, the stack schedules a work item.
The delay between scheduling the work item and submitting it to the workqueue
is defined by the [`CONFIG_BT_MESH_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_STORE_TIMEOUT "CONFIG_BT_MESH_STORE_TIMEOUT") option. Once
storing of data is scheduled, it can not be rescheduled until the work item is
processed. Exceptions are made in certain cases as described below.

When IV index, Sequence Number or CDB configuration have to be stored, the work
item is submitted to the workqueue without the delay. If the work item was
previously scheduled, it will be rescheduled without the delay.

The Replay Protection List uses the same work item to store RPL entries. If
storing of RPL entries is requested and no other configuration is pending to be
stored, the delay is set to [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_RPL_STORE_TIMEOUT "CONFIG_BT_MESH_RPL_STORE_TIMEOUT").
If other stack configuration has to be stored, the delay defined by
the [`CONFIG_BT_MESH_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_STORE_TIMEOUT "CONFIG_BT_MESH_STORE_TIMEOUT") option is less than
[`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_RPL_STORE_TIMEOUT "CONFIG_BT_MESH_RPL_STORE_TIMEOUT"), and the work item was
scheduled by the Replay Protection List, the work item will be rescheduled.

When the work item is running, the stack will store all pending configuration,
including the RPL entries.

### Work item execution context

The [`CONFIG_BT_MESH_SETTINGS_WORKQ`](../../../../kconfig.md#CONFIG_BT_MESH_SETTINGS_WORKQ "CONFIG_BT_MESH_SETTINGS_WORKQ") option configures the
context from which the work item is executed. This option is enabled by
default, and results in stack using a dedicated cooperative thread to
process the work item. This allows the stack to process other incoming and
outgoing messages, as well as other work items submitted to the system
workqueue, while the stack configuration is being stored.

When this option is disabled, the work item is submitted to the system workqueue.
This means that the system workqueue is blocked for the time it takes to store
the stack’s configuration. It is not recommended to disable this option as this
will make the device non-responsive for a noticeable amount of time.

## Advertisement identity

All mesh stack bearers advertise data with the [`BT_ID_DEFAULT`](../gap.md#c.BT_ID_DEFAULT "BT_ID_DEFAULT") local identity.
The value is preset in the mesh stack implementation. When Bluetooth® Low Energy (LE)
and Bluetooth Mesh coexist on the same device, the application should allocate and
configure another local identity for Bluetooth LE purposes before starting the communication.

## API reference

*group* Bluetooth Mesh
:   Bluetooth Mesh.

    Defines

    BT\_MESH\_NET\_PRIMARY
    :   Primary Network Key index.

    BT\_MESH\_FEAT\_RELAY
    :   Relay feature.

    BT\_MESH\_FEAT\_PROXY
    :   GATT Proxy feature.

    BT\_MESH\_FEAT\_FRIEND
    :   Friend feature.

    BT\_MESH\_FEAT\_LOW\_POWER
    :   Low Power Node feature.

    BT\_MESH\_FEAT\_SUPPORTED
    :   Supported heartbeat publication features.

    BT\_MESH\_LPN\_CB\_DEFINE(\_name)
    :   Register a callback structure for Friendship events.

        Parameters:
        :   - **\_name** – Name of callback structure.

    BT\_MESH\_FRIEND\_CB\_DEFINE(\_name)
    :   Register a callback structure for Friendship events.

        Registers a callback structure that will be called whenever Friendship gets established or terminated.

        Parameters:
        :   - **\_name** – Name of callback structure.

    Functions

    int bt\_mesh\_init(const struct [bt\_mesh\_prov](provisioning.md#c.bt_mesh_prov "bt_mesh_prov") \*prov, const struct [bt\_mesh\_comp](access.md#c.bt_mesh_comp "bt_mesh_comp") \*comp)
    :   Initialize Mesh support.

        After calling this API, the node will not automatically advertise as unprovisioned, rather the [bt\_mesh\_prov\_enable()](provisioning.md#group__bt__mesh__prov_1ga6c8dc1b09d4cde8738be83c992b860a9) API needs to be called to enable unprovisioned advertising on one or more provisioning bearers.

        Parameters:
        :   - **prov** – Node provisioning information.
            - **comp** – Node Composition.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    void bt\_mesh\_reset(void)
    :   Reset the state of the local Mesh node.

        Resets the state of the node, which means that it needs to be reprovisioned to become an active node in a Mesh network again.

        After calling this API, the node will not automatically advertise as unprovisioned, rather the [bt\_mesh\_prov\_enable()](provisioning.md#group__bt__mesh__prov_1ga6c8dc1b09d4cde8738be83c992b860a9) API needs to be called to enable unprovisioned advertising on one or more provisioning bearers.

    int bt\_mesh\_suspend(void)
    :   Suspend the Mesh network temporarily.

        This API can be used for power saving purposes, but the user should be aware that leaving the local node suspended for a long period of time may cause it to become permanently disconnected from the Mesh network. If at all possible, the Friendship feature should be used instead, to make the node into a Low Power Node.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_resume(void)
    :   Resume a suspended Mesh network.

        This API resumes the local node, after it has been suspended using the [bt\_mesh\_suspend()](#group__bt__mesh_1ga6c209dbad6881f1e9634d9b7d42f2c34) API.

        Returns:
        :   0 on success, or (negative) error code on failure.

    void bt\_mesh\_iv\_update\_test(bool enable)
    :   Toggle the IV Update test mode.

        This API is only available if the IV Update test mode has been enabled in Kconfig. It is needed for passing most of the IV Update qualification test cases.

        Parameters:
        :   - **enable** – true to enable IV Update test mode, false to disable it.

    bool bt\_mesh\_iv\_update(void)
    :   Toggle the IV Update state.

        This API is only available if the IV Update test mode has been enabled in Kconfig. It is needed for passing most of the IV Update qualification test cases.

        Returns:
        :   true if IV Update In Progress state was entered, false otherwise.

    int bt\_mesh\_lpn\_set(bool enable)
    :   Toggle the Low Power feature of the local device.

        Enables or disables the Low Power feature of the local device. This is exposed as a run-time feature, since the device might want to change this e.g. based on being plugged into a stable power source or running from a battery power source.

        Parameters:
        :   - **enable** – true to enable LPN functionality, false to disable it.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_mesh\_lpn\_poll(void)
    :   Send out a Friend Poll message.

        Send a Friend Poll message to the Friend of this node. If there is no established Friendship the function will return an error.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_mesh\_friend\_terminate(uint16\_t lpn\_addr)
    :   Terminate Friendship.

        Terminated Friendship for given LPN.

        Parameters:
        :   - **lpn\_addr** – Low Power Node address.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    void bt\_mesh\_rpl\_pending\_store(uint16\_t addr)
    :   Store pending RPL entry(ies) in the persistent storage.

        This API allows the user to store pending RPL entry(ies) in the persistent storage without waiting for the timeout.

        Note

        When flash is used as the persistent storage, calling this API too frequently may wear it out.

        Parameters:
        :   - **addr** – Address of the node which RPL entry needs to be stored or [BT\_MESH\_ADDR\_ALL\_NODES](access.md#group__bt__mesh__access_1ga27aafd100b6ccc1de060a75370184620) to store all pending RPL entries.

    const uint8\_t \*bt\_mesh\_va\_uuid\_get(uint16\_t addr, const uint8\_t \*uuid, uint16\_t \*retaddr)
    :   Iterate stored Label UUIDs.

        When `addr` is [BT\_MESH\_ADDR\_UNASSIGNED](access.md#group__bt__mesh__access_1ga6d11790af686e6d48f08c6f1cd65317c), this function iterates over all available addresses starting with `uuid`. In this case, use `retaddr` to get virtual address representation of the returned Label UUID. When `addr` is a virtual address, this function returns next Label UUID corresponding to the `addr`. When `uuid` is NULL, this function returns the first available UUID. If `uuid` is previously returned uuid, this function returns following uuid.

        Parameters:
        :   - **addr** – Virtual address to search for, or [BT\_MESH\_ADDR\_UNASSIGNED](access.md#group__bt__mesh__access_1ga6d11790af686e6d48f08c6f1cd65317c).
            - **uuid** – Pointer to the previously returned Label UUID or NULL.
            - **retaddr** – Pointer to a memory where virtual address representation of the returning UUID is to be stored to.

        Returns:
        :   Pointer to Label UUID, or NULL if no more entries found.

    struct bt\_mesh\_lpn\_cb
    :   *#include <main.h>*

        Low Power Node callback functions.

        Public Members

        void (\*established)(uint16\_t net\_idx, uint16\_t friend\_addr, uint8\_t queue\_size, uint8\_t recv\_window)
        :   Friendship established.

            This callback notifies the application that friendship has been successfully established.

            Param net\_idx:
            :   NetKeyIndex used during friendship establishment.

            Param friend\_addr:
            :   Friend address.

            Param queue\_size:
            :   Friend queue size.

            Param recv\_window:
            :   Low Power Node’s listens duration for Friend response.

        void (\*terminated)(uint16\_t net\_idx, uint16\_t friend\_addr)
        :   Friendship terminated.

            This callback notifies the application that friendship has been terminated.

            Param net\_idx:
            :   NetKeyIndex used during friendship establishment.

            Param friend\_addr:
            :   Friend address.

        void (\*polled)(uint16\_t net\_idx, uint16\_t friend\_addr, bool retry)
        :   Local Poll Request.

            This callback notifies the application that the local node has polled the friend node.

            This callback will be called before [bt\_mesh\_lpn\_cb::established](#structbt__mesh__lpn__cb_1a74b8b398b383518af069266cf3b0be91) when attempting to establish a friendship.

            Param net\_idx:
            :   NetKeyIndex used during friendship establishment.

            Param friend\_addr:
            :   Friend address.

            Param retry:
            :   Retry or first poll request for each transaction.

    struct bt\_mesh\_friend\_cb
    :   *#include <main.h>*

        Friend Node callback functions.

        Public Members

        void (\*established)(uint16\_t net\_idx, uint16\_t lpn\_addr, uint8\_t recv\_delay, uint32\_t polltimeout)
        :   Friendship established.

            This callback notifies the application that friendship has been successfully established.

            Param net\_idx:
            :   NetKeyIndex used during friendship establishment.

            Param lpn\_addr:
            :   Low Power Node address.

            Param recv\_delay:
            :   Receive Delay in units of 1 millisecond.

            Param polltimeout:
            :   PollTimeout in units of 1 millisecond.

        void (\*terminated)(uint16\_t net\_idx, uint16\_t lpn\_addr)
        :   Friendship terminated.

            This callback notifies the application that friendship has been terminated.

            Param net\_idx:
            :   NetKeyIndex used during friendship establishment.

            Param lpn\_addr:
            :   Low Power Node address.

        void (\*polled)(uint16\_t net\_idx, uint16\_t lpn\_addr)
        :   Friend Poll Request.

            This callback notifies the application that the low power node has polled the friend node.

            This callback will be called before [bt\_mesh\_friend\_cb::established](#structbt__mesh__friend__cb_1a824ed814a46a3954d2c6f669c8900156) when attempting to establish a friendship.

            Param net\_idx:
            :   NetKeyIndex used during friendship establishment.

            Param lpn\_addr:
            :   LPN address.
