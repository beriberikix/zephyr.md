---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/lcd_cli.html
original_path: connectivity/bluetooth/api/mesh/lcd_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Large Composition Data Client

The Large Composition Data Client model is a foundation model defined by the Bluetooth Mesh
specification. The model is optional, and is enabled through the
[`CONFIG_BT_MESH_LARGE_COMP_DATA_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_LARGE_COMP_DATA_CLI "CONFIG_BT_MESH_LARGE_COMP_DATA_CLI") option.

The Large Composition Data Client model was introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and supports the functionality of reading pages of Composition Data that do not fit in
a Config Composition Data Status message and reading the metadata of the model instances on a node
that supports the [Large Composition Data Server](lcd_srv.md#bluetooth-mesh-lcd-srv) model.

The Large Composition Data Client model communicates with a Large Composition Data Server model
using the device key of the node containing the target Large Composition Data Server model instance.

If present, the Large Composition Data Client model must only be instantiated on the primary
element.

## API reference

*group* bt\_mesh\_large\_comp\_data\_cli
:   Defines

    BT\_MESH\_MODEL\_LARGE\_COMP\_DATA\_CLI(cli\_data)
    :   Large Composition Data Client model Composition Data entry.

        Parameters:
        :   - **cli\_data** – Pointer to a [Large Composition Data Client model](#group__bt__mesh__large__comp__data__cli) instance.

    Functions

    int bt\_mesh\_large\_comp\_data\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t page, size\_t offset, struct [bt\_mesh\_large\_comp\_data\_rsp](#c.bt_mesh_large_comp_data_rsp) \*rsp)
    :   Send Large Composition Data Get message.

        This API is used to read a portion of a Composition Data Page.

        This API can be used asynchronously by setting `rsp` as NULL. This way, the method will not wait for a response and will return immediately after sending the command.

        When `rsp` is set, the user is responsible for providing a buffer for the Composition Data in [bt\_mesh\_large\_comp\_data\_rsp::data](#structbt__mesh__large__comp__data__rsp_1a02d92a210b5b7a26b1df4f5076ed99d8). If a buffer is not provided, the metadata won’t be copied.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node element address.
            - **page** – Composition Data Page to read.
            - **offset** – Offset within the Composition Data Page.
            - **rsp** – Pointer to a struct storing the received response from the server, or NULL to not wait for a response.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_models\_metadata\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t page, size\_t offset, struct [bt\_mesh\_large\_comp\_data\_rsp](#c.bt_mesh_large_comp_data_rsp) \*rsp)
    :   Send Models Metadata Get message.

        This API is used to read a portion of a Models Metadata Page.

        This API can be used asynchronously by setting `rsp` as NULL. This way, the method will not wait for a response and will return immediately after sending the command.

        When `rsp` is set, a user is responsible for providing a buffer for metadata in [bt\_mesh\_large\_comp\_data\_rsp::data](#structbt__mesh__large__comp__data__rsp_1a02d92a210b5b7a26b1df4f5076ed99d8). If a buffer is not provided, the metadata won’t be copied.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node element address.
            - **page** – Models Metadata Page to read.
            - **offset** – Offset within the Models Metadata Page.
            - **rsp** – Pointer to a struct storing the received response from the server, or NULL to not wait for a response.

        Returns:
        :   0 on success, or (negative) error code on failure.

    struct bt\_mesh\_large\_comp\_data\_rsp
    :   *#include <large\_comp\_data\_cli.h>*

        Large Composition Data response.

        Public Members

        uint8\_t page
        :   Page number.

        uint16\_t offset
        :   Offset within the page.

        uint16\_t total\_size
        :   Total size of the page.

        struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*data
        :   Pointer to allocated buffer for storing received data.

    struct bt\_mesh\_large\_comp\_data\_cli\_cb
    :   *#include <large\_comp\_data\_cli.h>*

        Large Composition Data Status messages callbacks.

        Public Members

        void (\*large\_comp\_data\_status)(struct [bt\_mesh\_large\_comp\_data\_cli](#c.bt_mesh_large_comp_data_cli) \*cli, uint16\_t addr, struct [bt\_mesh\_large\_comp\_data\_rsp](#c.bt_mesh_large_comp_data_rsp) \*rsp)
        :   Optional callback for Large Composition Data Status message.

            Handles received Large Composition Data Status messages from a Large Composition Data Server.

            If the content of `rsp` is needed after exiting this callback, a user should deep copy it.

            Param cli:
            :   Large Composition Data Client context.

            Param addr:
            :   Address of the sender.

            Param rsp:
            :   Response received from the server.

        void (\*models\_metadata\_status)(struct [bt\_mesh\_large\_comp\_data\_cli](#c.bt_mesh_large_comp_data_cli) \*cli, uint16\_t addr, struct [bt\_mesh\_large\_comp\_data\_rsp](#c.bt_mesh_large_comp_data_rsp) \*rsp)
        :   Optional callback for Models Metadata Status message.

            Handles received Models Metadata Status messages from a Large Composition Data Server.

            If the content of `rsp` is needed after exiting this callback, a user should deep copy it.

            Param cli:
            :   Large Composition Data Client context.

            Param addr:
            :   Address of the sender.

            Param rsp:
            :   Response received from the server.

    struct bt\_mesh\_large\_comp\_data\_cli
    :   *#include <large\_comp\_data\_cli.h>*

        Large Composition Data Client model context.

        Public Members

        const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model
        :   Model entry pointer.

        struct [bt\_mesh\_msg\_ack\_ctx](msg.md#c.bt_mesh_msg_ack_ctx "bt_mesh_msg_ack_ctx") ack\_ctx
        :   Internal parameters for tracking message responses.

        const struct [bt\_mesh\_large\_comp\_data\_cli\_cb](#c.bt_mesh_large_comp_data_cli_cb) \*cb
        :   Optional callback for Large Composition Data Status messages.
