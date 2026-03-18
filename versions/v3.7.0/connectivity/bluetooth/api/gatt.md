---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/gatt.html
original_path: connectivity/bluetooth/api/gatt.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Generic Attribute Profile (GATT)

GATT layer manages the service database providing APIs for service registration
and attribute declaration.

Services can be registered using [`bt_gatt_service_register()`](#c.bt_gatt_service_register) API
which takes the [`bt_gatt_service`](#c.bt_gatt_service) struct that provides the list of
attributes the service contains. The helper macro [`BT_GATT_SERVICE()`](#c.BT_GATT_SERVICE)
can be used to declare a service.

Attributes can be declared using the [`bt_gatt_attr`](#c.bt_gatt_attr) struct or using
one of the helper macros:

> [`BT_GATT_PRIMARY_SERVICE`](#c.BT_GATT_PRIMARY_SERVICE)
> :   Declares a Primary Service.
>
> [`BT_GATT_SECONDARY_SERVICE`](#c.BT_GATT_SECONDARY_SERVICE)
> :   Declares a Secondary Service.
>
> [`BT_GATT_INCLUDE_SERVICE`](#c.BT_GATT_INCLUDE_SERVICE)
> :   Declares a Include Service.
>
> [`BT_GATT_CHARACTERISTIC`](#c.BT_GATT_CHARACTERISTIC)
> :   Declares a Characteristic.
>
> [`BT_GATT_DESCRIPTOR`](#c.BT_GATT_DESCRIPTOR)
> :   Declares a Descriptor.
>
> [`BT_GATT_ATTRIBUTE`](#c.BT_GATT_ATTRIBUTE)
> :   Declares an Attribute.
>
> [`BT_GATT_CCC`](#c.BT_GATT_CCC)
> :   Declares a Client Characteristic Configuration.
>
> [`BT_GATT_CEP`](#c.BT_GATT_CEP)
> :   Declares a Characteristic Extended Properties.
>
> [`BT_GATT_CUD`](#c.BT_GATT_CUD)
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

Attribute value changes can be notified using [`bt_gatt_notify()`](#c.bt_gatt_notify) API,
alternatively there is [`bt_gatt_notify_cb()`](#c.bt_gatt_notify_cb) where it is possible to
pass a callback to be called when it is necessary to know the exact instant when
the data has been transmitted over the air. Indications are supported by
[`bt_gatt_indicate()`](#c.bt_gatt_indicate) API.

Client procedures can be enabled with the configuration option:
[`CONFIG_BT_GATT_CLIENT`](../../../kconfig.md#CONFIG_BT_GATT_CLIENT "CONFIG_BT_GATT_CLIENT")

Discover procedures can be initiated with the use of
[`bt_gatt_discover()`](#c.bt_gatt_discover) API which takes the
[`bt_gatt_discover_params`](#c.bt_gatt_discover_params) struct which describes the type of
discovery. The parameters also serves as a filter when setting the `uuid`
field only attributes which matches will be discovered, in contrast setting it
to NULL allows all attributes to be discovered.

Note

Caching discovered attributes is not supported.

Read procedures are supported by [`bt_gatt_read()`](#c.bt_gatt_read) API which takes the
[`bt_gatt_read_params`](#c.bt_gatt_read_params) struct as parameters. In the parameters one or
more attributes can be set, though setting multiple handles requires the option:
[`CONFIG_BT_GATT_READ_MULTIPLE`](../../../kconfig.md#CONFIG_BT_GATT_READ_MULTIPLE "CONFIG_BT_GATT_READ_MULTIPLE")

Write procedures are supported by [`bt_gatt_write()`](#c.bt_gatt_write) API and takes
[`bt_gatt_write_params`](#c.bt_gatt_write_params) struct as parameters. In case the write
operation don’t require a response [`bt_gatt_write_without_response()`](#c.bt_gatt_write_without_response)
or [`bt_gatt_write_without_response_cb()`](#c.bt_gatt_write_without_response_cb) APIs can be used, with the
later working similarly to [`bt_gatt_notify_cb()`](#c.bt_gatt_notify_cb).

Subscriptions to notification and indication can be initiated with use of
[`bt_gatt_subscribe()`](#c.bt_gatt_subscribe) API which takes
[`bt_gatt_subscribe_params`](#c.bt_gatt_subscribe_params) as parameters. Multiple subscriptions to
the same attribute are supported so there could be multiple `notify` callback
being triggered for the same attribute. Subscriptions can be removed with use of
[`bt_gatt_unsubscribe()`](#c.bt_gatt_unsubscribe) API.

Note

When subscriptions are removed `notify` callback is called with the data
set to NULL.

## API Reference

Related code samples

[BLE logging backend](../../../samples/subsys/logging/ble_backend/README.md#logging-ble-backend "Send log messages over BLE using the BLE logging backend.")
:   Send log messages over BLE using the BLE logging backend.

*group* Generic Attribute Profile (GATT)
:   Generic Attribute Profile (GATT).

    Defines

    BT\_GATT\_ERR(\_att\_err)
    :   Construct error return value for attribute read and write callbacks.

        Parameters:
        :   - **\_att\_err** – ATT error code

        Returns:
        :   Appropriate error code for the attribute callbacks.

    BT\_GATT\_CHRC\_BROADCAST
    :   Characteristic Properties Bit field values.

        Characteristic broadcast property.

        If set, permits broadcasts of the Characteristic Value using Server Characteristic Configuration Descriptor.

    BT\_GATT\_CHRC\_READ
    :   Characteristic read property.

        If set, permits reads of the Characteristic Value.

    BT\_GATT\_CHRC\_WRITE\_WITHOUT\_RESP
    :   Characteristic write without response property.

        If set, permits write of the Characteristic Value without response.

    BT\_GATT\_CHRC\_WRITE
    :   Characteristic write with response property.

        If set, permits write of the Characteristic Value with response.

    BT\_GATT\_CHRC\_NOTIFY
    :   Characteristic notify property.

        If set, permits notifications of a Characteristic Value without acknowledgment.

    BT\_GATT\_CHRC\_INDICATE
    :   Characteristic indicate property.

        If set, permits indications of a Characteristic Value with acknowledgment.

    BT\_GATT\_CHRC\_AUTH
    :   Characteristic Authenticated Signed Writes property.

        If set, permits signed writes to the Characteristic Value.

    BT\_GATT\_CHRC\_EXT\_PROP
    :   Characteristic Extended Properties property.

        If set, additional characteristic properties are defined in the Characteristic Extended Properties Descriptor.

    BT\_GATT\_CEP\_RELIABLE\_WRITE
    :   Characteristic Extended Properties Bit field values.

    BT\_GATT\_CEP\_WRITABLE\_AUX

    BT\_GATT\_CCC\_NOTIFY
    :   Client Characteristic Configuration Values.

        Client Characteristic Configuration Notification.

        If set, changes to Characteristic Value shall be notified.

    BT\_GATT\_CCC\_INDICATE
    :   Client Characteristic Configuration Indication.

        If set, changes to Characteristic Value shall be indicated.

    BT\_GATT\_SCC\_BROADCAST
    :   Server Characteristic Configuration Values.

        Server Characteristic Configuration Broadcast

        If set, the characteristic value shall be broadcast in the advertising data when the server is advertising.

    Typedefs

    typedef ssize\_t (\*bt\_gatt\_attr\_read\_func\_t)(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, void \*buf, uint16\_t len, uint16\_t offset)
    :   Attribute read callback.

        The callback can also be used locally to read the contents of the attribute in which case no connection will be set.

        Param conn:
        :   The connection that is requesting to read

        Param attr:
        :   The attribute that’s being read

        Param buf:
        :   Buffer to place the read result in

        Param len:
        :   Length of data to read

        Param offset:
        :   Offset to start reading from

        Return:
        :   Number of bytes read, or in case of an error `[BT_GATT_ERR()](#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7)` with a specific `BT_ATT_ERR_*` error code.

    typedef ssize\_t (\*bt\_gatt\_attr\_write\_func\_t)(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, const void \*buf, uint16\_t len, uint16\_t offset, uint8\_t flags)
    :   Attribute write callback.

        Param conn:
        :   The connection that is requesting to write

        Param attr:
        :   The attribute that’s being written

        Param buf:
        :   Buffer with the data to write

        Param len:
        :   Number of bytes in the buffer

        Param offset:
        :   Offset to start writing from

        Param flags:
        :   Flags (`BT_GATT_WRITE_FLAG_*`)

        Return:
        :   Number of bytes written, or in case of an error `[BT_GATT_ERR()](#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7)` with a specific `BT_ATT_ERR_*` error code.

    Enums

    enum bt\_gatt\_perm
    :   GATT attribute permission bit field values.

        *Values:*

        enumerator BT\_GATT\_PERM\_NONE = 0
        :   No operations supported, e.g.

            for notify-only

        enumerator BT\_GATT\_PERM\_READ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Attribute read permission.

        enumerator BT\_GATT\_PERM\_WRITE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Attribute write permission.

        enumerator BT\_GATT\_PERM\_READ\_ENCRYPT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Attribute read permission with encryption.

            If set, requires encryption for read access.

        enumerator BT\_GATT\_PERM\_WRITE\_ENCRYPT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Attribute write permission with encryption.

            If set, requires encryption for write access.

        enumerator BT\_GATT\_PERM\_READ\_AUTHEN = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Attribute read permission with authentication.

            If set, requires encryption using authenticated link-key for read access.

        enumerator BT\_GATT\_PERM\_WRITE\_AUTHEN = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   Attribute write permission with authentication.

            If set, requires encryption using authenticated link-key for write access.

        enumerator BT\_GATT\_PERM\_PREPARE\_WRITE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(6)
        :   Attribute prepare write permission.

            If set, allows prepare writes with use of `[BT_GATT_WRITE_FLAG_PREPARE](#group__bt__gatt_1gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383)` passed to write callback.

        enumerator BT\_GATT\_PERM\_READ\_LESC = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(7)
        :   Attribute read permission with LE Secure Connection encryption.

            If set, requires that LE Secure Connections is used for read access.

        enumerator BT\_GATT\_PERM\_WRITE\_LESC = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(8)
        :   Attribute write permission with LE Secure Connection encryption.

            If set, requires that LE Secure Connections is used for write access.

    enum [anonymous]
    :   GATT attribute write flags.

        *Values:*

        enumerator BT\_GATT\_WRITE\_FLAG\_PREPARE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Attribute prepare write flag.

            If set, write callback should only check if the device is authorized but no data shall be written.

        enumerator BT\_GATT\_WRITE\_FLAG\_CMD = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Attribute write command flag.

            If set, indicates that write operation is a command (Write without response) which doesn’t generate any response.

        enumerator BT\_GATT\_WRITE\_FLAG\_EXECUTE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Attribute write execute flag.

            If set, indicates that write operation is a execute, which indicates the end of a long write, and will come after 1 or more [BT\_GATT\_WRITE\_FLAG\_PREPARE](#group__bt__gatt_1gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383).

    struct bt\_gatt\_attr
    :   *#include <gatt.h>*

        GATT Attribute structure.

        Public Members

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   Attribute UUID.

        [bt\_gatt\_attr\_read\_func\_t](#c.bt_gatt_attr_read_func_t) read
        :   Attribute read callback.

        [bt\_gatt\_attr\_write\_func\_t](#c.bt_gatt_attr_write_func_t) write
        :   Attribute write callback.

        void \*user\_data
        :   Attribute user data.

        uint16\_t handle
        :   Attribute handle.

        uint16\_t perm
        :   Attribute permissions.

            Will be 0 if returned from `[bt_gatt_discover()](#group__bt__gatt__client_1gac06a945e5f7939b6716bc4f2cea781bd)`.

    struct bt\_gatt\_service\_static
    :   *#include <gatt.h>*

        GATT Service structure.

        Public Members

        const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attrs
        :   Service Attributes.

        size\_t attr\_count
        :   Service Attribute count.

    struct bt\_gatt\_service
    :   *#include <gatt.h>*

        GATT Service structure.

        Public Members

        struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attrs
        :   Service Attributes.

        size\_t attr\_count
        :   Service Attribute count.

    struct bt\_gatt\_service\_val
    :   *#include <gatt.h>*

        Service Attribute Value.

        Public Members

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   Service UUID.

        uint16\_t end\_handle
        :   Service end handle.

    struct bt\_gatt\_include
    :   *#include <gatt.h>*

        Include Attribute Value.

        Public Members

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   Service UUID.

        uint16\_t start\_handle
        :   Service start handle.

        uint16\_t end\_handle
        :   Service end handle.

    struct bt\_gatt\_cb
    :   *#include <gatt.h>*

        GATT callback structure.

        Public Members

        void (\*att\_mtu\_updated)(struct bt\_conn \*conn, uint16\_t tx, uint16\_t rx)
        :   The maximum ATT MTU on a connection has changed.

            This callback notifies the application that the maximum TX or RX ATT MTU has increased.

            Param conn:
            :   Connection object.

            Param tx:
            :   Updated TX ATT MTU.

            Param rx:
            :   Updated RX ATT MTU.

    struct bt\_gatt\_authorization\_cb
    :   *#include <gatt.h>*

        GATT authorization callback structure.

        Public Members

        bool (\*read\_authorize)(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr)
        :   Authorize the GATT read operation.

            This callback allows the application to authorize the GATT read operation for the attribute that is being read.

            Param conn:
            :   Connection object.

            Param attr:
            :   The attribute that is being read.

            Retval true:
            :   Authorize the operation and allow it to execute.

            Retval false:
            :   Reject the operation and prevent it from executing.

        bool (\*write\_authorize)(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr)
        :   Authorize the GATT write operation.

            This callback allows the application to authorize the GATT write operation for the attribute that is being written.

            Param conn:
            :   Connection object.

            Param attr:
            :   The attribute that is being written.

            Retval true:
            :   Authorize the operation and allow it to execute.

            Retval false:
            :   Reject the operation and prevent it from executing.

    struct bt\_gatt\_chrc
    :   *#include <gatt.h>*

        Characteristic Attribute Value.

        Public Members

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   Characteristic UUID.

        uint16\_t value\_handle
        :   Characteristic Value handle.

        uint8\_t properties
        :   Characteristic properties.

    struct bt\_gatt\_cep
    :   *#include <gatt.h>*

        Characteristic Extended Properties Attribute Value.

        Public Members

        uint16\_t properties
        :   Characteristic Extended properties.

    struct bt\_gatt\_ccc
    :   *#include <gatt.h>*

        Client Characteristic Configuration Attribute Value.

        Public Members

        uint16\_t flags
        :   Client Characteristic Configuration flags.

    struct bt\_gatt\_scc
    :   *#include <gatt.h>*

        Server Characteristic Configuration Attribute Value.

        Public Members

        uint16\_t flags
        :   Server Characteristic Configuration flags.

    struct bt\_gatt\_cpf
    :   *#include <gatt.h>*

        GATT Characteristic Presentation Format Attribute Value.

        Public Members

        uint8\_t format
        :   Format of the value of the characteristic.

        int8\_t exponent
        :   Exponent field to determine how the value of this characteristic is further formatted.

        uint16\_t unit
        :   Unit of the characteristic.

        uint8\_t name\_space
        :   Name space of the description.

        uint16\_t description
        :   Description of the characteristic as defined in a higher layer profile.

### GATT Server

*group* GATT Server APIs
:   Defines

    BT\_GATT\_SERVICE\_DEFINE(\_name, ...)
    :   Statically define and register a service.

        Helper macro to statically define and register a service.

        Parameters:
        :   - **\_name** – Service name.

    BT\_GATT\_SERVICE\_INSTANCE\_DEFINE(\_name, \_instances, \_instance\_num, \_attrs\_def)
    :   Statically define service structure array.

        Helper macro to statically define service structure array. Each element of the array is linked to the service attribute array which is also defined in this scope using `_attrs_def` macro.

        Parameters:
        :   - **\_name** – Name of service structure array.
            - **\_instances** – Array of instances to pass as user context to the attribute callbacks.
            - **\_instance\_num** – Number of elements in instance array.
            - **\_attrs\_def** – Macro provided by the user that defines attribute array for the service. This macro should accept single parameter which is the instance context.

    BT\_GATT\_SERVICE(\_attrs)
    :   Service Structure Declaration Macro.

        Helper macro to declare a service structure.

        Parameters:
        :   - **\_attrs** – Service attributes.

    BT\_GATT\_PRIMARY\_SERVICE(\_service)
    :   Primary Service Declaration Macro.

        Helper macro to declare a primary service attribute.

        Parameters:
        :   - **\_service** – Service attribute value.

    BT\_GATT\_SECONDARY\_SERVICE(\_service)
    :   Secondary Service Declaration Macro.

        Helper macro to declare a secondary service attribute.

        Note

        A secondary service is only intended to be included from a primary service or another secondary service or other higher layer specification.

        Parameters:
        :   - **\_service** – Service attribute value.

    BT\_GATT\_INCLUDE\_SERVICE(\_service\_incl)
    :   Include Service Declaration Macro.

        Helper macro to declare database internal include service attribute.

        Parameters:
        :   - **\_service\_incl** – the first service attribute of service to include

    BT\_GATT\_CHRC\_INIT(\_uuid, \_handle, \_props)

    BT\_GATT\_CHARACTERISTIC(\_uuid, \_props, \_perm, \_read, \_write, \_user\_data)
    :   Characteristic and Value Declaration Macro.

        Helper macro to declare a characteristic attribute along with its attribute value.

        Parameters:
        :   - **\_uuid** – Characteristic attribute uuid.
            - **\_props** – Characteristic attribute properties, a bitmap of `BT_GATT_CHRC_*` macros.
            - **\_perm** – Characteristic Attribute access permissions, a bitmap of [bt\_gatt\_perm](#group__bt__gatt_1ga96e57500d2340a45badb23701cc43833) values.
            - **\_read** – Characteristic Attribute read callback ([bt\_gatt\_attr\_read\_func\_t](#group__bt__gatt_1ga57e36bf94652531964fd4237c203fe7b)).
            - **\_write** – Characteristic Attribute write callback ([bt\_gatt\_attr\_write\_func\_t](#group__bt__gatt_1ga3fd8527a0f3e8f3699dc0d3b0339eba1)).
            - **\_user\_data** – Characteristic Attribute user data.

    BT\_GATT\_CCC\_MAX

    BT\_GATT\_CCC\_INITIALIZER(\_changed, \_write, \_match)
    :   Initialize Client Characteristic Configuration Declaration Macro.

        Helper macro to initialize a Managed CCC attribute value.

        Parameters:
        :   - **\_changed** – Configuration changed callback.
            - **\_write** – Configuration write callback.
            - **\_match** – Configuration match callback.

    BT\_GATT\_CCC\_MANAGED(\_ccc, \_perm)
    :   Managed Client Characteristic Configuration Declaration Macro.

        Helper macro to declare a Managed CCC attribute.

        Parameters:
        :   - **\_ccc** – CCC attribute user data, shall point to a \_bt\_gatt\_ccc.
            - **\_perm** – CCC access permissions, a bitmap of [bt\_gatt\_perm](#group__bt__gatt_1ga96e57500d2340a45badb23701cc43833) values.

    BT\_GATT\_CCC(\_changed, \_perm)
    :   Client Characteristic Configuration Declaration Macro.

        Helper macro to declare a CCC attribute.

        Parameters:
        :   - **\_changed** – Configuration changed callback.
            - **\_perm** – CCC access permissions, a bitmap of [bt\_gatt\_perm](#group__bt__gatt_1ga96e57500d2340a45badb23701cc43833) values.

    BT\_GATT\_CEP(\_value)
    :   Characteristic Extended Properties Declaration Macro.

        Helper macro to declare a CEP attribute.

        Parameters:
        :   - **\_value** – Pointer to a struct [bt\_gatt\_cep](#structbt__gatt__cep).

    BT\_GATT\_CUD(\_value, \_perm)
    :   Characteristic User Format Descriptor Declaration Macro.

        Helper macro to declare a CUD attribute.

        Parameters:
        :   - **\_value** – User description NULL-terminated C string.
            - **\_perm** – Descriptor attribute access permissions, a bitmap of [bt\_gatt\_perm](#group__bt__gatt_1ga96e57500d2340a45badb23701cc43833) values.

    BT\_GATT\_CPF(\_value)
    :   Characteristic Presentation Format Descriptor Declaration Macro.

        Helper macro to declare a CPF attribute.

        Parameters:
        :   - **\_value** – Pointer to a struct [bt\_gatt\_cpf](#structbt__gatt__cpf).

    BT\_GATT\_DESCRIPTOR(\_uuid, \_perm, \_read, \_write, \_user\_data)
    :   Descriptor Declaration Macro.

        Helper macro to declare a descriptor attribute.

        Parameters:
        :   - **\_uuid** – Descriptor attribute uuid.
            - **\_perm** – Descriptor attribute access permissions, a bitmap of [bt\_gatt\_perm](#group__bt__gatt_1ga96e57500d2340a45badb23701cc43833) values.
            - **\_read** – Descriptor attribute read callback ([bt\_gatt\_attr\_read\_func\_t](#group__bt__gatt_1ga57e36bf94652531964fd4237c203fe7b)).
            - **\_write** – Descriptor attribute write callback ([bt\_gatt\_attr\_write\_func\_t](#group__bt__gatt_1ga3fd8527a0f3e8f3699dc0d3b0339eba1)).
            - **\_user\_data** – Descriptor attribute user data.

    BT\_GATT\_ATTRIBUTE(\_uuid, \_perm, \_read, \_write, \_user\_data)
    :   Attribute Declaration Macro.

        Helper macro to declare an attribute.

        Parameters:
        :   - **\_uuid** – Attribute uuid.
            - **\_perm** – Attribute access permissions, a bitmap of [bt\_gatt\_perm](#group__bt__gatt_1ga96e57500d2340a45badb23701cc43833) values.
            - **\_read** – Attribute read callback ([bt\_gatt\_attr\_read\_func\_t](#group__bt__gatt_1ga57e36bf94652531964fd4237c203fe7b)).
            - **\_write** – Attribute write callback ([bt\_gatt\_attr\_write\_func\_t](#group__bt__gatt_1ga3fd8527a0f3e8f3699dc0d3b0339eba1)).
            - **\_user\_data** – Attribute user data.

    Typedefs

    typedef uint8\_t (\*bt\_gatt\_attr\_func\_t)(const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, uint16\_t handle, void \*user\_data)
    :   Attribute iterator callback.

        Param attr:
        :   Attribute found.

        Param handle:
        :   Attribute handle found.

        Param user\_data:
        :   Data given.

        Return:
        :   `[BT_GATT_ITER_CONTINUE](#group__bt__gatt__server_1ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5)` if should continue to the next attribute.

        Return:
        :   `[BT_GATT_ITER_STOP](#group__bt__gatt__server_1ggab94ce0108483b70392b31a621aa0712aaa3f2a25e27c7065a2c7bb2a9ff09542e)` to stop.

    typedef void (\*bt\_gatt\_complete\_func\_t)(struct bt\_conn \*conn, void \*user\_data)
    :   Notification complete result callback.

        Param conn:
        :   Connection object.

        Param user\_data:
        :   Data passed in by the user.

    typedef void (\*bt\_gatt\_indicate\_func\_t)(struct bt\_conn \*conn, struct [bt\_gatt\_indicate\_params](#c.bt_gatt_indicate_params) \*params, uint8\_t err)
    :   Indication complete result callback.

        Param conn:
        :   Connection object.

        Param params:
        :   Indication params object.

        Param err:
        :   ATT error code

    typedef void (\*bt\_gatt\_indicate\_params\_destroy\_t)(struct [bt\_gatt\_indicate\_params](#c.bt_gatt_indicate_params) \*params)

    Enums

    enum [anonymous]
    :   *Values:*

        enumerator BT\_GATT\_ITER\_STOP = 0

        enumerator BT\_GATT\_ITER\_CONTINUE

    Functions

    static inline const char \*bt\_gatt\_err\_to\_str(int gatt\_err)
    :   Converts a GATT error to string.

        The GATT errors are created with [BT\_GATT\_ERR](#group__bt__gatt_1gaff31756c1bf8ee755e65b1e0fb689bb7).

        The error codes are described in the Bluetooth Core specification, Vol 3, Part F, Section 3.4.1.1.

        The ATT and GATT documentation found in Vol 4, Part F and Part G describe when the different error codes are used.

        See also the defined BT\_ATT\_ERR\_\* macros.

        Returns:
        :   The string representation of the GATT error code. If  [`CONFIG_BT_ATT_ERR_TO_STR`](../../../kconfig.md#CONFIG_BT_ATT_ERR_TO_STR "CONFIG_BT_ATT_ERR_TO_STR") is not enabled, this just returns the empty string.

    void bt\_gatt\_cb\_register(struct [bt\_gatt\_cb](#c.bt_gatt_cb) \*cb)
    :   Register GATT callbacks.

        Register callbacks to monitor the state of GATT. The callback struct must remain valid for the remainder of the program.

        Parameters:
        :   - **cb** – Callback struct.

    int bt\_gatt\_authorization\_cb\_register(const struct [bt\_gatt\_authorization\_cb](#c.bt_gatt_authorization_cb) \*cb)
    :   Register GATT authorization callbacks.

        Register callbacks to perform application-specific authorization of GATT operations on all registered GATT attributes. The callback structure must remain valid throughout the entire duration of the Bluetooth subsys activity.

        The  [`CONFIG_BT_GATT_AUTHORIZATION_CUSTOM`](../../../kconfig.md#CONFIG_BT_GATT_AUTHORIZATION_CUSTOM "CONFIG_BT_GATT_AUTHORIZATION_CUSTOM") Kconfig must be enabled to make this API functional.

        This API allows the user to register only one callback structure concurrently. Passing NULL unregisters the previous set of callbacks and makes it possible to register a new one.

        Parameters:
        :   - **cb** – Callback struct.

        Returns:
        :   Zero on success or negative error code otherwise

    int bt\_gatt\_service\_register(struct [bt\_gatt\_service](#c.bt_gatt_service) \*svc)
    :   Register GATT service.

        Register GATT service. Applications can make use of macros such as `[BT_GATT_PRIMARY_SERVICE](#group__bt__gatt__server_1gaacada0ff1029af959b6fcd6703d4a0bf)`, `[BT_GATT_CHARACTERISTIC](#group__bt__gatt__server_1ga9e739546dbd906d3b3c4f1ed5ad9f41e)`, `[BT_GATT_DESCRIPTOR](#group__bt__gatt__server_1ga83207fc083454327004f7d3c3e5b3840)`, etc.

        When using  [`CONFIG_BT_SETTINGS`](../../../kconfig.md#CONFIG_BT_SETTINGS "CONFIG_BT_SETTINGS") then all services that should have bond configuration loaded, i.e. CCC values, must be registered before calling [settings\_load](../../../services/settings/index.md#group__settings_1ga89c6d618df81f197cc5c1a2018b00648).

        When using  [`CONFIG_BT_GATT_CACHING`](../../../kconfig.md#CONFIG_BT_GATT_CACHING "CONFIG_BT_GATT_CACHING") and  [`CONFIG_BT_SETTINGS`](../../../kconfig.md#CONFIG_BT_SETTINGS "CONFIG_BT_SETTINGS") then all services that should be included in the GATT Database Hash calculation should be added before calling [settings\_load](../../../services/settings/index.md#group__settings_1ga89c6d618df81f197cc5c1a2018b00648). All services registered after settings\_load will trigger a new database hash calculation and a new hash stored.

        There are two situations where this function can be called: either before `bt_init()` has been called, or after `[settings_load()](../../../services/settings/index.md#group__settings_1ga89c6d618df81f197cc5c1a2018b00648)` has been called. Registering a service in the middle is not supported and will return an error.

        Parameters:
        :   - **svc** – Service containing the available attributes

        Returns:
        :   0 in case of success or negative value in case of error.

        Returns:
        :   -EAGAIN if `bt_init()` has been called but `[settings_load()](../../../services/settings/index.md#group__settings_1ga89c6d618df81f197cc5c1a2018b00648)` hasn’t yet.

    int bt\_gatt\_service\_unregister(struct [bt\_gatt\_service](#c.bt_gatt_service) \*svc)
    :   Unregister GATT service.

        Parameters:
        :   - **svc** – Service to be unregistered.

        Returns:
        :   0 in case of success or negative value in case of error.

    bool bt\_gatt\_service\_is\_registered(const struct [bt\_gatt\_service](#c.bt_gatt_service) \*svc)
    :   Check if GATT service is registered.

        Parameters:
        :   - **svc** – Service to be checked.

        Returns:
        :   true if registered or false if not register.

    void bt\_gatt\_foreach\_attr\_type(uint16\_t start\_handle, uint16\_t end\_handle, const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid, const void \*attr\_data, uint16\_t num\_matches, [bt\_gatt\_attr\_func\_t](#c.bt_gatt_attr_func_t) func, void \*user\_data)
    :   Attribute iterator by type.

        Iterate attributes in the given range matching given UUID and/or data.

        Parameters:
        :   - **start\_handle** – Start handle.
            - **end\_handle** – End handle.
            - **uuid** – UUID to match, passing NULL skips UUID matching.
            - **attr\_data** – Attribute data to match, passing NULL skips data matching.
            - **num\_matches** – Number matches, passing 0 makes it unlimited.
            - **func** – Callback function.
            - **user\_data** – Data to pass to the callback.

    static inline void bt\_gatt\_foreach\_attr(uint16\_t start\_handle, uint16\_t end\_handle, [bt\_gatt\_attr\_func\_t](#c.bt_gatt_attr_func_t) func, void \*user\_data)
    :   Attribute iterator.

        Iterate attributes in the given range.

        Parameters:
        :   - **start\_handle** – Start handle.
            - **end\_handle** – End handle.
            - **func** – Callback function.
            - **user\_data** – Data to pass to the callback.

    struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*bt\_gatt\_attr\_next(const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr)
    :   Iterate to the next attribute.

        Iterate to the next attribute following a given attribute.

        Parameters:
        :   - **attr** – Current Attribute.

        Returns:
        :   The next attribute or NULL if it cannot be found.

    struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*bt\_gatt\_find\_by\_uuid(const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, uint16\_t attr\_count, const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid)
    :   Find Attribute by UUID.

        Find the attribute with the matching UUID. To limit the search to a service set the attr to the service attributes and the `attr_count` to the service attribute count .

        Parameters:
        :   - **attr** – Pointer to an attribute that serves as the starting point for the search of a match for the UUID. Passing NULL will search the entire range.
            - **attr\_count** – The number of attributes from the starting point to search for a match for the UUID. Set to 0 to search until the end.
            - **uuid** – UUID to match.

    uint16\_t bt\_gatt\_attr\_get\_handle(const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr)
    :   Get Attribute handle.

        Parameters:
        :   - **attr** – Attribute object.

        Returns:
        :   Handle of the corresponding attribute or zero if the attribute could not be found.

    uint16\_t bt\_gatt\_attr\_value\_handle(const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr)
    :   Get the handle of the characteristic value descriptor.

        Note

        The `user_data` of the attribute must of type [bt\_gatt\_chrc](#structbt__gatt__chrc).

        Parameters:
        :   - **attr** – A Characteristic Attribute.

        Returns:
        :   the handle of the corresponding Characteristic Value. The value will be zero (the invalid handle) if `attr` was not a characteristic attribute.

    ssize\_t bt\_gatt\_attr\_read(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, void \*buf, uint16\_t buf\_len, uint16\_t offset, const void \*value, uint16\_t value\_len)
    :   Generic Read Attribute value helper.

        Read attribute value from local database storing the result into buffer.

        Parameters:
        :   - **conn** – Connection object.
            - **attr** – Attribute to read.
            - **buf** – Buffer to store the value.
            - **buf\_len** – Buffer length.
            - **offset** – Start offset.
            - **value** – Attribute value.
            - **value\_len** – Length of the attribute value.

        Returns:
        :   number of bytes read in case of success or negative values in case of error.

    ssize\_t bt\_gatt\_attr\_read\_service(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, void \*buf, uint16\_t len, uint16\_t offset)
    :   Read Service Attribute helper.

        Read service attribute value from local database storing the result into buffer after encoding it.

        Note

        Only use this with attributes which `user_data` is a `[bt_uuid](uuid.md#structbt__uuid)`.

        Parameters:
        :   - **conn** – Connection object.
            - **attr** – Attribute to read.
            - **buf** – Buffer to store the value read.
            - **len** – Buffer length.
            - **offset** – Start offset.

        Returns:
        :   number of bytes read in case of success or negative values in case of error.

    ssize\_t bt\_gatt\_attr\_read\_included(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, void \*buf, uint16\_t len, uint16\_t offset)
    :   Read Include Attribute helper.

        Read include service attribute value from local database storing the result into buffer after encoding it.

        Note

        Only use this with attributes which user\_data is a `[bt_gatt_include](#structbt__gatt__include)`.

        Parameters:
        :   - **conn** – Connection object.
            - **attr** – Attribute to read.
            - **buf** – Buffer to store the value read.
            - **len** – Buffer length.
            - **offset** – Start offset.

        Returns:
        :   number of bytes read in case of success or negative values in case of error.

    ssize\_t bt\_gatt\_attr\_read\_chrc(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, void \*buf, uint16\_t len, uint16\_t offset)
    :   Read Characteristic Attribute helper.

        Read characteristic attribute value from local database storing the result into buffer after encoding it.

        Note

        Only use this with attributes which `user_data` is a `[bt_gatt_chrc](#structbt__gatt__chrc)`.

        Parameters:
        :   - **conn** – Connection object.
            - **attr** – Attribute to read.
            - **buf** – Buffer to store the value read.
            - **len** – Buffer length.
            - **offset** – Start offset.

        Returns:
        :   number of bytes read in case of success or negative values in case of error.

    ssize\_t bt\_gatt\_attr\_read\_ccc(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, void \*buf, uint16\_t len, uint16\_t offset)
    :   Read Client Characteristic Configuration Attribute helper.

        Read CCC attribute value from local database storing the result into buffer after encoding it.

        Note

        Only use this with attributes which user\_data is a \_bt\_gatt\_ccc.

        Parameters:
        :   - **conn** – Connection object.
            - **attr** – Attribute to read.
            - **buf** – Buffer to store the value read.
            - **len** – Buffer length.
            - **offset** – Start offset.

        Returns:
        :   number of bytes read in case of success or negative values in case of error.

    ssize\_t bt\_gatt\_attr\_write\_ccc(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, const void \*buf, uint16\_t len, uint16\_t offset, uint8\_t flags)
    :   Write Client Characteristic Configuration Attribute helper.

        Write value in the buffer into CCC attribute.

        Note

        Only use this with attributes which user\_data is a \_bt\_gatt\_ccc.

        Parameters:
        :   - **conn** – Connection object.
            - **attr** – Attribute to read.
            - **buf** – Buffer to store the value read.
            - **len** – Buffer length.
            - **offset** – Start offset.
            - **flags** – Write flags.

        Returns:
        :   number of bytes written in case of success or negative values in case of error.

    ssize\_t bt\_gatt\_attr\_read\_cep(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, void \*buf, uint16\_t len, uint16\_t offset)
    :   Read Characteristic Extended Properties Attribute helper.

        Read CEP attribute value from local database storing the result into buffer after encoding it.

        Note

        Only use this with attributes which user\_data is a [bt\_gatt\_cep](#structbt__gatt__cep).

        Parameters:
        :   - **conn** – Connection object
            - **attr** – Attribute to read
            - **buf** – Buffer to store the value read
            - **len** – Buffer length
            - **offset** – Start offset

        Returns:
        :   number of bytes read in case of success or negative values in case of error.

    ssize\_t bt\_gatt\_attr\_read\_cud(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, void \*buf, uint16\_t len, uint16\_t offset)
    :   Read Characteristic User Description Descriptor Attribute helper.

        Read CUD attribute value from local database storing the result into buffer after encoding it.

        Note

        Only use this with attributes which user\_data is a NULL-terminated C string.

        Parameters:
        :   - **conn** – Connection object
            - **attr** – Attribute to read
            - **buf** – Buffer to store the value read
            - **len** – Buffer length
            - **offset** – Start offset

        Returns:
        :   number of bytes read in case of success or negative values in case of error.

    ssize\_t bt\_gatt\_attr\_read\_cpf(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, void \*buf, uint16\_t len, uint16\_t offset)
    :   Read Characteristic Presentation format Descriptor Attribute helper.

        Read CPF attribute value from local database storing the result into buffer after encoding it.

        Note

        Only use this with attributes which user\_data is a bt\_gatt\_pf.

        Parameters:
        :   - **conn** – Connection object
            - **attr** – Attribute to read
            - **buf** – Buffer to store the value read
            - **len** – Buffer length
            - **offset** – Start offset

        Returns:
        :   number of bytes read in case of success or negative values in case of error.

    int bt\_gatt\_notify\_cb(struct bt\_conn \*conn, struct [bt\_gatt\_notify\_params](#c.bt_gatt_notify_params) \*params)
    :   Notify attribute value change.

        This function works in the same way as [bt\_gatt\_notify](#group__bt__gatt__server_1ga74ee552864c563aa5bc939f37395c14a). With the addition that after sending the notification the callback function will be called.

        The callback is run from System Workqueue context. When called from the System Workqueue context this API will not wait for resources for the callback but instead return an error. The number of pending callbacks can be increased with the  [`CONFIG_BT_CONN_TX_MAX`](../../../kconfig.md#CONFIG_BT_CONN_TX_MAX "CONFIG_BT_CONN_TX_MAX") option.

        Alternatively it is possible to notify by UUID by setting it on the parameters, when using this method the attribute if provided is used as the start range when looking up for possible matches.

        Parameters:
        :   - **conn** – Connection object.
            - **params** – Notification parameters.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_gatt\_notify\_multiple(struct bt\_conn \*conn, uint16\_t num\_params, struct [bt\_gatt\_notify\_params](#c.bt_gatt_notify_params) params[])
    :   Send multiple notifications in a single PDU.

        The GATT Server will send a single ATT\_MULTIPLE\_HANDLE\_VALUE\_NTF PDU containing all the notifications passed to this API.

        All `params` must have the same `func` and `user_data` (due to implementation limitation). But `func(user_data)` will be invoked for each parameter.

        As this API may block to wait for Bluetooth Host resources, it is not recommended to call it from a cooperative thread or a Bluetooth callback.

        The peer’s GATT Client must write to this device’s Client Supported Features attribute and set the bit for Multiple Handle Value Notifications before this API can be used.

        Only use this API to force the use of the ATT\_MULTIPLE\_HANDLE\_VALUE\_NTF PDU. For standard applications, `[bt_gatt_notify_cb](#group__bt__gatt__server_1ga55e3ef7cb43b8acb0a27643c78390146)` is preferred, as it will use this PDU if supported and automatically fallback to ATT\_HANDLE\_VALUE\_NTF when not supported by the peer.

        This API has an additional limitation: it only accepts valid attribute references and not UUIDs like `[bt_gatt_notify](#group__bt__gatt__server_1ga74ee552864c563aa5bc939f37395c14a)` and `[bt_gatt_notify_cb](#group__bt__gatt__server_1ga55e3ef7cb43b8acb0a27643c78390146)`.

        Parameters:
        :   - **conn** – Target client. Notifying all connected clients by passing `NULL` is not yet supported, please use `[bt_gatt_notify](#group__bt__gatt__server_1ga74ee552864c563aa5bc939f37395c14a)` instead.
            - **num\_params** – Element count of `params` array. Has to be greater than 1.
            - **params** – Array of notification parameters. It is okay to free this after calling this function.

        Return values:
        :   - **0** – Success. The PDU is queued for sending.
            - **-EINVAL** –

              - One of the attribute handles is invalid.
              - Only one parameter was passed. This API expects 2 or more.
              - Not all `func` were equal or not all `user_data` were equal.
              - One of the characteristics is not notifiable.
              - An UUID was passed in one of the parameters.
            - **-ERANGE** –

              - The notifications cannot all fit in a single ATT\_MULTIPLE\_HANDLE\_VALUE\_NTF.
              - They exceed the MTU of all open ATT bearers.
            - **-EPERM** – The connection has a lower security level than required by one of the attributes.
            - **-EOPNOTSUPP** – The peer hasn’t yet communicated that it supports this PDU type.

    static inline int bt\_gatt\_notify(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, const void \*data, uint16\_t len)
    :   Notify attribute value change.

        Send notification of attribute value change, if connection is NULL notify all peer that have notification enabled via CCC otherwise do a direct notification only the given connection.

        The attribute object on the parameters can be the so called Characteristic Declaration, which is usually declared with BT\_GATT\_CHARACTERISTIC followed by BT\_GATT\_CCC, or the Characteristic Value Declaration which is automatically created after the Characteristic Declaration when using BT\_GATT\_CHARACTERISTIC.

        Parameters:
        :   - **conn** – Connection object.
            - **attr** – Characteristic or Characteristic Value attribute.
            - **data** – Pointer to Attribute data.
            - **len** – Attribute value length.

        Returns:
        :   0 in case of success or negative value in case of error.

    static inline int bt\_gatt\_notify\_uuid(struct bt\_conn \*conn, const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, const void \*data, uint16\_t len)
    :   Notify attribute value change by UUID.

        Send notification of attribute value change, if connection is NULL notify all peer that have notification enabled via CCC otherwise do a direct notification only on the given connection.

        The attribute object is the starting point for the search of the UUID.

        Parameters:
        :   - **conn** – Connection object.
            - **uuid** – The UUID. If the server contains multiple services with the same UUID, then the first occurrence, starting from the attr given, is used.
            - **attr** – Pointer to an attribute that serves as the starting point for the search of a match for the UUID.
            - **data** – Pointer to Attribute data.
            - **len** – Attribute value length.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_gatt\_indicate(struct bt\_conn \*conn, struct [bt\_gatt\_indicate\_params](#c.bt_gatt_indicate_params) \*params)
    :   Indicate attribute value change.

        Send an indication of attribute value change. if connection is NULL indicate all peer that have notification enabled via CCC otherwise do a direct indication only the given connection.

        The attribute object on the parameters can be the so called Characteristic Declaration, which is usually declared with BT\_GATT\_CHARACTERISTIC followed by BT\_GATT\_CCC, or the Characteristic Value Declaration which is automatically created after the Characteristic Declaration when using BT\_GATT\_CHARACTERISTIC.

        Alternatively it is possible to indicate by UUID by setting it on the parameters, when using this method the attribute if provided is used as the start range when looking up for possible matches.

        Note

        This procedure is asynchronous therefore the parameters need to remains valid while it is active. The procedure is active until the destroy callback is run.

        Parameters:
        :   - **conn** – Connection object.
            - **params** – Indicate parameters.

        Returns:
        :   0 in case of success or negative value in case of error.

    bool bt\_gatt\_is\_subscribed(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, uint16\_t ccc\_type)
    :   Check if connection have subscribed to attribute.

        Check if connection has subscribed to attribute value change.

        The attribute object can be the so called Characteristic Declaration, which is usually declared with BT\_GATT\_CHARACTERISTIC followed by BT\_GATT\_CCC, or the Characteristic Value Declaration which is automatically created after the Characteristic Declaration when using BT\_GATT\_CHARACTERISTIC, or the Client Characteristic Configuration Descriptor (CCCD) which is created by BT\_GATT\_CCC.

        Parameters:
        :   - **conn** – Connection object.
            - **attr** – Attribute object.
            - **ccc\_type** – The subscription type, [BT\_GATT\_CCC\_NOTIFY](#group__bt__gatt_1ga240a10df32aa7a256a103ceee7211f8d) and/or [BT\_GATT\_CCC\_INDICATE](#group__bt__gatt_1ga60ff2ddcc2e3148881a2f15745ba06e8).

        Returns:
        :   true if the attribute object has been subscribed.

    uint16\_t bt\_gatt\_get\_mtu(struct bt\_conn \*conn)
    :   Get ATT MTU for a connection.

        Get negotiated ATT connection MTU, note that this does not equal the largest amount of attribute data that can be transferred within a single packet.

        Parameters:
        :   - **conn** – Connection object.

        Returns:
        :   MTU in bytes

    struct bt\_gatt\_ccc\_cfg
    :   *#include <gatt.h>*

        GATT CCC configuration entry.

        Public Members

        uint8\_t id
        :   Local identity, BT\_ID\_DEFAULT in most cases.

        [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") peer
        :   Remote peer address.

        uint16\_t value
        :   Configuration value.

    struct bt\_gatt\_notify\_params
    :   *#include <gatt.h>*

        Public Members

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   Notification Attribute UUID type.

            Optional, use to search for an attribute with matching UUID when the attribute object pointer is not known.

        const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr
        :   Notification Attribute object.

            Optional if uuid is provided, in this case it will be used as start range to search for the attribute with the given UUID.

        const void \*data
        :   Notification Value data.

        uint16\_t len
        :   Notification Value length.

        [bt\_gatt\_complete\_func\_t](#c.bt_gatt_complete_func_t) func
        :   Notification Value callback.

        void \*user\_data
        :   Notification Value callback user data.

    struct bt\_gatt\_indicate\_params
    :   *#include <gatt.h>*

        GATT Indicate Value parameters.

        Public Members

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   Indicate Attribute UUID type.

            Optional, use to search for an attribute with matching UUID when the attribute object pointer is not known.

        const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr
        :   Indicate Attribute object.

            Optional if uuid is provided, in this case it will be used as start range to search for the attribute with the given UUID.

        [bt\_gatt\_indicate\_func\_t](#c.bt_gatt_indicate_func_t) func
        :   Indicate Value callback.

        [bt\_gatt\_indicate\_params\_destroy\_t](#c.bt_gatt_indicate_params_destroy_t) destroy
        :   Indicate operation complete callback.

        const void \*data
        :   Indicate Value data.

        uint16\_t len
        :   Indicate Value length.

### GATT Client

*group* GATT Client APIs
:   Typedefs

    typedef uint8\_t (\*bt\_gatt\_discover\_func\_t)(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](#c.bt_gatt_attr) \*attr, struct [bt\_gatt\_discover\_params](#c.bt_gatt_discover_params) \*params)
    :   Discover attribute callback function.

        If discovery procedure has completed this callback will be called with attr set to NULL. This will not happen if procedure was stopped by returning BT\_GATT\_ITER\_STOP.

        The attribute object as well as its UUID and value objects are temporary and must be copied to in order to cache its information. Only the following fields of the attribute contains valid information:

        - uuid UUID representing the type of attribute.
        - handle Handle in the remote database.
        - user\_data The value of the attribute, if the discovery type maps to an ATT operation that provides this information. NULL otherwise. See below.

        The effective type of `attr->user_data` is determined by `params`. Note that the fields `params->type` and `params->uuid` are left unchanged by the discovery procedure.

        | `params->type` | `params->uuid` | Type of `attr->user_data` |
        | --- | --- | --- |
        | [BT\_GATT\_DISCOVER\_PRIMARY](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403ada9ac33aa77f6043da8133dcf269478f) | any | [bt\_gatt\_service\_val](#structbt__gatt__service__val) |
        | [BT\_GATT\_DISCOVER\_SECONDARY](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403a21be62548b816c7960a54dd6e3b37a97) | any | [bt\_gatt\_service\_val](#structbt__gatt__service__val) |
        | [BT\_GATT\_DISCOVER\_INCLUDE](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403a80afff1c83bb5ebb5603af699f2c26da) | any | [bt\_gatt\_include](#structbt__gatt__include) |
        | [BT\_GATT\_DISCOVER\_CHARACTERISTIC](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403a71355dfe0bf30c88f9fe2f7da1ba10ae) | any | [bt\_gatt\_chrc](#structbt__gatt__chrc) |
        | [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61) | [BT\_UUID\_GATT\_CEP](uuid.md#group__bt__uuid_1ga6aa143b721d810f1536d7431a9bf7cc7) | [bt\_gatt\_cep](#structbt__gatt__cep) |
        | [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61) | [BT\_UUID\_GATT\_CCC](uuid.md#group__bt__uuid_1ga03a2d3f0ce89508b794d5c87a4303057) | [bt\_gatt\_ccc](#structbt__gatt__ccc) |
        | [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61) | [BT\_UUID\_GATT\_SCC](uuid.md#group__bt__uuid_1ga82567cdce8c4411cd3daf26711ba9685) | [bt\_gatt\_scc](#structbt__gatt__scc) |
        | [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61) | [BT\_UUID\_GATT\_CPF](uuid.md#group__bt__uuid_1ga331a61702ffe9b15bac0de3d60414022) | [bt\_gatt\_cpf](#structbt__gatt__cpf) |
        | [BT\_GATT\_DISCOVER\_DESCRIPTOR](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403a0ccb2587aa8f21361c5d73847a33ecbe) | any | NULL |
        | [BT\_GATT\_DISCOVER\_ATTRIBUTE](#group__bt__gatt__client_1ggaa7bf94a9823d44c702cc26dc8ade8403afe2167b873b848935d56f6ee7f2c444c) | any | NULL |

        Also consider if using read-by-type instead of discovery is more convenient. See [bt\_gatt\_read](#group__bt__gatt__client_1ga1a18dd726ab960a88d7f85f2a014141a) with [bt\_gatt\_read\_params::handle\_count](#structbt__gatt__read__params_1a0a36063ac0b110fbf57ef6a66f7bece8) set to `0`.

        Param conn:
        :   Connection object.

        Param attr:
        :   Attribute found, or NULL if not found.

        Param params:
        :   Discovery parameters given.

        Return:
        :   BT\_GATT\_ITER\_CONTINUE to continue discovery procedure.

        Return:
        :   BT\_GATT\_ITER\_STOP to stop discovery procedure.

    typedef uint8\_t (\*bt\_gatt\_read\_func\_t)(struct bt\_conn \*conn, uint8\_t err, struct [bt\_gatt\_read\_params](#c.bt_gatt_read_params) \*params, const void \*data, uint16\_t length)
    :   Read callback function.

        When reading using by\_uuid, `params->start_handle` is the attribute handle for this `data` item.

        Param conn:
        :   Connection object.

        Param err:
        :   ATT error code.

        Param params:
        :   Read parameters used.

        Param data:
        :   Attribute value data. NULL means read has completed.

        Param length:
        :   Attribute value length.

        Return:
        :   BT\_GATT\_ITER\_CONTINUE if should continue to the next attribute.

        Return:
        :   BT\_GATT\_ITER\_STOP to stop.

    typedef void (\*bt\_gatt\_write\_func\_t)(struct bt\_conn \*conn, uint8\_t err, struct [bt\_gatt\_write\_params](#c.bt_gatt_write_params) \*params)
    :   Write callback function.

        Param conn:
        :   Connection object.

        Param err:
        :   ATT error code.

        Param params:
        :   Write parameters used.

    typedef uint8\_t (\*bt\_gatt\_notify\_func\_t)(struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](#c.bt_gatt_subscribe_params) \*params, const void \*data, uint16\_t length)
    :   Notification callback function.

        In the case of an empty notification, the `data` pointer will be non-NULL while the `length` will be 0, which is due to the special case where a `data` NULL pointer means unsubscribed.

        Param conn:
        :   Connection object. May be NULL, indicating that the peer is being unpaired

        Param params:
        :   Subscription parameters.

        Param data:
        :   Attribute value data. If NULL then subscription was removed.

        Param length:
        :   Attribute value length.

        Return:
        :   BT\_GATT\_ITER\_CONTINUE to continue receiving value notifications. BT\_GATT\_ITER\_STOP to unsubscribe from value notifications.

    typedef void (\*bt\_gatt\_subscribe\_func\_t)(struct bt\_conn \*conn, uint8\_t err, struct [bt\_gatt\_subscribe\_params](#c.bt_gatt_subscribe_params) \*params)
    :   Subscription callback function.

        Param conn:
        :   Connection object.

        Param err:
        :   ATT error code.

        Param params:
        :   Subscription parameters used.

    Enums

    enum [anonymous]
    :   GATT Discover types.

        *Values:*

        enumerator BT\_GATT\_DISCOVER\_PRIMARY
        :   Discover Primary Services.

        enumerator BT\_GATT\_DISCOVER\_SECONDARY
        :   Discover Secondary Services.

        enumerator BT\_GATT\_DISCOVER\_INCLUDE
        :   Discover Included Services.

        enumerator BT\_GATT\_DISCOVER\_CHARACTERISTIC
        :   Discover Characteristic Values.

            Discover Characteristic Value and its properties.

        enumerator BT\_GATT\_DISCOVER\_DESCRIPTOR
        :   Discover Descriptors.

            Discover Attributes which are not services or characteristics.

            Note

            The use of this type of discover is not recommended for discovering in ranges across multiple services/characteristics as it may incur in extra round trips.

        enumerator BT\_GATT\_DISCOVER\_ATTRIBUTE
        :   Discover Attributes.

            Discover Attributes of any type.

            Note

            The use of this type of discover is not recommended for discovering in ranges across multiple services/characteristics as it may incur in more round trips.

        enumerator BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC
        :   Discover standard characteristic descriptor values.

            Discover standard characteristic descriptor values and their properties. Supported descriptors:

            - Characteristic Extended Properties
            - Client Characteristic Configuration
            - Server Characteristic Configuration
            - Characteristic Presentation Format

    enum [anonymous]
    :   Subscription flags.

        *Values:*

        enumerator BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE
        :   Persistence flag.

            If set, indicates that the subscription is not saved on the GATT server side. Therefore, upon disconnection, the subscription will be automatically removed from the client’s subscriptions list and when the client reconnects, it will have to issue a new subscription.

        enumerator BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB
        :   No resubscribe flag.

            By default when BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE is unset, the subscription will be automatically renewed when the client reconnects, as a workaround for GATT servers that do not persist subscriptions.

            This flag will disable the automatic resubscription. It is useful if the application layer knows that the GATT server remembers subscriptions from previous connections and wants to avoid renewing the subscriptions.

        enumerator BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING
        :   Write pending flag.

            If set, indicates write operation is pending waiting remote end to respond.

            Note

            Internal use only.

        enumerator BT\_GATT\_SUBSCRIBE\_FLAG\_SENT
        :   Sent flag.

            If set, indicates that a subscription request (CCC write) has already been sent in the active connection.

            Used to avoid sending subscription requests multiple times when the  [`CONFIG_BT_GATT_AUTO_RESUBSCRIBE`](../../../kconfig.md#CONFIG_BT_GATT_AUTO_RESUBSCRIBE "CONFIG_BT_GATT_AUTO_RESUBSCRIBE") quirk is enabled.

            Note

            Internal use only.

        enumerator BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS

    Functions

    int bt\_gatt\_exchange\_mtu(struct bt\_conn \*conn, struct [bt\_gatt\_exchange\_params](#c.bt_gatt_exchange_params) \*params)
    :   Exchange MTU.

        This client procedure can be used to set the MTU to the maximum possible size the buffers can hold.

        The Response comes in callback `params->func`. The callback is run from the context specified by ‘config BT\_RECV\_CONTEXT’. `params` must remain valid until start of callback.

        This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

        Note

        Shall only be used once per connection.

        Parameters:
        :   - **conn** – Connection object.
            - **params** – Exchange MTU parameters.

        Return values:
        :   - **0** – Successfully queued request. Will call `params->func` on resolution.
            - **-ENOMEM** – ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by  [`CONFIG_BT_ATT_TX_COUNT`](../../../kconfig.md#CONFIG_BT_ATT_TX_COUNT "CONFIG_BT_ATT_TX_COUNT") .
            - **-EALREADY** – The MTU exchange procedure has been already performed.

    int bt\_gatt\_discover(struct bt\_conn \*conn, struct [bt\_gatt\_discover\_params](#c.bt_gatt_discover_params) \*params)
    :   GATT Discover function.

        This procedure is used by a client to discover attributes on a server.

        Primary Service Discovery: Procedure allows to discover primary services either by Discover All Primary Services or Discover Primary Services by Service UUID. Include Service Discovery: Procedure allows to discover all Include Services within specified range. Characteristic Discovery: Procedure allows to discover all characteristics within specified handle range as well as discover characteristics with specified UUID. Descriptors Discovery: Procedure allows to discover all characteristic descriptors within specified range.

        For each attribute found the callback is called which can then decide whether to continue discovering or stop.

        The Response comes in callback `params->func`. The callback is run from the BT RX thread. `params` must remain valid until start of callback where iter `attr` is `NULL` or callback will return `[BT_GATT_ITER_STOP](#group__bt__gatt__server_1ggab94ce0108483b70392b31a621aa0712aaa3f2a25e27c7065a2c7bb2a9ff09542e)`.

        This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

        Parameters:
        :   - **conn** – Connection object.
            - **params** – Discover parameters.

        Return values:
        :   - **0** – Successfully queued request. Will call `params->func` on resolution.
            - **-ENOMEM** – ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by  [`CONFIG_BT_ATT_TX_COUNT`](../../../kconfig.md#CONFIG_BT_ATT_TX_COUNT "CONFIG_BT_ATT_TX_COUNT") .

    int bt\_gatt\_read(struct bt\_conn \*conn, struct [bt\_gatt\_read\_params](#c.bt_gatt_read_params) \*params)
    :   Read Attribute Value by handle.

        This procedure read the attribute value and return it to the callback.

        When reading attributes by UUID the callback can be called multiple times depending on how many instances of given the UUID exists with the start\_handle being updated for each instance.

        To perform a GATT Long Read procedure, start with a Characteristic Value Read (by setting `offset` `0` and `handle_count` `1`) and then return [BT\_GATT\_ITER\_CONTINUE](#group__bt__gatt__server_1ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5) from the callback. This is equivalent to calling [bt\_gatt\_read](#group__bt__gatt__client_1ga1a18dd726ab960a88d7f85f2a014141a) again, but with the correct offset to continue the read. This may be repeated until the procedure is complete, which is signaled by the callback being called with `data` set to `NULL`.

        Note that returning [BT\_GATT\_ITER\_CONTINUE](#group__bt__gatt__server_1ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5) is really starting a new ATT operation, so this can fail to allocate resources. However, all API errors are reported as if the server returned [BT\_ATT\_ERR\_UNLIKELY](att.md#group__bt__att_1ga992baa1f0d763a00f314bdcf59965bdd). There is no way to distinguish between this condition and a [BT\_ATT\_ERR\_UNLIKELY](att.md#group__bt__att_1ga992baa1f0d763a00f314bdcf59965bdd) response from the server itself.

        Note that the effect of returning [BT\_GATT\_ITER\_CONTINUE](#group__bt__gatt__server_1ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5) from the callback varies depending on the type of read operation.

        The Response comes in callback `params->func`. The callback is run from the context specified by ‘config BT\_RECV\_CONTEXT’. `params` must remain valid until start of callback.

        This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

        Parameters:
        :   - **conn** – Connection object.
            - **params** – Read parameters.

        Return values:
        :   - **0** – Successfully queued request. Will call `params->func` on resolution.
            - **-ENOMEM** – ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by  [`CONFIG_BT_ATT_TX_COUNT`](../../../kconfig.md#CONFIG_BT_ATT_TX_COUNT "CONFIG_BT_ATT_TX_COUNT") .

    int bt\_gatt\_write(struct bt\_conn \*conn, struct [bt\_gatt\_write\_params](#c.bt_gatt_write_params) \*params)
    :   Write Attribute Value by handle.

        The Response comes in callback `params->func`. The callback is run from the context specified by ‘config BT\_RECV\_CONTEXT’. `params` must remain valid until start of callback.

        This function will block while the ATT request queue is full, except when called from Bluetooth event context. When called from Bluetooth context, this function will instead instead return `-[ENOMEM](../../../develop/languages/c/minimal_libc.md#group__system__errno_1ga6a05c923dad0c1208043e9c20a58c8e5)` if it would block to avoid a deadlock.

        Parameters:
        :   - **conn** – Connection object.
            - **params** – Write parameters.

        Return values:
        :   - **0** – Successfully queued request. Will call `params->func` on resolution.
            - **-ENOMEM** – ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside Bluetooth event context to get blocking behavior. Queue size is controlled by  [`CONFIG_BT_ATT_TX_COUNT`](../../../kconfig.md#CONFIG_BT_ATT_TX_COUNT "CONFIG_BT_ATT_TX_COUNT") .

    int bt\_gatt\_write\_without\_response\_cb(struct bt\_conn \*conn, uint16\_t handle, const void \*data, uint16\_t length, bool sign, [bt\_gatt\_complete\_func\_t](#c.bt_gatt_complete_func_t) func, void \*user\_data)
    :   Write Attribute Value by handle without response with callback.

        This function works in the same way as [bt\_gatt\_write\_without\_response](#group__bt__gatt__client_1ga9fc78e32230637a6f092da2400c50fe7). With the addition that after sending the write the callback function will be called.

        The callback is run from System Workqueue context. When called from the System Workqueue context this API will not wait for resources for the callback but instead return an error. The number of pending callbacks can be increased with the  [`CONFIG_BT_CONN_TX_MAX`](../../../kconfig.md#CONFIG_BT_CONN_TX_MAX "CONFIG_BT_CONN_TX_MAX") option.

        This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

        Note

        By using a callback it also disable the internal flow control which would prevent sending multiple commands without waiting for their transmissions to complete, so if that is required the caller shall not submit more data until the callback is called.

        Parameters:
        :   - **conn** – Connection object.
            - **handle** – Attribute handle.
            - **data** – Data to be written.
            - **length** – Data length.
            - **sign** – Whether to sign data
            - **func** – Transmission complete callback.
            - **user\_data** – User data to be passed back to callback.

        Return values:
        :   - **0** – Successfully queued request.
            - **-ENOMEM** – ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by  [`CONFIG_BT_ATT_TX_COUNT`](../../../kconfig.md#CONFIG_BT_ATT_TX_COUNT "CONFIG_BT_ATT_TX_COUNT") .

    static inline int bt\_gatt\_write\_without\_response(struct bt\_conn \*conn, uint16\_t handle, const void \*data, uint16\_t length, bool sign)
    :   Write Attribute Value by handle without response.

        This procedure write the attribute value without requiring an acknowledgment that the write was successfully performed

        This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

        Parameters:
        :   - **conn** – Connection object.
            - **handle** – Attribute handle.
            - **data** – Data to be written.
            - **length** – Data length.
            - **sign** – Whether to sign data

        Return values:
        :   - **0** – Successfully queued request.
            - **-ENOMEM** – ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by  [`CONFIG_BT_ATT_TX_COUNT`](../../../kconfig.md#CONFIG_BT_ATT_TX_COUNT "CONFIG_BT_ATT_TX_COUNT") .

    int bt\_gatt\_subscribe(struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](#c.bt_gatt_subscribe_params) \*params)
    :   Subscribe Attribute Value Notification.

        This procedure subscribe to value notification using the Client Characteristic Configuration handle. If notification received subscribe value callback is called to return notified value. One may then decide whether to unsubscribe directly from this callback. Notification callback with NULL data will not be called if subscription was removed by this method.

        The Response comes in callback `params->subscribe`. The callback is run from the context specified by ‘config BT\_RECV\_CONTEXT’. The Notification callback `params->notify` is also called from the BT RX thread.

        This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

        Note

        Notifications are asynchronous therefore the `params` must remain valid while subscribed and cannot be reused for additional subscriptions whilst active.

        Parameters:
        :   - **conn** – Connection object.
            - **params** – Subscribe parameters.

        Return values:
        :   - **0** – Successfully queued request. Will call `params->write` on resolution.
            - **-ENOMEM** – ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by  [`CONFIG_BT_ATT_TX_COUNT`](../../../kconfig.md#CONFIG_BT_ATT_TX_COUNT "CONFIG_BT_ATT_TX_COUNT") .
            - **-EALREADY** – if there already exist a subscription using the `params`.
            - **-EBUSY** – if `params.ccc_handle` is 0 and  [`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](../../../kconfig.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC "CONFIG_BT_GATT_AUTO_DISCOVER_CCC") is enabled and discovery for the `params` is already in progress.

    int bt\_gatt\_resubscribe(uint8\_t id, const [bt\_addr\_le\_t](gap.md#c.bt_addr_le_t "bt_addr_le_t") \*peer, struct [bt\_gatt\_subscribe\_params](#c.bt_gatt_subscribe_params) \*params)
    :   Resubscribe Attribute Value Notification subscription.

        Resubscribe to Attribute Value Notification when already subscribed from a previous connection. The GATT server will remember subscription from previous connections when bonded, so resubscribing can be done without performing a new subscribe procedure after a power cycle.

        Note

        Notifications are asynchronous therefore the parameters need to remain valid while subscribed.

        Parameters:
        :   - **id** – Local identity (in most cases BT\_ID\_DEFAULT).
            - **peer** – Remote address.
            - **params** – Subscribe parameters.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_gatt\_unsubscribe(struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](#c.bt_gatt_subscribe_params) \*params)
    :   Unsubscribe Attribute Value Notification.

        This procedure unsubscribe to value notification using the Client Characteristic Configuration handle. Notification callback with NULL data will be called if subscription was removed by this call, until then the parameters cannot be reused.

        The Response comes in callback `params->func`. The callback is run from the BT RX thread.

        This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

        Parameters:
        :   - **conn** – Connection object.
            - **params** – Subscribe parameters. The parameters shall be a [bt\_gatt\_subscribe\_params](#structbt__gatt__subscribe__params) from a previous call to [bt\_gatt\_subscribe()](#group__bt__gatt__client_1ga7d4a8e18f51ba6476886a15f81f48e5c).

        Return values:
        :   - **0** – Successfully queued request. Will call `params->write` on resolution.
            - **-ENOMEM** – ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by  [`CONFIG_BT_ATT_TX_COUNT`](../../../kconfig.md#CONFIG_BT_ATT_TX_COUNT "CONFIG_BT_ATT_TX_COUNT") .

    void bt\_gatt\_cancel(struct bt\_conn \*conn, void \*params)
    :   Try to cancel the first pending request identified by `params`.

        This function does not release `params` for reuse. The usual callbacks for the request still apply. A successful cancel simulates a [BT\_ATT\_ERR\_UNLIKELY](att.md#group__bt__att_1ga992baa1f0d763a00f314bdcf59965bdd) response from the server.

        This function can cancel the following request functions:

        - [bt\_gatt\_exchange\_mtu](#group__bt__gatt__client_1ga0f41da23c6559a8254b04295aff8198d)
        - [bt\_gatt\_discover](#group__bt__gatt__client_1gac06a945e5f7939b6716bc4f2cea781bd)
        - [bt\_gatt\_read](#group__bt__gatt__client_1ga1a18dd726ab960a88d7f85f2a014141a)
        - [bt\_gatt\_write](#group__bt__gatt__client_1ga843a42e68e0497d88d3f655f8ffd58d4)
        - [bt\_gatt\_subscribe](#group__bt__gatt__client_1ga7d4a8e18f51ba6476886a15f81f48e5c)
        - [bt\_gatt\_unsubscribe](#group__bt__gatt__client_1ga56509c9b8f73f729cfa5e75be22d79ae)

        Parameters:
        :   - **conn** – The connection the request was issued on.
            - **params** – The address `params` used in the request function call.

    struct bt\_gatt\_exchange\_params
    :   *#include <gatt.h>*

        GATT Exchange MTU parameters.

        Public Members

        void (\*func)(struct bt\_conn \*conn, uint8\_t err, struct [bt\_gatt\_exchange\_params](#c.bt_gatt_exchange_params) \*params)
        :   Response callback.

    struct bt\_gatt\_discover\_params
    :   *#include <gatt.h>*

        GATT Discover Attributes parameters.

        Public Members

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   Discover UUID type.

        [bt\_gatt\_discover\_func\_t](#c.bt_gatt_discover_func_t) func
        :   Discover attribute callback.

        uint16\_t attr\_handle
        :   Include service attribute declaration handle.

        uint16\_t start\_handle
        :   Included service start handle.

            Discover start handle.

        uint16\_t end\_handle
        :   Included service end handle.

            Discover end handle.

        uint8\_t type
        :   Discover type.

        struct [bt\_gatt\_subscribe\_params](#c.bt_gatt_subscribe_params) \*sub\_params
        :   Only for stack-internal use, used for automatic discovery.

    struct bt\_gatt\_read\_params
    :   *#include <gatt.h>*

        GATT Read parameters.

        Public Members

        [bt\_gatt\_read\_func\_t](#c.bt_gatt_read_func_t) func
        :   Read attribute callback.

        size\_t handle\_count
        :   If equals to 1 single.handle and single.offset are used.

            If greater than 1 multiple.handles are used. If equals to 0 by\_uuid is used for Read Using Characteristic UUID.

        uint16\_t handle
        :   Attribute handle.

        uint16\_t offset
        :   Attribute data offset.

        uint16\_t \*handles
        :   Attribute handles to read with Read Multiple Characteristic Values.

        bool variable
        :   If true use Read Multiple Variable Length Characteristic Values procedure.

            The values of the set of attributes may be of variable or unknown length. If false use Read Multiple Characteristic Values procedure. The values of the set of attributes must be of a known fixed length, with the exception of the last value that can have a variable length.

        uint16\_t start\_handle
        :   First requested handle number.

        uint16\_t end\_handle
        :   Last requested handle number.

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   2 or 16 octet UUID.

    struct bt\_gatt\_write\_params
    :   *#include <gatt.h>*

        GATT Write parameters.

        Public Members

        [bt\_gatt\_write\_func\_t](#c.bt_gatt_write_func_t) func
        :   Response callback.

        uint16\_t handle
        :   Attribute handle.

        uint16\_t offset
        :   Attribute data offset.

        const void \*data
        :   Data to be written.

        uint16\_t length
        :   Length of the data.

    struct bt\_gatt\_subscribe\_params
    :   *#include <gatt.h>*

        GATT Subscribe parameters.

        Public Members

        [bt\_gatt\_notify\_func\_t](#c.bt_gatt_notify_func_t) notify
        :   Notification value callback.

        [bt\_gatt\_subscribe\_func\_t](#c.bt_gatt_subscribe_func_t) subscribe
        :   Subscribe CCC write request response callback If given, called with the subscription parameters given when subscribing.

        uint16\_t value\_handle
        :   Subscribe value handle.

        uint16\_t ccc\_handle
        :   Subscribe CCC handle.

        uint16\_t end\_handle
        :   Subscribe End handle (for automatic discovery).

        struct [bt\_gatt\_discover\_params](#c.bt_gatt_discover_params) \*disc\_params
        :   Discover parameters used when ccc\_handle = 0.

        uint16\_t value
        :   Subscribe value.

        [bt\_security\_t](connection_mgmt.md#c.bt_security_t "bt_security_t") min\_security
        :   Minimum required security for received notification.

            Notifications and indications received over a connection with a lower security level are silently discarded.

        atomic\_t flags[[ATOMIC\_BITMAP\_SIZE](../../../kernel/services/other/atomic.md#c.ATOMIC_BITMAP_SIZE "ATOMIC_BITMAP_SIZE")([BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](#c.@172336054125152351005356152301225305321016010030.BT_GATT_SUBSCRIBE_NUM_FLAGS))]
        :   Subscription flags.
