---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/device_mgmt/smp_groups/smp_group_2.html
original_path: services/device_mgmt/smp_groups/smp_group_2.html
---

# Statistics management

Statistics management allows to obtain data gathered by Statistics subsystem
of Zephyr, enabled with [`CONFIG_STATS`](../../../kconfig.md#CONFIG_STATS "CONFIG_STATS").

Statistics management group defines commands:

| `Command ID` | Command description |
| --- | --- |
| `0` | Group data |
| `1` | List groups |

## Statistics: group data

The command is used to obtain data for group specified by a name.
The name is one of group names as registered, with
[`STATS_INIT_AND_REG`](../../../doxygen/html/stats_2stats_8h.md#a7a3f6d5dc044e6948998b8bc19efa493) macro or `stats_init_and_reg()` function
call, within module that gathers the statistics.

### Statistics: group data request

Statistics group data request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `2` | `0` |

CBOR data of request:

```text
{
    (str)"name" :  (str)
}
```

where:

| “name” | group name. |
| --- | --- |

### Statistics: group data response

Statistics group data response header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `2` | `0` |

CBOR data of successful response:

```text
{
    (str)"name"     : (str)
    (str)"fields"   : {
        (str)<entry_name> : (uint)
        ...
    }
}
```

In case of error the CBOR data takes the form:

SMP version 2SMP version 1 (and non-group SMP version 2)

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

| “name” | this is name of group the response contains data for. |
| --- | --- |
| “fields” | this is map of entries within groups that consists of pairs where the entry name is mapped to value it represents in statistics. |
| <entry\_name> | single entry to value mapping; value is hardcoded to unsigned integer type, in a CBOR meaning. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## Statistics: list of groups

The command is used to obtain list of groups of statistics that are gathered
on a device. This is a list of names as given to groups with
[`STATS_INIT_AND_REG`](../../../doxygen/html/stats_2stats_8h.md#a7a3f6d5dc044e6948998b8bc19efa493) macro or `stats_init_and_reg()` function
calls, within module that gathers the statistics; this means that this command
may be considered optional as it is known during compilation what groups will
be included into build and listing them is not needed prior to issuing a query.

### Statistics: list of groups request

Statistics group list request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `2` | `1` |

The command sends an empty CBOR map as data.

### Statistics: list of groups response

Statistics group list request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `2` | `1` |

CBOR data of successful response:

```text
{
    (str)"stat_list" :  [
        (str)<stat_group_name>, ...
    ]
}
```

In case of error the CBOR data takes the form:

SMP version 2SMP version 1 (and non-group SMP version 2)

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

| “stat\_list” | array of strings representing group names; this array may be empty if there are no groups. |
| --- | --- |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |
