---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/health_srv.html
original_path: connectivity/bluetooth/api/mesh/health_srv.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Health Server

The Health Server model provides attention callbacks and node diagnostics for
[Health Client](health_cli.md#bluetooth-mesh-models-health-cli) models. It is primarily used to report
faults in the mesh node and map the mesh nodes to their physical location.

If present, the Health Server model must be instantiated on the primary element.

## Faults

The Health Server model may report a list of faults that have occurred in the
device’s lifetime. Typically, the faults are events or conditions that may
alter the behavior of the node, like power outages or faulty peripherals.
Faults are split into warnings and errors. Warnings indicate conditions that
are close to the limits of what the node is designed to withstand, but not
necessarily damaging to the device. Errors indicate conditions that are
outside of the node’s design limits, and may have caused invalid behavior or
permanent damage to the device.

Fault values `0x01` to `0x7f` are reserved for the Bluetooth Mesh
specification, and the full list of specification defined faults are available
in [Health faults](#bluetooth-mesh-health-faults). Fault values `0x80` to `0xff` are
vendor specific. The list of faults are always reported with a company ID to
help interpreting the vendor specific faults.

## Attention state

The attention state is used to make the device call attention to itself
through some physical behavior like blinking, playing a sound or vibrating.
The attention state may be used during provisioning to let the user know which
device they’re provisioning, as well as through the Health models at runtime.

The attention state is always assigned a timeout in the range of one to 255
seconds when enabled. The Health Server API provides two callbacks for the
application to run their attention calling behavior:
[`bt_mesh_health_srv_cb.attn_on`](#c.bt_mesh_health_srv_cb.attn_on) is called at the beginning of the
attention period, [`bt_mesh_health_srv_cb.attn_off`](#c.bt_mesh_health_srv_cb.attn_off) is called at
the end.

The remaining time for the attention period may be queried through
[`bt_mesh_health_srv.attn_timer`](#c.bt_mesh_health_srv.attn_timer).

## API reference

*group* bt\_mesh\_health\_srv
:   Health Server Model.

    Defines

    BT\_MESH\_HEALTH\_PUB\_DEFINE(\_name, \_max\_faults)
    :   A helper to define a health publication context.

        Parameters:
        :   - **\_name** – Name given to the publication context variable.
            - **\_max\_faults** – Maximum number of faults the element can have.

    BT\_MESH\_MODEL\_HEALTH\_SRV(srv, pub)
    :   Define a new health server model.

        Note that this API needs to be repeated for each element that the application wants to have a health server model on. Each instance also needs a unique [bt\_mesh\_health\_srv](#structbt__mesh__health__srv) and [bt\_mesh\_model\_pub](access.md#structbt__mesh__model__pub) context.

        Parameters:
        :   - **srv** – Pointer to a unique struct [bt\_mesh\_health\_srv](#structbt__mesh__health__srv).
            - **pub** – Pointer to a unique struct [bt\_mesh\_model\_pub](access.md#structbt__mesh__model__pub).

        Returns:
        :   New mesh model instance.

    BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID
    :   Health Test Information Metadata ID.

    BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA(tests)

    BT\_MESH\_HEALTH\_TEST\_INFO(cid, tests...)
    :   Define a Health Test Info Metadata array.

        Parameters:
        :   - **cid** – Company ID of the Health Test suite.
            - **tests** – A comma separated list of tests.

        Returns:
        :   A comma separated list of values that make Health Test Info Metadata

    Functions

    int bt\_mesh\_health\_srv\_fault\_update(const struct [bt\_mesh\_elem](access.md#c.bt_mesh_elem "bt_mesh_elem") \*elem)
    :   Notify the stack that the fault array state of the given element has changed.

        This prompts the Health server on this element to publish the current fault array if periodic publishing is disabled.

        Parameters:
        :   - **elem** – Element to update the fault state of.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    struct bt\_mesh\_health\_srv\_cb
    :   *#include <health\_srv.h>*

        Callback function for the Health Server model.

        Public Members

        int (\*fault\_get\_cur)(const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model, uint8\_t \*test\_id, uint16\_t \*company\_id, uint8\_t \*faults, uint8\_t \*fault\_count)
        :   Callback for fetching current faults.

            Fault values may either be defined by the specification, or by a vendor. Vendor specific faults should be interpreted in the context of the accompanying Company ID. Specification defined faults may be reported for any Company ID, and the same fault may be presented for multiple Company IDs.

            All faults shall be associated with at least one Company ID, representing the device vendor or some other vendor whose vendor specific fault values are used.

            If there are multiple Company IDs that have active faults, return only the faults associated with one of them at the time. To report faults for multiple Company IDs, interleave which Company ID is reported for each call.

            Param model:
            :   Health Server model instance to get faults of.

            Param test\_id:
            :   Test ID response buffer.

            Param company\_id:
            :   Company ID response buffer.

            Param faults:
            :   Array to fill with current faults.

            Param fault\_count:
            :   The number of faults the fault array can fit. Should be updated to reflect the number of faults copied into the array.

            Return:
            :   0 on success, or (negative) error code otherwise.

        int (\*fault\_get\_reg)(const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model, uint16\_t company\_id, uint8\_t \*test\_id, uint8\_t \*faults, uint8\_t \*fault\_count)
        :   Callback for fetching all registered faults.

            Registered faults are all past and current faults since the last call to `fault_clear`. Only faults associated with the given Company ID should be reported.

            Fault values may either be defined by the specification, or by a vendor. Vendor specific faults should be interpreted in the context of the accompanying Company ID. Specification defined faults may be reported for any Company ID, and the same fault may be presented for multiple Company IDs.

            Param model:
            :   Health Server model instance to get faults of.

            Param company\_id:
            :   Company ID to get faults for.

            Param test\_id:
            :   Test ID response buffer.

            Param faults:
            :   Array to fill with registered faults.

            Param fault\_count:
            :   The number of faults the fault array can fit. Should be updated to reflect the number of faults copied into the array.

            Return:
            :   0 on success, or (negative) error code otherwise.

        int (\*fault\_clear)(const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model, uint16\_t company\_id)
        :   Clear all registered faults associated with the given Company ID.

            Param model:
            :   Health Server model instance to clear faults of.

            Param company\_id:
            :   Company ID to clear faults for.

            Return:
            :   0 on success, or (negative) error code otherwise.

        int (\*fault\_test)(const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model, uint8\_t test\_id, uint16\_t company\_id)
        :   Run a self-test.

            The Health server may support up to 256 self-tests for each Company ID. The behavior for all test IDs are vendor specific, and should be interpreted based on the accompanying Company ID. Test failures should result in changes to the fault array.

            Param model:
            :   Health Server model instance to run test for.

            Param test\_id:
            :   Test ID to run.

            Param company\_id:
            :   Company ID to run test for.

            Return:
            :   0 if the test execution was started successfully, or (negative) error code otherwise. Note that the fault array will not be reported back to the client if the test execution didn’t start.

        void (\*attn\_on)(const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model)
        :   Start calling attention to the device.

            The attention state is used to map an element address to a physical device. When this callback is called, the device should start some physical procedure meant to call attention to itself, like blinking, buzzing, vibrating or moving. If there are multiple Health server instances on the device, the attention state should also help identify the specific element the server is in.

            The attention calling behavior should continue until the `attn_off` callback is called.

            Param model:
            :   Health Server model to start the attention state of.

        void (\*attn\_off)(const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model)
        :   Stop the attention state.

            Any physical activity started to call attention to the device should be stopped.

            Param model:

    struct bt\_mesh\_health\_srv
    :   *#include <health\_srv.h>*

        Mesh Health Server Model Context.

        Public Members

        const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model
        :   Composition data model entry pointer.

        const struct [bt\_mesh\_health\_srv\_cb](#c.bt_mesh_health_srv_cb) \*cb
        :   Optional callback struct.

        struct [k\_work\_delayable](../../../../kernel/services/threads/workqueue.md#c.k_work_delayable "k_work_delayable") attn\_timer
        :   Attention Timer state.

### Health faults

Fault values defined by the Bluetooth Mesh specification.

*group* bt\_mesh\_health\_faults
:   List of specification defined Health fault values.

    Defines

    BT\_MESH\_HEALTH\_FAULT\_NO\_FAULT
    :   No fault has occurred.

    BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_MEMORY\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_MEMORY\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_TAMPER\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_TAMPER\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_EMPTY\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_EMPTY\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_WARNING

    BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_ERROR

    BT\_MESH\_HEALTH\_FAULT\_VENDOR\_SPECIFIC\_START
    :   Start of the vendor specific fault values.

        All values below this are reserved for the Bluetooth Specification.
