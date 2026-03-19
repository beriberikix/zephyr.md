---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/device_mgmt/smp_groups/smp_group_63.html
original_path: services/device_mgmt/smp_groups/smp_group_63.html
---

# Zephyr Management Group

Zephyr management group defines the following commands:

| `Command ID` | Command description |
| --- | --- |
| `0` | Erase storage |

## Erase storage command

Erase storage command allows clearing the `storage_partition` flash partition on a device,
generally this is used when switching to a new application build if the application uses storage
that should be cleared (application dependent).

### Erase storage request

Erase storage request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `2` | `63` | `0` |

The command sends sends empty CBOR map as data.

### Erase storage response

Read setting response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `3` | `63` | `0` |

The command sends an empty CBOR map as data if successful. In case of error the CBOR data takes
the form:

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

| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| --- | --- |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |
