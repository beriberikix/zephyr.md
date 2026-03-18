---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/volume.html
original_path: connectivity/bluetooth/api/volume.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth Audio Volume Control

## API Reference

*group* bt\_gatt\_vcp
:   Volume Control Profile (VCP).

    [Experimental] Users should note that the APIs can change as a part of ongoing development.

    Defines

    BT\_VCP\_VOL\_REND\_VOCS\_CNT

    BT\_VCP\_VOL\_REND\_AICS\_CNT

    BT\_VCP\_ERR\_INVALID\_COUNTER
    :   Volume Control Service Error codes.

    BT\_VCP\_ERR\_OP\_NOT\_SUPPORTED

    BT\_VCP\_STATE\_UNMUTED
    :   Volume Control Service Mute Values.

    BT\_VCP\_STATE\_MUTED

    Functions

    int bt\_vcp\_vol\_rend\_included\_get(struct [bt\_vcp\_included](#c.bt_vcp_included) \*included)
    :   Get Volume Control Service included services.

        Returns a pointer to a struct that contains information about the Volume Control Service included service instances, such as pointers to the Volume Offset Control Service (Volume Offset Control Service) or Audio Input Control Service (AICS) instances.

        Parameters:
        :   - **included** – **[out]** Pointer to store the result in.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_register(struct [bt\_vcp\_vol\_rend\_register\_param](#c.bt_vcp_vol_rend_register_param) \*param)
    :   Register the Volume Control Service.

        This will register and enable the service and make it discoverable by clients.

        Parameters:
        :   - **param** – Volume Control Service register parameters.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_set\_step(uint8\_t volume\_step)
    :   Set the Volume Control Service volume step size.

        Set the value that the volume changes, when changed relatively with e.g. [bt\_vcp\_vol\_rend\_vol\_down](#group__bt__gatt__vcp_1gaf3c622f151a21d1dd617e97917c5ff5e) or [bt\_vcp\_vol\_rend\_vol\_up](#group__bt__gatt__vcp_1ga6c10dd5a029b524994739f0b37a82c84).

        This can only be done as the server.

        Parameters:
        :   - **volume\_step** – The volume step size (1-255).

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_get\_state(void)
    :   Get the Volume Control Service volume state.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_get\_flags(void)
    :   Get the Volume Control Service flags.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_vol\_down(void)
    :   Turn the volume down by one step on the server.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_vol\_up(void)
    :   Turn the volume up by one step on the server.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_unmute\_vol\_down(void)
    :   Turn the volume down and unmute the server.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_unmute\_vol\_up(void)
    :   Turn the volume up and unmute the server.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_set\_vol(uint8\_t volume)
    :   Set the volume on the server.

        Parameters:
        :   - **volume** – The absolute volume to set.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_unmute(void)
    :   Unmute the server.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_rend\_mute(void)
    :   Mute the server.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_cb\_register(struct [bt\_vcp\_vol\_ctlr\_cb](#c.bt_vcp_vol_ctlr_cb) \*cb)
    :   Registers the callbacks used by the Volume Controller.

        Parameters:
        :   - **cb** – The callback structure.

        Return values:
        :   - **0** – on success
            - **-EINVAL** – if `cb` is NULL
            - **-EALREADY** – if `cb` was already registered

    int bt\_vcp\_vol\_ctlr\_cb\_unregister(struct [bt\_vcp\_vol\_ctlr\_cb](#c.bt_vcp_vol_ctlr_cb) \*cb)
    :   Unregisters the callbacks used by the Volume Controller.

        Parameters:
        :   - **cb** – The callback structure.

        Return values:
        :   - **0** – on success
            - **-EINVAL** – if `cb` is NULL
            - **-EALREADY** – if `cb` was not registered

    int bt\_vcp\_vol\_ctlr\_discover(struct bt\_conn \*conn, struct bt\_vcp\_vol\_ctlr \*\*vol\_ctlr)
    :   Discover Volume Control Service and included services.

        This will start a GATT discovery and setup handles and subscriptions. This shall be called once before any other actions can be executed for the peer device, and the [bt\_vcp\_vol\_ctlr\_cb::discover](#structbt__vcp__vol__ctlr__cb_1ada8fe8d838d6d2c983d746e7e7ed1171) callback will notify when it is possible to start remote operations.

        This shall only be done as the client,

        Parameters:
        :   - **conn** – The connection to discover Volume Control Service for.
            - **vol\_ctlr** – **[out]** Valid remote instance object on success.

        Returns:
        :   0 if success, errno on failure.

    struct bt\_vcp\_vol\_ctlr \*bt\_vcp\_vol\_ctlr\_get\_by\_conn(const struct bt\_conn \*conn)
    :   Get the volume controller from a connection pointer.

        Get the Volume Control Profile Volume Controller pointer from a connection pointer. Only volume controllers that have been initiated via [bt\_vcp\_vol\_ctlr\_discover()](#group__bt__gatt__vcp_1gac18d43a0785155c1131249f95554f2de) can be retrieved.

        Parameters:
        :   - **conn** – Connection pointer.

        Return values:
        :   - **Pointer** – to a Volume Control Profile Volume Controller instance
            - **NULL** – if `conn` is NULL or if the connection has not done discovery yet

    int bt\_vcp\_vol\_ctlr\_conn\_get(const struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct bt\_conn \*\*conn)
    :   Get the connection pointer of a client instance.

        Get the Bluetooth connection pointer of a Volume Control Service client instance.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.
            - **conn** – **[out]** Connection pointer.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_included\_get(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct [bt\_vcp\_included](#c.bt_vcp_included) \*included)
    :   Get Volume Control Service included services.

        Returns a pointer to a struct that contains information about the Volume Control Service included service instances, such as pointers to the Volume Offset Control Service (Volume Offset Control Service) or Audio Input Control Service (AICS) instances.

        Requires that  [`CONFIG_BT_VCP_VOL_CTLR_VOCS`](../../../kconfig.md#CONFIG_BT_VCP_VOL_CTLR_VOCS "CONFIG_BT_VCP_VOL_CTLR_VOCS") or  [`CONFIG_BT_VCP_VOL_CTLR_AICS`](../../../kconfig.md#CONFIG_BT_VCP_VOL_CTLR_AICS "CONFIG_BT_VCP_VOL_CTLR_AICS") is enabled.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.
            - **included** – **[out]** Pointer to store the result in.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_read\_state(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)
    :   Read the volume state of a remote Volume Renderer.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_read\_flags(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)
    :   Read the volume flags of a remote Volume Renderer.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_vol\_down(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)
    :   Turn the volume down one step on a remote Volume Renderer.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_vol\_up(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)
    :   Turn the volume up one step on a remote Volume Renderer.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_unmute\_vol\_down(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)
    :   Turn the volume down one step and unmute on a remote Volume Renderer.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_unmute\_vol\_up(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)
    :   Turn the volume up one step and unmute on a remote Volume Renderer.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_set\_vol(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, uint8\_t volume)
    :   Set the absolute volume on a remote Volume Renderer.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.
            - **volume** – The absolute volume to set.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_unmute(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)
    :   Unmute a remote Volume Renderer.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.

        Returns:
        :   0 if success, errno on failure.

    int bt\_vcp\_vol\_ctlr\_mute(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)
    :   Mute a remote Volume Renderer.

        Parameters:
        :   - **vol\_ctlr** – Volume Controller instance pointer.

        Returns:
        :   0 if success, errno on failure.

    struct bt\_vcp\_vol\_rend\_register\_param
    :   *#include <vcp.h>*

        Register structure for Volume Control Service.

        Public Members

        uint8\_t step
        :   Initial step size (1-255).

        uint8\_t mute
        :   Initial mute state (0-1).

        uint8\_t volume
        :   Initial volume level (0-255).

        struct bt\_vocs\_register\_param vocs\_param[0]
        :   Register parameters for Volume Offset Control Services.

        struct bt\_aics\_register\_param aics\_param[0]
        :   Register parameters for Audio Input Control Services.

        struct [bt\_vcp\_vol\_rend\_cb](#c.bt_vcp_vol_rend_cb) \*cb
        :   Volume Control Service callback structure.

    struct bt\_vcp\_included
    :   *#include <vcp.h>*

        Volume Control Service included services.

        Used for to represent the Volume Control Service included service instances, for either a client or a server. The instance pointers either represent local server instances, or remote service instances.

        Public Members

        uint8\_t vocs\_cnt
        :   Number of Volume Offset Control Service instances.

        struct bt\_vocs \*\*vocs
        :   Array of pointers to Volume Offset Control Service instances.

        uint8\_t aics\_cnt
        :   Number of Audio Input Control Service instances.

        struct bt\_aics \*\*aics
        :   Array of pointers to Audio Input Control Service instances.

    struct bt\_vcp\_vol\_rend\_cb
    :   *#include <vcp.h>*

        Public Members

        void (\*state)(int err, uint8\_t volume, uint8\_t mute)
        :   Callback function for Volume Control Service volume state.

            Called when the value is locally read with [bt\_vcp\_vol\_rend\_get\_state()](#group__bt__gatt__vcp_1ga9d1ac028abc88549ea18b6a0c585c781), or if the state is changed by either the Volume Renderer or a remote Volume Controller.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param volume:
            :   The volume of the Volume Control Service server.

            Param mute:
            :   The mute setting of the Volume Control Service server.

        void (\*flags)(int err, uint8\_t flags)
        :   Callback function for Volume Control Service flags.

            Called when the value is locally read as the server. Called when the value is remotely read as the client. Called if the value is changed by either the server or client.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param flags:
            :   The flags of the Volume Control Service server.

    struct bt\_vcp\_vol\_ctlr\_cb
    :   *#include <vcp.h>*

        Public Members

        void (\*state)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, uint8\_t volume, uint8\_t mute)
        :   Callback function for Volume Control Profile volume state.

            Called when the value is remotely read as the Volume Controller. Called if the value is changed by either the Volume Renderer or Volume Controller, and notified to the to Volume Controller.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param volume:
            :   The volume of the Volume Renderer.

            Param mute:
            :   The mute setting of the Volume Renderer.

        void (\*flags)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, uint8\_t flags)
        :   Callback function for Volume Control Profile volume flags.

            Called when the value is remotely read as the Volume Controller. Called if the value is changed by the Volume Renderer.

            A non-zero value indicates the the volume has been changed on the Volume Renderer since it was booted.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param flags:
            :   The flags of the Volume Renderer.

        void (\*discover)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, uint8\_t vocs\_count, uint8\_t aics\_count)
        :   Callback function for [bt\_vcp\_vol\_ctlr\_discover()](#group__bt__gatt__vcp_1gac18d43a0785155c1131249f95554f2de).

            This callback is called once the discovery procedure is completed.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param vocs\_count:
            :   Number of Volume Offset Control Service instances on the remote Volume Renderer.

            Param aics\_count:
            :   Number of Audio Input Control Service instances the remote Volume Renderer.

        void (\*vol\_down)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)
        :   Callback function for [bt\_vcp\_vol\_ctlr\_vol\_down()](#group__bt__gatt__vcp_1ga03e073e29920f4a530d2f8851b4b8df4).

            Called when the volume down procedure is completed.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

        void (\*vol\_up)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)
        :   Callback function for [bt\_vcp\_vol\_ctlr\_vol\_up()](#group__bt__gatt__vcp_1ga908eb20727e1d68ed569badfd13ff896).

            Called when the volume up procedure is completed.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

        void (\*mute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)
        :   Callback function for [bt\_vcp\_vol\_ctlr\_mute()](#group__bt__gatt__vcp_1ga106b7f826adec665b4f0ac3d5e82b867).

            Called when the mute procedure is completed.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

        void (\*unmute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)
        :   Callback function for [bt\_vcp\_vol\_ctlr\_unmute()](#group__bt__gatt__vcp_1ga4e95c3fb071cb94fbe75f88e96d34b36).

            Called when the unmute procedure is completed.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

        void (\*vol\_down\_unmute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)
        :   Callback function for bt\_vcp\_vol\_ctlr\_vol\_down\_unmute().

            Called when the volume down and unmute procedure is completed.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

        void (\*vol\_up\_unmute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)
        :   Callback function for bt\_vcp\_vol\_ctlr\_vol\_up\_unmute().

            Called when the volume up and unmute procedure is completed.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

        void (\*vol\_set)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)
        :   Callback function for bt\_vcp\_vol\_ctlr\_vol\_set().

            Called when the set absolute volume procedure is completed.

            Param vol\_ctlr:
            :   Volume Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.
