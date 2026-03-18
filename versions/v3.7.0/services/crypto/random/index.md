---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/crypto/random/index.html
original_path: services/crypto/random/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Random Number Generation

The random API subsystem provides random number generation APIs in both
cryptographically and non-cryptographically secure instances. Which
random API to use is based on the cryptographic requirements of the
random number. The non-cryptographic APIs will return random values
much faster if non-cryptographic values are needed.

The cryptographically secure random functions shall be compliant to the
FIPS 140-2 [[NIST02]](../../../security/security-citations.md#nist02) recommended algorithms. Hardware based random-number
generators (RNG) can be used on platforms with appropriate hardware support.
Platforms without hardware RNG support shall use the [CTR-DRBG algorithm](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf).
The algorithm can be provided by [TinyCrypt](https://01.org/tinycrypt)
or [mbedTLS](https://tls.mbed.org/ctr-drbg-source-code) depending on
your application performance and resource requirements.

> Note
>
> The CTR-DRBG generator needs an entropy source to establish and
> maintain the cryptographic security of the PRNG.

## Kconfig Options

These options can be found in the following path [subsys/random/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig).

[`CONFIG_TEST_RANDOM_GENERATOR`](../../../kconfig.md#CONFIG_TEST_RANDOM_GENERATOR "CONFIG_TEST_RANDOM_GENERATOR")
:   For testing, this option allows a non-random number generator to be used and
    permits random number APIs to return values that are not truly random.

The random number generator choice group allows selection of the RNG
source function for the system via the RNG\_GENERATOR\_CHOICE choice group.
An override of the default value can be specified in the SOC or board
.defconfig file by using:

```text
choice RNG_GENERATOR_CHOICE
        default XOSHIRO_RANDOM_GENERATOR
endchoice
```

The random number generators available include:

[`CONFIG_TIMER_RANDOM_GENERATOR`](../../../kconfig.md#CONFIG_TIMER_RANDOM_GENERATOR "CONFIG_TIMER_RANDOM_GENERATOR")
:   enables number generator based on system timer clock. This number
    generator is not random and used for testing only.

[`CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR`](../../../kconfig.md#CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR "CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR")
:   enables a random number generator that uses the enabled hardware
    entropy gathering driver to generate random numbers.

[`CONFIG_XOSHIRO_RANDOM_GENERATOR`](../../../kconfig.md#CONFIG_XOSHIRO_RANDOM_GENERATOR "CONFIG_XOSHIRO_RANDOM_GENERATOR")
:   enables the Xoshiro128++ pseudo-random number generator, that uses the
    entropy driver as a seed source.

The CSPRNG\_GENERATOR\_CHOICE choice group provides selection of the
cryptographically secure random number generator source function. An
override of the default value can be specified in the SOC or board
.defconfig file by using:

```text
choice CSPRNG_GENERATOR_CHOICE
        default CTR_DRBG_CSPRNG_GENERATOR
endchoice
```

The cryptographically secure random number generators available include:

[`CONFIG_HARDWARE_DEVICE_CS_GENERATOR`](../../../kconfig.md#CONFIG_HARDWARE_DEVICE_CS_GENERATOR "CONFIG_HARDWARE_DEVICE_CS_GENERATOR")
:   enables a cryptographically secure random number generator using the
    hardware random generator driver

[`CONFIG_CTR_DRBG_CSPRNG_GENERATOR`](../../../kconfig.md#CONFIG_CTR_DRBG_CSPRNG_GENERATOR "CONFIG_CTR_DRBG_CSPRNG_GENERATOR")
:   enables the CTR-DRBG pseudo-random number generator. The CTR-DRBG is
    a FIPS140-2 recommended cryptographically secure random number generator.

Personalization data can be provided in addition to the entropy source
to make the initialization of the CTR-DRBG as unique as possible.

[`CONFIG_CS_CTR_DRBG_PERSONALIZATION`](../../../kconfig.md#CONFIG_CS_CTR_DRBG_PERSONALIZATION "CONFIG_CS_CTR_DRBG_PERSONALIZATION")
:   CTR-DRBG Initialization Personalization string

## API Reference

Related code samples

[AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")
:   Connect to AWS IoT Core and publish messages using MQTT.

[Microsoft Azure IoT Hub MQTT](../../../samples/net/cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.")
:   Connect to Azure IoT Hub and publish messages using MQTT.

*group* Random Function APIs
:   Random Function APIs.

    **Since**
    :   1.0

    **Version**
    :   1.0.0

    Functions

    void sys\_rand\_get(void \*dst, size\_t len)
    :   Fill the destination buffer with random data values that should pass general randomness tests.

        Note

        The random values returned are not considered cryptographically secure random number values.

        Parameters:
        :   - **dst** – **[out]** destination buffer to fill with random data.
            - **len** – size of the destination buffer.

    int sys\_csrand\_get(void \*dst, size\_t len)
    :   Fill the destination buffer with cryptographically secure random data values.

        Note

        If the random values requested do not need to be cryptographically secure then use [sys\_rand\_get()](#group__random__api_1gaf4f6792ac29c876d59ace1deae53bbd7) instead.

        Parameters:
        :   - **dst** – **[out]** destination buffer to fill.
            - **len** – size of the destination buffer.

        Returns:
        :   0 if success, -EIO if entropy reseed error

    static inline uint8\_t sys\_rand8\_get(void)
    :   Return a 8-bit random value that should pass general randomness tests.

        Note

        The random value returned is not a cryptographically secure random number value.

        Returns:
        :   8-bit random value.

    static inline uint16\_t sys\_rand16\_get(void)
    :   Return a 16-bit random value that should pass general randomness tests.

        Note

        The random value returned is not a cryptographically secure random number value.

        Returns:
        :   16-bit random value.

    static inline uint32\_t sys\_rand32\_get(void)
    :   Return a 32-bit random value that should pass general randomness tests.

        Note

        The random value returned is not a cryptographically secure random number value.

        Returns:
        :   32-bit random value.

    static inline uint64\_t sys\_rand64\_get(void)
    :   Return a 64-bit random value that should pass general randomness tests.

        Note

        The random value returned is not a cryptographically secure random number value.

        Returns:
        :   64-bit random value.
