---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/audio/shell/bap.html
original_path: connectivity/bluetooth/api/audio/shell/bap.html
---

# Bluetooth: Basic Audio Profile

This document describes how to run Basic Audio Profile functionality which
includes:

> - Capabilities and Endpoint discovery
> - Audio Stream Endpoint procedures

## Commands

```shell
bap --help
Subcommands:
   init                   : [ase_sink_count, ase_source_count]
   select_broadcast       : <stream>
   create_broadcast       : [preset <preset_name>] [enc <broadcast_code>]
   start_broadcast        :
   stop_broadcast         :
   delete_broadcast       :
   create_broadcast_sink  : 0x<broadcast_id>
   create_sink_by_name    : <broadcast_name>
   sync_broadcast         : 0x<bis_index> [[[0x<bis_index>] 0x<bis_index>] ...]
                           [bcode <broadcast code> || bcode_str <broadcast code
                           as string>]
   stop_broadcast_sink    : Stops broadcast sink
   term_broadcast_sink    :
   discover               : [dir: sink, source]
   config                 : <direction: sink, source> <index> [loc <loc_bits>]
                           [preset <preset_name>]
   stream_qos             : interval [framing] [latency] [pd] [sdu] [phy] [rtn]
   qos                    : Send QoS configure for Unicast Group
   enable                 : [context]
   connect                : Connect the CIS of the stream
   stop
   list
   print_ase_info         : Print ASE info for default connection
   metadata               : [context]
   start
   disable
   release
   select_unicast         : <stream>
   preset                 : <sink, source, broadcast> [preset]
                           [config
                                 [freq <frequency>]
                                 [dur <duration>]
                                 [chan_alloc <location>]
                                 [frame_len <frame length>]
                                 [frame_blks <frame blocks>]]
                           [meta
                                 [pref_ctx <context>]
                                 [stream_ctx <context>]
                                 [program_info <program info>]
                                 [lang <ISO 639-3 lang>]
                                 [ccid_list <ccids>]
                                 [parental_rating <rating>]
                                 [program_info_uri <URI>]
                                 [audio_active_state <state>]
                                 [bcast_flag]
                                 [extended <meta>]
                                 [vendor <meta>]]
   send                   : Send to Audio Stream [data]
   bap_stats              : Sets or gets the statistics reporting interval in # of
                           packets
   set_location           : <direction: sink, source> <location bitmask>
   set_context            : <direction: sink, source><context bitmask> <type:
                           supported, available>
```

State Machine Transitions

| Command | Depends | Allowed States | Next States |
| --- | --- | --- | --- |
| init | none | any | none |
| discover | init | any | any |
| config | discover | idle/codec-configured/qos-configured | codec-configured |
| qos | config | codec-configured/qos-configured | qos-configured |
| enable | qos | qos-configured | enabling |
| connect | qos/enable | qos-configured/enabling | qos-configured/enabling |
| [start] | enable/connect | enabling | streaming |
| disable | enable | enabling/streaming | disabling |
| [stop] | disable | disabling | qos-configure/idle |
| release | config | any | releasing/codec-configure/idle |
| list | none | any | none |
| select\_unicast | none | any | none |
| send | enable | streaming | none |

## Example Central

Connect and establish a sink stream:

```shell
uart:~$ bt init
uart:~$ bap init
uart:~$ bt connect <address>
uart:~$ gatt exchange-mtu
uart:~$ bap discover sink
uart:~$ bap config sink 0
uart:~$ bap qos
uart:~$ bap enable
uart:~$ bap connect
```

Connect and establish a source stream:

```shell
uart:~$ bt init
uart:~$ bap init
uart:~$ bt connect <address>
uart:~$ gatt exchange-mtu
uart:~$ bap discover source
uart:~$ bap config source 0
uart:~$ bap qos
uart:~$ bap enable
uart:~$ bap connect
uart:~$ bap start
```

Disconnect and release:

```shell
uart:~$ bap disable
uart:~$ bap release
```

## Example Peripheral

Listen:

```shell
uart:~$ bt init
uart:~$ bap init
uart:~$ bt advertise on
```

Server initiated disable and release:

```shell
uart:~$ bap disable
uart:~$ bap release
```

## Example Broadcast Source

Create and establish a broadcast source stream:

```shell
uart:~$ bap init
uart:~$ bap create_broadcast
uart:~$ bap start_broadcast
```

