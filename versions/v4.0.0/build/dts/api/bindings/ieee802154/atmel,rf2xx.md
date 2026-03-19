---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/ieee802154/atmel,rf2xx.html
original_path: build/dts/api/bindings/ieee802154/atmel,rf2xx.html
---

# atmel,rf2xx (on spi bus)

Vendor: [Atmel Corporation](../../bindings.md#dt-vendor-atmel)

Note

An implementation of a driver matching this compatible is available in
[drivers/ieee802154/ieee802154\_rf2xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/ieee802154_rf2xx.c).

## Description

```text
ATMEL AT86RF2xx 802.15.4 wireless transceiver
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `irq-gpios` | `phandle-array` | This property is **required**. |
| `reset-gpios` | `phandle-array` | This property is **required**. |
| `slptr-gpios` | `phandle-array` | ```text Multi-functional pin that controls sleep, deep sleep, transmit start and receive states ```  This property is **required**. |
| `dig2-gpios` | `phandle-array` | ```text RX and TX Frame Time Stamping(TX_ARET) ``` |
| `clkm-gpios` | `phandle-array` | ```text Master clock signal output ``` |
| `local-mac-address` | `uint8-array` | ```text Specifies the MAC address that was assigned to the network device ``` |
| `channel-page` | `int` | ```text Selects Channel Page accordingly with IEEE 802.15.4 standard. The Page 0 is used in both Sub-Giga and 2.4GHz. It allows select channels 0-10 in Sub-Giga band (0: BPSK-20, 1-10: BPSK-40) and 11-26 in 2.4GHz band (11-26: O-QPSK-250). Channel 2 is for Sub-Giga and selects (0: OQPSK-SIN-RC-100, 1-10: OQPSK-SIN-250). Channel 5 is for Sub-Giga (JAPAN) and selects (0-3: OQPSK-RC-250) .   0: Page 0 - BPSK-20 [0], BPSK-40 [1-10], O-QPSK-250 [11-26].   2: Page 2 - OQPSK-SIN-RC-100 [0], OQPSK-SIN-250 [1-10].   5: Page 5 - OQPSK-RC-250 [0-3]. ```  Legal values: `0`, `2`, `5` |
| `tx-pwr-table` | `uint8-array` | ```text This is the Transmission Power Mapping Table array used to comply with local regulations. By default this value set an output power above 0dBm for all transceivers. This property must be used with tx-pwr-min and tx-pwr-max for normal operations. The number of elements is defined by the size of the tx-pwr-table array property. The max entry value for 2.4GHz is 0x0f and 0xff for Sub-Giga. See PHY_TX_PWR at datasheet for more details.  The output power is determined by following formula:    linear_step = (tx-pwr-max - tx-pwr-min)               / (sizeof(tx-pwr-table) - 1.0);   table_index = abs((value_in_dbm - tx-pwr-max) / linear_step);   output_power = tx-pwr-table[table_index];  Using AT86RF233 as example without external PA. By the datasheet the tx-pwr-min = -17 dBm and tx-pwr-max = +4 dBm. Using 48 elements in the tx-pwr-table array. The table array is filled from higher to lower power.    tx-pwr-min = [01 11]; /* -17.0 dBm */   tx-pwr-max = [00 04]; /*   4.0 dBm */   tx-pwr-table = [00 01 03 04 05 05 06 06                   07 07 07 08 08 09 09 0a                   0a 0a 0b 0b 0b 0b 0c 0c                   0c 0c 0d 0d 0d 0d 0d 0d                   0d 0d 0e 0e 0e 0e 0e 0e                   0e 0e 0e 0e 0e 0e 0f 0f];  The values in the table are filled based on table 9-9 [TX Output Power] using the linear step in dBm as:    linear_step = (4 - (-17)) / (48 - 1) => ~0.45 dBm  Assuming that user wants set 0 dBm as output power:    table_index = abs((0 - 4) / 0.45) => 8.95 ( round to 9 )   output_power = tx-pwr-table[9] => 0x07 ( 0 dBm as table 9-9 )  Note when tx-pwr-min is [0x00, 0x00] and tx-pwr-max is [0x00, 0x00] the linear step is zero. This means that table_index will be always the first element of the tx-pwr-table array, which is 0x00 by default. This is defined as general case when user not define any tx-pwr-* entries. It sets the transceiver to use always a value above 0 dBm as output power. ```  Default value: `[0]` |
| `tx-pwr-min` | `uint8-array` | ```text This value represent minimum normalized value in dBm for the transceiver output power. This property must be used when tx-pwr-table is defined. The value is represented by two entries where first element represents the signal indication [0x00-positive, 0x01-negative] and second element is the minimal value in dBm for the transceiver output power. By default, the combination of tx-pwr-min as [0x00, 0x00] and tx-pwr-max as [0x00, 0x00] will create a fixed transmission power. ```  Default value: `[0, 0]` |
| `tx-pwr-max` | `uint8-array` | ```text This value represent maximum normalized value in dBm for the transceiver output power. This property must be used when tx-pwr-table is defined. The value is represented by two entries where first element represents the signal indication [ 0x00-positive] and second element is the maximum value in dBm for the transceiver output power. By default, the combination of tx-pwr-max as [0x00, 0x00] and tx-pwr-min as [0x00, 0x00] will create a fixed transmission power. ```  Default value: `[0, 0]` |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “atmel,rf2xx” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
