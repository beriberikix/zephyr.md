---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/connection_mgmt.html
original_path: connectivity/bluetooth/api/connection_mgmt.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Connection Management

The Zephyr Bluetooth stack uses an abstraction called `bt_conn`
to represent connections to other devices. The internals of this struct
are not exposed to the application, but a limited amount of information
(such as the remote address) can be acquired using the
[`bt_conn_get_info()`](#c.bt_conn_get_info) API. Connection objects are reference
counted, and the application is expected to use the
[`bt_conn_ref()`](#c.bt_conn_ref) API whenever storing a connection pointer for a
longer period of time, since this ensures that the object remains valid
(even if the connection would get disconnected). Similarly the
[`bt_conn_unref()`](#c.bt_conn_unref) API is to be used when releasing a reference
to a connection.

An application may track connections by registering a
[`bt_conn_cb`](#c.bt_conn_cb) struct using the [`bt_conn_cb_register()`](#c.bt_conn_cb_register)
or [`BT_CONN_CB_DEFINE`](#c.BT_CONN_CB_DEFINE) APIs. This struct lets the application
define callbacks for connection & disconnection events, as well as other
events related to a connection such as a change in the security level or
the connection parameters. When acting as a central the application will
also get hold of the connection object through the return value of the
[`bt_conn_le_create()`](#c.bt_conn_le_create) API.

## API Reference

*group* bt\_conn
:   Connection management.

    Defines

    BT\_LE\_CONN\_PARAM\_INIT(int\_min, int\_max, lat, to)
    :   Initialize connection parameters.

        Parameters:
        :   - **int\_min** – Minimum Connection Interval (N \* 1.25 ms)
            - **int\_max** – Maximum Connection Interval (N \* 1.25 ms)
            - **lat** – Connection Latency
            - **to** – Supervision Timeout (N \* 10 ms)

    BT\_LE\_CONN\_PARAM(int\_min, int\_max, lat, to)
    :   Helper to declare connection parameters inline.

        Parameters:
        :   - **int\_min** – Minimum Connection Interval (N \* 1.25 ms)
            - **int\_max** – Maximum Connection Interval (N \* 1.25 ms)
            - **lat** – Connection Latency
            - **to** – Supervision Timeout (N \* 10 ms)

    BT\_LE\_CONN\_PARAM\_DEFAULT
    :   Default LE connection parameters: Connection Interval: 30-50 ms Latency: 0 Timeout: 4 s.

    BT\_CONN\_LE\_PHY\_PARAM\_INIT(\_pref\_tx\_phy, \_pref\_rx\_phy)
    :   Initialize PHY parameters.

        Parameters:
        :   - **\_pref\_tx\_phy** – Bitmask of preferred transmit PHYs.
            - **\_pref\_rx\_phy** – Bitmask of preferred receive PHYs.

    BT\_CONN\_LE\_PHY\_PARAM(\_pref\_tx\_phy, \_pref\_rx\_phy)
    :   Helper to declare PHY parameters inline.

        Parameters:
        :   - **\_pref\_tx\_phy** – Bitmask of preferred transmit PHYs.
            - **\_pref\_rx\_phy** – Bitmask of preferred receive PHYs.

    BT\_CONN\_LE\_PHY\_PARAM\_1M
    :   Only LE 1M PHY.

    BT\_CONN\_LE\_PHY\_PARAM\_2M
    :   Only LE 2M PHY.

    BT\_CONN\_LE\_PHY\_PARAM\_CODED
    :   Only LE Coded PHY.

    BT\_CONN\_LE\_PHY\_PARAM\_ALL
    :   All LE PHYs.

    BT\_CONN\_LE\_DATA\_LEN\_PARAM\_INIT(\_tx\_max\_len, \_tx\_max\_time)
    :   Initialize transmit data length parameters.

        Parameters:
        :   - **\_tx\_max\_len** – Maximum Link Layer transmission payload size in bytes.
            - **\_tx\_max\_time** – Maximum Link Layer transmission payload time in us.

    BT\_CONN\_LE\_DATA\_LEN\_PARAM(\_tx\_max\_len, \_tx\_max\_time)
    :   Helper to declare transmit data length parameters inline.

        Parameters:
        :   - **\_tx\_max\_len** – Maximum Link Layer transmission payload size in bytes.
            - **\_tx\_max\_time** – Maximum Link Layer transmission payload time in us.

    BT\_LE\_DATA\_LEN\_PARAM\_DEFAULT
    :   Default LE data length parameters.

    BT\_LE\_DATA\_LEN\_PARAM\_MAX
    :   Maximum LE data length parameters.

    BT\_CONN\_INTERVAL\_TO\_MS(interval)
    :   Convert connection interval to milliseconds.

        Multiply by 1.25 to get milliseconds.

        Note that this may be inaccurate, as something like 7.5 ms cannot be accurately presented with integers.

    BT\_CONN\_INTERVAL\_TO\_US(interval)
    :   Convert connection interval to microseconds.

        Multiply by 1250 to get microseconds.

    BT\_CONN\_ROLE\_MASTER
    :   Connection role (central or peripheral).

    BT\_CONN\_ROLE\_SLAVE

    BT\_CONN\_LE\_CREATE\_PARAM\_INIT(\_options, \_interval, \_window)
    :   Initialize create connection parameters.

        Parameters:
        :   - **\_options** – Create connection options.
            - **\_interval** – Create connection scan interval (N \* 0.625 ms).
            - **\_window** – Create connection scan window (N \* 0.625 ms).

    BT\_CONN\_LE\_CREATE\_PARAM(\_options, \_interval, \_window)
    :   Helper to declare create connection parameters inline.

        Parameters:
        :   - **\_options** – Create connection options.
            - **\_interval** – Create connection scan interval (N \* 0.625 ms).
            - **\_window** – Create connection scan window (N \* 0.625 ms).

    BT\_CONN\_LE\_CREATE\_CONN
    :   Default LE create connection parameters.

        Scan continuously by setting scan interval equal to scan window.

    BT\_CONN\_LE\_CREATE\_CONN\_AUTO
    :   Default LE create connection using filter accept list parameters.

        Scan window: 30 ms. Scan interval: 60 ms.

    BT\_CONN\_CB\_DEFINE(\_name)
    :   Register a callback structure for connection events.

        Parameters:
        :   - **\_name** – Name of callback structure.

    BT\_PASSKEY\_INVALID
    :   Special passkey value that can be used to disable a previously set fixed passkey.

    BT\_BR\_CONN\_PARAM\_INIT(role\_switch)
    :   Initialize BR/EDR connection parameters.

        Parameters:
        :   - **role\_switch** – True if role switch is allowed

    BT\_BR\_CONN\_PARAM(role\_switch)
    :   Helper to declare BR/EDR connection parameters inline.

        Parameters:
        :   - **role\_switch** – True if role switch is allowed

    BT\_BR\_CONN\_PARAM\_DEFAULT
    :   Default BR/EDR connection parameters: Role switch allowed.

    Enums

    enum [anonymous]
    :   Connection PHY options.

        *Values:*

        enumerator BT\_CONN\_LE\_PHY\_OPT\_NONE = 0
        :   Convenience value when no options are specified.

        enumerator BT\_CONN\_LE\_PHY\_OPT\_CODED\_S2 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   LE Coded using S=2 coding preferred when transmitting.

        enumerator BT\_CONN\_LE\_PHY\_OPT\_CODED\_S8 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   LE Coded using S=8 coding preferred when transmitting.

    enum bt\_conn\_type
    :   Connection Type.

        *Values:*

        enumerator BT\_CONN\_TYPE\_LE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   LE Connection Type.

        enumerator BT\_CONN\_TYPE\_BR = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   BR/EDR Connection Type.

        enumerator BT\_CONN\_TYPE\_SCO = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   SCO Connection Type.

        enumerator BT\_CONN\_TYPE\_ISO = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   ISO Connection Type.

        enumerator BT\_CONN\_TYPE\_ALL = [BT\_CONN\_TYPE\_LE](#c.bt_conn_type.BT_CONN_TYPE_LE) | [BT\_CONN\_TYPE\_BR](#c.bt_conn_type.BT_CONN_TYPE_BR) | [BT\_CONN\_TYPE\_SCO](#c.bt_conn_type.BT_CONN_TYPE_SCO) | [BT\_CONN\_TYPE\_ISO](#c.bt_conn_type.BT_CONN_TYPE_ISO)
        :   All Connection Type.

    enum [anonymous]
    :   *Values:*

        enumerator BT\_CONN\_ROLE\_CENTRAL = 0

        enumerator BT\_CONN\_ROLE\_PERIPHERAL = 1

    enum bt\_conn\_state
    :   *Values:*

        enumerator BT\_CONN\_STATE\_DISCONNECTED
        :   Channel disconnected.

        enumerator BT\_CONN\_STATE\_CONNECTING
        :   Channel in connecting state.

        enumerator BT\_CONN\_STATE\_CONNECTED
        :   Channel connected and ready for upper layer traffic on it.

        enumerator BT\_CONN\_STATE\_DISCONNECTING
        :   Channel in disconnecting state.

    enum bt\_security\_t
    :   Security level.

        *Values:*

        enumerator BT\_SECURITY\_L0
        :   Level 0: Only for BR/EDR special cases, like SDP.

        enumerator BT\_SECURITY\_L1
        :   Level 1: No encryption and no authentication.

        enumerator BT\_SECURITY\_L2
        :   Level 2: Encryption and no authentication (no MITM).

        enumerator BT\_SECURITY\_L3
        :   Level 3: Encryption and authentication (MITM).

        enumerator BT\_SECURITY\_L4
        :   Level 4: Authenticated Secure Connections and 128-bit key.

        enumerator BT\_SECURITY\_FORCE\_PAIR = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(7)
        :   Bit to force new pairing procedure, bit-wise OR with requested security level.

    enum bt\_security\_flag
    :   Security Info Flags.

        *Values:*

        enumerator BT\_SECURITY\_FLAG\_SC = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Paired with Secure Connections.

        enumerator BT\_SECURITY\_FLAG\_OOB = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Paired with Out of Band method.

    enum bt\_conn\_le\_tx\_power\_phy
    :   *Values:*

        enumerator BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE
        :   Convenience macro for when no PHY is set.

        enumerator BT\_CONN\_LE\_TX\_POWER\_PHY\_1M
        :   LE 1M PHY.

        enumerator BT\_CONN\_LE\_TX\_POWER\_PHY\_2M
        :   LE 2M PHY.

        enumerator BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8
        :   LE Coded PHY using S=8 coding.

        enumerator BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2
        :   LE Coded PHY using S=2 coding.

    enum bt\_conn\_auth\_keypress
    :   Passkey Keypress Notification type.

        The numeric values are the same as in the Core specification for Pairing Keypress Notification PDU.

        *Values:*

        enumerator BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED = 0x00

        enumerator BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED = 0x01

        enumerator BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED = 0x02

        enumerator BT\_CONN\_AUTH\_KEYPRESS\_CLEARED = 0x03

        enumerator BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED = 0x04

    enum [anonymous]
    :   *Values:*

        enumerator BT\_CONN\_LE\_OPT\_NONE = 0
        :   Convenience value when no options are specified.

        enumerator BT\_CONN\_LE\_OPT\_CODED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Enable LE Coded PHY.

            Enable scanning on the LE Coded PHY.

        enumerator BT\_CONN\_LE\_OPT\_NO\_1M = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Disable LE 1M PHY.

            Disable scanning on the LE 1M PHY.

            Note

            Requires [BT\_CONN\_LE\_OPT\_CODED](#group__bt__conn_1gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b).

    enum bt\_security\_err
    :   *Values:*

        enumerator BT\_SECURITY\_ERR\_SUCCESS
        :   Security procedure successful.

        enumerator BT\_SECURITY\_ERR\_AUTH\_FAIL
        :   Authentication failed.

        enumerator BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING
        :   PIN or encryption key is missing.

        enumerator BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE
        :   OOB data is not available.

        enumerator BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT
        :   The requested security level could not be reached.

        enumerator BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED
        :   Pairing is not supported.

        enumerator BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED
        :   Pairing is not allowed.

        enumerator BT\_SECURITY\_ERR\_INVALID\_PARAM
        :   Invalid parameters.

        enumerator BT\_SECURITY\_ERR\_KEY\_REJECTED
        :   Distributed Key Rejected.

        enumerator BT\_SECURITY\_ERR\_UNSPECIFIED
        :   Pairing failed but the exact reason could not be specified.

    Functions

    struct bt\_conn \*bt\_conn\_ref(struct bt\_conn \*conn)
    :   Increment a connection’s reference count.

        Increment the reference count of a connection object.

        Note

        Will return NULL if the reference count is zero.

        Parameters:
        :   - **conn** – Connection object.

        Returns:
        :   Connection object with incremented reference count, or NULL if the reference count is zero.

    void bt\_conn\_unref(struct bt\_conn \*conn)
    :   Decrement a connection’s reference count.

        Decrement the reference count of a connection object.

        Parameters:
        :   - **conn** – Connection object.

    void bt\_conn\_foreach(enum [bt\_conn\_type](#c.bt_conn_type) type, void (\*func)(struct bt\_conn \*conn, void \*data), void \*data)
    :   Iterate through all bt\_conn objects.

        Iterates trough all bt\_conn objects that are alive in the Host allocator.

        To find established connections, combine this with [bt\_conn\_get\_info](#group__bt__conn_1ga2de54f2ac83f0d8dca2a85a9fbfadcaa). Check that [bt\_conn\_info::state](#structbt__conn__info_1ae566e2382b69ff27314dc1dd632dbdbc) is [BT\_CONN\_STATE\_CONNECTED](#group__bt__conn_1gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f).

        Thread safety: This API is thread safe, but it does not guarantee a sequentially-consistent view for objects allocated during the current invocation of this API. E.g. If preempted while allocations A then B then C happen then results may include A and C but miss B.

        Parameters:
        :   - **type** – Connection Type
            - **func** – Function to call for each connection.
            - **data** – Data to pass to the callback function.

    struct bt\_conn \*bt\_conn\_lookup\_addr\_le(uint8\_t id, const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*peer)
    :   Look up an existing connection by address.

        Look up an existing connection based on the remote address.

        The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#group__bt__conn_1ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

        Parameters:
        :   - **id** – Local identity (in most cases BT\_ID\_DEFAULT).
            - **peer** – Remote address.

        Returns:
        :   Connection object or NULL if not found.

    const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*bt\_conn\_get\_dst(const struct bt\_conn \*conn)
    :   Get destination (peer) address of a connection.

        Parameters:
        :   - **conn** – Connection object.

        Returns:
        :   Destination address.

    uint8\_t bt\_conn\_index(const struct bt\_conn \*conn)
    :   Get array index of a connection.

        This function is used to map bt\_conn to index of an array of connections. The array has CONFIG\_BT\_MAX\_CONN elements.

        Parameters:
        :   - **conn** – Connection object.

        Returns:
        :   Index of the connection object. The range of the returned value is 0..CONFIG\_BT\_MAX\_CONN-1

    int bt\_conn\_get\_info(const struct bt\_conn \*conn, struct [bt\_conn\_info](#c.bt_conn_info) \*info)
    :   Get connection info.

        Parameters:
        :   - **conn** – Connection object.
            - **info** – Connection info object.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_get\_remote\_info(struct bt\_conn \*conn, struct [bt\_conn\_remote\_info](#c.bt_conn_remote_info) \*remote\_info)
    :   Get connection info for the remote device.

        Note

        In order to retrieve the remote version (version, manufacturer and subversion)  [`CONFIG_BT_REMOTE_VERSION`](../../../kconfig.md#CONFIG_BT_REMOTE_VERSION "CONFIG_BT_REMOTE_VERSION") must be enabled

        Note

        The remote information is exchanged directly after the connection has been established. The application can be notified about when the remote information is available through the remote\_info\_available callback.

        Parameters:
        :   - **conn** – Connection object.
            - **remote\_info** – Connection remote info object.

        Returns:
        :   Zero on success or (negative) error code on failure.

        Returns:
        :   -EBUSY The remote information is not yet available.

    int bt\_conn\_le\_get\_tx\_power\_level(struct bt\_conn \*conn, struct [bt\_conn\_le\_tx\_power](#c.bt_conn_le_tx_power) \*tx\_power\_level)
    :   Get connection transmit power level.

        Parameters:
        :   - **conn** – Connection object.
            - **tx\_power\_level** – Transmit power level descriptor.

        Returns:
        :   Zero on success or (negative) error code on failure.

        Returns:
        :   -ENOBUFS HCI command buffer is not available.

    int bt\_conn\_le\_enhanced\_get\_tx\_power\_level(struct bt\_conn \*conn, struct [bt\_conn\_le\_tx\_power](#c.bt_conn_le_tx_power) \*tx\_power)
    :   Get local enhanced connection transmit power level.

        Parameters:
        :   - **conn** – Connection object.
            - **tx\_power** – Transmit power level descriptor.

        Return values:
        :   **-ENOBUFS** – HCI command buffer is not available.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_le\_get\_remote\_tx\_power\_level(struct bt\_conn \*conn, enum [bt\_conn\_le\_tx\_power\_phy](#c.bt_conn_le_tx_power_phy) phy)
    :   Get remote (peer) transmit power level.

        Parameters:
        :   - **conn** – Connection object.
            - **phy** – PHY information.

        Return values:
        :   **-ENOBUFS** – HCI command buffer is not available.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_le\_set\_tx\_power\_report\_enable(struct bt\_conn \*conn, bool local\_enable, bool remote\_enable)
    :   Enable transmit power reporting.

        Parameters:
        :   - **conn** – Connection object.
            - **local\_enable** – Enable/disable reporting for local.
            - **remote\_enable** – Enable/disable reporting for remote.

        Return values:
        :   **-ENOBUFS** – HCI command buffer is not available.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_le\_param\_update(struct bt\_conn \*conn, const struct [bt\_le\_conn\_param](#c.bt_le_conn_param) \*param)
    :   Update the connection parameters.

        If the local device is in the peripheral role then updating the connection parameters will be delayed. This delay can be configured by through the  [`CONFIG_BT_CONN_PARAM_UPDATE_TIMEOUT`](../../../kconfig.md#CONFIG_BT_CONN_PARAM_UPDATE_TIMEOUT "CONFIG_BT_CONN_PARAM_UPDATE_TIMEOUT") option.

        Parameters:
        :   - **conn** – Connection object.
            - **param** – Updated connection parameters.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_le\_data\_len\_update(struct bt\_conn \*conn, const struct [bt\_conn\_le\_data\_len\_param](#c.bt_conn_le_data_len_param) \*param)
    :   Update the connection transmit data length parameters.

        Parameters:
        :   - **conn** – Connection object.
            - **param** – Updated data length parameters.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_le\_phy\_update(struct bt\_conn \*conn, const struct [bt\_conn\_le\_phy\_param](#c.bt_conn_le_phy_param) \*param)
    :   Update the connection PHY parameters.

        Update the preferred transmit and receive PHYs of the connection. Use [BT\_GAP\_LE\_PHY\_NONE](gap.md#group__bt__gap__defines_1gga7dc8e89251aa575e28331e05775ba20baaf7e1b40f6464a603e5116db269cacab) to indicate no preference.

        Parameters:
        :   - **conn** – Connection object.
            - **param** – Updated connection parameters.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_disconnect(struct bt\_conn \*conn, uint8\_t reason)
    :   Disconnect from a remote device or cancel pending connection.

        Disconnect an active connection with the specified reason code or cancel pending outgoing connection.

        The disconnect reason for a normal disconnect should be: BT\_HCI\_ERR\_REMOTE\_USER\_TERM\_CONN.

        The following disconnect reasons are accepted:

        - BT\_HCI\_ERR\_AUTH\_FAIL
        - BT\_HCI\_ERR\_REMOTE\_USER\_TERM\_CONN
        - BT\_HCI\_ERR\_REMOTE\_LOW\_RESOURCES
        - BT\_HCI\_ERR\_REMOTE\_POWER\_OFF
        - BT\_HCI\_ERR\_UNSUPP\_REMOTE\_FEATURE
        - BT\_HCI\_ERR\_PAIRING\_NOT\_SUPPORTED
        - BT\_HCI\_ERR\_UNACCEPT\_CONN\_PARAM

        Parameters:
        :   - **conn** – Connection to disconnect.
            - **reason** – Reason code for the disconnection.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_le\_create(const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*peer, const struct [bt\_conn\_le\_create\_param](#c.bt_conn_le_create_param) \*create\_param, const struct [bt\_le\_conn\_param](#c.bt_le_conn_param) \*conn\_param, struct bt\_conn \*\*conn)
    :   Initiate an LE connection to a remote device.

        Allows initiate new LE link to remote peer using its address.

        The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#group__bt__conn_1ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

        This uses the General Connection Establishment procedure.

        The application must disable explicit scanning before initiating a new LE connection.

        Parameters:
        :   - **peer** – **[in]** Remote address.
            - **create\_param** – **[in]** Create connection parameters.
            - **conn\_param** – **[in]** Initial connection parameters.
            - **conn** – **[out]** Valid connection object on success.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_le\_create\_synced(const struct bt\_le\_ext\_adv \*adv, const struct [bt\_conn\_le\_create\_synced\_param](#c.bt_conn_le_create_synced_param) \*synced\_param, const struct [bt\_le\_conn\_param](#c.bt_le_conn_param) \*conn\_param, struct bt\_conn \*\*conn)
    :   Create a connection to a synced device.

        Initiate a connection to a synced device from a Periodic Advertising with Responses (PAwR) train.

        The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#group__bt__conn_1ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

        This uses the Periodic Advertising Connection Procedure.

        Parameters:
        :   - **adv** – **[in]** The adverting set the PAwR advertiser belongs to.
            - **synced\_param** – **[in]** Create connection parameters.
            - **conn\_param** – **[in]** Initial connection parameters.
            - **conn** – **[out]** Valid connection object on success.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_conn\_le\_create\_auto(const struct [bt\_conn\_le\_create\_param](#c.bt_conn_le_create_param) \*create\_param, const struct [bt\_le\_conn\_param](#c.bt_le_conn_param) \*conn\_param)
    :   Automatically connect to remote devices in the filter accept list.

        This uses the Auto Connection Establishment procedure. The procedure will continue until a single connection is established or the procedure is stopped through [bt\_conn\_create\_auto\_stop](#group__bt__conn_1ga62dc2663b4fa39a33adb76dc9a136aa4). To establish connections to all devices in the the filter accept list the procedure should be started again in the connected callback after a new connection has been established.

        Parameters:
        :   - **create\_param** – Create connection parameters
            - **conn\_param** – Initial connection parameters.

        Returns:
        :   Zero on success or (negative) error code on failure.

        Returns:
        :   -ENOMEM No free connection object available.

    int bt\_conn\_create\_auto\_stop(void)
    :   Stop automatic connect creation.

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_le\_set\_auto\_conn(const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*addr, const struct [bt\_le\_conn\_param](#c.bt_le_conn_param) \*param)
    :   Automatically connect to remote device if it’s in range.

        This function enables/disables automatic connection initiation. Every time the device loses the connection with peer, this connection will be re-established if connectable advertisement from peer is received.

        Note

        Auto connect is disabled during explicit scanning.

        Parameters:
        :   - **addr** – Remote Bluetooth address.
            - **param** – If non-NULL, auto connect is enabled with the given parameters. If NULL, auto connect is disabled.

        Returns:
        :   Zero on success or error code otherwise.

    int bt\_conn\_set\_security(struct bt\_conn \*conn, [bt\_security\_t](#c.bt_security_t) sec)
    :   Set security level for a connection.

        This function enable security (encryption) for a connection. If the device has bond information for the peer with sufficiently strong key encryption will be enabled. If the connection is already encrypted with sufficiently strong key this function does nothing.

        If the device has no bond information for the peer and is not already paired then the pairing procedure will be initiated. Note that `sec` has no effect on the security level selected for the pairing process. The selection is instead controlled by the values of the registered [bt\_conn\_auth\_cb](#structbt__conn__auth__cb). If the device has bond information or is already paired and the keys are too weak then the pairing procedure will be initiated.

        This function may return an error if the required level of security defined using `sec` is not possible to achieve due to local or remote device limitation (e.g., input output capabilities), or if the maximum number of paired devices has been reached.

        This function may return an error if the pairing procedure has already been initiated by the local device or the peer device.

        Note

        When  [`CONFIG_BT_SMP_SC_ONLY`](../../../kconfig.md#CONFIG_BT_SMP_SC_ONLY "CONFIG_BT_SMP_SC_ONLY") is enabled then the security level will always be level 4.

        Note

        When  [`CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY`](../../../kconfig.md#CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY "CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY") is enabled then the security level will always be level 3.

        Note

        When [BT\_SECURITY\_FORCE\_PAIR](#group__bt__conn_1ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae) within `sec` is enabled then the pairing procedure will always be initiated.

        Parameters:
        :   - **conn** – Connection object.
            - **sec** – Requested minimum security level.

        Returns:
        :   0 on success or negative error

    [bt\_security\_t](#c.bt_security_t) bt\_conn\_get\_security(const struct bt\_conn \*conn)
    :   Get security level for a connection.

        Returns:
        :   Connection security level

    uint8\_t bt\_conn\_enc\_key\_size(const struct bt\_conn \*conn)
    :   Get encryption key size.

        This function gets encryption key size. If there is no security (encryption) enabled 0 will be returned.

        Parameters:
        :   - **conn** – Existing connection object.

        Returns:
        :   Encryption key size.

    void bt\_conn\_cb\_register(struct [bt\_conn\_cb](#c.bt_conn_cb) \*cb)
    :   Register connection callbacks.

        Register callbacks to monitor the state of connections.

        Parameters:
        :   - **cb** – Callback struct. Must point to memory that remains valid.

    int bt\_conn\_cb\_unregister(struct [bt\_conn\_cb](#c.bt_conn_cb) \*cb)
    :   Unregister connection callbacks.

        Unregister the state of connections callbacks.

        Parameters:
        :   - **cb** – Callback struct point to memory that remains valid.

        Return values:
        :   - **0** – Success
            - **-EINVAL** – If `cb` is NULL
            - **-ENOENT** – if `cb` was not registered

    void bt\_set\_bondable(bool enable)
    :   Enable/disable bonding.

        Set/clear the Bonding flag in the Authentication Requirements of SMP Pairing Request/Response data. The initial value of this flag depends on BT\_BONDABLE Kconfig setting. For the vast majority of applications calling this function shouldn’t be needed.

        Parameters:
        :   - **enable** – Value allowing/disallowing to be bondable.

    int bt\_conn\_set\_bondable(struct bt\_conn \*conn, bool enable)
    :   Set/clear the bonding flag for a given connection.

        Set/clear the Bonding flag in the Authentication Requirements of SMP Pairing Request/Response data for a given connection.

        The bonding flag for a given connection cannot be set/cleared if security procedures in the SMP module have already started. This function can be called only once per connection.

        If the bonding flag is not set/cleared for a given connection, the value will depend on global configuration which is set using bt\_set\_bondable. The default value of the global configuration is defined using CONFIG\_BT\_BONDABLE Kconfig option.

        Parameters:
        :   - **conn** – Connection object.
            - **enable** – Value allowing/disallowing to be bondable.

    void bt\_le\_oob\_set\_sc\_flag(bool enable)
    :   Allow/disallow remote LE SC OOB data to be used for pairing.

        Set/clear the OOB data flag for LE SC SMP Pairing Request/Response data.

        Parameters:
        :   - **enable** – Value allowing/disallowing remote LE SC OOB data.

    void bt\_le\_oob\_set\_legacy\_flag(bool enable)
    :   Allow/disallow remote legacy OOB data to be used for pairing.

        Set/clear the OOB data flag for legacy SMP Pairing Request/Response data.

        Parameters:
        :   - **enable** – Value allowing/disallowing remote legacy OOB data.

    int bt\_le\_oob\_set\_legacy\_tk(struct bt\_conn \*conn, const uint8\_t \*tk)
    :   Set OOB Temporary Key to be used for pairing.

        This function allows to set OOB data for the LE legacy pairing procedure. The function should only be called in response to the oob\_data\_request() callback provided that the legacy method is user pairing.

        Parameters:
        :   - **conn** – Connection object
            - **tk** – Pointer to 16 byte long TK array

        Returns:
        :   Zero on success or -EINVAL if NULL

    int bt\_le\_oob\_set\_sc\_data(struct bt\_conn \*conn, const struct [bt\_le\_oob\_sc\_data](gap.md#c.bt_le_oob_sc_data "bt_le_oob_sc_data") \*oobd\_local, const struct [bt\_le\_oob\_sc\_data](gap.md#c.bt_le_oob_sc_data "bt_le_oob_sc_data") \*oobd\_remote)
    :   Set OOB data during LE Secure Connections (SC) pairing procedure.

        This function allows to set OOB data during the LE SC pairing procedure. The function should only be called in response to the oob\_data\_request() callback provided that LE SC method is used for pairing.

        The user should submit OOB data according to the information received in the callback. This may yield three different configurations: with only local OOB data present, with only remote OOB data present or with both local and remote OOB data present.

        Parameters:
        :   - **conn** – Connection object
            - **oobd\_local** – Local OOB data or NULL if not present
            - **oobd\_remote** – Remote OOB data or NULL if not present

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    int bt\_le\_oob\_get\_sc\_data(struct bt\_conn \*conn, const struct [bt\_le\_oob\_sc\_data](gap.md#c.bt_le_oob_sc_data "bt_le_oob_sc_data") \*\*oobd\_local, const struct [bt\_le\_oob\_sc\_data](gap.md#c.bt_le_oob_sc_data "bt_le_oob_sc_data") \*\*oobd\_remote)
    :   Get OOB data used for LE Secure Connections (SC) pairing procedure.

        This function allows to get OOB data during the LE SC pairing procedure that were set by the [bt\_le\_oob\_set\_sc\_data()](#group__bt__conn_1gac365f9748ad0737f09142ee1de982503) API.

        Note

        The OOB data will only be available as long as the connection object associated with it is valid.

        Parameters:
        :   - **conn** – Connection object
            - **oobd\_local** – Local OOB data or NULL if not set
            - **oobd\_remote** – Remote OOB data or NULL if not set

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    int bt\_passkey\_set(unsigned int passkey)
    :   Set a fixed passkey to be used for pairing.

        This API is only available when the CONFIG\_BT\_FIXED\_PASSKEY configuration option has been enabled.

        Sets a fixed passkey to be used for pairing. If set, the pairing\_confirm() callback will be called for all incoming pairings.

        Parameters:
        :   - **passkey** – A valid passkey (0 - 999999) or BT\_PASSKEY\_INVALID to disable a previously set fixed passkey.

        Returns:
        :   0 on success or a negative error code on failure.

    int bt\_conn\_auth\_cb\_register(const struct [bt\_conn\_auth\_cb](#c.bt_conn_auth_cb) \*cb)
    :   Register authentication callbacks.

        Register callbacks to handle authenticated pairing. Passing NULL unregisters a previous callbacks structure.

        Parameters:
        :   - **cb** – Callback struct.

        Returns:
        :   Zero on success or negative error code otherwise

    int bt\_conn\_auth\_cb\_overlay(struct bt\_conn \*conn, const struct [bt\_conn\_auth\_cb](#c.bt_conn_auth_cb) \*cb)
    :   Overlay authentication callbacks used for a given connection.

        This function can be used only for Bluetooth LE connections. The  [`CONFIG_BT_SMP`](../../../kconfig.md#CONFIG_BT_SMP "CONFIG_BT_SMP") must be enabled for this function.

        The authentication callbacks for a given connection cannot be overlaid if security procedures in the SMP module have already started. This function can be called only once per connection.

        Parameters:
        :   - **conn** – Connection object.
            - **cb** – Callback struct.

        Returns:
        :   Zero on success or negative error code otherwise

    int bt\_conn\_auth\_info\_cb\_register(struct [bt\_conn\_auth\_info\_cb](#c.bt_conn_auth_info_cb) \*cb)
    :   Register authentication information callbacks.

        Register callbacks to get authenticated pairing information. Multiple registrations can be done.

        Parameters:
        :   - **cb** – Callback struct.

        Returns:
        :   Zero on success or negative error code otherwise

    int bt\_conn\_auth\_info\_cb\_unregister(struct [bt\_conn\_auth\_info\_cb](#c.bt_conn_auth_info_cb) \*cb)
    :   Unregister authentication information callbacks.

        Unregister callbacks to stop getting authenticated pairing information.

        Parameters:
        :   - **cb** – Callback struct.

        Returns:
        :   Zero on success or negative error code otherwise

    int bt\_conn\_auth\_passkey\_entry(struct bt\_conn \*conn, unsigned int passkey)
    :   Reply with entered passkey.

        This function should be called only after passkey\_entry callback from [bt\_conn\_auth\_cb](#structbt__conn__auth__cb) structure was called.

        Parameters:
        :   - **conn** – Connection object.
            - **passkey** – Entered passkey.

        Returns:
        :   Zero on success or negative error code otherwise

    int bt\_conn\_auth\_keypress\_notify(struct bt\_conn \*conn, enum [bt\_conn\_auth\_keypress](#c.bt_conn_auth_keypress) type)
    :   Send Passkey Keypress Notification during pairing.

        This function may be called only after passkey\_entry callback from [bt\_conn\_auth\_cb](#structbt__conn__auth__cb) structure was called.

        Requires  [`CONFIG_BT_PASSKEY_KEYPRESS`](../../../kconfig.md#CONFIG_BT_PASSKEY_KEYPRESS "CONFIG_BT_PASSKEY_KEYPRESS") .

        See also

        [bt\_conn\_auth\_keypress](#group__bt__conn_1ga57465d3a61214531ddaffc2c30939043).

        Parameters:
        :   - **conn** – Destination for the notification.
            - **type** – What keypress event type to send.

        Return values:
        :   - **0** – Success
            - **-EINVAL** – Improper use of the API.
            - **-ENOMEM** – Failed to allocate.
            - **-ENOBUFS** – Failed to allocate.

    int bt\_conn\_auth\_cancel(struct bt\_conn \*conn)
    :   Cancel ongoing authenticated pairing.

        This function allows to cancel ongoing authenticated pairing.

        Parameters:
        :   - **conn** – Connection object.

        Returns:
        :   Zero on success or negative error code otherwise

    int bt\_conn\_auth\_passkey\_confirm(struct bt\_conn \*conn)
    :   Reply if passkey was confirmed to match by user.

        This function should be called only after passkey\_confirm callback from [bt\_conn\_auth\_cb](#structbt__conn__auth__cb) structure was called.

        Parameters:
        :   - **conn** – Connection object.

        Returns:
        :   Zero on success or negative error code otherwise

    int bt\_conn\_auth\_pairing\_confirm(struct bt\_conn \*conn)
    :   Reply if incoming pairing was confirmed by user.

        This function should be called only after pairing\_confirm callback from [bt\_conn\_auth\_cb](#structbt__conn__auth__cb) structure was called if user confirmed incoming pairing.

        Parameters:
        :   - **conn** – Connection object.

        Returns:
        :   Zero on success or negative error code otherwise

    int bt\_conn\_auth\_pincode\_entry(struct bt\_conn \*conn, const char \*pin)
    :   Reply with entered PIN code.

        This function should be called only after PIN code callback from [bt\_conn\_auth\_cb](#structbt__conn__auth__cb) structure was called. It’s for legacy 2.0 devices.

        Parameters:
        :   - **conn** – Connection object.
            - **pin** – Entered PIN code.

        Returns:
        :   Zero on success or negative error code otherwise

    struct bt\_conn \*bt\_conn\_create\_br(const [bt\_addr\_t](gap.md#c.bt_addr_t "bt_addr_t") \*peer, const struct [bt\_br\_conn\_param](#c.bt_br_conn_param) \*param)
    :   Initiate an BR/EDR connection to a remote device.

        Allows initiate new BR/EDR link to remote peer using its address.

        The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#group__bt__conn_1ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

        Parameters:
        :   - **peer** – Remote address.
            - **param** – Initial connection parameters.

        Returns:
        :   Valid connection object on success or NULL otherwise.

    struct bt\_conn \*bt\_conn\_create\_sco(const [bt\_addr\_t](gap.md#c.bt_addr_t "bt_addr_t") \*peer)
    :   Initiate an SCO connection to a remote device.

        Allows initiate new SCO link to remote peer using its address.

        The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#group__bt__conn_1ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

        Parameters:
        :   - **peer** – Remote address.

        Returns:
        :   Valid connection object on success or NULL otherwise.

    struct bt\_le\_conn\_param
    :   *#include <conn.h>*

        Connection parameters for LE connections.

    struct bt\_conn\_le\_phy\_info
    :   *#include <conn.h>*

        Connection PHY information for LE connections.

        Public Members

        uint8\_t rx\_phy
        :   Connection transmit PHY.

    struct bt\_conn\_le\_phy\_param
    :   *#include <conn.h>*

        Preferred PHY parameters for LE connections.

        Public Members

        uint16\_t options
        :   Connection PHY options.

        uint8\_t pref\_tx\_phy
        :   Bitmask of preferred transmit PHYs.

        uint8\_t pref\_rx\_phy
        :   Bitmask of preferred receive PHYs.

    struct bt\_conn\_le\_data\_len\_info
    :   *#include <conn.h>*

        Connection data length information for LE connections.

        Public Members

        uint16\_t tx\_max\_len
        :   Maximum Link Layer transmission payload size in bytes.

        uint16\_t tx\_max\_time
        :   Maximum Link Layer transmission payload time in us.

        uint16\_t rx\_max\_len
        :   Maximum Link Layer reception payload size in bytes.

        uint16\_t rx\_max\_time
        :   Maximum Link Layer reception payload time in us.

    struct bt\_conn\_le\_data\_len\_param
    :   *#include <conn.h>*

        Connection data length parameters for LE connections.

        Public Members

        uint16\_t tx\_max\_len
        :   Maximum Link Layer transmission payload size in bytes.

        uint16\_t tx\_max\_time
        :   Maximum Link Layer transmission payload time in us.

    struct bt\_conn\_le\_info
    :   *#include <conn.h>*

        LE Connection Info Structure.

        Public Members

        const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*src
        :   Source (Local) Identity Address.

        const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*dst
        :   Destination (Remote) Identity Address or remote Resolvable Private Address (RPA) before identity has been resolved.

        const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*local
        :   Local device address used during connection setup.

        const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*remote
        :   Remote device address used during connection setup.

        uint16\_t interval
        :   Connection interval.

        uint16\_t latency
        :   Connection peripheral latency.

        uint16\_t timeout
        :   Connection supervision timeout.

    struct bt\_conn\_br\_info
    :   *#include <conn.h>*

        BR/EDR Connection Info Structure.

        Public Members

        const [bt\_addr\_t](gap.md#c.bt_addr_t "bt_addr_t") \*dst
        :   Destination (Remote) BR/EDR address.

    struct bt\_security\_info
    :   *#include <conn.h>*

        Security Info Structure.

        Public Members

        [bt\_security\_t](#c.bt_security_t) level
        :   Security Level.

        uint8\_t enc\_key\_size
        :   Encryption Key Size.

        enum [bt\_security\_flag](#c.bt_security_flag) flags
        :   Flags.

    struct bt\_conn\_info
    :   *#include <conn.h>*

        Connection Info Structure.

        Public Members

        enum [bt\_conn\_type](#c.bt_conn_type) type
        :   Connection Type.

        uint8\_t role
        :   Connection Role.

        uint8\_t id
        :   Which local identity the connection was created with.

        struct [bt\_conn\_le\_info](#c.bt_conn_le_info) le
        :   LE Connection specific Info.

        struct [bt\_conn\_br\_info](#c.bt_conn_br_info) br
        :   BR/EDR Connection specific Info.

        union [bt\_conn\_info](#c.bt_conn_info).[anonymous] [anonymous]
        :   Connection Type specific Info.

        enum [bt\_conn\_state](#c.bt_conn_state) state
        :   Connection state.

        struct [bt\_security\_info](#c.bt_security_info) security
        :   Security specific info.

    struct bt\_conn\_le\_remote\_info
    :   *#include <conn.h>*

        LE Connection Remote Info Structure.

        Public Members

        const uint8\_t \*features
        :   Remote LE feature set (bitmask).

    struct bt\_conn\_br\_remote\_info
    :   *#include <conn.h>*

        BR/EDR Connection Remote Info structure.

        Public Members

        const uint8\_t \*features
        :   Remote feature set (pages of bitmasks).

        uint8\_t num\_pages
        :   Number of pages in the remote feature set.

    struct bt\_conn\_remote\_info
    :   *#include <conn.h>*

        Connection Remote Info Structure.

        Note

        The version, manufacturer and subversion fields will only contain valid data if  [`CONFIG_BT_REMOTE_VERSION`](../../../kconfig.md#CONFIG_BT_REMOTE_VERSION "CONFIG_BT_REMOTE_VERSION") is enabled.

        Public Members

        uint8\_t type
        :   Connection Type.

        uint8\_t version
        :   Remote Link Layer version.

        uint16\_t manufacturer
        :   Remote manufacturer identifier.

        uint16\_t subversion
        :   Per-manufacturer unique revision.

        struct [bt\_conn\_le\_remote\_info](#c.bt_conn_le_remote_info) le
        :   LE connection remote info.

        struct [bt\_conn\_br\_remote\_info](#c.bt_conn_br_remote_info) br
        :   BR/EDR connection remote info.

    struct bt\_conn\_le\_tx\_power
    :   *#include <conn.h>*

        LE Transmit Power Level Structure.

        Public Members

        uint8\_t phy
        :   Input: 1M, 2M, Coded S2 or Coded S8.

        int8\_t current\_level
        :   Output: current transmit power level.

        int8\_t max\_level
        :   Output: maximum transmit power level.

    struct bt\_conn\_le\_tx\_power\_report
    :   *#include <conn.h>*

        LE Transmit Power Reporting Structure.

        Public Members

        uint8\_t reason
        :   Reason for Transmit power reporting, as documented in Core Spec.

            Version 5.4 Vol. 4, Part E, 7.7.65.33.

        enum [bt\_conn\_le\_tx\_power\_phy](#c.bt_conn_le_tx_power_phy) phy
        :   Phy of Transmit power reporting.

        int8\_t tx\_power\_level
        :   Transmit power level.

            - 0xXX - Transmit power level

              - Range: -127 to 20
              - Units: dBm
            - 0x7E - Remote device is not managing power levels on this PHY.
            - 0x7F - Transmit power level is not available

        uint8\_t tx\_power\_level\_flag
        :   Bit 0: Transmit power level is at minimum level.

            Bit 1: Transmit power level is at maximum level.

        int8\_t delta
        :   Change in transmit power level.

            - 0xXX - Change in transmit power level (positive indicates increased power, negative indicates decreased power, zero indicates unchanged) Units: dB
            - 0x7F - Change is not available or is out of range.

    struct bt\_conn\_le\_create\_param
    :   *#include <conn.h>*

        Public Members

        uint32\_t options
        :   Bit-field of create connection options.

        uint16\_t interval
        :   Scan interval (N \* 0.625 ms).

        uint16\_t window
        :   Scan window (N \* 0.625 ms).

        uint16\_t interval\_coded
        :   Scan interval LE Coded PHY (N \* 0.625 MS).

            Set zero to use same as LE 1M PHY scan interval

        uint16\_t window\_coded
        :   Scan window LE Coded PHY (N \* 0.625 MS).

            Set zero to use same as LE 1M PHY scan window.

        uint16\_t timeout
        :   Connection initiation timeout (N \* 10 MS).

            Set zero to use the default  [`CONFIG_BT_CREATE_CONN_TIMEOUT`](../../../kconfig.md#CONFIG_BT_CREATE_CONN_TIMEOUT "CONFIG_BT_CREATE_CONN_TIMEOUT") timeout.

            Note

            Unused in [bt\_conn\_le\_create\_auto](#group__bt__conn_1gaecfaf2cb44772511dbb585de8f76f09b)

    struct bt\_conn\_le\_create\_synced\_param
    :   *#include <conn.h>*

        Public Members

        const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*peer
        :   Remote address.

            The peer must be synchronized to the PAwR train.

        uint8\_t subevent
        :   The subevent where the connection will be initiated.

    struct bt\_conn\_cb
    :   *#include <conn.h>*

        Connection callback structure.

        This structure is used for tracking the state of a connection. It is registered with the help of the [bt\_conn\_cb\_register()](#group__bt__conn_1ga33b35e6457af183e059078aead4562b4) API. It’s permissible to register multiple instances of this [bt\_conn\_cb](#structbt__conn__cb) type, in case different modules of an application are interested in tracking the connection state. If a callback is not of interest for an instance, it may be set to NULL and will as a consequence not be used for that instance.

        Public Members

        void (\*connected)(struct bt\_conn \*conn, uint8\_t err)
        :   A new connection has been established.

            This callback notifies the application of a new connection. In case the err parameter is non-zero it means that the connection establishment failed.

            `err` can mean either of the following:

            - BT\_HCI\_ERR\_UNKNOWN\_CONN\_ID Creating the connection started by [bt\_conn\_le\_create](#group__bt__conn_1ga8d66f3e0262a51279e9fa8b3139252e6) was canceled either by the user through [bt\_conn\_disconnect](#group__bt__conn_1ga14e7c852b0271781594e742ae509c5d3) or by the timeout in the host through [bt\_conn\_le\_create\_param](#structbt__conn__le__create__param) timeout parameter, which defaults to  [`CONFIG_BT_CREATE_CONN_TIMEOUT`](../../../kconfig.md#CONFIG_BT_CREATE_CONN_TIMEOUT "CONFIG_BT_CREATE_CONN_TIMEOUT") seconds.
            - `BT_HCI_ERR_ADV_TIMEOUT` High duty cycle directed connectable advertiser started by [bt\_le\_adv\_start](gap.md#group__bt__gap_1gad2e3caef88d52d720e8e4d21df767b02) failed to be connected within the timeout.

            Note

            If the connection was established from an advertising set then the advertising set cannot be restarted directly from this callback. Instead use the connected callback of the advertising set.

            Param conn:
            :   New connection object.

            Param err:
            :   HCI error. Zero for success, non-zero otherwise.

        void (\*disconnected)(struct bt\_conn \*conn, uint8\_t reason)
        :   A connection has been disconnected.

            This callback notifies the application that a connection has been disconnected.

            When this callback is called the stack still has one reference to the connection object. If the application in this callback tries to start either a connectable advertiser or create a new connection this might fail because there are no free connection objects available. To avoid this issue it is recommended to either start connectable advertise or create a new connection using [k\_work\_submit](../../../kernel/services/threads/workqueue.md#group__workqueue__apis_1gace61b59575093d7442f39ccb7be686d7) or increase  [`CONFIG_BT_MAX_CONN`](../../../kconfig.md#CONFIG_BT_MAX_CONN "CONFIG_BT_MAX_CONN") .

            Param conn:
            :   Connection object.

            Param reason:
            :   BT\_HCI\_ERR\_\* reason for the disconnection.

        void (\*recycled)(void)
        :   A connection object has been returned to the pool.

            This callback notifies the application that it might be able to allocate a connection object. No guarantee, first come, first serve.

            Use this to e.g. re-start connectable advertising or scanning.

            Treat this callback as an ISR, as it originates from [bt\_conn\_unref](#group__bt__conn_1ga4b18c6b22a9f02be0d7d078b2ce51ff6) which is used by the BT stack. Making Bluetooth API calls in this context is error-prone and strongly discouraged.

        bool (\*le\_param\_req)(struct bt\_conn \*conn, struct [bt\_le\_conn\_param](#c.bt_le_conn_param) \*param)
        :   LE connection parameter update request.

            This callback notifies the application that a remote device is requesting to update the connection parameters. The application accepts the parameters by returning true, or rejects them by returning false. Before accepting, the application may also adjust the parameters to better suit its needs.

            It is recommended for an application to have just one of these callbacks for simplicity. However, if an application registers multiple it needs to manage the potentially different requirements for each callback. Each callback gets the parameters as returned by previous callbacks, i.e. they are not necessarily the same ones as the remote originally sent.

            If the application does not have this callback then the default is to accept the parameters.

            Param conn:
            :   Connection object.

            Param param:
            :   Proposed connection parameters.

            Return:
            :   true to accept the parameters, or false to reject them.

        void (\*le\_param\_updated)(struct bt\_conn \*conn, uint16\_t interval, uint16\_t latency, uint16\_t timeout)
        :   The parameters for an LE connection have been updated.

            This callback notifies the application that the connection parameters for an LE connection have been updated.

            Param conn:
            :   Connection object.

            Param interval:
            :   Connection interval.

            Param latency:
            :   Connection latency.

            Param timeout:
            :   Connection supervision timeout.

        void (\*identity\_resolved)(struct bt\_conn \*conn, const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*rpa, const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*identity)
        :   Remote Identity Address has been resolved.

            This callback notifies the application that a remote Identity Address has been resolved

            Param conn:
            :   Connection object.

            Param rpa:
            :   Resolvable Private Address.

            Param identity:
            :   Identity Address.

        void (\*security\_changed)(struct bt\_conn \*conn, [bt\_security\_t](#c.bt_security_t) level, enum [bt\_security\_err](#c.bt_security_err) err)
        :   The security level of a connection has changed.

            This callback notifies the application that the security of a connection has changed.

            The security level of the connection can either have been increased or remain unchanged. An increased security level means that the pairing procedure has been performed or the bond information from a previous connection has been applied. If the security level remains unchanged this means that the encryption key has been refreshed for the connection.

            Param conn:
            :   Connection object.

            Param level:
            :   New security level of the connection.

            Param err:
            :   Security error. Zero for success, non-zero otherwise.

        void (\*remote\_info\_available)(struct bt\_conn \*conn, struct [bt\_conn\_remote\_info](#c.bt_conn_remote_info) \*remote\_info)
        :   Remote information procedures has completed.

            This callback notifies the application that the remote information has been retrieved from the remote peer.

            Param conn:
            :   Connection object.

            Param remote\_info:
            :   Connection information of remote device.

        void (\*le\_phy\_updated)(struct bt\_conn \*conn, struct [bt\_conn\_le\_phy\_info](#c.bt_conn_le_phy_info) \*param)
        :   The PHY of the connection has changed.

            This callback notifies the application that the PHY of the connection has changed.

            Param conn:
            :   Connection object.

            Param info:
            :   Connection LE PHY information.

        void (\*le\_data\_len\_updated)(struct bt\_conn \*conn, struct [bt\_conn\_le\_data\_len\_info](#c.bt_conn_le_data_len_info) \*info)
        :   The data length parameters of the connection has changed.

            This callback notifies the application that the maximum Link Layer payload length or transmission time has changed.

            Param conn:
            :   Connection object.

            Param info:
            :   Connection data length information.

    struct bt\_conn\_oob\_info
    :   *#include <conn.h>*

        Info Structure for OOB pairing.

        Public Types

        enum [anonymous]
        :   Type of OOB pairing method.

            *Values:*

            enumerator BT\_CONN\_OOB\_LE\_LEGACY
            :   LE legacy pairing.

            enumerator BT\_CONN\_OOB\_LE\_SC
            :   LE SC pairing.

        Public Members

        enum [bt\_conn\_oob\_info](#c.bt_conn_oob_info).[[anonymous]](#c.bt_conn_oob_info.@071154206266322234333176322374364375362306302210) type
        :   Type of OOB pairing method.

        enum [bt\_conn\_oob\_info](#c.bt_conn_oob_info).[anonymous].[anonymous].[anonymous] oob\_config
        :   OOB data configuration.

        struct [bt\_conn\_oob\_info](#c.bt_conn_oob_info).[anonymous].[anonymous] lesc
        :   LE Secure Connections OOB pairing parameters.

    struct bt\_conn\_pairing\_feat
    :   *#include <conn.h>*

        Pairing request and pairing response info structure.

        This structure is the same for both smp\_pairing\_req and smp\_pairing\_rsp and a subset of the packet data, except for the initial Code octet. It is documented in Core Spec. Vol. 3, Part H, 3.5.1 and 3.5.2.

        Public Members

        uint8\_t io\_capability
        :   IO Capability, Core Spec.

            Vol 3, Part H, 3.5.1, Table 3.4

        uint8\_t oob\_data\_flag
        :   OOB data flag, Core Spec.

            Vol 3, Part H, 3.5.1, Table 3.5

        uint8\_t auth\_req
        :   AuthReq, Core Spec.

            Vol 3, Part H, 3.5.1, Fig. 3.3

        uint8\_t max\_enc\_key\_size
        :   Maximum Encryption Key Size, Core Spec.

            Vol 3, Part H, 3.5.1

        uint8\_t init\_key\_dist
        :   Initiator Key Distribution/Generation, Core Spec.

            Vol 3, Part H, 3.6.1, Fig. 3.11

        uint8\_t resp\_key\_dist
        :   Responder Key Distribution/Generation, Core Spec.

            Vol 3, Part H 3.6.1, Fig. 3.11

    struct bt\_conn\_auth\_cb
    :   *#include <conn.h>*

        Authenticated pairing callback structure.

        Public Members

        enum [bt\_security\_err](#c.bt_security_err) (\*pairing\_accept)(struct bt\_conn \*conn, const struct [bt\_conn\_pairing\_feat](#c.bt_conn_pairing_feat) \*const feat)
        :   Query to proceed incoming pairing or not.

            On any incoming pairing req/rsp this callback will be called for the application to decide whether to allow for the pairing to continue.

            The pairing info received from the peer is passed to assist making the decision.

            As this callback is synchronous the application should return a response value immediately. Otherwise it may affect the timing during pairing. Hence, this information should not be conveyed to the user to take action.

            The remaining callbacks are not affected by this, but do notice that other callbacks can be called during the pairing. Eg. if pairing\_confirm is registered both will be called for Just-Works pairings.

            This callback may be unregistered in which case pairing continues as if the Kconfig flag was not set.

            This callback is not called for BR/EDR Secure Simple Pairing (SSP).

            Param conn:
            :   Connection where pairing is initiated.

            Param feat:
            :   Pairing req/resp info.

        void (\*passkey\_display)(struct bt\_conn \*conn, unsigned int passkey)
        :   Display a passkey to the user.

            When called the application is expected to display the given passkey to the user, with the expectation that the passkey will then be entered on the peer device. The passkey will be in the range of 0 - 999999, and is expected to be padded with zeroes so that six digits are always shown. E.g. the value 37 should be shown as 000037.

            This callback may be set to NULL, which means that the local device lacks the ability do display a passkey. If set to non-NULL the cancel callback must also be provided, since this is the only way the application can find out that it should stop displaying the passkey.

            Param conn:
            :   Connection where pairing is currently active.

            Param passkey:
            :   Passkey to show to the user.

        void (\*passkey\_entry)(struct bt\_conn \*conn)
        :   Request the user to enter a passkey.

            When called the user is expected to enter a passkey. The passkey must be in the range of 0 - 999999, and should be expected to be zero-padded, as that’s how the peer device will typically be showing it (e.g. 37 would be shown as 000037).

            Once the user has entered the passkey its value should be given to the stack using the [bt\_conn\_auth\_passkey\_entry()](#group__bt__conn_1ga3906d8d3d192e8a6ad1bf6b7acc32ff0) API.

            This callback may be set to NULL, which means that the local device lacks the ability to enter a passkey. If set to non-NULL the cancel callback must also be provided, since this is the only way the application can find out that it should stop requesting the user to enter a passkey.

            Param conn:
            :   Connection where pairing is currently active.

        void (\*passkey\_confirm)(struct bt\_conn \*conn, unsigned int passkey)
        :   Request the user to confirm a passkey.

            When called the user is expected to confirm that the given passkey is also shown on the peer device.. The passkey will be in the range of 0 - 999999, and should be zero-padded to always be six digits (e.g. 37 would be shown as 000037).

            Once the user has confirmed the passkey to match, the [bt\_conn\_auth\_passkey\_confirm()](#group__bt__conn_1gab8c3ecf2a3d68e54379917844a29d995) API should be called. If the user concluded that the passkey doesn’t match the [bt\_conn\_auth\_cancel()](#group__bt__conn_1ga89e5fc4bcab3f5598d20a9cd8ace5f59) API should be called.

            This callback may be set to NULL, which means that the local device lacks the ability to confirm a passkey. If set to non-NULL the cancel callback must also be provided, since this is the only way the application can find out that it should stop requesting the user to confirm a passkey.

            Param conn:
            :   Connection where pairing is currently active.

            Param passkey:
            :   Passkey to be confirmed.

        void (\*oob\_data\_request)(struct bt\_conn \*conn, struct [bt\_conn\_oob\_info](#c.bt_conn_oob_info) \*info)
        :   Request the user to provide Out of Band (OOB) data.

            When called the user is expected to provide OOB data. The required data are indicated by the information structure.

            For LE Secure Connections OOB pairing, the user should provide local OOB data, remote OOB data or both depending on their availability. Their value should be given to the stack using the [bt\_le\_oob\_set\_sc\_data()](#group__bt__conn_1gac365f9748ad0737f09142ee1de982503) API.

            This callback must be set to non-NULL in order to support OOB pairing.

            Param conn:
            :   Connection where pairing is currently active.

            Param info:
            :   OOB pairing information.

        void (\*cancel)(struct bt\_conn \*conn)
        :   Cancel the ongoing user request.

            This callback will be called to notify the application that it should cancel any previous user request (passkey display, entry or confirmation).

            This may be set to NULL, but must always be provided whenever the passkey\_display, passkey\_entry passkey\_confirm or pairing\_confirm callback has been provided.

            Param conn:
            :   Connection where pairing is currently active.

        void (\*pairing\_confirm)(struct bt\_conn \*conn)
        :   Request confirmation for an incoming pairing.

            This callback will be called to confirm an incoming pairing request where none of the other user callbacks is applicable.

            If the user decides to accept the pairing the [bt\_conn\_auth\_pairing\_confirm()](#group__bt__conn_1ga3e15b9deb6787d3e415bbea35c9aa91d) API should be called. If the user decides to reject the pairing the [bt\_conn\_auth\_cancel()](#group__bt__conn_1ga89e5fc4bcab3f5598d20a9cd8ace5f59) API should be called.

            This callback may be set to NULL, which means that the local device lacks the ability to confirm a pairing request. If set to non-NULL the cancel callback must also be provided, since this is the only way the application can find out that it should stop requesting the user to confirm a pairing request.

            Param conn:
            :   Connection where pairing is currently active.

        void (\*pincode\_entry)(struct bt\_conn \*conn, bool highsec)
        :   Request the user to enter a passkey.

            This callback will be called for a BR/EDR (Bluetooth Classic) connection where pairing is being performed. Once called the user is expected to enter a PIN code with a length between 1 and 16 digits. If the *highsec* parameter is set to true the PIN code must be 16 digits long.

            Once entered, the PIN code should be given to the stack using the [bt\_conn\_auth\_pincode\_entry()](#group__bt__conn_1ga4002a1b092832807218afa8ad279ab98) API.

            This callback may be set to NULL, however in that case pairing over BR/EDR will not be possible. If provided, the cancel callback must be provided as well.

            Param conn:
            :   Connection where pairing is currently active.

            Param highsec:
            :   true if 16 digit PIN is required.

    struct bt\_conn\_auth\_info\_cb
    :   *#include <conn.h>*

        Authenticated pairing information callback structure.

        Public Members

        void (\*pairing\_complete)(struct bt\_conn \*conn, bool bonded)
        :   notify that pairing procedure was complete.

            This callback notifies the application that the pairing procedure has been completed.

            Param conn:
            :   Connection object.

            Param bonded:
            :   Bond information has been distributed during the pairing procedure.

        void (\*pairing\_failed)(struct bt\_conn \*conn, enum [bt\_security\_err](#c.bt_security_err) reason)
        :   notify that pairing process has failed.

            Param conn:
            :   Connection object.

            Param reason:
            :   Pairing failed reason

        void (\*bond\_deleted)(uint8\_t id, const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*peer)
        :   Notify that bond has been deleted.

            This callback notifies the application that the bond information for the remote peer has been deleted

            Param id:
            :   Which local identity had the bond.

            Param peer:
            :   Remote address.

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Internally used field for list handling.

    struct bt\_br\_conn\_param
    :   *#include <conn.h>*

        Connection parameters for BR/EDR connections.