Stop and release a broadcast source stream:

```shell
uart:~$ bap stop_broadcast
uart:~$ bap delete_broadcast
```

## Example Broadcast Sink

Scan for and establish a broadcast sink stream.
The command `bap create_broadcast_sink` will either use existing periodic advertising
sync (if exist) or start scanning and sync to the periodic advertising with the provided broadcast
ID before syncing to the BIG.

```shell
uart:~$ bap init
uart:~$ bap create_broadcast_sink 0xEF6716
No PA sync available, starting scanning for broadcast_id
Found broadcaster with ID 0xEF6716 and addr 03:47:95:75:C0:08 (random) and sid 0x00
Attempting to PA sync to the broadcaster
PA synced to broadcast with broadcast ID 0xEF6716
Attempting to sync to the BIG
Received BASE from sink 0x20019080:
Presentation delay: 40000
Subgroup count: 1
Subgroup 0x20024182:
   Codec Format: 0x06
   Company ID  : 0x0000
   Vendor ID   : 0x0000
   codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
      Codec specific configuration:
      Sampling frequency: 16000 Hz (3)
      Frame duration: 10000 us (1)
      Channel allocation:
               Front left (0x00000001)
               Front right (0x00000002)
      Octets per codec frame: 40
      Codec specific metadata:
      Streaming audio contexts:
         Unspecified (0x0001)
      BIS index: 0x01
         codec cfg id 0x06 cid 0x0000 vid 0x0000 count 6
         Codec specific configuration:
            Channel allocation:
               Front left (0x00000001)
         Codec specific metadata:
            None
      BIS index: 0x02
         codec cfg id 0x06 cid 0x0000 vid 0x0000 count 6
         Codec specific configuration:
            Channel allocation:
               Front right (0x00000002)
         Codec specific metadata:
            None
Possible indexes: 0x01 0x02
Sink 0x20019110 is ready to sync without encryption
uart:~$ bap sync_broadcast 0x01
```

### Scan for and establish a broadcast sink stream by broadcast name

The command `bap create_sink_by_name` will start scanning and sync to the periodic
advertising with the provided broadcast name before syncing to the BIG.

```shell
uart:~$ bap init
uart:~$ bap create_sink_by_name "Test Broadcast"
Starting scanning for broadcast_name
Found matched broadcast name 'Test Broadcast' with address 03:47:95:75:C0:08 (random)
Found broadcaster with ID 0xEF6716 and addr 03:47:95:75:C0:08 (random) and sid 0x00
Attempting to PA sync to the broadcaster
PA synced to broadcast with broadcast ID 0xEF6716
Attempting to create the sink
Received BASE from sink 0x20019080:
Presentation delay: 40000
Subgroup count: 1
Subgroup 0x20024182:
   Codec Format: 0x06
   Company ID  : 0x0000
   Vendor ID   : 0x0000
   codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
      Codec specific configuration:
      Sampling frequency: 16000 Hz (3)
      Frame duration: 10000 us (1)
      Channel allocation:
               Front left (0x00000001)
               Front right (0x00000002)
      Octets per codec frame: 40
      Codec specific metadata:
      Streaming audio contexts:
         Unspecified (0x0001)
      BIS index: 0x01
         codec cfg id 0x06 cid 0x0000 vid 0x0000 count 6
         Codec specific configuration:
            Channel allocation:
               Front left (0x00000001)
         Codec specific metadata:
            None
      BIS index: 0x02
         codec cfg id 0x06 cid 0x0000 vid 0x0000 count 6
         Codec specific configuration:
            Channel allocation:
               Front right (0x00000002)
         Codec specific metadata:
            None
Possible indexes: 0x01 0x02
Sink 0x20019110 is ready to sync without encryption
uart:~$ bap sync_broadcast 0x01
```

### Syncing to encrypted broadcast

If the broadcast is encrypted, the broadcast code can be entered with the `bap sync_broadcast`
command as such:

```shell
Sink 0x20019110 is ready to sync with encryption
uart:~$ bap sync_broadcast 0x01 bcode 0102030405060708090a0b0c0d0e0f
```

The broadcast code can be 1-16 values, either as a string or a hexadecimal value.

```shell
Sink 0x20019110 is ready to sync with encryption
uart:~$ bap sync_broadcast 0x01 bcode_str thisismycode
```

