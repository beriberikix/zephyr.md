---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/crypto/api/index.html
original_path: services/crypto/api/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Crypto APIs

## Overview

## API Reference

### Generic API for crypto drivers

Related code samples

[Crypto](../../../samples/drivers/crypto/README.md#crypto "Use the crypto APIs to perform various encryption/decryption operations.")
:   Use the crypto APIs to perform various encryption/decryption operations.

*group* Crypto
:   Crypto APIs.

    **Since**
    :   1.7

    **Version**
    :   1.0.0

    Defines

    CAP\_OPAQUE\_KEY\_HNDL

    CAP\_RAW\_KEY

    CAP\_KEY\_LOADING\_API

    CAP\_INPLACE\_OPS
    :   Whether the output is placed in separate buffer or not.

    CAP\_SEPARATE\_IO\_BUFS

    CAP\_SYNC\_OPS
    :   These denotes if the output (completion of a cipher\_xxx\_op) is conveyed by the op function returning, or it is conveyed by an async notification.

    CAP\_ASYNC\_OPS

    CAP\_AUTONONCE
    :   Whether the hardware/driver supports autononce feature.

    CAP\_NO\_IV\_PREFIX
    :   Don’t prefix IV to cipher blocks.

    Functions

    static inline int crypto\_query\_hwcaps(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Query the crypto hardware capabilities.

        This API is used by the app to query the capabilities supported by the crypto device. Based on this the app can specify a subset of the supported options to be honored for a session during [cipher\_begin\_session()](#group__crypto__cipher_1ga0720700438ba5819aa826aa37f0c4227).

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   bitmask of supported options.

    struct crypto\_driver\_api
    :   *#include <crypto.h>*

        Crypto driver API definition.

### Ciphers API

*group* Cipher
:   Crypto Cipher APIs.

    Typedefs

    typedef int (\*block\_op\_t)(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_pkt](#c.cipher_pkt) \*pkt)

    typedef int (\*cbc\_op\_t)(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_pkt](#c.cipher_pkt) \*pkt, uint8\_t \*iv)

    typedef int (\*ctr\_op\_t)(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_pkt](#c.cipher_pkt) \*pkt, uint8\_t \*ctr)

    typedef int (\*ccm\_op\_t)(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_aead\_pkt](#c.cipher_aead_pkt) \*pkt, uint8\_t \*nonce)

    typedef int (\*gcm\_op\_t)(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_aead\_pkt](#c.cipher_aead_pkt) \*pkt, uint8\_t \*nonce)

    typedef void (\*cipher\_completion\_cb)(struct [cipher\_pkt](#c.cipher_pkt) \*completed, int status)

    Enums

    enum cipher\_algo
    :   Cipher Algorithm.

        *Values:*

        enumerator CRYPTO\_CIPHER\_ALGO\_AES = 1

    enum cipher\_op
    :   Cipher Operation.

        *Values:*

        enumerator CRYPTO\_CIPHER\_OP\_DECRYPT = 0

        enumerator CRYPTO\_CIPHER\_OP\_ENCRYPT = 1

    enum cipher\_mode
    :   Possible cipher mode options.

        More to be added as required.

        *Values:*

        enumerator CRYPTO\_CIPHER\_MODE\_ECB = 1

        enumerator CRYPTO\_CIPHER\_MODE\_CBC = 2

        enumerator CRYPTO\_CIPHER\_MODE\_CTR = 3

        enumerator CRYPTO\_CIPHER\_MODE\_CCM = 4

        enumerator CRYPTO\_CIPHER\_MODE\_GCM = 5

    Functions

    static inline int cipher\_begin\_session(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [cipher\_ctx](#c.cipher_ctx) \*ctx, enum [cipher\_algo](#c.cipher_algo) algo, enum [cipher\_mode](#c.cipher_mode) mode, enum [cipher\_op](#c.cipher_op) optype)
    :   Setup a crypto session.

        Initializes one time parameters, like the session key, algorithm and cipher mode which may remain constant for all operations in the session. The state may be cached in hardware and/or driver data state variables.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ctx** – Pointer to the context structure. Various one time parameters like key, keylength, etc. are supplied via this structure. The structure documentation specifies which fields are to be populated by the app before making this call.
            - **algo** – The crypto algorithm to be used in this session. e.g AES
            - **mode** – The cipher mode to be used in this session. e.g CBC, CTR
            - **optype** – Whether we should encrypt or decrypt in this session

        Returns:
        :   0 on success, negative errno code on fail.

    static inline int cipher\_free\_session(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [cipher\_ctx](#c.cipher_ctx) \*ctx)
    :   Cleanup a crypto session.

        Clears the hardware and/or driver state of a previous session.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ctx** – Pointer to the crypto context structure of the session to be freed.

        Returns:
        :   0 on success, negative errno code on fail.

    static inline int cipher\_callback\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [cipher\_completion\_cb](#c.cipher_completion_cb) cb)
    :   Registers an async crypto op completion callback with the driver.

        The application can register an async crypto op completion callback handler to be invoked by the driver, on completion of a prior request submitted via cipher\_do\_op(). Based on crypto device hardware semantics, this is likely to be invoked from an ISR context.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **cb** – Pointer to application callback to be called by the driver.

        Returns:
        :   0 on success, -ENOTSUP if the driver does not support async op, negative errno code on other error.

    static inline int cipher\_block\_op(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_pkt](#c.cipher_pkt) \*pkt)
    :   Perform single-block crypto operation (ECB cipher mode).

        This should not be overloaded to operate on multiple blocks for security reasons.

        Parameters:
        :   - **ctx** – Pointer to the crypto context of this op.
            - **pkt** – Structure holding the input/output buffer pointers.

        Returns:
        :   0 on success, negative errno code on fail.

    static inline int cipher\_cbc\_op(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_pkt](#c.cipher_pkt) \*pkt, uint8\_t \*iv)
    :   Perform Cipher Block Chaining (CBC) crypto operation.

        Parameters:
        :   - **ctx** – Pointer to the crypto context of this op.
            - **pkt** – Structure holding the input/output buffer pointers.
            - **iv** – Initialization Vector (IV) for the operation. Same IV value should not be reused across multiple operations (within a session context) for security.

        Returns:
        :   0 on success, negative errno code on fail.

    static inline int cipher\_ctr\_op(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_pkt](#c.cipher_pkt) \*pkt, uint8\_t \*iv)
    :   Perform Counter (CTR) mode crypto operation.

        Parameters:
        :   - **ctx** – Pointer to the crypto context of this op.
            - **pkt** – Structure holding the input/output buffer pointers.
            - **iv** – Initialization Vector (IV) for the operation. We use a split counter formed by appending IV and ctr. Consequently ivlen = keylen - ctrlen. ‘ctrlen’ is specified during session setup through the ‘ctx.mode\_params.ctr\_params.ctr\_len’ parameter. IV should not be reused across multiple operations (within a session context) for security. The non-IV part of the split counter is transparent to the caller and is fully managed by the crypto provider.

        Returns:
        :   0 on success, negative errno code on fail.

    static inline int cipher\_ccm\_op(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_aead\_pkt](#c.cipher_aead_pkt) \*pkt, uint8\_t \*nonce)
    :   Perform Counter with CBC-MAC (CCM) mode crypto operation.

        Parameters:
        :   - **ctx** – Pointer to the crypto context of this op.
            - **pkt** – Structure holding the input/output, Associated Data (AD) and auth tag buffer pointers.
            - **nonce** – Nonce for the operation. Same nonce value should not be reused across multiple operations (within a session context) for security.

        Returns:
        :   0 on success, negative errno code on fail.

    static inline int cipher\_gcm\_op(struct [cipher\_ctx](#c.cipher_ctx) \*ctx, struct [cipher\_aead\_pkt](#c.cipher_aead_pkt) \*pkt, uint8\_t \*nonce)
    :   Perform Galois/Counter Mode (GCM) crypto operation.

        Parameters:
        :   - **ctx** – Pointer to the crypto context of this op.
            - **pkt** – Structure holding the input/output, Associated Data (AD) and auth tag buffer pointers.
            - **nonce** – Nonce for the operation. Same nonce value should not be reused across multiple operations (within a session context) for security.

        Returns:
        :   0 on success, negative errno code on fail.

    struct cipher\_ops
    :   *#include <cipher.h>*

    struct ccm\_params
    :   *#include <cipher.h>*

    struct ctr\_params
    :   *#include <cipher.h>*

    struct gcm\_params
    :   *#include <cipher.h>*

    struct cipher\_ctx
    :   *#include <cipher.h>*

        Structure encoding session parameters.

        Refer to comments for individual fields to know the contract in terms of who fills what and when w.r.t begin\_session() call.

        Public Members

        struct [cipher\_ops](#c.cipher_ops) ops
        :   Place for driver to return function pointers to be invoked per cipher operation.

            To be populated by crypto driver on return from begin\_session() based on the algo/mode chosen by the app.

        union [cipher\_ctx](#c.cipher_ctx).[anonymous] key
        :   To be populated by the app before calling begin\_session().

        const struct [device](#c.cipher_ctx.device) \*device
        :   The device driver instance this crypto context relates to.

            Will be populated by the begin\_session() API.

        void \*drv\_sessn\_state
        :   If the driver supports multiple simultaneously crypto sessions, this will identify the specific driver state this crypto session relates to.

            Since dynamic memory allocation is not possible, it is suggested that at build time drivers allocate space for the max simultaneous sessions they intend to support. To be populated by the driver on return from begin\_session().

        void \*app\_sessn\_state
        :   Place for the user app to put info relevant stuff for resuming when completion callback happens for async ops.

            Totally managed by the app.

        union [cipher\_ctx](#c.cipher_ctx).[anonymous] mode\_params
        :   Cypher mode parameters, which remain constant for all ops in a session.

            To be populated by the app before calling begin\_session().

        uint16\_t keylen
        :   Cryptographic keylength in bytes.

            To be populated by the app before calling begin\_session()

        uint16\_t flags
        :   How certain fields are to be interpreted for this session.

            (A bitmask of CAP\_\* below.) To be populated by the app before calling begin\_session(). An app can obtain the capability flags supported by a hw/driver by calling [crypto\_query\_hwcaps()](#group__crypto_1gadb2c24136bb56927bb14d4cfffdd5d80).

    struct cipher\_pkt
    :   *#include <cipher.h>*

        Structure encoding IO parameters of one cryptographic operation like encrypt/decrypt.

        The fields which has not been explicitly called out has to be filled up by the app before making the cipher\_xxx\_op() call.

        Public Members

        uint8\_t \*in\_buf
        :   Start address of input buffer.

        int in\_len
        :   Bytes to be operated upon.

        uint8\_t \*out\_buf
        :   Start of the output buffer, to be allocated by the application.

            Can be NULL for in-place ops. To be populated with contents by the driver on return from op / async callback.

        int out\_buf\_max
        :   Size of the out\_buf area allocated by the application.

            Drivers should not write past the size of output buffer.

        int out\_len
        :   To be populated by driver on return from cipher\_xxx\_op() and holds the size of the actual result.

        struct [cipher\_ctx](#c.cipher_ctx) \*ctx
        :   Context this packet relates to.

            This can be useful to get the session details, especially for async ops. Will be populated by the cipher\_xxx\_op() API based on the ctx parameter.

    struct cipher\_aead\_pkt
    :   *#include <cipher.h>*

        Structure encoding IO parameters in AEAD (Authenticated Encryption with Associated Data) scenario like in CCM.

        App has to furnish valid contents prior to making [cipher\_ccm\_op()](#group__crypto__cipher_1ga4886e7e1cc2fcff411066875b35b8b45) call.

        Public Members

        uint8\_t \*ad
        :   Start address for Associated Data.

            This has to be supplied by app.

        uint32\_t ad\_len
        :   Size of Associated Data.

            This has to be supplied by the app.

        uint8\_t \*tag
        :   Start address for the auth hash.

            For an encryption op this will be populated by the driver when it returns from cipher\_ccm\_op call. For a decryption op this has to be supplied by the app.
