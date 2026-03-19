---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/usb/usb-audio-mic.html
original_path: build/dts/api/bindings/usb/usb-audio-mic.html
---

# usb-audio-mic

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
USB Audio microphone specific fields.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `resolution` | `int` | Default value: `16`  Legal values: `8`, `16`, `24`, `32` |
| `sync-type` | `string` | ```text Type of endpoint synchronization for IN devices. Default value is Synchronous. Adaptive is not supported. ```  Default value: `Synchronous`  Legal values: `'No Synchronization'`, `'Asynchronous'`, `'Adaptive'`, `'Synchronous'` |
| `sample-rate-hz` | `int` | Default value: `48000` |
| `polling-interval` | `int` | Default value: `1` |
| `channel-l` | `boolean` | ```text Enable (l) channel. ``` |
| `channel-r` | `boolean` | ```text Enable (r) channel. ``` |
| `channel-c` | `boolean` | ```text Enable (c) channel. ``` |
| `channel-lfe` | `boolean` | ```text Enable (lfe) channel. ``` |
| `channel-ls` | `boolean` | ```text Enable (ls) channel. ``` |
| `channel-rs` | `boolean` | ```text Enable (rs) channel. ``` |
| `channel-lc` | `boolean` | ```text Enable (lc) channel. ``` |
| `channel-rc` | `boolean` | ```text Enable (rc) channel. ``` |
| `channel-s` | `boolean` | ```text Enable (s) channel. ``` |
| `channel-sl` | `boolean` | ```text Enable (sl) channel. ``` |
| `channel-sr` | `boolean` | ```text Enable (sr) channel. ``` |
| `channel-t` | `boolean` | ```text Enable (t) channel. ``` |
| `channel-cfg` | `boolean` | ```text Enable (cfg) channel. ``` |
| `feature-mute` | `boolean` | ```text Enable Mute feature. ```  This property is **required**. |
| `feature-volume` | `boolean` | ```text Enable Volume feature. Currently not supported. ``` |
| `feature-tone-control` | `boolean` | ```text Enable Tone Control (Bass, Mid, Treble) feature. Currently not supported. ``` |
| `feature-graphic-equalizer` | `boolean` | ```text Enable  Graphic Equalizer feature. Currently not supported. ``` |
| `feature-automatic-gain-control` | `boolean` | ```text Enable Autoamtic Gain Control feature. Currently not supported. ``` |
| `feature-delay` | `boolean` | ```text Enable Delay feature. Currently not supported. ``` |
| `feature-bass-boost` | `boolean` | ```text Enable Bass Boost feature. Currently not supported. ``` |
| `feature-loudness` | `boolean` | ```text Enable Loudness feature. Currently not supported. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “usb-audio-mic” compatible.

(None)