Stop and release a broadcast sink stream:

```shell
uart:~$ bap stop_broadcast_sink
uart:~$ bap term_broadcast_sink
```

## Init

The `init` command register local PAC records which are necessary to be
able to configure stream and properly manage capabilities in use.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| none | any | none |

```shell
uart:~$ bap init
```

## Discover PAC(s) and ASE(s)

Once connected the `discover` command discover PAC records and ASE
characteristics representing remote endpoints.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| init | any | any |

Note

Use command `gatt exchange-mtu` to make sure the MTU is configured
properly.

```shell
uart:~$ gatt exchange-mtu
Exchange pending
Exchange successful
uart:~$ bap discover [type: sink, source]
uart:~$ bap discover sink
conn 0x2000b168: codec_cap 0x2001f8ec dir 0x02
codec cap id 0x06 cid 0x0000 vid 0x0000
   Codec specific capabilities:
      Supported sampling frequencies:
         8000 Hz (0x0001)
         11025 Hz (0x0002)
         16000 Hz (0x0004)
         22050 Hz (0x0008)
         24000 Hz (0x0010)
         32000 Hz (0x0020)
         44100 Hz (0x0040)
         48000 Hz (0x0080)
         88200 Hz (0x0100)
         96000 Hz (0x0200)
         176400 Hz (0x0400)
         192000 Hz (0x0800)
         384000 Hz (0x1000)
      Supported frame durations:
         10 ms (0x02)
      Supported channel counts:
         1 channel (0x01)
      Supported octets per codec frame counts:
         Min: 40
         Max: 120
      Supported max codec frames per SDU: 1
   Codec capabilities metadata:
      Preferred audio contexts:
         Conversational (0x0002)
         Media (0x0004)
ep 0x81754e0
ep 0x81755d4
Discover complete: err 0
```

## Select preset

The `preset` command can be used to either print the default preset
configuration or set a different one, it is worth noting that it doesn’t change
any stream previously configured.

```shell
uart:~$ bap preset
preset - <sink, source, broadcast> [preset]
         [config
               [freq <frequency>]
               [dur <duration>]
               [chan_alloc <location>]
               [frame_len <frame length>]
               [frame_blks <frame blocks>]]
         [meta
               [pref_ctx <context>]
               [stream_ctx <context>]
               [program_info <program info>]
               [lang <ISO 639-3 lang>]
               [ccid_list <ccids>]
               [parental_rating <rating>]
               [program_info_uri <URI>]
               [audio_active_state <state>]
               [bcast_flag]
               [extended <meta>]
               [vendor <meta>]]
uart:~$ bap preset sink
16_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
   Codec specific configuration:
      Sampling frequency: 16000 Hz (3)
      Frame duration: 10000 us (1)
      Channel allocation:
                  Front left (0x00000001)
                  Front right (0x00000002)
      Octets per codec frame: 40
   Codec specific metadata:
      Streaming audio contexts:
         Game (0x0008)
QoS: interval 10000 framing 0x00 phy 0x02 sdu 40 rtn 2 latency 10 pd 40000

uart:~$ bap preset sink 32_2_1
32_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
   Codec specific configuration:
      Sampling frequency: 32000 Hz (6)
      Frame duration: 10000 us (1)
      Channel allocation:
                  Front left (0x00000001)
                  Front right (0x00000002)
      Octets per codec frame: 80
   Codec specific metadata:
      Streaming audio contexts:
         Game (0x0008)
   QoS: interval 10000 framing 0x00 phy 0x02 sdu 80 rtn 2 latency 10 pd 40000
```

## Configure preset

The `bap preset` command can also be used to configure the preset used for the subsequent
commands. It is possible to add or set (or reset) any value. To reset the preset, the command can simply be run without the `config` or `meta` parameter. The parameters are using the
assigned numbers values.

