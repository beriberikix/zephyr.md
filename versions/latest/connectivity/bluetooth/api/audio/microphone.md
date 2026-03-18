---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/audio/microphone.html
original_path: connectivity/bluetooth/api/audio/microphone.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth Microphone Control

## API Reference

*group* Microphone Control Profile (MICP)
:   Microphone Control Profile (MICP).

    **Since**
    :   2.7

    **Version**
    :   0.8.0

    Application error codes

    BT\_MICP\_ERR\_MUTE\_DISABLED
    :   Mute/unmute commands are disabled.

    Microphone Control Profile mute states

    BT\_MICP\_MUTE\_UNMUTED
    :   The microphone state is unmuted.

    BT\_MICP\_MUTE\_MUTED
    :   The microphone state is muted.

    BT\_MICP\_MUTE\_DISABLED
    :   The microphone state is disabled and cannot be muted or unmuted.

    Defines

    BT\_MICP\_MIC\_DEV\_AICS\_CNT
    :   Defines the maximum number of Microphone Control Service instances for the Microphone Control Profile Microphone Device.

    Functions

    int bt\_micp\_mic\_dev\_register(struct [bt\_micp\_mic\_dev\_register\_param](#c.bt_micp_mic_dev_register_param) \*param)
    :   Initialize the Microphone Control Profile Microphone Device.

        This will enable the Microphone Control Service instance and make it discoverable by Microphone Controllers.

        Parameters:
        :   - **param** – Pointer to an initialization structure.

        Returns:
        :   0 if success, errno on failure.

    int bt\_micp\_mic\_dev\_included\_get(struct [bt\_micp\_included](#c.bt_micp_included) \*included)
    :   Get Microphone Device included services.

        Returns a pointer to a struct that contains information about the Microphone Device included Audio Input Control Service instances.

        Requires that  [`CONFIG_BT_MICP_MIC_DEV_AICS`](../../../../kconfig.md#CONFIG_BT_MICP_MIC_DEV_AICS "CONFIG_BT_MICP_MIC_DEV_AICS") is enabled.

        Parameters:
        :   - **included** – Pointer to store the result in.

        Returns:
        :   0 if success, errno on failure.

    int bt\_micp\_mic\_dev\_unmute(void)
    :   Unmute the Microphone Device.

        Returns:
        :   0 on success, GATT error value on fail.

    int bt\_micp\_mic\_dev\_mute(void)
    :   Mute the Microphone Device.

        Returns:
        :   0 on success, GATT error value on fail.

    int bt\_micp\_mic\_dev\_mute\_disable(void)
    :   Disable the mute functionality on the Microphone Device.

        Can be reenabled by called [bt\_micp\_mic\_dev\_mute](#group__bt__gatt__micp_1ga47f971c9c259e43504d586a55cf22c4e) or [bt\_micp\_mic\_dev\_unmute](#group__bt__gatt__micp_1ga19ec08afa7784b80fce039fe84a4e33c).

        Returns:
        :   0 on success, GATT error value on fail.

    int bt\_micp\_mic\_dev\_mute\_get(void)
    :   Read the mute state on the Microphone Device.

        Returns:
        :   0 on success, GATT error value on fail.

    int bt\_micp\_mic\_ctlr\_included\_get(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, struct [bt\_micp\_included](#c.bt_micp_included) \*included)
    :   Get Microphone Control Profile included services.

        Returns a pointer to a struct that contains information about the Microphone Control Profile included services instances, such as pointers to the Audio Input Control Service instances.

        Requires that  [`CONFIG_BT_MICP_MIC_CTLR_AICS`](../../../../kconfig.md#CONFIG_BT_MICP_MIC_CTLR_AICS "CONFIG_BT_MICP_MIC_CTLR_AICS") is enabled.

        Parameters:
        :   - **mic\_ctlr** – Microphone Controller instance pointer.
            - **included** – **[out]** Pointer to store the result in.

        Returns:
        :   0 if success, errno on failure.

    int bt\_micp\_mic\_ctlr\_conn\_get(const struct bt\_micp\_mic\_ctlr \*mic\_ctlr, struct bt\_conn \*\*conn)
    :   Get the connection pointer of a Microphone Controller instance.

        Get the Bluetooth connection pointer of a Microphone Controller instance.

        Parameters:
        :   - **mic\_ctlr** – Microphone Controller instance pointer.
            - **conn** – Connection pointer.

        Returns:
        :   0 if success, errno on failure.

    struct bt\_micp\_mic\_ctlr \*bt\_micp\_mic\_ctlr\_get\_by\_conn(const struct bt\_conn \*conn)
    :   Get the volume controller from a connection pointer.

        Get the Volume Control Profile Volume Controller pointer from a connection pointer. Only volume controllers that have been initiated via [bt\_micp\_mic\_ctlr\_discover()](#group__bt__gatt__micp_1ga26187007ebf35ba2a5c57a076a3a7212) can be retrieved.

        Parameters:
        :   - **conn** – Connection pointer.

        Return values:
        :   - **Pointer** – to a Microphone Control Profile Microphone Controller instance
            - **NULL** – if `conn` is NULL or if the connection has not done discovery yet

    int bt\_micp\_mic\_ctlr\_discover(struct bt\_conn \*conn, struct bt\_micp\_mic\_ctlr \*\*mic\_ctlr)
    :   Discover Microphone Control Service.

        This will start a GATT discovery and setup handles and subscriptions. This shall be called once before any other actions can be executed for the peer device, and the [bt\_micp\_mic\_ctlr\_cb::discover](#structbt__micp__mic__ctlr__cb_1a2359b88344bf36c3a491b0126dac006b) callback will notify when it is possible to start remote operations.

        Parameters:
        :   - **conn** – The connection to initialize the profile for.
            - **mic\_ctlr** – **[out]** Valid remote instance object on success.

        Returns:
        :   0 on success, GATT error value on fail.

    int bt\_micp\_mic\_ctlr\_unmute(struct bt\_micp\_mic\_ctlr \*mic\_ctlr)
    :   Unmute a remote Microphone Device.

        Parameters:
        :   - **mic\_ctlr** – Microphone Controller instance pointer.

        Returns:
        :   0 on success, GATT error value on fail.

    int bt\_micp\_mic\_ctlr\_mute(struct bt\_micp\_mic\_ctlr \*mic\_ctlr)
    :   Mute a remote Microphone Device.

        Parameters:
        :   - **mic\_ctlr** – Microphone Controller instance pointer.

        Returns:
        :   0 on success, GATT error value on fail.

    int bt\_micp\_mic\_ctlr\_mute\_get(struct bt\_micp\_mic\_ctlr \*mic\_ctlr)
    :   Read the mute state of a remote Microphone Device.

        Parameters:
        :   - **mic\_ctlr** – Microphone Controller instance pointer.

        Returns:
        :   0 on success, GATT error value on fail.

    int bt\_micp\_mic\_ctlr\_cb\_register(struct [bt\_micp\_mic\_ctlr\_cb](#c.bt_micp_mic_ctlr_cb) \*cb)
    :   Registers the callbacks used by Microphone Controller.

        This can only be done as the client.

        Parameters:
        :   - **cb** – The callback structure.

        Returns:
        :   0 if success, errno on failure.

    struct bt\_micp\_mic\_dev\_register\_param
    :   *#include <micp.h>*

        Register parameters structure for Microphone Control Service.

        Public Members

        struct bt\_aics\_register\_param aics\_param[0]
        :   Register parameter structure for Audio Input Control Services.

        struct [bt\_micp\_mic\_dev\_cb](#c.bt_micp_mic_dev_cb) \*cb
        :   Microphone Control Profile callback structure.

    struct bt\_micp\_included
    :   *#include <micp.h>*

        Microphone Control Profile included services.

        Used for to represent the Microphone Control Profile included service instances, for either a Microphone Controller or a Microphone Device. The instance pointers either represent local service instances, or remote service instances.

        Public Members

        uint8\_t aics\_cnt
        :   Number of Audio Input Control Service instances.

        struct bt\_aics \*\*aics
        :   Array of pointers to Audio Input Control Service instances.

    struct bt\_micp\_mic\_dev\_cb
    :   *#include <micp.h>*

        Struct to hold the Microphone Device callbacks.

        These can be registered for usage with [bt\_micp\_mic\_dev\_register()](#group__bt__gatt__micp_1ga5dee6c7a1115bffbea39ba0575f369fc).

        Public Members

        void (\*mute)(uint8\_t mute)
        :   Callback function for Microphone Device mute.

            Called when the value is read with [bt\_micp\_mic\_dev\_mute\_get()](#group__bt__gatt__micp_1ga263bf5cf51e4ef8d7e6986f0d8358da3), or if the value is changed by either the Microphone Device or a Microphone Controller.

            Param mute:
            :   The mute setting of the Microphone Control Service.

    struct bt\_micp\_mic\_ctlr\_cb
    :   *#include <micp.h>*

        Struct to hold the Microphone Controller callbacks.

        These can be registered for usage with [bt\_micp\_mic\_ctlr\_cb\_register()](#group__bt__gatt__micp_1ga148ffcd0672adff9ccfaf35c522897c4).

        Public Members

        void (\*mute)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err, uint8\_t mute)
        :   Callback function for Microphone Control Profile mute.

            Called when the value is read, or if the value is changed by either the Microphone Device or a Microphone Controller.

            Param mic\_ctlr:
            :   Microphone Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error or errno on fail. For notifications, this will always be 0.

            Param mute:
            :   The mute setting of the Microphone Control Service.

        void (\*discover)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err, uint8\_t aics\_count)
        :   Callback function for [bt\_micp\_mic\_ctlr\_discover()](#group__bt__gatt__micp_1ga26187007ebf35ba2a5c57a076a3a7212).

            Param mic\_ctlr:
            :   Microphone Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error or errno on fail.

            Param aics\_count:
            :   Number of Audio Input Control Service instances on peer device.

        void (\*mute\_written)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err)
        :   Callback function for Microphone Control Profile mute/unmute.

            Param mic\_ctlr:
            :   Microphone Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error or errno on fail.

        void (\*unmute\_written)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err)
        :   Callback function for Microphone Control Profile mute/unmute.

            Param mic\_ctlr:
            :   Microphone Controller instance pointer.

            Param err:
            :   Error value. 0 on success, GATT error or errno on fail.
