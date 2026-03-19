---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/gatt.html
original_path: connectivity/bluetooth/api/gatt.html
---

# Generic Attribute Profile (GATT)

GATT layer manages the service database providing APIs for service registration
and attribute declaration.

Services can be registered using [`bt_gatt_service_register()`](../../../doxygen/html/group__bt__gatt__server.md#gab4d9cfea04e44445d5dc30ad52842b64) API
which takes the [`bt_gatt_service`](../../../doxygen/html/structbt__gatt__service.md) struct that provides the list of
attributes the service contains. The helper macro [`BT_GATT_SERVICE()`](../../../doxygen/html/group__bt__gatt__server.md#ga7d413ec013b91a633ec24d80d2814e2b)
can be used to declare a service.

Attributes can be declared using the [`bt_gatt_attr`](../../../doxygen/html/structbt__gatt__attr.md) struct or using
one of the helper macros:

> [`BT_GATT_PRIMARY_SERVICE`](../../../doxygen/html/group__bt__gatt__server.md#gaacada0ff1029af959b6fcd6703d4a0bf)
> :   Declares a Primary Service.
>
> [`BT_GATT_SECONDARY_SERVICE`](../../../doxygen/html/group__bt__gatt__server.md#gaecb4d30282677d3450ad79c5f83f3445)
> :   Declares a Secondary Service.
>
> [`BT_GATT_INCLUDE_SERVICE`](../../../doxygen/html/group__bt__gatt__server.md#ga08ffee706d271b75a54b1b99249dba24)
> :   Declares a Include Service.
>
> [`BT_GATT_CHARACTERISTIC`](../../../doxygen/html/group__bt__gatt__server.md#ga9e739546dbd906d3b3c4f1ed5ad9f41e)
> :   Declares a Characteristic.
>
> [`BT_GATT_DESCRIPTOR`](../../../doxygen/html/group__bt__gatt__server.md#ga83207fc083454327004f7d3c3e5b3840)
> :   Declares a Descriptor.
>
> [`BT_GATT_ATTRIBUTE`](../../../doxygen/html/group__bt__gatt__server.md#gac4abfeb068d16dcdaceee812c12bf406)
> :   Declares an Attribute.
>
> [`BT_GATT_CCC`](../../../doxygen/html/group__bt__gatt__server.md#ga140b9c25d10244bebd9c891f881fdc94)
> :   Declares a Client Characteristic Configuration.
>
> [`BT_GATT_CEP`](../../../doxygen/html/group__bt__gatt__server.md#ga55a82cada1093c4ff75fe5504ac504b1)
> :   Declares a Characteristic Extended Properties.
>
> [`BT_GATT_CUD`](../../../doxygen/html/group__bt__gatt__server.md#ga1e1cd9d0853e2dcbefcb85fda44dc9c7)
> :   Declares a Characteristic User Format.

Each attribute contain a `uuid`, which describes their type, a `read`
callback, a `write` callback and a set of permission. Both read and write
callbacks can be set to NULL if the attribute permission don’t allow their
respective operations.

Note

32-bit UUIDs are not supported in GATT. All 32-bit UUIDs shall be converted
to 128-bit UUIDs when the UUID is contained in an ATT PDU.

Note

Attribute `read` and `write` callbacks are called directly from RX Thread
thus it is not recommended to block for long periods of time in them.

Attribute value changes can be notified using [`bt_gatt_notify()`](../../../doxygen/html/group__bt__gatt__server.md#ga74ee552864c563aa5bc939f37395c14a) API,
alternatively there is [`bt_gatt_notify_cb()`](../../../doxygen/html/group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146) where it is possible to
pass a callback to be called when it is necessary to know the exact instant when
the data has been transmitted over the air. Indications are supported by
[`bt_gatt_indicate()`](../../../doxygen/html/group__bt__gatt__server.md#ga4f2272692cc0f1d44638828012296c80) API.

Client procedures can be enabled with the configuration option:
[`CONFIG_BT_GATT_CLIENT`](../../../kconfig.md#CONFIG_BT_GATT_CLIENT "CONFIG_BT_GATT_CLIENT")

Discover procedures can be initiated with the use of
[`bt_gatt_discover()`](../../../doxygen/html/group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd) API which takes the
[`bt_gatt_discover_params`](../../../doxygen/html/structbt__gatt__discover__params.md) struct which describes the type of
discovery. The parameters also serves as a filter when setting the `uuid`
field only attributes which matches will be discovered, in contrast setting it
to NULL allows all attributes to be discovered.

Note

Caching discovered attributes is not supported.

Read procedures are supported by [`bt_gatt_read()`](../../../doxygen/html/group__bt__gatt__client.md#ga1a18dd726ab960a88d7f85f2a014141a) API which takes the
[`bt_gatt_read_params`](../../../doxygen/html/structbt__gatt__read__params.md) struct as parameters. In the parameters one or
more attributes can be set, though setting multiple handles requires the option:
[`CONFIG_BT_GATT_READ_MULTIPLE`](../../../kconfig.md#CONFIG_BT_GATT_READ_MULTIPLE "CONFIG_BT_GATT_READ_MULTIPLE")

Write procedures are supported by [`bt_gatt_write()`](../../../doxygen/html/group__bt__gatt__client.md#ga843a42e68e0497d88d3f655f8ffd58d4) API and takes
[`bt_gatt_write_params`](../../../doxygen/html/structbt__gatt__write__params.md) struct as parameters. In case the write
operation don’t require a response [`bt_gatt_write_without_response()`](../../../doxygen/html/group__bt__gatt__client.md#ga9fc78e32230637a6f092da2400c50fe7)
or [`bt_gatt_write_without_response_cb()`](../../../doxygen/html/group__bt__gatt__client.md#ga49439413d12b5a8a1c68735e961ab6fa) APIs can be used, with the
later working similarly to [`bt_gatt_notify_cb()`](../../../doxygen/html/group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146).

Subscriptions to notification and indication can be initiated with use of
[`bt_gatt_subscribe()`](../../../doxygen/html/group__bt__gatt__client.md#ga7d4a8e18f51ba6476886a15f81f48e5c) API which takes
[`bt_gatt_subscribe_params`](../../../doxygen/html/structbt__gatt__subscribe__params.md) as parameters. Multiple subscriptions to
the same attribute are supported so there could be multiple `notify` callback
being triggered for the same attribute. Subscriptions can be removed with use of
[`bt_gatt_unsubscribe()`](../../../doxygen/html/group__bt__gatt__client.md#ga56509c9b8f73f729cfa5e75be22d79ae) API.

Note

When subscriptions are removed `notify` callback is called with the data
set to NULL.

## API Reference

[Generic Attribute Profile (GATT)](../../../doxygen/html/group__bt__gatt.md)

Related code samples

- [BLE logging backend](../../../samples/subsys/logging/ble_backend/README.md#logging-ble-backend "Send log messages over BLE using the BLE logging backend.")Send log messages over BLE using the BLE logging backend.
- [Bluetooth Mesh badge](../../../samples/boards/phytec/reel_board/mesh_badge/README.md#mesh_badge "Implement a smart badge using the reel board and Bluetooth Mesh.")Implement a smart badge using the reel board and Bluetooth Mesh.
- [Cycling Speed and Cadence (CSC) Peripheral](../../../samples/bluetooth/peripheral_csc/README.md#ble_peripheral_csc "Expose a Cycling Speed and Cadence (CSC) GATT Service.")Expose a Cycling Speed and Cadence (CSC) GATT Service.
- [DIS Peripheral](../../../samples/bluetooth/peripheral_dis/README.md#ble_peripheral_dis "Expose device information using the Device Information Service (DIS).")Expose device information using the Device Information Service (DIS).
- [ESP Peripheral](../../../samples/bluetooth/peripheral_esp/README.md#ble_peripheral_esp "Expose environmental information using the Environmental Sensing Profile (ESP).")Expose environmental information using the Environmental Sensing Profile (ESP).
- [HID Peripheral](../../../samples/bluetooth/peripheral_hids/README.md#ble_peripheral_hids "Implement a Bluetooth HID peripheral (generic mouse)")Implement a Bluetooth HID peripheral (generic mouse)
- [MTU Update](../../../samples/bluetooth/mtu_update/README.md#bluetooth_mtu_update "Configure and exchange MTU between two devices.")Configure and exchange MTU between two devices.
- [Peripheral](../../../samples/bluetooth/peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).
- [Peripheral Accept List](../../../samples/bluetooth/peripheral_accept_list/README.md#ble_peripheral_accept_list "Advertise and accept connections only from devices on an accept list.")Advertise and accept connections only from devices on an accept list.
- [Peripheral GATT Write](../../../samples/bluetooth/peripheral_gatt_write/README.md#ble_peripheral_gatt_write "Write a value to a characteristic using GATT Write Without Response.")Write a value to a characteristic using GATT Write Without Response.
- [ST Bluetooth LE Sensor Demo](../../../samples/bluetooth/st_ble_sensor/README.md#bluetooth_st_ble_sensor "Export vendor-specific GATT services over BLE.")Export vendor-specific GATT services over BLE.

### GATT Server

[GATT Server APIs](../../../doxygen/html/group__bt__gatt__server.md)

### GATT Client

[GATT Client APIs](../../../doxygen/html/group__bt__gatt__client.md)
