---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/rpr_cli.html
original_path: connectivity/bluetooth/api/mesh/rpr_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Remote Provisioning Client

The Remote Provisioning Client model is a foundation model defined by the Bluetooth
mesh specification. It is enabled with the
[`CONFIG_BT_MESH_RPR_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_RPR_CLI "CONFIG_BT_MESH_RPR_CLI") option.

The Remote Provisioning Client model is introduced in the Bluetooth Mesh Protocol
Specification version 1.1.
This model provides functionality to remotely provision devices into a mesh network, and perform
Node Provisioning Protocol Interface procedures by interacting with mesh nodes that support the
[Remote Provisioning Server](rpr_srv.md#bluetooth-mesh-models-rpr-srv) model.

The Remote Provisioning Client model communicates with a Remote Provisioning Server model
using the device key of the node containing the target Remote Provisioning Server model instance.

If present, the Remote Provisioning Client model must be instantiated on the primary
element.

## Scanning

The scanning procedure is used to scan for unprovisioned devices located nearby the Remote
Provisioning Server. The Remote Provisioning Client starts a scan procedure by using the
[`bt_mesh_rpr_scan_start()`](#c.bt_mesh_rpr_scan_start) call:

```c
static void rpr_scan_report(struct bt_mesh_rpr_cli *cli,
            const struct bt_mesh_rpr_node *srv,
            struct bt_mesh_rpr_unprov *unprov,
            struct net_buf_simple *adv_data)
{

}

struct bt_mesh_rpr_cli rpr_cli = {
   .scan_report = rpr_scan_report,
};

const struct bt_mesh_rpr_node srv = {
   .addr = 0x0004,
   .net_idx = 0,
   .ttl = BT_MESH_TTL_DEFAULT,
};

struct bt_mesh_rpr_scan_status status;
uint8_t *uuid = NULL;
uint8_t timeout = 10;
uint8_t max_devs = 3;

bt_mesh_rpr_scan_start(&rpr_cli, &srv, uuid, timeout, max_devs, &status);
```

The above example shows pseudo code for starting a scan procedure on the target Remote Provisioning
Server node. This procedure will start a ten-second, multiple-device scanning where the generated
scan report will contain a maximum of three unprovisioned devices. If the UUID argument was
specified, the same procedure would only scan for the device with the corresponding UUID. After the
procedure completes, the server sends the scan report that will be handled in the client’s
[`bt_mesh_rpr_cli.scan_report`](#c.bt_mesh_rpr_cli.scan_report) callback.

Additionally, the Remote Provisioning Client model also supports extended scanning with the
[`bt_mesh_rpr_scan_start_ext()`](#c.bt_mesh_rpr_scan_start_ext) call. Extended scanning supplements regular scanning by
allowing the Remote Provisioning Server to report additional data for a specific device. The Remote
Provisioning Server will use active scanning to request a scan response from the unprovisioned
device if it is supported by the unprovisioned device.

## Provisioning

The Remote Provisioning Client starts a provisioning procedure by using the
[`bt_mesh_provision_remote()`](provisioning.md#c.bt_mesh_provision_remote "bt_mesh_provision_remote") call:

```c
struct bt_mesh_rpr_cli rpr_cli;

const struct bt_mesh_rpr_node srv = {
   .addr = 0x0004,
   .net_idx = 0,
   .ttl = BT_MESH_TTL_DEFAULT,
};

uint8_t uuid[16] = { 0xaa };
uint16_t addr = 0x0006;
uint16_t net_idx = 0;

bt_mesh_provision_remote(&rpr_cli, &srv, uuid, net_idx, addr);
```

The above example shows pseudo code for remotely provisioning a device through a Remote Provisioning
Server node. This procedure will attempt to provision the device with the corresponding UUID, and
assign the address 0x0006 to its primary element using the network key located at index zero.

Note

During the remote provisioning, the same [`bt_mesh_prov`](provisioning.md#c.bt_mesh_prov "bt_mesh_prov") callbacks are triggered as for
ordinary provisioning. See section [Provisioning](provisioning.md#bluetooth-mesh-provisioning) for further details.

## Re-provisioning

In addition to scanning and provisioning functionality, the Remote Provisioning Client also provides
means to reconfigure node addresses, device keys and Composition Data on devices that support the
[Remote Provisioning Server](rpr_srv.md#bluetooth-mesh-models-rpr-srv) model. This is provided through the Node Provisioning Protocol
Interface (NPPI) which supports the following three procedures:

- Device Key Refresh procedure: Used to change the device key of the Target node without a need to
  reconfigure the node.
- Node Address Refresh procedure: Used to change the node’s device key and unicast address.
- Node Composition Refresh procedure: Used to change the device key of the node, and to add or
  delete models or features of the node.

The three NPPI procedures can be initiated with the [`bt_mesh_reprovision_remote()`](provisioning.md#c.bt_mesh_reprovision_remote "bt_mesh_reprovision_remote") call:

```c
struct bt_mesh_rpr_cli rpr_cli;
struct bt_mesh_rpr_node srv = {
   .addr = 0x0006,
   .net_idx = 0,
   .ttl = BT_MESH_TTL_DEFAULT,
};

bool composition_changed = false;
uint16_t new_addr = 0x0009;

bt_mesh_reprovision_remote(&rpr_cli, &srv, new_addr, composition_changed);
```

The above example shows pseudo code for triggering a Node Address Refresh procedure on the Target
node. The specific procedure is not chosen directly, but rather through the other parameters that
are inputted. In the example we can see that the current unicast address of the Target is 0x0006,
while the new address is set to 0x0009. If the two addresses were the same, and the
`composition_changed` flag was set to true, this code would instead trigger a Node Composition
Refresh procedure. If the two addresses were the same, and the `composition_changed` flag was set
to false, this code would trigger a Device Key Refresh procedure.

## API reference

*group* bt\_mesh\_rpr\_cli
:   Defines

    BT\_MESH\_RPR\_SCAN\_MAX\_DEVS\_ANY
    :   Special value for the `max_devs` parameter of [bt\_mesh\_rpr\_scan\_start](#group__bt__mesh__rpr__cli_1gaf404922f2340442490f1ab29191f43e3).

        Tells the Remote Provisioning Server not to put restrictions on the max number of devices reported to the Client.

    BT\_MESH\_MODEL\_RPR\_CLI(\_cli)
    :   Remote Provisioning Client model composition data entry.

        Parameters:
        :   - **\_cli** – Pointer to a [Remote Provisioning Client model](#group__bt__mesh__rpr__cli) instance.

    Functions

    int bt\_mesh\_rpr\_scan\_caps\_get(struct [bt\_mesh\_rpr\_cli](#c.bt_mesh_rpr_cli) \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct [bt\_mesh\_rpr\_caps](#c.bt_mesh_rpr_caps) \*caps)
    :   Get scanning capabilities of Remote Provisioning Server.

        Parameters:
        :   - **cli** – Remote Provisioning Client.
            - **srv** – Remote Provisioning Server.
            - **caps** – Capabilities response buffer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_rpr\_scan\_get(struct [bt\_mesh\_rpr\_cli](#c.bt_mesh_rpr_cli) \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct [bt\_mesh\_rpr\_scan\_status](#c.bt_mesh_rpr_scan_status) \*status)
    :   Get current scanning state of Remote Provisioning Server.

        Parameters:
        :   - **cli** – Remote Provisioning Client.
            - **srv** – Remote Provisioning Server.
            - **status** – Scan status response buffer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_rpr\_scan\_start(struct [bt\_mesh\_rpr\_cli](#c.bt_mesh_rpr_cli) \*cli, const struct bt\_mesh\_rpr\_node \*srv, const uint8\_t uuid[16], uint8\_t timeout, uint8\_t max\_devs, struct [bt\_mesh\_rpr\_scan\_status](#c.bt_mesh_rpr_scan_status) \*status)
    :   Start scanning for unprovisioned devices.

        Tells the Remote Provisioning Server to start scanning for unprovisioned devices. The Server will report back the results through the [bt\_mesh\_rpr\_cli::scan\_report](#structbt__mesh__rpr__cli_1a32b3c63218b506d1bc5759640cb3fb81) callback.

        Use the `uuid` parameter to scan for a specific device, or leave it as NULL to report all unprovisioned devices.

        The Server will ignore duplicates, and report up to `max_devs` number of devices. Requesting a `max_devs` number that’s higher than the Server’s capability will result in an error.

        Parameters:
        :   - **cli** – Remote Provisioning Client.
            - **srv** – Remote Provisioning Server.
            - **uuid** – Device UUID to scan for, or NULL to report all devices.
            - **timeout** – Scan timeout in seconds. Must be at least 1 second.
            - **max\_devs** – Max number of devices to report, or 0 to report as many as possible.
            - **status** – Scan status response buffer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_rpr\_scan\_start\_ext(struct [bt\_mesh\_rpr\_cli](#c.bt_mesh_rpr_cli) \*cli, const struct bt\_mesh\_rpr\_node \*srv, const uint8\_t uuid[16], uint8\_t timeout, const uint8\_t \*ad\_types, size\_t ad\_count)
    :   Start extended scanning for unprovisioned devices.

        Extended scanning supplements regular unprovisioned scanning, by allowing the Server to report additional data for a specific device. The Remote Provisioning Server will use active scanning to request a scan response from the unprovisioned device, if supported. If no UUID is provided, the Server will report a scan on its own OOB information and advertising data.

        Use the ad\_types array to specify which AD types to include in the scan report. Some AD types invoke special behavior:

        - [BT\_DATA\_NAME\_COMPLETE](../gap.md#group__bt__gap__defines_1gab94a7c5689d296acf47f976538056ab5) Will report both the complete and the shortened name.
        - [BT\_DATA\_URI](../gap.md#group__bt__gap__defines_1ga3c6a5903cc4a46aaf0b30a0de0179403) If the unprovisioned beacon contains a URI hash, the Server will extend the scanning to include packets other than the scan response, to look for URIs matching the URI hash. Only matching URIs will be reported.

        The following AD types should not be used:

        - [BT\_DATA\_NAME\_SHORTENED](../gap.md#group__bt__gap__defines_1gafc509b33a8d2dd9124f6893eadbe1662)
        - [BT\_DATA\_UUID16\_SOME](../gap.md#group__bt__gap__defines_1ga6c725bd3d31c159a4d046561dbca38ba)
        - [BT\_DATA\_UUID32\_SOME](../gap.md#group__bt__gap__defines_1ga2486a6748490ba57e442ca15223482ef)
        - [BT\_DATA\_UUID128\_SOME](../gap.md#group__bt__gap__defines_1ga5c4f7fc1b93c611e95f735330fba243b)

        Additionally, each AD type should only occur once.

        Parameters:
        :   - **cli** – Remote Provisioning Client.
            - **srv** – Remote Provisioning Server.
            - **uuid** – Device UUID to start extended scanning for, or NULL to scan the remote server.
            - **timeout** – Scan timeout in seconds. Valid values from BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MIN to BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MAX. Ignored if UUID is NULL.
            - **ad\_types** – List of AD types to include in the scan report. Must contain 1 to CONFIG\_BT\_MESH\_RPR\_AD\_TYPES\_MAX entries.
            - **ad\_count** – Number of AD types in `ad_types`.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_rpr\_scan\_stop(struct [bt\_mesh\_rpr\_cli](#c.bt_mesh_rpr_cli) \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct [bt\_mesh\_rpr\_scan\_status](#c.bt_mesh_rpr_scan_status) \*status)
    :   Stop any ongoing scanning on the Remote Provisioning Server.

        Parameters:
        :   - **cli** – Remote Provisioning Client.
            - **srv** – Remote Provisioning Server.
            - **status** – Scan status response buffer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_rpr\_link\_get(struct [bt\_mesh\_rpr\_cli](#c.bt_mesh_rpr_cli) \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct bt\_mesh\_rpr\_link \*rsp)
    :   Get the current link status of the Remote Provisioning Server.

        Parameters:
        :   - **cli** – Remote Provisioning Client.
            - **srv** – Remote Provisioning Server.
            - **rsp** – Link status response buffer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_rpr\_link\_close(struct [bt\_mesh\_rpr\_cli](#c.bt_mesh_rpr_cli) \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct bt\_mesh\_rpr\_link \*rsp)
    :   Close any open link on the Remote Provisioning Server.

        Parameters:
        :   - **cli** – Remote Provisioning Client.
            - **srv** – Remote Provisioning Server.
            - **rsp** – Link status response buffer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int32\_t bt\_mesh\_rpr\_cli\_timeout\_get(void)
    :   Get the current transmission timeout value.

        Returns:
        :   The configured transmission timeout in milliseconds.

    void bt\_mesh\_rpr\_cli\_timeout\_set(int32\_t timeout)
    :   Set the transmission timeout value.

        The transmission timeout controls the amount of time the Remote Provisioning Client models will wait for a response from the Server.

        Parameters:
        :   - **timeout** – The new transmission timeout.

    struct bt\_mesh\_rpr\_scan\_status
    :   *#include <rpr\_cli.h>*

        Scan status response.

        Public Members

        enum bt\_mesh\_rpr\_status status
        :   Current scan status.

        enum bt\_mesh\_rpr\_scan scan
        :   Current scan state.

        uint8\_t max\_devs
        :   Max number of devices to report in current scan.

        uint8\_t timeout
        :   Seconds remaining of the scan.

    struct bt\_mesh\_rpr\_caps
    :   *#include <rpr\_cli.h>*

        Remote Provisioning Server scanning capabilities.

        Public Members

        uint8\_t max\_devs
        :   Max number of scannable devices.

        bool active\_scan
        :   Supports active scan.

    struct bt\_mesh\_rpr\_cli
    :   *#include <rpr\_cli.h>*

        Remote Provisioning Client model instance.

        Public Members

        void (\*scan\_report)(struct [bt\_mesh\_rpr\_cli](#c.bt_mesh_rpr_cli) \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct bt\_mesh\_rpr\_unprov \*unprov, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*adv\_data)
        :   Scan report callback.

            Param cli:
            :   Remote Provisioning Client.

            Param srv:
            :   Remote Provisioning Server.

            Param unprov:
            :   Unprovisioned device.

            Param adv\_data:
            :   Advertisement data for the unprovisioned device, or NULL if extended scanning hasn’t been enabled. An empty buffer indicates that the extended scanning finished without collecting additional information.
