---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/gpio/adi,sdp-120.html
original_path: build/dts/api/bindings/gpio/adi,sdp-120.html
---

# adi,sdp-120

Vendor: [Analog Devices, Inc.](../../bindings.md#dt-vendor-adi)

## Description

```text
GPIO pins exposed on a Analog devices SDP interface.

120-pin SDP interface:

     1  VIN                                NC  120
     2  NC                                 NC  119
     3  GND                               GND  118
     4  GND                               GND  117
     5  USB_VBUS                          VIO  116
     6  GND                               GND  115
     7  PAR_D23                       PAR_D22  114
     8  PAR_D21                       PAR_D20  113
     9  PAR_D19                       PAR_D18  112
    10  PAR_D17                       PAR_D16  111
    11  GND                           PAR_D15  110
    12  PAR_D14                           GND  109
    13  PAR_D13                       PAR_D12  108
    14  PAR_D11                       PAR_D10  107
    15  PAR_D9                         PAR_D8  106
    16  PAR_D7                         PAR_D6  105
    17  GND                               GND  104
    18  PAR_D5                         PAR_D4  103
    19  PAR_D3                         PAR_D2  102
    20  PAR_D1                         PAR_D0  101
    21  PAR_RD_N                     PAR_WR_N  100
    22  PAR_CS_N                      PAR_INT  99
    23  GND                               GND  98
    24  PAR_A3                         PAR_A2  97
    25  PAR_A1                         PAR_A0  96
    26  PAR_FS3                       PAR_FS2  95
    27  PAR_FS1                       PAR_CLK  94
    28  GND                               GND  93
    29  SPORT_TDV0                SPORT_RSCLK  92
    30  SPORT_TDV1                  SPORT_DR0  91
    31  SPORT_DR1                   SPORT_RFS  90
    32  SPORT_DT1                   SPORT_TFS  89
    33  SPI_D2                      SPORT_DT0  88
    34  SPI_D3                    SPORT_TSCLK  87
    35  SERIAL_INT                        GND  86
    36  GND                       SPI_SEL_A_N  85
    37  SPI_SEL_B_N                  SPI_MOSI  84
    38  SPI_SEL_C_N                  SPI_MISO  83
    39  SPI_SEL1/SPI_SS_N             SPI_CLK  82
    40  GND                               GND  81
    41  SDA_1                           SDA_0  80
    42  SCL_1                           SCL_0  79
    43  GPIO0                           GPIO1  78
    44  GPIO2                           GPIO3  77
    45  GPIO4                           GPIO5  76
    46  GND                               GND  75
    47  GPIO6                           GPIO7  74
    48  TMR_A                           TMR_B  73
    49  TMR_C                           TMR_D  72
    50  NC                             CLKOUT  71
    51  NC                                 NC  70
    52  GND                               GND  69
    53  NC                                 NC  68
    54  NC                                 NC  67
    55  NC                                 NC  66
    56  EEPROM_A0                      WAKE_N  65
    57  RESET_OUT_N                   SLEEP_N  64
    58  GND                               GND  63
    59  UART_RX                       UART_TX  62
    60  RESET_IN_N                     BMODE1  61
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `gpio-map` | `compound` | This property is **required**. |
| `gpio-map-mask` | `compound` |  |
| `gpio-map-pass-thru` | `compound` |  |
| `#gpio-cells` | `int` | ```text Number of items to expect in a GPIO specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “adi,sdp-120” compatible.

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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
