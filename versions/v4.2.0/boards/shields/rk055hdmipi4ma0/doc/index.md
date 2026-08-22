---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/rk055hdmipi4ma0/doc/index.html
original_path: boards/shields/rk055hdmipi4ma0/doc/index.html
---

# NXP RK055HDMIPI4MA0 MIPI Display

## Overview

The Rocktech RK055HDMIPI4MA0 MIPI Display is a 5.5 inch TFT 720x1280 pixels
panel with LED backlighting, full viewing angle, MIPI interface and
capacitive touch panel from Rocktech.

More information about the shield can be found
at the [RK055HDMIPI4MA0 product page](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0) [[8]](#id15).

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

Set `--shield rk055hdmipi4ma0` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b mixmrt1170_evk_cm7 --shield rk055hdmipi4ma0 samples/drivers/display
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk) [[1]](#id1)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC) [[2]](#id3), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) [[3]](#id5) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started) [[4]](#id7)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548) [[5]](#id9)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) [[6]](#id11) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project) [[7]](#id13)

## References

[[1](#id2)]

[https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

[[2](#id4)]

[https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC)

[[3](#id6)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki)

[[4](#id8)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)

[[5](#id10)]

[https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

[[6](#id12)]

[https://nxp.com/zephyr](https://nxp.com/zephyr)

[[7](#id14)]

[https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

[[8](#id16)]

[https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/5-5-lcd-panel:RK055HDMIPI4MA0)
