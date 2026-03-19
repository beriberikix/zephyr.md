---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/device_mgmt/smp_groups/smp_group_8.html
original_path: services/device_mgmt/smp_groups/smp_group_8.html
---

# File management

The file management group provides commands that allow to upload and download files
to/from a device.

File management group defines following commands:

| `Command ID` | Command description |
| --- | --- |
| `0` | File download/upload |
| `1` | File status |
| `2` | File hash/checksum |
| `3` | Supported file hash/checksum types |
| `4` | File close |

## File download

Command allows to download contents of an existing file from specified path
of a target device. Client applications must keep track of data they have
already downloaded and where their position in the file is (MCUmgr will cache
these also), and issue subsequent requests, with modified offset, to gather
the entire file.
Request does not carry size of requested chunk, the size is specified
by application itself.
Note that file handles will remain open for consecutive requests (as long as
an idle timeout has not been reached and another transport does not make use
of uploading/downloading files using fs\_mgmt), but files are not exclusively
owned by MCUmgr, for the time of download session, and may change between
requests or even be removed.

Note

By default, all file upload/download requests are unconditionally allowed.
However, if the Kconfig option
[`CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK`](../../../kconfig.md#CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK "CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK") is enabled, then an
application can register a callback handler for
[`MGMT_EVT_OP_FS_MGMT_FILE_ACCESS`](../../../doxygen/html/group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3) (see
[MCUmgr callbacks](../mcumgr_callbacks.md#mcumgr-callbacks)), which allows for allowing or
declining access to reading/writing a particular file, or for rewriting the
path supplied by the client.

### File download request

File download request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `8` | `0` |

CBOR data of request:

```text
{
    (str)"off" :  (uint)
    (str)"name" : (str)
}
```

where:

| “off” | offset to start download at |
| --- | --- |
| “name” | absolute path to a file |

### File download response

File download response header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `8` | `0` |

CBOR data of successful response:

```text
{
    (str)"off"      : (uint)
    (str)"data"     : (byte str)
    (str,opt)"len"  : (uint)
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

| “off” | offset the response is for. |
| --- | --- |
| “data” | chunk of data read from file; it is CBOR encoded stream of bytes with embedded size; “data” appears only in responses where “rc” is 0. |
| “len” | length of file, this field is only mandatory when “off” is 0. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## File upload

Allows to upload a file to a specified location. Command will automatically overwrite
existing file or create a new one if it does not exist at specified path.
The protocol supports stateless upload where each requests carries different chunk
of a file and it is client side responsibility to track progress of upload.

Note that file handles will remain open for consecutive requests (as long as
an idle timeout has not been reached, but files are not exclusively owned by
MCUmgr, for the time of download session, and may change between requests or
even be removed. Note that file handles will remain open for consecutive
requests (as long as an idle timeout has not been reached and another transport
does not make use of uploading/downloading files using fs\_mgmt), but files are
not exclusively owned by MCUmgr, for the time of download session, and may
change between requests or even be removed.

Note

Weirdly, the current Zephyr implementation is half-stateless as is able to hold
single upload context, holding information on ongoing upload, that consists
of bool flag indicating in-progress upload, last successfully uploaded offset
and total length only.

Note

By default, all file upload/download requests are unconditionally allowed.
However, if the Kconfig option
[`CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK`](../../../kconfig.md#CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK "CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK") is enabled, then an
application can register a callback handler for
[`MGMT_EVT_OP_FS_MGMT_FILE_ACCESS`](../../../doxygen/html/group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3) (see
[MCUmgr callbacks](../mcumgr_callbacks.md#mcumgr-callbacks)), which allows for allowing or
declining access to reading/writing a particular file, or for rewriting the
path supplied by the client.

### File upload request

File upload request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `2` | `8` | `0` |

CBOR data of request:

```text
{
    (str)"off"      : (uint)
    (str)"data"     : (str)
    (str)"name"     : (str)
    (str,opt)"len"  : (uint)
}
```

where:

| “off” | offset to start/continue upload at. |
| --- | --- |
| “data” | chunk of data to write to the file; it is CBOR encoded with length embedded. |
| “name” | absolute path to a file. |
| “len” | length of file, this field is only mandatory when “off” is 0. |

### File upload response

File upload response header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `3` | `8` | `0` |

CBOR data of successful response:

```text
{
    (str)"off"      : (uint)
}
```

In case of error the CBOR data takes the form:

where:

| “off” | offset of last successfully written data. |
| --- | --- |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## File status

Command allows to retrieve status of an existing file from specified path
of a target device.

### File status request

File status request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `8` | `1` |

CBOR data of request:

```text
{
    (str)"name" : (str)
}
```

where:

| “name” | absolute path to a file. |
| --- | --- |

### File status response

File status response header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `8` | `1` |

CBOR data of successful response:

```text
{
    (str)"len"      : (uint)
}
```

In case of error the CBOR data takes form:

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

| “len” | length of file (in bytes). |
| --- | --- |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## File hash/checksum

Command allows to generate a hash/checksum of an existing file at a specified
path on a target device. Note that kernel heap memory is required for buffers to
be allocated for this to function, and large stack memory buffers are required
for generation of the output hash/checksum.
Requires [`CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH`](../../../kconfig.md#CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH "CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH") to be enabled for
the base functionality, supported hash/checksum are opt-in with
[`CONFIG_MCUMGR_GRP_FS_CHECKSUM_IEEE_CRC32`](../../../kconfig.md#CONFIG_MCUMGR_GRP_FS_CHECKSUM_IEEE_CRC32 "CONFIG_MCUMGR_GRP_FS_CHECKSUM_IEEE_CRC32") or
[`CONFIG_MCUMGR_GRP_FS_HASH_SHA256`](../../../kconfig.md#CONFIG_MCUMGR_GRP_FS_HASH_SHA256 "CONFIG_MCUMGR_GRP_FS_HASH_SHA256").

### File hash/checksum request

File hash/checksum request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `8` | `2` |

CBOR data of request:

```text
{
    (str)"name"     : (str)
    (str,opt)"type" : (str)
    (str,opt)"off"  : (uint)
    (str,opt)"len"  : (uint)
}
```

where:

| “name” | absolute path to a file. |
| --- | --- |
| “type” | type of hash/checksum to perform [Hash/checksum types](#mcumgr-group-8-hash-checksum-types) or omit to use default. |
| “off” | offset to start hash/checksum calculation at (optional, 0 if not provided). |
| “len” | maximum length of data to read from file to generate hash/checksum with (optional, full file size if not provided). |

### Hash/checksum types

| String name | Hash/checksum | Byte string | Size (bytes) |
| --- | --- | --- | --- |
| `crc32` | IEEE CRC32 checksum | No | 4 |
| `sha256` | SHA256 (Secure Hash Algorithm) | Yes | 32 |

Note that the default type will be crc32 if it is enabled, or sha256 if crc32 is
not enabled.

### File hash/checksum response

File hash/checksum response header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `8` | `2` |

CBOR data of successful response:

```text
{
    (str)"type"     : (str)
    (str,opt)"off"  : (uint)
    (str)"len"      : (uint)
    (str)"output"   : (uint or bstr)
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

| “type” | type of hash/checksum that was performed [Hash/checksum types](#mcumgr-group-8-hash-checksum-types). |
| --- | --- |
| “off” | offset that hash/checksum calculation started at (only present if not 0). |
| “len” | length of input data used for hash/checksum generation (in bytes). |
| “output” | output hash/checksum. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## Supported file hash/checksum types

Command allows listing which hash and checksum types are available on a device.
Requires Kconfig [`CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_CMD`](../../../kconfig.md#CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_CMD "CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_CMD")
to be enabled.

### Supported file hash/checksum types request

Supported file hash/checksum types request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `8` | `3` |

The command sends empty CBOR map as data.

### Supported file hash/checksum types response

Supported file hash/checksum types response header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `8` | `3` |

CBOR data of successful response:

```text
{
    (str)"types" : {
        (str)<hash_checksum_name> : {
            (str)"format"       : (uint)
            (str)"size"         : (uint)
        }
        ...
    }
}
```

In case of error the CBOR data takes form:

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

| <hash\_checksum\_name> | name of the hash/checksum type [Hash/checksum types](#mcumgr-group-8-hash-checksum-types). |
| --- | --- |
| “format” | format that the hash/checksum returns where 0 is for numerical and 1 is for byte array. |
| “size” | size (in bytes) of output hash/checksum response. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

## File close

Command allows closing any open file handles held by fs\_mgmt upload/download
requests that might have stalled or be incomplete.

### File close request

File close request header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `2` | `8` | `4` |

The command sends empty CBOR map as data.

### File close response

File close response header:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `3` | `8` | `4` |

The command sends an empty CBOR map as data if successful.
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

| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| --- | --- |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |
