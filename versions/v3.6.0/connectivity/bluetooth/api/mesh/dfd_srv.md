---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/dfd_srv.html
original_path: connectivity/bluetooth/api/mesh/dfd_srv.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Firmware Distribution Server

The Firmware Distribution Server model implements the Distributor role for the
[Device Firmware Update (DFU)](dfu.md#bluetooth-mesh-dfu) subsystem. It extends the [BLOB Transfer Server](blob_srv.md#bluetooth-mesh-blob-srv), which it uses to
receive the firmware image binary from the Initiator node. It also instantiates a
[Firmware Update Client](dfu_cli.md#bluetooth-mesh-dfu-cli), which it uses to distribute firmware updates throughout the mesh
network.

Note

Currently, the Firmware Distribution Server supports out-of-band (OOB) retrieval of firmware
images over SMP service only.

The Firmware Distribution Server does not have an API of its own, but relies on a Firmware
Distribution Client model on a different device to give it information and trigger image
distribution and upload.

## Firmware slots

The Firmware Distribution Server is capable of storing multiple firmware images for distribution.
Each slot contains a separate firmware image with metadata, and can be distributed to other mesh
nodes in the network in any order. The contents, format and size of the firmware images are vendor
specific, and may contain data from other vendors. The application should never attempt to execute
or modify them.

The slots are managed remotely by a Firmware Distribution Client, which can both upload new slots
and delete old ones. The application is notified of changes to the slots through the Firmware
Distribution Server’s callbacks (`bt_mesh_fd_srv_cb`). While the metadata for each
firmware slot is stored internally, the application must provide a [BLOB streams](blob.md#bluetooth-mesh-blob-stream)
for reading and writing the firmware image.

## API reference

*group* bt\_mesh\_dfd\_srv
:   API for the Firmware Distribution Server model.

    Defines

    CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX

    CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_MAX\_SIZE

    CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_SPACE

    BT\_MESH\_DFD\_SRV\_INIT(\_cb)
    :   Initialization parameters for the [Firmware Distribution Server model](#group__bt__mesh__dfd__srv).

        Parameters:
        :   - **\_cb** – **[in]** Pointer to a [bt\_mesh\_dfd\_srv\_cb](#structbt__mesh__dfd__srv__cb) instance.

    BT\_MESH\_MODEL\_DFD\_SRV(\_srv)
    :   Firmware Distribution Server model Composition Data entry.

        Parameters:
        :   - **\_srv** – Pointer to a [Firmware Distribution Server model](#group__bt__mesh__dfd__srv) instance.

    struct bt\_mesh\_dfd\_srv\_cb
    :   *#include <dfd\_srv.h>*

        Firmware Distribution Server callbacks:

        Public Members

        int (\*recv)(struct [bt\_mesh\_dfd\_srv](#c.bt_mesh_dfd_srv) \*srv, const struct [bt\_mesh\_dfu\_slot](dfu.md#c.bt_mesh_dfu_slot "bt_mesh_dfu_slot") \*slot, const struct [bt\_mesh\_blob\_io](blob.md#c.bt_mesh_blob_io "bt_mesh_blob_io") \*\*io)
        :   Slot receive callback.

            Called at the start of an upload procedure. The callback must fill `io` with a pointer to a writable BLOB stream for the Firmware Distribution Server to write the firmware image to.

            Param srv:
            :   Firmware Distribution Server model instance.

            Param slot:
            :   DFU image slot being received.

            Param io:
            :   BLOB stream response pointer.

            Return:
            :   0 on success, or (negative) error code otherwise.

        void (\*del)(struct [bt\_mesh\_dfd\_srv](#c.bt_mesh_dfd_srv) \*srv, const struct [bt\_mesh\_dfu\_slot](dfu.md#c.bt_mesh_dfu_slot "bt_mesh_dfu_slot") \*slot)
        :   Slot delete callback.

            Called when the Firmware Distribution Server is about to delete a DFU image slot. All allocated data associated with the firmware slot should be deleted.

            Param srv:
            :   Firmware Update Server instance.

            Param slot:
            :   DFU image slot being deleted.

        int (\*send)(struct [bt\_mesh\_dfd\_srv](#c.bt_mesh_dfd_srv) \*srv, const struct [bt\_mesh\_dfu\_slot](dfu.md#c.bt_mesh_dfu_slot "bt_mesh_dfu_slot") \*slot, const struct [bt\_mesh\_blob\_io](blob.md#c.bt_mesh_blob_io "bt_mesh_blob_io") \*\*io)
        :   Slot send callback.

            Called at the start of a distribution procedure. The callback must fill `io` with a pointer to a readable BLOB stream for the Firmware Distribution Server to read the firmware image from.

            Param srv:
            :   Firmware Distribution Server model instance.

            Param slot:
            :   DFU image slot being sent.

            Param io:
            :   BLOB stream response pointer.

            Return:
            :   0 on success, or (negative) error code otherwise.

        void (\*phase)(struct [bt\_mesh\_dfd\_srv](#c.bt_mesh_dfd_srv) \*srv, enum [bt\_mesh\_dfd\_phase](dfu.md#c.bt_mesh_dfd_phase "bt_mesh_dfd_phase") phase)
        :   Phase change callback (Optional).

            Called whenever the phase of the Firmware Distribution Server changes.

            Param srv:
            :   Firmware Distribution Server model instance.

            Param phase:
            :   New Firmware Distribution phase.

    struct bt\_mesh\_dfd\_srv
    :   *#include <dfd\_srv.h>*

        Firmware Distribution Server instance.
