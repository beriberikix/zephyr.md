---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/crypto.html
original_path: connectivity/bluetooth/api/crypto.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Cryptography

## API Reference

*group* bt\_crypto
:   Cryptography.

    Functions

    int bt\_rand(void \*buf, size\_t len)
    :   Generate random data.

        A random number generation helper which utilizes the Bluetooth controller’s own RNG.

        Parameters:
        :   - **buf** – Buffer to insert the random data
            - **len** – Length of random data to generate

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error

    int bt\_encrypt\_le(const uint8\_t key[16], const uint8\_t plaintext[16], uint8\_t enc\_data[16])
    :   AES encrypt little-endian data.

        An AES encrypt helper is used to request the Bluetooth controller’s own hardware to encrypt the plaintext using the key and returns the encrypted data.

        Parameters:
        :   - **key** – 128 bit LS byte first key for the encryption of the plaintext
            - **plaintext** – 128 bit LS byte first plaintext data block to be encrypted
            - **enc\_data** – 128 bit LS byte first encrypted data block

        Returns:
        :   Zero on success or error code otherwise.

    int bt\_encrypt\_be(const uint8\_t key[16], const uint8\_t plaintext[16], uint8\_t enc\_data[16])
    :   AES encrypt big-endian data.

        An AES encrypt helper is used to request the Bluetooth controller’s own hardware to encrypt the plaintext using the key and returns the encrypted data.

        Parameters:
        :   - **key** – 128 bit MS byte first key for the encryption of the plaintext
            - **plaintext** – 128 bit MS byte first plaintext data block to be encrypted
            - **enc\_data** – 128 bit MS byte first encrypted data block

        Returns:
        :   Zero on success or error code otherwise.

    int bt\_ccm\_decrypt(const uint8\_t key[16], uint8\_t nonce[13], const uint8\_t \*enc\_data, size\_t len, const uint8\_t \*aad, size\_t aad\_len, uint8\_t \*plaintext, size\_t mic\_size)
    :   Decrypt big-endian data with AES-CCM.

        Decrypts and authorizes `enc_data` with AES-CCM, as described in [https://tools.ietf.org/html/rfc3610](https://tools.ietf.org/html/rfc3610).

        Assumes that the MIC follows directly after the encrypted data.

        Parameters:
        :   - **key** – 128 bit MS byte first key
            - **nonce** – 13 byte MS byte first nonce
            - **enc\_data** – Encrypted data
            - **len** – Length of the encrypted data
            - **aad** – Additional authenticated data
            - **aad\_len** – Additional authenticated data length
            - **plaintext** – Plaintext buffer to place result in
            - **mic\_size** – Size of the trailing MIC (in bytes)

        Return values:
        :   - **0** – Successfully decrypted the data.
            - **-EINVAL** – Invalid parameters.
            - **-EBADMSG** – Authentication failed.

    int bt\_ccm\_encrypt(const uint8\_t key[16], uint8\_t nonce[13], const uint8\_t \*plaintext, size\_t len, const uint8\_t \*aad, size\_t aad\_len, uint8\_t \*enc\_data, size\_t mic\_size)
    :   Encrypt big-endian data with AES-CCM.

        Encrypts and generates a MIC from `plaintext` with AES-CCM, as described in [https://tools.ietf.org/html/rfc3610](https://tools.ietf.org/html/rfc3610).

        Places the MIC directly after the encrypted data.

        Parameters:
        :   - **key** – 128 bit MS byte first key
            - **nonce** – 13 byte MS byte first nonce
            - **plaintext** – Plaintext buffer to encrypt
            - **len** – Length of the encrypted data
            - **aad** – Additional authenticated data
            - **aad\_len** – Additional authenticated data length
            - **enc\_data** – Buffer to place encrypted data in
            - **mic\_size** – Size of the trailing MIC (in bytes)

        Return values:
        :   - **0** – Successfully encrypted the data.
            - **-EINVAL** – Invalid parameters.
