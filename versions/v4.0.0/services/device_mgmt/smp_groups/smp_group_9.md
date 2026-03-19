---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/device_mgmt/smp_groups/smp_group_9.html
original_path: services/device_mgmt/smp_groups/smp_group_9.html
---

# Shell management

Shell management allows passing commands to the shell subsystem over the SMP
protocol.

Shell management group defines following commands:

| `Command ID` | Command description |
| --- | --- |
| `0` | Shell command line execute |

## Shell command line execute

The command allows to execute command line in a similar way to typing it into
a shell, but both a request and a response are transported over SMP.

### Shell command line execute request

Execute command request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `2` | `9` | `0` |

CBOR data of request:

```text
{
    (str)"argv"     : [
        (str)<cmd>
        (str,opt)<arg>
        ...
    ]
}
```

where:

| “argv” | array consisting of strings representing command and its arguments. |
| --- | --- |
| <cmd> | command to be executed. |
| <arg> | optional arguments to command. |

### Shell command line execute response

Command line execute response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `3` | `9` | `0` |

CBOR data of successful response:

```text
{
    (str)"o"            : (str)
    (str)"ret"          : (int)
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

| “o” | command output. |
| --- | --- |
| “ret” | return code from shell command execution. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

Note

In older versions of Zephyr, “rc” was used for both the mcumgr status code
and shell command execution return code, this legacy behaviour can be
restored by enabling [`CONFIG_MCUMGR_GRP_SHELL_LEGACY_RC_RETURN_CODE`](../../../kconfig.md#CONFIG_MCUMGR_GRP_SHELL_LEGACY_RC_RETURN_CODE "CONFIG_MCUMGR_GRP_SHELL_LEGACY_RC_RETURN_CODE")
