---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/waveshare_epaper/doc/index.html
original_path: boards/shields/waveshare_epaper/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# WAVESHARE e-Paper Raw Panel Shield

## Overview

The WAVESHARE e-Paper Raw Panel Shield is a universal driver shield.
The shield can be used to drive various Electrophoretic (electronic ink)
Display (EPD) with a SPI interface.
This shield includes a 23LC1024 1Mb SPI Serial SRAM that is
not currently supported by the Zephyr RTOS.

More information about the shield can be found
at the [Universal e-Paper Raw Panel Driver Shield website](https://www.waveshare.com/e-paper-shield.htm) [[1]](#id2).

### Pins Assignment of the e-Paper Shield

| Shield Connector Pin | Function |  |
| --- | --- | --- |
| D5 | RAM CSn | RAM Chip Select |
| D6 | SD CSn | EPD SD Card Chip Select |
| D7 | EPD BUSY | EPD Busy Output |
| D8 | EPD RESETn | EPD Reset Input |
| D9 | EPD DC | EPD Data/Command Input |
| D10 | EPD CSn | EPD Chip Select Input |
| D11 | SPI MOSI | Serial Data Input |
| D12 | SPI MISO | Serial Data Out |
| D13 | SPI SCK | Serial Clock Input |

### Current supported displays

| Display | Ribbon Cable Label | Controller / Driver | Shield Designation |
| --- | --- | --- | --- |
| Good Display GDEH0213B1 | HINK-E0213 | SSD1673 / ssd16xx | waveshare\_epaper\_gdeh0213b1 |
| Good Display GDEH0213B72 | HINK-E0213A22 | SSD1675A / ssd16xx | waveshare\_epaper\_gdeh0213b72 |
| Good Display GDEH029A1 | E029A01 | SSD1608 / ssd16xx | waveshare\_epaper\_gdeh029a1 |
| Good Display GDEW075T7 | WFT0583CZ61 | UC8179 / gd7965 | waveshare\_epaper\_gdew075t7 |
| Good Display GDEH0154D67 | HINK-E0154A07 | SSD1681 / ssd16xx | waveshare\_epaper\_gdeh0154a07 |
| Good Display GDEW042T2 | WFT0420CZ15 | UC8176 / gd7965 | waveshare\_epaper\_gdew042t2 waveshare\_epaper\_gdew042t2-p |

## Requirements

This shield can only be used with a board that provides a configuration
for Arduino connectors and defines node aliases for SPI and GPIO interfaces
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Correct shield designation (see the table above) for your display must
be entered when you invoke `west build`.
For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk_nrf52840 samples/subsys/display/lvgl -- -DSHIELD=waveshare_epaper_gdeh0213b1
```

## References

[[1](#id3)]

[https://www.waveshare.com/e-paper-shield.htm](https://www.waveshare.com/e-paper-shield.htm)
