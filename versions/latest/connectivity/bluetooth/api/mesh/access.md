---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/access.html
original_path: connectivity/bluetooth/api/mesh/access.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Access layer

The access layer is the application’s interface to the Bluetooth Mesh network.
The access layer provides mechanisms for compartmentalizing the node behavior
into elements and models, which are implemented by the application.

## Mesh models

The functionality of a mesh node is represented by models. A model implements
a single behavior the node supports, like being a light, a sensor or a
thermostat. The mesh models are grouped into *elements*. Each element is
assigned its own unicast address, and may only contain one of each type of
model. Conventionally, each element represents a single aspect of the mesh
node behavior. For instance, a node that contains a sensor, two lights and a
power outlet would spread this functionality across four elements, with each
element instantiating all the models required for a single aspect of the
supported behavior.

The node’s element and model structure is specified in the node composition
data, which is passed to [`bt_mesh_init()`](core.md#c.bt_mesh_init "bt_mesh_init") during initialization. The
Bluetooth SIG have defined a set of foundation models (see
[Mesh models](models.md#bluetooth-mesh-models)) and a set of models for implementing common
behavior in the [Bluetooth Mesh Model Specification](https://www.bluetooth.com/specifications/mesh-specifications/). All models
not specified by the Bluetooth SIG are vendor models, and must be tied to a
Company ID.

Mesh models have several parameters that can be configured either through
initialization of the mesh stack or with the
[Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv):

### Opcode list

The opcode list contains all message opcodes the model can receive, as well as
the minimum acceptable payload length and the callback to pass them to. Models
can support any number of opcodes, but each opcode can only be listed by one
model in each element.

The full opcode list must be passed to the model structure in the composition
data, and cannot be changed at runtime. The end of the opcode list is
determined by the special [`BT_MESH_MODEL_OP_END`](#c.BT_MESH_MODEL_OP_END) entry. This entry
must always be present in the opcode list, unless the list is empty. In that
case, [`BT_MESH_MODEL_NO_OPS`](#c.BT_MESH_MODEL_NO_OPS) should be used in place of a proper
opcode list definition.

### AppKey list

The AppKey list contains all the application keys the model can receive
messages on. Only messages encrypted with application keys in the AppKey list
will be passed to the model.

The maximum number of supported application keys each model can hold is
configured with the [`CONFIG_BT_MESH_MODEL_KEY_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_MODEL_KEY_COUNT "CONFIG_BT_MESH_MODEL_KEY_COUNT") configuration
option. The contents of the AppKey list is managed by the
[Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv).

### Subscription list

A model will process all messages addressed to the unicast address of their
element (given that the utilized application key is present in the AppKey
list). Additionally, the model will process packets addressed to any group or
virtual address in its subscription list. This allows nodes to address
multiple nodes throughout the mesh network with a single message.

The maximum number of supported addresses in the Subscription list each model
can hold is configured with the [`CONFIG_BT_MESH_MODEL_GROUP_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_MODEL_GROUP_COUNT "CONFIG_BT_MESH_MODEL_GROUP_COUNT")
configuration option. The contents of the subscription list is managed by the
[Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv).

### Model publication

The models may send messages in two ways:

- By specifying a set of message parameters in a [`bt_mesh_msg_ctx`](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx"),
  and calling [`bt_mesh_model_send()`](#c.bt_mesh_model_send).
- By setting up a [`bt_mesh_model_pub`](#c.bt_mesh_model_pub) structure and calling
  [`bt_mesh_model_publish()`](#c.bt_mesh_model_publish).

When publishing messages with [`bt_mesh_model_publish()`](#c.bt_mesh_model_publish), the model
will use the publication parameters configured by the
[Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv). This is the recommended way to send
unprompted model messages, as it passes the responsibility of selecting
message parameters to the network administrator, which likely knows more about
the mesh network than the individual nodes will.

To support publishing with the publication parameters, the model must allocate
a packet buffer for publishing, and pass it to
[`bt_mesh_model_pub.msg`](#c.bt_mesh_model_pub.msg). The Config Server may also set up period
publication for the publication message. To support this, the model must
populate the [`bt_mesh_model_pub.update`](#c.bt_mesh_model_pub.update) callback. The
[`bt_mesh_model_pub.update`](#c.bt_mesh_model_pub.update) callback will be called right before the
message is published, allowing the model to change the payload to reflect its
current state.

By setting [`bt_mesh_model_pub.retr_update`](#c.bt_mesh_model_pub.retr_update) to 1, the model can
configure the [`bt_mesh_model_pub.update`](#c.bt_mesh_model_pub.update) callback to be triggered
on every retransmission. This can, for example, be used by models that make
use of a Delay parameter, which can be adjusted for every retransmission.
The [`bt_mesh_model_pub_is_retransmission()`](#c.bt_mesh_model_pub_is_retransmission) function can be
used to differentiate a first publication and a retransmission.
The [`BT_MESH_PUB_MSG_TOTAL`](#c.BT_MESH_PUB_MSG_TOTAL) and [`BT_MESH_PUB_MSG_NUM`](#c.BT_MESH_PUB_MSG_NUM) macros
can be used to return total number of transmissions and the retransmission
number within one publication interval.

### Extended models

The Bluetooth Mesh specification allows the mesh models to extend each other.
When a model extends another, it inherits that model’s functionality, and
extension can be used to construct complex models out of simple ones,
leveraging the existing model functionality to avoid defining new opcodes.
Models may extend any number of models, from any element. When one model
extends another in the same element, the two models will share subscription
lists. The mesh stack implements this by merging the subscription lists of the
two models into one, combining the number of subscriptions the models can have
in total. Models may extend models that extend others, creating an “extension
tree”. All models in an extension tree share a single subscription list per
element it spans.

Model extensions are done by calling [`bt_mesh_model_extend()`](#c.bt_mesh_model_extend) during
initialization. A model can only be extended by one other model, and
extensions cannot be circular. Note that binding of node states and other
relationships between the models must be defined by the model implementations.

The model extension concept adds some overhead in the access layer packet
processing, and must be explicitly enabled with
[`CONFIG_BT_MESH_MODEL_EXTENSIONS`](../../../../kconfig.md#CONFIG_BT_MESH_MODEL_EXTENSIONS "CONFIG_BT_MESH_MODEL_EXTENSIONS") to have any effect.

### Model data storage

Mesh models may have data associated with each model instance that needs to be
stored persistently. The access API provides a mechanism for storing this
data, leveraging the internal model instance encoding scheme. Models can store
one user defined data entry per instance by calling
[`bt_mesh_model_data_store()`](#c.bt_mesh_model_data_store). To be able to read out the data the
next time the device reboots, the model’s
[`bt_mesh_model_cb.settings_set`](#c.bt_mesh_model_cb.settings_set) callback must be populated. This
callback gets called when model specific data is found in the persistent
storage. The model can retrieve the data by calling the `read_cb` passed as
a parameter to the callback. See the [Settings](../../../../services/settings/index.md#settings-api) module documentation for
details.

When model data changes frequently, storing it on every change may lead to
increased wear of flash. To reduce the wear, the model can postpone storing of
data by calling [`bt_mesh_model_data_store_schedule()`](#c.bt_mesh_model_data_store_schedule). The stack will
schedule a work item with delay defined by the
[`CONFIG_BT_MESH_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_STORE_TIMEOUT "CONFIG_BT_MESH_STORE_TIMEOUT") option. When the work item is
running, the stack will call the [`bt_mesh_model_cb.pending_store`](#c.bt_mesh_model_cb.pending_store)
callback for every model that has requested storing of data. The model can
then call [`bt_mesh_model_data_store()`](#c.bt_mesh_model_data_store) to store the data.

If [`CONFIG_BT_MESH_SETTINGS_WORKQ`](../../../../kconfig.md#CONFIG_BT_MESH_SETTINGS_WORKQ "CONFIG_BT_MESH_SETTINGS_WORKQ") is enabled, the
[`bt_mesh_model_cb.pending_store`](#c.bt_mesh_model_cb.pending_store) callback is called from a dedicated
thread. This allows the stack to process other incoming and outgoing messages
while model data is being stored. It is recommended to use this option and the
[`bt_mesh_model_data_store_schedule()`](#c.bt_mesh_model_data_store_schedule) function when large amount of data
needs to be stored.

### Composition Data

The Composition Data provides information about a mesh device.
A device’s Composition Data holds information about the elements on the
device, the models that it supports, and other features. The Composition
Data is split into different pages, where each page contains specific feature
information about the device. In order to access this information, the user
may use the [Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv) model or, if supported,
the [Large Composition Data Server](lcd_srv.md#bluetooth-mesh-lcd-srv) model.

#### Composition Data Page 0

Composition Data Page 0 provides the fundamental information about a device, and
is mandatory for all mesh devices. It contains the element and model composition,
the supported features, and manufacturer information.

#### Composition Data Page 1

Composition Data Page 1 provides information about the relationships between models,
and is mandatory for all mesh devices. A model may extend and/or correspond to one
or more models. A model can extend another model by calling [`bt_mesh_model_extend()`](#c.bt_mesh_model_extend),
or correspond to another model by calling [`bt_mesh_model_correspond()`](#c.bt_mesh_model_correspond).
[`CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE`](../../../../kconfig.md#CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE "CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE") specifies how many model
relations can be stored in the composition on a device, and this number should reflect the
number of [`bt_mesh_model_extend()`](#c.bt_mesh_model_extend) and [`bt_mesh_model_correspond()`](#c.bt_mesh_model_correspond) calls.

#### Composition Data Page 2

Composition Data Page 2 provides information for supported mesh profiles. Mesh profile
specifications define product requirements for devices that want to support a specific
Bluetooth SIG defined profile. Currently supported profiles can be found in section
3.12 in [Bluetooth SIG Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers/uri-scheme-name-string-mapping/).
Composition Data Page 2 is only mandatory for devices that claim support for one or more
mesh profile(s).

#### Composition Data Pages 128, 129 and 130

Composition Data Pages 128, 129 and 130 mirror Composition Data Pages 0, 1 and 2 respectively.
They are used to represent the new content of the mirrored pages when the Composition Data will
change after a firmware update. See [Composition Data and Models Metadata](dfu_srv.md#bluetooth-mesh-dfu-srv-comp-data-and-models-metadata)
for details.

### Delayable messages

The delayable message functionality is enabled with Kconfig option
[`CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG`](../../../../kconfig.md#CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG "CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG").
This is an optional functionality that implements specification recommendations for
messages that are transmitted by a model in a response to a received message, also called
response messages.

Response messages should be sent with the following random delays:

- Between 20 and 50 milliseconds if the received message was sent
  to a unicast address
- Between 20 and 500 milliseconds if the received message was sent
  to a group or virtual address

The delayable message functionality is triggered if the [`bt_mesh_msg_ctx.rnd_delay`](msg.md#c.bt_mesh_msg_ctx.rnd_delay "bt_mesh_msg_ctx.rnd_delay")
flag is set.
The delayable message functionality stores messages in the local memory while they are
waiting for the random delay expiration.

If the transport layer doesn’t have sufficient memory to send a message at the moment
the random delay expires, the message is postponed for another 10 milliseconds.
If the transport layer cannot send a message for any other reason, the delayable message
functionality raises the [`bt_mesh_send_cb.start`](#c.bt_mesh_send_cb.start) callback with a transport layer
error code.

If the delayable message functionality cannot find enough free memory to store an incoming
message, it will send messages with delay close to expiration to free memory.

When the mesh stack is suspended or reset, messages not yet sent are removed and
the [`bt_mesh_send_cb.start`](#c.bt_mesh_send_cb.start) callback is raised with an error code.

Note

When a model sends several messages in a row, it may happen that the messages are not sent in
the order they were passed to the access layer. This is because some messages can be delayed
for a longer time than the others.

Disable the randomization by setting the [`bt_mesh_msg_ctx.rnd_delay`](msg.md#c.bt_mesh_msg_ctx.rnd_delay "bt_mesh_msg_ctx.rnd_delay") to `false`,
when a set of messages originated by the same model needs to be sent in a certain order.

### Delayable publications

The delayable publication functionality implements the specification recommendations for message
publication delays in the following cases:

- Between 20 to 500 milliseconds when the Bluetooth Mesh stack starts or when the publication is
  triggered by the [`bt_mesh_model_publish()`](#c.bt_mesh_model_publish) function
- Between 20 to 50 milliseconds for periodically published messages

This feature is optional and enabled with the [`CONFIG_BT_MESH_DELAYABLE_PUBLICATION`](../../../../kconfig.md#CONFIG_BT_MESH_DELAYABLE_PUBLICATION "CONFIG_BT_MESH_DELAYABLE_PUBLICATION")
Kconfig option. When enabled, each model can enable or disable the delayable publication by setting
the [`bt_mesh_model_pub.delayable`](#c.bt_mesh_model_pub.delayable) bit field to `1` or `0` correspondingly. This bit
field can be changed at any time.

## API reference

*group* bt\_mesh\_access
:   Access layer.

    Group addresses

    BT\_MESH\_ADDR\_UNASSIGNED
    :   unassigned

    BT\_MESH\_ADDR\_ALL\_NODES
    :   all-nodes

    BT\_MESH\_ADDR\_RELAYS
    :   all-relays

    BT\_MESH\_ADDR\_FRIENDS
    :   all-friends

    BT\_MESH\_ADDR\_PROXIES
    :   all-proxies

    BT\_MESH\_ADDR\_DFW\_NODES
    :   all-directed-forwarding-nodes

    BT\_MESH\_ADDR\_IP\_NODES
    :   all-ipt-nodes

    BT\_MESH\_ADDR\_IP\_BR\_ROUTERS
    :   all-ipt-border-routers

    Predefined key indexes

    BT\_MESH\_KEY\_UNUSED
    :   Key unused.

    BT\_MESH\_KEY\_ANY
    :   Any key index.

    BT\_MESH\_KEY\_DEV
    :   Device key.

    BT\_MESH\_KEY\_DEV\_LOCAL
    :   Local device key.

    BT\_MESH\_KEY\_DEV\_REMOTE
    :   Remote device key.

    BT\_MESH\_KEY\_DEV\_ANY
    :   Any device key.

    Foundation Models

    BT\_MESH\_MODEL\_ID\_CFG\_SRV
    :   Configuration Server.

    BT\_MESH\_MODEL\_ID\_CFG\_CLI
    :   Configuration Client.

    BT\_MESH\_MODEL\_ID\_HEALTH\_SRV
    :   Health Server.

    BT\_MESH\_MODEL\_ID\_HEALTH\_CLI
    :   Health Client.

    BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV
    :   Remote Provisioning Server.

    BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI
    :   Remote Provisioning Client.

    BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_SRV
    :   Private Beacon Server.

    BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI
    :   Private Beacon Client.

    BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV
    :   SAR Configuration Server.

    BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI
    :   SAR Configuration Client.

    BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV
    :   Opcodes Aggregator Server.

    BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI
    :   Opcodes Aggregator Client.

    BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_SRV
    :   Large Composition Data Server.

    BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI
    :   Large Composition Data Client.

    BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_SRV
    :   Solicitation PDU RPL Configuration Client.

    BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI
    :   Solicitation PDU RPL Configuration Server.

    BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV
    :   Private Proxy Server.

    BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI
    :   Private Proxy Client.

    Models from the Mesh Model Specification

    BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_SRV
    :   Generic OnOff Server.

    BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_CLI
    :   Generic OnOff Client.

    BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_SRV
    :   Generic Level Server.

    BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_CLI
    :   Generic Level Client.

    BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_SRV
    :   Generic Default Transition Time Server.

    BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_CLI
    :   Generic Default Transition Time Client.

    BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SRV
    :   Generic Power OnOff Server.

    BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SETUP\_SRV
    :   Generic Power OnOff Setup Server.

    BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_CLI
    :   Generic Power OnOff Client.

    BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SRV
    :   Generic Power Level Server.

    BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SETUP\_SRV
    :   Generic Power Level Setup Server.

    BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_CLI
    :   Generic Power Level Client.

    BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_SRV
    :   Generic Battery Server.

    BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_CLI
    :   Generic Battery Client.

    BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SRV
    :   Generic Location Server.

    BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SETUPSRV
    :   Generic Location Setup Server.

    BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_CLI
    :   Generic Location Client.

    BT\_MESH\_MODEL\_ID\_GEN\_ADMIN\_PROP\_SRV
    :   Generic Admin Property Server.

    BT\_MESH\_MODEL\_ID\_GEN\_MANUFACTURER\_PROP\_SRV
    :   Generic Manufacturer Property Server.

    BT\_MESH\_MODEL\_ID\_GEN\_USER\_PROP\_SRV
    :   Generic User Property Server.

    BT\_MESH\_MODEL\_ID\_GEN\_CLIENT\_PROP\_SRV
    :   Generic Client Property Server.

    BT\_MESH\_MODEL\_ID\_GEN\_PROP\_CLI
    :   Generic Property Client.

    BT\_MESH\_MODEL\_ID\_SENSOR\_SRV
    :   Sensor Server.

    BT\_MESH\_MODEL\_ID\_SENSOR\_SETUP\_SRV
    :   Sensor Setup Server.

    BT\_MESH\_MODEL\_ID\_SENSOR\_CLI
    :   Sensor Client.

    BT\_MESH\_MODEL\_ID\_TIME\_SRV
    :   Time Server.

    BT\_MESH\_MODEL\_ID\_TIME\_SETUP\_SRV
    :   Time Setup Server.

    BT\_MESH\_MODEL\_ID\_TIME\_CLI
    :   Time Client.

    BT\_MESH\_MODEL\_ID\_SCENE\_SRV
    :   Scene Server.

    BT\_MESH\_MODEL\_ID\_SCENE\_SETUP\_SRV
    :   Scene Setup Server.

    BT\_MESH\_MODEL\_ID\_SCENE\_CLI
    :   Scene Client.

    BT\_MESH\_MODEL\_ID\_SCHEDULER\_SRV
    :   Scheduler Server.

    BT\_MESH\_MODEL\_ID\_SCHEDULER\_SETUP\_SRV
    :   Scheduler Setup Server.

    BT\_MESH\_MODEL\_ID\_SCHEDULER\_CLI
    :   Scheduler Client.

    BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SRV
    :   Light Lightness Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SETUP\_SRV
    :   Light Lightness Setup Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_CLI
    :   Light Lightness Client.

    BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SRV
    :   Light CTL Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SETUP\_SRV
    :   Light CTL Setup Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_CLI
    :   Light CTL Client.

    BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_TEMP\_SRV
    :   Light CTL Temperature Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SRV
    :   Light HSL Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SETUP\_SRV
    :   Light HSL Setup Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_CLI
    :   Light HSL Client.

    BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_HUE\_SRV
    :   Light HSL Hue Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SAT\_SRV
    :   Light HSL Saturation Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SRV
    :   Light xyL Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SETUP\_SRV
    :   Light xyL Setup Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_CLI
    :   Light xyL Client.

    BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SRV
    :   Light LC Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SETUPSRV
    :   Light LC Setup Server.

    BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_CLI
    :   Light LC Client.

    Models from the Mesh Binary Large Object Transfer Model Specification

    BT\_MESH\_MODEL\_ID\_BLOB\_SRV
    :   BLOB Transfer Server.

    BT\_MESH\_MODEL\_ID\_BLOB\_CLI
    :   BLOB Transfer Client.

    Models from the Mesh Device Firmware Update Model Specification

    BT\_MESH\_MODEL\_ID\_DFU\_SRV
    :   Firmware Update Server.

    BT\_MESH\_MODEL\_ID\_DFU\_CLI
    :   Firmware Update Client.

    BT\_MESH\_MODEL\_ID\_DFD\_SRV
    :   Firmware Distribution Server.

    BT\_MESH\_MODEL\_ID\_DFD\_CLI
    :   Firmware Distribution Client.

    Defines

    BT\_MESH\_ADDR\_IS\_UNICAST(addr)
    :   Check if a Bluetooth Mesh address is a unicast address.

    BT\_MESH\_ADDR\_IS\_GROUP(addr)
    :   Check if a Bluetooth Mesh address is a group address.

    BT\_MESH\_ADDR\_IS\_FIXED\_GROUP(addr)
    :   Check if a Bluetooth Mesh address is a fixed group address.

    BT\_MESH\_ADDR\_IS\_VIRTUAL(addr)
    :   Check if a Bluetooth Mesh address is a virtual address.

    BT\_MESH\_ADDR\_IS\_RFU(addr)
    :   Check if a Bluetooth Mesh address is an RFU address.

    BT\_MESH\_IS\_DEV\_KEY(key)
    :   Check if a Bluetooth Mesh key is a device key.

    BT\_MESH\_APP\_SEG\_SDU\_MAX
    :   Maximum size of an access message segment (in octets).

    BT\_MESH\_APP\_UNSEG\_SDU\_MAX
    :   Maximum payload size of an unsegmented access message (in octets).

    BT\_MESH\_RX\_SEG\_MAX
    :   Maximum number of segments supported for incoming messages.

    BT\_MESH\_TX\_SEG\_MAX
    :   Maximum number of segments supported for outgoing messages.

    BT\_MESH\_TX\_SDU\_MAX
    :   Maximum possible payload size of an outgoing access message (in octets).

    BT\_MESH\_RX\_SDU\_MAX
    :   Maximum possible payload size of an incoming access message (in octets).

    BT\_MESH\_ELEM(\_loc, \_mods, \_vnd\_mods)
    :   Helper to define a mesh element within an array.

        In case the element has no SIG or Vendor models the helper macro BT\_MESH\_MODEL\_NONE can be given instead.

        Parameters:
        :   - **\_loc** – Location Descriptor.
            - **\_mods** – Array of models.
            - **\_vnd\_mods** – Array of vendor models.

    BT\_MESH\_MODEL\_OP\_1(b0)

    BT\_MESH\_MODEL\_OP\_2(b0, b1)

    BT\_MESH\_MODEL\_OP\_3(b0, cid)

    BT\_MESH\_LEN\_EXACT(len)
    :   Macro for encoding exact message length for fixed-length messages.

    BT\_MESH\_LEN\_MIN(len)
    :   Macro for encoding minimum message length for variable-length messages.

    BT\_MESH\_MODEL\_OP\_END
    :   End of the opcode list.

        Must always be present.

    BT\_MESH\_MODEL\_NO\_OPS
    :   Helper to define an empty opcode list.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

    BT\_MESH\_MODEL\_NONE
    :   Helper to define an empty model array.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

    BT\_MESH\_MODEL\_CNT\_CB(\_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb)
    :   Composition data SIG model entry with callback functions with specific number of keys & groups.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

        Parameters:
        :   - **\_id** – Model ID.
            - **\_op** – Array of model opcode handlers.
            - **\_pub** – Model publish parameters.
            - **\_user\_data** – User data for the model.
            - **\_keys** – Number of keys that can be bound to the model. Shall not exceed  [`CONFIG_BT_MESH_MODEL_KEY_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_MODEL_KEY_COUNT "CONFIG_BT_MESH_MODEL_KEY_COUNT") .
            - **\_grps** – Number of addresses that the model can be subscribed to. Shall not exceed  [`CONFIG_BT_MESH_MODEL_GROUP_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_MODEL_GROUP_COUNT "CONFIG_BT_MESH_MODEL_GROUP_COUNT") .
            - **\_cb** – Callback structure, or NULL to keep no callbacks.

    BT\_MESH\_MODEL\_CNT\_VND\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb)
    :   Composition data vendor model entry with callback functions with specific number of keys & groups.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

        Parameters:
        :   - **\_company** – Company ID.
            - **\_id** – Model ID.
            - **\_op** – Array of model opcode handlers.
            - **\_pub** – Model publish parameters.
            - **\_user\_data** – User data for the model.
            - **\_keys** – Number of keys that can be bound to the model. Shall not exceed  [`CONFIG_BT_MESH_MODEL_KEY_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_MODEL_KEY_COUNT "CONFIG_BT_MESH_MODEL_KEY_COUNT") .
            - **\_grps** – Number of addresses that the model can be subscribed to. Shall not exceed  [`CONFIG_BT_MESH_MODEL_GROUP_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_MODEL_GROUP_COUNT "CONFIG_BT_MESH_MODEL_GROUP_COUNT") .
            - **\_cb** – Callback structure, or NULL to keep no callbacks.

    BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)
    :   Composition data SIG model entry with callback functions.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

        Parameters:
        :   - **\_id** – Model ID.
            - **\_op** – Array of model opcode handlers.
            - **\_pub** – Model publish parameters.
            - **\_user\_data** – User data for the model.
            - **\_cb** – Callback structure, or NULL to keep no callbacks.

    BT\_MESH\_MODEL\_METADATA\_CB(\_id, \_op, \_pub, \_user\_data, \_cb, \_metadata)
    :   Composition data SIG model entry with callback functions and metadata.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

        Parameters:
        :   - **\_id** – Model ID.
            - **\_op** – Array of model opcode handlers.
            - **\_pub** – Model publish parameters.
            - **\_user\_data** – User data for the model.
            - **\_cb** – Callback structure, or NULL to keep no callbacks.
            - **\_metadata** – Metadata structure.

    BT\_MESH\_MODEL\_VND\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_cb)
    :   Composition data vendor model entry with callback functions.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

        Parameters:
        :   - **\_company** – Company ID.
            - **\_id** – Model ID.
            - **\_op** – Array of model opcode handlers.
            - **\_pub** – Model publish parameters.
            - **\_user\_data** – User data for the model.
            - **\_cb** – Callback structure, or NULL to keep no callbacks.

    BT\_MESH\_MODEL\_VND\_METADATA\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_cb, \_metadata)
    :   Composition data vendor model entry with callback functions and metadata.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

        Parameters:
        :   - **\_company** – Company ID.
            - **\_id** – Model ID.
            - **\_op** – Array of model opcode handlers.
            - **\_pub** – Model publish parameters.
            - **\_user\_data** – User data for the model.
            - **\_cb** – Callback structure, or NULL to keep no callbacks.
            - **\_metadata** – Metadata structure.

    BT\_MESH\_MODEL(\_id, \_op, \_pub, \_user\_data)
    :   Composition data SIG model entry.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

        Parameters:
        :   - **\_id** – Model ID.
            - **\_op** – Array of model opcode handlers.
            - **\_pub** – Model publish parameters.
            - **\_user\_data** – User data for the model.

    BT\_MESH\_MODEL\_VND(\_company, \_id, \_op, \_pub, \_user\_data)
    :   Composition data vendor model entry.

        This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

        Parameters:
        :   - **\_company** – Company ID.
            - **\_id** – Model ID.
            - **\_op** – Array of model opcode handlers.
            - **\_pub** – Model publish parameters.
            - **\_user\_data** – User data for the model.

    BT\_MESH\_TRANSMIT(count, int\_ms)
    :   Encode transmission count & interval steps.

        Parameters:
        :   - **count** – Number of retransmissions (first transmission is excluded).
            - **int\_ms** – Interval steps in milliseconds. Must be greater than 0, less than or equal to 320, and a multiple of 10.

        Returns:
        :   Mesh transmit value that can be used e.g. for the default values of the configuration model data.

    BT\_MESH\_TRANSMIT\_COUNT(transmit)
    :   Decode transmit count from a transmit value.

        Parameters:
        :   - **transmit** – Encoded transmit count & interval value.

        Returns:
        :   Transmission count (actual transmissions is N + 1).

    BT\_MESH\_TRANSMIT\_INT(transmit)
    :   Decode transmit interval from a transmit value.

        Parameters:
        :   - **transmit** – Encoded transmit count & interval value.

        Returns:
        :   Transmission interval in milliseconds.

    BT\_MESH\_PUB\_TRANSMIT(count, int\_ms)
    :   Encode Publish Retransmit count & interval steps.

        Parameters:
        :   - **count** – Number of retransmissions (first transmission is excluded).
            - **int\_ms** – Interval steps in milliseconds. Must be greater than 0 and a multiple of 50.

        Returns:
        :   Mesh transmit value that can be used e.g. for the default values of the configuration model data.

    BT\_MESH\_PUB\_TRANSMIT\_COUNT(transmit)
    :   Decode Publish Retransmit count from a given value.

        Parameters:
        :   - **transmit** – Encoded Publish Retransmit count & interval value.

        Returns:
        :   Retransmission count (actual transmissions is N + 1).

    BT\_MESH\_PUB\_TRANSMIT\_INT(transmit)
    :   Decode Publish Retransmit interval from a given value.

        Parameters:
        :   - **transmit** – Encoded Publish Retransmit count & interval value.

        Returns:
        :   Transmission interval in milliseconds.

    BT\_MESH\_PUB\_MSG\_TOTAL(pub)
    :   Get total number of messages within one publication interval including initial publication.

        Parameters:
        :   - **pub** – Model publication context.

        Returns:
        :   total number of messages.

    BT\_MESH\_PUB\_MSG\_NUM(pub)
    :   Get message number within one publication interval.

        Meant to be used inside [bt\_mesh\_model\_pub::update](#structbt__mesh__model__pub_1a0354344e08e633dc4d6c0b4e7b169080).

        Parameters:
        :   - **pub** – Model publication context.

        Returns:
        :   message number starting from 1.

    BT\_MESH\_MODEL\_PUB\_DEFINE(\_name, \_update, \_msg\_len)
    :   Define a model publication context.

        Parameters:
        :   - **\_name** – Variable name given to the context.
            - **\_update** – Optional message update callback (may be NULL).
            - **\_msg\_len** – Length of the publication message.

    BT\_MESH\_MODELS\_METADATA\_ENTRY(\_len, \_id, \_data)
    :   Initialize a Models Metadata entry structure in a list.

        Parameters:
        :   - **\_len** – Length of the metadata entry.
            - **\_id** – ID of the Models Metadata entry.
            - **\_data** – Pointer to a contiguous memory that contains the metadata.

    BT\_MESH\_MODELS\_METADATA\_NONE
    :   Helper to define an empty Models metadata array.

    BT\_MESH\_MODELS\_METADATA\_END
    :   End of the Models Metadata list.

        Must always be present.

    BT\_MESH\_TTL\_DEFAULT
    :   Special TTL value to request using configured default TTL.

    BT\_MESH\_TTL\_MAX
    :   Maximum allowed TTL value.

    Functions

    int bt\_mesh\_model\_send(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*msg, const struct [bt\_mesh\_send\_cb](#c.bt_mesh_send_cb) \*cb, void \*cb\_data)
    :   Send an Access Layer message.

        Parameters:
        :   - **model** – Mesh (client) Model that the message belongs to.
            - **ctx** – Message context, includes keys, TTL, etc.
            - **msg** – Access Layer payload (the actual message to be sent).
            - **cb** – Optional “message sent” callback.
            - **cb\_data** – User data to be passed to the callback.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_model\_publish(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model)
    :   Send a model publication message.

        Before calling this function, the user needs to ensure that the model publication message ([bt\_mesh\_model\_pub::msg](#structbt__mesh__model__pub_1a5f5639c01d3704ec3d527c418d35f827)) contains a valid message to be sent. Note that this API is only to be used for non-period publishing. For periodic publishing the app only needs to make sure that [bt\_mesh\_model\_pub::msg](#structbt__mesh__model__pub_1a5f5639c01d3704ec3d527c418d35f827) contains a valid message whenever the [bt\_mesh\_model\_pub::update](#structbt__mesh__model__pub_1a0354344e08e633dc4d6c0b4e7b169080) callback is called.

        Parameters:
        :   - **model** – Mesh (client) Model that’s publishing the message.

        Returns:
        :   0 on success, or (negative) error code on failure.

    static inline bool bt\_mesh\_model\_pub\_is\_retransmission(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model)
    :   Check if a message is being retransmitted.

        Meant to be used inside the [bt\_mesh\_model\_pub::update](#structbt__mesh__model__pub_1a0354344e08e633dc4d6c0b4e7b169080) callback.

        Parameters:
        :   - **model** – Mesh Model that supports publication.

        Returns:
        :   true if this is a retransmission, false if this is a first publication.

    const struct [bt\_mesh\_elem](#c.bt_mesh_elem) \*bt\_mesh\_model\_elem(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*mod)
    :   Get the element that a model belongs to.

        Parameters:
        :   - **mod** – Mesh model.

        Returns:
        :   Pointer to the element that the given model belongs to.

    const struct [bt\_mesh\_model](#c.bt_mesh_model) \*bt\_mesh\_model\_find(const struct [bt\_mesh\_elem](#c.bt_mesh_elem) \*elem, uint16\_t id)
    :   Find a SIG model.

        Parameters:
        :   - **elem** – Element to search for the model in.
            - **id** – Model ID of the model.

        Returns:
        :   A pointer to the Mesh model matching the given parameters, or NULL if no SIG model with the given ID exists in the given element.

    const struct [bt\_mesh\_model](#c.bt_mesh_model) \*bt\_mesh\_model\_find\_vnd(const struct [bt\_mesh\_elem](#c.bt_mesh_elem) \*elem, uint16\_t company, uint16\_t id)
    :   Find a vendor model.

        Parameters:
        :   - **elem** – Element to search for the model in.
            - **company** – Company ID of the model.
            - **id** – Model ID of the model.

        Returns:
        :   A pointer to the Mesh model matching the given parameters, or NULL if no vendor model with the given ID exists in the given element.

    static inline bool bt\_mesh\_model\_in\_primary(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*mod)
    :   Get whether the model is in the primary element of the device.

        Parameters:
        :   - **mod** – Mesh model.

        Returns:
        :   true if the model is on the primary element, false otherwise.

    int bt\_mesh\_model\_data\_store(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*mod, bool vnd, const char \*name, const void \*data, size\_t data\_len)
    :   Immediately store the model’s user data in persistent storage.

        Parameters:
        :   - **mod** – Mesh model.
            - **vnd** – This is a vendor model.
            - **name** – Name/key of the settings item. Only [SETTINGS\_MAX\_DIR\_DEPTH](../../../../services/settings/index.md#group__settings_1ga2afa32b032e88a188c5263156d9e73e1) bytes will be used at most.
            - **data** – Model data to store, or NULL to delete any model data.
            - **data\_len** – Length of the model data.

        Returns:
        :   0 on success, or (negative) error code on failure.

    void bt\_mesh\_model\_data\_store\_schedule(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*mod)
    :   Schedule the model’s user data store in persistent storage.

        This function triggers the [bt\_mesh\_model\_cb::pending\_store](#structbt__mesh__model__cb_1ae28f875dffc7f5f2ce99abe590369f43) callback for the corresponding model after delay defined by  [`CONFIG_BT_MESH_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_STORE_TIMEOUT "CONFIG_BT_MESH_STORE_TIMEOUT") .

        The delay is global for all models. Once scheduled, the callback can not be re-scheduled until previous schedule completes.

        Parameters:
        :   - **mod** – Mesh model.

    int bt\_mesh\_model\_extend(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*extending\_mod, const struct [bt\_mesh\_model](#c.bt_mesh_model) \*base\_mod)
    :   Let a model extend another.

        Mesh models may be extended to reuse their functionality, forming a more complex model. A Mesh model may extend any number of models, in any element. The extensions may also be nested, ie a model that extends another may itself be extended.

        A set of models that extend each other form a model extension list.

        All models in an extension list share one subscription list per element. The access layer will utilize the combined subscription list of all models in an extension list and element, giving the models extended subscription list capacity.

        If  [`CONFIG_BT_MESH_COMP_PAGE_1`](../../../../kconfig.md#CONFIG_BT_MESH_COMP_PAGE_1 "CONFIG_BT_MESH_COMP_PAGE_1") is enabled, it is not allowed to call this function before the [bt\_mesh\_model\_cb::init](#structbt__mesh__model__cb_1a1688a2c6d7b3b17ba49a0975b6f4f68e) callback is called for both models, except if it is called as part of the final callback.

        Parameters:
        :   - **extending\_mod** – Mesh model that is extending the base model.
            - **base\_mod** – The model being extended.

        Return values:
        :   **0** – Successfully extended the base\_mod model.

    int bt\_mesh\_model\_correspond(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*corresponding\_mod, const struct [bt\_mesh\_model](#c.bt_mesh_model) \*base\_mod)
    :   Let a model correspond to another.

        Mesh models may correspond to each other, which means that if one is present, other must be present too. A Mesh model may correspond to any number of models, in any element. All models connected together via correspondence form single Correspondence Group, which has it’s unique Correspondence ID. Information about Correspondence is used to construct Composition Data Page 1.

        This function must be called on already initialized base\_mod. Because this function is designed to be called in corresponding\_mod initializer, this means that base\_mod shall be initialized before corresponding\_mod is.

        Parameters:
        :   - **corresponding\_mod** – Mesh model that is corresponding to the base model.
            - **base\_mod** – The model being corresponded to.

        Return values:
        :   - **0** – Successfully saved correspondence to the base\_mod model.
            - **-ENOMEM** – There is no more space to save this relation.
            - **-ENOTSUP** – Composition Data Page 1 is not supported.

    bool bt\_mesh\_model\_is\_extended(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model)
    :   Check if model is extended by another model.

        Parameters:
        :   - **model** – The model to check.

        Return values:
        :   **true** – If model is extended by another model, otherwise false

    int bt\_mesh\_comp\_change\_prepare(void)
    :   Indicate that the composition data will change on next bootup.

        Tell the config server that the composition data is expected to change on the next bootup, and the current composition data should be backed up.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_mesh\_models\_metadata\_change\_prepare(void)
    :   Indicate that the metadata will change on next bootup.

        Tell the config server that the models metadata is expected to change on the next bootup, and the current models metadata should be backed up.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_mesh\_comp2\_register(const struct [bt\_mesh\_comp2](#c.bt_mesh_comp2) \*comp2)
    :   Register composition data page 2 of the device.

        Register Mesh Profiles information (Ref section 3.12 in Bluetooth SIG Assigned Numbers) for composition data page 2 of the device.

        Note

        There must be at least one record present in `comp2`

        Parameters:
        :   - **comp2** – Pointer to composition data page 2.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    struct bt\_mesh\_elem
    :   *#include <access.h>*

        Abstraction that describes a Mesh Element.

        Public Members

        const uint16\_t loc
        :   Location Descriptor (GATT Bluetooth Namespace Descriptors).

        const uint8\_t model\_count
        :   The number of SIG models in this element.

        const uint8\_t vnd\_model\_count
        :   The number of vendor models in this element.

        const struct [bt\_mesh\_model](#c.bt_mesh_model) \*const models
        :   The list of SIG models in this element.

        const struct [bt\_mesh\_model](#c.bt_mesh_model) \*const vnd\_models
        :   The list of vendor models in this element.

        struct bt\_mesh\_elem\_rt\_ctx
        :   *#include <access.h>*

            Mesh Element runtime information.

            Public Members

            uint16\_t addr
            :   Unicast Address.

                Set at runtime during provisioning.

    struct bt\_mesh\_model\_op
    :   *#include <access.h>*

        Model opcode handler.

        Public Members

        const uint32\_t opcode
        :   OpCode encoded using the BT\_MESH\_MODEL\_OP\_\* macros.

        const ssize\_t len
        :   Message length.

            If the message has variable length then this value indicates minimum message length and should be positive. Handler function should verify precise length based on the contents of the message. If the message has fixed length then this value should be negative. Use BT\_MESH\_LEN\_\* macros when defining this value.

        int (\*const func)(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
        :   Handler function for this opcode.

            Param model:
            :   Model instance receiving the message.

            Param ctx:
            :   Message context for the message.

            Param buf:
            :   Message buffer containing the message payload, not including the opcode.

            Return:
            :   Zero on success or (negative) error code otherwise.

    struct bt\_mesh\_model\_pub
    :   *#include <access.h>*

        Model publication context.

        The context should primarily be created using the BT\_MESH\_MODEL\_PUB\_DEFINE macro.

        Public Members

        const struct [bt\_mesh\_model](#c.bt_mesh_model) \*mod
        :   The model the context belongs to.

            Initialized by the stack.

        uint16\_t addr
        :   Publish Address.

        const uint8\_t \*uuid
        :   Label UUID if Publish Address is Virtual Address.

        uint16\_t key
        :   Publish AppKey Index.

        uint16\_t cred
        :   Friendship Credentials Flag.

        uint16\_t send\_rel
        :   Force reliable sending (segment acks).

        uint16\_t fast\_period
        :   Use FastPeriodDivisor.

        uint16\_t retr\_update
        :   Call update callback on every retransmission.

        uint8\_t ttl
        :   Publish Time to Live.

        uint8\_t retransmit
        :   Retransmit Count & Interval Steps.

        uint8\_t period
        :   Publish Period.

        uint8\_t period\_div
        :   Divisor for the Period.

        uint8\_t count
        :   Transmissions left.

        uint8\_t delayable
        :   Use random delay for publishing.

        uint32\_t period\_start
        :   Start of the current period.

        struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*msg
        :   Publication buffer, containing the publication message.

            This will get correctly created when the publication context has been defined using the BT\_MESH\_MODEL\_PUB\_DEFINE macro.

            ```text
            BT_MESH_MODEL_PUB_DEFINE(name, update, size);
            ```

        int (\*update)(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*mod)
        :   Callback for updating the publication buffer.

            When set to NULL, the model is assumed not to support periodic publishing. When set to non-NULL the callback will be called periodically and is expected to update [bt\_mesh\_model\_pub::msg](#structbt__mesh__model__pub_1a5f5639c01d3704ec3d527c418d35f827) with a valid publication message.

            If the callback returns non-zero, the publication is skipped and will resume on the next periodic publishing interval.

            When [bt\_mesh\_model\_pub::retr\_update](#structbt__mesh__model__pub_1a16c13e46c012ab836acd02b8fe5f05e3) is set to 1, the callback will be called on every retransmission.

            Param mod:
            :   The Model the Publication Context belongs to.

            Return:
            :   Zero on success or (negative) error code otherwise.

        struct [k\_work\_delayable](../../../../kernel/services/threads/workqueue.md#c.k_work_delayable "k_work_delayable") timer
        :   Publish Period Timer.

            Only for stack-internal use.

    struct bt\_mesh\_models\_metadata\_entry
    :   *#include <access.h>*

        Models Metadata Entry struct.

        The struct should primarily be created using the BT\_MESH\_MODELS\_METADATA\_ENTRY macro.

    struct bt\_mesh\_model\_cb
    :   *#include <access.h>*

        Model callback functions.

        Public Members

        int (\*const settings\_set)(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model, const char \*name, size\_t len\_rd, [settings\_read\_cb](../../../../services/settings/index.md#c.settings_read_cb "settings_read_cb") read\_cb, void \*cb\_arg)
        :   Set value handler of user data tied to the model.

            See also

            [settings\_handler::h\_set](../../../../services/settings/index.md#structsettings__handler_1a70aa25bf3b53898ab22906e9949963a4)

            Param model:
            :   Model to set the persistent data of.

            Param name:
            :   Name/key of the settings item.

            Param len\_rd:
            :   The size of the data found in the backend.

            Param read\_cb:
            :   Function provided to read the data from the backend.

            Param cb\_arg:
            :   Arguments for the read function provided by the backend.

            Return:
            :   0 on success, error otherwise.

        int (\*const start)(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model)
        :   Callback called when the mesh is started.

            This handler gets called after the node has been provisioned, or after all mesh data has been loaded from persistent storage.

            When this callback fires, the mesh model may start its behavior, and all Access APIs are ready for use.

            Param model:
            :   Model this callback belongs to.

            Return:
            :   0 on success, error otherwise.

        int (\*const init)(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model)
        :   Model init callback.

            Called on every model instance during mesh initialization.

            If any of the model init callbacks return an error, the Mesh subsystem initialization will be aborted, and the error will be returned to the caller of [bt\_mesh\_init](core.md#group__bt__mesh_1ga521def6f74467a9bd3f2757c6aabd405).

            Param model:
            :   Model to be initialized.

            Return:
            :   0 on success, error otherwise.

        void (\*const reset)(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model)
        :   Model reset callback.

            Called when the mesh node is reset. All model data is deleted on reset, and the model should clear its state.

            Note

            If the model stores any persistent data, this needs to be erased manually.

            Param model:
            :   Model this callback belongs to.

        void (\*const pending\_store)(const struct [bt\_mesh\_model](#c.bt_mesh_model) \*model)
        :   Callback used to store pending model’s user data.

            Triggered by [bt\_mesh\_model\_data\_store\_schedule](#group__bt__mesh__access_1ga762896dd2e806b5be061b220d53ce4db).

            To store the user data, call [bt\_mesh\_model\_data\_store](#group__bt__mesh__access_1gadff0895c5c34928d778fa615512b3d85).

            Param model:
            :   Model this callback belongs to.

    struct bt\_mesh\_mod\_id\_vnd
    :   *#include <access.h>*

        Vendor model ID.

        Public Members

        uint16\_t company
        :   Vendor’s company ID.

        uint16\_t id
        :   Model ID.

    struct bt\_mesh\_model
    :   *#include <access.h>*

        Abstraction that describes a Mesh Model instance.

        Public Members

        const uint16\_t id
        :   SIG model ID.

        const struct [bt\_mesh\_mod\_id\_vnd](#c.bt_mesh_mod_id_vnd) vnd
        :   Vendor model ID.

        struct [bt\_mesh\_model\_pub](#c.bt_mesh_model_pub) \*const pub
        :   Model Publication.

        uint16\_t \*const keys
        :   AppKey List.

        uint16\_t \*const groups
        :   Subscription List (group or virtual addresses).

        const uint8\_t \*\*const uuids
        :   List of Label UUIDs the model is subscribed to.

        const struct [bt\_mesh\_model\_op](#c.bt_mesh_model_op) \*const op
        :   Opcode handler list.

        const struct [bt\_mesh\_model\_cb](#c.bt_mesh_model_cb) \*const cb
        :   Model callback structure.

        struct bt\_mesh\_model\_rt\_ctx
        :   *#include <access.h>*

            Public Members

            void \*user\_data
            :   Model-specific user data.

    struct bt\_mesh\_send\_cb
    :   *#include <access.h>*

        Callback structure for monitoring model message sending.

        Public Members

        void (\*start)(uint16\_t duration, int err, void \*cb\_data)
        :   Handler called at the start of the transmission.

            Param duration:
            :   The duration of the full transmission.

            Param err:
            :   Error occurring during sending.

            Param cb\_data:
            :   Callback data, as passed to the send API.

        void (\*end)(int err, void \*cb\_data)
        :   Handler called at the end of the transmission.

            Param err:
            :   Error occurring during sending.

            Param cb\_data:
            :   Callback data, as passed to the send API.

    struct bt\_mesh\_comp
    :   *#include <access.h>*

        Node Composition.

        Public Members

        uint16\_t cid
        :   Company ID.

        uint16\_t pid
        :   Product ID.

        uint16\_t vid
        :   Version ID.

        size\_t elem\_count
        :   The number of elements in this device.

        const struct [bt\_mesh\_elem](#c.bt_mesh_elem) \*elem
        :   List of elements.

    struct bt\_mesh\_comp2\_record
    :   *#include <access.h>*

        Composition data page 2 record.

        Public Members

        uint16\_t id
        :   Mesh profile ID.

        uint8\_t x
        :   Major version.

        uint8\_t y
        :   Minor version.

        uint8\_t z
        :   Z version.

        struct [bt\_mesh\_comp2\_record](#c.bt_mesh_comp2_record).[anonymous] version
        :   Mesh Profile Version.

        uint8\_t elem\_offset\_cnt
        :   Element offset count.

        const uint8\_t \*elem\_offset
        :   Element offset list.

        uint16\_t data\_len
        :   Length of additional data.

        const void \*data
        :   Additional data.

    struct bt\_mesh\_comp2
    :   *#include <access.h>*

        Node Composition data page 2.

        Public Members

        size\_t record\_cnt
        :   The number of Mesh Profile records on a device.

        const struct [bt\_mesh\_comp2\_record](#c.bt_mesh_comp2_record) \*record
        :   List of records.
