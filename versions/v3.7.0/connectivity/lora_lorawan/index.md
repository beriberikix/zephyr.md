---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/lora_lorawan/index.html
original_path: connectivity/lora_lorawan/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# LoRa and LoRaWAN

## Overview

LoRa (abbrev. for Long Range) is a proprietary low-power wireless
communication protocol developed by the [Semtech Corporation](https://www.semtech.com/).

LoRa acts as the physical layer (PHY) based on the chirp spread spectrum
(CSS) modulation technique.

LoRaWAN (for Long Range Wide Area Network) defines a networking layer
on top of the LoRa PHY.

Zephyr provides APIs for LoRa to send raw data packets directly over the
wireless interface as well as APIs for LoRaWAN to connect the end device
to the internet through a gateway.

The Zephyr implementation is based on Semtech’s [LoRaMac-node library](https://github.com/Lora-net/LoRaMac-node), which
is included as a Zephyr module.

The LoRaWAN specification is published by the [LoRa Alliance](https://lora-alliance.org/).

## Configuration Options

### LoRa PHY

Related configuration options can be found under
[drivers/lora/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig).

- [`CONFIG_LORA`](../../kconfig.md#CONFIG_LORA "CONFIG_LORA")
- [`CONFIG_LORA_SHELL`](../../kconfig.md#CONFIG_LORA_SHELL "CONFIG_LORA_SHELL")
- [`CONFIG_LORA_INIT_PRIORITY`](../../kconfig.md#CONFIG_LORA_INIT_PRIORITY "CONFIG_LORA_INIT_PRIORITY")

### LoRaWAN

Related configuration options can be found under
[subsys/lorawan/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig).

- [`CONFIG_LORAWAN`](../../kconfig.md#CONFIG_LORAWAN "CONFIG_LORAWAN")
- [`CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR`](../../kconfig.md#CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR "CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR")
- [`CONFIG_LORAMAC_REGION_AS923`](../../kconfig.md#CONFIG_LORAMAC_REGION_AS923 "CONFIG_LORAMAC_REGION_AS923")
- [`CONFIG_LORAMAC_REGION_AU915`](../../kconfig.md#CONFIG_LORAMAC_REGION_AU915 "CONFIG_LORAMAC_REGION_AU915")
- [`CONFIG_LORAMAC_REGION_CN470`](../../kconfig.md#CONFIG_LORAMAC_REGION_CN470 "CONFIG_LORAMAC_REGION_CN470")
- [`CONFIG_LORAMAC_REGION_CN779`](../../kconfig.md#CONFIG_LORAMAC_REGION_CN779 "CONFIG_LORAMAC_REGION_CN779")
- [`CONFIG_LORAMAC_REGION_EU433`](../../kconfig.md#CONFIG_LORAMAC_REGION_EU433 "CONFIG_LORAMAC_REGION_EU433")
- [`CONFIG_LORAMAC_REGION_EU868`](../../kconfig.md#CONFIG_LORAMAC_REGION_EU868 "CONFIG_LORAMAC_REGION_EU868")
- [`CONFIG_LORAMAC_REGION_KR920`](../../kconfig.md#CONFIG_LORAMAC_REGION_KR920 "CONFIG_LORAMAC_REGION_KR920")
- [`CONFIG_LORAMAC_REGION_IN865`](../../kconfig.md#CONFIG_LORAMAC_REGION_IN865 "CONFIG_LORAMAC_REGION_IN865")
- [`CONFIG_LORAMAC_REGION_US915`](../../kconfig.md#CONFIG_LORAMAC_REGION_US915 "CONFIG_LORAMAC_REGION_US915")
- [`CONFIG_LORAMAC_REGION_RU864`](../../kconfig.md#CONFIG_LORAMAC_REGION_RU864 "CONFIG_LORAMAC_REGION_RU864")

## API Reference

### LoRa PHY

Related code samples

[LoRa receive](../../samples/drivers/lora/receive/README.md#lora-receive "Receive packets in both synchronous and asynchronous mode using the LoRa radio.")
:   Receive packets in both synchronous and asynchronous mode using the LoRa
    radio.

[LoRa send](../../samples/drivers/lora/send/README.md#lora-send "Transmit a preconfigured payload every second using the LoRa radio.")
:   Transmit a preconfigured payload every second using the LoRa radio.

*group* LoRa APIs
:   **Since**
    :   2.2

    **Version**
    :   0.1.0

    Enums

    enum lora\_signal\_bandwidth
    :   LoRa signal bandwidth.

        *Values:*

        enumerator BW\_125\_KHZ = 0

        enumerator BW\_250\_KHZ

        enumerator BW\_500\_KHZ

    enum lora\_datarate
    :   LoRa data-rate.

        *Values:*

        enumerator SF\_6 = 6

        enumerator SF\_7

        enumerator SF\_8

        enumerator SF\_9

        enumerator SF\_10

        enumerator SF\_11

        enumerator SF\_12

    enum lora\_coding\_rate
    :   LoRa coding rate.

        *Values:*

        enumerator CR\_4\_5 = 1

        enumerator CR\_4\_6 = 2

        enumerator CR\_4\_7 = 3

        enumerator CR\_4\_8 = 4

    Functions

    static inline int lora\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [lora\_modem\_config](#c.lora_modem_config) \*config)
    :   Configure the LoRa modem.

        Parameters:
        :   - **dev** – LoRa device
            - **config** – Data structure containing the intended configuration for the modem

        Returns:
        :   0 on success, negative on error

    static inline int lora\_send(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*data, uint32\_t data\_len)
    :   Send data over LoRa.

        Note

        This blocks until transmission is complete.

        Parameters:
        :   - **dev** – LoRa device
            - **data** – Data to be sent
            - **data\_len** – Length of the data to be sent

        Returns:
        :   0 on success, negative on error

    static inline int lora\_send\_async(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*data, uint32\_t data\_len, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*async)
    :   Asynchronously send data over LoRa.

        Note

        This returns immediately after starting transmission, and locks the LoRa modem until the transmission completes.

        Parameters:
        :   - **dev** – LoRa device
            - **data** – Data to be sent
            - **data\_len** – Length of the data to be sent
            - **async** – A pointer to a valid and ready to be signaled struct [k\_poll\_signal](../../kernel/services/polling.md#structk__poll__signal). (Note: if NULL this function will not notify the end of the transmission).

        Returns:
        :   0 on success, negative on error

    static inline int lora\_recv(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*data, uint8\_t size, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout, int16\_t \*rssi, int8\_t \*snr)
    :   Receive data over LoRa.

        Note

        This is a blocking call.

        Parameters:
        :   - **dev** – LoRa device
            - **data** – Buffer to hold received data
            - **size** – Size of the buffer to hold the received data. Max size allowed is 255.
            - **timeout** – Duration to wait for a packet.
            - **rssi** – RSSI of received data
            - **snr** – SNR of received data

        Returns:
        :   Length of the data received on success, negative on error

    static inline int lora\_recv\_async(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, lora\_recv\_cb cb)
    :   Receive data asynchronously over LoRa.

        Receive packets continuously under the configuration previously setup by [lora\_config](#group__lora__api_1gad7c6c516d2d0e023da952666d3f8decb).

        Reception is cancelled by calling this function again with `cb` = NULL. This can be done within the callback handler.

        Parameters:
        :   - **dev** – Modem to receive data on.
            - **cb** – Callback to run on receiving data. If NULL, any pending asynchronous receptions will be cancelled.

        Returns:
        :   0 when reception successfully setup, negative on error

    static inline int lora\_test\_cw(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t frequency, int8\_t tx\_power, uint16\_t duration)
    :   Transmit an unmodulated continuous wave at a given frequency.

        Note

        Only use this functionality in a test setup where the transmission does not interfere with other devices.

        Parameters:
        :   - **dev** – LoRa device
            - **frequency** – Output frequency (Hertz)
            - **tx\_power** – TX power (dBm)
            - **duration** – Transmission duration in seconds.

        Returns:
        :   0 on success, negative on error

    struct lora\_modem\_config
    :   *#include <lora.h>*

        Structure containing the configuration of a LoRa modem.

        Public Members

        uint32\_t frequency
        :   Frequency in Hz to use for transceiving.

        enum [lora\_signal\_bandwidth](#c.lora_signal_bandwidth) bandwidth
        :   The bandwidth to use for transceiving.

        enum [lora\_datarate](#c.lora_datarate) datarate
        :   The data-rate to use for transceiving.

        enum [lora\_coding\_rate](#c.lora_coding_rate) coding\_rate
        :   The coding rate to use for transceiving.

        uint16\_t preamble\_len
        :   Length of the preamble.

        int8\_t tx\_power
        :   TX-power in dBm to use for transmission.

        bool tx
        :   Set to true for transmission, false for receiving.

        bool iq\_inverted
        :   Invert the In-Phase and Quadrature (IQ) signals.

            Normally this should be set to false. In advanced use-cases where a differentation is needed between “uplink” and “downlink” traffic, the IQ can be inverted to create two different channels on the same frequency

        bool public\_network
        :   Sets the sync-byte to use:

            - false: for using the private network sync-byte
            - true: for using the public network sync-byte The public network sync-byte is only intended for advanced usage. Normally the private network sync-byte should be used for peer to peer communications and the LoRaWAN APIs should be used for interacting with a public network.

### LoRaWAN

Related code samples

[LoRaWAN FUOTA](../../samples/subsys/lorawan/fuota/README.md#lorawan-fuota "Perform a LoRaWAN firmware-upgrade over the air (FUOTA) operation.")
:   Perform a LoRaWAN firmware-upgrade over the air (FUOTA) operation.

[LoRaWAN class A device](../../samples/subsys/lorawan/class_a/README.md#lorawan-class-a "Join a LoRaWAN network and send a message periodically.")
:   Join a LoRaWAN network and send a message periodically.

*group* LoRaWAN APIs
:   **Since**
    :   2.5

    **Version**
    :   0.1.0

    Defines

    LW\_RECV\_PORT\_ANY
    :   Flag to indicate receiving on any port.

    Typedefs

    typedef uint8\_t (\*lorawan\_battery\_level\_cb\_t)(void)
    :   Defines the battery level callback handler function signature.

        Retval 0:
        :   if the node is connected to an external power source

        Retval 1..254:
        :   battery level, where 1 is the minimum and 254 is the maximum value

        Retval 255:
        :   if the node was not able to measure the battery level

    typedef void (\*lorawan\_dr\_changed\_cb\_t)(enum [lorawan\_datarate](#c.lorawan_datarate) dr)
    :   Defines the datarate changed callback handler function signature.

        Param dr:
        :   Updated datarate.

    Enums

    enum lorawan\_class
    :   LoRaWAN class types.

        *Values:*

        enumerator LORAWAN\_CLASS\_A = 0x00
        :   Class A device.

        enumerator LORAWAN\_CLASS\_B = 0x01
        :   Class B device.

        enumerator LORAWAN\_CLASS\_C = 0x02
        :   Class C device.

    enum lorawan\_act\_type
    :   LoRaWAN activation types.

        *Values:*

        enumerator LORAWAN\_ACT\_OTAA = 0
        :   Over-the-Air Activation (OTAA).

        enumerator LORAWAN\_ACT\_ABP
        :   Activation by Personalization (ABP).

    enum lorawan\_channels\_mask\_size
    :   LoRaWAN channels mask sizes.

        *Values:*

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_AS923 = 1
        :   Region AS923 mask size.

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_AU915 = 6
        :   Region AU915 mask size.

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_CN470 = 6
        :   Region CN470 mask size.

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_CN779 = 1
        :   Region CN779 mask size.

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_EU433 = 1
        :   Region EU433 mask size.

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_EU868 = 1
        :   Region EU868 mask size.

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_KR920 = 1
        :   Region KR920 mask size.

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_IN865 = 1
        :   Region IN865 mask size.

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_US915 = 6
        :   Region US915 mask size.

        enumerator LORAWAN\_CHANNELS\_MASK\_SIZE\_RU864 = 1
        :   Region RU864 mask size.

    enum lorawan\_datarate
    :   LoRaWAN datarate types.

        *Values:*

        enumerator LORAWAN\_DR\_0 = 0
        :   DR0 data rate.

        enumerator LORAWAN\_DR\_1
        :   DR1 data rate.

        enumerator LORAWAN\_DR\_2
        :   DR2 data rate.

        enumerator LORAWAN\_DR\_3
        :   DR3 data rate.

        enumerator LORAWAN\_DR\_4
        :   DR4 data rate.

        enumerator LORAWAN\_DR\_5
        :   DR5 data rate.

        enumerator LORAWAN\_DR\_6
        :   DR6 data rate.

        enumerator LORAWAN\_DR\_7
        :   DR7 data rate.

        enumerator LORAWAN\_DR\_8
        :   DR8 data rate.

        enumerator LORAWAN\_DR\_9
        :   DR9 data rate.

        enumerator LORAWAN\_DR\_10
        :   DR10 data rate.

        enumerator LORAWAN\_DR\_11
        :   DR11 data rate.

        enumerator LORAWAN\_DR\_12
        :   DR12 data rate.

        enumerator LORAWAN\_DR\_13
        :   DR13 data rate.

        enumerator LORAWAN\_DR\_14
        :   DR14 data rate.

        enumerator LORAWAN\_DR\_15
        :   DR15 data rate.

    enum lorawan\_region
    :   LoRaWAN region types.

        *Values:*

        enumerator LORAWAN\_REGION\_AS923
        :   Asia 923 MHz frequency band.

        enumerator LORAWAN\_REGION\_AU915
        :   Australia 915 MHz frequency band.

        enumerator LORAWAN\_REGION\_CN470
        :   China 470 MHz frequency band.

        enumerator LORAWAN\_REGION\_CN779
        :   China 779 MHz frequency band.

        enumerator LORAWAN\_REGION\_EU433
        :   Europe 433 MHz frequency band.

        enumerator LORAWAN\_REGION\_EU868
        :   Europe 868 MHz frequency band.

        enumerator LORAWAN\_REGION\_KR920
        :   South Korea 920 MHz frequency band.

        enumerator LORAWAN\_REGION\_IN865
        :   India 865 MHz frequency band.

        enumerator LORAWAN\_REGION\_US915
        :   United States 915 MHz frequency band.

        enumerator LORAWAN\_REGION\_RU864
        :   Russia 864 MHz frequency band.

    enum lorawan\_message\_type
    :   LoRaWAN message types.

        *Values:*

        enumerator LORAWAN\_MSG\_UNCONFIRMED = 0
        :   Unconfirmed message.

        enumerator LORAWAN\_MSG\_CONFIRMED
        :   Confirmed message.

    Functions

    void lorawan\_register\_battery\_level\_callback([lorawan\_battery\_level\_cb\_t](#c.lorawan_battery_level_cb_t) cb)
    :   Register a battery level callback function.

        Provide the LoRaWAN stack with a function to be called whenever a battery level needs to be read.

        Should no callback be provided the lorawan backend will report 255.

        Parameters:
        :   - **cb** – Pointer to the battery level function

    void lorawan\_register\_downlink\_callback(struct [lorawan\_downlink\_cb](#c.lorawan_downlink_cb) \*cb)
    :   Register a callback to be run on downlink packets.

        Parameters:
        :   - **cb** – Pointer to structure containing callback parameters

    void lorawan\_register\_dr\_changed\_callback([lorawan\_dr\_changed\_cb\_t](#c.lorawan_dr_changed_cb_t) cb)
    :   Register a callback to be called when the datarate changes.

        The callback is called once upon successfully joining a network and again each time the datarate changes due to ADR.

        Parameters:
        :   - **cb** – Pointer to datarate update callback

    int lorawan\_join(const struct [lorawan\_join\_config](#c.lorawan_join_config) \*config)
    :   Join the LoRaWAN network.

        Join the LoRaWAN network using OTAA or AWB.

        Parameters:
        :   - **config** – Configuration to be used

        Returns:
        :   0 if successful, negative errno code if failure

    int lorawan\_start(void)
    :   Start the LoRaWAN stack.

        This function need to be called before joining the network.

        Returns:
        :   0 if successful, negative errno code if failure

    int lorawan\_send(uint8\_t port, uint8\_t \*data, uint8\_t len, enum [lorawan\_message\_type](#c.lorawan_message_type) type)
    :   Send data to the LoRaWAN network.

        Send data to the connected LoRaWAN network.

        Parameters:
        :   - **port** – Port to be used for sending data. Must be set if the payload is not empty.
            - **data** – Data buffer to be sent
            - **len** – Length of the buffer to be sent. Maximum length of this buffer is 255 bytes but the actual payload size varies with region and datarate.
            - **type** – Specifies if the message shall be confirmed or unconfirmed. Must be one of [lorawan\_message\_type](#group__lorawan__api_1ga5d78efba3f8e62ccd6317aed8af4bc54).

        Returns:
        :   0 if successful, negative errno code if failure

    int lorawan\_set\_class(enum [lorawan\_class](#c.lorawan_class) dev\_class)
    :   Set the current device class.

        Change the current device class. This function may be called before or after a network connection has been established.

        Parameters:
        :   - **dev\_class** – New device class

        Returns:
        :   0 if successful, negative errno code if failure

    int lorawan\_set\_conf\_msg\_tries(uint8\_t tries)
    :   Set the number of tries used for transmissions.

        Parameters:
        :   - **tries** – Number of tries to be used

        Returns:
        :   0 if successful, negative errno code if failure

    void lorawan\_enable\_adr(bool enable)
    :   Enable Adaptive Data Rate (ADR).

        Control whether adaptive data rate (ADR) is enabled. When ADR is enabled, the data rate is treated as a default data rate that will be used if the ADR algorithm has not established a data rate. ADR should normally only be enabled for devices with stable RF conditions (i.e., devices in a mostly static location).

        Parameters:
        :   - **enable** – Enable or Disable adaptive data rate.

    int lorawan\_set\_channels\_mask(uint16\_t \*channels\_mask, size\_t channels\_mask\_size)
    :   Set the channels mask.

        Change the default channels mask. When mask is not changed, all the channels can be used for data transmission. Some Network Servers don’t use all the channels, in this case, the channels mask must be provided.

        Parameters:
        :   - **channels\_mask** – Buffer with channels mask to be used.
            - **channels\_mask\_size** – Size of channels mask buffer.

        Return values:
        :   - **0** – successful
            - **-EINVAL** – channels mask or channels mask size is wrong

    int lorawan\_set\_datarate(enum [lorawan\_datarate](#c.lorawan_datarate) dr)
    :   Set the default data rate.

        Change the default data rate.

        Parameters:
        :   - **dr** – Data rate used for transmissions

        Returns:
        :   0 if successful, negative errno code if failure

    enum [lorawan\_datarate](#c.lorawan_datarate) lorawan\_get\_min\_datarate(void)
    :   Get the minimum possible datarate.

        The minimum possible datarate may change in response to a TxParamSetupReq command from the network server.

        Returns:
        :   Minimum possible data rate

    void lorawan\_get\_payload\_sizes(uint8\_t \*max\_next\_payload\_size, uint8\_t \*max\_payload\_size)
    :   Get the current payload sizes.

        Query the current payload sizes. The maximum payload size varies with datarate, while the current payload size can be less due to MAC layer commands which are inserted into uplink packets.

        Parameters:
        :   - **max\_next\_payload\_size** – Maximum payload size for the next transmission
            - **max\_payload\_size** – Maximum payload size for this datarate

    int lorawan\_set\_region(enum [lorawan\_region](#c.lorawan_region) region)
    :   Set the region and frequency to be used.

        Control the LoRa region and frequency settings. This should be called before *[lorawan\_start()](#group__lorawan__api_1ga640d93930e09327ee87563597f919725)*. If you only have support for a single region selected via Kconfig, this function does not need to be called at all.

        Parameters:
        :   - **region** – The region to be selected

        Returns:
        :   0 if successful, negative errno otherwise

    struct lorawan\_join\_otaa
    :   *#include <lorawan.h>*

        LoRaWAN join parameters for over-the-Air activation (OTAA).

        Note that all of the fields use LoRaWAN 1.1 terminology.

        All parameters are optional if a secure element is present in which case the values stored in the secure element will be used instead.

        Public Members

        uint8\_t \*join\_eui
        :   Join EUI.

        uint8\_t \*nwk\_key
        :   Network Key.

        uint8\_t \*app\_key
        :   Application Key.

        uint16\_t dev\_nonce
        :   Device Nonce.

            Starting with LoRaWAN 1.0.4 the DevNonce must be monotonically increasing for each OTAA join with the same EUI. The DevNonce should be stored in non-volatile memory by the application.

    struct lorawan\_join\_abp
    :   *#include <lorawan.h>*

        LoRaWAN join parameters for activation by personalization (ABP).

        Public Members

        uint32\_t dev\_addr
        :   Device address on the network.

        uint8\_t \*app\_skey
        :   Application session key.

        uint8\_t \*nwk\_skey
        :   Network session key.

        uint8\_t \*app\_eui
        :   Application EUI.

    struct lorawan\_join\_config
    :   *#include <lorawan.h>*

        LoRaWAN join parameters.

        Public Members

        struct [lorawan\_join\_otaa](#c.lorawan_join_otaa) otaa
        :   OTAA join parameters.

        struct [lorawan\_join\_abp](#c.lorawan_join_abp) abp
        :   ABP join parameters.

        union [lorawan\_join\_config](#c.lorawan_join_config).[anonymous] [anonymous]
        :   Join parameters.

        uint8\_t \*dev\_eui
        :   Device EUI.

            Optional if a secure element is present.

        enum [lorawan\_act\_type](#c.lorawan_act_type) mode
        :   Activation mode.

    struct lorawan\_downlink\_cb
    :   *#include <lorawan.h>*

        LoRaWAN downlink callback parameters.

        Public Members

        uint16\_t port
        :   Port to handle messages for.

            - Port 0: TX packet acknowledgements
            - Ports 1-255: Standard downlink port
            - LW\_RECV\_PORT\_ANY: All downlinks

        void (\*cb)(uint8\_t port, bool data\_pending, int16\_t rssi, int8\_t snr, uint8\_t len, const uint8\_t \*data)
        :   Callback function to run on downlink data.

            Note

            Callbacks are run on the system workqueue, and should therefore be as short as possible.

            Param port:
            :   Port message was sent on

            Param data\_pending:
            :   Network server has more downlink packets pending

            Param rssi:
            :   Received signal strength in dBm

            Param snr:
            :   Signal to Noise ratio in dBm

            Param len:
            :   Length of data received, will be 0 for ACKs

            Param data:
            :   Data received, will be NULL for ACKs

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Node for callback list.
