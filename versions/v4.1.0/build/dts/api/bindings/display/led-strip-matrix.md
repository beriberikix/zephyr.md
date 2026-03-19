---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/display/led-strip-matrix.html
original_path: build/dts/api/bindings/display/led-strip-matrix.html
---

# led-strip-matrix

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

Note

An implementation of a driver matching this compatible is available in
[drivers/display/display\_led\_strip\_matrix.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/display_led_strip_matrix.c).

## Description

```text
Generic LED strip matrix (LED strip arranged in a grid pattern)
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `circulative` | `boolean` | ```text Use a circulative layout that returns to the left edge of the next row after reaching the right edge. If not set, turn around and go left in a serpentine layout when it reaches the right edge.  * circulative layout   [ 0][ 1][ 2][ 3]   [ 4][ 5][ 6][ 7]   [ 8][ 9][10][11]   [12][13][14][15]  * serpentine layout   [ 0][ 1][ 2][ 3]   [ 7][ 6][ 5][ 4]   [ 8][ 9][10][11]   [15][14][13][12] ``` |
| `start-from-right` | `boolean` | ```text Specify if the first LED is at the right.  * Start from the right with a serpentine layout   [ 3][ 2][ 1][ 0]   [ 4][ 5][ 6][ 7]   [11][10][ 9][ 8]   [12][13][14][15]  * Start from the right with a circulative layout   [ 3][ 2][ 1][ 0]   [ 7][ 6][ 5][ 4]   [11][10][ 9][ 8]   [15][14][13][12] ``` |
| `start-from-bottom` | `boolean` | ```text Specify if the first LED is at the bottom.  * Start from the bottom with a circulative layout   [12][13][14][15]   [ 8][ 9][10][11]   [ 4][ 5][ 6][ 7]   [ 0][ 1][ 2][ 3]  * Start from the bottom with a serpentine layout   [15][14][13][12]   [ 8][ 9][10][11]   [ 7][ 6][ 5][ 4]   [ 0][ 1][ 2][ 3] ``` |
| `width` | `int` | ```text Specifies the overall width of the matrix. If the matrix consists of multiple modules, it is the sum of their widths. ```  This property is **required**. |
| `height` | `int` | ```text Specifies the overall height of the matrix. If the matrix consists of multiple modules, it is the sum of their heights. ```  This property is **required**. |
| `horizontal-modules` | `int` | ```text If the display forms with multiple modules, specify the horizontal number of modules. The number must be able to divide the width value. If not set, it controls a single matrix.  * 8x4 display with 2 serpentine layout modules   [ 0][ 1][ 2][ 3]  [16][17][18][19]   [ 7][ 6][ 5][ 4]  [23][22][21][20]   [ 8][ 9][10][11]  [24][25][26][27]   [15][14][13][12]  [31][30][29][28] ```  Default value: `1` |
| `vertical-modules` | `int` | ```text If the display forms with multiple modules, specify the vertical number of modules. The number must be able to divide the height value. If not set, it controls a single matrix.  * 4x8 display with 2 serpentine layout modules   [ 0][ 1][ 2][ 3]   [ 7][ 6][ 5][ 4]   [ 8][ 9][10][11]   [15][14][13][12]    [16][17][18][19]   [23][22][21][20]   [24][25][26][27]   [31][30][29][28] ```  Default value: `1` |
| `modules-circulative` | `boolean` | ```text Specifies that the order of the modules that make up the matrix is circulative.  * circulative module layout   [M0][M1][M2]   [M3][M4][M5]   [M6][M7][M8]  * serpentine module layout   [M0][M1][M2]   [M5][M4][M3]   [M6][M7][M8] ``` |
| `modules-start-from-right` | `boolean` | ```text Specifies that modules are ordered from right to left.  * Start from the right with a module serpentine layout   [M2][M1][M0]   [M3][M4][M5]   [M8][M7][M6]  * Start from the right with a module circulative layout   [M2][M1][M0]   [M5][M4][M3]   [M8][M7][M6] ``` |
| `modules-start-from-bottom` | `boolean` | ```text Specifies that modules are ordered from bottom to top.  * Start from the right with a module serpentine layout   [M6][M7][M8]   [M5][M4][M3]   [M0][M1][M2]  * Start from the right with a module circulative layout   [M6][M7][M8]   [M3][M4][M5]   [M0][M1][M2] ``` |
| `led-strips` | `phandles` | ```text Specify the LED strip that is the substance of the matrix. If multiple strips are specified, they are "flattened" and sequentialized. For example, if `strip0` and `strip1` with 128 LEDs are specified, the first LED of `strip1` will be treated as the 129th LED. These LEDs are mapped to coordinates according to the layout rule in order. The amount of LEDs must equal the [width * height] value. ```  This property is **required**. |
| `chain-lengths` | `array` | ```text Specify the number of LEDs for each strip. It can omit the value if all strip nodes have a `chain-length` property. Each value must be a multiple of the number of LEDs per module [(width / horizontal-modules) * (height / vertical-modules)]. ``` |
| `pixel-format` | `int` | ```text Initial Pixel format. See dt-bindings/display/panel.h for a list. This property only accepts PANEL_PIXEL_FORMAT_RGB_888 and PANEL_PIXEL_FORMAT_RRGB_8888. If this property is not set, use PANEL_PIXEL_FORMAT_RGB_888 as a default. ```  Default value: `1` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “led-strip-matrix” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `dmas` | `phandle-array` | ```text DMA channel specifiers relevant to the device. ``` |
| `dma-names` | `string-array` | ```text Optional names given to the DMA channel specifiers in the "dmas" property. ``` |
| `io-channels` | `phandle-array` | ```text IO channel specifiers relevant to the device. ``` |
| `io-channel-names` | `string-array` | ```text Optional names given to the IO channel specifiers in the "io-channels" property. ``` |
| `mboxes` | `phandle-array` | ```text Mailbox / IPM channel specifiers relevant to the device. ``` |
| `mbox-names` | `string-array` | ```text Optional names given to the mbox specifiers in the "mboxes" property. ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers relevant to the device. ``` |
| `power-domain-names` | `string-array` | ```text Optional names given to the power domain specifiers in the "power-domains" property. ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
