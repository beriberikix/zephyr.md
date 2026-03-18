---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/misc.html
original_path: services/misc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Miscellaneous

## Checksum APIs

### CRC

*group* crc
:   Enums

    enum crc\_type
    :   CRC algorithm enumeration.

        These values should be used with the [CRC](#group__crc) dispatch function.

        *Values:*

        enumerator CRC4
        :   Use [crc4](#group__crc_1ga4458d7743f9a3394fb68cddcc100e456).

        enumerator CRC4\_TI
        :   Use [crc4\_ti](#group__crc_1ga322365098ec65bde3d55b0c059896668).

        enumerator CRC7\_BE
        :   Use [crc7\_be](#group__crc_1ga1169005fd900b2787035044eeea38af1).

        enumerator CRC8
        :   Use [crc8](#group__crc_1gaa614e73ee7484ca0424fa7d14a54bbb6).

        enumerator CRC8\_CCITT
        :   Use [crc8\_ccitt](#group__crc_1ga9a925de71cd0255a22c769dc4b130da5).

        enumerator CRC16
        :   Use [crc16](#group__crc_1ga204a779aa0c1a152763ea8edc6fc3a8c).

        enumerator CRC16\_ANSI
        :   Use [crc16\_ansi](#group__crc_1gaac3ac50c029b656f5cc070e6c742601a).

        enumerator CRC16\_CCITT
        :   Use [crc16\_ccitt](#group__crc_1ga74fa5608612c629291d15bc00b1c411c).

        enumerator CRC16\_ITU\_T
        :   Use [crc16\_itu\_t](#group__crc_1ga5502729e443496719de338e8b6692ac1).

        enumerator CRC32\_C
        :   Use [crc32\_c](#group__crc_1ga88d510b3958aee0990ca345aba260bc1).

        enumerator CRC32\_IEEE
        :   Use [crc32\_ieee](#group__crc_1gafc24e79ed7f978f5bb813091ef318982).

    Functions

    uint16\_t crc16(uint16\_t poly, uint16\_t seed, const uint8\_t \*src, size\_t len)
    :   Generic function for computing a CRC-16 without input or output reflection.

        Compute CRC-16 by passing in the address of the input, the input length and polynomial used in addition to the initial value. This is O(n\*8) where n is the length of the buffer provided. No reflection is performed.

        Note

        If you are planning to use a CRC based on poly 0x1012 the functions [crc16\_itu\_t()](#group__crc_1ga5502729e443496719de338e8b6692ac1) is faster and thus recommended over this one.

        Parameters:
        :   - **poly** – The polynomial to use omitting the leading x^16 coefficient
            - **seed** – Initial value for the CRC computation
            - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes

        Returns:
        :   The computed CRC16 value (without any XOR applied to it)

    uint16\_t crc16\_reflect(uint16\_t poly, uint16\_t seed, const uint8\_t \*src, size\_t len)
    :   Generic function for computing a CRC-16 with input and output reflection.

        Compute CRC-16 by passing in the address of the input, the input length and polynomial used in addition to the initial value. This is O(n\*8) where n is the length of the buffer provided. Both input and output are reflected.

        The following checksums can, among others, be calculated by this function, depending on the value provided for the initial seed and the value the final calculated CRC is XORed with:

        - CRC-16/ANSI, CRC-16/MODBUS, CRC-16/USB, CRC-16/IBM [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-modbus](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-modbus) poly: 0x8005 (0xA001) initial seed: 0xffff, xor output: 0x0000

        Note

        If you are planning to use a CRC based on poly 0x1012 the function [crc16\_ccitt()](#group__crc_1ga74fa5608612c629291d15bc00b1c411c) is faster and thus recommended over this one.

        Parameters:
        :   - **poly** – The polynomial to use omitting the leading x^16 coefficient. Important: please reflect the poly. For example, use 0xA001 instead of 0x8005 for CRC-16-MODBUS.
            - **seed** – Initial value for the CRC computation
            - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes

        Returns:
        :   The computed CRC16 value (without any XOR applied to it)

    uint8\_t crc8(const uint8\_t \*src, size\_t len, uint8\_t polynomial, uint8\_t initial\_value, bool reversed)
    :   Generic function for computing CRC 8.

        Compute CRC 8 by passing in the address of the input, the input length and polynomial used in addition to the initial value.

        Parameters:
        :   - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes
            - **polynomial** – The polynomial to use omitting the leading x^8 coefficient
            - **initial\_value** – Initial value for the CRC computation
            - **reversed** – Should we use reflected/reversed values or not

        Returns:
        :   The computed CRC8 value

    uint16\_t crc16\_ccitt(uint16\_t seed, const uint8\_t \*src, size\_t len)
    :   Compute the checksum of a buffer with polynomial 0x1021, reflecting input and output.

        This function is able to calculate any CRC that uses 0x1021 as it polynomial and requires reflecting both the input and the output. It is a fast variant that runs in O(n) time, where n is the length of the input buffer.

        The following checksums can, among others, be calculated by this function, depending on the value provided for the initial seed and the value the final calculated CRC is XORed with:

        - CRC-16/CCITT, CRC-16/CCITT-TRUE, CRC-16/KERMIT [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-kermit](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-kermit) initial seed: 0x0000, xor output: 0x0000
        - CRC-16/X-25, CRC-16/IBM-SDLC, CRC-16/ISO-HDLC [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-sdlc](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-sdlc) initial seed: 0xffff, xor output: 0xffff

        See ITU-T Recommendation V.41 (November 1988).

        Note

        To calculate the CRC across non-contiguous blocks use the return value from block N-1 as the seed for block N.

        Parameters:
        :   - **seed** – Value to seed the CRC with
            - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes

        Returns:
        :   The computed CRC16 value (without any XOR applied to it)

    uint16\_t crc16\_itu\_t(uint16\_t seed, const uint8\_t \*src, size\_t len)
    :   Compute the checksum of a buffer with polynomial 0x1021, no reflection of input or output.

        This function is able to calculate any CRC that uses 0x1021 as it polynomial and requires no reflection on both the input and the output. It is a fast variant that runs in O(n) time, where n is the length of the input buffer.

        The following checksums can, among others, be calculated by this function, depending on the value provided for the initial seed and the value the final calculated CRC is XORed with:

        - CRC-16/XMODEM, CRC-16/ACORN, CRC-16/LTE [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-xmodem](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-xmodem) initial seed: 0x0000, xor output: 0x0000
        - CRC16/CCITT-FALSE, CRC-16/IBM-3740, CRC-16/AUTOSAR [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-3740](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-3740) initial seed: 0xffff, xor output: 0x0000
        - CRC-16/GSM [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-gsm](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-gsm) initial seed: 0x0000, xor output: 0xffff

        See ITU-T Recommendation V.41 (November 1988) (MSB first).

        Note

        To calculate the CRC across non-contiguous blocks use the return value from block N-1 as the seed for block N.

        Parameters:
        :   - **seed** – Value to seed the CRC with
            - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes

        Returns:
        :   The computed CRC16 value (without any XOR applied to it)

    static inline uint16\_t crc16\_ansi(const uint8\_t \*src, size\_t len)
    :   Compute the ANSI (or Modbus) variant of CRC-16.

        The ANSI variant of CRC-16 uses 0x8005 (0xA001 reflected) as its polynomial with the initial \* value set to 0xffff.

        Parameters:
        :   - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes

        Returns:
        :   The computed CRC16 value

    uint32\_t crc32\_ieee(const uint8\_t \*data, size\_t len)
    :   Generate IEEE conform CRC32 checksum.

        Parameters:
        :   - **data** – Pointer to data on which the CRC should be calculated.
            - **len** – Data length.

        Returns:
        :   CRC32 value.

    uint32\_t crc32\_ieee\_update(uint32\_t crc, const uint8\_t \*data, size\_t len)
    :   Update an IEEE conforming CRC32 checksum.

        Parameters:
        :   - **CRC** – CRC32 checksum that needs to be updated.
            - **data** – Pointer to data on which the CRC should be calculated.
            - **len** – Data length.

        Returns:
        :   CRC32 value.

    uint32\_t crc32\_c(uint32\_t crc, const uint8\_t \*data, size\_t len, bool first\_pkt, bool last\_pkt)
    :   Calculate CRC32C (Castagnoli) checksum.

        Parameters:
        :   - **CRC** – CRC32C checksum that needs to be updated.
            - **data** – Pointer to data on which the CRC should be calculated.
            - **len** – Data length.
            - **first\_pkt** – Whether this is the first packet in the stream.
            - **last\_pkt** – Whether this is the last packet in the stream.

        Returns:
        :   CRC32 value.

    uint8\_t crc8\_ccitt(uint8\_t initial\_value, const void \*buf, size\_t len)
    :   Compute CCITT variant of CRC 8.

        Normal CCITT variant of CRC 8 is using 0x07.

        Parameters:
        :   - **initial\_value** – Initial value for the CRC computation
            - **buf** – Input bytes for the computation
            - **len** – Length of the input in bytes

        Returns:
        :   The computed CRC8 value

    uint8\_t crc7\_be(uint8\_t seed, const uint8\_t \*src, size\_t len)
    :   Compute the CRC-7 checksum of a buffer.

        See JESD84-A441. Used by the MMC protocol. Uses 0x09 as the polynomial with no reflection. The CRC is left justified, so bit 7 of the result is bit 6 of the CRC.

        Parameters:
        :   - **seed** – Value to seed the CRC with
            - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes

        Returns:
        :   The computed CRC7 value

    uint8\_t crc4\_ti(uint8\_t seed, const uint8\_t \*src, size\_t len)
    :   Compute the CRC-4 checksum of a buffer.

        Used by the TMAG5170 sensor. Uses 0x03 as the polynomial with no reflection. 4 most significant bits of the CRC result will be set to zero.

        Parameters:
        :   - **seed** – Value to seed the CRC with
            - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes

        Returns:
        :   The computed CRC4 value

    uint8\_t crc4(const uint8\_t \*src, size\_t len, uint8\_t polynomial, uint8\_t initial\_value, bool reversed)
    :   Generic function for computing CRC 4.

        Compute CRC 4 by passing in the address of the input, the input length and polynomial used in addition to the initial value. The input buffer must be aligned to a whole byte. It is guaranteed that 4 most significant bits of the result will be set to zero.

        Parameters:
        :   - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes
            - **polynomial** – The polynomial to use omitting the leading x^4 coefficient
            - **initial\_value** – Initial value for the CRC computation
            - **reversed** – Should we use reflected/reversed values or not

        Returns:
        :   The computed CRC4 value

    static inline uint32\_t crc\_by\_type(enum [crc\_type](#c.crc_type) type, const uint8\_t \*src, size\_t len, uint32\_t seed, uint32\_t poly, bool reflect, bool first, bool last)
    :   Compute a CRC checksum, in a generic way.

        This is a dispatch function that calls the individual CRC routine determined by `type`.

        For 7, 8, and 16-bit CRCs, the relevant `seed` and `poly` values should be passed in via the least-significant byte(s).

        Similarly, for 7, 8, and 16-bit CRCs, the relevant result is stored in the least-significant byte(s) of the returned value.

        Parameters:
        :   - **type** – CRC algorithm to use.
            - **src** – Input bytes for the computation
            - **len** – Length of the input in bytes
            - **seed** – Value to seed the CRC with
            - **poly** – The polynomial to use omitting the leading coefficient
            - **reflect** – Should we use reflected/reversed values or not
            - **first** – Whether this is the first packet in the stream.
            - **last** – Whether this is the last packet in the stream.

        Returns:
        :   uint32\_t the computed CRC value

## Structured Data APIs

### JSON

Related code samples

[AWS IoT Core MQTT](../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")
:   Connect to AWS IoT Core and publish messages using MQTT.

*group* json
:   Defines

    JSON\_OBJ\_DESCR\_PRIM(struct\_, field\_name\_, type\_)
    :   Helper macro to declare a descriptor for supported primitive values.

        Here’s an example of use:

        ```text
        struct foo {
            int32_t some_int;
        };

        struct json_obj_descr foo[] = {
            JSON_OBJ_DESCR_PRIM(struct foo, some_int, JSON_TOK_NUMBER),
        };
        ```

        Parameters:
        :   - **struct\_** – Struct packing the values
            - **field\_name\_** – Field name in the struct
            - **type\_** – Token type for JSON value corresponding to a primitive type. Must be one of: JSON\_TOK\_STRING for strings, JSON\_TOK\_NUMBER for numbers, JSON\_TOK\_TRUE (or JSON\_TOK\_FALSE) for booleans.

    JSON\_OBJ\_DESCR\_OBJECT(struct\_, field\_name\_, sub\_descr\_)
    :   Helper macro to declare a descriptor for an object value.

        Here’s an example of use:

        ```text
         struct nested {
             int32_t foo;
             struct {
                int32_t baz;
             } bar;
         };

         struct json_obj_descr nested_bar[] = {
             { ... declare bar.baz descriptor ... },
         };
         struct json_obj_descr nested[] = {
             { ... declare foo descriptor ... },
             JSON_OBJ_DESCR_OBJECT(struct nested, bar, nested_bar),
         };
        ```

        Parameters:
        :   - **struct\_** – Struct packing the values
            - **field\_name\_** – Field name in the struct
            - **sub\_descr\_** – Array of [json\_obj\_descr](#structjson__obj__descr) describing the subobject

    JSON\_OBJ\_DESCR\_ARRAY(struct\_, field\_name\_, max\_len\_, len\_field\_, elem\_type\_)
    :   Helper macro to declare a descriptor for an array of primitives.

        Here’s an example of use:

        ```text
         struct example {
             int32_t foo[10];
             size_t foo_len;
         };

         struct json_obj_descr array[] = {
              JSON_OBJ_DESCR_ARRAY(struct example, foo, 10, foo_len,
                                   JSON_TOK_NUMBER)
         };
        ```

        Parameters:
        :   - **struct\_** – Struct packing the values
            - **field\_name\_** – Field name in the struct
            - **max\_len\_** – Maximum number of elements in array
            - **len\_field\_** – Field name in the struct for the number of elements in the array
            - **elem\_type\_** – Element type, must be a primitive type

    JSON\_OBJ\_DESCR\_OBJ\_ARRAY(struct\_, field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_)
    :   Helper macro to declare a descriptor for an array of objects.

        Here’s an example of use:

        ```text
         struct person_height {
             const char *name;
             int32_t height;
         };

         struct people_heights {
             struct person_height heights[10];
             size_t heights_len;
         };

         struct json_obj_descr person_height_descr[] = {
              JSON_OBJ_DESCR_PRIM(struct person_height, name, JSON_TOK_STRING),
              JSON_OBJ_DESCR_PRIM(struct person_height, height, JSON_TOK_NUMBER),
         };

         struct json_obj_descr array[] = {
              JSON_OBJ_DESCR_OBJ_ARRAY(struct people_heights, heights, 10,
                                       heights_len, person_height_descr,
                                       ARRAY_SIZE(person_height_descr)),
         };
        ```

        Parameters:
        :   - **struct\_** – Struct packing the values
            - **field\_name\_** – Field name in the struct containing the array
            - **max\_len\_** – Maximum number of elements in the array
            - **len\_field\_** – Field name in the struct for the number of elements in the array
            - **elem\_descr\_** – Element descriptor, pointer to a descriptor array
            - **elem\_descr\_len\_** – Number of elements in elem\_descr\_

    JSON\_OBJ\_DESCR\_ARRAY\_ARRAY(struct\_, field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_)
    :   Helper macro to declare a descriptor for an array of array.

        Here’s an example of use:

        ```text
         struct person_height {
             const char *name;
             int32_t height;
         };

         struct person_heights_array {
             struct person_height heights;
         }

         struct people_heights {
             struct person_height_array heights[10];
             size_t heights_len;
         };

         struct json_obj_descr person_height_descr[] = {
             JSON_OBJ_DESCR_PRIM(struct person_height, name, JSON_TOK_STRING),
             JSON_OBJ_DESCR_PRIM(struct person_height, height, JSON_TOK_NUMBER),
         };

         struct json_obj_descr person_height_array_descr[] = {
             JSON_OBJ_DESCR_OBJECT(struct person_heights_array,
                                   heights, person_height_descr),
         };

         struct json_obj_descr array_array[] = {
              JSON_OBJ_DESCR_ARRAY_ARRAY(struct people_heights, heights, 10,
                                         heights_len, person_height_array_descr,
                                         ARRAY_SIZE(person_height_array_descr)),
         };
        ```

        Parameters:
        :   - **struct\_** – Struct packing the values
            - **field\_name\_** – Field name in the struct containing the array
            - **max\_len\_** – Maximum number of elements in the array
            - **len\_field\_** – Field name in the struct for the number of elements in the array
            - **elem\_descr\_** – Element descriptor, pointer to a descriptor array
            - **elem\_descr\_len\_** – Number of elements in elem\_descr\_

    JSON\_OBJ\_DESCR\_ARRAY\_ARRAY\_NAMED(struct\_, json\_field\_name\_, struct\_field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_)
    :   Variant of JSON\_OBJ\_DESCR\_ARRAY\_ARRAY that can be used when the structure and JSON field names differ.

        This is useful when the JSON field is not a valid C identifier.

        See also

        [JSON\_OBJ\_DESCR\_ARRAY\_ARRAY](#group__json_1gaed8189235fd30d2bc041cafee9591ec9)

        Parameters:
        :   - **struct\_** – Struct packing the values
            - **json\_field\_name\_** – String, field name in JSON strings
            - **struct\_field\_name\_** – Field name in the struct containing the array
            - **max\_len\_** – Maximum number of elements in the array
            - **len\_field\_** – Field name in the struct for the number of elements in the array
            - **elem\_descr\_** – Element descriptor, pointer to a descriptor array
            - **elem\_descr\_len\_** – Number of elements in elem\_descr\_

    JSON\_OBJ\_DESCR\_PRIM\_NAMED(struct\_, json\_field\_name\_, struct\_field\_name\_, type\_)
    :   Variant of JSON\_OBJ\_DESCR\_PRIM that can be used when the structure and JSON field names differ.

        This is useful when the JSON field is not a valid C identifier.

        See also

        [JSON\_OBJ\_DESCR\_PRIM](#group__json_1ga1ed917f5a247ca33f2778afe62ff1a88)

        Parameters:
        :   - **struct\_** – Struct packing the values.
            - **json\_field\_name\_** – String, field name in JSON strings
            - **struct\_field\_name\_** – Field name in the struct
            - **type\_** – Token type for JSON value corresponding to a primitive type.

    JSON\_OBJ\_DESCR\_OBJECT\_NAMED(struct\_, json\_field\_name\_, struct\_field\_name\_, sub\_descr\_)
    :   Variant of JSON\_OBJ\_DESCR\_OBJECT that can be used when the structure and JSON field names differ.

        This is useful when the JSON field is not a valid C identifier.

        See also

        [JSON\_OBJ\_DESCR\_OBJECT](#group__json_1ga4ee365f43cfa86a214973defe81f1e88)

        Parameters:
        :   - **struct\_** – Struct packing the values
            - **json\_field\_name\_** – String, field name in JSON strings
            - **struct\_field\_name\_** – Field name in the struct
            - **sub\_descr\_** – Array of [json\_obj\_descr](#structjson__obj__descr) describing the subobject

    JSON\_OBJ\_DESCR\_ARRAY\_NAMED(struct\_, json\_field\_name\_, struct\_field\_name\_, max\_len\_, len\_field\_, elem\_type\_)
    :   Variant of JSON\_OBJ\_DESCR\_ARRAY that can be used when the structure and JSON field names differ.

        This is useful when the JSON field is not a valid C identifier.

        See also

        [JSON\_OBJ\_DESCR\_ARRAY](#group__json_1ga0b510decbc755c82903b54fcbc4a3b64)

        Parameters:
        :   - **struct\_** – Struct packing the values
            - **json\_field\_name\_** – String, field name in JSON strings
            - **struct\_field\_name\_** – Field name in the struct
            - **max\_len\_** – Maximum number of elements in array
            - **len\_field\_** – Field name in the struct for the number of elements in the array
            - **elem\_type\_** – Element type, must be a primitive type

    JSON\_OBJ\_DESCR\_OBJ\_ARRAY\_NAMED(struct\_, json\_field\_name\_, struct\_field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_)
    :   Variant of JSON\_OBJ\_DESCR\_OBJ\_ARRAY that can be used when the structure and JSON field names differ.

        This is useful when the JSON field is not a valid C identifier.

        Here’s an example of use:

        ```text
         struct person_height {
             const char *name;
             int32_t height;
         };

         struct people_heights {
             struct person_height heights[10];
             size_t heights_len;
         };

         struct json_obj_descr person_height_descr[] = {
              JSON_OBJ_DESCR_PRIM(struct person_height, name, JSON_TOK_STRING),
              JSON_OBJ_DESCR_PRIM(struct person_height, height, JSON_TOK_NUMBER),
         };

         struct json_obj_descr array[] = {
              JSON_OBJ_DESCR_OBJ_ARRAY_NAMED(struct people_heights,
                                             "people-heights", heights,
                                             10, heights_len,
                                             person_height_descr,
                                             ARRAY_SIZE(person_height_descr)),
         };
        ```

        Parameters:
        :   - **struct\_** – Struct packing the values
            - **json\_field\_name\_** – String, field name of the array in JSON strings
            - **struct\_field\_name\_** – Field name in the struct containing the array
            - **max\_len\_** – Maximum number of elements in the array
            - **len\_field\_** – Field name in the struct for the number of elements in the array
            - **elem\_descr\_** – Element descriptor, pointer to a descriptor array
            - **elem\_descr\_len\_** – Number of elements in elem\_descr\_

    Typedefs

    typedef int (\*json\_append\_bytes\_t)(const char \*bytes, size\_t len, void \*data)
    :   Function pointer type to append bytes to a buffer while encoding JSON data.

        Param bytes:
        :   Contents to write to the output

        Param len:
        :   Number of bytes to append to output

        Param data:
        :   User-provided pointer

        Return:
        :   This callback function should return a negative number on error (which will be propagated to the return value of [json\_obj\_encode()](#group__json_1gafec772f687a0280f5211139bd019e582)), or 0 on success.

    Enums

    enum json\_tokens
    :   *Values:*

        enumerator JSON\_TOK\_NONE = '\_'

        enumerator JSON\_TOK\_OBJECT\_START = '{'

        enumerator JSON\_TOK\_OBJECT\_END = '}'

        enumerator JSON\_TOK\_LIST\_START = '['

        enumerator JSON\_TOK\_ARRAY\_START = '['

        enumerator JSON\_TOK\_LIST\_END = ']'

        enumerator JSON\_TOK\_ARRAY\_END = ']'

        enumerator JSON\_TOK\_STRING = '"'

        enumerator JSON\_TOK\_COLON = ':'

        enumerator JSON\_TOK\_COMMA = ','

        enumerator JSON\_TOK\_NUMBER = '0'

        enumerator JSON\_TOK\_FLOAT = '1'

        enumerator JSON\_TOK\_OPAQUE = '2'

        enumerator JSON\_TOK\_OBJ\_ARRAY = '3'

        enumerator JSON\_TOK\_TRUE = 't'

        enumerator JSON\_TOK\_FALSE = 'f'

        enumerator JSON\_TOK\_NULL = 'n'

        enumerator JSON\_TOK\_ERROR = '!'

        enumerator JSON\_TOK\_EOF = '\0'

    Functions

    int64\_t json\_obj\_parse(char \*json, size\_t len, const struct [json\_obj\_descr](#c.json_obj_descr) \*descr, size\_t descr\_len, void \*val)
    :   Parses the JSON-encoded object pointed to by *json*, with size *len*, according to the descriptor pointed to by *descr*.

        Values are stored in a struct pointed to by *val*. Set up the descriptor like this:

        struct s { int32\_t foo; char \*bar; } struct [json\_obj\_descr](#structjson__obj__descr) descr[] = { [JSON\_OBJ\_DESCR\_PRIM(struct s, foo, JSON\_TOK\_NUMBER)](#group__json_1ga1ed917f5a247ca33f2778afe62ff1a88), [JSON\_OBJ\_DESCR\_PRIM(struct s, bar, JSON\_TOK\_STRING)](#group__json_1ga1ed917f5a247ca33f2778afe62ff1a88), };

        Since this parser is designed for machine-to-machine communications, some liberties were taken to simplify the design: (1) strings are not unescaped (but only valid escape sequences are accepted); (2) no UTF-8 validation is performed; and (3) only integer numbers are supported (no strtod() in the minimal libc).

        Parameters:
        :   - **JSON** – Pointer to JSON-encoded value to be parsed
            - **len** – Length of JSON-encoded value
            - **descr** – Pointer to the descriptor array
            - **descr\_len** – Number of elements in the descriptor array. Must be less than 63 due to implementation detail reasons (if more fields are necessary, use two descriptors)
            - **val** – Pointer to the struct to hold the decoded values

        Returns:
        :   < 0 if error, bitmap of decoded fields on success (bit 0 is set if first field in the descriptor has been properly decoded, etc).

    int json\_arr\_parse(char \*json, size\_t len, const struct [json\_obj\_descr](#c.json_obj_descr) \*descr, void \*val)
    :   Parses the JSON-encoded array pointed to by *json*, with size *len*, according to the descriptor pointed to by *descr*.

        Values are stored in a struct pointed to by *val*. Set up the descriptor like this:

        struct s { int32\_t foo; char \*bar; } struct [json\_obj\_descr](#structjson__obj__descr) descr[] = { [JSON\_OBJ\_DESCR\_PRIM(struct s, foo, JSON\_TOK\_NUMBER)](#group__json_1ga1ed917f5a247ca33f2778afe62ff1a88), [JSON\_OBJ\_DESCR\_PRIM(struct s, bar, JSON\_TOK\_STRING)](#group__json_1ga1ed917f5a247ca33f2778afe62ff1a88), }; struct a { struct s baz[10]; size\_t count; } struct [json\_obj\_descr](#structjson__obj__descr) array[] = { [JSON\_OBJ\_DESCR\_OBJ\_ARRAY(struct a, baz, 10, count,descr, ARRAY\_SIZE(descr))](#group__json_1gae012264df03546a1c01eec4216b52ffd), };

        Since this parser is designed for machine-to-machine communications, some liberties were taken to simplify the design: (1) strings are not unescaped (but only valid escape sequences are accepted); (2) no UTF-8 validation is performed; and (3) only integer numbers are supported (no strtod() in the minimal libc).

        Parameters:
        :   - **JSON** – Pointer to JSON-encoded array to be parsed
            - **len** – Length of JSON-encoded array
            - **descr** – Pointer to the descriptor array
            - **val** – Pointer to the struct to hold the decoded values

        Returns:
        :   0 if array has been successfully parsed. A negative value indicates an error (as defined on errno.h).

    int json\_arr\_separate\_object\_parse\_init(struct [json\_obj](#c.json_obj) \*json, char \*payload, size\_t len)
    :   Initialize single-object array parsing.

        JSON-encoded array data is going to be parsed one object at a time. Data is provided by *payload* with the size of *len* bytes.

        Function validate that Json Array start is detected and initialize *json* object for Json object parsing separately.

        Parameters:
        :   - **JSON** – Provide storage for parser states. To be used when parsing the array.
            - **payload** – Pointer to JSON-encoded array to be parsed
            - **len** – Length of JSON-encoded array

        Returns:
        :   0 if array start is detected and initialization is successful or negative error code in case of failure.

    int json\_arr\_separate\_parse\_object(struct [json\_obj](#c.json_obj) \*json, const struct [json\_obj\_descr](#c.json_obj_descr) \*descr, size\_t descr\_len, void \*val)
    :   Parse a single object from array.

        Parses the JSON-encoded object pointed to by *json* object array, with size *len*, according to the descriptor pointed to by *descr*.

        Parameters:
        :   - **JSON** – Pointer to JSON-object message state
            - **descr** – Pointer to the descriptor array
            - **descr\_len** – Number of elements in the descriptor array. Must be less than 31.
            - **val** – Pointer to the struct to hold the decoded values

        Returns:
        :   < 0 if error, 0 for end of message, bitmap of decoded fields on success (bit 0 is set if first field in the descriptor has been properly decoded, etc).

    ssize\_t json\_escape(char \*str, size\_t \*len, size\_t buf\_size)
    :   Escapes the string so it can be used to encode JSON objects.

        Parameters:
        :   - **str** – The string to escape; the escape string is stored the buffer pointed to by this parameter
            - **len** – Points to a size\_t containing the size before and after the escaping process
            - **buf\_size** – The size of buffer str points to

        Returns:
        :   0 if string has been escaped properly, or -ENOMEM if there was not enough space to escape the buffer

    size\_t json\_calc\_escaped\_len(const char \*str, size\_t len)
    :   Calculates the JSON-escaped string length.

        Parameters:
        :   - **str** – The string to analyze
            - **len** – String size

        Returns:
        :   The length str would have if it were escaped

    ssize\_t json\_calc\_encoded\_len(const struct [json\_obj\_descr](#c.json_obj_descr) \*descr, size\_t descr\_len, const void \*val)
    :   Calculates the string length to fully encode an object.

        Parameters:
        :   - **descr** – Pointer to the descriptor array
            - **descr\_len** – Number of elements in the descriptor array
            - **val** – Struct holding the values

        Returns:
        :   Number of bytes necessary to encode the values if >0, an error code is returned.

    ssize\_t json\_calc\_encoded\_arr\_len(const struct [json\_obj\_descr](#c.json_obj_descr) \*descr, const void \*val)
    :   Calculates the string length to fully encode an array.

        Parameters:
        :   - **descr** – Pointer to the descriptor array
            - **val** – Struct holding the values

        Returns:
        :   Number of bytes necessary to encode the values if >0, an error code is returned.

    int json\_obj\_encode\_buf(const struct [json\_obj\_descr](#c.json_obj_descr) \*descr, size\_t descr\_len, const void \*val, char \*buffer, size\_t buf\_size)
    :   Encodes an object in a contiguous memory location.

        Parameters:
        :   - **descr** – Pointer to the descriptor array
            - **descr\_len** – Number of elements in the descriptor array
            - **val** – Struct holding the values
            - **buffer** – Buffer to store the JSON data
            - **buf\_size** – Size of buffer, in bytes, with space for the terminating NUL character

        Returns:
        :   0 if object has been successfully encoded. A negative value indicates an error (as defined on errno.h).

    int json\_arr\_encode\_buf(const struct [json\_obj\_descr](#c.json_obj_descr) \*descr, const void \*val, char \*buffer, size\_t buf\_size)
    :   Encodes an array in a contiguous memory location.

        Parameters:
        :   - **descr** – Pointer to the descriptor array
            - **val** – Struct holding the values
            - **buffer** – Buffer to store the JSON data
            - **buf\_size** – Size of buffer, in bytes, with space for the terminating NUL character

        Returns:
        :   0 if object has been successfully encoded. A negative value indicates an error (as defined on errno.h).

    int json\_obj\_encode(const struct [json\_obj\_descr](#c.json_obj_descr) \*descr, size\_t descr\_len, const void \*val, [json\_append\_bytes\_t](#c.json_append_bytes_t) append\_bytes, void \*data)
    :   Encodes an object using an arbitrary writer function.

        Parameters:
        :   - **descr** – Pointer to the descriptor array
            - **descr\_len** – Number of elements in the descriptor array
            - **val** – Struct holding the values
            - **append\_bytes** – Function to append bytes to the output
            - **data** – Data pointer to be passed to the append\_bytes callback function.

        Returns:
        :   0 if object has been successfully encoded. A negative value indicates an error.

    int json\_arr\_encode(const struct [json\_obj\_descr](#c.json_obj_descr) \*descr, const void \*val, [json\_append\_bytes\_t](#c.json_append_bytes_t) append\_bytes, void \*data)
    :   Encodes an array using an arbitrary writer function.

        Parameters:
        :   - **descr** – Pointer to the descriptor array
            - **val** – Struct holding the values
            - **append\_bytes** – Function to append bytes to the output
            - **data** – Data pointer to be passed to the append\_bytes callback function.

        Returns:
        :   0 if object has been successfully encoded. A negative value indicates an error.

    struct json\_token
    :   *#include <json.h>*

    struct json\_lexer
    :   *#include <json.h>*

    struct json\_obj
    :   *#include <json.h>*

    struct json\_obj\_token
    :   *#include <json.h>*

    struct json\_obj\_descr
    :   *#include <json.h>*

### JWT

JSON Web Tokens (JWT) are an open, industry standard [RFC
7519]([https://tools.ietf.org/html/rfc7519](https://tools.ietf.org/html/rfc7519)) method for representing
claims securely between two parties. Although JWT is fairly flexible,
this API is limited to creating the simplistic tokens needed to
authenticate with the Google Core IoT infrastructure.

*group* jwt
:   JSON Web Token (JWT).

    Functions

    int jwt\_init\_builder(struct [jwt\_builder](#c.jwt_builder) \*builder, char \*buffer, size\_t buffer\_size)
    :   Initialize the JWT builder.

        Initialize the given JWT builder for the creation of a fresh token. The buffer size should at least be as long as JWT\_BUILDER\_MAX\_SIZE returns.

        Parameters:
        :   - **builder** – The builder to initialize.
            - **buffer** – The buffer to write the token to.
            - **buffer\_size** – The size of this buffer. The token will be NULL terminated, which needs to be allowed for in this size.

        Return values:
        :   - **0** – Success
            - **-ENOSPC** – Buffer is insufficient to initialize

    int jwt\_add\_payload(struct [jwt\_builder](#c.jwt_builder) \*builder, int32\_t exp, int32\_t iat, const char \*aud)
    :   add JWT primary payload.

    int jwt\_sign(struct [jwt\_builder](#c.jwt_builder) \*builder, const char \*der\_key, size\_t der\_key\_len)
    :   Sign the JWT token.

    static inline size\_t jwt\_payload\_len(struct [jwt\_builder](#c.jwt_builder) \*builder)

    struct jwt\_builder
    :   *#include <jwt.h>*

        JWT data tracking.

        JSON Web Tokens contain several sections, each encoded in base-64. This structure tracks the token as it is being built, including limits on the amount of available space. It should be initialized with jwt\_init().

        Public Members

        char \*base
        :   The base of the buffer we are writing to.

        char \*buf
        :   The place in this buffer where we are currently writing.

        size\_t len
        :   The length remaining to write.

        bool overflowed
        :   Flag that is set if we try to write past the end of the buffer.

            If set, the token is not valid.
