---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/usb/usb-audio-hs.html
original_path: build/dts/api/bindings/usb/usb-audio-hs.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# usb-audio-hs

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
USB Audio headset specific fields.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `mic-resolution` | `int` | Default value: `16`  Legal values: `8`, `16`, `24`, `32` |
| `mic-sync-type` | `string` | ```text Type of endpoint synchronization for IN devices. Default value is Synchronous. Adaptive is not supported. ```  Default value: `Synchronous`  Legal values: `'No Synchronization'`, `'Asynchronous'`, `'Adaptive'`, `'Synchronous'` |
| `mic-sample-rate-hz` | `int` | Default value: `48000` |
| `mic-polling-interval` | `int` | Default value: `1` |
| `hp-resolution` | `int` | Default value: `16`  Legal values: `8`, `16`, `24`, `32` |
| `hp-sample-rate-hz` | `int` | Default value: `48000` |
| `hp-polling-interval` | `int` | Default value: `1` |
| `mic-channel-l` | `boolean` | ```text Enable (l) channel. ``` |
| `mic-channel-r` | `boolean` | ```text Enable (r) channel. ``` |
| `mic-channel-c` | `boolean` | ```text Enable (c) channel. ``` |
| `mic-channel-lfe` | `boolean` | ```text Enable (lfe) channel. ``` |
| `mic-channel-ls` | `boolean` | ```text Enable (ls) channel. ``` |
| `mic-channel-rs` | `boolean` | ```text Enable (rs) channel. ``` |
| `mic-channel-lc` | `boolean` | ```text Enable (lc) channel. ``` |
| `mic-channel-rc` | `boolean` | ```text Enable (rc) channel. ``` |
| `mic-channel-s` | `boolean` | ```text Enable (s) channel. ``` |
| `mic-channel-sl` | `boolean` | ```text Enable (sl) channel. ``` |
| `mic-channel-sr` | `boolean` | ```text Enable (sr) channel. ``` |
| `mic-channel-t` | `boolean` | ```text Enable (t) channel. ``` |
| `mic-channel-cfg` | `boolean` | ```text Enable (cfg) channel. ``` |
| `mic-feature-mute` | `boolean` | ```text Enable Mute feature. ```  This property is **required**. |
| `mic-feature-volume` | `boolean` | ```text Enable Volume feature. Currently not supported. ``` |
| `mic-feature-tone-control` | `boolean` | ```text Enable Tone Control (Bass, Mid, Treble) feature. Currently not supported. ``` |
| `mic-feature-graphic-equalizer` | `boolean` | ```text Enable  Graphic Equalizer feature. Currently not supported. ``` |
| `mic-feature-automatic-gain-control` | `boolean` | ```text Enable Autoamtic Gain Control feature. Currently not supported. ``` |
| `mic-feature-delay` | `boolean` | ```text Enable Delay feature. Currently not supported. ``` |
| `mic-feature-bass-boost` | `boolean` | ```text Enable Bass Boost feature. Currently not supported. ``` |
| `mic-feature-loudness` | `boolean` | ```text Enable Loudness feature. Currently not supported. ``` |
| `hp-channel-l` | `boolean` | ```text Enable (l) channel. ``` |
| `hp-channel-r` | `boolean` | ```text Enable (r) channel. ``` |
| `hp-channel-c` | `boolean` | ```text Enable (c) channel. ``` |
| `hp-channel-lfe` | `boolean` | ```text Enable (lfe) channel. ``` |
| `hp-channel-ls` | `boolean` | ```text Enable (ls) channel. ``` |
| `hp-channel-rs` | `boolean` | ```text Enable (rs) channel. ``` |
| `hp-channel-lc` | `boolean` | ```text Enable (lc) channel. ``` |
| `hp-channel-rc` | `boolean` | ```text Enable (rc) channel. ``` |
| `hp-channel-s` | `boolean` | ```text Enable (s) channel. ``` |
| `hp-channel-sl` | `boolean` | ```text Enable (sl) channel. ``` |
| `hp-channel-sr` | `boolean` | ```text Enable (sr) channel. ``` |
| `hp-channel-t` | `boolean` | ```text Enable (t) channel. ``` |
| `hp-channel-cfg` | `boolean` | ```text Enable (cfg) channel. ``` |
| `hp-feature-mute` | `boolean` | ```text Enable Mute feature. ```  This property is **required**. |
| `hp-feature-volume` | `boolean` | ```text Enable Volume feature. ``` |
| `hp-feature-tone-control` | `boolean` | ```text Enable Tone Control (Bass, Mid, Treble) feature. Currently not supported. ``` |
| `hp-feature-graphic-equalizer` | `boolean` | ```text Enable  Graphic Equalizer feature. Currently not supported. ``` |
| `hp-feature-automatic-gain-control` | `boolean` | ```text Enable Autoamtic Gain Control feature. Currently not supported. ``` |
| `hp-feature-delay` | `boolean` | ```text Enable Delay feature. Currently not supported. ``` |
| `hp-feature-bass-boost` | `boolean` | ```text Enable Bass Boost feature. Currently not supported. ``` |
| `hp-feature-loudness` | `boolean` | ```text Enable Loudness feature. Currently not supported. ``` |
| `volume-max` | `int` | ```text attention: this attribute is a signed value. This attribute represents the maximum volume level. The range from +127.9961 dB (0x7FFF) down to -127.9961 dB (0x8001). Valid range: 0 - 0xFFFF ```  Default value: `2560` |
| `volume-min` | `int` | ```text attention: this attribute is a signed value. This attribute represents the minimum volume level. The range from +127.9961 dB (0x7FFF) down to -127.9961 dB (0x8001). Valid range: 0 - 0xFFFF ```  Default value: `47616` |
| `volume-res` | `int` | ```text attention: this attribute can only take positive values. This attribute represents the volume resolution(step). 1 = 1/256 dB or 0.00390625 dB. 0x100(256) = 1dB. Valid range: 1 - 0x7FFF ```  Default value: `256` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “usb-audio-hs” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