```shell
uart:~$ bap preset sink 32_2_1
32_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
data #0: type 0x01 value_len 1
00000000: 06                                               |.                |
data #1: type 0x02 value_len 1
00000000: 01                                               |.                |
data #2: type 0x03 value_len 4
00000000: 03 00 00 00                                      |....             |
data #3: type 0x04 value_len 2
00000000: 50 00                                            |P.               |
meta #0: type 0x02 value_len 2
00000000: 08 00                                            |..               |
QoS: interval 10000 framing 0x00 phy 0x02 sdu 80 rtn 2 latency 10 pd 40000

uart:~$ bap preset sink 32_2_1 config freq 10
32_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
data #0: type 0x01 value_len 1
00000000: 0a                                               |.                |
data #1: type 0x02 value_len 1
00000000: 01                                               |.                |
data #2: type 0x03 value_len 4
00000000: 03 00 00 00                                      |....             |
data #3: type 0x04 value_len 2
00000000: 50 00                                            |P.               |
meta #0: type 0x02 value_len 2
00000000: 08 00                                            |..               |
QoS: interval 10000 framing 0x00 phy 0x02 sdu 80 rtn 2 latency 10 pd 40000

uart:~$ bap preset sink 32_2_1 config freq 10 meta lang "eng" stream_ctx 4
32_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
data #0: type 0x01 value_len 1
00000000: 0a                                               |.                |
data #1: type 0x02 value_len 1
00000000: 01                                               |.                |
data #2: type 0x03 value_len 4
00000000: 03 00 00 00                                      |....             |
data #3: type 0x04 value_len 2
00000000: 50 00                                            |P.               |
meta #0: type 0x02 value_len 2
00000000: 04 00                                            |..               |
meta #1: type 0x04 value_len 3
00000000: 65 6e 67                                         |eng              |
QoS: interval 10000 framing 0x00 phy 0x02 sdu 80 rtn 2 latency 10 pd 40000
```

## Configure Codec

The `config` command attempts to configure a stream for the given
direction using a preset codec configuration which can either be passed directly
or in case it is omitted the default preset is used.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| discover | idle/codec-configured/qos-configured | codec-configured |

```shell
uart:~$ bap config <direction: sink, source> <index> [loc <loc_bits>] [preset <preset_name>]
uart:~$ bap config sink 0
Setting location to 0x00000000
ASE config: preset 16_2_1
stream 0x2000df70 config operation rsp_code 0 reason 0
```

## Configure Stream QoS

The `stream_qos` Sets a new stream QoS.

```shell
uart:~$ bap stream_qos <interval> [framing] [latency] [pd] [sdu] [phy] [rtn]
uart:~$ bap stream_qos 10
```

## Configure QoS

The `qos` command attempts to configure the stream QoS using the preset
configuration, each individual QoS parameter can be set with use optional
parameters.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| config | qos-configured/codec-configured | qos-configured |

```shell
uart:~$ bap qos
```

## Enable

The `enable` command attempts to enable the stream previously configured.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| qos | qos-configured | enabling |

```shell
uart:~$ bap enable [context]
uart:~$ bap enable Media
```

## Connect

The `connect` command attempts to connect the stream previously configured.
Sink streams will have to be started by the unicast server, and source streams will have to be
started by the unicast client.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| qos/enable | qos-configured/enabling | qos-configured/enabling |

```shell
uart:~$ bap connect
```

## Start

The `start` command is only necessary when starting a source stream.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| enable/connect | enabling | streaming |

```shell
uart:~$ bap start
```

## Disable

The `disable` command attempts to disable the stream previously enabled,
if the remote peer accepts then the ISO disconnection procedure is also
initiated.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| enable | enabling/streaming | disabling |

```shell
uart:~$ bap disable
```

## Stop

The `stop` command is only necessary when acting as a sink as it indicates
to the source the stack is ready to stop receiving data.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| disable | disabling | qos-configure/idle |

```shell
uart:~$ bap stop
```

## Release

The `release` command releases the current stream and its configuration.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| config | any | releasing/codec-configure/idle |

```shell
uart:~$ bap release
```

## List

The `list` command list the available streams.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| none | any | none |

```shell
uart:~$ bap list
*0: ase 0x01 dir 0x01 state 0x01
```

## Select Unicast

The `select_unicast` command set a unicast stream as default.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| none | any | none |

```shell
uart:~$ bap select <ase>
uart:~$ bap select 0x01
Default stream: 1
```

To select a broadcast stream:

```shell
uart:~$ bap select 0x01 broadcast
Default stream: 1 (broadcast)
```

## Send

The `send` command sends data over BAP Stream.

State Machine Transitions

| Depends | Allowed States | Next States |
| --- | --- | --- |
| enable | streaming | none |

```shell
uart:~$ bap send [count]
uart:~$ bap send
Audio sending...
```
