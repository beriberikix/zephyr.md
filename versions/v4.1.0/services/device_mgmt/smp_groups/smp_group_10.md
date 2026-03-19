---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/device_mgmt/smp_groups/smp_group_10.html
original_path: services/device_mgmt/smp_groups/smp_group_10.html
---

# Enumeration Management Group

Enumeration management group defines the following commands:

| `Command ID` | Command description |
| --- | --- |
| `0` | Count of supported groups |
| `1` | List supported groups |
| `2` | Fetch single group ID |
| `3` | Details on supported groups |

## Count of supported groups command

Count of supported groups returns the total number of MCUmgr command groups that a device supports.

### Count of supported groups request

Read setting request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `10` | `0` |

The command sends an empty CBOR map as data.

### Count of supported groups response

Count of supported groups response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `10` | `0` |

CBOR data of successful response:

```text
{
    (str)"count"        : (uint)
}
```

In case of error the CBOR data takes the form:

SMP version 2SMP version 1

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

```text
{
    (str)"rc"       : (int)
}
```

where:

| “count” | contains the total number of supported MCUmgr groups on the device. |
| --- | --- |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## List supported groups command

List supported groups command allows listing the group IDs of supported MCUmgr groups on the
device.

### List supported groups request

List supported groups request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `10` | `1` |

The command sends an empty CBOR map as data.

### List supported groups response

List supported groups response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `10` | `1` |

CBOR data of successful response:

```text
{
    (str)"groups" : [
        (uint)
        ...
    ]
}
```

In case of error the CBOR data takes the form:

SMP version 2SMP version 1

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

```text
{
    (str)"rc"       : (int)
}
```

where:

| “groups” | contains a list of the supported MCUmgr group IDs on the device. |
| --- | --- |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## Fetch single group ID command

Fetch single group ID command allows listing the group IDs of supported MCUmgr groups on the
device, one by one.

### Fetch single group ID request

Fetch single group ID request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `10` | `2` |

CBOR data of request:

```text
{
    (str,opt)"index" : (uint)
}
```

where:

| “index” | contains the (0-based) index of the group to return information on, can be omitted to return the first group’s details. |
| --- | --- |

### Fetch single group ID response

Fetch single group ID response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `10` | `2` |

CBOR data of successful response:

```text
{
    (str)"group"    : (uint)
    (str,opt)"end"  : (bool)
}
```

In case of error the CBOR data takes the form:

SMP version 2SMP version 1

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

```text
{
    (str)"rc"       : (int)
}
```

where:

| “group” | contains the list of the supported MCUmgr group IDs on the device. |
| --- | --- |
| “end” | will be set to true if the listed group is the final supported group on the device, otherwise will be omitted. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## Details on supported groups command

Details on supported groups command allows fetching details on each supported MCUmgr group, such
as the name and number of handlers. A device can specify an allow list of groups to return details
on or details on all groups can be returned.

This command is optional, it can be enabled using [`CONFIG_MCUMGR_GRP_ENUM_DETAILS`](../../../kconfig.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS "CONFIG_MCUMGR_GRP_ENUM_DETAILS").
The optional name and number of handlers can be enabled/disabled with
[`CONFIG_MCUMGR_GRP_ENUM_DETAILS_NAME`](../../../kconfig.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_NAME "CONFIG_MCUMGR_GRP_ENUM_DETAILS_NAME") and
[`CONFIG_MCUMGR_GRP_ENUM_DETAILS_HANDLERS`](../../../kconfig.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_HANDLERS "CONFIG_MCUMGR_GRP_ENUM_DETAILS_HANDLERS").

### Details on supported groups request

Details on supported groups request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `10` | `3` |

Details on all groupsDetails on specified groups

The command sends an empty CBOR map as data.

CBOR data of request:

```text
{
    (str)"groups" : [
        (uint)
        ...
    ]
}
```

where:

| “groups” | contains a list of the MCUmgr group IDs to fetch details on. |
| --- | --- |

### Details on supported groups response

Details on supported groups response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `10` | `3` |

CBOR data of successful response:

```text
{
    (str)"groups" : [
        {
            (str)"group"          : (uint)
            (str,opt)"name"       : (str)
            (str,opt)"handlers"   : (uint)
        }
        ...
    ]
}
```

In case of error the CBOR data takes the form:

SMP version 2SMP version 1

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

```text
{
    (str)"rc"       : (int)
}
```

where:

| “group” | the group ID of the MCUmgr command group. |
| --- | --- |
| “name” | the name of the MCUmgr command group. |
| “handlers” | the number of handlers that the MCUmgr command group supports. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## Details on supported groups callback

There is a details on supported groups MCUmgr callback available (see [MCUmgr Callbacks](../mcumgr_callbacks.md#mcumgr-callbacks) for
details on callbacks) which allows for applications/modules to add additional fields to this
response. This callback can be enabled with [`CONFIG_MCUMGR_GRP_ENUM_DETAILS_HOOK`](../../../kconfig.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_HOOK "CONFIG_MCUMGR_GRP_ENUM_DETAILS_HOOK"),
registered with the event [`MGMT_EVT_OP_ENUM_MGMT_DETAILS`](../../../doxygen/html/group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf), whereby the supplied
callback data is [`enum_mgmt_detail_output`](../../../doxygen/html/structenum__mgmt__detail__output.md). Note that
[`CONFIG_MCUMGR_GRP_ENUM_DETAILS_STATES`](../../../kconfig.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_STATES "CONFIG_MCUMGR_GRP_ENUM_DETAILS_STATES") will need incrementing by the number of
additional extra fields that are added.
