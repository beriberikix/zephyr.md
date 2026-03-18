---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/display/panel/panel-timing.html
original_path: build/dts/api/bindings/display/panel/panel-timing.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,panel-timing

Vendor: [Zephyr-specific binding](../../../bindings.md#dt-vendor-zephyr)

## Description

```text
Common timing settings for display panels. These timings can be added to
a panel under display-timings node. For example:

&lcdif {
  display-timings {
    compatible = "zephyr,panel-timing";
    hsync-len = <8>;
    hfront-porch = <32>;
    hback-porch = <32>;
    vsync-len = <2>;
    vfront-porch = <16>;
    vback-porch = <14>;
    hsync-active = <0>;
    vsync-active = <0>;
    de-active = <1>;
    pixelclk-active = <0>;
    clock-frequency = <62346240>;
  };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text Pixel clock for display controller in Hz. Must be at least as large as: (height + vsync-len + vfront-porch + vback-porch) * (width + hsync-len + hfront-porch + hback-porch) * desired frame rate ``` |
| `hsync-len` | `int` | ```text Horizontal synchronization pulse duration of panel driven by this controller, in pixels ```  This property is **required**. |
| `vsync-len` | `int` | ```text Vertical synchronization pulse duration of panel driven by this controller, in lines ```  This property is **required**. |
| `hback-porch` | `int` | ```text Horizontal back porch duration of panel driven by this controller, in pixels ```  This property is **required**. |
| `vback-porch` | `int` | ```text Vertical back porch duration of panel driven by this controller, in lines ```  This property is **required**. |
| `hfront-porch` | `int` | ```text Horizontal front porch duration of panel driven by this controller, in pixels ```  This property is **required**. |
| `vfront-porch` | `int` | ```text Vertical front porch duration of panel driven by this controller, in lines ```  This property is **required**. |
| `hsync-active` | `int` | ```text Polarity of horizontal sync pulse 0 selects active low 1 selects active high ```  This property is **required**.  Legal values: `0`, `1` |
| `vsync-active` | `int` | ```text Polarity of vertical sync pulse 0 selects active low 1 selects active high ```  This property is **required**.  Legal values: `0`, `1` |
| `de-active` | `int` | ```text Polarity of data enable, sent with each horizontal interval. 0 selects active low 1 selects active high. ```  This property is **required**.  Legal values: `0`, `1` |
| `pixelclk-active` | `int` | ```text Polarity of pixel clock. Selects which edge to drive data to display on. 0 drives pixel data on falling edge, and samples on rising edge. 1 drives pixel data on rising edge, and samples data on falling edge ```  This property is **required**.  Legal values: `0`, `1` |
| `syncclk-active` | `int` | ```text Drive sync on rising or sample sync on falling edge. If not specified then the controller uses the setup specified by pixelclk-active. Use 0 to drive sync on falling edge and sample sync on rising edge of pixel clock. Use 1 to drive sync on rising edge and sample sync on falling edge of pixel clock. ```  Legal values: `0`, `1` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,panel-timing” compatible.

(None)
