---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/device_mgmt/smp_protocol.html
original_path: services/device_mgmt/smp_protocol.html
---

# SMP Protocol Specification

This is description of Simple Management Protocol, SMP, that is used by
MCUmgr to pass requests to devices and receive responses from them.

SMP is an application layer protocol. The underlying transport layer is not
in scope of this documentation.

Note

SMP in this context refers to SMP for MCUmgr (Simple Management Protocol),
it is unrelated to SMP in Bluetooth (Security Manager Protocol), but there
is an MCUmgr SMP transport for Bluetooth.

## Frame: The envelope

Each frame consists of a header and data. The `Data Length` field in the
header may be used for reassembly purposes if underlying transport layer supports
fragmentation.
Frames are encoded in “Big Endian” (Network endianness) when fields are more than
one byte long, and takes the following form:

| 3 | | | | | | | | 2 | | | | | | | | 1 | | | | | | | | 0 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Res | | | Ver | | OP | | | Flags | | | | | | | | Data Length | | | | | | | | | | | | | | | |
| Group ID | | | | | | | | | | | | | | | | Sequence Num | | | | | | | | Command ID | | | | | | | |
| Data … | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

Note

The original specification states that SMP should support receiving
both the “Little-endian” and “Big-endian” frames but in reality the
MCUmgr library is hardcoded to always treat “Network” side as
“Big-endian”.

Data is optional and is not present when `Data Length` is zero.
The encoding of data depends on the target of group/ID.

A description of the various fields and their meaning:

| Field | Description |
| --- | --- |
| `Res` | This is reserved, not-used field and must be always set to 0. |
| `Ver` (Version) | This indicates the version of the protocol being used, this should be set to 0b01 to use the newer SMP transport where error codes are more detailed and returned in the map, otherwise left as 0b00 to use the legacy SMP protocol. Versions 0b10 and 0b11 are reserved for future use and should not be used. |
| `OP` | [`mcumgr_op_t`](../../doxygen/html/group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd), determines whether information is written to a device or requested from it and whether a packet contains request to an SMP server or response from it. |
| `Flags` | Reserved for flags; there are no flags defined yet, the field should be set to 0 |
| `Data Length` | Length of the `Data` field |
| `Group ID` | [`mcumgr_group_t`](../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5), see [Management Group ID’s](#mcumgr-smp-protocol-group-ids) for further details. |
| `Sequence Num` | This is a frame sequence number. The number is increased by one with each request frame. The Sequence Num of a response should match the one in the request. |
| `Command ID` | This is a command, within `Group`. |
| `Data` | This is data payload of the `Data Length` size. It is optional as `Data Length` may be set to zero, which means that no data follows the header. |

Note

Contents of `Data` depends on a value of an `OP`, a `Group ID`,
and a `Command ID`.

### Management `Group ID`’s

The SMP protocol supports predefined common groups and allows user defined
groups. The following table presents a list of common groups:

| Decimal ID | Group description |
| --- | --- |
| `0` | [Default/OS Management Group](smp_groups/smp_group_0.md#mcumgr-smp-group-0) |
| `1` | [Application/software image management group](smp_groups/smp_group_1.md#mcumgr-smp-group-1) |
| `2` | [Statistics management](smp_groups/smp_group_2.md#mcumgr-smp-group-2) |
| `3` | [Settings (Config) Management Group](smp_groups/smp_group_3.md#mcumgr-smp-group-3) |
| `4` | Application/system log management (currently not used by Zephyr) |
| `5` | Run-time tests (unused by Zephyr) |
| `6` | Split image management (unused by Zephyr) |
| `7` | Test crashing application (unused by Zephyr) |
| `8` | [File management](smp_groups/smp_group_8.md#mcumgr-smp-group-8) |
| `9` | [Shell management](smp_groups/smp_group_9.md#mcumgr-smp-group-9) |
| `63` | [Zephyr Management Group](smp_groups/smp_group_63.md#mcumgr-smp-group-63) |
| `64` | This is the base group for defining an application specific management groups. |

The payload for above groups, except for user groups (`64` and above) is
always CBOR encoded. The group `64`, and above can define their own scheme
for data communication.

## Minimal response

Regardless of a command issued, as long as there is SMP client on the
other side of a request, a response should be issued containing the header
followed by CBOR map container.
Lack of response is only allowed when there is no SMP service or device is
non-responsive.

### Minimal response SMP data

Minimal response is:

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

| “err” -> “group” | [`mcumgr_group_t`](../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| --- | --- |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |

Note that in the case of a successful command, an empty map will be returned (`rc`/`err` is
only returned if there is an error condition, therefore if only an empty map is returned or a
response lacks these, the request can be considered as being successful. For SMP version 2,
errors relating to SMP itself that are not group specific will still be returned as `rc`
errors, SMP version 2 clients must therefore be able to handle both types of errors.

## Specifications of management groups supported by Zephyr
