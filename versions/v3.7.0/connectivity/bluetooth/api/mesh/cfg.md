---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/cfg.html
original_path: connectivity/bluetooth/api/mesh/cfg.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Runtime Configuration

The runtime configuration API allows applications to change their runtime
configuration directly, without going through the Configuration models.

Bluetooth Mesh nodes should generally be configured by a central network
configurator device with a [Configuration Client](cfg_cli.md#bluetooth-mesh-models-cfg-cli) model. Each
mesh node instantiates a [Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv) model that the
Configuration Client can communicate with to change the node configuration. In some
cases, the mesh node can’t rely on the Configuration Client to detect or determine
local constraints, such as low battery power or changes in topology. For these
scenarios, this API can be used to change the configuration locally.

Note

Runtime configuration changes before the node is provisioned will not be stored
in the [persistent storage](core.md#bluetooth-mesh-persistent-storage).

## API reference

*group* Runtime Configuration
:   Runtime Configuration.

    Defines

    BT\_MESH\_KR\_NORMAL

    BT\_MESH\_KR\_PHASE\_1

    BT\_MESH\_KR\_PHASE\_2

    BT\_MESH\_KR\_PHASE\_3

    BT\_MESH\_RELAY\_DISABLED

    BT\_MESH\_RELAY\_ENABLED

    BT\_MESH\_RELAY\_NOT\_SUPPORTED

    BT\_MESH\_BEACON\_DISABLED

    BT\_MESH\_BEACON\_ENABLED

    BT\_MESH\_PRIV\_BEACON\_DISABLED

    BT\_MESH\_PRIV\_BEACON\_ENABLED

    BT\_MESH\_GATT\_PROXY\_DISABLED

    BT\_MESH\_GATT\_PROXY\_ENABLED

    BT\_MESH\_GATT\_PROXY\_NOT\_SUPPORTED

    BT\_MESH\_PRIV\_GATT\_PROXY\_DISABLED

    BT\_MESH\_PRIV\_GATT\_PROXY\_ENABLED

    BT\_MESH\_PRIV\_GATT\_PROXY\_NOT\_SUPPORTED

    BT\_MESH\_FRIEND\_DISABLED

    BT\_MESH\_FRIEND\_ENABLED

    BT\_MESH\_FRIEND\_NOT\_SUPPORTED

    BT\_MESH\_NODE\_IDENTITY\_STOPPED

    BT\_MESH\_NODE\_IDENTITY\_RUNNING

    BT\_MESH\_NODE\_IDENTITY\_NOT\_SUPPORTED

    Enums

    enum bt\_mesh\_feat\_state
    :   Bluetooth Mesh feature states.

        *Values:*

        enumerator BT\_MESH\_FEATURE\_DISABLED
        :   Feature is supported, but disabled.

        enumerator BT\_MESH\_FEATURE\_ENABLED
        :   Feature is supported and enabled.

        enumerator BT\_MESH\_FEATURE\_NOT\_SUPPORTED
        :   Feature is not supported, and cannot be enabled.

    Functions

    void bt\_mesh\_beacon\_set(bool beacon)
    :   Enable or disable sending of the Secure Network Beacon.

        Parameters:
        :   - **beacon** – New Secure Network Beacon state.

    bool bt\_mesh\_beacon\_enabled(void)
    :   Get the current Secure Network Beacon state.

        Returns:
        :   Whether the Secure Network Beacon feature is enabled.

    int bt\_mesh\_priv\_beacon\_set(enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) priv\_beacon)
    :   Enable or disable sending of the Mesh Private beacon.

        Support for the Private beacon state must be enabled with `CONFIG_BT_MESH_PRIV_BEACONS`.

        Parameters:
        :   - **priv\_beacon** – New Mesh Private beacon state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729).

        Return values:
        :   - **0** – Successfully changed the Mesh Private beacon feature state.
            - **-ENOTSUP** – The Mesh Private beacon feature is not supported.
            - **-EINVAL** – Invalid parameter.
            - **-EALREADY** – Already in the given state.

    enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) bt\_mesh\_priv\_beacon\_get(void)
    :   Get the current Mesh Private beacon state.

        Returns:
        :   The Mesh Private beacon feature state.

    void bt\_mesh\_priv\_beacon\_update\_interval\_set(uint8\_t interval)
    :   Set the current Mesh Private beacon update interval.

        The Mesh Private beacon’s randomization value is updated regularly to maintain the node’s privacy. The update interval controls how often the beacon is updated, in 10 second increments.

        Parameters:
        :   - **interval** – Private beacon update interval in 10 second steps, or 0 to update on every beacon transmission.

    uint8\_t bt\_mesh\_priv\_beacon\_update\_interval\_get(void)
    :   Get the current Mesh Private beacon update interval.

        The Mesh Private beacon’s randomization value is updated regularly to maintain the node’s privacy. The update interval controls how often the beacon is updated, in 10 second increments.

        Returns:
        :   The Private beacon update interval in 10 second steps, or 0 if the beacon is updated every time it’s transmitted.

    int bt\_mesh\_default\_ttl\_set(uint8\_t default\_ttl)
    :   Set the default TTL value.

        The default TTL value is used when no explicit TTL value is set. Models will use the default TTL value when [bt\_mesh\_msg\_ctx::send\_ttl](msg.md#structbt__mesh__msg__ctx_1a43b0ebfdc3c8018a02886d93dfe2f21b) is [BT\_MESH\_TTL\_DEFAULT](access.md#group__bt__mesh__access_1ga16516272b42420263b1c47c3ea16c0c8).

        Parameters:
        :   - **default\_ttl** – The new default TTL value. Valid values are 0x00 and 0x02 to [BT\_MESH\_TTL\_MAX](access.md#group__bt__mesh__access_1ga071e85e929589d31bf876e2e09cf2f19).

        Return values:
        :   - **0** – Successfully set the default TTL value.
            - **-EINVAL** – Invalid TTL value.

    uint8\_t bt\_mesh\_default\_ttl\_get(void)
    :   Get the current default TTL value.

        Returns:
        :   The current default TTL value.

    int bt\_mesh\_od\_priv\_proxy\_get(void)
    :   Get the current Mesh On-Demand Private Proxy state.

        Return values:
        :   - **0** – or positive value represents On-Demand Private Proxy feature state
            - **-ENOTSUP** – The On-Demand Private Proxy feature is not supported.

    int bt\_mesh\_od\_priv\_proxy\_set(uint8\_t on\_demand\_proxy)
    :   Set state of Mesh On-Demand Private Proxy.

        Support for the On-Demand Private Proxy state must be enabled with `BT_MESH_OD_PRIV_PROXY_SRV`.

        Parameters:
        :   - **on\_demand\_proxy** – New Mesh On-Demand Private Proxy state. Value of 0x00 means that advertising with Private Network Identity cannot be enabled on demand. Values in range 0x01 - 0xFF set interval of this advertising after valid Solicitation PDU is received or client disconnects.

        Return values:
        :   - **0** – Successfully changed the Mesh On-Demand Private Proxy feature state.
            - **-ENOTSUP** – The On-Demand Private Proxy feature is not supported.
            - **-EINVAL** – Invalid parameter.
            - **-EALREADY** – Already in the given state.

    void bt\_mesh\_net\_transmit\_set(uint8\_t xmit)
    :   Set the Network Transmit parameters.

        The Network Transmit parameters determine the parameters local messages are transmitted with.

        See also

        [BT\_MESH\_TRANSMIT](access.md#group__bt__mesh__access_1gaff82bf652232fbce71c31f38a10577a9)

        Parameters:
        :   - **xmit** – New Network Transmit parameters. Use [BT\_MESH\_TRANSMIT](access.md#group__bt__mesh__access_1gaff82bf652232fbce71c31f38a10577a9) for encoding.

    uint8\_t bt\_mesh\_net\_transmit\_get(void)
    :   Get the current Network Transmit parameters.

        The [BT\_MESH\_TRANSMIT\_COUNT](access.md#group__bt__mesh__access_1ga62fda0d731241efbaa4827e4eb9d1795) and [BT\_MESH\_TRANSMIT\_INT](access.md#group__bt__mesh__access_1ga2aa21171c5677d23ad0c472291639417) macros can be used to decode the Network Transmit parameters.

        Returns:
        :   The current Network Transmit parameters.

    int bt\_mesh\_relay\_set(enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) relay, uint8\_t xmit)
    :   Configure the Relay feature.

        Enable or disable the Relay feature, and configure the parameters to transmit relayed messages with.

        Support for the Relay feature must be enabled through the `CONFIG_BT_MESH_RELAY` configuration option.

        See also

        [BT\_MESH\_TRANSMIT](access.md#group__bt__mesh__access_1gaff82bf652232fbce71c31f38a10577a9)

        Parameters:
        :   - **relay** – New Relay feature state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729).
            - **xmit** – New Relay retransmit parameters. Use [BT\_MESH\_TRANSMIT](access.md#group__bt__mesh__access_1gaff82bf652232fbce71c31f38a10577a9) for encoding.

        Return values:
        :   - **0** – Successfully changed the Relay configuration.
            - **-ENOTSUP** – The Relay feature is not supported.
            - **-EINVAL** – Invalid parameter.
            - **-EALREADY** – Already using the given parameters.

    enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) bt\_mesh\_relay\_get(void)
    :   Get the current Relay feature state.

        Returns:
        :   The Relay feature state.

    uint8\_t bt\_mesh\_relay\_retransmit\_get(void)
    :   Get the current Relay Retransmit parameters.

        The [BT\_MESH\_TRANSMIT\_COUNT](access.md#group__bt__mesh__access_1ga62fda0d731241efbaa4827e4eb9d1795) and [BT\_MESH\_TRANSMIT\_INT](access.md#group__bt__mesh__access_1ga2aa21171c5677d23ad0c472291639417) macros can be used to decode the Relay Retransmit parameters.

        Returns:
        :   The current Relay Retransmit parameters, or 0 if relay is not supported.

    int bt\_mesh\_gatt\_proxy\_set(enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) gatt\_proxy)
    :   Enable or disable the GATT Proxy feature.

        Support for the GATT Proxy feature must be enabled through the `CONFIG_BT_MESH_GATT_PROXY` configuration option.

        Note

        The GATT Proxy feature only controls a Proxy node’s ability to relay messages to the mesh network. A node that supports GATT Proxy will still advertise Connectable Proxy beacons, even if the feature is disabled. The Proxy feature can only be fully disabled through compile time configuration.

        Parameters:
        :   - **gatt\_proxy** – New GATT Proxy state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729).

        Return values:
        :   - **0** – Successfully changed the GATT Proxy feature state.
            - **-ENOTSUP** – The GATT Proxy feature is not supported.
            - **-EINVAL** – Invalid parameter.
            - **-EALREADY** – Already in the given state.

    enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) bt\_mesh\_gatt\_proxy\_get(void)
    :   Get the current GATT Proxy state.

        Returns:
        :   The GATT Proxy feature state.

    int bt\_mesh\_priv\_gatt\_proxy\_set(enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) priv\_gatt\_proxy)
    :   Enable or disable the Private GATT Proxy feature.

        Support for the Private GATT Proxy feature must be enabled through the  [`CONFIG_BT_MESH_PRIV_BEACONS`](../../../../kconfig.md#CONFIG_BT_MESH_PRIV_BEACONS "CONFIG_BT_MESH_PRIV_BEACONS") and  [`CONFIG_BT_MESH_GATT_PROXY`](../../../../kconfig.md#CONFIG_BT_MESH_GATT_PROXY "CONFIG_BT_MESH_GATT_PROXY") configuration options.

        Parameters:
        :   - **priv\_gatt\_proxy** – New Private GATT Proxy state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729).

        Return values:
        :   - **0** – Successfully changed the Private GATT Proxy feature state.
            - **-ENOTSUP** – The Private GATT Proxy feature is not supported.
            - **-EINVAL** – Invalid parameter.
            - **-EALREADY** – Already in the given state.

    enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) bt\_mesh\_priv\_gatt\_proxy\_get(void)
    :   Get the current Private GATT Proxy state.

        Returns:
        :   The Private GATT Proxy feature state.

    int bt\_mesh\_friend\_set(enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) friendship)
    :   Enable or disable the Friend feature.

        Any active friendships will be terminated immediately if the Friend feature is disabled.

        Support for the Friend feature must be enabled through the `CONFIG_BT_MESH_FRIEND` configuration option.

        Parameters:
        :   - **friendship** – New Friend feature state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#group__bt__mesh__cfg_1gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729).

        Return values:
        :   - **0** – Successfully changed the Friend feature state.
            - **-ENOTSUP** – The Friend feature is not supported.
            - **-EINVAL** – Invalid parameter.
            - **-EALREADY** – Already in the given state.

    enum [bt\_mesh\_feat\_state](#c.bt_mesh_feat_state) bt\_mesh\_friend\_get(void)
    :   Get the current Friend state.

        Returns:
        :   The Friend feature state.
