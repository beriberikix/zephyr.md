---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/core.html
original_path: connectivity/bluetooth/api/mesh/core.html
---

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
[`bt_mesh_lpn_poll()`](../../../../doxygen/html/group__bt__mesh.md#ga3fd66605950a55e299ca3a7cc697d453). The LPN operation parameters, including poll
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
by calling [`bt_mesh_rpl_pending_store()`](../../../../doxygen/html/group__bt__mesh.md#ga62f9a72c4e9dc5e4f3f42bd4df4fe452). This is up to the node to decide,
which RPL entries are to be stored in this case.

Setting [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_RPL_STORE_TIMEOUT "CONFIG_BT_MESH_RPL_STORE_TIMEOUT") to -1 allows to completely
switch off the timer, which can help to significantly reduce flash wear out.
This moves the responsibility of storing RPL to the user application and
requires that sufficient power backup is available from the time this API
is called until all RPL entries are written to the flash.

Finding the right balance between [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_RPL_STORE_TIMEOUT "CONFIG_BT_MESH_RPL_STORE_TIMEOUT") and
calling [`bt_mesh_rpl_pending_store()`](../../../../doxygen/html/group__bt__mesh.md#ga62f9a72c4e9dc5e4f3f42bd4df4fe452) may reduce a risk of security
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

All mesh stack bearers advertise data with the [`BT_ID_DEFAULT`](../../../../doxygen/html/group__bt__gap.md#gaded4b52c9bb87fd4d19b1eb9361973e5) local identity.
The value is preset in the mesh stack implementation. When Bluetooth® Low Energy (LE)
and Bluetooth Mesh coexist on the same device, the application should allocate and
configure another local identity for Bluetooth LE purposes before starting the communication.

## API reference

[Bluetooth Mesh](../../../../doxygen/html/group__bt__mesh.md)

Related code samples

- [Bluetooth Mesh badge](../../../../samples/boards/phytec/reel_board/mesh_badge/README.md#mesh_badge "Implement a smart badge using the reel board and Bluetooth Mesh.")Implement a smart badge using the reel board and Bluetooth Mesh.
- [Mesh](../../../../samples/bluetooth/mesh/README.md#ble_mesh "Use basic Bluetooth LE Mesh functionality.")Use basic Bluetooth LE Mesh functionality.
- [Mesh Demo](../../../../samples/bluetooth/mesh_demo/README.md#ble_mesh_demo "Implement a Bluetooth Mesh demo application.")Implement a Bluetooth Mesh demo application.
- [Mesh Models](../../../../samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/README.md#nrf_bluetooth_mesh_onoff_level_lighting_vnd_app "Setup a Bluetooth Mesh node with various models (generic OnOff, generic Level, ...).")Setup a Bluetooth Mesh node with various models (generic OnOff, generic Level, ...).
- [Mesh OnOff Model](../../../../samples/boards/nordic/mesh/onoff-app/README.md#nrf_bluetooth_mesh_onoff "Control LEDs on a mesh network using the Bluetooth Mesh OnOff model.")Control LEDs on a mesh network using the Bluetooth Mesh OnOff model.
- [Mesh Provisioner](../../../../samples/bluetooth/mesh_provisioner/README.md#ble_mesh_provisioner "Provision a node and configure it using the Bluetooth Mesh APIs.")Provision a node and configure it using the Bluetooth Mesh APIs.
