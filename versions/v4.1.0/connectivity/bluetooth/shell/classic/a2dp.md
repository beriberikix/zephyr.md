---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/shell/classic/a2dp.html
original_path: connectivity/bluetooth/shell/classic/a2dp.html
---

# Bluetooth: A2DP Shell

The `a2dp` command exposes parts of the A2DP API.

The following examples assume that you have two devices already connected.

Here is a example connecting two devices:
:   - Source and Sink sides register a2dp callbacks. using `a2dp register_cb`.
    - Source and Sink sides register stream endpoints. using `a2dp register_ep source sbc` and `a2dp register_ep sink sbc`.
    - Source establish A2dp connection. It will create the AVDTP Signaling and Media L2CAP channels. using `a2dp connect`.
    - Source and Sink side can discover remote device’s stream endpoints. using `a2dp discover_peer_eps`
    - Source or Sink configure the stream to create the stream after discover remote’s endpoints. using `a2dp configure`.
    - Source or Sink establish the stream. using `a2dp establish`.
    - Source or Sink start the media. using `a2dp start`.
    - Source test the media sending. using `a2dp send_media` to send one test packet data.
    - Source or Sink suspend the media. using `a2dp suspend`.
    - Source or Sink release the media. using `a2dp release`.

Device A (Audio Source Side)Device B (Audio Sink Side)

```shell
uart:~$ a2dp register_cb
success
uart:~$ a2dp register_ep source sbc
SBC source endpoint is registered
uart:~$ a2dp connect
Bonded with XX:XX:XX:XX:XX:XX
Security changed: XX:XX:XX:XX:XX:XX level 2
a2dp connected
uart:~$ a2dp discover_peer_eps
endpoint id: 1, (sink), (idle):
  codec type: SBC
  sample frequency:
          44100
          48000
  channel mode:
          Mono
          Stereo
          Joint-Stereo
  Block Length:
          16
  Subbands:
          8
  Allocation Method:
          Loudness
  Bitpool Range: 18 - 35
uart:~$ a2dp configure
success to configure
stream configured
uart:~$ a2dp establish
success to establish
stream established
uart:~$ a2dp start
success to start
stream started
uart:~$ a2dp send_media
frames num: 1, data length: 160
data: 1, 2, 3, 4, 5, 6 ......
uart:~$ a2dp suspend
success to suspend
stream suspended
uart:~$ a2dp release
success to release
stream released
```

```shell
uart:~$ a2dp register_cb
success
uart:~$ a2dp register_ep sink sbc
SBC sink endpoint is registered
<after a2dp connect>
Connected: XX:XX:XX:XX:XX:XX
Bonded with XX:XX:XX:XX:XX:XX
Security changed: XX:XX:XX:XX:XX:XX level 2
a2dp connected
<after a2dp configure of source side>
receive requesting config and accept
sample rate 44100Hz
stream configured
<after a2dp establish of source side>
receive requesting establishment and accept
stream established
<after a2dp start of source side>
receive requesting start and accept
stream started
<after a2dp send_media of source side>
received, num of frames: 1, data length: 160
data: 1, 2, 3, 4, 5, 6 ......
<after a2dp suspend of source side>
receive requesting suspend and accept
stream suspended
<after a2dp release of source side>
receive requesting release and accept
stream released
...
```
