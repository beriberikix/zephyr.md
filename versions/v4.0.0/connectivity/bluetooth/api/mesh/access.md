---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/access.html
original_path: connectivity/bluetooth/api/mesh/access.html
---

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
data, which is passed to [`bt_mesh_init()`](../../../../doxygen/html/group__bt__mesh.md#ga521def6f74467a9bd3f2757c6aabd405) during initialization. The
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
determined by the special [`BT_MESH_MODEL_OP_END`](../../../../doxygen/html/group__bt__mesh__access.md#gaf2c164506c601214c85d451747176827) entry. This entry
must always be present in the opcode list, unless the list is empty. In that
case, [`BT_MESH_MODEL_NO_OPS`](../../../../doxygen/html/group__bt__mesh__access.md#gae6d55e0a27bb7c448affd312a2e11656) should be used in place of a proper
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

- By specifying a set of message parameters in a [`bt_mesh_msg_ctx`](../../../../doxygen/html/structbt__mesh__msg__ctx.md),
  and calling [`bt_mesh_model_send()`](../../../../doxygen/html/group__bt__mesh__access.md#ga7cac052ef76f4b37a95343329b078e77).
- By setting up a [`bt_mesh_model_pub`](../../../../doxygen/html/structbt__mesh__model__pub.md) structure and calling
  [`bt_mesh_model_publish()`](../../../../doxygen/html/group__bt__mesh__access.md#ga06644f8a5fa43351328d3f3403dbad03).

When publishing messages with [`bt_mesh_model_publish()`](../../../../doxygen/html/group__bt__mesh__access.md#ga06644f8a5fa43351328d3f3403dbad03), the model
will use the publication parameters configured by the
[Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv). This is the recommended way to send
unprompted model messages, as it passes the responsibility of selecting
message parameters to the network administrator, which likely knows more about
the mesh network than the individual nodes will.

To support publishing with the publication parameters, the model must allocate
a packet buffer for publishing, and pass it to
[`bt_mesh_model_pub.msg`](../../../../doxygen/html/structbt__mesh__model__pub.md#a5f5639c01d3704ec3d527c418d35f827). The Config Server may also set up period
publication for the publication message. To support this, the model must
populate the [`bt_mesh_model_pub.update`](../../../../doxygen/html/structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080) callback. The
[`bt_mesh_model_pub.update`](../../../../doxygen/html/structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080) callback will be called right before the
message is published, allowing the model to change the payload to reflect its
current state.

By setting [`bt_mesh_model_pub.retr_update`](../../../../doxygen/html/structbt__mesh__model__pub.md#a16c13e46c012ab836acd02b8fe5f05e3) to 1, the model can
configure the [`bt_mesh_model_pub.update`](../../../../doxygen/html/structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080) callback to be triggered
on every retransmission. This can, for example, be used by models that make
use of a Delay parameter, which can be adjusted for every retransmission.
The [`bt_mesh_model_pub_is_retransmission()`](../../../../doxygen/html/group__bt__mesh__access.md#ga1b961d45f8b7c231c698ca229115e434) function can be
used to differentiate a first publication and a retransmission.
The [`BT_MESH_PUB_MSG_TOTAL`](../../../../doxygen/html/group__bt__mesh__access.md#ga230538bb39ac3d6c8c0327d1fad77e69) and [`BT_MESH_PUB_MSG_NUM`](../../../../doxygen/html/group__bt__mesh__access.md#ga115ee29aba3c3e985aa11d6692ca0d83) macros
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

Model extensions are done by calling [`bt_mesh_model_extend()`](../../../../doxygen/html/group__bt__mesh__access.md#gaf6356f715c8968151b8d539f2dd1880c) during
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
[`bt_mesh_model_data_store()`](../../../../doxygen/html/group__bt__mesh__access.md#gadff0895c5c34928d778fa615512b3d85). To be able to read out the data the
next time the device reboots, the model’s
[`bt_mesh_model_cb.settings_set`](../../../../doxygen/html/structbt__mesh__model__cb.md#a21fc24829c6933a035b0f0be1a1f58e5) callback must be populated. This
callback gets called when model specific data is found in the persistent
storage. The model can retrieve the data by calling the `read_cb` passed as
a parameter to the callback. See the [Settings](../../../../services/settings/index.md#settings-api) module documentation for
details.

When model data changes frequently, storing it on every change may lead to
increased wear of flash. To reduce the wear, the model can postpone storing of
data by calling [`bt_mesh_model_data_store_schedule()`](../../../../doxygen/html/group__bt__mesh__access.md#ga762896dd2e806b5be061b220d53ce4db). The stack will
schedule a work item with delay defined by the
[`CONFIG_BT_MESH_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_STORE_TIMEOUT "CONFIG_BT_MESH_STORE_TIMEOUT") option. When the work item is
running, the stack will call the [`bt_mesh_model_cb.pending_store`](../../../../doxygen/html/structbt__mesh__model__cb.md#ae28f875dffc7f5f2ce99abe590369f43)
callback for every model that has requested storing of data. The model can
then call [`bt_mesh_model_data_store()`](../../../../doxygen/html/group__bt__mesh__access.md#gadff0895c5c34928d778fa615512b3d85) to store the data.

If [`CONFIG_BT_MESH_SETTINGS_WORKQ`](../../../../kconfig.md#CONFIG_BT_MESH_SETTINGS_WORKQ "CONFIG_BT_MESH_SETTINGS_WORKQ") is enabled, the
[`bt_mesh_model_cb.pending_store`](../../../../doxygen/html/structbt__mesh__model__cb.md#ae28f875dffc7f5f2ce99abe590369f43) callback is called from a dedicated
thread. This allows the stack to process other incoming and outgoing messages
while model data is being stored. It is recommended to use this option and the
[`bt_mesh_model_data_store_schedule()`](../../../../doxygen/html/group__bt__mesh__access.md#ga762896dd2e806b5be061b220d53ce4db) function when large amount of data
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
or more models. A model can extend another model by calling [`bt_mesh_model_extend()`](../../../../doxygen/html/group__bt__mesh__access.md#gaf6356f715c8968151b8d539f2dd1880c),
or correspond to another model by calling [`bt_mesh_model_correspond()`](../../../../doxygen/html/group__bt__mesh__access.md#ga03ce9f6f9ccf734ea72beede09288923).
[`CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE`](../../../../kconfig.md#CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE "CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE") specifies how many model
relations can be stored in the composition on a device, and this number should reflect the
number of [`bt_mesh_model_extend()`](../../../../doxygen/html/group__bt__mesh__access.md#gaf6356f715c8968151b8d539f2dd1880c) and [`bt_mesh_model_correspond()`](../../../../doxygen/html/group__bt__mesh__access.md#ga03ce9f6f9ccf734ea72beede09288923) calls.

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

The delayable message functionality is triggered if the [`bt_mesh_msg_ctx.rnd_delay`](../../../../doxygen/html/structbt__mesh__msg__ctx.md#acb5b5de55f35b37ba4f34ffc08943184)
flag is set.
The delayable message functionality stores messages in the local memory while they are
waiting for the random delay expiration.

If the transport layer doesn’t have sufficient memory to send a message at the moment
the random delay expires, the message is postponed for another 10 milliseconds.
If the transport layer cannot send a message for any other reason, the delayable message
functionality raises the [`bt_mesh_send_cb.start`](../../../../doxygen/html/structbt__mesh__send__cb.md#a2f84ef4cb2d28729cd98b844a3d25f55) callback with a transport layer
error code.

If the delayable message functionality cannot find enough free memory to store an incoming
message, it will send messages with delay close to expiration to free memory.

When the mesh stack is suspended or reset, messages not yet sent are removed and
the [`bt_mesh_send_cb.start`](../../../../doxygen/html/structbt__mesh__send__cb.md#a2f84ef4cb2d28729cd98b844a3d25f55) callback is raised with an error code.

Note

When a model sends several messages in a row, it may happen that the messages are not sent in
the order they were passed to the access layer. This is because some messages can be delayed
for a longer time than the others.

Disable the randomization by setting the [`bt_mesh_msg_ctx.rnd_delay`](../../../../doxygen/html/structbt__mesh__msg__ctx.md#acb5b5de55f35b37ba4f34ffc08943184) to `false`,
when a set of messages originated by the same model needs to be sent in a certain order.

### Delayable publications

The delayable publication functionality implements the specification recommendations for message
publication delays in the following cases:

- Between 20 to 500 milliseconds when the Bluetooth Mesh stack starts or when the publication is
  triggered by the [`bt_mesh_model_publish()`](../../../../doxygen/html/group__bt__mesh__access.md#ga06644f8a5fa43351328d3f3403dbad03) function
- Between 20 to 50 milliseconds for periodically published messages

This feature is optional and enabled with the [`CONFIG_BT_MESH_DELAYABLE_PUBLICATION`](../../../../kconfig.md#CONFIG_BT_MESH_DELAYABLE_PUBLICATION "CONFIG_BT_MESH_DELAYABLE_PUBLICATION")
Kconfig option. When enabled, each model can enable or disable the delayable publication by setting
the [`bt_mesh_model_pub.delayable`](../../../../doxygen/html/structbt__mesh__model__pub.md#a23a865dbd2dce5c1af074097864611e9) bit field to `1` or `0` correspondingly. This bit
field can be changed at any time.

## API reference

[Access layer](../../../../doxygen/html/group__bt__mesh__access.md)
