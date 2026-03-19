---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__conn__cb.html
original_path: doxygen/html/structbt__conn__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Connection callback structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#ab3618150bfeea9492095ba27ce978c69) )(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err) |
|  | A new connection has been established. |
| void(\* | [disconnected](#a8b8983b5b5b05c9e2dae242485b6c914) )(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | A connection has been disconnected. |
| void(\* | [recycled](#a1bd8d99988ad0ae3f79aad3d03fcbd8b) )(void) |
|  | A connection object has been returned to the pool. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [le\_param\_req](#a2c52c2e2798062708c373fae9610fadd) )(struct bt\_conn \*conn, struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param) |
|  | LE connection parameter update request. |
| void(\* | [le\_param\_updated](#a01582ed3e3801e10c665534eaa991454) )(struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) interval, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) latency, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout) |
|  | The parameters for an LE connection have been updated. |
| void(\* | [identity\_resolved](#aea9b62ab1a1469be97a207a8e07d2f14) )(struct bt\_conn \*conn, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*rpa, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*identity) |
|  | Remote Identity Address has been resolved. |
| void(\* | [security\_changed](#ae454d5bc2664e90ba2b1e0c867db374e) )(struct bt\_conn \*conn, [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) level, enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) err) |
|  | The security level of a connection has changed. |
| void(\* | [remote\_info\_available](#af726f004c06b86f770ece263ed6c9ca4) )(struct bt\_conn \*conn, struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) \*remote\_info) |
|  | Remote information procedures has completed. |
| void(\* | [le\_phy\_updated](#ae02a23d823954a747f8f474fb19276d7) )(struct bt\_conn \*conn, struct [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md) \*param) |
|  | The PHY of the connection has changed. |
| void(\* | [le\_data\_len\_updated](#a1142d1861cc0b0058f68ecf537d0cec3) )(struct bt\_conn \*conn, struct [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md) \*info) |
|  | The data length parameters of the connection has changed. |

## Detailed Description

Connection callback structure.

This structure is used for tracking the state of a connection. It is registered with the help of the [bt\_conn\_cb\_register()](group__bt__conn.md#gaa9b79cd44734c1e560d6f30509be4d0b "Register connection callbacks.") API. It's permissible to register multiple instances of this [bt\_conn\_cb](structbt__conn__cb.md "bt_conn_cb") type, in case different modules of an application are interested in tracking the connection state. If a callback is not of interest for an instance, it may be set to NULL and will as a consequence not be used for that instance.

## Field Documentation

## [◆ ](#ab3618150bfeea9492095ba27ce978c69)connected

| void(\* bt\_conn\_cb::connected) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err) |
| --- |

A new connection has been established.

This callback notifies the application of a new connection. In case the err parameter is non-zero it means that the connection establishment failed.

Note
:   If the connection was established from an advertising set then the advertising set cannot be restarted directly from this callback. Instead use the connected callback of the advertising set.

Parameters
:   | conn | New connection object. |
    | --- | --- |
    | err | HCI error. Zero for success, non-zero otherwise. |

`err` can mean either of the following:

- [BT\_HCI\_ERR\_UNKNOWN\_CONN\_ID](hci__types_8h.md#afd68afeb0296e3af363d7d60eaf4e9a1 "BT_HCI_ERR_UNKNOWN_CONN_ID") Creating the connection started by [bt\_conn\_le\_create](group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6 "bt_conn_le_create") was canceled either by the user through [bt\_conn\_disconnect](group__bt__conn.md#ga14e7c852b0271781594e742ae509c5d3 "bt_conn_disconnect") or by the timeout in the host through [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md "bt_conn_le_create_param") timeout parameter, which defaults to `CONFIG_BT_CREATE_CONN_TIMEOUT` seconds.
- `BT_HCI_ERR_ADV_TIMEOUT` High duty cycle directed connectable advertiser started by [bt\_le\_adv\_start](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02 "bt_le_adv_start") failed to be connected within the timeout.

## [◆ ](#a8b8983b5b5b05c9e2dae242485b6c914)disconnected

| void(\* bt\_conn\_cb::disconnected) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

A connection has been disconnected.

This callback notifies the application that a connection has been disconnected.

When this callback is called the stack still has one reference to the connection object. If the application in this callback tries to start either a connectable advertiser or create a new connection this might fail because there are no free connection objects available. To avoid this issue it is recommended to either start connectable advertise or create a new connection using [k\_work\_submit](group__workqueue__apis.md#gace61b59575093d7442f39ccb7be686d7 "k_work_submit") or increase `CONFIG_BT_MAX_CONN`.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | reason | BT\_HCI\_ERR\_\* reason for the disconnection. |

## [◆ ](#aea9b62ab1a1469be97a207a8e07d2f14)identity\_resolved

| void(\* bt\_conn\_cb::identity\_resolved) (struct bt\_conn \*conn, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*rpa, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*identity) |
| --- |

Remote Identity Address has been resolved.

This callback notifies the application that a remote Identity Address has been resolved

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | rpa | Resolvable Private Address. |
    | identity | Identity Address. |

## [◆ ](#a1142d1861cc0b0058f68ecf537d0cec3)le\_data\_len\_updated

| void(\* bt\_conn\_cb::le\_data\_len\_updated) (struct bt\_conn \*conn, struct [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md) \*info) |
| --- |

The data length parameters of the connection has changed.

This callback notifies the application that the maximum Link Layer payload length or transmission time has changed.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | info | Connection data length information. |

## [◆ ](#a2c52c2e2798062708c373fae9610fadd)le\_param\_req

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_conn\_cb::le\_param\_req) (struct bt\_conn \*conn, struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param) |
| --- |

LE connection parameter update request.

This callback notifies the application that a remote device is requesting to update the connection parameters. The application accepts the parameters by returning true, or rejects them by returning false. Before accepting, the application may also adjust the parameters to better suit its needs.

It is recommended for an application to have just one of these callbacks for simplicity. However, if an application registers multiple it needs to manage the potentially different requirements for each callback. Each callback gets the parameters as returned by previous callbacks, i.e. they are not necessarily the same ones as the remote originally sent.

If the application does not have this callback then the default is to accept the parameters.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | param | Proposed connection parameters. |

Returns
:   true to accept the parameters, or false to reject them.

## [◆ ](#a01582ed3e3801e10c665534eaa991454)le\_param\_updated

| void(\* bt\_conn\_cb::le\_param\_updated) (struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) interval, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) latency, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout) |
| --- |

The parameters for an LE connection have been updated.

This callback notifies the application that the connection parameters for an LE connection have been updated.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | interval | Connection interval. |
    | latency | Connection latency. |
    | timeout | Connection supervision timeout. |

## [◆ ](#ae02a23d823954a747f8f474fb19276d7)le\_phy\_updated

| void(\* bt\_conn\_cb::le\_phy\_updated) (struct bt\_conn \*conn, struct [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md) \*param) |
| --- |

The PHY of the connection has changed.

This callback notifies the application that the PHY of the connection has changed.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | info | Connection LE PHY information. |

## [◆ ](#a1bd8d99988ad0ae3f79aad3d03fcbd8b)recycled

| void(\* bt\_conn\_cb::recycled) (void) |
| --- |

A connection object has been returned to the pool.

This callback notifies the application that it might be able to allocate a connection object. No guarantee, first come, first serve.

Use this to e.g. re-start connectable advertising or scanning.

Treat this callback as an ISR, as it originates from [bt\_conn\_unref](group__bt__conn.md#ga4b18c6b22a9f02be0d7d078b2ce51ff6 "bt_conn_unref") which is used by the BT stack. Making Bluetooth API calls in this context is error-prone and strongly discouraged.

## [◆ ](#af726f004c06b86f770ece263ed6c9ca4)remote\_info\_available

| void(\* bt\_conn\_cb::remote\_info\_available) (struct bt\_conn \*conn, struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) \*remote\_info) |
| --- |

Remote information procedures has completed.

This callback notifies the application that the remote information has been retrieved from the remote peer.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | remote\_info | Connection information of remote device. |

## [◆ ](#ae454d5bc2664e90ba2b1e0c867db374e)security\_changed

| void(\* bt\_conn\_cb::security\_changed) (struct bt\_conn \*conn, [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) level, enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) err) |
| --- |

The security level of a connection has changed.

This callback notifies the application that the security of a connection has changed.

The security level of the connection can either have been increased or remain unchanged. An increased security level means that the pairing procedure has been performed or the bond information from a previous connection has been applied. If the security level remains unchanged this means that the encryption key has been refreshed for the connection.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | level | New security level of the connection. |
    | err | Security error. Zero for success, non-zero otherwise. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_cb](structbt__conn__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
