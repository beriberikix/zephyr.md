---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/connection_mgmt.html
original_path: connectivity/bluetooth/api/connection_mgmt.html
---

# Connection Management

The Zephyr Bluetooth stack uses an abstraction called `bt_conn`
to represent connections to other devices. The internals of this struct
are not exposed to the application, but a limited amount of information
(such as the remote address) can be acquired using the
[`bt_conn_get_info()`](../../../doxygen/html/group__bt__conn.md#ga2de54f2ac83f0d8dca2a85a9fbfadcaa) API. Connection objects are reference
counted, and the application is expected to use the
[`bt_conn_ref()`](../../../doxygen/html/group__bt__conn.md#ga060d51eb2208de6f805b1fc0672d2d0c) API whenever storing a connection pointer for a
longer period of time, since this ensures that the object remains valid
(even if the connection would get disconnected). Similarly the
[`bt_conn_unref()`](../../../doxygen/html/group__bt__conn.md#ga4b18c6b22a9f02be0d7d078b2ce51ff6) API is to be used when releasing a reference
to a connection.

A common mistake is to forget unreleasing a reference to a connection
object created by functions [`bt_conn_le_create()`](../../../doxygen/html/group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6) and
[`bt_conn_le_create_synced()`](../../../doxygen/html/group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1). To protect against this, use the
[`CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE`](../../../kconfig.md#CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE "CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE") Kconfig option,
which forces these functions return an error if the connection pointer
passed to them is not NULL. This helps to spot such issues and avoid
sporadic bugs caused by not releasing the connection object.

An application may track connections by registering a
[`bt_conn_cb`](../../../doxygen/html/structbt__conn__cb.md) struct using the [`bt_conn_cb_register()`](../../../doxygen/html/group__bt__conn.md#gaa9b79cd44734c1e560d6f30509be4d0b)
or [`BT_CONN_CB_DEFINE`](../../../doxygen/html/group__bt__conn.md#ga9227880a1ae5fc373d334171e1450f00) APIs. This struct lets the application
define callbacks for connection & disconnection events, as well as other
events related to a connection such as a change in the security level or
the connection parameters. When acting as a central the application will
also get hold of the connection object through the return value of the
[`bt_conn_le_create()`](../../../doxygen/html/group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6) API.

## API Reference

[Connection management](../../../doxygen/html/group__bt__conn.md)

Related code samples

- [Basic Audio Profile (BAP) Broadcast Audio Assistant](../../../samples/bluetooth/bap_broadcast_assistant/README.md#bluetooth_bap_broadcast_assistant "Use BAP Broadcast Assistant functionality.")Use BAP Broadcast Assistant functionality.
- [Basic Audio Profile (BAP) Broadcast Audio Sink](../../../samples/bluetooth/bap_broadcast_sink/README.md#bluetooth_bap_broadcast_sink "Use BAP Broadcast Sink functionality.")Use BAP Broadcast Sink functionality.
- [Basic Audio Profile (BAP) Unicast Audio Client](../../../samples/bluetooth/bap_unicast_client/README.md#bluetooth_bap_unicast_client "Use BAP Unicast Client functionality.")Use BAP Unicast Client functionality.
- [Common Audio Profile (CAP) Initiator](../../../samples/bluetooth/cap_initiator/README.md#bluetooth_cap_initiator "Connect to CAP Acceptors and setup unicast audio streaming or broadcast audio streams.")Connect to CAP Acceptors and setup unicast audio streaming or broadcast audio streams.
- [Peripheral Accept List](../../../samples/bluetooth/peripheral_accept_list/README.md#ble_peripheral_accept_list "Advertise and accept connections only from devices on an accept list.")Advertise and accept connections only from devices on an accept list.
- [Peripheral SC-only](../../../samples/bluetooth/peripheral_sc_only/README.md#ble_peripheral_sc_only "Enable "Secure Connections Only" mode for a Bluetooth LE peripheral.")Enable "Secure Connections Only" mode for a Bluetooth LE peripheral.
- [Telephone and Media Audio Profile (TMAP) Central](../../../samples/bluetooth/tmap_central/README.md#ble_peripheral_tmap_central "Implement the TMAP Call Gateway (CG) and Unicast Media Sender (UMS) roles.")Implement the TMAP Call Gateway (CG) and Unicast Media Sender (UMS) roles.
