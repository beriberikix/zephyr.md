---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/audio/bap.html
original_path: connectivity/bluetooth/api/audio/bap.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Basic Audio Profile

## API Reference

Related code samples

[Bluetooth: Broadcast Audio Assistant](../../../../samples/bluetooth/bap_broadcast_assistant/README.md#bluetooth_bap_broadcast_assistant "Use LE Audio Broadcast Assistant functionality")
:   Use LE Audio Broadcast Assistant functionality

[Bluetooth: Common Audio Profile Acceptor](../../../../samples/bluetooth/cap_acceptor/README.md#bluetooth_cap_acceptor "CAP Acceptor sample that advertises audio availability to CAP Initiators.")
:   CAP Acceptor sample that advertises audio availability to CAP Initiators.

[Bluetooth: Common Audio Profile Initiator](../../../../samples/bluetooth/cap_initiator/README.md#bluetooth_cap_initiator "CAP Initiator sample that connects to CAP Acceptors and setup audio streaming.")
:   CAP Initiator sample that connects to CAP Acceptors and setup audio streaming.

*group* Bluetooth Basic Audio Profile
:   Bluetooth Basic Audio Profile (BAP).

    The Basic Audio Profile (BAP) allows for both unicast and broadcast Audio Stream control.

    **Since**
    :   3.0

    **Version**
    :   0.8.0

    Defines

    BT\_BAP\_PA\_INTERVAL\_UNKNOWN
    :   Value indicating that the periodic advertising interval is unknown.

    BT\_BAP\_BIS\_SYNC\_NO\_PREF
    :   Broadcast Assistant no BIS sync preference.

        Value indicating that the Broadcast Assistant has no preference to which BIS the Scan Delegator syncs to

    BT\_BAP\_ASCS\_RSP(c, r)
    :   Macro used to initialise the object storing values of ASE Control Point notification.

        Parameters:
        :   - **c** – Response Code field
            - **r** – Reason field - [bt\_bap\_ascs\_reason](#group__bt__bap_1ga9ca1630544a336b15af8a8e8934c5a45) or [bt\_audio\_metadata\_type](audio.md#group__bt__audio_1gab53d0dd62bceff97cf8eed7d8cf80354) (see notes in [bt\_bap\_ascs\_rsp](#structbt__bap__ascs__rsp)).

    Typedefs

    typedef bool (\*bt\_bap\_scan\_delegator\_state\_func\_t)(const struct [bt\_bap\_scan\_delegator\_recv\_state](#c.bt_bap_scan_delegator_recv_state) \*recv\_state, void \*user\_data)
    :   Callback function for Scan Delegator receive state search functions.

        Param recv\_state:
        :   The receive state.

        Param user\_data:
        :   User data.

        Retval true:
        :   to stop iterating. If this is used in the context of [bt\_bap\_scan\_delegator\_find\_state()](#group__bt__bap_1gabec9fd0a2966e1811fd4770855050510), the recv\_state will be returned by [bt\_bap\_scan\_delegator\_find\_state()](#group__bt__bap_1gabec9fd0a2966e1811fd4770855050510)

        Retval false:
        :   to continue iterating

    typedef void (\*bt\_bap\_broadcast\_assistant\_write\_cb)(struct bt\_conn \*conn, int err)
    :   Callback function for writes.

        Param conn:
        :   The connection to the peer device.

        Param err:
        :   Error value. 0 on success, GATT error on fail.

    Enums

    enum bt\_bap\_pa\_state
    :   Periodic advertising state reported by the Scan Delegator.

        *Values:*

        enumerator BT\_BAP\_PA\_STATE\_NOT\_SYNCED = 0x00
        :   The periodic advertising has not been synchronized.

        enumerator BT\_BAP\_PA\_STATE\_INFO\_REQ = 0x01
        :   Waiting for SyncInfo from Broadcast Assistant.

        enumerator BT\_BAP\_PA\_STATE\_SYNCED = 0x02
        :   Synchronized to periodic advertising.

        enumerator BT\_BAP\_PA\_STATE\_FAILED = 0x03
        :   Failed to synchronized to periodic advertising.

        enumerator BT\_BAP\_PA\_STATE\_NO\_PAST = 0x04
        :   No periodic advertising sync transfer receiver from Broadcast Assistant.

    enum bt\_bap\_big\_enc\_state
    :   Broadcast Isochronous Group encryption state reported by the Scan Delegator.

        *Values:*

        enumerator BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC = 0x00
        :   The Broadcast Isochronous Group not encrypted.

        enumerator BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ = 0x01
        :   The Broadcast Isochronous Group broadcast code requested.

        enumerator BT\_BAP\_BIG\_ENC\_STATE\_DEC = 0x02
        :   The Broadcast Isochronous Group decrypted.

        enumerator BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE = 0x03
        :   The Broadcast Isochronous Group bad broadcast code.

    enum bt\_bap\_bass\_att\_err
    :   Broadcast Audio Scan Service (BASS) specific ATT error codes.

        *Values:*

        enumerator BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED = 0x80
        :   Opcode not supported.

        enumerator BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID = 0x81
        :   Invalid source ID supplied.

    enum bt\_bap\_ep\_state
    :   Endpoint states.

        *Values:*

        enumerator BT\_BAP\_EP\_STATE\_IDLE = 0x00
        :   Audio Stream Endpoint Idle state.

        enumerator BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED = 0x01
        :   Audio Stream Endpoint Codec Configured state.

        enumerator BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED = 0x02
        :   Audio Stream Endpoint QoS Configured state.

        enumerator BT\_BAP\_EP\_STATE\_ENABLING = 0x03
        :   Audio Stream Endpoint Enabling state.

        enumerator BT\_BAP\_EP\_STATE\_STREAMING = 0x04
        :   Audio Stream Endpoint Streaming state.

        enumerator BT\_BAP\_EP\_STATE\_DISABLING = 0x05
        :   Audio Stream Endpoint Disabling state.

        enumerator BT\_BAP\_EP\_STATE\_RELEASING = 0x06
        :   Audio Stream Endpoint Streaming state.

    enum bt\_bap\_ascs\_rsp\_code
    :   Response Status Code.

        These are sent by the server to the client when a stream operation is requested.

        *Values:*

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS = 0x00
        :   Server completed operation successfully.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED = 0x01
        :   Server did not support operation by client.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH = 0x02
        :   Server rejected due to invalid operation length.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE = 0x03
        :   Invalid ASE ID.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE = 0x04
        :   Invalid ASE state.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR = 0x05
        :   Invalid operation for direction.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED = 0x06
        :   Capabilities not supported by server.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED = 0x07
        :   Configuration parameters not supported by server.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED = 0x08
        :   Configuration parameters rejected by server.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID = 0x09
        :   Invalid Configuration parameters.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED = 0x0a
        :   Unsupported metadata.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED = 0x0b
        :   Metadata rejected by server.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID = 0x0c
        :   Invalid metadata.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM = 0x0d
        :   Server has insufficient resources.

        enumerator BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED = 0x0e
        :   Unspecified error.

    enum bt\_bap\_ascs\_reason
    :   Response Reasons.

        These are used if the [bt\_bap\_ascs\_rsp\_code](#group__bt__bap_1ga9f7efa749c75edd32dc50503397ab9d1) value is [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62), [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21) or [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219).

        *Values:*

        enumerator BT\_BAP\_ASCS\_REASON\_NONE = 0x00
        :   No reason.

        enumerator BT\_BAP\_ASCS\_REASON\_CODEC = 0x01
        :   Codec ID.

        enumerator BT\_BAP\_ASCS\_REASON\_CODEC\_DATA = 0x02
        :   Codec configuration.

        enumerator BT\_BAP\_ASCS\_REASON\_INTERVAL = 0x03
        :   SDU interval.

        enumerator BT\_BAP\_ASCS\_REASON\_FRAMING = 0x04
        :   Framing.

        enumerator BT\_BAP\_ASCS\_REASON\_PHY = 0x05
        :   PHY.

        enumerator BT\_BAP\_ASCS\_REASON\_SDU = 0x06
        :   Maximum SDU size.

        enumerator BT\_BAP\_ASCS\_REASON\_RTN = 0x07
        :   RTN.

        enumerator BT\_BAP\_ASCS\_REASON\_LATENCY = 0x08
        :   Max transport latency.

        enumerator BT\_BAP\_ASCS\_REASON\_PD = 0x09
        :   Presendation delay.

        enumerator BT\_BAP\_ASCS\_REASON\_CIS = 0x0a
        :   Invalid CIS mapping.

    Functions

    int bt\_bap\_ep\_get\_info(const struct bt\_bap\_ep \*ep, struct [bt\_bap\_ep\_info](#c.bt_bap_ep_info) \*info)
    :   Return structure holding information of audio stream endpoint.

        Parameters:
        :   - **ep** – The audio stream endpoint object.
            - **info** – The structure object to be filled with the info.

        Return values:
        :   - **0** – in case of success
            - **-EINVAL** – if `ep` or `info` are NULL

    void bt\_bap\_stream\_cb\_register(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct [bt\_bap\_stream\_ops](#c.bt_bap_stream_ops) \*ops)
    :   Register Audio callbacks for a stream.

        Register Audio callbacks for a stream.

        Parameters:
        :   - **stream** – Stream object.
            - **ops** – Stream operations structure.

    int bt\_bap\_stream\_config(struct bt\_conn \*conn, struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct bt\_bap\_ep \*ep, struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg)
    :   Configure Audio Stream.

        This procedure is used by a client to configure a new stream using the remote endpoint, local capability and codec configuration.

        Parameters:
        :   - **conn** – Connection object
            - **stream** – Stream object being configured
            - **ep** – Remote Audio Endpoint being configured
            - **codec\_cfg** – Codec configuration

        Returns:
        :   Allocated Audio Stream object or NULL in case of error.

    int bt\_bap\_stream\_reconfig(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg)
    :   Reconfigure Audio Stream.

        This procedure is used by a unicast client or unicast server to reconfigure a stream to use a different local codec configuration.

        This can only be done for unicast streams.

        Parameters:
        :   - **stream** – Stream object being reconfigured
            - **codec\_cfg** – Codec configuration

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_stream\_qos(struct bt\_conn \*conn, struct bt\_bap\_unicast\_group \*group)
    :   Configure Audio Stream QoS.

        This procedure is used by a client to configure the Quality of Service of streams in a unicast group. All streams in the group for the specified `conn` will have the Quality of Service configured. This shall only be used to configure unicast streams.

        Parameters:
        :   - **conn** – Connection object
            - **group** – Unicast group object

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_stream\_enable(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, const uint8\_t meta[], size\_t meta\_len)
    :   Enable Audio Stream.

        This procedure is used by a client to enable a stream.

        This shall only be called for unicast streams, as broadcast streams will always be enabled once created.

        Parameters:
        :   - **stream** – Stream object
            - **meta** – Metadata
            - **meta\_len** – Metadata length

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_stream\_metadata(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, const uint8\_t meta[], size\_t meta\_len)
    :   Change Audio Stream Metadata.

        This procedure is used by a unicast client or unicast server to change the metadata of a stream.

        Parameters:
        :   - **stream** – Stream object
            - **meta** – Metadata
            - **meta\_len** – Metadata length

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_stream\_disable(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
    :   Disable Audio Stream.

        This procedure is used by a unicast client or unicast server to disable a stream.

        This shall only be called for unicast streams, as broadcast streams will always be enabled once created.

        Parameters:
        :   - **stream** – Stream object

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_stream\_connect(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
    :   Connect unicast audio stream.

        This procedure is used by a unicast client to connect the connected isochronous stream (CIS) associated with the audio stream. If two audio streams share a CIS, then this only needs to be done once for those streams. This can only be done for streams in the QoS configured or enabled states.

        The [bt\_bap\_stream\_ops.connected()](#structbt__bap__stream__ops_1a533d5ea96aa67b9b74b19c55afd43df1) callback will be called on the streams once this has finished.

        This shall only be called for unicast streams, and only as the unicast client ( [`CONFIG_BT_BAP_UNICAST_CLIENT`](../../../../kconfig.md#CONFIG_BT_BAP_UNICAST_CLIENT "CONFIG_BT_BAP_UNICAST_CLIENT") ).

        Parameters:
        :   - **stream** – Stream object

        Return values:
        :   - **0** – in case of success
            - **-EINVAL** – if the stream, endpoint, ISO channel or connection is NULL
            - **-EBADMSG** – if the stream or ISO channel is in an invalid state for connection
            - **-EOPNOTSUPP** – if the role of the stream is not BT\_HCI\_ROLE\_CENTRAL
            - **-EALREADY** – if the ISO channel is already connecting or connected
            - **-EBUSY** – if another ISO channel is connecting
            - **-ENOEXEC** – if otherwise rejected by the ISO layer

    int bt\_bap\_stream\_start(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
    :   Start Audio Stream.

        This procedure is used by a unicast client or unicast server to make a stream start streaming.

        For the unicast client, this will send the receiver start ready command to the unicast server for [BT\_AUDIO\_DIR\_SOURCE](audio.md#group__bt__audio_1gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) ASEs. The CIS is required to be connected first by [bt\_bap\_stream\_connect()](#group__bt__bap_1gaa75f2cd2c36fdaef04a62c95bec6e2e3) before the command can be sent.

        For the unicast server, this will execute the receiver start ready command on the unicast server for [BT\_AUDIO\_DIR\_SINK](audio.md#group__bt__audio_1gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8) ASEs. If the CIS is not connected yet, the stream will go into the streaming state as soon as the CIS is connected.

        This shall only be called for unicast streams.

        Broadcast sinks will always be started once synchronized, and broadcast source streams shall be started with [bt\_bap\_broadcast\_source\_start()](#group__bt__bap__broadcast__source_1gac4640f5207599d51c1a63ff47f3c1d5a).

        Parameters:
        :   - **stream** – Stream object

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_stream\_stop(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
    :   Stop Audio Stream.

        This procedure is used by a client to make a stream stop streaming.

        This shall only be called for unicast streams. Broadcast sinks cannot be stopped. Broadcast sources shall be stopped with [bt\_bap\_broadcast\_source\_stop()](#group__bt__bap__broadcast__source_1ga36a885581eec5cab8b3f652db19b9aba).

        Parameters:
        :   - **stream** – Stream object

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_stream\_release(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
    :   Release Audio Stream.

        This procedure is used by a unicast client or unicast server to release a unicast stream.

        Broadcast sink streams cannot be released, but can be deleted by [bt\_bap\_broadcast\_sink\_delete()](#group__bt__bap__broadcast__sink_1ga8b9d6cb409a3671654e053475ada3fda). Broadcast source streams cannot be released, but can be deleted by [bt\_bap\_broadcast\_source\_delete()](#group__bt__bap__broadcast__source_1ga12e0a4856115a8eb297fe2d1fc130155).

        Parameters:
        :   - **stream** – Stream object

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_stream\_send(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, uint16\_t seq\_num)
    :   Send data to Audio stream without timestamp.

        Send data from buffer to the stream.

        Note

        Support for sending must be supported, determined by  [`CONFIG_BT_AUDIO_TX`](../../../../kconfig.md#CONFIG_BT_AUDIO_TX "CONFIG_BT_AUDIO_TX") .

        Parameters:
        :   - **stream** – Stream object.
            - **buf** – Buffer containing data to be sent.
            - **seq\_num** – Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel.

        Returns:
        :   Bytes sent in case of success or negative value in case of error.

    int bt\_bap\_stream\_send\_ts(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, uint16\_t seq\_num, uint32\_t ts)
    :   Send data to Audio stream with timestamp.

        Send data from buffer to the stream.

        Note

        Support for sending must be supported, determined by  [`CONFIG_BT_AUDIO_TX`](../../../../kconfig.md#CONFIG_BT_AUDIO_TX "CONFIG_BT_AUDIO_TX") .

        Parameters:
        :   - **stream** – Stream object.
            - **buf** – Buffer containing data to be sent.
            - **seq\_num** – Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel.
            - **ts** – Timestamp of the SDU in microseconds (us). This value can be used to transmit multiple SDUs in the same SDU interval in a CIG or BIG.

        Returns:
        :   Bytes sent in case of success or negative value in case of error.

    int bt\_bap\_stream\_get\_tx\_sync(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct bt\_iso\_tx\_info \*info)
    :   Get ISO transmission timing info for a Basic Audio Profile stream.

        Reads timing information for transmitted ISO packet on an ISO channel. The HCI\_LE\_Read\_ISO\_TX\_Sync HCI command is used to retrieve this information from the controller.

        Note

        An SDU must have already been successfully transmitted on the ISO channel for this function to return successfully. Support for sending must be supported, determined by  [`CONFIG_BT_AUDIO_TX`](../../../../kconfig.md#CONFIG_BT_AUDIO_TX "CONFIG_BT_AUDIO_TX") .

        Parameters:
        :   - **stream** – **[in]** Stream object.
            - **info** – **[out]** Transmit info object.

        Return values:
        :   - **0** – on success
            - **-EINVAL** – if the stream is invalid, if the stream is not configured for sending or if it is not connected with a isochronous stream
            - **Any** – return value from bt\_iso\_chan\_get\_tx\_sync()

    void bt\_bap\_scan\_delegator\_register\_cb(struct [bt\_bap\_scan\_delegator\_cb](#c.bt_bap_scan_delegator_cb) \*cb)
    :   Register the callbacks for the Basic Audio Profile Scan Delegator.

        Only one set of callbacks can be registered at any one time, and calling this function multiple times will override any previously registered callbacks.

        Parameters:
        :   - **cb** – Pointer to the callback struct

    int bt\_bap\_scan\_delegator\_set\_pa\_state(uint8\_t src\_id, enum [bt\_bap\_pa\_state](#c.bt_bap_pa_state) pa\_state)
    :   Set the periodic advertising sync state to syncing.

        Set the periodic advertising sync state for a receive state to syncing, notifying Broadcast Assistants.

        Parameters:
        :   - **src\_id** – The source id used to identify the receive state.
            - **pa\_state** – The Periodic Advertising sync state to set. BT\_BAP\_PA\_STATE\_NOT\_SYNCED and BT\_BAP\_PA\_STATE\_SYNCED is not necessary to provide, as they are handled internally.

        Returns:
        :   int Error value. 0 on success, errno on fail.

    int bt\_bap\_scan\_delegator\_set\_bis\_sync\_state(uint8\_t src\_id, uint32\_t bis\_synced[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS])
    :   Set the sync state of a receive state in the server.

        Parameters:
        :   - **src\_id** – The source id used to identify the receive state.
            - **bis\_synced** – Array of bitfields to set the BIS sync state for each subgroup.

        Returns:
        :   int Error value. 0 on success, ERRNO on fail.

    int bt\_bap\_scan\_delegator\_add\_src(const struct [bt\_bap\_scan\_delegator\_add\_src\_param](#c.bt_bap_scan_delegator_add_src_param) \*param)
    :   Add a receive state source locally.

        This will notify any connected clients about the new source. This allows them to modify and even remove it.

        If  [`CONFIG_BT_BAP_BROADCAST_SINK`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SINK "CONFIG_BT_BAP_BROADCAST_SINK") is enabled, any Broadcast Sink sources are autonomously added.

        Parameters:
        :   - **param** – The parameters for adding the new source

        Returns:
        :   int errno on failure, or source ID on success.

    int bt\_bap\_scan\_delegator\_mod\_src(const struct [bt\_bap\_scan\_delegator\_mod\_src\_param](#c.bt_bap_scan_delegator_mod_src_param) \*param)
    :   Add a receive state source locally.

        This will notify any connected clients about the new source. This allows them to modify and even remove it.

        If  [`CONFIG_BT_BAP_BROADCAST_SINK`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SINK "CONFIG_BT_BAP_BROADCAST_SINK") is enabled, any Broadcast Sink sources are autonomously modified.

        Parameters:
        :   - **param** – The parameters for adding the new source

        Returns:
        :   int errno on failure, or source ID on success.

    int bt\_bap\_scan\_delegator\_rem\_src(uint8\_t src\_id)
    :   Remove a receive state source.

        This will remove the receive state. If the receive state periodic advertising is synced, [bt\_bap\_scan\_delegator\_cb.pa\_sync\_term\_req()](#structbt__bap__scan__delegator__cb_1a5b918538cfe0edaa69155f891981eeae) will be called.

        If  [`CONFIG_BT_BAP_BROADCAST_SINK`](../../../../kconfig.md#CONFIG_BT_BAP_BROADCAST_SINK "CONFIG_BT_BAP_BROADCAST_SINK") is enabled, any Broadcast Sink sources are autonomously removed.

        Parameters:
        :   - **src\_id** – The source ID to remove

        Returns:
        :   int Error value. 0 on success, errno on fail.

    void bt\_bap\_scan\_delegator\_foreach\_state([bt\_bap\_scan\_delegator\_state\_func\_t](#c.bt_bap_scan_delegator_state_func_t) func, void \*user\_data)
    :   Iterate through all existing receive states.

        Parameters:
        :   - **func** – The callback function
            - **user\_data** – User specified data that sent to the callback function

    const struct [bt\_bap\_scan\_delegator\_recv\_state](#c.bt_bap_scan_delegator_recv_state) \*bt\_bap\_scan\_delegator\_find\_state([bt\_bap\_scan\_delegator\_state\_func\_t](#c.bt_bap_scan_delegator_state_func_t) func, void \*user\_data)
    :   Find and return a receive state based on a compare function.

        Parameters:
        :   - **func** – The compare callback function
            - **user\_data** – User specified data that sent to the callback function

        Returns:
        :   The first receive state where the `func` returned true, or NULL

    int bt\_bap\_broadcast\_assistant\_discover(struct bt\_conn \*conn)
    :   Discover Broadcast Audio Scan Service on the server.

        Warning: Only one connection can be active at any time; discovering for a new connection, will delete all previous data.

        Parameters:
        :   - **conn** – The connection

        Returns:
        :   int Error value. 0 on success, GATT error or ERRNO on fail.

    int bt\_bap\_broadcast\_assistant\_scan\_start(struct bt\_conn \*conn, bool start\_scan)
    :   Scan start for BISes for a remote server.

        This will let the Broadcast Audio Scan Service server know that this device is actively scanning for broadcast sources. The function can optionally also start scanning, if the caller does not want to start scanning itself.

        Scan results, if `start_scan` is true, is sent to the bt\_bap\_broadcast\_assistant\_scan\_cb callback.

        Parameters:
        :   - **conn** – Connection to the Broadcast Audio Scan Service server. Used to let the server know that we are scanning.
            - **start\_scan** – Start scanning if true. If false, the application should enable scan itself.

        Returns:
        :   int Error value. 0 on success, GATT error or ERRNO on fail.

    int bt\_bap\_broadcast\_assistant\_scan\_stop(struct bt\_conn \*conn)
    :   Stop remote scanning for BISes for a server.

        Parameters:
        :   - **conn** – Connection to the server.

        Returns:
        :   int Error value. 0 on success, GATT error or ERRNO on fail.

    int bt\_bap\_broadcast\_assistant\_register\_cb(struct [bt\_bap\_broadcast\_assistant\_cb](#c.bt_bap_broadcast_assistant_cb) \*cb)
    :   Registers the callbacks used by Broadcast Audio Scan Service client.

        Parameters:
        :   - **cb** – The callback structure.

        Return values:
        :   - **0** – on success
            - **-EINVAL** – if `cb` is NULL
            - **-EALREADY** – if `cb` was already registered

    int bt\_bap\_broadcast\_assistant\_unregister\_cb(struct [bt\_bap\_broadcast\_assistant\_cb](#c.bt_bap_broadcast_assistant_cb) \*cb)
    :   Unregisters the callbacks used by the Broadcast Audio Scan Service client.

        Parameters:
        :   - **cb** – The callback structure.

        Return values:
        :   - **0** – on success
            - **-EINVAL** – if `cb` is NULL
            - **-EALREADY** – if `cb` was not registered

    int bt\_bap\_broadcast\_assistant\_add\_src(struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_add\_src\_param](#c.bt_bap_broadcast_assistant_add_src_param) \*param)
    :   Add a source on the server.

        Parameters:
        :   - **conn** – Connection to the server.
            - **param** – Parameter struct.

        Returns:
        :   Error value. 0 on success, GATT error or ERRNO on fail.

    int bt\_bap\_broadcast\_assistant\_mod\_src(struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_mod\_src\_param](#c.bt_bap_broadcast_assistant_mod_src_param) \*param)
    :   Modify a source on the server.

        Parameters:
        :   - **conn** – Connection to the server.
            - **param** – Parameter struct.

        Returns:
        :   Error value. 0 on success, GATT error or ERRNO on fail.

    int bt\_bap\_broadcast\_assistant\_set\_broadcast\_code(struct bt\_conn \*conn, uint8\_t src\_id, const uint8\_t broadcast\_code[16])
    :   Set a broadcast code to the specified receive state.

        Parameters:
        :   - **conn** – Connection to the server.
            - **src\_id** – Source ID of the receive state.
            - **broadcast\_code** – The broadcast code.

        Returns:
        :   Error value. 0 on success, GATT error or ERRNO on fail.

    int bt\_bap\_broadcast\_assistant\_rem\_src(struct bt\_conn \*conn, uint8\_t src\_id)
    :   Remove a source from the server.

        Parameters:
        :   - **conn** – Connection to the server.
            - **src\_id** – Source ID of the receive state.

        Returns:
        :   Error value. 0 on success, GATT error or ERRNO on fail.

    int bt\_bap\_broadcast\_assistant\_read\_recv\_state(struct bt\_conn \*conn, uint8\_t idx)
    :   Read the specified receive state from the server.

        Parameters:
        :   - **conn** – Connection to the server.
            - **idx** – The index of the receive start (0 up to the value from bt\_bap\_broadcast\_assistant\_discover\_cb)

        Returns:
        :   Error value. 0 on success, GATT error or ERRNO on fail.

    struct bt\_bap\_ascs\_rsp
    :   *#include <bap.h>*

        Structure storing values of fields of ASE Control Point notification.

        Public Members

        enum [bt\_bap\_ascs\_rsp\_code](#c.bt_bap_ascs_rsp_code) code
        :   Value of the Response Code field.

            The following response codes are accepted:

            - [BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a)

        enum [bt\_bap\_ascs\_reason](#c.bt_bap_ascs_reason) reason
        :   Response reason.

            If the Response Code is one of the following:

            - [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21) all values from [bt\_bap\_ascs\_reason](#group__bt__bap_1ga9ca1630544a336b15af8a8e8934c5a45) can be used.

            If the Response Code is one of the following:

            - [BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a) only value [BT\_BAP\_ASCS\_REASON\_NONE](#group__bt__bap_1gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd) shall be used.

        enum [bt\_audio\_metadata\_type](audio.md#c.bt_audio_metadata_type "bt_audio_metadata_type") metadata\_type
        :   Response metadata type.

            If the Response Code is one of the following:

            - [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7)
            - [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](#group__bt__bap_1gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06) the value of the Metadata Type shall be used.

        union [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp).[anonymous] [anonymous]
        :   Value of the Reason field.

            The meaning of this value depend on the Response Code field.

    struct bt\_bap\_bass\_subgroup
    :   *#include <bap.h>*

        Struct to hold subgroup specific information for the receive state.

        Public Members

        uint32\_t bis\_sync
        :   BIS synced bitfield.

        uint8\_t metadata\_len
        :   Length of the metadata.

        uint8\_t metadata[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE]
        :   The metadata.

    struct bt\_bap\_scan\_delegator\_recv\_state
    :   *#include <bap.h>*

        Represents the Broadcast Audio Scan Service receive state.

        Public Members

        uint8\_t src\_id
        :   The source ID.

        [bt\_addr\_le\_t](../gap.md#c.bt_addr_le_t "bt_addr_le_t") addr
        :   The Bluetooth address.

        uint8\_t adv\_sid
        :   The advertising set ID.

        enum [bt\_bap\_pa\_state](#c.bt_bap_pa_state) pa\_sync\_state
        :   The periodic adverting sync state.

        enum [bt\_bap\_big\_enc\_state](#c.bt_bap_big_enc_state) encrypt\_state
        :   The broadcast isochronous group encryption state.

        uint32\_t broadcast\_id
        :   The 24-bit broadcast ID.

        uint8\_t bad\_code[16]
        :   The bad broadcast code.

            Only valid if encrypt\_state is [BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ](#group__bt__bap_1gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2)

        uint8\_t num\_subgroups
        :   Number of subgroups.

        struct [bt\_bap\_bass\_subgroup](#c.bt_bap_bass_subgroup) subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]
        :   Subgroup specific information.

    struct bt\_bap\_scan\_delegator\_cb
    :   *#include <bap.h>*

        Struct to hold the Basic Audio Profile Scan Delegator callbacks.

        These can be registered for usage with [bt\_bap\_scan\_delegator\_register\_cb()](#group__bt__bap_1ga5841f00a46c8b32bc8253d70dc05f104).

        Public Members

        void (\*recv\_state\_updated)(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](#c.bt_bap_scan_delegator_recv_state) \*recv\_state)
        :   Receive state updated.

            Param conn:
            :   Pointer to the connection to a remote device if the change was caused by it, otherwise NULL.

            Param recv\_state:
            :   Pointer to the receive state that was updated.

            Return:
            :   0 in case of success or negative value in case of error.

        int (\*pa\_sync\_req)(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](#c.bt_bap_scan_delegator_recv_state) \*recv\_state, bool past\_avail, uint16\_t pa\_interval)
        :   Periodic advertising sync request.

            Request from peer device to synchronize with the periodic advertiser denoted by the `recv_state`. To notify the Broadcast Assistant about any pending sync

            Param conn:
            :   Pointer to the connection requesting the periodic advertising sync.

            Param recv\_state:
            :   Pointer to the receive state that is being requested for periodic advertising sync.

            Param past\_avail:
            :   True if periodic advertising sync transfer is available.

            Param pa\_interval:
            :   The periodic advertising interval.

            Return:
            :   0 in case of accept, or other value to reject.

        int (\*pa\_sync\_term\_req)(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](#c.bt_bap_scan_delegator_recv_state) \*recv\_state)
        :   Periodic advertising sync termination request.

            Request from peer device to terminate the periodic advertiser sync denoted by the `recv_state`.

            Param conn:
            :   Pointer to the connection requesting the periodic advertising sync termination.

            Param recv\_state:
            :   Pointer to the receive state that is being requested for periodic advertising sync.

            Return:
            :   0 in case of success or negative value in case of error.

        void (\*broadcast\_code)(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](#c.bt_bap_scan_delegator_recv_state) \*recv\_state, const uint8\_t broadcast\_code[16])
        :   Broadcast code received.

            Broadcast code received from a broadcast assistant

            Param conn:
            :   Pointer to the connection providing the broadcast code.

            Param recv\_state:
            :   Pointer to the receive state the broadcast code is being provided for.

            Param broadcast\_code:
            :   The 16-octet broadcast code

        int (\*bis\_sync\_req)(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](#c.bt_bap_scan_delegator_recv_state) \*recv\_state, const uint32\_t bis\_sync\_req[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS])
        :   Broadcast Isochronous Stream synchronize request.

            Request from Broadcast Assistant device to modify the Broadcast Isochronous Stream states. The request shall be fulfilled with accordance to the `bis_sync_req` within reasonable time. The Broadcast Assistant may also request fewer, or none, indexes to be synchronized.

            Param conn:
            :   **[in]** Pointer to the connection of the Broadcast Assistant requesting the sync.

            Param recv\_state:
            :   **[in]** Pointer to the receive state that is being requested for the sync.

            Param bis\_sync\_req:
            :   Array of bitfields of which BIS indexes that is requested to sync for each subgroup by the Broadcast Assistant. A value of 0 indicates a request to terminate the BIG sync.

            Return:
            :   0 in case of accept, or other value to reject.

    struct bt\_bap\_ep\_info
    :   *#include <bap.h>*

        Structure holding information of audio stream endpoint.

        Public Members

        uint8\_t id
        :   The ID of the endpoint.

        enum [bt\_bap\_ep\_state](#c.bt_bap_ep_state) state
        :   The state of the endpoint.

        enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir
        :   Capabilities type.

        struct bt\_iso\_chan \*iso\_chan
        :   The isochronous channel associated with the endpoint.

        bool can\_send
        :   True if the stream associated with the endpoint is able to send data.

        bool can\_recv
        :   True if the stream associated with the endpoint is able to receive data.

        struct bt\_bap\_ep \*paired\_ep
        :   Pointer to paired endpoint if the endpoint is part of a bidirectional CIS, otherwise NULL.

        const struct [bt\_audio\_codec\_qos\_pref](audio.md#c.bt_audio_codec_qos_pref "bt_audio_codec_qos_pref") \*qos\_pref
        :   Pointer to the preferred QoS settings associated with the endpoint.

    struct bt\_bap\_stream
    :   *#include <bap.h>*

        Basic Audio Profile stream structure.

        Streams represents a stream configuration of a Remote Endpoint and a Local Capability.

        Note

        Streams are unidirectional but can be paired with other streams to use a bidirectional connected isochronous stream.

        Public Members

        struct bt\_conn \*conn
        :   Connection reference.

        struct bt\_bap\_ep \*ep
        :   Endpoint reference.

        struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg
        :   Codec Configuration.

        struct [bt\_audio\_codec\_qos](audio.md#c.bt_audio_codec_qos "bt_audio_codec_qos") \*qos
        :   QoS Configuration.

        struct [bt\_bap\_stream\_ops](#c.bt_bap_stream_ops) \*ops
        :   Audio stream operations.

        void \*user\_data
        :   Stream user data.

    struct bt\_bap\_stream\_ops
    :   *#include <bap.h>*

        Stream operation.

        Public Members

        void (\*configured)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, const struct [bt\_audio\_codec\_qos\_pref](audio.md#c.bt_audio_codec_qos_pref "bt_audio_codec_qos_pref") \*pref)
        :   Stream configured callback.

            Configured callback is called whenever an Audio Stream has been configured.

            Param stream:
            :   Stream object that has been configured.

            Param pref:
            :   Remote QoS preferences.

        void (\*qos\_set)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
        :   Stream QoS set callback.

            QoS set callback is called whenever an Audio Stream Quality of Service has been set or updated.

            Param stream:
            :   Stream object that had its QoS updated.

        void (\*enabled)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
        :   Stream enabled callback.

            Enabled callback is called whenever an Audio Stream has been enabled.

            Param stream:
            :   Stream object that has been enabled.

        void (\*metadata\_updated)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
        :   Stream metadata updated callback.

            Metadata Updated callback is called whenever an Audio Stream’s metadata has been updated.

            Param stream:
            :   Stream object that had its metadata updated.

        void (\*disabled)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
        :   Stream disabled callback.

            Disabled callback is called whenever an Audio Stream has been disabled.

            Param stream:
            :   Stream object that has been disabled.

        void (\*released)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
        :   Stream released callback.

            Released callback is called whenever a Audio Stream has been released and can be deallocated.

            Param stream:
            :   Stream object that has been released.

        void (\*started)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
        :   Stream started callback.

            Started callback is called whenever an Audio Stream has been started and will be usable for streaming.

            Param stream:
            :   Stream object that has been started.

        void (\*stopped)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, uint8\_t reason)
        :   Stream stopped callback.

            Stopped callback is called whenever an Audio Stream has been stopped.

            Param stream:
            :   Stream object that has been stopped.

            Param reason:
            :   BT\_HCI\_ERR\_\* reason for the disconnection.

        void (\*recv)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, const struct bt\_iso\_recv\_info \*info, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
        :   Stream audio HCI receive callback.

            This callback is only used if the ISO data path is HCI.

            Param stream:
            :   Stream object.

            Param info:
            :   Pointer to the metadata for the buffer. The lifetime of the pointer is linked to the lifetime of the [net\_buf](../../../networking/api/net_buf.md#structnet__buf). Metadata such as sequence number and timestamp can be provided by the bluetooth controller.

            Param buf:
            :   Buffer containing incoming audio data.

        void (\*sent)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
        :   Stream audio HCI sent callback.

            This callback will be called once the controller marks the SDU as completed. When the controller does so is implementation dependent. It could be after the SDU is enqueued for transmission, or after it is sent on air or flushed.

            This callback is only used if the ISO data path is HCI.

            Param stream:
            :   Stream object.

        void (\*connected)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream)
        :   Isochronous channel connected callback.

            If this callback is provided it will be called whenever the isochronous channel for the stream has been connected. This does not mean that the stream is ready to be used, which is indicated by the [bt\_bap\_stream\_ops::started](#structbt__bap__stream__ops_1a7f595e37d40b94510bf09c1f82b479f3) callback.

            If the stream shares an isochronous channel with another stream, then this callback may still be called, without the stream going into the started state.

            Param stream:
            :   Stream object.

        void (\*disconnected)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, uint8\_t reason)
        :   Isochronous channel disconnected callback.

            If this callback is provided it will be called whenever the isochronous channel is disconnected, including when a connection gets rejected.

            If the stream shares an isochronous channel with another stream, then this callback may not be called, even if the stream is leaving the streaming state.

            Param stream:
            :   Stream object.

            Param reason:
            :   BT\_HCI\_ERR\_\* reason for the disconnection.

    struct bt\_bap\_scan\_delegator\_add\_src\_param
    :   *#include <bap.h>*

        Parameters for [bt\_bap\_scan\_delegator\_add\_src()](#group__bt__bap_1ga6eb2a782d761da12d112356cfe723ff0).

        Public Members

        struct bt\_le\_per\_adv\_sync \*pa\_sync
        :   The periodic adverting sync.

        enum [bt\_bap\_big\_enc\_state](#c.bt_bap_big_enc_state) encrypt\_state
        :   The broadcast isochronous group encryption state.

        uint32\_t broadcast\_id
        :   The 24-bit broadcast ID.

        uint8\_t num\_subgroups
        :   Number of subgroups.

        struct [bt\_bap\_bass\_subgroup](#c.bt_bap_bass_subgroup) subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]
        :   Subgroup specific information.

    struct bt\_bap\_scan\_delegator\_mod\_src\_param
    :   *#include <bap.h>*

        Parameters for [bt\_bap\_scan\_delegator\_mod\_src()](#group__bt__bap_1gac022f38269742f16ff6887840ef5ba9a).

        Public Members

        uint8\_t src\_id
        :   The periodic adverting sync.

        enum [bt\_bap\_big\_enc\_state](#c.bt_bap_big_enc_state) encrypt\_state
        :   The broadcast isochronous group encryption state.

        uint32\_t broadcast\_id
        :   The 24-bit broadcast ID.

        uint8\_t num\_subgroups
        :   Number of subgroups.

        struct [bt\_bap\_bass\_subgroup](#c.bt_bap_bass_subgroup) subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]
        :   Subgroup specific information.

            If a subgroup’s metadata\_len is set to 0, the existing metadata for the subgroup will remain unchanged

    struct bt\_bap\_broadcast\_assistant\_cb
    :   *#include <bap.h>*

        Struct to hold the Basic Audio Profile Broadcast Assistant callbacks.

        These can be registered for usage with [bt\_bap\_broadcast\_assistant\_register\_cb()](#group__bt__bap_1gabab24c44e9833029965475ad7b149e6e).

        Public Members

        void (\*discover)(struct bt\_conn \*conn, int err, uint8\_t recv\_state\_count)
        :   Callback function for bt\_bap\_broadcast\_assistant\_discover.

            Param conn:
            :   The connection that was used to discover Broadcast Audio Scan Service.

            Param err:
            :   Error value. 0 on success, GATT error or ERRNO on fail.

            Param recv\_state\_count:
            :   Number of receive states on the server.

        void (\*scan)(const struct [bt\_le\_scan\_recv\_info](../gap.md#c.bt_le_scan_recv_info "bt_le_scan_recv_info") \*info, uint32\_t broadcast\_id)
        :   Callback function for Broadcast Audio Scan Service client scan results.

            Called when the scanner finds an advertiser that advertises the BT\_UUID\_BROADCAST\_AUDIO UUID.

            Param info:
            :   Advertiser information.

            Param broadcast\_id:
            :   24-bit broadcast ID.

        void (\*recv\_state)(struct bt\_conn \*conn, int err, const struct [bt\_bap\_scan\_delegator\_recv\_state](#c.bt_bap_scan_delegator_recv_state) \*state)
        :   Callback function for when a receive state is read or updated.

            Called whenever a receive state is read or updated.

            Param conn:
            :   The connection to the Broadcast Audio Scan Service server.

            Param err:
            :   Error value. 0 on success, GATT error on fail.

            Param state:
            :   The receive state or NULL if the receive state is empty.

        void (\*recv\_state\_removed)(struct bt\_conn \*conn, uint8\_t src\_id)
        :   Callback function for when a receive state is removed.

            Param conn:
            :   The connection to the Broadcast Audio Scan Service server.

            Param src\_id:
            :   The receive state.

        void (\*scan\_start)(struct bt\_conn \*conn, int err)
        :   Callback function for [bt\_bap\_broadcast\_assistant\_scan\_start()](#group__bt__bap_1ga98ac067e66d263aa41fc6f8df6bb9126).

            Param conn:
            :   The connection to the peer device.

            Param err:
            :   Error value. 0 on success, GATT error on fail.

        void (\*scan\_stop)(struct bt\_conn \*conn, int err)
        :   Callback function for [bt\_bap\_broadcast\_assistant\_scan\_stop()](#group__bt__bap_1ga76cae35df980b78a10551811050b2760).

            Param conn:
            :   The connection to the peer device.

            Param err:
            :   Error value. 0 on success, GATT error on fail.

        void (\*add\_src)(struct bt\_conn \*conn, int err)
        :   Callback function for [bt\_bap\_broadcast\_assistant\_add\_src()](#group__bt__bap_1gac93cb4cab33d0b937e752bc0b71cad9e).

            Param conn:
            :   The connection to the peer device.

            Param err:
            :   Error value. 0 on success, GATT error on fail.

        void (\*mod\_src)(struct bt\_conn \*conn, int err)
        :   Callback function for [bt\_bap\_broadcast\_assistant\_mod\_src()](#group__bt__bap_1gaa9c292a7dcb470926d8d7d4be699a0c7).

            Param conn:
            :   The connection to the peer device.

            Param err:
            :   Error value. 0 on success, GATT error on fail.

        void (\*broadcast\_code)(struct bt\_conn \*conn, int err)
        :   Callback function for bt\_bap\_broadcast\_assistant\_broadcast\_code().

            Param conn:
            :   The connection to the peer device.

            Param err:
            :   Error value. 0 on success, GATT error on fail.

        void (\*rem\_src)(struct bt\_conn \*conn, int err)
        :   Callback function for [bt\_bap\_broadcast\_assistant\_rem\_src()](#group__bt__bap_1ga09785690db551677a043fcaa2fdb7f29).

            Param conn:
            :   The connection to the peer device.

            Param err:
            :   Error value. 0 on success, GATT error on fail.

    struct bt\_bap\_broadcast\_assistant\_add\_src\_param
    :   *#include <bap.h>*

        Parameters for adding a source to a Broadcast Audio Scan Service server.

        Public Members

        [bt\_addr\_le\_t](../gap.md#c.bt_addr_le_t "bt_addr_le_t") addr
        :   Address of the advertiser.

        uint8\_t adv\_sid
        :   SID of the advertising set.

        bool pa\_sync
        :   Whether to sync to periodic advertisements.

        uint32\_t broadcast\_id
        :   24-bit broadcast ID

        uint16\_t pa\_interval
        :   Periodic advertising interval in milliseconds.

            BT\_BAP\_PA\_INTERVAL\_UNKNOWN if unknown.

        uint8\_t num\_subgroups
        :   Number of subgroups.

        struct [bt\_bap\_bass\_subgroup](#c.bt_bap_bass_subgroup) \*subgroups
        :   Pointer to array of subgroups.

    struct bt\_bap\_broadcast\_assistant\_mod\_src\_param
    :   *#include <bap.h>*

        Parameters for modifying a source.

        Public Members

        uint8\_t src\_id
        :   Source ID of the receive state.

        bool pa\_sync
        :   Whether to sync to periodic advertisements.

        uint16\_t pa\_interval
        :   Periodic advertising interval.

            BT\_BAP\_PA\_INTERVAL\_UNKNOWN if unknown.

        uint8\_t num\_subgroups
        :   Number of subgroups.

        struct [bt\_bap\_bass\_subgroup](#c.bt_bap_bass_subgroup) \*subgroups
        :   Pointer to array of subgroups.

*group* BAP Unicast Client APIs
:   Functions

    int bt\_bap\_unicast\_group\_create(struct [bt\_bap\_unicast\_group\_param](#c.bt_bap_unicast_group_param) \*param, struct bt\_bap\_unicast\_group \*\*unicast\_group)
    :   Create audio unicast group.

        Create a new audio unicast group with one or more audio streams as a unicast client. Streams in a unicast group shall share the same interval, framing and latency (see [bt\_audio\_codec\_qos](audio.md#structbt__audio__codec__qos)).

        Parameters:
        :   - **param** – **[in]** The unicast group create parameters.
            - **unicast\_group** – **[out]** Pointer to the unicast group created.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_unicast\_group\_add\_streams(struct bt\_bap\_unicast\_group \*unicast\_group, struct [bt\_bap\_unicast\_group\_stream\_pair\_param](#c.bt_bap_unicast_group_stream_pair_param) params[], size\_t num\_param)
    :   Add streams to a unicast group as a unicast client.

        This function can be used to add additional streams to a bt\_bap\_unicast\_group.

        This can be called at any time before any of the streams in the group has been started (see [bt\_bap\_stream\_ops.started()](#structbt__bap__stream__ops_1a7f595e37d40b94510bf09c1f82b479f3)). This can also be called after the streams have been stopped (see [bt\_bap\_stream\_ops.stopped()](#structbt__bap__stream__ops_1ab50ea295069a2cd1ab6f4353052262f5)).

        Once a stream has been added to a unicast group, it cannot be removed. To remove a stream from a group, the group must be deleted with [bt\_bap\_unicast\_group\_delete()](#group__bt__bap__unicast__client_1ga34dbdce6133f8366df453ec937fb47d2), but this will require all streams in the group to be released first.

        Parameters:
        :   - **unicast\_group** – Pointer to the unicast group
            - **params** – Array of stream parameters with streams being added to the group.
            - **num\_param** – Number of parameters in `params`.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_unicast\_group\_delete(struct bt\_bap\_unicast\_group \*unicast\_group)
    :   Delete audio unicast group.

        Delete a audio unicast group as a client. All streams in the group shall be in the idle or configured state.

        Parameters:
        :   - **unicast\_group** – Pointer to the unicast group to delete

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_unicast\_client\_register\_cb(const struct [bt\_bap\_unicast\_client\_cb](#c.bt_bap_unicast_client_cb) \*cb)
    :   Register unicast client callbacks.

        Only one callback structure can be registered, and attempting to registering more than one will result in an error.

        Parameters:
        :   - **cb** – Unicast client callback structure.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_unicast\_client\_discover(struct bt\_conn \*conn, enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir)
    :   Discover remote capabilities and endpoints.

        This procedure is used by a client to discover remote capabilities and endpoints and notifies via params callback.

        Parameters:
        :   - **conn** – Connection object
            - **dir** – The type of remote endpoints and capabilities to discover.

    struct bt\_bap\_unicast\_group\_stream\_param
    :   *#include <bap.h>*

        Parameter struct for each stream in the unicast group.

        Public Members

        struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream
        :   Pointer to a stream object.

        struct [bt\_audio\_codec\_qos](audio.md#c.bt_audio_codec_qos "bt_audio_codec_qos") \*qos
        :   The QoS settings for the stream object.

    struct bt\_bap\_unicast\_group\_stream\_pair\_param
    :   *#include <bap.h>*

        Parameter struct for the unicast group functions.

        Parameter struct for the [bt\_bap\_unicast\_group\_create()](#group__bt__bap__unicast__client_1gaafd53b5f45d998b44e94a1b58e93ba21) and [bt\_bap\_unicast\_group\_add\_streams()](#group__bt__bap__unicast__client_1ga9cc792cd1eaaa79d56f3df0e2341cbf6) functions.

        Public Members

        struct [bt\_bap\_unicast\_group\_stream\_param](#c.bt_bap_unicast_group_stream_param) \*rx\_param
        :   Pointer to a receiving stream parameters.

        struct [bt\_bap\_unicast\_group\_stream\_param](#c.bt_bap_unicast_group_stream_param) \*tx\_param
        :   Pointer to a transmitting stream parameters.

    struct bt\_bap\_unicast\_group\_param
    :   *#include <bap.h>*

        Parameters for the creating unicast groups with [bt\_bap\_unicast\_group\_create()](#group__bt__bap__unicast__client_1gaafd53b5f45d998b44e94a1b58e93ba21).

        Public Members

        size\_t params\_count
        :   The number of parameters in `params`.

        struct [bt\_bap\_unicast\_group\_stream\_pair\_param](#c.bt_bap_unicast_group_stream_pair_param) \*params
        :   Array of stream parameters.

        uint8\_t packing
        :   Unicast Group packing mode.

            BT\_ISO\_PACKING\_SEQUENTIAL or BT\_ISO\_PACKING\_INTERLEAVED.

            Note

            This is a recommendation to the controller, which the controller may ignore.

        uint8\_t c\_to\_p\_ft
        :   Central to Peripheral flush timeout.

            The flush timeout in multiples of ISO\_Interval for each payload sent from the Central to Peripheral.

            Value range from BT\_ISO\_FT\_MIN to BT\_ISO\_FT\_MAX

        uint8\_t p\_to\_c\_ft
        :   Peripheral to Central flush timeout.

            The flush timeout in multiples of ISO\_Interval for each payload sent from the Peripheral to Central.

            Value range from BT\_ISO\_FT\_MIN to BT\_ISO\_FT\_MAX.

        uint16\_t iso\_interval
        :   ISO interval.

            Time between consecutive CIS anchor points.

            Value range from BT\_ISO\_ISO\_INTERVAL\_MIN to BT\_ISO\_ISO\_INTERVAL\_MAX.

    struct bt\_bap\_unicast\_client\_cb
    :   *#include <bap.h>*

        Unicast Client callback structure.

        Public Members

        void (\*location)(struct bt\_conn \*conn, enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, enum [bt\_audio\_location](audio.md#c.bt_audio_location "bt_audio_location") loc)
        :   Remote Unicast Server Audio Locations.

            This callback is called whenever the audio locations is read from the server or otherwise notified to the client.

            Param conn:
            :   Connection to the remote unicast server.

            Param dir:
            :   Direction of the location.

            Param loc:
            :   The location bitfield value.

            Return:
            :   0 in case of success or negative value in case of error.

        void (\*available\_contexts)(struct bt\_conn \*conn, enum [bt\_audio\_context](audio.md#c.bt_audio_context "bt_audio_context") snk\_ctx, enum [bt\_audio\_context](audio.md#c.bt_audio_context "bt_audio_context") src\_ctx)
        :   Remote Unicast Server Available Contexts.

            This callback is called whenever the available contexts are read from the server or otherwise notified to the client.

            Param conn:
            :   Connection to the remote unicast server.

            Param snk\_ctx:
            :   The sink context bitfield value.

            Param src\_ctx:
            :   The source context bitfield value.

            Return:
            :   0 in case of success or negative value in case of error.

        void (\*config)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, enum [bt\_bap\_ascs\_rsp\_code](#c.bt_bap_ascs_rsp_code) rsp\_code, enum [bt\_bap\_ascs\_reason](#c.bt_bap_ascs_reason) reason)
        :   Callback function for [bt\_bap\_stream\_config()](#group__bt__bap_1ga1e19aa4746132a2231037e82778bc402) and [bt\_bap\_stream\_reconfig()](#group__bt__bap_1gaac84ee7b3ab5578d258848754f752546).

            Called when the codec configure operation is completed on the server.

            Param stream:
            :   Stream the operation was performed on.

            Param rsp\_code:
            :   Response code.

            Param reason:
            :   Reason code.

        void (\*qos)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, enum [bt\_bap\_ascs\_rsp\_code](#c.bt_bap_ascs_rsp_code) rsp\_code, enum [bt\_bap\_ascs\_reason](#c.bt_bap_ascs_reason) reason)
        :   Callback function for [bt\_bap\_stream\_qos()](#group__bt__bap_1gac878ed89242cac9a8514e8e4f1da4d9d).

            Called when the QoS configure operation is completed on the server. This will be called for each stream in the group that was being QoS configured.

            Param stream:
            :   Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server.

            Param rsp\_code:
            :   Response code.

            Param reason:
            :   Reason code.

        void (\*enable)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, enum [bt\_bap\_ascs\_rsp\_code](#c.bt_bap_ascs_rsp_code) rsp\_code, enum [bt\_bap\_ascs\_reason](#c.bt_bap_ascs_reason) reason)
        :   Callback function for [bt\_bap\_stream\_enable()](#group__bt__bap_1ga13a859b31b0310ec22339ec7ed0754f8).

            Called when the enable operation is completed on the server.

            Param stream:
            :   Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server.

            Param rsp\_code:
            :   Response code.

            Param reason:
            :   Reason code.

        void (\*start)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, enum [bt\_bap\_ascs\_rsp\_code](#c.bt_bap_ascs_rsp_code) rsp\_code, enum [bt\_bap\_ascs\_reason](#c.bt_bap_ascs_reason) reason)
        :   Callback function for [bt\_bap\_stream\_start()](#group__bt__bap_1ga8f2dc67c35299334d21c7dee7b8664ae).

            Called when the start operation is completed on the server. This will only be called if the stream supplied to [bt\_bap\_stream\_start()](#group__bt__bap_1ga8f2dc67c35299334d21c7dee7b8664ae) is for a [BT\_AUDIO\_DIR\_SOURCE](audio.md#group__bt__audio_1gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) endpoint.

            Param stream:
            :   Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server.

            Param rsp\_code:
            :   Response code.

            Param reason:
            :   Reason code.

        void (\*stop)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, enum [bt\_bap\_ascs\_rsp\_code](#c.bt_bap_ascs_rsp_code) rsp\_code, enum [bt\_bap\_ascs\_reason](#c.bt_bap_ascs_reason) reason)
        :   Callback function for [bt\_bap\_stream\_stop()](#group__bt__bap_1gada72bcd3951eff2bc6b70c02dcaed98b).

            Called when the stop operation is completed on the server. This will only be called if the stream supplied to [bt\_bap\_stream\_stop()](#group__bt__bap_1gada72bcd3951eff2bc6b70c02dcaed98b) is for a [BT\_AUDIO\_DIR\_SOURCE](audio.md#group__bt__audio_1gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) endpoint.

            Param stream:
            :   Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server.

            Param rsp\_code:
            :   Response code.

            Param reason:
            :   Reason code.

        void (\*disable)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, enum [bt\_bap\_ascs\_rsp\_code](#c.bt_bap_ascs_rsp_code) rsp\_code, enum [bt\_bap\_ascs\_reason](#c.bt_bap_ascs_reason) reason)
        :   Callback function for [bt\_bap\_stream\_disable()](#group__bt__bap_1ga0fd2bb35909fc19e3e9cff068ba9e9aa).

            Called when the disable operation is completed on the server.

            Param stream:
            :   Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server.

            Param rsp\_code:
            :   Response code.

            Param reason:
            :   Reason code.

        void (\*metadata)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, enum [bt\_bap\_ascs\_rsp\_code](#c.bt_bap_ascs_rsp_code) rsp\_code, enum [bt\_bap\_ascs\_reason](#c.bt_bap_ascs_reason) reason)
        :   Callback function for [bt\_bap\_stream\_metadata()](#group__bt__bap_1ga0afe6c927729697e2f984cefcbc7c0f1).

            Called when the metadata operation is completed on the server.

            Param stream:
            :   Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server.

            Param rsp\_code:
            :   Response code.

            Param reason:
            :   Reason code.

        void (\*release)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, enum [bt\_bap\_ascs\_rsp\_code](#c.bt_bap_ascs_rsp_code) rsp\_code, enum [bt\_bap\_ascs\_reason](#c.bt_bap_ascs_reason) reason)
        :   Callback function for [bt\_bap\_stream\_release()](#group__bt__bap_1gaaf94f1f0dda7ef356c0f9ae79b5c60e4).

            Called when the release operation is completed on the server.

            Param stream:
            :   Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server.

            Param rsp\_code:
            :   Response code.

            Param reason:
            :   Reason code.

        void (\*pac\_record)(struct bt\_conn \*conn, enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, const struct [bt\_audio\_codec\_cap](audio.md#c.bt_audio_codec_cap "bt_audio_codec_cap") \*codec\_cap)
        :   Remote Published Audio Capability (PAC) record discovered.

            Called when a PAC record has been discovered as part of the discovery procedure.

            The `codec` is only valid while in the callback, so the values must be stored by the receiver if future use is wanted.

            If discovery procedure has complete both `codec` and `ep` are set to NULL.

            Param conn:
            :   Connection to the remote unicast server.

            Param dir:
            :   The type of remote endpoints and capabilities discovered.

            Param codec\_cap:
            :   Remote capabilities.

        void (\*endpoint)(struct bt\_conn \*conn, enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, struct bt\_bap\_ep \*ep)
        :   Remote Audio Stream Endpoint (ASE) discovered.

            Called when an ASE has been discovered as part of the discovery procedure.

            If discovery procedure has complete both `codec` and `ep` are set to NULL.

            Param conn:
            :   Connection to the remote unicast server.

            Param dir:
            :   The type of remote endpoints and capabilities discovered.

            Param ep:
            :   Remote endpoint.

        void (\*discover)(struct bt\_conn \*conn, int err, enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir)
        :   BAP discovery callback function.

            If discovery procedure has completed `ep` is set to NULL and `err` is 0.

            If discovery procedure has complete both `codec` and `ep` are set to NULL.

            Param conn:
            :   Connection to the remote unicast server.

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param dir:
            :   The type of remote endpoints and capabilities discovered.

*group* BAP Unicast Server APIs
:   Typedefs

    typedef void (\*bt\_bap\_ep\_func\_t)(struct bt\_bap\_ep \*ep, void \*user\_data)
    :   The callback function called for each endpoint.

        Param ep:
        :   The structure object with endpoint info.

        Param user\_data:
        :   Data to pass to the function.

    Functions

    int bt\_bap\_unicast\_server\_register\_cb(const struct [bt\_bap\_unicast\_server\_cb](#c.bt_bap_unicast_server_cb) \*cb)
    :   Register unicast server callbacks.

        Only one callback structure can be registered, and attempting to registering more than one will result in an error.

        Parameters:
        :   - **cb** – Unicast server callback structure.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_unicast\_server\_unregister\_cb(const struct [bt\_bap\_unicast\_server\_cb](#c.bt_bap_unicast_server_cb) \*cb)
    :   Unregister unicast server callbacks.

        May only unregister a callback structure that has previously been registered by [bt\_bap\_unicast\_server\_register\_cb()](#group__bt__bap__unicast__server_1ga7669133936bc13f7ab38817db9ce69c0).

        Parameters:
        :   - **cb** – Unicast server callback structure.

        Returns:
        :   0 in case of success or negative value in case of error.

    void bt\_bap\_unicast\_server\_foreach\_ep(struct bt\_conn \*conn, [bt\_bap\_ep\_func\_t](#c.bt_bap_ep_func_t) func, void \*user\_data)
    :   Iterate through all endpoints of the given connection.

        Parameters:
        :   - **conn** – Connection object
            - **func** – Function to call for each endpoint.
            - **user\_data** – Data to pass to the callback function.

    int bt\_bap\_unicast\_server\_config\_ase(struct bt\_conn \*conn, struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg, const struct [bt\_audio\_codec\_qos\_pref](audio.md#c.bt_audio_codec_qos_pref "bt_audio_codec_qos_pref") \*qos\_pref)
    :   Initialize and configure a new ASE.

        Parameters:
        :   - **conn** – Connection object
            - **stream** – Configured stream object to be attached to the ASE
            - **codec\_cfg** – Codec configuration
            - **qos\_pref** – Audio Stream Quality of Service Preference

        Returns:
        :   0 in case of success or negative value in case of error.

    struct bt\_bap\_unicast\_server\_cb
    :   *#include <bap.h>*

        Unicast Server callback structure.

        Public Members

        int (\*config)(struct bt\_conn \*conn, const struct bt\_bap\_ep \*ep, enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, const struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg, struct [bt\_bap\_stream](#c.bt_bap_stream) \*\*stream, struct [bt\_audio\_codec\_qos\_pref](audio.md#c.bt_audio_codec_qos_pref "bt_audio_codec_qos_pref") \*const pref, struct [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp) \*rsp)
        :   Endpoint config request callback.

            Config callback is called whenever an endpoint is requested to be configured

            Param conn:
            :   **[in]** Connection object.

            Param ep:
            :   **[in]** Local Audio Endpoint being configured.

            Param dir:
            :   **[in]** Direction of the endpoint.

            Param codec\_cfg:
            :   **[in]** Codec configuration.

            Param stream:
            :   **[out]** Pointer to stream that will be configured for the endpoint.

            Param pref:
            :   **[out]** Pointer to a QoS preference object that shall be populated with values. Invalid values will reject the codec configuration request.

            Param rsp:
            :   **[out]** Object for the ASE operation response. Only used if the return value is non-zero.

            Return:
            :   0 in case of success or negative value in case of error.

        int (\*reconfig)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, const struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg, struct [bt\_audio\_codec\_qos\_pref](audio.md#c.bt_audio_codec_qos_pref "bt_audio_codec_qos_pref") \*const pref, struct [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp) \*rsp)
        :   Stream reconfig request callback.

            Reconfig callback is called whenever an Audio Stream needs to be reconfigured with different codec configuration.

            Param stream:
            :   **[in]** Stream object being reconfigured.

            Param dir:
            :   **[in]** Direction of the endpoint.

            Param codec\_cfg:
            :   **[in]** Codec configuration.

            Param pref:
            :   **[out]** Pointer to a QoS preference object that shall be populated with values. Invalid values will reject the codec configuration request.

            Param rsp:
            :   **[out]** Object for the ASE operation response. Only used if the return value is non-zero.

            Return:
            :   0 in case of success or negative value in case of error.

        int (\*qos)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, const struct [bt\_audio\_codec\_qos](audio.md#c.bt_audio_codec_qos "bt_audio_codec_qos") \*qos, struct [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp) \*rsp)
        :   Stream QoS request callback.

            QoS callback is called whenever an Audio Stream Quality of Service needs to be configured.

            Param stream:
            :   **[in]** Stream object being reconfigured.

            Param qos:
            :   Quality of Service configuration.

            Param rsp:
            :   **[out]** Object for the ASE operation response. Only used if the return value is non-zero.

            Return:
            :   0 in case of success or negative value in case of error.

        int (\*enable)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, const uint8\_t meta[], size\_t meta\_len, struct [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp) \*rsp)
        :   Stream Enable request callback.

            Enable callback is called whenever an Audio Stream is requested to be enabled to stream.

            Param stream:
            :   **[in]** Stream object being enabled.

            Param meta:
            :   **[in]** Metadata entries.

            Param meta\_len:
            :   **[in]** Length of metadata.

            Param rsp:
            :   **[out]** Object for the ASE operation response. Only used if the return value is non-zero.

            Return:
            :   0 in case of success or negative value in case of error.

        int (\*start)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp) \*rsp)
        :   Stream Start request callback.

            Start callback is called whenever an Audio Stream is requested to start streaming.

            Param stream:
            :   **[in]** Stream object.

            Param rsp:
            :   **[out]** Object for the ASE operation response. Only used if the return value is non-zero.

            Return:
            :   0 in case of success or negative value in case of error.

        int (\*metadata)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, const uint8\_t meta[], size\_t meta\_len, struct [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp) \*rsp)
        :   Stream Metadata update request callback.

            Metadata callback is called whenever an Audio Stream is requested to update its metadata.

            Param stream:
            :   **[in]** Stream object.

            Param meta:
            :   **[in]** Metadata entries.

            Param meta\_len:
            :   **[in]** Length of metadata.

            Param rsp:
            :   **[out]** Object for the ASE operation response. Only used if the return value is non-zero.

            Return:
            :   0 in case of success or negative value in case of error.

        int (\*disable)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp) \*rsp)
        :   Stream Disable request callback.

            Disable callback is called whenever an Audio Stream is requested to disable the stream.

            Param stream:
            :   **[in]** Stream object being disabled.

            Param rsp:
            :   **[out]** Object for the ASE operation response. Only used if the return value is non-zero.

            Return:
            :   0 in case of success or negative value in case of error.

        int (\*stop)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp) \*rsp)
        :   Stream Stop callback.

            Stop callback is called whenever an Audio Stream is requested to stop streaming.

            Param stream:
            :   **[in]** Stream object.

            Param rsp:
            :   **[out]** Object for the ASE operation response. Only used if the return value is non-zero.

            Return:
            :   0 in case of success or negative value in case of error.

        int (\*release)(struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream, struct [bt\_bap\_ascs\_rsp](#c.bt_bap_ascs_rsp) \*rsp)
        :   Stream release callback.

            Release callback is called whenever a new Audio Stream needs to be released and thus deallocated.

            Param stream:
            :   **[in]** Stream object.

            Param rsp:
            :   **[out]** Object for the ASE operation response. Only used if the return value is non-zero.

            Return:
            :   0 in case of success or negative value in case of error.

*group* BAP Broadcast  APIs
:   BAP Broadcast APIs.

    Functions

    const struct bt\_bap\_base \*bt\_bap\_base\_get\_base\_from\_ad(const struct [bt\_data](../gap.md#c.bt_data "bt_data") \*ad)
    :   Generate a pointer to a BASE from periodic advertising data.

        Parameters:
        :   - **ad** – The periodic advertising data

        Return values:
        :   - **NULL** – if the data does not contain a BASE
            - **Pointer** – to a bt\_bap\_base structure

    int bt\_bap\_base\_get\_size(const struct bt\_bap\_base \*base)
    :   Get the size of a BASE.

        Parameters:
        :   - **base** – The BASE pointer

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **The** – size of the BASE

    int bt\_bap\_base\_get\_pres\_delay(const struct bt\_bap\_base \*base)
    :   Get the presentation delay value of a BASE.

        Parameters:
        :   - **base** – The BASE pointer

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **The** – 24-bit presentation delay value

    int bt\_bap\_base\_get\_subgroup\_count(const struct bt\_bap\_base \*base)
    :   Get the subgroup count of a BASE.

        Parameters:
        :   - **base** – The BASE pointer

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **The** – 8-bit subgroup count value

    int bt\_bap\_base\_get\_bis\_indexes(const struct bt\_bap\_base \*base, uint32\_t \*bis\_indexes)
    :   Get all BIS indexes of a BASE.

        Parameters:
        :   - **base** – **[in]** The BASE pointer
            - **bis\_indexes** – **[out]** 32-bit BIS index bitfield that will be populated

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **0** – on success

    int bt\_bap\_base\_foreach\_subgroup(const struct bt\_bap\_base \*base, bool (\*func)(const struct bt\_bap\_base\_subgroup \*subgroup, void \*user\_data), void \*user\_data)
    :   Iterate on all subgroups in the BASE.

        Parameters:
        :   - **base** – The BASE pointer
            - **func** – Callback function. Return true to continue iterating, or false to stop.
            - **user\_data** – Userdata supplied to `func`

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **-ECANCELED** – if iterating over the subgroups stopped prematurely by `func`
            - **0** – if all subgroups were iterated

    int bt\_bap\_base\_get\_subgroup\_codec\_id(const struct bt\_bap\_base\_subgroup \*subgroup, struct [bt\_bap\_base\_codec\_id](#c.bt_bap_base_codec_id) \*codec\_id)
    :   Get the codec ID of a subgroup.

        Parameters:
        :   - **subgroup** – **[in]** The subgroup pointer
            - **codec\_id** – **[out]** Pointer to the struct where the results are placed

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **0** – on success

    int bt\_bap\_base\_get\_subgroup\_codec\_data(const struct bt\_bap\_base\_subgroup \*subgroup, uint8\_t \*\*data)
    :   Get the codec configuration data of a subgroup.

        Parameters:
        :   - **subgroup** – **[in]** The subgroup pointer
            - **data** – **[out]** Pointer that will point to the resulting codec configuration data

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **0** – on success

    int bt\_bap\_base\_get\_subgroup\_codec\_meta(const struct bt\_bap\_base\_subgroup \*subgroup, uint8\_t \*\*meta)
    :   Get the codec metadata of a subgroup.

        Parameters:
        :   - **subgroup** – **[in]** The subgroup pointer
            - **meta** – **[out]** Pointer that will point to the resulting codec metadata

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **0** – on success

    int bt\_bap\_base\_subgroup\_codec\_to\_codec\_cfg(const struct bt\_bap\_base\_subgroup \*subgroup, struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg)
    :   Store subgroup codec data in a [Codec config parsing APIs](audio.md#group__bt__audio__codec__cfg).

        Parameters:
        :   - **subgroup** – **[in]** The subgroup pointer
            - **codec\_cfg** – **[out]** Pointer to the struct where the results are placed

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the `codec_cfg` cannot store the `subgroup` codec data
            - **0** – on success

    int bt\_bap\_base\_get\_subgroup\_bis\_count(const struct bt\_bap\_base\_subgroup \*subgroup)
    :   Get the BIS count of a subgroup.

        Parameters:
        :   - **subgroup** – The subgroup pointer

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **The** – 8-bit BIS count value

    int bt\_bap\_base\_subgroup\_get\_bis\_indexes(const struct bt\_bap\_base\_subgroup \*subgroup, uint32\_t \*bis\_indexes)
    :   Get all BIS indexes of a subgroup.

        Parameters:
        :   - **subgroup** – **[in]** The subgroup pointer
            - **bis\_indexes** – **[out]** 32-bit BIS index bitfield that will be populated

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **0** – on success

    int bt\_bap\_base\_subgroup\_foreach\_bis(const struct bt\_bap\_base\_subgroup \*subgroup, bool (\*func)(const struct [bt\_bap\_base\_subgroup\_bis](#c.bt_bap_base_subgroup_bis) \*bis, void \*user\_data), void \*user\_data)
    :   Iterate on all BIS in the subgroup.

        Parameters:
        :   - **subgroup** – The subgroup pointer
            - **func** – Callback function. Return true to continue iterating, or false to stop.
            - **user\_data** – Userdata supplied to `func`

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **-ECANCELED** – if iterating over the subgroups stopped prematurely by `func`
            - **0** – if all BIS were iterated

    int bt\_bap\_base\_subgroup\_bis\_codec\_to\_codec\_cfg(const struct [bt\_bap\_base\_subgroup\_bis](#c.bt_bap_base_subgroup_bis) \*bis, struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg)
    :   Store BIS codec configuration data in a [Codec config parsing APIs](audio.md#group__bt__audio__codec__cfg).

        This only sets the [Codec config parsing APIs](audio.md#group__bt__audio__codec__cfg) data and [Codec config parsing APIs](audio.md#group__bt__audio__codec__cfg) data\_len, but is useful to use the BIS codec configuration data with the bt\_audio\_codec\_cfg\_\* functions.

        Parameters:
        :   - **bis** – **[in]** The BIS pointer
            - **codec\_cfg** – **[out]** Pointer to the struct where the results are placed

        Return values:
        :   - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the `codec_cfg` cannot store the `subgroup` codec data
            - **0** – on success

    struct bt\_bap\_base\_codec\_id
    :   *#include <bap.h>*

        Codec ID structure for a Broadcast Audio Source Endpoint (BASE).

        Public Members

        uint8\_t id
        :   Codec ID.

        uint16\_t cid
        :   Codec Company ID.

        uint16\_t vid
        :   Codec Company Vendor ID.

    struct bt\_bap\_base\_subgroup\_bis
    :   *#include <bap.h>*

        BIS structure for each BIS in a Broadcast Audio Source Endpoint (BASE) subgroup.

        Public Members

        uint8\_t index
        :   Unique index of the BIS.

        uint8\_t data\_len
        :   Codec Specific Data length.

        uint8\_t \*data
        :   Codec Specific Data.

*group* BAP Broadcast Sink APIs
:   BAP Broadcast Sink APIs.

    Functions

    int bt\_bap\_broadcast\_sink\_register\_cb(struct [bt\_bap\_broadcast\_sink\_cb](#c.bt_bap_broadcast_sink_cb) \*cb)
    :   Register Broadcast sink callbacks.

        It is possible to register multiple struct of callbacks, but a single struct can only be registered once. Registering the same callback multiple times is undefined behavior and may break the stack.

        Parameters:
        :   - **cb** – Broadcast sink callback structure.

        Return values:
        :   - **0** – in case of success
            - **-EINVAL** – if `cb` is NULL

    int bt\_bap\_broadcast\_sink\_create(struct bt\_le\_per\_adv\_sync \*pa\_sync, uint32\_t broadcast\_id, struct bt\_bap\_broadcast\_sink \*\*sink)
    :   Create a Broadcast Sink from a periodic advertising sync.

        This should only be done after verifying that the periodic advertising sync is from a Broadcast Source.

        The created Broadcast Sink will need to be supplied to [bt\_bap\_broadcast\_sink\_sync()](#group__bt__bap__broadcast__sink_1ga3485ef8527928209274ae0b5351b72b3) in order to synchronize to the broadcast audio.

        bt\_bap\_broadcast\_sink\_cb.pa\_synced() will be called with the Broadcast Sink object created if this is successful.

        Parameters:
        :   - **pa\_sync** – Pointer to the periodic advertising sync object.
            - **broadcast\_id** – 24-bit broadcast ID.
            - **sink** – **[out]** Pointer to the Broadcast Sink created.

        Returns:
        :   0 in case of success or errno value in case of error.

    int bt\_bap\_broadcast\_sink\_sync(struct bt\_bap\_broadcast\_sink \*sink, uint32\_t indexes\_bitfield, struct [bt\_bap\_stream](#c.bt_bap_stream) \*streams[], const uint8\_t broadcast\_code[16])
    :   Sync to a broadcaster’s audio.

        Example: The string “Broadcast Code” shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

        Parameters:
        :   - **sink** – Pointer to the sink object from the base\_recv callback.
            - **indexes\_bitfield** – Bitfield of the BIS index to sync to. To sync to e.g. BIS index 1 and 2, this should have the value of [BIT(1)](../../../../kernel/util/index.md#group__sys-util_1ga3a8ea58898cb58fc96013383d39f482c) | [BIT(2)](../../../../kernel/util/index.md#group__sys-util_1ga3a8ea58898cb58fc96013383d39f482c).
            - **streams** – Stream object pointers to be used for the receiver. If multiple BIS indexes shall be synchronized, multiple streams shall be provided.
            - **broadcast\_code** – The 16-octet broadcast code. Shall be supplied if the broadcast is encrypted (see [bt\_bap\_broadcast\_sink\_cb::syncable](#structbt__bap__broadcast__sink__cb_1a23390a63acbcf831a177a550d1012047)). If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_bap\_broadcast\_sink\_stop(struct bt\_bap\_broadcast\_sink \*sink)
    :   Stop audio broadcast sink.

        Stop an audio broadcast sink. The broadcast sink will stop receiving BIGInfo, and audio data can no longer be streamed.

        Parameters:
        :   - **sink** – Pointer to the broadcast sink

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_broadcast\_sink\_delete(struct bt\_bap\_broadcast\_sink \*sink)
    :   Release a broadcast sink.

        Once a broadcast sink has been allocated after the pa\_synced callback, it can be deleted using this function. If the sink has synchronized to any broadcast audio streams, these must first be stopped using bt\_bap\_stream\_stop.

        Parameters:
        :   - **sink** – Pointer to the sink object to delete.

        Returns:
        :   0 in case of success or negative value in case of error.

    struct bt\_bap\_broadcast\_sink\_cb
    :   *#include <bap.h>*

        Broadcast Audio Sink callback structure.

        Public Members

        void (\*base\_recv)(struct bt\_bap\_broadcast\_sink \*sink, const struct bt\_bap\_base \*base, size\_t base\_size)
        :   Broadcast Audio Source Endpoint (BASE) received.

            Callback for when we receive a BASE from a broadcaster after syncing to the broadcaster’s periodic advertising.

            Param sink:
            :   Pointer to the sink structure.

            Param base:
            :   Broadcast Audio Source Endpoint (BASE).

            Param base\_size:
            :   Size of the `base`

        void (\*syncable)(struct bt\_bap\_broadcast\_sink \*sink, const struct bt\_iso\_biginfo \*biginfo)
        :   Broadcast sink is syncable.

            Called whenever a broadcast sink is not synchronized to audio, but the audio is synchronizable. This is inferred when a BIGInfo report is received.

            Once this callback has been called, it is possible to call [bt\_bap\_broadcast\_sink\_sync()](#group__bt__bap__broadcast__sink_1ga3485ef8527928209274ae0b5351b72b3) to synchronize to the audio stream(s).

            Param sink:
            :   Pointer to the sink structure.

            Param biginfo:
            :   The BIGInfo report.

*group* BAP Broadcast Source APIs
:   BAP Broadcast Source APIs.

    Functions

    int bt\_bap\_broadcast\_source\_create(struct [bt\_bap\_broadcast\_source\_param](#c.bt_bap_broadcast_source_param) \*param, struct bt\_bap\_broadcast\_source \*\*source)
    :   Create audio broadcast source.

        Create a new audio broadcast source with one or more audio streams.

        The broadcast source will be visible for scanners once this has been called, and the device will advertise audio announcements.

        No audio data can be sent until [bt\_bap\_broadcast\_source\_start()](#group__bt__bap__broadcast__source_1gac4640f5207599d51c1a63ff47f3c1d5a) has been called and no audio information (BIGInfo) will be visible to scanners (see [bt\_le\_per\_adv\_sync\_cb](../gap.md#structbt__le__per__adv__sync__cb)).

        Parameters:
        :   - **param** – **[in]** Pointer to parameters used to create the broadcast source.
            - **source** – **[out]** Pointer to the broadcast source created

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_broadcast\_source\_reconfig(struct bt\_bap\_broadcast\_source \*source, struct [bt\_bap\_broadcast\_source\_param](#c.bt_bap_broadcast_source_param) \*param)
    :   Reconfigure audio broadcast source.

        Reconfigure an audio broadcast source with a new codec and codec quality of service parameters. This can only be done when the source is stopped.

        Since this may modify the Broadcast Audio Source Endpoint (BASE), [bt\_bap\_broadcast\_source\_get\_base()](#group__bt__bap__broadcast__source_1gafe07e4c6962858500fcf66415a173be8) should be called after this to get the new BASE information.

        If the `param.params_count` is smaller than the number of subgroups that have been created in the Broadcast Source, only the first `param.params_count` subgroups are updated. If a stream exist in a subgroup not part of `param`, then that stream is left as is (i.e. it is not removed; the only way to remove a stream from a Broadcast Source is to recreate the Broadcast Source).

        Parameters:
        :   - **source** – Pointer to the broadcast source
            - **param** – Pointer to parameters used to reconfigure the broadcast source.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_broadcast\_source\_update\_metadata(struct bt\_bap\_broadcast\_source \*source, const uint8\_t meta[], size\_t meta\_len)
    :   Modify the metadata of an audio broadcast source.

        Modify the metadata an audio broadcast source. This can only be done when the source is started. To update the metadata in the stopped state, use [bt\_bap\_broadcast\_source\_reconfig()](#group__bt__bap__broadcast__source_1gabecaa9db7be5cb03ed997ba478878d40).

        Parameters:
        :   - **source** – Pointer to the broadcast source.
            - **meta** – Metadata.
            - **meta\_len** – Length of metadata.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_broadcast\_source\_start(struct bt\_bap\_broadcast\_source \*source, struct bt\_le\_ext\_adv \*adv)
    :   Start audio broadcast source.

        Start an audio broadcast source with one or more audio streams. The broadcast source will start advertising BIGInfo, and audio data can be streamed.

        Parameters:
        :   - **source** – Pointer to the broadcast source
            - **adv** – Pointer to an extended advertising set with periodic advertising configured.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_broadcast\_source\_stop(struct bt\_bap\_broadcast\_source \*source)
    :   Stop audio broadcast source.

        Stop an audio broadcast source. The broadcast source will stop advertising BIGInfo, and audio data can no longer be streamed.

        Parameters:
        :   - **source** – Pointer to the broadcast source

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_broadcast\_source\_delete(struct bt\_bap\_broadcast\_source \*source)
    :   Delete audio broadcast source.

        Delete an audio broadcast source. The broadcast source will stop advertising entirely, and the source can no longer be used.

        Parameters:
        :   - **source** – Pointer to the broadcast source

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_broadcast\_source\_get\_id(struct bt\_bap\_broadcast\_source \*source, uint32\_t \*const broadcast\_id)
    :   Get the broadcast ID of a broadcast source.

        This will return the 3-octet broadcast ID that should be advertised in the extended advertising data with [BT\_UUID\_BROADCAST\_AUDIO\_VAL](../uuid.md#group__bt__uuid_1ga0c67f9e1a5fef34fd1fddc539e20119b) as [BT\_DATA\_SVC\_DATA16](../gap.md#group__bt__gap__defines_1ga76990dda919688b369decaf9d3606b32).

        See table 3.14 in the Basic Audio Profile v1.0.1 for the structure.

        Parameters:
        :   - **source** – **[in]** Pointer to the broadcast source.
            - **broadcast\_id** – **[out]** Pointer to the 3-octet broadcast ID.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_bap\_broadcast\_source\_get\_base(struct bt\_bap\_broadcast\_source \*source, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*base\_buf)
    :   Get the Broadcast Audio Stream Endpoint of a broadcast source.

        This will encode the BASE of a broadcast source into a buffer, that can be used for advertisement. The encoded BASE will thus be encoded as little-endian. The BASE shall be put into the periodic advertising data (see [bt\_le\_per\_adv\_set\_data()](../gap.md#group__bt__gap_1gafd0e7ccca93a8347a4ca6cca88e77899)).

        See table 3.15 in the Basic Audio Profile v1.0.1 for the structure.

        Parameters:
        :   - **source** – Pointer to the broadcast source.
            - **base\_buf** – Pointer to a buffer where the BASE will be inserted.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    struct bt\_bap\_broadcast\_source\_stream\_param
    :   *#include <bap.h>*

        Broadcast Source stream parameters.

        Public Members

        struct [bt\_bap\_stream](#c.bt_bap_stream) \*stream
        :   Audio stream.

        size\_t data\_len
        :   The number of elements in the `data` array.

            The BIS specific data may be omitted and this set to 0.

        uint8\_t \*data
        :   BIS Codec Specific Configuration.

    struct bt\_bap\_broadcast\_source\_subgroup\_param
    :   *#include <bap.h>*

        Broadcast Source subgroup parameters.

        Public Members

        size\_t params\_count
        :   The number of parameters in `stream_params`.

        struct [bt\_bap\_broadcast\_source\_stream\_param](#c.bt_bap_broadcast_source_stream_param) \*params
        :   Array of stream parameters.

        struct [bt\_audio\_codec\_cfg](audio.md#c.bt_audio_codec_cfg "bt_audio_codec_cfg") \*codec\_cfg
        :   Subgroup Codec configuration.

    struct bt\_bap\_broadcast\_source\_param
    :   *#include <bap.h>*

        Broadcast Source create parameters.

        Public Members

        size\_t params\_count
        :   The number of parameters in `subgroup_params`.

        struct [bt\_bap\_broadcast\_source\_subgroup\_param](#c.bt_bap_broadcast_source_subgroup_param) \*params
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

        uint8\_t broadcast\_code[16]
        :   Broadcast code.

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
