---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/audio/cap.html
original_path: connectivity/bluetooth/api/audio/cap.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Common Audio Profile

## API Reference

Related code samples

[Bluetooth: Common Audio Profile Acceptor](../../../../samples/bluetooth/cap_acceptor/README.md#bluetooth_cap_acceptor "CAP Acceptor sample that advertises audio availability to CAP Initiators.")
:   CAP Acceptor sample that advertises audio availability to CAP Initiators.

[Bluetooth: Common Audio Profile Initiator](../../../../samples/bluetooth/cap_initiator/README.md#bluetooth_cap_initiator "CAP Initiator sample that connects to CAP Acceptors and setup audio streaming.")
:   CAP Initiator sample that connects to CAP Acceptors and setup audio streaming.

*group* Common Audio Profile (CAP)
:   Common Audio Profile (CAP).

    Common Audio Profile (CAP) provides procedures to start, update, and stop unicast and broadcast Audio Streams on individual or groups of devices using procedures in the Basic Audio Profile (BAP). This profile also provides procedures to control volume and device input on groups of devices using procedures in the Volume Control Profile (VCP) and the Microphone Control Profile (MICP). This profile specification also refers to the Common Audio Service (CAS).

    **Since**
    :   3.2

    **Version**
    :   0.8.0

    Enums

    enum bt\_cap\_set\_type
    :   Type of CAP set.

        *Values:*

        enumerator BT\_CAP\_SET\_TYPE\_AD\_HOC
        :   The set is an ad-hoc set.

        enumerator BT\_CAP\_SET\_TYPE\_CSIP
        :   The set is a CSIP Coordinated Set.

    Functions

    int bt\_cap\_acceptor\_register(const struct [bt\_csip\_set\_member\_register\_param](coordinated_sets.md#c.bt_csip_set_member_register_param "bt_csip_set_member_register_param") \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst)
    :   Register the Common Audio Service.

        This will register and enable the service and make it discoverable by clients. This will also register a Coordinated Set Identification Service instance.

        This shall only be done as a server, and requires  `BT_CAP_ACCEPTOR_SET_MEMBER` . If  `BT_CAP_ACCEPTOR_SET_MEMBER` is not enabled, the Common Audio Service will by statically registered.

        Parameters:
        :   - **param** – **[in]** Coordinated Set Identification Service register parameters.
            - **svc\_inst** – **[out]** Pointer to the registered Coordinated Set Identification Service.

        Returns:
        :   0 if success, errno on failure.

    int bt\_cap\_initiator\_unicast\_discover(struct bt\_conn \*conn)
    :   Discovers audio support on a remote device.

        This will discover the Common Audio Service (CAS) on the remote device, to verify if the remote device supports the Common Audio Profile.

        Parameters:
        :   - **conn** – Connection to a remote server.

        Return values:
        :   - **0** – Success
            - **-EINVAL** – `conn` is NULL
            - **-ENOTCONN** – `conn` is not connected
            - **-ENOMEM** – Could not allocated memory for the request

    void bt\_cap\_stream\_ops\_register(struct [bt\_cap\_stream](#c.bt_cap_stream) \*stream, struct [bt\_bap\_stream\_ops](bap.md#c.bt_bap_stream_ops "bt_bap_stream_ops") \*ops)
    :   Register Audio operations for a Common Audio Profile stream.

        Register Audio operations for a stream.

        Parameters:
        :   - **stream** – Stream object.
            - **ops** – Stream operations structure.

    int bt\_cap\_stream\_send(struct [bt\_cap\_stream](#c.bt_cap_stream) \*stream, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, uint16\_t seq\_num)
    :   Send data to Common Audio Profile stream without timestamp.

        See [bt\_bap\_stream\_send()](bap.md#group__bt__bap_1ga63b69967aa92224a2bd9cf79eb41773e) for more information

        Note

        Support for sending must be supported, determined by  [`CONFIG_BT_AUDIO_TX`](../../../../kconfig.md#CONFIG_BT_AUDIO_TX "CONFIG_BT_AUDIO_TX") .

        Parameters:
        :   - **stream** – Stream object.
            - **buf** – Buffer containing data to be sent.
            - **seq\_num** – Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel.

        Return values:
        :   - **-EINVAL** – if stream object is NULL
            - **Any** – return value from [bt\_bap\_stream\_send()](bap.md#group__bt__bap_1ga63b69967aa92224a2bd9cf79eb41773e)

    int bt\_cap\_stream\_send\_ts(struct [bt\_cap\_stream](#c.bt_cap_stream) \*stream, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, uint16\_t seq\_num, uint32\_t ts)
    :   Send data to Common Audio Profile stream with timestamp.

        See [bt\_bap\_stream\_send()](bap.md#group__bt__bap_1ga63b69967aa92224a2bd9cf79eb41773e) for more information

        Note

        Support for sending must be supported, determined by  [`CONFIG_BT_AUDIO_TX`](../../../../kconfig.md#CONFIG_BT_AUDIO_TX "CONFIG_BT_AUDIO_TX") .

        Parameters:
        :   - **stream** – Stream object.
            - **buf** – Buffer containing data to be sent.
            - **seq\_num** – Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel.
            - **ts** – Timestamp of the SDU in microseconds (us). This value can be used to transmit multiple SDUs in the same SDU interval in a CIG or BIG.

        Return values:
        :   - **-EINVAL** – if stream object is NULL
            - **Any** – return value from [bt\_bap\_stream\_send()](bap.md#group__bt__bap_1ga63b69967aa92224a2bd9cf79eb41773e)

    int bt\_cap\_stream\_get\_tx\_sync(struct [bt\_cap\_stream](#c.bt_cap_stream) \*stream, struct bt\_iso\_tx\_info \*info)
    :   Get ISO transmission timing info for a Common Audio Profile stream.

        See [bt\_bap\_stream\_get\_tx\_sync()](bap.md#group__bt__bap_1ga47eb6219d730d75ddc4f49dceac7e928) for more information

        Note

        Support for sending must be supported, determined by  [`CONFIG_BT_AUDIO_TX`](../../../../kconfig.md#CONFIG_BT_AUDIO_TX "CONFIG_BT_AUDIO_TX") .

        Parameters:
        :   - **stream** – **[in]** Stream object.
            - **info** – **[out]** Transmit info object.

        Return values:
        :   - **-EINVAL** – if stream object is NULL
            - **Any** – return value from [bt\_bap\_stream\_get\_tx\_sync()](bap.md#group__bt__bap_1ga47eb6219d730d75ddc4f49dceac7e928)

    int bt\_cap\_initiator\_register\_cb(const struct [bt\_cap\_initiator\_cb](#c.bt_cap_initiator_cb) \*cb)
    :   Register Common Audio Profile Initiator callbacks.

        Parameters:
        :   - **cb** – The callback structure. Shall remain static.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_unregister\_cb(const struct [bt\_cap\_initiator\_cb](#c.bt_cap_initiator_cb) \*cb)
    :   Unregister Common Audio Profile Initiator callbacks.

        Parameters:
        :   - **cb** – The callback structure that was previously registered.

        Return values:
        :   - **0** – Success
            - **-EINVAL** – `cb` is NULL or `cb` was not registered

    int bt\_cap\_initiator\_unicast\_audio\_start(const struct [bt\_cap\_unicast\_audio\_start\_param](#c.bt_cap_unicast_audio_start_param) \*param)
    :   Setup and start unicast audio streams for a set of devices.

        The result of this operation is that the streams in `param` will be initialized and will be usable for streaming audio data. The `unicast_group` value can be used to update and stop the streams.

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") and  [`CONFIG_BT_BAP_UNICAST_CLIENT`](../../../../kconfig.md#CONFIG_BT_BAP_UNICAST_CLIENT "CONFIG_BT_BAP_UNICAST_CLIENT") must be enabled for this function to be enabled.

        Parameters:
        :   - **param** – Parameters to start the audio streams.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_unicast\_audio\_update(const struct [bt\_cap\_unicast\_audio\_update\_param](#c.bt_cap_unicast_audio_update_param) \*param)
    :   Update unicast audio streams.

        This will update the metadata of one or more streams.

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") and  [`CONFIG_BT_BAP_UNICAST_CLIENT`](../../../../kconfig.md#CONFIG_BT_BAP_UNICAST_CLIENT "CONFIG_BT_BAP_UNICAST_CLIENT") must be enabled for this function to be enabled.

        Parameters:
        :   - **param** – Update parameters.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_unicast\_audio\_stop(const struct [bt\_cap\_unicast\_audio\_stop\_param](#c.bt_cap_unicast_audio_stop_param) \*param)
    :   Stop unicast audio streams.

        This will stop one or more streams.

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") and  [`CONFIG_BT_BAP_UNICAST_CLIENT`](../../../../kconfig.md#CONFIG_BT_BAP_UNICAST_CLIENT "CONFIG_BT_BAP_UNICAST_CLIENT") must be enabled for this function to be enabled.

        Parameters:
        :   - **param** – Stop parameters.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_unicast\_audio\_cancel(void)
    :   Cancel any current Common Audio Profile procedure.

        This will stop the current procedure from continuing and making it possible to run a new Common Audio Profile procedure.

        It is recommended to do this if any existing procedure takes longer time than expected, which could indicate a missing response from the Common Audio Profile Acceptor.

        This does not send any requests to any Common Audio Profile Acceptors involved with the current procedure, and thus notifications from the Common Audio Profile Acceptors may arrive after this has been called. It is thus recommended to either only use this if a procedure has stalled, or wait a short while before starting any new Common Audio Profile procedure after this has been called to avoid getting notifications from the cancelled procedure. The wait time depends on the connection interval, the number of devices in the previous procedure and the behavior of the Common Audio Profile Acceptors.

        The respective callbacks of the procedure will be called as part of this with the connection pointer set to 0 and the err value set to -ECANCELED.

        Return values:
        :   - **0** – on success
            - **-EALREADY** – if no procedure is active

    int bt\_cap\_initiator\_broadcast\_audio\_create(const struct [bt\_cap\_initiator\_broadcast\_create\_param](#c.bt_cap_initiator_broadcast_create_param) \*param, struct bt\_cap\_broadcast\_source \*\*broadcast\_source)
    :   Create a Common Audio Profile broadcast source.

        Create a new audio broadcast source with one or more audio streams.

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") and  [`CONFIG_BT_BAP_BROADCAST_SOURCE`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SOURCE "CONFIG_BT_BAP_BROADCAST_SOURCE") must be enabled for this function to be enabled.

        Parameters:
        :   - **param** – **[in]** Parameters to start the audio streams.
            - **broadcast\_source** – **[out]** Pointer to the broadcast source created.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_broadcast\_audio\_start(struct bt\_cap\_broadcast\_source \*broadcast\_source, struct bt\_le\_ext\_adv \*adv)
    :   Start Common Audio Profile broadcast source.

        The broadcast source will be visible for scanners once this has been called, and the device will advertise audio announcements.

        This will allow the streams in the broadcast source to send audio by calling [bt\_bap\_stream\_send()](bap.md#group__bt__bap_1ga63b69967aa92224a2bd9cf79eb41773e).

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") and  [`CONFIG_BT_BAP_BROADCAST_SOURCE`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SOURCE "CONFIG_BT_BAP_BROADCAST_SOURCE") must be enabled for this function to be enabled.

        Parameters:
        :   - **broadcast\_source** – Pointer to the broadcast source.
            - **adv** – Pointer to an extended advertising set with periodic advertising configured.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_broadcast\_audio\_update(struct bt\_cap\_broadcast\_source \*broadcast\_source, const uint8\_t meta[], size\_t meta\_len)
    :   Update broadcast audio streams for a Common Audio Profile broadcast source.

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") and  [`CONFIG_BT_BAP_BROADCAST_SOURCE`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SOURCE "CONFIG_BT_BAP_BROADCAST_SOURCE") must be enabled for this function to be enabled.

        Parameters:
        :   - **broadcast\_source** – The broadcast source to update.
            - **meta** – The new metadata. The metadata shall contain a list of CCIDs as well as a non-0 context bitfield.
            - **meta\_len** – The length of `meta`.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_broadcast\_audio\_stop(struct bt\_cap\_broadcast\_source \*broadcast\_source)
    :   Stop broadcast audio streams for a Common Audio Profile broadcast source.

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") and  [`CONFIG_BT_BAP_BROADCAST_SOURCE`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SOURCE "CONFIG_BT_BAP_BROADCAST_SOURCE") must be enabled for this function to be enabled.

        Parameters:
        :   - **broadcast\_source** – The broadcast source to stop. The audio streams in this will be stopped and reset.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_broadcast\_audio\_delete(struct bt\_cap\_broadcast\_source \*broadcast\_source)
    :   Delete Common Audio Profile broadcast source.

        This can only be done after the broadcast source has been stopped by calling [bt\_cap\_initiator\_broadcast\_audio\_stop()](#group__bt__cap_1gae4e348f74e3c12e73879082d00cdb17e) and after the [bt\_bap\_stream\_ops.stopped()](bap.md#structbt__bap__stream__ops_1ab50ea295069a2cd1ab6f4353052262f5) callback has been called for all streams in the broadcast source.

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") and  [`CONFIG_BT_BAP_BROADCAST_SOURCE`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SOURCE "CONFIG_BT_BAP_BROADCAST_SOURCE") must be enabled for this function to be enabled.

        Parameters:
        :   - **broadcast\_source** – The broadcast source to delete. The `broadcast_source` will be invalidated.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_broadcast\_get\_id(const struct bt\_cap\_broadcast\_source \*broadcast\_source, uint32\_t \*const broadcast\_id)
    :   Get the broadcast ID of a Common Audio Profile broadcast source.

        This will return the 3-octet broadcast ID that should be advertised in the extended advertising data with [BT\_UUID\_BROADCAST\_AUDIO\_VAL](../uuid.md#group__bt__uuid_1ga0c67f9e1a5fef34fd1fddc539e20119b) as [BT\_DATA\_SVC\_DATA16](../gap.md#group__bt__gap__defines_1ga76990dda919688b369decaf9d3606b32).

        See table 3.14 in the Basic Audio Profile v1.0.1 for the structure.

        Parameters:
        :   - **broadcast\_source** – **[in]** Pointer to the broadcast source.
            - **broadcast\_id** – **[out]** Pointer to the 3-octet broadcast ID.

        Returns:
        :   int 0 if on success, errno on error.

    int bt\_cap\_initiator\_broadcast\_get\_base(struct bt\_cap\_broadcast\_source \*broadcast\_source, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*base\_buf)
    :   Get the Broadcast Audio Stream Endpoint of a Common Audio Profile broadcast source.

        This will encode the BASE of a broadcast source into a buffer, that can be used for advertisement. The encoded BASE will thus be encoded as little-endian. The BASE shall be put into the periodic advertising data (see [bt\_le\_per\_adv\_set\_data()](../gap.md#group__bt__gap_1gafd0e7ccca93a8347a4ca6cca88e77899)).

        See table 3.15 in the Basic Audio Profile v1.0.1 for the structure.

        Parameters:
        :   - **broadcast\_source** – Pointer to the broadcast source.
            - **base\_buf** – Pointer to a buffer where the BASE will be inserted.

        Returns:
        :   int 0 if on success, errno on error.

    int bt\_cap\_initiator\_unicast\_to\_broadcast(const struct [bt\_cap\_unicast\_to\_broadcast\_param](#c.bt_cap_unicast_to_broadcast_param) \*param, struct bt\_cap\_broadcast\_source \*\*source)
    :   Hands over the data streams in a unicast group to a broadcast source.

        The streams in the unicast group will be stopped and the unicast group will be deleted. This can only be done for source streams.

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") ,  [`CONFIG_BT_BAP_UNICAST_CLIENT`](../../../../kconfig.md#CONFIG_BT_BAP_UNICAST_CLIENT "CONFIG_BT_BAP_UNICAST_CLIENT") and  [`CONFIG_BT_BAP_BROADCAST_SOURCE`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SOURCE "CONFIG_BT_BAP_BROADCAST_SOURCE") must be enabled for this function to be enabled.

        Parameters:
        :   - **param** – The parameters for the handover.
            - **source** – The resulting broadcast source.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_initiator\_broadcast\_to\_unicast(const struct [bt\_cap\_broadcast\_to\_unicast\_param](#c.bt_cap_broadcast_to_unicast_param) \*param, struct bt\_bap\_unicast\_group \*\*unicast\_group)
    :   Hands over the data streams in a broadcast source to a unicast group.

        The streams in the broadcast source will be stopped and the broadcast source will be deleted.

        Note

        [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") ,  [`CONFIG_BT_BAP_UNICAST_CLIENT`](../../../../kconfig.md#CONFIG_BT_BAP_UNICAST_CLIENT "CONFIG_BT_BAP_UNICAST_CLIENT") and  [`CONFIG_BT_BAP_BROADCAST_SOURCE`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SOURCE "CONFIG_BT_BAP_BROADCAST_SOURCE") must be enabled for this function to be enabled.

        Parameters:
        :   - **param** – **[in]** The parameters for the handover.
            - **unicast\_group** – **[out]** The resulting broadcast source.

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_commander\_register\_cb(const struct [bt\_cap\_commander\_cb](#c.bt_cap_commander_cb) \*cb)
    :   Register Common Audio Profile Commander callbacks.

        Parameters:
        :   - **cb** – The callback structure. Shall remain static.

        Return values:
        :   - **0** – Success
            - **-EINVAL** – `cb` is NULL
            - **-EALREADY** – Callbacks are already registered

    int bt\_cap\_commander\_unregister\_cb(const struct [bt\_cap\_commander\_cb](#c.bt_cap_commander_cb) \*cb)
    :   Unregister Common Audio Profile Commander callbacks.

        Parameters:
        :   - **cb** – The callback structure that was previously registered.

        Return values:
        :   - **0** – Success
            - **-EINVAL** – `cb` is NULL or `cb` was not registered

    int bt\_cap\_commander\_discover(struct bt\_conn \*conn)
    :   Discovers audio support on a remote device.

        This will discover the Common Audio Service (CAS) on the remote device, to verify if the remote device supports the Common Audio Profile.

        Note

        [`CONFIG_BT_CAP_COMMANDER`](../../../../kconfig.md#CONFIG_BT_CAP_COMMANDER "CONFIG_BT_CAP_COMMANDER") must be enabled for this function. If  [`CONFIG_BT_CAP_INITIATOR`](../../../../kconfig.md#CONFIG_BT_CAP_INITIATOR "CONFIG_BT_CAP_INITIATOR") is also enabled, it does not matter if [bt\_cap\_commander\_discover()](#group__bt__cap_1ga165c67bddcbe220050293a4c73fb6ede) or [bt\_cap\_initiator\_unicast\_discover()](#group__bt__cap_1gab7b273d06abf9a3cb43afdd4e3c30c8d) is used.

        Parameters:
        :   - **conn** – Connection to a remote server.

        Return values:
        :   - **0** – Success
            - **-EINVAL** – `conn` is NULL
            - **-ENOTCONN** – `conn` is not connected
            - **-ENOMEM** – Could not allocated memory for the request
            - **-EBUSY** – Already doing discovery for `conn`

    int bt\_cap\_commander\_cancel(void)
    :   Cancel any current Common Audio Profile commander procedure.

        This will stop the current procedure from continuing and making it possible to run a new Common Audio Profile procedure.

        It is recommended to do this if any existing procedure takes longer time than expected, which could indicate a missing response from the Common Audio Profile Acceptor.

        This does not send any requests to any Common Audio Profile Acceptors involved with the current procedure, and thus notifications from the Common Audio Profile Acceptors may arrive after this has been called. It is thus recommended to either only use this if a procedure has stalled, or wait a short while before starting any new Common Audio Profile procedure after this has been called to avoid getting notifications from the cancelled procedure. The wait time depends on the connection interval, the number of devices in the previous procedure and the behavior of the Common Audio Profile Acceptors.

        The respective callbacks of the procedure will be called as part of this with the connection pointer set to NULL and the err value set to -ECANCELED.

        Return values:
        :   - **0** – on success
            - **-EALREADY** – if no procedure is active

    int bt\_cap\_commander\_broadcast\_reception\_start(const struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](#c.bt_cap_commander_broadcast_reception_start_param) \*param)
    :   Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors.

        Parameters:
        :   - **param** – The parameters to start the broadcast audio

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_commander\_broadcast\_reception\_stop(const struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](#c.bt_cap_commander_broadcast_reception_stop_param) \*param)
    :   Stops the reception of broadcast audio on one or more remote Common Audio Profile Acceptors.

        Parameters:
        :   - **param** – The parameters to stop the broadcast audio

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_commander\_change\_volume(const struct [bt\_cap\_commander\_change\_volume\_param](#c.bt_cap_commander_change_volume_param) \*param)
    :   Change the volume on one or more Common Audio Profile Acceptors.

        Parameters:
        :   - **param** – The parameters for the volume change

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_commander\_change\_volume\_offset(const struct [bt\_cap\_commander\_change\_volume\_offset\_param](#c.bt_cap_commander_change_volume_offset_param) \*param)
    :   Change the volume offset on one or more Common Audio Profile Acceptors.

        Parameters:
        :   - **param** – The parameters for the volume offset change

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_commander\_change\_volume\_mute\_state(const struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](#c.bt_cap_commander_change_volume_mute_state_param) \*param)
    :   Change the volume mute state on one or more Common Audio Profile Acceptors.

        Parameters:
        :   - **param** – The parameters for the volume mute state change

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_commander\_change\_microphone\_mute\_state(const struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](#c.bt_cap_commander_change_microphone_mute_state_param) \*param)
    :   Change the microphone mute state on one or more Common Audio Profile Acceptors.

        Parameters:
        :   - **param** – The parameters for the microphone mute state change

        Returns:
        :   0 on success or negative error value on failure.

    int bt\_cap\_commander\_change\_microphone\_gain\_setting(const struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](#c.bt_cap_commander_change_microphone_gain_setting_param) \*param)
    :   Change the microphone gain setting on one or more Common Audio Profile Acceptors.

        Parameters:
        :   - **param** – The parameters for the microphone gain setting change

        Returns:
        :   0 on success or negative error value on failure.

    struct bt\_cap\_initiator\_cb
    :   *#include <cap.h>*

        Callback structure for CAP procedures.

        Public Members

        void (\*unicast\_discovery\_complete)(struct bt\_conn \*conn, int err, const struct [bt\_csip\_set\_coordinator\_set\_member](coordinated_sets.md#c.bt_csip_set_coordinator_set_member "bt_csip_set_coordinator_set_member") \*member, const struct [bt\_csip\_set\_coordinator\_csis\_inst](coordinated_sets.md#c.bt_csip_set_coordinator_csis_inst "bt_csip_set_coordinator_csis_inst") \*csis\_inst)
        :   Callback for [bt\_cap\_initiator\_unicast\_discover()](#group__bt__cap_1gab7b273d06abf9a3cb43afdd4e3c30c8d).

            Param conn:
            :   The connection pointer supplied to [bt\_cap\_initiator\_unicast\_discover()](#group__bt__cap_1gab7b273d06abf9a3cb43afdd4e3c30c8d).

            Param err:
            :   0 if Common Audio Service was found else -ENODATA.

            Param member:
            :   Pointer to the set member. NULL if err != 0.

            Param csis\_inst:
            :   The Coordinated Set Identification Service if Common Audio Service was found and includes a Coordinated Set Identification Service. NULL on error or if remote device does not include Coordinated Set Identification Service. NULL if err != 0.

        void (\*unicast\_start\_complete)(int err, struct bt\_conn \*conn)
        :   Callback for [bt\_cap\_initiator\_unicast\_audio\_start()](#group__bt__cap_1gae19686be7f8aef1cc92c70fea93e1184).

            Param err:
            :   0 if success, [BT\_GATT\_ERR()](../gatt.md#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](#group__bt__cap_1ga9fbddf102e29e8e969eade40fd60da4f).

            Param conn:
            :   Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](#group__bt__cap_1ga9fbddf102e29e8e969eade40fd60da4f)

        void (\*unicast\_update\_complete)(int err, struct bt\_conn \*conn)
        :   Callback for [bt\_cap\_initiator\_unicast\_audio\_update()](#group__bt__cap_1ga92e4e2c12720ec25c4050cde307cd639).

            Param err:
            :   0 if success, [BT\_GATT\_ERR()](../gatt.md#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](#group__bt__cap_1ga9fbddf102e29e8e969eade40fd60da4f).

            Param conn:
            :   Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](#group__bt__cap_1ga9fbddf102e29e8e969eade40fd60da4f)

        void (\*unicast\_stop\_complete)(int err, struct bt\_conn \*conn)
        :   Callback for [bt\_cap\_initiator\_unicast\_audio\_stop()](#group__bt__cap_1gafdf6f1656249ab3ae6296272dc36b66f).

            Param err:
            :   0 if success, [BT\_GATT\_ERR()](../gatt.md#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](#group__bt__cap_1ga9fbddf102e29e8e969eade40fd60da4f).

            Param conn:
            :   Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](#group__bt__cap_1ga9fbddf102e29e8e969eade40fd60da4f)

    union bt\_cap\_set\_member
    :   *#include <cap.h>*

        Represents a Common Audio Set member that are either in a Coordinated or ad-hoc set.

        Public Members

        struct bt\_conn \*member
        :   Connection pointer if the type is BT\_CAP\_SET\_TYPE\_AD\_HOC.

        struct [bt\_csip\_set\_coordinator\_csis\_inst](coordinated_sets.md#c.bt_csip_set_coordinator_csis_inst "bt_csip_set_coordinator_csis_inst") \*csip
        :   CSIP Coordinated Set struct used if type is BT\_CAP\_SET\_TYPE\_CSIP.

    struct bt\_cap\_stream
    :   *#include <cap.h>*

        Common Audio Profile stream structure.

        Streams represents a Basic Audio Profile (BAP) stream and operation callbacks. See [bt\_bap\_stream](bap.md#structbt__bap__stream) for additional information.

        Public Members

        struct [bt\_bap\_stream](bap.md#c.bt_bap_stream "bt_bap_stream") bap\_stream
        :   The underlying BAP audio stream.

        struct [bt\_bap\_stream\_ops](bap.md#c.bt_bap_stream_ops "bt_bap_stream_ops") \*ops
        :   Audio stream operations.

    struct bt\_cap\_unicast\_audio\_start\_stream\_param
    :   *#include <cap.h>*

        Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_start()](#group__bt__cap_1gae19686be7f8aef1cc92c70fea93e1184) function.

        Public Members

        union [bt\_cap\_set\_member](#c.bt_cap_set_member) member
        :   Coordinated or ad-hoc set member.

        struct [bt\_cap\_stream](#c.bt_cap_stream) \*stream
        :   Stream for the `member`.

        struct bt\_bap\_ep \*ep
        :   Endpoint reference for the `stream`.

        struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg
        :   Codec configuration.

            The `codec_cfg.meta` shall include a list of CCIDs ([BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](audio.md#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)) as well as a non-0 stream context ([BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](audio.md#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)) bitfield.

            This value is assigned to the `stream`, and shall remain valid while the stream is non-idle.

    struct bt\_cap\_unicast\_audio\_start\_param
    :   *#include <cap.h>*

        Parameters for the [bt\_cap\_initiator\_unicast\_audio\_start()](#group__bt__cap_1gae19686be7f8aef1cc92c70fea93e1184) function.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        size\_t count
        :   The number of parameters in `stream_params`.

        struct [bt\_cap\_unicast\_audio\_start\_stream\_param](#c.bt_cap_unicast_audio_start_stream_param) \*stream\_params
        :   Array of stream parameters.

    struct bt\_cap\_unicast\_audio\_update\_stream\_param
    :   *#include <cap.h>*

        Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](#group__bt__cap_1ga92e4e2c12720ec25c4050cde307cd639) function.

        Public Members

        struct [bt\_cap\_stream](#c.bt_cap_stream) \*stream
        :   Stream to update.

        size\_t meta\_len
        :   The length of `meta`.

        uint8\_t \*meta
        :   The new metadata.

            The metadata shall contain a list of CCIDs as well as a non-0 context bitfield.

    struct bt\_cap\_unicast\_audio\_update\_param
    :   *#include <cap.h>*

        Parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](#group__bt__cap_1ga92e4e2c12720ec25c4050cde307cd639) function.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        size\_t count
        :   The number of parameters in `stream_params`.

        struct [bt\_cap\_unicast\_audio\_update\_stream\_param](#c.bt_cap_unicast_audio_update_stream_param) \*stream\_params
        :   Array of stream parameters.

    struct bt\_cap\_unicast\_audio\_stop\_param
    :   *#include <cap.h>*

        Parameters for the [bt\_cap\_initiator\_unicast\_audio\_stop()](#group__bt__cap_1gafdf6f1656249ab3ae6296272dc36b66f) function.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        size\_t count
        :   The number of streams in `streams`.

        struct [bt\_cap\_stream](#c.bt_cap_stream) \*\*streams
        :   Array of streams to stop.

    struct bt\_cap\_initiator\_broadcast\_stream\_param
    :   *#include <cap.h>*

        Parameters part of `[bt_cap_initiator_broadcast_subgroup_param](#structbt__cap__initiator__broadcast__subgroup__param)` for [bt\_cap\_initiator\_broadcast\_audio\_create()](#group__bt__cap_1ga78697225c6b1291dfc016e20fd605fc4).

        Public Members

        struct [bt\_cap\_stream](#c.bt_cap_stream) \*stream
        :   Audio stream.

        size\_t data\_len
        :   The length of the p data array.

            The BIS specific data may be omitted and this set to 0.

        uint8\_t \*data
        :   BIS Codec Specific Configuration.

    struct bt\_cap\_initiator\_broadcast\_subgroup\_param
    :   *#include <cap.h>*

        Parameters part of `[bt_cap_initiator_broadcast_create_param](#structbt__cap__initiator__broadcast__create__param)` for [bt\_cap\_initiator\_broadcast\_audio\_create()](#group__bt__cap_1ga78697225c6b1291dfc016e20fd605fc4).

        Public Members

        size\_t stream\_count
        :   The number of parameters in `stream_params`.

        struct [bt\_cap\_initiator\_broadcast\_stream\_param](#c.bt_cap_initiator_broadcast_stream_param) \*stream\_params
        :   Array of stream parameters.

        struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg
        :   Subgroup Codec configuration.

    struct bt\_cap\_initiator\_broadcast\_create\_param
    :   *#include <cap.h>*

        Parameters for \* [bt\_cap\_initiator\_broadcast\_audio\_create()](#group__bt__cap_1ga78697225c6b1291dfc016e20fd605fc4).

        Public Members

        size\_t subgroup\_count
        :   The number of parameters in `subgroup_params`.

        struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](#c.bt_cap_initiator_broadcast_subgroup_param) \*subgroup\_params
        :   Array of stream parameters.

        struct [bt\_audio\_codec\_qos](audio.md#c.bt_audio_codec_qos "bt_audio_codec_qos") \*qos
        :   Quality of Service configuration.

        uint8\_t packing
        :   Broadcast Source packing mode.

            BT\_ISO\_PACKING\_SEQUENTIAL or BT\_ISO\_PACKING\_INTERLEAVED.

            Note

            This is a recommendation to the controller, which the controller may ignore.

        bool encryption
        :   Whether or not to encrypt the streams.

        uint8\_t broadcast\_code[[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](audio.md#c.BT_AUDIO_BROADCAST_CODE_SIZE "BT_AUDIO_BROADCAST_CODE_SIZE")]
        :   16-octet broadcast code.

            Only valid if `encrypt` is true.

            If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

            Example: The string “Broadcast Code” shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

        uint8\_t irc
        :   Immediate Repetition Count.

            The number of times the scheduled payloads are transmitted in a given event.

            Value range from BT\_ISO\_IRC\_MIN to BT\_ISO\_IRC\_MAX.

        uint8\_t pto
        :   Pre-transmission offset.

            Offset used for pre-transmissions.

            Value range from BT\_ISO\_PTO\_MIN to BT\_ISO\_PTO\_MAX.

        uint16\_t iso\_interval
        :   ISO interval.

            Time between consecutive BIS anchor points.

            Value range from BT\_ISO\_ISO\_INTERVAL\_MIN to BT\_ISO\_ISO\_INTERVAL\_MAX.

    struct bt\_cap\_unicast\_to\_broadcast\_param
    :   *#include <cap.h>*

        Parameters for [bt\_cap\_initiator\_unicast\_to\_broadcast()](#group__bt__cap_1ga6ab41d799396175c8c14e1d8222f3558).

        Public Members

        struct bt\_bap\_unicast\_group \*unicast\_group
        :   The source unicast group with the streams.

        bool encrypt
        :   Whether or not to encrypt the streams.

            If set to true, then the broadcast code in `broadcast_code` will be used to encrypt the streams.

        uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE]
        :   16-octet broadcast code.

            Only valid if `encrypt` is true.

            If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

            Example: The string “Broadcast Code” shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

    struct bt\_cap\_broadcast\_to\_unicast\_param
    :   *#include <cap.h>*

        Parameters for [bt\_cap\_initiator\_broadcast\_to\_unicast()](#group__bt__cap_1ga372e555208da722f0a89470d3b7e3e8b).

        Public Members

        struct bt\_cap\_broadcast\_source \*broadcast\_source
        :   The source broadcast source with the streams.

            The broadcast source will be stopped and deleted.

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        size\_t count
        :   The number of set members in `members`.

            This value shall match the number of streams in the `broadcast_source`.

        union [bt\_cap\_set\_member](#c.bt_cap_set_member) \*\*members
        :   Coordinated or ad-hoc set members.

    struct bt\_cap\_commander\_cb
    :   *#include <cap.h>*

        Callback structure for CAP procedures.

        Public Members

        void (\*discovery\_complete)(struct bt\_conn \*conn, int err, const struct [bt\_csip\_set\_coordinator\_set\_member](coordinated_sets.md#c.bt_csip_set_coordinator_set_member "bt_csip_set_coordinator_set_member") \*member, const struct [bt\_csip\_set\_coordinator\_csis\_inst](coordinated_sets.md#c.bt_csip_set_coordinator_csis_inst "bt_csip_set_coordinator_csis_inst") \*csis\_inst)
        :   Callback for [bt\_cap\_initiator\_unicast\_discover()](#group__bt__cap_1gab7b273d06abf9a3cb43afdd4e3c30c8d).

            Param conn:
            :   The connection pointer supplied to [bt\_cap\_initiator\_unicast\_discover()](#group__bt__cap_1gab7b273d06abf9a3cb43afdd4e3c30c8d).

            Param err:
            :   0 if Common Audio Service was found else -ENODATA.

            Param member:
            :   Pointer to the set member. NULL if err != 0.

            Param csis\_inst:
            :   The Coordinated Set Identification Service if Common Audio Service was found and includes a Coordinated Set Identification Service. NULL on error or if remote device does not include Coordinated Set Identification Service. NULL if err != 0.

        void (\*volume\_changed)(struct bt\_conn \*conn, int err)
        :   Callback for [bt\_cap\_commander\_change\_volume()](#group__bt__cap_1gaff96953334eab1a38b30720b41c0d1a6).

            Param conn:
            :   Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c)

            Param err:
            :   0 on success, [BT\_GATT\_ERR()](../gatt.md#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c).

        void (\*volume\_mute\_changed)(struct bt\_conn \*conn, int err)
        :   Callback for [bt\_cap\_commander\_change\_volume\_mute\_state()](#group__bt__cap_1gac5f94baa82fa6deade6f83346a56b5e4).

            Param conn:
            :   Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c)

            Param err:
            :   0 on success, [BT\_GATT\_ERR()](../gatt.md#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c).

        void (\*volume\_offset\_changed)(struct bt\_conn \*conn, int err)
        :   Callback for [bt\_cap\_commander\_change\_volume\_offset()](#group__bt__cap_1gae2cd451b387659b0a2021a9023d74dfa).

            Param conn:
            :   Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c)

            Param err:
            :   0 on success, [BT\_GATT\_ERR()](../gatt.md#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c).

        void (\*microphone\_mute\_changed)(struct bt\_conn \*conn, int err)
        :   Callback for [bt\_cap\_commander\_change\_microphone\_mute\_state()](#group__bt__cap_1ga19cc7ed5992a528a7795b76e7add6d54).

            Param conn:
            :   Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c)

            Param err:
            :   0 on success, [BT\_GATT\_ERR()](../gatt.md#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c).

        void (\*microphone\_gain\_changed)(struct bt\_conn \*conn, int err)
        :   Callback for [bt\_cap\_commander\_change\_microphone\_gain\_setting()](#group__bt__cap_1ga958cd5925699624d23479ad2ace6b55b).

            Param conn:
            :   Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c)

            Param err:
            :   0 on success, [BT\_GATT\_ERR()](../gatt.md#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c).

        void (\*broadcast\_reception\_start)(struct bt\_conn \*conn, int err)
        :   Callback for [bt\_cap\_commander\_broadcast\_reception\_start()](#group__bt__cap_1ga25be83bb53c8e2ab76f311eaf4f615b9).

            Param conn:
            :   Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c)

            Param err:
            :   0 on success, [BT\_GATT\_ERR()](../gatt.md#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](#group__bt__cap_1ga7abf029533fed391930257605f3c752c).

    struct bt\_cap\_commander\_broadcast\_reception\_start\_member\_param
    :   *#include <cap.h>*

        Parameters part of [bt\_cap\_commander\_broadcast\_reception\_start\_param](#structbt__cap__commander__broadcast__reception__start__param) for [bt\_cap\_commander\_broadcast\_reception\_start()](#group__bt__cap_1ga25be83bb53c8e2ab76f311eaf4f615b9).

        Public Members

        union [bt\_cap\_set\_member](#c.bt_cap_set_member) member
        :   Coordinated or ad-hoc set member.

        [bt\_addr\_le\_t](../gap.md#c.bt_addr_le_t "bt_addr_le_t") addr
        :   Address of the advertiser.

        uint8\_t adv\_sid
        :   SID of the advertising set.

        uint16\_t pa\_interval
        :   Periodic advertising interval in milliseconds.

            BT\_BAP\_PA\_INTERVAL\_UNKNOWN if unknown.

        uint32\_t broadcast\_id
        :   24-bit broadcast ID

        struct [bt\_bap\_bass\_subgroup](bap.md#c.bt_bap_bass_subgroup "bt_bap_bass_subgroup") subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]
        :   Pointer to array of subgroups.

            At least one bit in one of the subgroups bis\_sync parameters shall be set.

        size\_t num\_subgroups
        :   Number of subgroups.

    struct bt\_cap\_commander\_broadcast\_reception\_start\_param
    :   *#include <cap.h>*

        Parameters for starting broadcast reception.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        struct [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](#c.bt_cap_commander_broadcast_reception_start_member_param) \*param
        :   The set of devices for this procedure.

        size\_t count
        :   The number of parameters in `param`.

    struct bt\_cap\_commander\_broadcast\_reception\_stop\_param
    :   *#include <cap.h>*

        Parameters for stopping broadcast reception.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        union [bt\_cap\_set\_member](#c.bt_cap_set_member) \*members
        :   Coordinated or ad-hoc set member.

        size\_t count
        :   The number of members in `members`.

    struct bt\_cap\_commander\_change\_volume\_param
    :   *#include <cap.h>*

        Parameters for changing absolute volume.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        union [bt\_cap\_set\_member](#c.bt_cap_set_member) \*members
        :   Coordinated or ad-hoc set member.

        size\_t count
        :   The number of members in `members`.

        uint8\_t volume
        :   The absolute volume to set.

    struct bt\_cap\_commander\_change\_volume\_offset\_member\_param
    :   *#include <cap.h>*

        Parameters part of [bt\_cap\_commander\_change\_volume\_offset\_param](#structbt__cap__commander__change__volume__offset__param) for [bt\_cap\_commander\_change\_volume\_offset()](#group__bt__cap_1gae2cd451b387659b0a2021a9023d74dfa).

        Public Members

        union [bt\_cap\_set\_member](#c.bt_cap_set_member) member
        :   Coordinated or ad-hoc set member.

        int16\_t offset
        :   The offset to set.

            Value shall be between BT\_VOCS\_MIN\_OFFSET and BT\_VOCS\_MAX\_OFFSET

    struct bt\_cap\_commander\_change\_volume\_offset\_param
    :   *#include <cap.h>*

        Parameters for changing volume offset.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        struct [bt\_cap\_commander\_change\_volume\_offset\_member\_param](#c.bt_cap_commander_change_volume_offset_member_param) \*param
        :   The set of devices for this procedure.

        size\_t count
        :   The number of parameters in `param`.

    struct bt\_cap\_commander\_change\_volume\_mute\_state\_param
    :   *#include <cap.h>*

        Parameters for changing volume mute state.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        union [bt\_cap\_set\_member](#c.bt_cap_set_member) \*members
        :   Coordinated or ad-hoc set member.

        size\_t count
        :   The number of members in `members`.

        bool mute
        :   The volume mute state to set.

            true to mute, and false to unmute

    struct bt\_cap\_commander\_change\_microphone\_mute\_state\_param
    :   *#include <cap.h>*

        Parameters for changing microphone mute state.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        union [bt\_cap\_set\_member](#c.bt_cap_set_member) \*members
        :   Coordinated or ad-hoc set member.

        size\_t count
        :   The number of members in `members`.

        bool mute
        :   The microphone mute state to set.

            true to mute, and false to unmute

    struct bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param
    :   *#include <cap.h>*

        Parameters part of [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](#structbt__cap__commander__change__microphone__gain__setting__param) for [bt\_cap\_commander\_change\_microphone\_gain\_setting()](#group__bt__cap_1ga958cd5925699624d23479ad2ace6b55b).

        Public Members

        union [bt\_cap\_set\_member](#c.bt_cap_set_member) member
        :   Coordinated or ad-hoc set member.

        int8\_t gain
        :   The microphone gain setting to set.

    struct bt\_cap\_commander\_change\_microphone\_gain\_setting\_param
    :   *#include <cap.h>*

        Parameters for changing microphone mute state.

        Public Members

        enum [bt\_cap\_set\_type](#c.bt_cap_set_type) type
        :   The type of the set.

        struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](#c.bt_cap_commander_change_microphone_gain_setting_member_param) \*param
        :   The set of devices for this procedure.

        size\_t count
        :   The number of parameters in `param`.
