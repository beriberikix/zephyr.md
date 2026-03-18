---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/health_cli.html
original_path: connectivity/bluetooth/api/mesh/health_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Health Client

The Health Client model interacts with a Health Server model to read out
diagnostics and control the node’s attention state.

All message passing functions in the Health Client API have `cli` as
their first parameter. This is a pointer to the client model instance to be
used in this function call. The second parameter is the `ctx` or message
context. Message context contains netkey index, appkey index and unicast
address that the target node uses.

The Health Client model is optional, and may be instantiated on any element.
However, if a Health Client model is instantiated on an element other than the
primary, an instance must also be present on the primary element.

See [Health faults](health_srv.md#bluetooth-mesh-health-faults) for a list of specification defined
fault values.

## API reference

*group* bt\_mesh\_health\_cli
:   Health Client Model.

    Defines

    BT\_MESH\_MODEL\_HEALTH\_CLI(cli\_data)
    :   Generic Health Client model composition data entry.

        Parameters:
        :   - **cli\_data** – Pointer to a [Health Client Model](#group__bt__mesh__health__cli) instance.

    Functions

    int bt\_mesh\_health\_cli\_fault\_get(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint16\_t cid, uint8\_t \*test\_id, uint8\_t \*faults, size\_t \*fault\_count)
    :   Get the registered fault state for the given Company ID.

        This method can be used asynchronously by setting `test_id` and ( `faults` or `fault_count` ) as NULL This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `fault_status` callback in `[bt_mesh_health_cli](#structbt__mesh__health__cli)` struct.

        See also

        [Health faults](health_srv.md#group__bt__mesh__health__faults)

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **cid** – Company ID to get the registered faults of.
            - **test\_id** – Test ID response buffer.
            - **faults** – Fault array response buffer.
            - **fault\_count** – Fault count response buffer.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_fault\_clear(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint16\_t cid, uint8\_t \*test\_id, uint8\_t \*faults, size\_t \*fault\_count)
    :   Clear the registered faults for the given Company ID.

        This method can be used asynchronously by setting `test_id` and ( `faults` or `fault_count` ) as NULL This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `fault_status` callback in `[bt_mesh_health_cli](#structbt__mesh__health__cli)` struct.

        See also

        [Health faults](health_srv.md#group__bt__mesh__health__faults)

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **cid** – Company ID to clear the registered faults for.
            - **test\_id** – Test ID response buffer.
            - **faults** – Fault array response buffer.
            - **fault\_count** – Fault count response buffer.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_fault\_clear\_unack(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint16\_t cid)
    :   Clear the registered faults for the given Company ID (unacked).

        See also

        [Health faults](health_srv.md#group__bt__mesh__health__faults)

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **cid** – Company ID to clear the registered faults for.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_fault\_test(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint16\_t cid, uint8\_t test\_id, uint8\_t \*faults, size\_t \*fault\_count)
    :   Invoke a self-test procedure for the given Company ID.

        This method can be used asynchronously by setting `faults` or `fault_count` as NULL This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `fault_status` callback in `[bt_mesh_health_cli](#structbt__mesh__health__cli)` struct.

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **cid** – Company ID to invoke the test for.
            - **test\_id** – Test ID response buffer.
            - **faults** – Fault array response buffer.
            - **fault\_count** – Fault count response buffer.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_fault\_test\_unack(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint16\_t cid, uint8\_t test\_id)
    :   Invoke a self-test procedure for the given Company ID (unacked).

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **cid** – Company ID to invoke the test for.
            - **test\_id** – Test ID response buffer.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_period\_get(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint8\_t \*divisor)
    :   Get the target node’s Health fast period divisor.

        The health period divisor is used to increase the publish rate when a fault is registered. Normally, the Health server will publish with the period in the configured publish parameters. When a fault is registered, the publish period is divided by (1 << divisor). For example, if the target node’s Health server is configured to publish with a period of 16 seconds, and the Health fast period divisor is 5, the Health server will publish with an interval of 500 ms when a fault is registered.

        This method can be used asynchronously by setting `divisor` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `period_status` callback in `[bt_mesh_health_cli](#structbt__mesh__health__cli)` struct.

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **divisor** – Health period divisor response buffer.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_period\_set(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint8\_t divisor, uint8\_t \*updated\_divisor)
    :   Set the target node’s Health fast period divisor.

        The health period divisor is used to increase the publish rate when a fault is registered. Normally, the Health server will publish with the period in the configured publish parameters. When a fault is registered, the publish period is divided by (1 << divisor). For example, if the target node’s Health server is configured to publish with a period of 16 seconds, and the Health fast period divisor is 5, the Health server will publish with an interval of 500 ms when a fault is registered.

        This method can be used asynchronously by setting `updated_divisor` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `period_status` callback in `[bt_mesh_health_cli](#structbt__mesh__health__cli)` struct.

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **divisor** – New Health period divisor.
            - **updated\_divisor** – Health period divisor response buffer.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_period\_set\_unack(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint8\_t divisor)
    :   Set the target node’s Health fast period divisor (unacknowledged).

        This is an unacknowledged version of this API.

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **divisor** – New Health period divisor.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_attention\_get(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint8\_t \*attention)
    :   Get the current attention timer value.

        This method can be used asynchronously by setting `attention` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `attention_status` callback in `[bt_mesh_health_cli](#structbt__mesh__health__cli)` struct.

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **attention** – Attention timer response buffer, measured in seconds.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_attention\_set(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint8\_t attention, uint8\_t \*updated\_attention)
    :   Set the attention timer.

        This method can be used asynchronously by setting `updated_attention` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `attention_status` callback in `[bt_mesh_health_cli](#structbt__mesh__health__cli)` struct.

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **attention** – New attention timer time, in seconds.
            - **updated\_attention** – Attention timer response buffer, measured in seconds.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_health\_cli\_attention\_set\_unack(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint8\_t attention)
    :   Set the attention timer (unacknowledged).

        Parameters:
        :   - **cli** – Client model to send on.
            - **ctx** – Message context, or NULL to use the configured publish parameters.
            - **attention** – New attention timer time, in seconds.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int32\_t bt\_mesh\_health\_cli\_timeout\_get(void)
    :   Get the current transmission timeout value.

        Returns:
        :   The configured transmission timeout in milliseconds.

    void bt\_mesh\_health\_cli\_timeout\_set(int32\_t timeout)
    :   Set the transmission timeout value.

        Parameters:
        :   - **timeout** – The new transmission timeout.

    struct bt\_mesh\_health\_cli
    :   *#include <health\_cli.h>*

        Health Client Model Context.

        Public Members

        const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model
        :   Composition data model entry pointer.

        struct [bt\_mesh\_model\_pub](access.md#c.bt_mesh_model_pub "bt_mesh_model_pub") pub
        :   Publication structure instance.

        struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") pub\_buf
        :   Publication buffer.

        uint8\_t pub\_data[[BT\_MESH\_MODEL\_BUF\_LEN](msg.md#c.BT_MESH_MODEL_BUF_LEN "BT_MESH_MODEL_BUF_LEN")([BT\_MESH\_MODEL\_OP\_2](access.md#c.BT_MESH_MODEL_OP_2 "BT_MESH_MODEL_OP_2")(0x80, 0x32), 3)]
        :   Publication data.

        void (\*period\_status)(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, uint16\_t addr, uint8\_t divisor)
        :   Optional callback for Health Period Status messages.

            Handles received Health Period Status messages from a Health server. The `divisor` param represents the period divisor value.

            Param cli:
            :   Health client that received the status message.

            Param addr:
            :   Address of the sender.

            Param divisor:
            :   Health Period Divisor value.

        void (\*attention\_status)(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, uint16\_t addr, uint8\_t attention)
        :   Optional callback for Health Attention Status messages.

            Handles received Health Attention Status messages from a Health server. The `attention` param represents the current attention value.

            Param cli:
            :   Health client that received the status message.

            Param addr:
            :   Address of the sender.

            Param attention:
            :   Current attention value.

        void (\*fault\_status)(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, uint16\_t addr, uint8\_t test\_id, uint16\_t cid, uint8\_t \*faults, size\_t fault\_count)
        :   Optional callback for Health Fault Status messages.

            Handles received Health Fault Status messages from a Health server. The `fault` array represents all faults that are currently present in the server’s element.

            See also

            [Health faults](health_srv.md#group__bt__mesh__health__faults)

            Param cli:
            :   Health client that received the status message.

            Param addr:
            :   Address of the sender.

            Param test\_id:
            :   Identifier of a most recently performed test.

            Param cid:
            :   Company Identifier of the node.

            Param faults:
            :   Array of faults.

            Param fault\_count:
            :   Number of faults in the fault array.

        void (\*current\_status)(struct [bt\_mesh\_health\_cli](#c.bt_mesh_health_cli) \*cli, uint16\_t addr, uint8\_t test\_id, uint16\_t cid, uint8\_t \*faults, size\_t fault\_count)
        :   Optional callback for Health Current Status messages.

            Handles received Health Current Status messages from a Health server. The `fault` array represents all faults that are currently present in the server’s element.

            See also

            [Health faults](health_srv.md#group__bt__mesh__health__faults)

            Param cli:
            :   Health client that received the status message.

            Param addr:
            :   Address of the sender.

            Param test\_id:
            :   Identifier of a most recently performed test.

            Param cid:
            :   Company Identifier of the node.

            Param faults:
            :   Array of faults.

            Param fault\_count:
            :   Number of faults in the fault array.
