---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/rk055hdmipi4ma0/doc/index.html
original_path: boards/shields/rk055hdmipi4ma0/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# RK055HDMIPI4MA0 MIPI Display

## Overview

The Rocktech RK055HDMIPI4MA0 MIPI Display is a 5.5 inch TFT 720x1280 pixels
panel with LED backlighting, full viewing angle, MIPI interface and
capacitive touch panel from Rocktech.

More information about the shield can be found
at the [RK055HDMIPI4MA0 product page](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0) [[1]](#id1).

This display uses a 40 pin FPC interface, which is available on many
NXP EVKs.

### Pins Assignment of the Rocktech RK055HDMIPI4MA0 MIPI Display

| FPC Connector Pin | Function |
| --- | --- |
| 1 | LED backlight cathode |
| 21 | Controller reset |
| 22 | Controller LPTE |
| 26 | Touch ctrl I2C SDA |
| 27 | Touch ctrl I2C SCL |
| 28 | Touch ctrl reset |
| 29 | Touch ctrl interrupt |
| 32 | LCD power enable |
| 34 | Backlight power enable |

## Requirements

This shield can only be used with a board which provides a configuration
for the 40 pin FPC interface

## Programming

Set `-DSHIELD=rk055hdmipi4ma0` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b mixmrt1170_evk_cm7 samples/drivers/display -- -DSHIELD=rk055hdmipi4ma0
```

## References

[[1](#id2)]

[https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0)
