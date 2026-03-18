---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__prov.html
original_path: doxygen/html/structbt__mesh__prov.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_prov Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Provisioning](group__bt__mesh__prov.md)

Provisioning properties & capabilities.
[More...](#details)

`#include <[main.h](main_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [uuid](#a1152d77c4c4d9271bbd72514d94052f2) |
|  | The UUID that's used when advertising as unprovisioned. |
| const char \* | [uri](#a6a11cc0d36ca2f4c5aee67a023c295a2) |
|  | Optional URI. |
| [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) | [oob\_info](#a6ed61556291f7f9d9a32062d588b8f2a) |
|  | Out of Band information field. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [public\_key\_be](#a1261ba69e785f005d5834ac49da00778) |
|  | Pointer to Public Key in big-endian for OOB public key type support. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [private\_key\_be](#a1ab714e9be35242e02099884c3af45f5) |
|  | Pointer to Private Key in big-endian for OOB public key type support. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [static\_val](#a97cf41cf857479c8eefee640f7b66788) |
|  | Static OOB value. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [static\_val\_len](#a97394dded5fd55b553364a566a2441e8) |
|  | Static OOB value length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [output\_size](#a4c51aa8e5887b3364d9480c92da3a0a0) |
|  | Maximum size of Output OOB supported. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [output\_actions](#a8b88959c5eef7f47591468e9c9768b7c) |
|  | Supported Output OOB Actions. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [input\_size](#ab9044f6dbf9780b3237f18270b2c8582) |
|  | Maximum size of Input OOB supported. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [input\_actions](#af928a9419f684bcbda0563dda2c34d76) |
|  | Supported Input OOB Actions. |
| void(\* | [capabilities](#afbc65bb8be99f7dc37ecc911f4ac2151) )(const struct [bt\_mesh\_dev\_capabilities](structbt__mesh__dev__capabilities.md) \*cap) |
|  | Provisioning Capabilities. |
| int(\* | [output\_number](#af5c30f061ba8b0a713a3d54068dd68cc) )([bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) act, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num) |
|  | Output of a number is requested. |
| int(\* | [output\_string](#a28284efee6478637446702d7839f6b8c) )(const char \*str) |
|  | Output of a string is requested. |
| int(\* | [input](#a31eff9c903ac721bbca7ab586dda9e80) )([bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) act, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
|  | Input is requested. |
| void(\* | [input\_complete](#a2717ddf38465b95452724078f780f9e5) )(void) |
|  | The other device finished their OOB input. |
| void(\* | [unprovisioned\_beacon](#a8142a3b8120b1686f68513caeac09497) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](#a1152d77c4c4d9271bbd72514d94052f2)[16], [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) [oob\_info](#a6ed61556291f7f9d9a32062d588b8f2a), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*uri\_hash) |
|  | Unprovisioned beacon has been received. |
| void(\* | [unprovisioned\_beacon\_gatt](#a7eddf1f088264f8b6e3fb86dce4c108e) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](#a1152d77c4c4d9271bbd72514d94052f2)[16], [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) [oob\_info](#a6ed61556291f7f9d9a32062d588b8f2a)) |
|  | PB-GATT Unprovisioned Advertising has been received. |
| void(\* | [link\_open](#a44efea3e9221c182cbcacce8219ef6b7) )([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearer) |
|  | Provisioning link has been opened. |
| void(\* | [link\_close](#a0183cef77dda3978ef8a40ce7aad043a) )([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearer) |
|  | Provisioning link has been closed. |
| void(\* | [complete](#ad55abc2b1632455bb23fbd8b03df85ea) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Provisioning is complete. |
| void(\* | [reprovisioned](#ac131476cdeb002f0027407b4cf80c2b5) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Local node has been reprovisioned. |
| void(\* | [node\_added](#aaa49675e358ea4cba7552b3e855befba) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](#a1152d77c4c4d9271bbd72514d94052f2)[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_elem) |
|  | A new node has been added to the provisioning database. |
| void(\* | [reset](#ae87570de25c89e74bece2516ff957779) )(void) |
|  | Node has been reset. |

## Detailed Description

Provisioning properties & capabilities.

## Field Documentation

## [◆ ](#afbc65bb8be99f7dc37ecc911f4ac2151)capabilities

| void(\* bt\_mesh\_prov::capabilities) (const struct [bt\_mesh\_dev\_capabilities](structbt__mesh__dev__capabilities.md) \*cap) |
| --- |

Provisioning Capabilities.

This callback notifies the application that the provisioning capabilities of the unprovisioned device has been received.

The application can consequently call bt\_mesh\_auth\_method\_set\_<\*> to select suitable provisioning oob authentication method.

When this callback returns, the provisioner will start authentication with the chosen method.

Parameters
:   | cap | capabilities supported by device. |
    | --- | --- |

## [◆ ](#ad55abc2b1632455bb23fbd8b03df85ea)complete

| void(\* bt\_mesh\_prov::complete) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
| --- |

Provisioning is complete.

This callback notifies the application that provisioning has been successfully completed, and that the local node has been assigned the specified NetKeyIndex and primary element address.

Parameters
:   | net\_idx | NetKeyIndex given during provisioning. |
    | --- | --- |
    | addr | Primary element address. |

## [◆ ](#a31eff9c903ac721bbca7ab586dda9e80)input

| int(\* bt\_mesh\_prov::input) ([bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) act, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
| --- |

Input is requested.

This callback notifies the application that it should request input from the user using the given action. The requested input will either be a string or a number, and the application needs to consequently call the [bt\_mesh\_input\_string()](group__bt__mesh__prov.md#ga2592abf429b40ef9242bce26f5bd085e "Provide provisioning input OOB string.") or [bt\_mesh\_input\_number()](group__bt__mesh__prov.md#gace8cbf2a6e9144d3118054f234de02ef "Provide provisioning input OOB number.") functions once the data has been acquired from the user.

Parameters
:   | act | Action for inputting data. |
    | --- | --- |
    | num | Maximum size of the inputted data. |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#af928a9419f684bcbda0563dda2c34d76)input\_actions

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_prov::input\_actions |
| --- |

Supported Input OOB Actions.

## [◆ ](#a2717ddf38465b95452724078f780f9e5)input\_complete

| void(\* bt\_mesh\_prov::input\_complete) (void) |
| --- |

The other device finished their OOB input.

This callback notifies the application that it should stop displaying its output OOB value, as the other party finished their OOB input.

## [◆ ](#ab9044f6dbf9780b3237f18270b2c8582)input\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_prov::input\_size |
| --- |

Maximum size of Input OOB supported.

## [◆ ](#a0183cef77dda3978ef8a40ce7aad043a)link\_close

| void(\* bt\_mesh\_prov::link\_close) ([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearer) |
| --- |

Provisioning link has been closed.

This callback notifies the application that a provisioning link has been closed on the given provisioning bearer.

Parameters
:   | bearer | Provisioning bearer. |
    | --- | --- |

## [◆ ](#a44efea3e9221c182cbcacce8219ef6b7)link\_open

| void(\* bt\_mesh\_prov::link\_open) ([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearer) |
| --- |

Provisioning link has been opened.

This callback notifies the application that a provisioning link has been opened on the given provisioning bearer.

Parameters
:   | bearer | Provisioning bearer. |
    | --- | --- |

## [◆ ](#aaa49675e358ea4cba7552b3e855befba)node\_added

| void(\* bt\_mesh\_prov::node\_added) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](#a1152d77c4c4d9271bbd72514d94052f2)[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_elem) |
| --- |

A new node has been added to the provisioning database.

This callback notifies the application that provisioning has been successfully completed, and that a node has been assigned the specified NetKeyIndex and primary element address.

Parameters
:   | net\_idx | NetKeyIndex given during provisioning. |
    | --- | --- |
    | [uuid](#a1152d77c4c4d9271bbd72514d94052f2) | UUID of the added node |
    | addr | Primary element address. |
    | num\_elem | Number of elements that this node has. |

## [◆ ](#a6ed61556291f7f9d9a32062d588b8f2a)oob\_info

| [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) bt\_mesh\_prov::oob\_info |
| --- |

Out of Band information field.

## [◆ ](#a8b88959c5eef7f47591468e9c9768b7c)output\_actions

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_prov::output\_actions |
| --- |

Supported Output OOB Actions.

## [◆ ](#af5c30f061ba8b0a713a3d54068dd68cc)output\_number

| int(\* bt\_mesh\_prov::output\_number) ([bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) act, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num) |
| --- |

Output of a number is requested.

This callback notifies the application that it should output the given number using the given action.

Parameters
:   | act | Action for outputting the number. |
    | --- | --- |
    | num | Number to be outputted. |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#a4c51aa8e5887b3364d9480c92da3a0a0)output\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_prov::output\_size |
| --- |

Maximum size of Output OOB supported.

## [◆ ](#a28284efee6478637446702d7839f6b8c)output\_string

| int(\* bt\_mesh\_prov::output\_string) (const char \*str) |
| --- |

Output of a string is requested.

This callback notifies the application that it should display the given string to the user.

Parameters
:   | str | String to be displayed. |
    | --- | --- |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#a1ab714e9be35242e02099884c3af45f5)private\_key\_be

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_prov::private\_key\_be |
| --- |

Pointer to Private Key in big-endian for OOB public key type support.

Remember to enable `CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY` when initializing this parameter.

Must be used together with [bt\_mesh\_prov::public\_key\_be](#a1261ba69e785f005d5834ac49da00778).

## [◆ ](#a1261ba69e785f005d5834ac49da00778)public\_key\_be

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_prov::public\_key\_be |
| --- |

Pointer to Public Key in big-endian for OOB public key type support.

Remember to enable `CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY` when initializing this parameter.

Must be used together with [bt\_mesh\_prov::private\_key\_be](#a1ab714e9be35242e02099884c3af45f5).

## [◆ ](#ac131476cdeb002f0027407b4cf80c2b5)reprovisioned

| void(\* bt\_mesh\_prov::reprovisioned) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
| --- |

Local node has been reprovisioned.

This callback notifies the application that reprovisioning has been successfully completed.

Parameters
:   | addr | New primary element address. |
    | --- | --- |

## [◆ ](#ae87570de25c89e74bece2516ff957779)reset

| void(\* bt\_mesh\_prov::reset) (void) |
| --- |

Node has been reset.

This callback notifies the application that the local node has been reset and needs to be provisioned again. The node will not automatically advertise as unprovisioned, rather the [bt\_mesh\_prov\_enable()](group__bt__mesh__prov.md#ga6c8dc1b09d4cde8738be83c992b860a9 "Enable specific provisioning bearers.") API needs to be called to enable unprovisioned advertising on one or more provisioning bearers.

## [◆ ](#a97cf41cf857479c8eefee640f7b66788)static\_val

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_prov::static\_val |
| --- |

Static OOB value.

## [◆ ](#a97394dded5fd55b553364a566a2441e8)static\_val\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_prov::static\_val\_len |
| --- |

Static OOB value length.

## [◆ ](#a8142a3b8120b1686f68513caeac09497)unprovisioned\_beacon

| void(\* bt\_mesh\_prov::unprovisioned\_beacon) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](#a1152d77c4c4d9271bbd72514d94052f2)[16], [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) [oob\_info](#a6ed61556291f7f9d9a32062d588b8f2a), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*uri\_hash) |
| --- |

Unprovisioned beacon has been received.

This callback notifies the application that an unprovisioned beacon has been received.

Parameters
:   | [uuid](#a1152d77c4c4d9271bbd72514d94052f2) | UUID |
    | --- | --- |
    | [oob\_info](#a6ed61556291f7f9d9a32062d588b8f2a) | OOB Information |
    | uri\_hash | Pointer to URI Hash value. NULL if no hash was present in the beacon. |

## [◆ ](#a7eddf1f088264f8b6e3fb86dce4c108e)unprovisioned\_beacon\_gatt

| void(\* bt\_mesh\_prov::unprovisioned\_beacon\_gatt) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](#a1152d77c4c4d9271bbd72514d94052f2)[16], [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) [oob\_info](#a6ed61556291f7f9d9a32062d588b8f2a)) |
| --- |

PB-GATT Unprovisioned Advertising has been received.

This callback notifies the application that an PB-GATT unprovisioned Advertising has been received.

Parameters
:   | [uuid](#a1152d77c4c4d9271bbd72514d94052f2) | UUID |
    | --- | --- |
    | [oob\_info](#a6ed61556291f7f9d9a32062d588b8f2a) | OOB Information |

## [◆ ](#a6a11cc0d36ca2f4c5aee67a023c295a2)uri

| const char\* bt\_mesh\_prov::uri |
| --- |

Optional URI.

This will be advertised separately from the unprovisioned beacon, however the unprovisioned beacon will contain a hash of it so the two can be associated by the provisioner.

## [◆ ](#a1152d77c4c4d9271bbd72514d94052f2)uuid

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_prov::uuid |
| --- |

The UUID that's used when advertising as unprovisioned.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[main.h](main_8h_source.md)

- [bt\_mesh\_prov](structbt__mesh__prov.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
