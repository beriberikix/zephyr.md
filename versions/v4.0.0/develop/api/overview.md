---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/develop/api/overview.html
original_path: develop/api/overview.html
---

# API Overview

The table lists Zephyr’s APIs and information about them, including their
current [stability level](api_lifecycle.md#api-lifecycle). More details about API changes
between major releases are available in the [Releases](../../releases/index.md#zephyr-release-notes).

The version column uses [semantic version](https://semver.org/), and has the
following expectations:

> - Major version zero (0.y.z) is for initial development. Anything MAY
>   change at any time. The public API SHOULD NOT be considered stable.
>
>   - If minor version is up to one (0.1.z), API is considered
>     [experimental](api_lifecycle.md#api-lifecycle-experimental).
>   - If minor version is larger than one (0.y.z | y > 1), API is considered
>     [unstable](api_lifecycle.md#api-lifecycle-unstable).
> - Version 1.0.0 defines the public API. The way in which the version number
>   is incremented after this release is dependent on this public API and how it
>   changes.
>
>   - APIs with major versions equal or larger than one (x.y.z | x >= 1 ) are
>     considered [stable](api_lifecycle.md#api-lifecycle-stable).
>   - All existing stable APIs in Zephyr will be start with version 1.0.0.
> - Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards
>   compatible bug fixes are introduced. A bug fix is defined as an internal
>   change that fixes incorrect behavior.
> - Minor version Y (x.Y.z | x > 0) MUST be incremented if new, backwards
>   compatible functionality is introduced to the public API. It MUST be
>   incremented if any public API functionality is marked as deprecated. It MAY
>   be incremented if substantial new functionality or improvements are
>   introduced within the private code. It MAY include patch level changes.
>   Patch version MUST be reset to 0 when minor version is incremented.
> - Major version X (x.Y.z | x > 0) MUST be incremented if a compatibility
>   breaking change was made to the API.

Note

Version for existing APIs are initially set based on the current state of the
APIs:

> - 0.1.0 denotes an [experimental](api_lifecycle.md#api-lifecycle-experimental) API
> - 0.8.0 denote an [unstable](api_lifecycle.md#api-lifecycle-unstable) API,
> - and finally 1.0.0 indicates a [stable](api_lifecycle.md#api-lifecycle-stable) APIs.

Changes to APIs in the future will require adapting the version following the
guidelines above.

| API | Version | Available in Zephyr Since |
| --- | --- | --- |
| [Audio](../../doxygen/html/group__audio__interface.md) |  |  |
| [Audio Codec Interface](../../doxygen/html/group__audio__codec__interface.md) | 0.1.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [Digital Microphone Interface](../../doxygen/html/group__audio__dmic__interface.md) | 0.1.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [Connectivity](../../doxygen/html/group__connectivity.md) |  |  |
| [Bluetooth APIs](../../doxygen/html/group__bluetooth.md) |  |  |
| [Attribute Protocol (ATT)](../../doxygen/html/group__bt__att.md) |  |  |
| [Audio Input Control Service (AICS)](../../doxygen/html/group__bt__aics.md) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.6.0) |
| [Basic Audio Profile (BAP) LC3 Presets](../../doxygen/html/group__bt__bap__lc3__preset.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Battery Service (BAS)](../../doxygen/html/group__bt__bas.md) |  |  |
| [BlueNRG HCI driver extended API](../../doxygen/html/group__bluenrg__hci__driver.md) |  |  |
| [Bluetooth Audio](../../doxygen/html/group__bt__audio.md) |  |  |
| [Assigned numbers to string API](../../doxygen/html/group__bt__audio__to__str.md) |  |  |
| [Codec capability parsing APIs](../../doxygen/html/group__bt__audio__codec__cap.md) |  |  |
| [Codec config parsing APIs](../../doxygen/html/group__bt__audio__codec__cfg.md) |  |  |
| [Bluetooth Basic Audio Profile](../../doxygen/html/group__bt__bap.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [BAP Broadcast APIs](../../doxygen/html/group__bt__bap__broadcast.md) |  |  |
| [BAP Broadcast Sink APIs](../../doxygen/html/group__bt__bap__broadcast__sink.md) |  |  |
| [BAP Broadcast Source APIs](../../doxygen/html/group__bt__bap__broadcast__source.md) |  |  |
| [BAP Broadcast Sink APIs](../../doxygen/html/group__bt__bap__broadcast__sink.md) |  |  |
| [BAP Broadcast Source APIs](../../doxygen/html/group__bt__bap__broadcast__source.md) |  |  |
| [BAP Unicast Client APIs](../../doxygen/html/group__bt__bap__unicast__client.md) |  |  |
| [BAP Unicast Server APIs](../../doxygen/html/group__bt__bap__unicast__server.md) |  |  |
| [Bluetooth Content Control Identifier](../../doxygen/html/group__bt__ccid.md) | 0.8.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.7.0) |
| [Bluetooth Controller](../../doxygen/html/group__bt__ctrl.md) |  |  |
| [Bluetooth Gaming Audio Profile](../../doxygen/html/group__bt__gmap.md) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [Bluetooth HCI APIs](../../doxygen/html/group__bt__hci__api.md) | 0.2.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.7.0) |
| [Bluetooth LC3 codec](../../doxygen/html/group__bt__lc3.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Bluetooth Mesh](../../doxygen/html/group__bt__mesh.md) |  |  |
| [Access layer](../../doxygen/html/group__bt__mesh__access.md) |  |  |
| [Bluetooth Mesh BLOB Transfer Client model API](../../doxygen/html/group__bt__mesh__blob__cli.md) |  |  |
| [Bluetooth Mesh BLOB Transfer Server model API](../../doxygen/html/group__bt__mesh__blob__srv.md) |  |  |
| [Bluetooth Mesh BLOB flash stream](../../doxygen/html/group__bt__mesh__blob__io__flash.md) |  |  |
| [Bluetooth Mesh BLOB model API](../../doxygen/html/group__bt__mesh__blob.md) |  |  |
| [Bluetooth Mesh Device Firmware Update](../../doxygen/html/group__bt__mesh__dfu.md) |  |  |
| [Bluetooth Mesh Device Firmware Update (DFU) metadata](../../doxygen/html/group__bt__mesh__dfu__metadata.md) |  |  |
| [Firmware Update Server model](../../doxygen/html/group__bt__mesh__dfu__srv.md) |  |  |
| [Firmware Uppdate Client model](../../doxygen/html/group__bt__mesh__dfu__cli.md) |  |  |
| [Bluetooth Mesh On-Demand Private GATT Proxy Client](../../doxygen/html/group__bt__mesh__od__priv__proxy__cli.md) |  |  |
| [Bluetooth Mesh On-Demand Private GATT Proxy Server](../../doxygen/html/group__bt__mesh__od__priv__proxy__srv.md) |  |  |
| [Bluetooth Mesh Private Beacon Client](../../doxygen/html/group__bt__mesh__priv__beacon__cli.md) |  |  |
| [Bluetooth Mesh Private Beacon Server](../../doxygen/html/group__bt__mesh__priv__beacon__srv.md) |  |  |
| [Bluetooth Mesh SAR Configuration Client Model](../../doxygen/html/group__bt__mesh__sar__cfg__cli.md) |  |  |
| [Bluetooth Mesh SAR Configuration Server Model](../../doxygen/html/group__bt__mesh__sar__cfg__srv.md) |  |  |
| [Bluetooth Mesh Solicitation PDU RPL Client](../../doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.md) |  |  |
| [Bluetooth Mesh Solicitation PDU RPL Server](../../doxygen/html/group__bt__mesh__sol__pdu__rpl__srv.md) |  |  |
| [Bridge Configuration Client Model](../../doxygen/html/group__bt__mesh__brg__cfg__cli.md) |  |  |
| [Bridge Configuration Server Model](../../doxygen/html/group__bt__mesh__brg__cfg__srv.md) |  |  |
| [Bridge Configuration common header](../../doxygen/html/group__bt__mesh__brg__cfg.md) |  |  |
| [Configuration Client Model](../../doxygen/html/group__bt__mesh__cfg__cli.md) |  |  |
| [Configuration Server Model](../../doxygen/html/group__bt__mesh__cfg__srv.md) |  |  |
| [Firmware Distribution models](../../doxygen/html/group__bt__mesh__dfd.md) |  |  |
| [Firmware Distribution Server model](../../doxygen/html/group__bt__mesh__dfd__srv.md) |  |  |
| [Health Client Model](../../doxygen/html/group__bt__mesh__health__cli.md) |  |  |
| [Health Server Model](../../doxygen/html/group__bt__mesh__health__srv.md) |  |  |
| [Health faults](../../doxygen/html/group__bt__mesh__health__faults.md) |  |  |
| [Heartbeat](../../doxygen/html/group__bt__mesh__heartbeat.md) |  |  |
| [Large Composition Data Client model](../../doxygen/html/group__bt__mesh__large__comp__data__cli.md) |  |  |
| [Large Composition Data Server model](../../doxygen/html/group__bt__mesh__large__comp__data__srv.md) |  |  |
| [Message](../../doxygen/html/group__bt__mesh__msg.md) |  |  |
| [Opcodes Aggregator Client model](../../doxygen/html/group__bt__mesh__op__agg__cli.md) |  |  |
| [Opcodes Aggregator Server model](../../doxygen/html/group__bt__mesh__op__agg__srv.md) |  |  |
| [Provisioning](../../doxygen/html/group__bt__mesh__prov.md) |  |  |
| [Proxy](../../doxygen/html/group__bt__mesh__proxy.md) |  |  |
| [Remote Provisioning Client model](../../doxygen/html/group__bt__mesh__rpr__cli.md) |  |  |
| [Remote Provisioning models](../../doxygen/html/group__bt__mesh__rpr.md) |  |  |
| [Remote provisioning server](../../doxygen/html/group__bt__mesh__rpr__srv.md) |  |  |
| [Runtime Configuration](../../doxygen/html/group__bt__mesh__cfg.md) |  |  |
| [Application Configuration](../../doxygen/html/group__bt__mesh__cfg__app.md) |  |  |
| [Subnet Configuration](../../doxygen/html/group__bt__mesh__cfg__subnet.md) |  |  |
| [SAR Configuration common header](../../doxygen/html/group__bt__mesh__sar__cfg.md) |  |  |
| [Statistic](../../doxygen/html/group__bt__mesh__stat.md) |  |  |
| [Byteorder](../../doxygen/html/group__bt__byteorder.md) |  |  |
| [Channel Sounding (CS)](../../doxygen/html/group__bt__le__cs.md) |  |  |
| [Common Audio Profile (CAP)](../../doxygen/html/group__bt__cap.md) | 0.8.0 | [v3.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.2.0) |
| [Connection management](../../doxygen/html/group__bt__conn.md) |  |  |
| [Coordinated Set Identification Profile (CSIP)](../../doxygen/html/group__bt__csip.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Cryptography](../../doxygen/html/group__bt__crypto.md) |  |  |
| [Current Time Service (CTS)](../../doxygen/html/group__bt__cts.md) |  |  |
| [Data buffers](../../doxygen/html/group__bt__buf.md) |  |  |
| [Device Address](../../doxygen/html/group__bt__addr.md) |  |  |
| [Encrypted Advertising Data (EAD)](../../doxygen/html/group__bt__ead.md) |  |  |
| [Gaming Audio Profile (GMAP) LC3 Presets](../../doxygen/html/group__bt__gmap__lc3__preset.md) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [Generic Access Profile (GAP)](../../doxygen/html/group__bt__gap.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Defines and Assigned Numbers](../../doxygen/html/group__bt__gap__defines.md) |  |  |
| [Generic Attribute Profile (GATT)](../../doxygen/html/group__bt__gatt.md) |  |  |
| [GATT Client APIs](../../doxygen/html/group__bt__gatt__client.md) |  |  |
| [GATT Server APIs](../../doxygen/html/group__bt__gatt__server.md) |  |  |
| [HCI RAW channel](../../doxygen/html/group__hci__raw.md) |  |  |
| [HCI drivers](../../doxygen/html/group__bt__hci__driver.md) |  |  |
| [Hands Free Profile (HFP)](../../doxygen/html/group__bt__hfp.md) |  |  |
| [Hands Free Profile - Audio Gateway (HFP-AG)](../../doxygen/html/group__bt__hfp__ag.md) |  |  |
| [Hearing Access Service (HAS)](../../doxygen/html/group__bt__has.md) | 0.8.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.1.0) |
| [Heart Rate Service (HRS)](../../doxygen/html/group__bt__hrs.md) |  |  |
| [Immediate Alert Service (IAS)](../../doxygen/html/group__bt__ias.md) |  |  |
| [Isochronous channels (ISO)](../../doxygen/html/group__bt__iso.md) | 0.8.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.3.0) |
| [L2CAP](../../doxygen/html/group__bt__l2cap.md) |  |  |
| [Media Control Client (MCC)](../../doxygen/html/group__bt__mcc.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Media Control Service (MCS)](../../doxygen/html/group__bt__mcs.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Media Proxy](../../doxygen/html/group__bt__media__proxy.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Microphone Control Profile (MICP)](../../doxygen/html/group__bt__micp.md) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.7.0) |
| [Object Transfer Service (OTS)](../../doxygen/html/group__bt__ots.md) |  |  |
| [Public Broadcast Profile (PBP)](../../doxygen/html/group__bt__pbp.md) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [Published Audio Capabilities Service (PACS)](../../doxygen/html/group__bt__pacs.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [RFCOMM](../../doxygen/html/group__bt__rfcomm.md) |  |  |
| [Service Discovery Protocol (SDP)](../../doxygen/html/group__bt__sdp.md) |  |  |
| [Telephone Bearer Service (TBS)](../../doxygen/html/group__bt__tbs.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Telephone and Media Audio Profile (TMAP)](../../doxygen/html/group__bt__tmap.md) | 0.8.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [UUIDs](../../doxygen/html/group__bt__uuid.md) |  |  |
| [Volume Control Profile (VCP)](../../doxygen/html/group__bt__vcp.md) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.7.0) |
| [Volume Offset Control Service (VOCS)](../../doxygen/html/group__bt__vocs.md) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.6.0) |
| [CAN ISO-TP Protocol](../../doxygen/html/group__can__isotp.md) |  |  |
| [IEEE 802.15.4 and Thread APIs](../../doxygen/html/group__ieee802154.md) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [IEEE 802.15.4 Drivers](../../doxygen/html/group__ieee802154__driver.md) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [IEEE 802.15.4 L2](../../doxygen/html/group__ieee802154__l2.md) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [IEEE 802.15.4 Net Management](../../doxygen/html/group__ieee802154__mgmt.md) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [OpenThread L2 abstraction layer](../../doxygen/html/group__openthread.md) | 0.8.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.11.0) |
| [LoRaWAN APIs](../../doxygen/html/group__lorawan__api.md) | 0.1.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.5.0) |
| [Modem APIs](../../doxygen/html/group__modem.md) | 0.1.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [Modem CMUX](../../doxygen/html/group__modem__cmux.md) |  |  |
| [Modem PPP](../../doxygen/html/group__modem__ppp.md) |  |  |
| [Modem Pipe](../../doxygen/html/group__modem__pipe.md) |  |  |
| [Modem Ubx](../../doxygen/html/group__modem__ubx.md) |  |  |
| [Modem pipelink](../../doxygen/html/group__modem__pipelink.md) |  |  |
| [Networking](../../doxygen/html/group__networking.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Application network context](../../doxygen/html/group__net__context.md) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [BSD Sockets compatible API](../../doxygen/html/group__bsd__sockets.md) | 1.0.0 | [v1.9.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.9.0) |
| [Socket options for TLS](../../doxygen/html/group__secure__sockets__options.md) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [BSD socket service API](../../doxygen/html/group__bsd__socket__service.md) | 0.2.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.6.0) |
| [COAP Library](../../doxygen/html/group__coap.md) | 0.8.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.10.0) |
| [CoAP Manager Events](../../doxygen/html/group__coap__mgmt.md) | 0.1.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.6.0) |
| [CoAP client API](../../doxygen/html/group__coap__client.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [CoAP service API](../../doxygen/html/group__coap__service.md) | 0.1.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.6.0) |
| [Connection Manager API](../../doxygen/html/group__conn__mgr.md) | 0.1.0 | [v2.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.0.0) |
| [Connection Manager Connectivity API](../../doxygen/html/group__conn__mgr__connectivity.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [Connection Manager Connectivity Bulk API](../../doxygen/html/group__conn__mgr__connectivity__bulk.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [Connection Manager Connectivity Implementation API](../../doxygen/html/group__conn__mgr__connectivity__impl.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [DHCPv4](../../doxygen/html/group__dhcpv4.md) | 0.8.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.7.0) |
| [DHCPv4 server](../../doxygen/html/group__dhcpv4__server.md) | 0.8.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.6.0) |
| [DHCPv6](../../doxygen/html/group__dhcpv6.md) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [DNS Resolve Library](../../doxygen/html/group__dns__resolve.md) | 0.8.0 | [v1.8.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.8.0) |
| [DNS Service Discovery](../../doxygen/html/group__dns__sd.md) | 0.8.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.5.0) |
| [Distributed Switch Architecture definitions and helpers](../../doxygen/html/group__DSA.md) | 0.8.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.5.0) |
| [Dummy L2/driver Support Functions](../../doxygen/html/group__dummy.md) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.14.0) |
| [Ethernet Bridging API](../../doxygen/html/group__eth__bridge.md) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.7.0) |
| [Ethernet Library](../../doxygen/html/group__ethernet__mgmt.md) | 0.8.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.12.0) |
| [Ethernet PHY Interface](../../doxygen/html/group__ethernet__phy.md) | 0.8.0 | [v2.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.7.0) |
| [Ethernet Support Functions](../../doxygen/html/group__ethernet.md) | 0.8.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Ethernet MII Support Functions](../../doxygen/html/group__ethernet__mii.md) | 0.8.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.7.0) |
| [IEEE 802.3 management interface](../../doxygen/html/group__ethernet__mdio.md) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [HTTP HPACK](../../doxygen/html/group__http__hpack.md) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.7.0) |
| [HTTP client API](../../doxygen/html/group__http__client.md) | 0.2.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.1.0) |
| [HTTP request methods](../../doxygen/html/group__http__methods.md) | 0.8.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [HTTP response status codes](../../doxygen/html/group__http__status__codes.md) | 0.8.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [HTTP server API](../../doxygen/html/group__http__server.md) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.7.0) |
| [HTTP service API](../../doxygen/html/group__http__service.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [IGMP API](../../doxygen/html/group__igmp.md) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.6.0) |
| [IPv4/IPv6 primitives and helpers](../../doxygen/html/group__ip__4__6.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Link Layer Discovery Protocol definitions and helpers](../../doxygen/html/group__lldp.md) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [LwM2M high-level API](../../doxygen/html/group__lwm2m__api.md) | 0.8.0 | [v1.9.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.9.0) |
| [LwM2M path helper macros](../../doxygen/html/group__lwm2m__path__helpers.md) | 0.8.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.5.0) |
| [MQTT Client library](../../doxygen/html/group__mqtt__socket.md) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.14.0) |
| [MQTT-SN Client library](../../doxygen/html/group__mqtt__sn__socket.md) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [Multicast Listener Discovery API](../../doxygen/html/group__mld.md) | 0.8.0 | [v1.8.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.8.0) |
| [Network Configuration Library](../../doxygen/html/group__net__config.md) | 0.8.0 | [v1.8.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.8.0) |
| [Network Core Library](../../doxygen/html/group__net__core.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Network Hostname Library](../../doxygen/html/group__net__hostname.md) | 0.8.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.10.0) |
| [Network Interface abstraction layer](../../doxygen/html/group__net__if.md) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.5.0) |
| [Network L2 Abstraction Layer](../../doxygen/html/group__net__l2.md) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.5.0) |
| [Network Link Address Library](../../doxygen/html/group__net__linkaddr.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Network Management](../../doxygen/html/group__net__mgmt.md) | 1.0.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.7.0) |
| [Network Offloading Interface](../../doxygen/html/group__net__offload.md) | 0.8.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.7.0) |
| [Network Packet Filter API](../../doxygen/html/group__net__pkt__filter.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Basic Filter Conditions](../../doxygen/html/group__npf__basic__cond.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Ethernet Filter Conditions](../../doxygen/html/group__npf__eth__cond.md) | 0.8.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Network Packet Library](../../doxygen/html/group__net__pkt.md) | 0.8.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.5.0) |
| [Network Statistics Library](../../doxygen/html/group__net__stats.md) | 0.8.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.5.0) |
| [Network long timeout primitives and helpers](../../doxygen/html/group__net__timeout.md) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.14.0) |
| [Network packet capture](../../doxygen/html/group__net__capture.md) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.6.0) |
| [Network time representation.](../../doxygen/html/group__net__time.md) | 0.1.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [Offloaded Net Devices](../../doxygen/html/group__offloaded__netdev.md) | 0.8.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [PPP L2/driver Support Functions](../../doxygen/html/group__ppp.md) | 0.8.0 | [v2.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.0.0) |
| [PTP support](../../doxygen/html/group__ptp.md) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.7.0) |
| [PTP time](../../doxygen/html/group__ptp__time.md) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [Prometheus API](../../doxygen/html/group__prometheus.md) | 0.1.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v4.0.0) |
| [Promiscuous mode](../../doxygen/html/group__promiscuous.md) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [SNTP](../../doxygen/html/group__sntp.md) | 0.8.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.10.0) |
| [Send and receive IPv4 or IPv6 ICMP Echo Request messages.](../../doxygen/html/group__icmp.md) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [Socket NET\_MGMT library](../../doxygen/html/group__socket__net__mgmt.md) | 0.1.0 | [v2.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.0.0) |
| [SocketCAN library](../../doxygen/html/group__socket__can.md) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.14.0) |
| [TFTP Client library](../../doxygen/html/group__tftp__client.md) | 0.1.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.3.0) |
| [TLS credentials management](../../doxygen/html/group__tls__credentials.md) | 0.8.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [Trickle Algorithm Library](../../doxygen/html/group__trickle.md) | 0.8.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.7.0) |
| [Virtual Interface Library](../../doxygen/html/group__virtual__mgmt.md) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.6.0) |
| [Virtual LAN definitions and helpers](../../doxygen/html/group__vlan__api.md) | 0.8.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.12.0) |
| [Virtual Network Interface Support Functions](../../doxygen/html/group__virtual.md) | 0.8.0 | [v2.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.6.0) |
| [Websocket API](../../doxygen/html/group__websocket.md) | 0.1.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.12.0) |
| [Wi-Fi Management](../../doxygen/html/group__wifi__mgmt.md) | 0.8.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.12.0) |
| [Wi-Fi Network Manager API](../../doxygen/html/group__wifi__nm.md) | 0.8.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [Wi-Fi credentials library](../../doxygen/html/group__wifi__credentials.md) | 0.1.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v4.0.0) |
| [Zperf API](../../doxygen/html/group__zperf.md) | 0.8.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [gPTP support](../../doxygen/html/group__gptp.md) | 0.1.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [USB](../../doxygen/html/group__usb.md) |  |  |
| [Buffer macros and definitions used in USB device support](../../doxygen/html/group__udc__buf.md) | 0.1.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v4.0.0) |
| [USB Audio Class 2 device API](../../doxygen/html/group__uac2__device.md) | 0.1.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.6.0) |
| [USB BOS support](../../doxygen/html/group__usb__bos.md) | 1.0.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [USB HID class API](../../doxygen/html/group__usb__hid__class.md) | 1.0.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.11.0) |
| [HID class USB specific definitions](../../doxygen/html/group__usb__hid__device__api.md) |  |  |
| [USB HID common definitions](../../doxygen/html/group__usb__hid__definitions.md) | 1.0.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.11.0) |
| [Mouse and keyboard report descriptors](../../doxygen/html/group__usb__hid__mk__report__desc.md) |  |  |
| [USB HID Item helpers](../../doxygen/html/group__usb__hid__items.md) |  |  |
| [USB Host Core API](../../doxygen/html/group__usb__host__core__api.md) |  |  |
| [USB Mass Storage Class device API](../../doxygen/html/group__usbd__msc__device.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [USB device core API](../../doxygen/html/group__usbd__api.md) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [USB device core API](../../doxygen/html/group__usbd__msg__api.md) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.7.0) |
| [USBD HID device API](../../doxygen/html/group__usbd__hid__device.md) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.7.0) |
| [Coresight APIs](../../doxygen/html/group__coresight__apis.md) |  |  |
| [Coresight Trace Deformatter](../../doxygen/html/group__cs__trace__defmt.md) |  |  |
| [DSP Interface](../../doxygen/html/group__math__dsp.md) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [Basic Math Functions](../../doxygen/html/group__math__dsp__basic.md) |  |  |
| [Vector Absolute Value](../../doxygen/html/group__math__dsp__basic__abs.md) |  |  |
| [Vector Addition](../../doxygen/html/group__math__dsp__basic__add.md) |  |  |
| [Vector Clipping](../../doxygen/html/group__math__dsp__basic__clip.md) |  |  |
| [Vector Dot Product](../../doxygen/html/group__math__dsp__basic__dot.md) |  |  |
| [Vector Multiplication](../../doxygen/html/group__math__dsp__basic__mult.md) |  |  |
| [Vector Negate](../../doxygen/html/group__math__dsp__basic__negate.md) |  |  |
| [Vector Offset](../../doxygen/html/group__math__dsp__basic__offset.md) |  |  |
| [Vector Scale](../../doxygen/html/group__math__dsp__basic__scale.md) |  |  |
| [Vector Shift](../../doxygen/html/group__math__dsp__basic__shift.md) |  |  |
| [Vector Subtraction](../../doxygen/html/group__math__dsp__basic__sub.md) |  |  |
| [Vector bitwise AND](../../doxygen/html/group__math__dsp__basic__and.md) |  |  |
| [Vector bitwise NOT](../../doxygen/html/group__math__dsp__basic__not.md) |  |  |
| [Vector bitwise OR](../../doxygen/html/group__math__dsp__basic__or.md) |  |  |
| [Vector bitwise XOR](../../doxygen/html/group__math__dsp__basic__xor.md) |  |  |
| [Helper macros for printing Q values.](../../doxygen/html/group__math__printing.md) |  |  |
| [Device Driver APIs](../../doxygen/html/group__io__interfaces.md) |  |  |
| [1-Wire Interface](../../doxygen/html/group__w1__interface.md) | 0.1.0 | [v3.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.2.0) |
| [1-Wire Sensor API](../../doxygen/html/group__w1__sensor.md) |  |  |
| [1-Wire data link layer](../../doxygen/html/group__w1__data__link.md) |  |  |
| [1-Wire network layer](../../doxygen/html/group__w1__network.md) |  |  |
| [ADC driver APIs](../../doxygen/html/group__adc__interface.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Emulated ADC](../../doxygen/html/group__adc__emul.md) |  |  |
| [Analog axis API](../../doxygen/html/group__input__analog__axis.md) |  |  |
| [BBRAM Interface](../../doxygen/html/group__bbram__interface.md) |  |  |
| [BBRAM emulator backend API](../../doxygen/html/group__bbram__emulator__backend.md) |  |  |
| [BC1.2 backed emulator APIs](../../doxygen/html/group__b12__emulator__backend.md) |  |  |
| [BC1.2 driver APIs](../../doxygen/html/group__b12__interface.md) |  |  |
| [CAN Interface](../../doxygen/html/group__can__interface.md) | 1.1.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.12.0) |
| [CAN Transceiver](../../doxygen/html/group__can__transceiver.md) | 0.1.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.1.0) |
| [Cache Controller Interface](../../doxygen/html/group__cache__arch__interface.md) |  |  |
| [Cellular Interface](../../doxygen/html/group__cellular__interface.md) |  |  |
| [Charger Interface](../../doxygen/html/group__charger__interface.md) |  |  |
| [Clock Control Interface](../../doxygen/html/group__clock__control__interface.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [LiteX Clock Control driver interface](../../doxygen/html/group__clock__control__litex__interface.md) |  |  |
| [Comparator Interface](../../doxygen/html/group__comparator__interface.md) | 0.1.0 | [v4.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v4.0.0) |
| [Coredump pseudo-device driver APIs](../../doxygen/html/group__coredump__device__interface.md) |  |  |
| [Counter Interface](../../doxygen/html/group__counter__interface.md) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.14.0) |
| [DAC driver APIs](../../doxygen/html/group__dac__interface.md) | 0.8.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.3.0) |
| [DAI Interface](../../doxygen/html/group__dai__interface.md) | 0.1.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.1.0) |
| [DMA Interface](../../doxygen/html/group__dma__interface.md) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.5.0) |
| [Disk Driver Interface](../../doxygen/html/group__disk__driver__interface.md) | 1.0.0 | [v1.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.6.0) |
| [Display Interface](../../doxygen/html/group__display__interface.md) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.14.0) |
| [LCD Interface](../../doxygen/html/group__lcd__interface.md) |  |  |
| [EC Host Command Interface](../../doxygen/html/group__ec__host__cmd__interface.md) | 0.1.0 | [v2.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.4.0) |
| [EDAC API](../../doxygen/html/group__edac.md) | 0.8.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.5.0) |
| [EEPROM Interface](../../doxygen/html/group__eeprom__interface.md) | 1.0.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.1.0) |
| [ESPI Driver APIs](../../doxygen/html/group__espi__interface.md) |  |  |
| [Entropy Interface](../../doxygen/html/group__entropy__interface.md) | 1.0.0 | [v1.10.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.10.0) |
| [External Cache Controller Interface](../../doxygen/html/group__cache__external__interface.md) |  |  |
| [FLASH Interface](../../doxygen/html/group__flash__interface.md) | 1.0.0 | [v1.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.2.0) |
| [FLASH internal Interface](../../doxygen/html/group__flash__internal__interface.md) |  |  |
| [Fuel Gauge Interface](../../doxygen/html/group__fuel__gauge__interface.md) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [Fuel gauge backend emulator APIs](../../doxygen/html/group__fuel__gauge__emulator__backend.md) |  |  |
| [GNSS Interface](../../doxygen/html/group__gnss__interface.md) | 0.1.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.6.0) |
| [GPIO Driver APIs](../../doxygen/html/group__gpio__interface.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Emulated GPIO](../../doxygen/html/group__gpio__emul.md) |  |  |
| [MAX32-specific GPIO Flags](../../doxygen/html/group__gpio__interface__max32.md) |  |  |
| [nPM1300-specific GPIO Flags](../../doxygen/html/group__gpio__interface__npm1300.md) |  |  |
| [nPM6001-specific GPIO Flags](../../doxygen/html/group__gpio__interface__npm6001.md) |  |  |
| [nRF-specific GPIO Flags](../../doxygen/html/group__gpio__interface__nrf.md) |  |  |
| [HW spinlock Interface](../../doxygen/html/group__hwspinlock__interface.md) |  |  |
| [Haptics Interface](../../doxygen/html/group__haptics__interface.md) |  |  |
| [Hardware Info Interface](../../doxygen/html/group__hwinfo__interface.md) | 1.0.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.14.0) |
| [I2C EEPROM Target Driver API](../../doxygen/html/group__i2c__eeprom__target__api.md) | 1.0.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [I2C Interface](../../doxygen/html/group__i2c__interface.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [I2S Interface](../../doxygen/html/group__i2s__interface.md) | 1.0.0 | [v1.9.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.9.0) |
| [I3C Interface](../../doxygen/html/group__i3c__interface.md) | 0.1.0 | [v3.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.2.0) |
| [I3C Address-related Helper Code](../../doxygen/html/group__i3c__addresses.md) |  |  |
| [I3C Common Command Codes](../../doxygen/html/group__i3c__ccc.md) |  |  |
| [I3C Devicetree related bits](../../doxygen/html/group__i3c__devicetree.md) |  |  |
| [I3C HDR DDR API](../../doxygen/html/group__i3c__hdr__ddr.md) |  |  |
| [I3C In-Band Interrupts](../../doxygen/html/group__i3c__ibi.md) |  |  |
| [I3C Target Device API](../../doxygen/html/group__i3c__target__device.md) |  |  |
| [I3C Transfer API](../../doxygen/html/group__i3c__transfer__api.md) |  |  |
| [IPM Interface](../../doxygen/html/group__ipm__interface.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Input Interface](../../doxygen/html/group__input__interface.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [Input Event Definitions](../../doxygen/html/group__input__events.md) |  |  |
| [Inter-VM Shared Memory (ivshmem) reference API](../../doxygen/html/group__ivshmem.md) |  |  |
| [Keyboard Matrix API](../../doxygen/html/group__input__kbd__matrix.md) |  |  |
| [Keyboard Scan Driver APIs](../../doxygen/html/group__kscan__interface.md) | 1.0.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.1.0) |
| [LED Interface](../../doxygen/html/group__led__interface.md) | 1.0.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.12.0) |
| [LED Strip Interface](../../doxygen/html/group__led__strip__interface.md) |  |  |
| [LoRa APIs](../../doxygen/html/group__lora__api.md) | 0.1.0 | [v2.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.2.0) |
| [MBOX Interface](../../doxygen/html/group__mbox__interface.md) | 0.1.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [MDIO Interface](../../doxygen/html/group__mdio__interface.md) |  |  |
| [MIPI Display interface](../../doxygen/html/group__mipi__interface.md) |  |  |
| [MIPI-DBI driver APIs](../../doxygen/html/group__mipi__dbi__interface.md) | 0.1.0 | [v3.6.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.6.0) |
| [MIPI-DSI driver APIs](../../doxygen/html/group__mipi__dsi__interface.md) | 0.1.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.1.0) |
| [MODBUS](../../doxygen/html/group__modbus.md) |  |  |
| [MSPI Devicetree related macros](../../doxygen/html/group__mspi__devicetree.md) |  |  |
| [MSPI Driver APIs](../../doxygen/html/group__mspi__interface.md) |  |  |
| [MSPI Configure API](../../doxygen/html/group__mspi__configure__api.md) |  |  |
| [MSPI Transfer API](../../doxygen/html/group__mspi__transfer__api.md) |  |  |
| [MSPI callback API](../../doxygen/html/group__mspi__callback__api.md) |  |  |
| [Miscellaneous Drivers APIs](../../doxygen/html/group__misc__interfaces.md) |  |  |
| [Coresight STMESP interface](../../doxygen/html/group__stmsp__interface.md) |  |  |
| [Devmux Driver APIs](../../doxygen/html/group__demux__interface.md) |  |  |
| [FT8xx driver APIs](../../doxygen/html/group__ft8xx__interface.md) |  |  |
| [FT8xx co-processor](../../doxygen/html/group__ft8xx__copro.md) |  |  |
| [FT8xx common functions](../../doxygen/html/group__ft8xx__common.md) |  |  |
| [FT8xx display list](../../doxygen/html/group__ft8xx__dl.md) |  |  |
| [FT8xx memory map](../../doxygen/html/group__ft8xx__memory.md) |  |  |
| [FT8xx reference API](../../doxygen/html/group__ft8xx__reference__api.md) |  |  |
| [Multi Function Device Drivers APIs](../../doxygen/html/group__mfd__interfaces.md) |  |  |
| [MFD AD559X interface](../../doxygen/html/group__mdf__interface__ad559x.md) |  |  |
| [MFD AXP192 interface](../../doxygen/html/group__mdf__interface__axp192.md) |  |  |
| [MFD BD8LB600FS interface](../../doxygen/html/group__mdf__interface__bd8lb600fs.md) |  |  |
| [MFD NPM1300 Interface](../../doxygen/html/group__mdf__interface__npm1300.md) |  |  |
| [PCI Express Controller Interface](../../doxygen/html/group__pcie__controller__interface.md) |  |  |
| [PCIe Host Interface](../../doxygen/html/group__pcie__host__interface.md) |  |  |
| [PCIe Capabilities](../../doxygen/html/group__pcie__capabilities.md) |  |  |
| [PCIe Host MSI Interface](../../doxygen/html/group__pcie__host__msi__interface.md) |  |  |
| [PCIe Host PTM Interface](../../doxygen/html/group__pcie__host__ptm__interface.md) |  |  |
| [PCIe Virtual Channel Host Interface](../../doxygen/html/group__pcie__vc__host__interface.md) |  |  |
| [PECI Interface](../../doxygen/html/group__peci__interface.md) | 1.0.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.1.0) |
| [PS/2 Driver APIs](../../doxygen/html/group__ps2__interface.md) |  |  |
| [PWM Interface](../../doxygen/html/group__pwm__interface.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Pin Controller Interface](../../doxygen/html/group__pinctrl__interface.md) | 0.1.0 | [v3.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.0.0) |
| [Dynamic Pin Control](../../doxygen/html/group__pinctrl__interface__dynamic.md) |  |  |
| [RTC DS3231 Interface](../../doxygen/html/group__rtc__ds3231__interface.md) |  |  |
| [RTC Interface](../../doxygen/html/group__rtc__interface.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [Regulator Interface](../../doxygen/html/group__regulator__interface.md) | 0.1.0 | [v2.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.4.0) |
| [ADP5360 Devicetree helpers.](../../doxygen/html/group__regulator__adp5360.md) |  |  |
| [AXP192 Devicetree helpers.](../../doxygen/html/group__regulator__axp192.md) |  |  |
| [Devicetree helpers](../../doxygen/html/group__regulator__nxp__vref.md) |  |  |
| [MAX20335 Devicetree helpers.](../../doxygen/html/group__regulator__max20335.md) |  |  |
| [NPM1100 Devicetree helpers.](../../doxygen/html/group__regulator__npm1100.md) |  |  |
| [NPM1300 Devicetree helpers.](../../doxygen/html/group__regulator__npm1300.md) |  |  |
| [NPM6001 Devicetree helpers.](../../doxygen/html/group__regulator__npm6001.md) |  |  |
| [Regulator Parent Interface](../../doxygen/html/group__regulator__parent__interface.md) |  |  |
| [PCA9420 Utilities.](../../doxygen/html/group__regulator__parent__pca9420.md) |  |  |
| [Silabs DCDC devicetree helpers.](../../doxygen/html/group__regulator__silabs__dcdc.md) |  |  |
| [nRF5X regulator devicetree helpers.](../../doxygen/html/group__regulator__nrf5x.md) |  |  |
| [Reset Controller Interface](../../doxygen/html/group__reset__controller__interface.md) | 0.2.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.1.0) |
| [Retained memory driver interface](../../doxygen/html/group__retained__mem__interface.md) | 0.8.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [SDHC interface](../../doxygen/html/group__sdhc__interface.md) | 0.1.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.1.0) |
| [SMBus Interface](../../doxygen/html/group__smbus__interface.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [SPI Interface](../../doxygen/html/group__spi__interface.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [SYSCON Interface](../../doxygen/html/group__syscon__interface.md) |  |  |
| [Sensor Interface](../../doxygen/html/group__sensor__interface.md) | 1.0.0 | [v1.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.2.0) |
| [Invensense (TDK) ICM42688 DT Options](../../doxygen/html/group__ICM42688.md) |  |  |
| [Accelerometer data rate options](../../doxygen/html/group__ICM42688__ACCEL__DATA__RATE.md) |  |  |
| [Accelerometer power modes](../../doxygen/html/group__ICM42688__ACCEL__POWER__MODES.md) |  |  |
| [Accelerometer scale options](../../doxygen/html/group__ICM42688__ACCEL__SCALE.md) |  |  |
| [Gyroscope data rate options](../../doxygen/html/group__ICM42688__GYRO__DATA__RATE.md) |  |  |
| [Gyroscope power modes](../../doxygen/html/group__ICM42688__GYRO__POWER__MODES.md) |  |  |
| [Gyroscope scale options](../../doxygen/html/group__ICM42688__GYRO__SCALE.md) |  |  |
| [Memsic DT Options](../../doxygen/html/group__MC3419.md) |  |  |
| [Lowe pass filter configurations](../../doxygen/html/group__MC3419__LPF__CONFIGS.md) |  |  |
| [decimate sampling rate by provided rate](../../doxygen/html/group__MC3419__DECIMATION__RATES.md) |  |  |
| [Sensor emulator backend API](../../doxygen/html/group__sensor__emulator__backend.md) |  |  |
| [Stepper Controller Interface](../../doxygen/html/group__stepper__interface.md) |  |  |
| [Trinamic Stepper Controller Interface](../../doxygen/html/group__trinamic__stepper__interface.md) |  |  |
| [TEE Interface](../../doxygen/html/group__tee__interface.md) |  |  |
| [Text Display Interface](../../doxygen/html/group__auxdisplay__interface.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [Time-aware GPIO Interface](../../doxygen/html/group__tgpio__interface.md) | 0.1.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [Touchscreen Event Report API](../../doxygen/html/group__touch__events.md) | 0.1.0 | [v3.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.7.0) |
| [UART Interface](../../doxygen/html/group__uart__interface.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Async UART API](../../doxygen/html/group__uart__async.md) | 0.8.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.14.0) |
| [Interrupt-driven UART API](../../doxygen/html/group__uart__interrupt.md) |  |  |
| [Polling UART API](../../doxygen/html/group__uart__polling.md) |  |  |
| [USB Power Delivery](../../doxygen/html/group__usb__power__delivery.md) |  |  |
| [USB Type-C](../../doxygen/html/group__usb__type__c.md) |  |  |
| [USB Type-C Port Controller API](../../doxygen/html/group__usb__type__c__port__controller__api.md) | 0.1.0 | [v3.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.1.0) |
| [USB device controller driver API](../../doxygen/html/group__udc__api.md) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [USB host controller driver API](../../doxygen/html/group__uhc__api.md) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [USB-C VBUS API](../../doxygen/html/group__usbc__vbus__api.md) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [Video Controls](../../doxygen/html/group__video__controls.md) |  |  |
| [Video Interface](../../doxygen/html/group__video__interface.md) | 1.0.0 | [v2.1.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.1.0) |
| [Video pixel formats](../../doxygen/html/group__video__pixel__formats.md) |  |  |
| [Watchdog Interface](../../doxygen/html/group__watchdog__interface.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Device Model](../../doxygen/html/group__device__model.md) | 1.1.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Device memory-mapped IO management](../../doxygen/html/group__device-mmio.md) |  |  |
| [Named MMIO region macros](../../doxygen/html/group__device-mmio-named.md) |  |  |
| [Single MMIO region macros](../../doxygen/html/group__device-mmio-single.md) |  |  |
| [Top-level MMIO region macros](../../doxygen/html/group__device-mmio-toplevel.md) |  |  |
| [Devicetree](../../doxygen/html/group__devicetree.md) | 1.2.0 | [v2.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.2.0) |
| [“For-each” macros](../../doxygen/html/group__devicetree-generic-foreach.md) |  |  |
| [Bus helpers](../../doxygen/html/group__devicetree-generic-bus.md) |  |  |
| [Chosen nodes](../../doxygen/html/group__devicetree-generic-chosen.md) |  |  |
| [Dependency tracking](../../doxygen/html/group__devicetree-dep-ord.md) |  |  |
| [Devicetree CAN API](../../doxygen/html/group__devicetree-can.md) |  |  |
| [Devicetree Clocks API](../../doxygen/html/group__devicetree-clocks.md) |  |  |
| [Devicetree DMA API](../../doxygen/html/group__devicetree-dmas.md) |  |  |
| [Devicetree Fixed Partition API](../../doxygen/html/group__devicetree-fixed-partition.md) |  |  |
| [Devicetree GPIO API](../../doxygen/html/group__devicetree-gpio.md) |  |  |
| [Devicetree IO Channels API](../../doxygen/html/group__devicetree-io-channels.md) |  |  |
| [Devicetree Interrupt Controller API](../../doxygen/html/group__devicetree-interrupt__controller.md) |  |  |
| [Devicetree MBOX API](../../doxygen/html/group__devicetree-mbox.md) |  |  |
| [Devicetree PWMs API](../../doxygen/html/group__devicetree-pwms.md) |  |  |
| [Devicetree Reset Controller API](../../doxygen/html/group__devicetree-reset-controller.md) |  |  |
| [Devicetree SPI API](../../doxygen/html/group__devicetree-spi.md) |  |  |
| [Existence checks](../../doxygen/html/group__devicetree-generic-exist.md) |  |  |
| [Instance-based devicetree APIs](../../doxygen/html/group__devicetree-inst.md) |  |  |
| [Node identifiers and helpers](../../doxygen/html/group__devicetree-generic-id.md) |  |  |
| [Pin control](../../doxygen/html/group__devicetree-pinctrl.md) |  |  |
| [Property accessors](../../doxygen/html/group__devicetree-generic-prop.md) |  |  |
| [Vendor and model name helpers](../../doxygen/html/group__devicetree-generic-vendor.md) |  |  |
| [interrupts property](../../doxygen/html/group__devicetree-interrupts-prop.md) |  |  |
| [ranges property](../../doxygen/html/group__devicetree-ranges-prop.md) |  |  |
| [reg property](../../doxygen/html/group__devicetree-reg-prop.md) |  |  |
| [Error numbers](../../doxygen/html/group__system__errno.md) |  |  |
| [Internal and System API](../../doxygen/html/group__internal__api.md) |  |  |
| [Architecture Interface](../../doxygen/html/group__arch-interface.md) |  |  |
| [Architecture thread APIs](../../doxygen/html/group__arch-threads.md) |  |  |
| [Architecture timing APIs](../../doxygen/html/group__arch-timing.md) |  |  |
| [Architecture-specific IRQ APIs](../../doxygen/html/group__arch-irq.md) |  |  |
| [Architecture-specific SMP APIs](../../doxygen/html/group__arch-smp.md) |  |  |
| [Architecture-specific Stack Walk APIs](../../doxygen/html/group__arch-stackwalk.md) |  |  |
| [Architecture-specific Thread Local Storage APIs](../../doxygen/html/group__arch-tls.md) |  |  |
| [Architecture-specific core dump APIs](../../doxygen/html/group__arch-coredump.md) |  |  |
| [Architecture-specific gdbstub APIs](../../doxygen/html/group__arch-gdbstub.md) |  |  |
| [Architecture-specific memory-mapping APIs](../../doxygen/html/group__arch-mmu.md) |  |  |
| [Architecture-specific power management APIs](../../doxygen/html/group__arch-pm.md) |  |  |
| [Architecture-specific userspace APIs](../../doxygen/html/group__arch-userspace.md) |  |  |
| [Miscellaneous architecture APIs](../../doxygen/html/group__arch-misc.md) |  |  |
| [Xtensa APIs](../../doxygen/html/group__xtensa__apis.md) |  |  |
| [Xtensa Internal APIs](../../doxygen/html/group__xtensa__internal__apis.md) |  |  |
| [Xtensa Memory Management Unit (MMU) APIs](../../doxygen/html/group__xtensa__mmu__apis.md) |  |  |
| [Xtensa Memory Protection Unit (MPU) APIs](../../doxygen/html/group__xtensa__mpu__apis.md) |  |  |
| [Kernel Memory Management Internal APIs](../../doxygen/html/group__kernel__mm__internal__apis.md) |  |  |
| [User Mode Internal APIs](../../doxygen/html/group__usermode__internal__apis.md) |  |  |
| [User mode and Syscall APIs](../../doxygen/html/group__syscall__apis.md) |  |  |
| [Kernel APIs](../../doxygen/html/group__kernel__apis.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [Async polling APIs](../../doxygen/html/group__poll__apis.md) |  |  |
| [Asynchronous Notification APIs](../../doxygen/html/group__sys__notify__apis.md) |  |  |
| [Atomic Services APIs](../../doxygen/html/group__atomic__apis.md) |  |  |
| [Barrier Services APIs](../../doxygen/html/group__barrier__apis.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [CPU Idling APIs](../../doxygen/html/group__cpu__idle__apis.md) |  |  |
| [Condition Variables APIs](../../doxygen/html/group__condvar__apis.md) |  |  |
| [Event APIs](../../doxygen/html/group__event__apis.md) |  |  |
| [FIFO APIs](../../doxygen/html/group__fifo__apis.md) |  |  |
| [FUTEX APIs](../../doxygen/html/group__futex__apis.md) |  |  |
| [Fatal error APIs](../../doxygen/html/group__fatal__apis.md) |  |  |
| [Fatal error base types](../../doxygen/html/group__fatal__types.md) |  |  |
| [Floating Point APIs](../../doxygen/html/group__float__apis.md) |  |  |
| [Heap APIs](../../doxygen/html/group__heap__apis.md) |  |  |
| [Interrupt Service Routine APIs](../../doxygen/html/group__isr__apis.md) |  |  |
| [Kernel Memory Management](../../doxygen/html/group__kernel__memory__management.md) |  |  |
| [Demand Paging](../../doxygen/html/group__demand__paging.md) |  |  |
| [Backing Store APIs](../../doxygen/html/group__mem-demand-paging-backing-store.md) |  |  |
| [Demand Paging APIs](../../doxygen/html/group__mem-demand-paging.md) |  |  |
| [Eviction Algorithm APIs](../../doxygen/html/group__mem-demand-paging-eviction.md) |  |  |
| [LIFO APIs](../../doxygen/html/group__lifo__apis.md) |  |  |
| [Mailbox APIs](../../doxygen/html/group__mailbox__apis.md) |  |  |
| [Memory Slab APIs](../../doxygen/html/group__mem__slab__apis.md) |  |  |
| [Memory domain APIs](../../doxygen/html/group__mem__domain__apis.md) |  |  |
| [Application memory domain APIs](../../doxygen/html/group__mem__domain__apis__app.md) |  |  |
| [Message Queue APIs](../../doxygen/html/group__msgq__apis.md) |  |  |
| [Mutex APIs](../../doxygen/html/group__mutex__apis.md) |  |  |
| [Object Core APIs](../../doxygen/html/group__obj__core__apis.md) |  |  |
| [Object Core Statistics APIs](../../doxygen/html/group__obj__core__stats__apis.md) |  |  |
| [On-Off Service APIs](../../doxygen/html/group__resource__mgmt__onoff__apis.md) |  |  |
| [Pipe APIs](../../doxygen/html/group__pipe__apis.md) |  |  |
| [Queue APIs](../../doxygen/html/group__queue__apis.md) |  |  |
| [Semaphore APIs](../../doxygen/html/group__semaphore__apis.md) |  |  |
| [Spinlock APIs](../../doxygen/html/group__spinlock__apis.md) |  |  |
| [Stack APIs](../../doxygen/html/group__stack__apis.md) |  |  |
| [System Clock APIs](../../doxygen/html/group__clock__apis.md) |  |  |
| [Thread APIs](../../doxygen/html/group__thread__apis.md) |  |  |
| [Thread Stack APIs](../../doxygen/html/group__thread__stack__api.md) |  |  |
| [Timer APIs](../../doxygen/html/group__timer__apis.md) |  |  |
| [User Mode APIs](../../doxygen/html/group__usermode__apis.md) |  |  |
| [User mode mutex APIs](../../doxygen/html/group__user__mutex__apis.md) |  |  |
| [User mode semaphore APIs](../../doxygen/html/group__user__semaphore__apis.md) |  |  |
| [Version APIs](../../doxygen/html/group__version__apis.md) |  |  |
| [Work Queue APIs](../../doxygen/html/group__workqueue__apis.md) |  |  |
| [Memory Management APIs](../../doxygen/html/group__mem__mgmt.md) |  |  |
| [Memory heaps based on memory attributes](../../doxygen/html/group__memory__attr__heap.md) |  |  |
| [Memory-Attr Interface](../../doxygen/html/group__memory__attr__interface.md) |  |  |
| [Operating System Services](../../doxygen/html/group__os__services.md) |  |  |
| [Bindesc Define](../../doxygen/html/group__bindesc__define.md) |  |  |
| [Bindesc Read](../../doxygen/html/group__bindesc__read.md) |  |  |
| [Cache Interface](../../doxygen/html/group__cache__interface.md) |  |  |
| [Checksum](../../doxygen/html/group__checksum.md) |  |  |
| [CRC](../../doxygen/html/group__crc.md) |  |  |
| [Console API](../../doxygen/html/group__console__api.md) |  |  |
| [Coredump APIs](../../doxygen/html/group__coredump__apis.md) |  |  |
| [Crypto](../../doxygen/html/group__crypto.md) | 1.0.0 | [v1.7.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.7.0) |
| [Cipher](../../doxygen/html/group__crypto__cipher.md) |  |  |
| [Hash](../../doxygen/html/group__crypto__hash.md) |  |  |
| [Random Function APIs](../../doxygen/html/group__random__api.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [File System APIs](../../doxygen/html/group__file__system__api.md) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.5.0) |
| [File System Storage](../../doxygen/html/group__file__system__storage.md) |  |  |
| [Flash Circular Buffer (FCB)](../../doxygen/html/group__fcb.md) | 1.0.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.11.0) |
| [Flash Circular Buffer Data Structures](../../doxygen/html/group__fcb__data__structures.md) |  |  |
| [fcb API](../../doxygen/html/group__fcb__api.md) |  |  |
| [fcb non-API prototypes](../../doxygen/html/group__fcb__internal.md) |  |  |
| [Non-volatile Storage (NVS)](../../doxygen/html/group__nvs.md) | 1.0.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.12.0) |
| [Non-volatile Storage APIs](../../doxygen/html/group__nvs__high__level__api.md) |  |  |
| [Non-volatile Storage Data Structures](../../doxygen/html/group__nvs__data__structures.md) |  |  |
| [Settings](../../doxygen/html/group__settings.md) | 1.0.0 | [v1.12.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.12.0) |
| [Settings backend interface](../../doxygen/html/group__settings__backend.md) |  |  |
| [Settings name processing](../../doxygen/html/group__settings__name__proc.md) |  |  |
| [Settings subsystem runtime](../../doxygen/html/group__settings__rt.md) |  |  |
| [Zephyr Memory Storage (ZMS)](../../doxygen/html/group__zms.md) |  |  |
| [ZMS API](../../doxygen/html/group__zms__high__level__api.md) |  |  |
| [ZMS data structures](../../doxygen/html/group__zms__data__structures.md) |  |  |
| [Flash image API](../../doxygen/html/group__flash__img__api.md) |  |  |
| [Heap Management](../../doxygen/html/group__heaps.md) |  |  |
| [Heap Listener APIs](../../doxygen/html/group__heap__listener__apis.md) |  |  |
| [Low Level Heap Allocator](../../doxygen/html/group__low__level__heap__allocator.md) |  |  |
| [Multi-Heap Wrapper](../../doxygen/html/group__multi__heap__wrapper.md) |  |  |
| [Shared multi-heap interface](../../doxygen/html/group__shared__multi__heap.md) |  |  |
| [IPC](../../doxygen/html/group__ipc.md) |  |  |
| [IPC service APIs](../../doxygen/html/group__ipc__service__api.md) |  |  |
| [IPC service RPMsg API](../../doxygen/html/group__ipc__service__rpmsg__api.md) |  |  |
| [IPC service backend](../../doxygen/html/group__ipc__service__backend.md) |  |  |
| [IPC service static VRINGs API](../../doxygen/html/group__ipc__service__static__vrings__api.md) |  |  |
| [Icmsg IPC library API](../../doxygen/html/group__ipc__icmsg__api.md) |  |  |
| [Icmsg multi-endpoint IPC library API](../../doxygen/html/group__ipc__icmsg__me__api.md) |  |  |
| [Packed Buffer API](../../doxygen/html/group__pbuf.md) |  |  |
| [RPMsg service APIs](../../doxygen/html/group__rpmsg__service__api.md) |  |  |
| [Iterable Sections APIs](../../doxygen/html/group__iterable__section__apis.md) |  |  |
| [Linkable loadable extensions](../../doxygen/html/group__llext__apis.md) | 0.1.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [ELF constants and data types](../../doxygen/html/group__llext__elf.md) |  |  |
| [ELF loader context](../../doxygen/html/group__llext__loader__apis.md) |  |  |
| [Exported symbol definitions](../../doxygen/html/group__llext__symbols.md) |  |  |
| [Logging](../../doxygen/html/group__logging.md) | 1.0.0 | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [Logger system](../../doxygen/html/group__logger.md) |  | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [Log link API](../../doxygen/html/group__log__link.md) |  |  |
| [Log message API](../../doxygen/html/group__log__msg.md) |  |  |
| [Log output API](../../doxygen/html/group__log__output.md) |  |  |
| [Log output formatting flags.](../../doxygen/html/group__LOG__OUTPUT__FLAGS.md) |  |  |
| [Logger backend interface](../../doxygen/html/group__log__backend.md) |  |  |
| [Logger multidomain backend helpers](../../doxygen/html/group__log__backend__multidomain.md) |  |  |
| [Logger backend standard interface](../../doxygen/html/group__log__backend__std.md) |  |  |
| [Logger control API](../../doxygen/html/group__log__ctrl.md) |  | [v1.13.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.13.0) |
| [Logging API](../../doxygen/html/group__log__api.md) |  |  |
| [MCUmgr](../../doxygen/html/group__mcumgr.md) |  |  |
| [MCUmgr callback API](../../doxygen/html/group__mcumgr__callback__api.md) |  |  |
| [MCUmgr enum\_mgmt callback API](../../doxygen/html/group__mcumgr__callback__api__enum__mgmt.md) |  |  |
| [MCUmgr fs\_mgmt callback API](../../doxygen/html/group__mcumgr__callback__api__fs__mgmt.md) |  |  |
| [MCUmgr img\_mgmt callback API](../../doxygen/html/group__mcumgr__callback__api__img__mgmt.md) |  |  |
| [MCUmgr os\_mgmt callback API](../../doxygen/html/group__mcumgr__callback__api__os__mgmt.md) |  |  |
| [MCUmgr settings\_mgmt callback API](../../doxygen/html/group__mcumgr__callback__api__settings__mgmt.md) |  |  |
| [MCUmgr enum\_mgmt API](../../doxygen/html/group__mcumgr__enum__mgmt.md) |  |  |
| [MCUmgr handler API](../../doxygen/html/group__mcumgr__handler__api.md) |  |  |
| [MCUmgr img\_mgmt API](../../doxygen/html/group__mcumgr__img__mgmt.md) |  |  |
| [MCUmgr img\_mgmt\_client API](../../doxygen/html/group__mcumgr__img__mgmt__client.md) |  |  |
| [MCUmgr mgmt API](../../doxygen/html/group__mcumgr__mgmt__api.md) | 1.0.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.11.0) |
| [MCUmgr os\_mgmt\_client API](../../doxygen/html/group__mcumgr__os__mgmt__client.md) |  |  |
| [MCUmgr transport SMP API](../../doxygen/html/group__mcumgr__transport__smp.md) |  |  |
| [SMP client API](../../doxygen/html/group__mcumgr__smp__client.md) |  |  |
| [Memory Management](../../doxygen/html/group__memory__management.md) |  |  |
| [Memory Banks Driver APIs](../../doxygen/html/group__mm__drv__bank__apis.md) |  |  |
| [Memory Blocks APIs](../../doxygen/html/group__mem__blocks__apis.md) |  |  |
| [Memory Management Driver APIs](../../doxygen/html/group__mm__drv__apis.md) |  |  |
| [Network Buffer Library](../../doxygen/html/group__net__buf.md) | 1.0.0 | [v1.0.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.0.0) |
| [PSA Secure Storage API](../../doxygen/html/group__psa__secure__storage.md) |  |  |
| [Power Management (PM)](../../doxygen/html/group__subsys__pm.md) |  | [v1.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.2.0) |
| [CPU Power Management](../../doxygen/html/group__power__management__cpu__api.md) |  |  |
| [Device](../../doxygen/html/group__subsys__pm__device.md) |  |  |
| [Device Runtime](../../doxygen/html/group__subsys__pm__device__runtime.md) |  |  |
| [S2RAM APIs](../../doxygen/html/group__pm__s2ram.md) |  |  |
| [States](../../doxygen/html/group__subsys__pm__states.md) |  |  |
| [System](../../doxygen/html/group__subsys__pm__sys.md) |  | [v1.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.2.0) |
| [Hooks](../../doxygen/html/group__subsys__pm__sys__hooks.md) |  |  |
| [Policy](../../doxygen/html/group__subsys__pm__sys__policy.md) |  |  |
| [RTIO](../../doxygen/html/group__rtio.md) | 0.1.0 | [v3.2.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.2.0) |
| [RTIO CQE Flags](../../doxygen/html/group__rtio__cqe__flags.md) |  |  |
| [RTIO Priorities](../../doxygen/html/group__rtio__sqe__prio.md) |  |  |
| [RTIO SQE Flags](../../doxygen/html/group__rtio__sqe__flags.md) |  |  |
| [Retention API](../../doxygen/html/group__retention__api.md) | 0.1.0 | [v3.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.4.0) |
| [Boot mode interface](../../doxygen/html/group__boot__mode__interface.md) |  |  |
| [Bootloader info interface](../../doxygen/html/group__bootloader__info__interface.md) | 0.1.0 | [v3.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.5.0) |
| [STP Decoder API](../../doxygen/html/group__mipi__stp__decoder__apis.md) |  |  |
| [Semihosting APIs](../../doxygen/html/group__semihost.md) |  |  |
| [Shell API](../../doxygen/html/group__shell__api.md) | 1.0.0 | [v1.14.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.14.0) |
| [State Machine Framework API](../../doxygen/html/group__smf.md) | 0.1.0 |  |
| [Storage APIs](../../doxygen/html/group__storage__apis.md) |  |  |
| [Disk Access Interface](../../doxygen/html/group__disk__access__interface.md) |  |  |
| [Stream to flash interface](../../doxygen/html/group__stream__flash.md) | 0.1.0 | [v2.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.3.0) |
| [flash area Interface](../../doxygen/html/group__flash__area__api.md) | 1.0.0 | [v1.11.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.11.0) |
| [Symbol Table API](../../doxygen/html/group__symtab__apis.md) |  |  |
| [System Initialization](../../doxygen/html/group__sys__init.md) |  |  |
| [System power off](../../doxygen/html/group__sys__poweroff.md) |  |  |
| [Task Watchdog APIs](../../doxygen/html/group__task__wdt__api.md) | 0.8.0 | [v2.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.5.0) |
| [Thread analyzer](../../doxygen/html/group__thread__analyzer.md) |  |  |
| [Timing Measurement APIs](../../doxygen/html/group__timing__api.md) |  |  |
| [Arch specific Timing Measurement APIs](../../doxygen/html/group__timing__api__arch.md) |  |  |
| [Board specific Timing Measurement APIs](../../doxygen/html/group__timing__api__board.md) |  |  |
| [SoC specific Timing Measurement APIs](../../doxygen/html/group__timing__api__soc.md) |  |  |
| [Tracing](../../doxygen/html/group__subsys__tracing.md) |  |  |
| [Object tracking](../../doxygen/html/group__subsys__tracing__object__tracking.md) |  |  |
| [Tracing APIs](../../doxygen/html/group__subsys__tracing__apis.md) |  |  |
| [Conditional Variable Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__condvar.md) |  |  |
| [Event Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__event.md) |  |  |
| [FIFO Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__fifo.md) |  |  |
| [Heap Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__heap.md) |  |  |
| [LIFO Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__lifo.md) |  |  |
| [Mailbox Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__mbox.md) |  |  |
| [Memory Slab Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__mslab.md) |  |  |
| [Message Queue Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__msgq.md) |  |  |
| [Mutex Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__mutex.md) |  |  |
| [Named tracing APIs](../../doxygen/html/group__subsys__tracing__apis__named.md) |  |  |
| [Network Core Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__net.md) |  |  |
| [Network Socket Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__socket.md) |  |  |
| [PM Device Runtime Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__pm__device__runtime.md) |  |  |
| [Pipe Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__pipe.md) |  |  |
| [Poll Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__poll.md) |  |  |
| [Queue Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__queue.md) |  |  |
| [Semaphore Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__sem.md) |  |  |
| [Stack Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__stack.md) |  |  |
| [Syscall Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__syscall.md) |  |  |
| [System PM Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__pm__system.md) |  |  |
| [Thread Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__thread.md) |  |  |
| [Timer Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__timer.md) |  |  |
| [Work Delayable Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__work__delayable.md) |  |  |
| [Work Poll Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__work__poll.md) |  |  |
| [Work Queue Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__work__q.md) |  |  |
| [Work Tracing APIs](../../doxygen/html/group__subsys__tracing__apis__work.md) |  |  |
| [Tracing format APIs](../../doxygen/html/group__subsys__tracing__format__apis.md) |  |  |
| [Tracing utility macros](../../doxygen/html/group__subsys__tracing__macros.md) |  |  |
| [Zbus APIs](../../doxygen/html/group__zbus__apis.md) |  |  |
| [Sensing](../../doxygen/html/group__sensing.md) |  |  |
| [Data Types](../../doxygen/html/group__sensing__datatypes.md) |  |  |
| [Sensing Sensor API](../../doxygen/html/group__sensing__sensor.md) |  |  |
| [Sensor Callbacks](../../doxygen/html/group__sensing__sensor__callbacks.md) |  |  |
| [Sensing Subsystem API](../../doxygen/html/group__sensing__api.md) |  |  |
| [Sensor Types](../../doxygen/html/group__sensing__sensor__types.md) |  |  |
| [Testing](../../doxygen/html/group__testing.md) |  |  |
| [Emulator interface](../../doxygen/html/group__io__emulators.md) |  |  |
| [I2C Emulation Interface](../../doxygen/html/group__i2c__emul__interface.md) |  |  |
| [MSPI Emulation Interface](../../doxygen/html/group__mspi__emul__interface.md) |  |  |
| [SPI Emulation Interface](../../doxygen/html/group__spi__emul__interface.md) |  |  |
| [UART Emulation Interface](../../doxygen/html/group__uart__emul__interface.md) |  |  |
| [eSPI Emulation Interface](../../doxygen/html/group__espi__emul__interface.md) |  |  |
| [FFF extensions](../../doxygen/html/group__fff__extensions.md) |  |  |
| [Zephyr Testing Framework (ZTest)](../../doxygen/html/group__ztest.md) |  |  |
| [Ztest assertion macros](../../doxygen/html/group__ztest__assert.md) |  |  |
| [Ztest assumption macros](../../doxygen/html/group__ztest__assume.md) |  |  |
| [Ztest expectation macros](../../doxygen/html/group__ztest__expect.md) |  |  |
| [Ztest mocking support](../../doxygen/html/group__ztest__mock.md) |  |  |
| [Ztest testing macros](../../doxygen/html/group__ztest__test.md) |  |  |
| [Ztest ztress macros](../../doxygen/html/group__ztest__ztress.md) |  |  |
| [Tests](../../doxygen/html/group__all__tests.md) |  |  |
| [Memory Protection](../../doxygen/html/group__kernel__memprotect__tests.md) |  |  |
| [Third-party](../../doxygen/html/group__third__party.md) |  |  |
| [BBC micro:bit display APIs](../../doxygen/html/group__mb__display.md) |  |  |
| [Grove display APIs](../../doxygen/html/group__grove__display.md) |  |  |
| [MCUboot image control API](../../doxygen/html/group__mcuboot__api.md) |  |  |
| [UpdateHub Firmware Over-the-Air](../../doxygen/html/group__updatehub.md) |  |  |
| [hawkBit Firmware Over-the-Air](../../doxygen/html/group__hawkbit.md) |  |  |
| [hawkBit autohandler API](../../doxygen/html/group__hawkbit__autohandler.md) |  |  |
| [hawkBit configuration API](../../doxygen/html/group__hawkbit__config.md) |  |  |
| [Trace and Debug Domain APIs](../../doxygen/html/group__log__frontend__stmesp__apis.md) |  |  |
| [Logging frontend STMESP Demultiplexer API](../../doxygen/html/group__log__frontend__stpesp__demux__apis.md) |  |  |
| [USB Device Controller API](../../doxygen/html/group____usb__device__controller__api.md) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.5.0) |
| [USB Device Core API](../../doxygen/html/group____usb__device__core__api.md) | 1.0.0 | [v1.5.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v1.5.0) |
| [USB-C Device API](../../doxygen/html/group____usbc__device__api.md) | 0.1.0 | [v3.3.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v3.3.0) |
| [Sink\_callbacks](../../doxygen/html/group__sink__callbacks.md) |  |  |
| [Source\_callbacks](../../doxygen/html/group__source__callbacks.md) |  |  |
| [Utilities](../../doxygen/html/group__utilities.md) |  |  |
| [Base64](../../doxygen/html/group__base64.md) |  |  |
| [Data Structure APIs](../../doxygen/html/group__datastructure__apis.md) |  |  |
| [Balanced Red/Black Tree](../../doxygen/html/group__rbtree__apis.md) |  |  |
| [Bit array](../../doxygen/html/group__bitarray__apis.md) |  |  |
| [Doubly-linked list](../../doxygen/html/group__doubly-linked-list__apis.md) |  |  |
| [Flagged Single-linked list](../../doxygen/html/group__flagged-single-linked-list__apis.md) |  |  |
| [Hashmap](../../doxygen/html/group__hashmap__apis.md) |  |  |
| [Hash Functions](../../doxygen/html/group__hash__functions.md) |  |  |
| [Hashmap Implementations](../../doxygen/html/group__hashmap__implementations.md) |  |  |
| [MPSC (Multi producer, single consumer) packet buffer API](../../doxygen/html/group__mpsc__buf.md) |  |  |
| [MPSC (Multi producer, single consumer) packet header](../../doxygen/html/group__mpsc__packet.md) |  |  |
| [MPSC packet buffer flags](../../doxygen/html/group__MPSC__PBUF__FLAGS.md) |  |  |
| [MPSC Lockfree Queue API](../../doxygen/html/group__mpsc__lockfree.md) |  |  |
| [Ring Buffer APIs](../../doxygen/html/group__ring__buffer__apis.md) |  |  |
| [SPSC (Single producer, single consumer) packet buffer API](../../doxygen/html/group__spsc__buf.md) |  |  |
| [SPSC packet buffer flags](../../doxygen/html/group__SPSC__PBUF__FLAGS.md) |  |  |
| [SPSC API](../../doxygen/html/group__spsc__lockfree.md) |  |  |
| [Single-linked list](../../doxygen/html/group__single-linked-list__apis.md) |  |  |
| [Formatted Output APIs](../../doxygen/html/group__cbprintf__apis.md) |  |  |
| [Package convert flags](../../doxygen/html/group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md) |  |  |
| [Package flags](../../doxygen/html/group__CBPRINTF__PACKAGE__FLAGS.md) |  |  |
| [cbvprintf processing flags.](../../doxygen/html/group__Z__CBVPRINTF__PROCESS__FLAGS.md) |  |  |
| [JSON](../../doxygen/html/group__json.md) |  |  |
| [JSON Web Token (JWT)](../../doxygen/html/group__jwt.md) |  |  |
| [Linear Range](../../doxygen/html/group__linear__range.md) |  |  |
| [Math extras](../../doxygen/html/group__math__extras.md) |  |  |
| [Monochrome Character Framebuffer](../../doxygen/html/group__monochrome__character__framebuffer.md) |  |  |
| [Navigation](../../doxygen/html/group__navigation.md) |  |  |
| [Time Utility APIs](../../doxygen/html/group__timeutil__apis.md) |  |  |
| [Time Representation APIs](../../doxygen/html/group__timeutil__repr__apis.md) |  |  |
| [Time Synchronization APIs](../../doxygen/html/group__timeutil__sync__apis.md) |  |  |
| [Time Units Helpers](../../doxygen/html/group__timeutil__unit__apis.md) |  |  |
| [Utility Functions](../../doxygen/html/group__sys-util.md) | 0.1.0 | [v2.4.0](https://github.com/zephyrproject-rtos/zephyr/releases/tag//v2.4.0) |
| [battery APIs](../../doxygen/html/group__battery__apis.md) |  |  |
| [nRF70 Offloaded raw TX API](../../doxygen/html/group__nrf70__off__raw__tx__api.md) |  |  |
