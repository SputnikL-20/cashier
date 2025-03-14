# -*- coding: utf-8 -*-

import ctypes
import sys
import json
import datetime
import os
import platform

if sys.version_info[0] == 3:
    if platform.system() == 'Windows':
        from winreg import *
    TEXT = str
    RANGE = range
else:
    if platform.system() == 'Windows':
        from _winreg import *
    TEXT = basestring
    RANGE = xrange


class IFptr(object):
    (
        LIBFPTR_PARAM_TEXT,
        LIBFPTR_PARAM_TEXT_WRAP,
        LIBFPTR_PARAM_ALIGNMENT,
        LIBFPTR_PARAM_FONT,
        LIBFPTR_PARAM_FONT_DOUBLE_WIDTH,
        LIBFPTR_PARAM_FONT_DOUBLE_HEIGHT,
        LIBFPTR_PARAM_LINESPACING,
        LIBFPTR_PARAM_BRIGHTNESS,
        LIBFPTR_PARAM_MODEL,
        LIBFPTR_PARAM_RECEIPT_TYPE,
        LIBFPTR_PARAM_REPORT_TYPE,
        LIBFPTR_PARAM_MODE,
        LIBFPTR_PARAM_EXTERNAL_DEVICE_TYPE,
        LIBFPTR_PARAM_EXTERNAL_DEVICE_DATA,
        LIBFPTR_PARAM_FREQUENCY,
        LIBFPTR_PARAM_DURATION,
        LIBFPTR_PARAM_CUT_TYPE,
        LIBFPTR_PARAM_DRAWER_ON_TIMEOUT,
        LIBFPTR_PARAM_DRAWER_OFF_TIMEOUT,
        LIBFPTR_PARAM_DRAWER_ON_QUANTITY,
        LIBFPTR_PARAM_TIMEOUT_ENQ,
        LIBFPTR_PARAM_COMMAND_BUFFER,
        LIBFPTR_PARAM_ANSWER_BUFFER,
        LIBFPTR_PARAM_SERIAL_NUMBER,
        LIBFPTR_PARAM_MANUFACTURER_CODE,
        LIBFPTR_PARAM_NO_NEED_ANSWER,
        LIBFPTR_PARAM_INFO_DISCOUNT_SUM,
        LIBFPTR_PARAM_USE_ONLY_TAX_TYPE,
        LIBFPTR_PARAM_PAYMENT_TYPE,
        LIBFPTR_PARAM_PAYMENT_SUM,
        LIBFPTR_PARAM_REMAINDER,
        LIBFPTR_PARAM_CHANGE,
        LIBFPTR_PARAM_DEPARTMENT,
        LIBFPTR_PARAM_TAX_TYPE,
        LIBFPTR_PARAM_TAX_SUM,
        LIBFPTR_PARAM_TAX_MODE,
        LIBFPTR_PARAM_RECEIPT_ELECTRONICALLY,
        LIBFPTR_PARAM_USER_PASSWORD,
        LIBFPTR_PARAM_SCALE,
        LIBFPTR_PARAM_LEFT_MARGIN,
        LIBFPTR_PARAM_BARCODE,
        LIBFPTR_PARAM_BARCODE_TYPE,
        LIBFPTR_PARAM_BARCODE_PRINT_TEXT,
        LIBFPTR_PARAM_BARCODE_VERSION,
        LIBFPTR_PARAM_BARCODE_CORRECTION,
        LIBFPTR_PARAM_BARCODE_COLUMNS,
        LIBFPTR_PARAM_BARCODE_INVERT,
        LIBFPTR_PARAM_HEIGHT,
        LIBFPTR_PARAM_WIDTH,
        LIBFPTR_PARAM_FILENAME,
        LIBFPTR_PARAM_PICTURE_NUMBER,
        LIBFPTR_PARAM_DATA_TYPE,
        LIBFPTR_PARAM_OPERATOR_ID,
        LIBFPTR_PARAM_LOGICAL_NUMBER,
        LIBFPTR_PARAM_DATE_TIME,
        LIBFPTR_PARAM_FISCAL,
        LIBFPTR_PARAM_SHIFT_STATE,
        LIBFPTR_PARAM_CASHDRAWER_OPENED,
        LIBFPTR_PARAM_RECEIPT_PAPER_PRESENT,
        LIBFPTR_PARAM_COVER_OPENED,
        LIBFPTR_PARAM_SUBMODE,
        LIBFPTR_PARAM_RECEIPT_NUMBER,
        LIBFPTR_PARAM_DOCUMENT_NUMBER,
        LIBFPTR_PARAM_SHIFT_NUMBER,
        LIBFPTR_PARAM_RECEIPT_SUM,
        LIBFPTR_PARAM_RECEIPT_LINE_LENGTH,
        LIBFPTR_PARAM_RECEIPT_LINE_LENGTH_PIX,
        LIBFPTR_PARAM_MODEL_NAME,
        LIBFPTR_PARAM_UNIT_VERSION,
        LIBFPTR_PARAM_PRINTER_CONNECTION_LOST,
        LIBFPTR_PARAM_PRINTER_ERROR,
        LIBFPTR_PARAM_CUT_ERROR,
        LIBFPTR_PARAM_PRINTER_OVERHEAT,
        LIBFPTR_PARAM_UNIT_TYPE,
        LIBFPTR_PARAM_LICENSE_NUMBER,
        LIBFPTR_PARAM_LICENSE_ENTERED,
        LIBFPTR_PARAM_LICENSE,
        LIBFPTR_PARAM_SUM,
        LIBFPTR_PARAM_COUNT,
        LIBFPTR_PARAM_COUNTER_TYPE,
        LIBFPTR_PARAM_STEP_COUNTER_TYPE,
        LIBFPTR_PARAM_ERROR_TAG_NUMBER,
        LIBFPTR_PARAM_TABLE,
        LIBFPTR_PARAM_ROW,
        LIBFPTR_PARAM_FIELD,
        LIBFPTR_PARAM_FIELD_VALUE,
        LIBFPTR_PARAM_FN_DATA_TYPE,
        LIBFPTR_PARAM_TAG_NUMBER,
        LIBFPTR_PARAM_TAG_VALUE,
        LIBFPTR_PARAM_DOCUMENTS_COUNT,
        LIBFPTR_PARAM_FISCAL_SIGN,
        LIBFPTR_PARAM_DEVICE_FFD_VERSION,
        LIBFPTR_PARAM_FN_FFD_VERSION,
        LIBFPTR_PARAM_FFD_VERSION,
        LIBFPTR_PARAM_CHECK_SUM,
        LIBFPTR_PARAM_COMMODITY_NAME,
        LIBFPTR_PARAM_PRICE,
        LIBFPTR_PARAM_QUANTITY,
        LIBFPTR_PARAM_POSITION_SUM,
        LIBFPTR_PARAM_FN_TYPE,
        LIBFPTR_PARAM_FN_VERSION,
        LIBFPTR_PARAM_REGISTRATIONS_REMAIN,
        LIBFPTR_PARAM_REGISTRATIONS_COUNT,
        LIBFPTR_PARAM_NO_ERROR_IF_NOT_SUPPORTED,
        LIBFPTR_PARAM_OFD_EXCHANGE_STATUS,
        LIBFPTR_PARAM_FN_ERROR_DATA,
        LIBFPTR_PARAM_FN_ERROR_CODE,
        LIBFPTR_PARAM_ENVD_MODE,
        LIBFPTR_PARAM_DOCUMENT_CLOSED,
        LIBFPTR_PARAM_JSON_DATA,
        LIBFPTR_PARAM_COMMAND_SUBSYSTEM,
        LIBFPTR_PARAM_FN_OPERATION_TYPE,
        LIBFPTR_PARAM_FN_STATE,
        LIBFPTR_PARAM_ENVD_MODE_ENABLED,
        LIBFPTR_PARAM_SETTING_ID,
        LIBFPTR_PARAM_SETTING_VALUE,
        LIBFPTR_PARAM_MAPPING_KEY,
        LIBFPTR_PARAM_MAPPING_VALUE,
        LIBFPTR_PARAM_COMMODITY_PIECE,
        LIBFPTR_PARAM_POWER_SOURCE_TYPE,
        LIBFPTR_PARAM_BATTERY_CHARGE,
        LIBFPTR_PARAM_VOLTAGE,
        LIBFPTR_PARAM_USE_BATTERY,
        LIBFPTR_PARAM_BATTERY_CHARGING,
        LIBFPTR_PARAM_CAN_PRINT_WHILE_ON_BATTERY,
        LIBFPTR_PARAM_MAC_ADDRESS,
        LIBFPTR_PARAM_FN_FISCAL,
        LIBFPTR_PARAM_NETWORK_ERROR,
        LIBFPTR_PARAM_OFD_ERROR,
        LIBFPTR_PARAM_FN_ERROR,
        LIBFPTR_PARAM_COMMAND_CODE,
        LIBFPTR_PARAM_PRINTER_TEMPERATURE,
        LIBFPTR_PARAM_RECORDS_TYPE,
        LIBFPTR_PARAM_OFD_FISCAL_SIGN,
        LIBFPTR_PARAM_HAS_OFD_TICKET,
        LIBFPTR_PARAM_NO_SERIAL_NUMBER,
        LIBFPTR_PARAM_RTC_FAULT,
        LIBFPTR_PARAM_SETTINGS_FAULT,
        LIBFPTR_PARAM_COUNTERS_FAULT,
        LIBFPTR_PARAM_USER_MEMORY_FAULT,
        LIBFPTR_PARAM_SERVICE_COUNTERS_FAULT,
        LIBFPTR_PARAM_ATTRIBUTES_FAULT,
        LIBFPTR_PARAM_FN_FAULT,
        LIBFPTR_PARAM_INVALID_FN,
        LIBFPTR_PARAM_HARD_FAULT,
        LIBFPTR_PARAM_MEMORY_MANAGER_FAULT,
        LIBFPTR_PARAM_SCRIPTS_FAULT,
        LIBFPTR_PARAM_FULL_RESET,
        LIBFPTR_PARAM_WAIT_FOR_REBOOT,
        LIBFPTR_PARAM_SCALE_PERCENT,
        LIBFPTR_PARAM_FN_NEED_REPLACEMENT,
        LIBFPTR_PARAM_FN_RESOURCE_EXHAUSTED,
        LIBFPTR_PARAM_FN_MEMORY_OVERFLOW,
        LIBFPTR_PARAM_FN_OFD_TIMEOUT,
        LIBFPTR_PARAM_FN_CRITICAL_ERROR,
        LIBFPTR_PARAM_OFD_MESSAGE_READ,
        LIBFPTR_PARAM_DEVICE_MIN_FFD_VERSION,
        LIBFPTR_PARAM_DEVICE_MAX_FFD_VERSION,
        LIBFPTR_PARAM_DEVICE_UPTIME,
        LIBFPTR_PARAM_NOMENCLATURE_TYPE,
        LIBFPTR_PARAM_GTIN,
        LIBFPTR_PARAM_FN_DOCUMENT_TYPE,
        LIBFPTR_PARAM_NETWORK_ERROR_TEXT,
        LIBFPTR_PARAM_FN_ERROR_TEXT,
        LIBFPTR_PARAM_OFD_ERROR_TEXT,
        LIBFPTR_PARAM_USER_SCRIPT_ID,
        LIBFPTR_PARAM_USER_SCRIPT_PARAMETER,
        LIBFPTR_PARAM_USER_MEMORY_OPERATION,
        LIBFPTR_PARAM_USER_MEMORY_DATA,
        LIBFPTR_PARAM_USER_MEMORY_STRING,
        LIBFPTR_PARAM_USER_MEMORY_ADDRESS,
        LIBFPTR_PARAM_FN_PRESENT,
        LIBFPTR_PARAM_BLOCKED,
        LIBFPTR_PARAM_DOCUMENT_PRINTED,
        LIBFPTR_PARAM_DISCOUNT_SUM,
        LIBFPTR_PARAM_SURCHARGE_SUM,
        LIBFPTR_PARAM_LK_USER_CODE,
        LIBFPTR_PARAM_LICENSE_COUNT,
        LIBFPTR_PARAM_DEFER,
        LIBFPTR_PARAM_CAP_54FZ,
        LIBFPTR_PARAM_CAP_MANUAL_CLICHE_CONTROL,
    ) = RANGE(65536, 65717)

    (
        LIBFPTR_OK,
        LIBFPTR_ERROR_CONNECTION_DISABLED,
        LIBFPTR_ERROR_NO_CONNECTION,
        LIBFPTR_ERROR_PORT_BUSY,
        LIBFPTR_ERROR_PORT_NOT_AVAILABLE,
        LIBFPTR_ERROR_INCORRECT_DATA,
        LIBFPTR_ERROR_INTERNAL,
        LIBFPTR_ERROR_UNSUPPORTED_CAST,
        LIBFPTR_ERROR_NO_REQUIRED_PARAM,
        LIBFPTR_ERROR_INVALID_SETTINGS,
        LIBFPTR_ERROR_NOT_CONFIGURED,
        LIBFPTR_ERROR_NOT_SUPPORTED,
        LIBFPTR_ERROR_INVALID_MODE,
        LIBFPTR_ERROR_INVALID_PARAM,
        LIBFPTR_ERROR_NOT_LOADED,
        LIBFPTR_ERROR_UNKNOWN,
        LIBFPTR_ERROR_INVALID_SUM,
        LIBFPTR_ERROR_INVALID_QUANTITY,
        LIBFPTR_ERROR_CASH_COUNTER_OVERFLOW,
        LIBFPTR_ERROR_LAST_OPERATION_STORNO_DENIED,
        LIBFPTR_ERROR_STORNO_BY_CODE_DENIED,
        LIBFPTR_ERROR_LAST_OPERATION_NOT_REPEATABLE,
        LIBFPTR_ERROR_DISCOUNT_NOT_REPEATABLE,
        LIBFPTR_ERROR_DISCOUNT_DENIED,
        LIBFPTR_ERROR_INVALID_COMMODITY_CODE,
        LIBFPTR_ERROR_INVALID_COMMODITY_BARCODE,
        LIBFPTR_ERROR_INVALID_COMMAND_FORMAT,
        LIBFPTR_ERROR_INVALID_COMMAND_LENGTH,
        LIBFPTR_ERROR_BLOCKED_IN_DATE_INPUT_MODE,
        LIBFPTR_ERROR_NEED_DATE_ACCEPT,
        LIBFPTR_ERROR_NO_MORE_DATA,
        LIBFPTR_ERROR_NO_ACCEPT_OR_CANCEL,
        LIBFPTR_ERROR_BLOCKED_BY_REPORT_INTERRUPTION,
        LIBFPTR_ERROR_DISABLE_CASH_CONTROL_DENIED,
        LIBFPTR_ERROR_MODE_BLOCKED,
        LIBFPTR_ERROR_CHECK_DATE_TIME,
        LIBFPTR_ERROR_DATE_TIME_LESS_THAN_FS,
        LIBFPTR_ERROR_CLOSE_ARCHIVE_DENIED,
        LIBFPTR_ERROR_COMMODITY_NOT_FOUND,
        LIBFPTR_ERROR_WEIGHT_BARCODE_WITH_INVALID_QUANTITY,
        LIBFPTR_ERROR_RECEIPT_BUFFER_OVERFLOW,
        LIBFPTR_ERROR_QUANTITY_TOO_FEW,
        LIBFPTR_ERROR_STORNO_TOO_MUCH,
        LIBFPTR_ERROR_BLOCKED_COMMODITY_NOT_FOUND,
        LIBFPTR_ERROR_NO_PAPER,
        LIBFPTR_ERROR_COVER_OPENED,
        LIBFPTR_ERROR_PRINTER_FAULT,
        LIBFPTR_ERROR_MECHANICAL_FAULT,
        LIBFPTR_ERROR_INVALID_RECEIPT_TYPE,
        LIBFPTR_ERROR_INVALID_UNIT_TYPE,
        LIBFPTR_ERROR_NO_MEMORY,
        LIBFPTR_ERROR_PICTURE_NOT_FOUND,
        LIBFPTR_ERROR_NONCACH_PAYMENTS_TOO_MUCH,
        LIBFPTR_ERROR_RETURN_DENIED,
        LIBFPTR_ERROR_PAYMENTS_OVERFLOW,
        LIBFPTR_ERROR_BUSY,
        LIBFPTR_ERROR_GSM,
        LIBFPTR_ERROR_INVALID_DISCOUNT,
        LIBFPTR_ERROR_OPERATION_AFTER_DISCOUNT_DENIED,
        LIBFPTR_ERROR_INVALID_DEPARTMENT,
        LIBFPTR_ERROR_INVALID_PAYMENT_TYPE,
        LIBFPTR_ERROR_MULTIPLICATION_OVERFLOW,
        LIBFPTR_ERROR_DENIED_BY_SETTINGS,
        LIBFPTR_ERROR_TOTAL_OVERFLOW,
        LIBFPTR_ERROR_DENIED_IN_ANNULATION_RECEIPT,
        LIBFPTR_ERROR_JOURNAL_OVERFLOW,
        LIBFPTR_ERROR_NOT_FULLY_PAID,
        LIBFPTR_ERROR_DENIED_IN_RETURN_RECEIPT,
        LIBFPTR_ERROR_SHIFT_EXPIRED,
        LIBFPTR_ERROR_DENIED_IN_SELL_RECEIPT,
        LIBFPTR_ERROR_FISCAL_MEMORY_OVERFLOW,
        LIBFPTR_ERROR_INVALID_PASSWORD,
        LIBFPTR_ERROR_JOURNAL_BUSY,
        LIBFPTR_ERROR_DENIED_IN_CLOSED_SHIFT,
        LIBFPTR_ERROR_INVALID_TABLE_NUMBER,
        LIBFPTR_ERROR_INVALID_ROW_NUMBER,
        LIBFPTR_ERROR_INVALID_FIELD_NUMBER,
        LIBFPTR_ERROR_INVALID_DATE_TIME,
        LIBFPTR_ERROR_INVALID_STORNO_SUM,
        LIBFPTR_ERROR_CHANGE_CALCULATION,
        LIBFPTR_ERROR_NO_CASH,
        LIBFPTR_ERROR_DENIED_IN_CLOSED_RECEIPT,
        LIBFPTR_ERROR_DENIED_IN_OPENED_RECEIPT,
        LIBFPTR_ERROR_DENIED_IN_OPENED_SHIFT,
        LIBFPTR_ERROR_SERIAL_NUMBER_ALREADY_ENTERED,
        LIBFPTR_ERROR_TOO_MUCH_REREGISTRATIONS,
        LIBFPTR_ERROR_INVALID_SHIFT_NUMBER,
        LIBFPTR_ERROR_INVALID_SERIAL_NUMBER,
        LIBFPTR_ERROR_INVALID_RNM_VATIN,
        LIBFPTR_ERROR_FISCAL_PRINTER_NOT_ACTIVATED,
        LIBFPTR_ERROR_SERIAL_NUMBER_NOT_ENTERED,
        LIBFPTR_ERROR_NO_MORE_REPORTS,
        LIBFPTR_ERROR_MODE_NOT_ACTIVATED,
        LIBFPTR_ERROR_RECORD_NOT_FOUND_IN_JOURNAL,
        LIBFPTR_ERROR_INVALID_LICENSE,
        LIBFPTR_ERROR_NEED_FULL_RESET,
        LIBFPTR_ERROR_DENIED_BY_LICENSE,
        LIBFPTR_ERROR_DISCOUNT_CANCELLATION_DENIED,
        LIBFPTR_ERROR_CLOSE_RECEIPT_DENIED,
        LIBFPTR_ERROR_INVALID_ROUTE_NUMBER,
        LIBFPTR_ERROR_INVALID_START_ZONE_NUMBER,
        LIBFPTR_ERROR_INVALID_END_ZONE_NUMBER,
        LIBFPTR_ERROR_INVALID_RATE_TYPE,
        LIBFPTR_ERROR_INVALID_RATE,
        LIBFPTR_ERROR_FISCAL_MODULE_EXCHANGE,
        LIBFPTR_ERROR_NEED_TECHNICAL_SUPPORT,
        LIBFPTR_ERROR_SHIFT_NUMBERS_DID_NOT_MATCH,
        LIBFPTR_ERROR_DEVICE_NOT_FOUND,
        LIBFPTR_ERROR_EXTERNAL_DEVICE_CONNECTION,
        LIBFPTR_ERROR_DISPENSER_INVALID_STATE,
        LIBFPTR_ERROR_INVALID_POSITIONS_COUNT,
        LIBFPTR_ERROR_DISPENSER_INVALID_NUMBER,
        LIBFPTR_ERROR_INVALID_DIVIDER,
        LIBFPTR_ERROR_FN_ACTIVATION_DENIED,
        LIBFPTR_ERROR_PRINTER_OVERHEAT,
        LIBFPTR_ERROR_FN_EXCHANGE,
        LIBFPTR_ERROR_FN_INVALID_FORMAT,
        LIBFPTR_ERROR_FN_INVALID_STATE,
        LIBFPTR_ERROR_FN_FAULT,
        LIBFPTR_ERROR_FN_CRYPTO_FAULT,
        LIBFPTR_ERROR_FN_EXPIRED,
        LIBFPTR_ERROR_FN_OVERFLOW,
        LIBFPTR_ERROR_FN_INVALID_DATE_TIME,
        LIBFPTR_ERROR_FN_NO_MORE_DATA,
        LIBFPTR_ERROR_FN_TOTAL_OVERFLOW,
        LIBFPTR_ERROR_BUFFER_OVERFLOW,
        LIBFPTR_ERROR_PRINT_SECOND_COPY_DENIED,
        LIBFPTR_ERROR_NEED_RESET_JOURNAL,
        LIBFPTR_ERROR_TAX_SUM_TOO_MUCH,
        LIBFPTR_ERROR_TAX_ON_LAST_OPERATION_DENIED,
        LIBFPTR_ERROR_INVALID_FN_NUMBER,
        LIBFPTR_ERROR_TAX_CANCEL_DENIED,
        LIBFPTR_ERROR_LOW_BATTERY,
        LIBFPTR_ERROR_FN_INVALID_COMMAND,
        LIBFPTR_ERROR_FN_COMMAND_OVERFLOW,
        LIBFPTR_ERROR_FN_NO_TRANSPORT_CONNECTION,
        LIBFPTR_ERROR_FN_CRYPTO_HAS_EXPIRED,
        LIBFPTR_ERROR_FN_RESOURCE_HAS_EXPIRED,
        LIBFPTR_ERROR_INVALID_MESSAGE_FROM_OFD,
        LIBFPTR_ERROR_FN_HAS_NOT_SEND_DOCUMENTS,
        LIBFPTR_ERROR_FN_TIMEOUT,
        LIBFPTR_ERROR_FN_SHIFT_EXPIRED,
        LIBFPTR_ERROR_FN_INVALID_TIME_DIFFERENCE,
        LIBFPTR_ERROR_INVALID_TAXATION_TYPE,
        LIBFPTR_ERROR_INVALID_TAX_TYPE,
        LIBFPTR_ERROR_INVALID_COMMODITY_PAYMENT_TYPE,
        LIBFPTR_ERROR_INVALID_COMMODITY_CODE_TYPE,
        LIBFPTR_ERROR_EXCISABLE_COMMODITY_DENIED,
        LIBFPTR_ERROR_FISCAL_PROPERTY_WRITE,
        LIBFPTR_ERROR_INVALID_COUNTER_TYPE,
        LIBFPTR_ERROR_CUTTER_FAULT,
        LIBFPTR_ERROR_REPORT_INTERRUPTED,
        LIBFPTR_ERROR_INVALID_LEFT_MARGIN,
        LIBFPTR_ERROR_INVALID_ALIGNMENT,
        LIBFPTR_ERROR_INVALID_TAX_MODE,
        LIBFPTR_ERROR_FILE_NOT_FOUND,
        LIBFPTR_ERROR_PICTURE_TOO_BIG,
        LIBFPTR_ERROR_INVALID_BARCODE_PARAMS,
        LIBFPTR_ERROR_FISCAL_PROPERTY_DENIED,
        LIBFPTR_ERROR_FN_INTERFACE,
        LIBFPTR_ERROR_DATA_DUPLICATE,
        LIBFPTR_ERROR_NO_REQUIRED_FISCAL_PROPERTY,
        LIBFPTR_ERROR_FN_READ_DOCUMENT,
        LIBFPTR_ERROR_FLOAT_OVERFLOW,
        LIBFPTR_ERROR_INVALID_SETTING_VALUE,
        LIBFPTR_ERROR_HARD_FAULT,
        LIBFPTR_ERROR_FN_NOT_FOUND,
        LIBFPTR_ERROR_INVALID_AGENT_FISCAL_PROPERTY,
        LIBFPTR_ERROR_INVALID_FISCAL_PROPERTY_VALUE_1002_1056,
        LIBFPTR_ERROR_INVALID_FISCAL_PROPERTY_VALUE_1002_1017,
        LIBFPTR_ERROR_SCRIPT,
        LIBFPTR_ERROR_INVALID_USER_MEMORY_INDEX,
        LIBFPTR_ERROR_NO_ACTIVE_OPERATOR,
        LIBFPTR_ERROR_REGISTRATION_REPORT_INTERRUPTED,
        LIBFPTR_ERROR_CLOSE_FN_REPORT_INTERRUPTED,
        LIBFPTR_ERROR_OPEN_SHIFT_REPORT_INTERRUPTED,
        LIBFPTR_ERROR_OFD_EXCHANGE_REPORT_INTERRUPTED,
        LIBFPTR_ERROR_CLOSE_RECEIPT_INTERRUPTED,
        LIBFPTR_ERROR_FN_QUERY_INTERRUPTED,
        LIBFPTR_ERROR_RTC_FAULT,
        LIBFPTR_ERROR_MEMORY_FAULT,
        LIBFPTR_ERROR_CHIP_FAULT,
        LIBFPTR_ERROR_TEMPLATES_CORRUPTED,
        LIBFPTR_ERROR_INVALID_MAC_ADDRESS,
        LIBFPTR_ERROR_INVALID_SCRIPT_NUMBER,
        LIBFPTR_ERROR_SCRIPTS_FAULT,
        LIBFPTR_ERROR_INVALID_SCRIPTS_VERSION,
        LIBFPTR_ERROR_INVALID_CLICHE_FORMAT,
        LIBFPTR_ERROR_WAIT_FOR_REBOOT,
        LIBFPTR_ERROR_NO_LICENSE,
        LIBFPTR_ERROR_INVALID_FFD_VERSION,
        LIBFPTR_ERROR_CHANGE_SETTING_DENIED,
        LIBFPTR_ERROR_INVALID_NOMENCLATURE_TYPE,
        LIBFPTR_ERROR_INVALID_GTIN,
        LIBFPTR_ERROR_NEGATIVE_MATH_RESULT,
        LIBFPTR_ERROR_FISCAL_PROPERTIES_COMBINATION,
        LIBFPTR_ERROR_OPERATOR_LOGIN,
        LIBFPTR_ERROR_INVALID_INTERNET_CHANNEL,
        LIBFPTR_ERROR_DATETIME_NOT_SYNCRONIZED,
        LIBFPTR_ERROR_JOURNAL,
        LIBFPTR_ERROR_DENIED_IN_OPENED_DOC,
        LIBFPTR_ERROR_DENIED_IN_CLOSED_DOC,
    ) = RANGE(0, 202)

    (
        LIBFPTR_ERROR_BASE_WEB,
        LIBFPTR_ERROR_RECEIPT_PARSE_ERROR,
        LIBFPTR_ERROR_INTERRUPTED_BY_PREVIOUS_ERRORS,
    ) = RANGE(500, 503)

    (
        LIBFPTR_PORT_COM,
        LIBFPTR_PORT_USB,
        LIBFPTR_PORT_TCPIP,
        LIBFPTR_PORT_BLUETOOTH,
    ) = RANGE(0, 4)

    (
        LIBFPTR_PORT_BITS_7,
        LIBFPTR_PORT_BITS_8,
    ) = RANGE(7, 9)

    (
        LIBFPTR_PORT_PARITY_NO,
        LIBFPTR_PORT_PARITY_ODD,
        LIBFPTR_PORT_PARITY_EVEN,
        LIBFPTR_PORT_PARITY_MARK,
        LIBFPTR_PORT_PARITY_SPACE,
    ) = RANGE(0, 5)

    (
        LIBFPTR_PORT_SB_1,
        LIBFPTR_PORT_SB_1_5,
        LIBFPTR_PORT_SB_2,
    ) = RANGE(0, 3)

    (
        LIBFPTR_BT_EAN_8,
        LIBFPTR_BT_EAN_13,
        LIBFPTR_BT_UPC_A,
        LIBFPTR_BT_UPC_E,
        LIBFPTR_BT_CODE_39,
        LIBFPTR_BT_CODE_93,
        LIBFPTR_BT_CODE_128,
        LIBFPTR_BT_CODABAR,
        LIBFPTR_BT_ITF,
        LIBFPTR_BT_ITF_14,
        LIBFPTR_BT_GS1_128,
        LIBFPTR_BT_QR,
        LIBFPTR_BT_PDF417,
        LIBFPTR_BT_AZTEC,
    ) = RANGE(0, 14)

    (
        LIBFPTR_BC_DEFAULT,
        LIBFPTR_BC_0,
        LIBFPTR_BC_1,
        LIBFPTR_BC_2,
        LIBFPTR_BC_3,
        LIBFPTR_BC_4,
        LIBFPTR_BC_5,
        LIBFPTR_BC_6,
        LIBFPTR_BC_7,
        LIBFPTR_BC_8,
    ) = RANGE(0, 10)

    (
        LIBFPTR_TM_POSITION,
        LIBFPTR_TM_UNIT,
    ) = RANGE(0, 2)

    (
        LIBFPTR_SCT_OVERALL,
        LIBFPTR_SCT_FORWARD,
    ) = RANGE(0, 2)

    (
        LIBFPTR_CT_ROLLUP,
        LIBFPTR_CT_RESETTABLE,
    ) = RANGE(0, 2)

    (
        LIBFPTR_SS_CLOSED,
        LIBFPTR_SS_OPENED,
        LIBFPTR_SS_EXPIRED,
    ) = RANGE(0, 3)

    (
        LIBFPTR_CT_FULL,
        LIBFPTR_CT_PART,
    ) = RANGE(0, 2)

    (
        LIBFPTR_ALIGNMENT_LEFT,
        LIBFPTR_ALIGNMENT_CENTER,
        LIBFPTR_ALIGNMENT_RIGHT,
    ) = RANGE(0, 3)

    (
        LIBFPTR_TW_NONE,
        LIBFPTR_TW_WORDS,
        LIBFPTR_TW_CHARS,
    ) = RANGE(0, 3)

    (
        LIBFPTR_FNT_DEBUG,
        LIBFPTR_FNT_RELEASE,
        LIBFPTR_FNT_UNKNOWN,
    ) = RANGE(0, 3)

    (
        LIBFPTR_RT_CLOSE_SHIFT,
        LIBFPTR_RT_X,
        LIBFPTR_RT_LAST_DOCUMENT,
        LIBFPTR_RT_OFD_EXCHANGE_STATUS,
        LIBFPTR_RT_KKT_DEMO,
        LIBFPTR_RT_KKT_INFO,
        LIBFPTR_RT_OFD_TEST,
        LIBFPTR_RT_FN_DOC_BY_NUMBER,
        LIBFPTR_RT_QUANTITY,
        LIBFPTR_RT_DEPARTMENTS,
        LIBFPTR_RT_OPERATORS,
        LIBFPTR_RT_HOURS,
        LIBFPTR_RT_FN_REGISTRATIONS,
        LIBFPTR_RT_FN_SHIFT_TOTAL_COUNTERS,
        LIBFPTR_RT_FN_TOTAL_COUNTERS,
        LIBFPTR_RT_FN_NOT_SENT_DOCUMENTS_COUNTERS,
        LIBFPTR_RT_COMMODITIES_BY_TAXATION_TYPES,
        LIBFPTR_RT_COMMODITIES_BY_DEPARTMENTS,
        LIBFPTR_RT_COMMODITIES_BY_SUMS,
        LIBFPTR_RT_START_SERVICE,
    ) = RANGE(0, 20)

    (
        LIBFPTR_PT_CASH,
        LIBFPTR_PT_ELECTRONICALLY,
        LIBFPTR_PT_PREPAID,
        LIBFPTR_PT_CREDIT,
        LIBFPTR_PT_OTHER,
        LIBFPTR_PT_6,
        LIBFPTR_PT_7,
        LIBFPTR_PT_8,
        LIBFPTR_PT_9,
        LIBFPTR_PT_10,
    ) = RANGE(0, 10)

    (
        LIBFPTR_TAX_DEPARTMENT,
        LIBFPTR_TAX_VAT18,
        LIBFPTR_TAX_VAT10,
        LIBFPTR_TAX_VAT118,
        LIBFPTR_TAX_VAT110,
        LIBFPTR_TAX_VAT0,
        LIBFPTR_TAX_NO,
    ) = RANGE(0, 7)

    (
        LIBFPTR_EXTERNAL_DEVICE_DISPLAY,
        LIBFPTR_EXTERNAL_DEVICE_PINPAD,
        LIBFPTR_EXTERNAL_DEVICE_MODEM,
        LIBFPTR_EXTERNAL_DEVICE_BARCODE_SCANNER,
    ) = RANGE(0, 4)

    (
        LIBFPTR_DT_STATUS,
        LIBFPTR_DT_CASH_SUM,
        LIBFPTR_DT_UNIT_VERSION,
        LIBFPTR_DT_PICTURE_INFO,
        LIBFPTR_DT_LICENSE_ACTIVATED,
        LIBFPTR_DT_REGISTRATIONS_SUM,
        LIBFPTR_DT_REGISTRATIONS_COUNT,
        LIBFPTR_DT_PAYMENT_SUM,
        LIBFPTR_DT_CASHIN_SUM,
        LIBFPTR_DT_CASHIN_COUNT,
        LIBFPTR_DT_CASHOUT_SUM,
        LIBFPTR_DT_CASHOUT_COUNT,
        LIBFPTR_DT_REVENUE,
        LIBFPTR_DT_DATE_TIME,
        LIBFPTR_DT_SHIFT_STATE,
        LIBFPTR_DT_RECEIPT_STATE,
        LIBFPTR_DT_SERIAL_NUMBER,
        LIBFPTR_DT_MODEL_INFO,
        LIBFPTR_DT_RECEIPT_LINE_LENGTH,
        LIBFPTR_DT_CUTTER_RESOURCE,
        LIBFPTR_DT_STEP_RESOURCE,
        LIBFPTR_DT_TERMAL_RESOURCE,
        LIBFPTR_DT_ENVD_MODE,
        LIBFPTR_DT_SHIFT_TAX_SUM,
        LIBFPTR_DT_RECEIPT_TAX_SUM,
        LIBFPTR_DT_NON_NULLABLE_SUM,
        LIBFPTR_DT_RECEIPT_COUNT,
        LIBFPTR_DT_CANCELLATION_COUNT_ALL,
        LIBFPTR_DT_CANCELLATION_SUM,
        LIBFPTR_DT_CANCELLATION_SUM_ALL,
        LIBFPTR_DT_POWER_SOURCE_STATE,
        LIBFPTR_DT_CANCELLATION_COUNT,
        LIBFPTR_DT_NON_NULLABLE_SUM_BY_PAYMENTS,
        LIBFPTR_DT_PRINTER_TEMPERATURE,
        LIBFPTR_DT_FATAL_STATUS,
        LIBFPTR_DT_MAC_ADDRESS,
        LIBFPTR_DT_DEVICE_UPTIME,
        LIBFPTR_DT_RECEIPT_BYTE_COUNT,
        LIBFPTR_DT_DISCOUNT_AND_SURCHARGE_SUM,
        LIBFPTR_DT_LK_USER_CODE,
        LIBFPTR_DT_LAST_SENT_OFD_DOCUMENT_DATE_TIME,
    ) = RANGE(0, 41)

    (
        LIBFPTR_FNDT_TAG_VALUE,
        LIBFPTR_FNDT_OFD_EXCHANGE_STATUS,
        LIBFPTR_FNDT_FN_INFO,
        LIBFPTR_FNDT_LAST_REGISTRATION,
        LIBFPTR_FNDT_LAST_RECEIPT,
        LIBFPTR_FNDT_LAST_DOCUMENT,
        LIBFPTR_FNDT_SHIFT,
        LIBFPTR_FNDT_FFD_VERSIONS,
        LIBFPTR_FNDT_VALIDITY,
        LIBFPTR_FNDT_REG_INFO,
        LIBFPTR_FNDT_DOCUMENTS_COUNT_IN_SHIFT,
        LIBFPTR_FNDT_ERRORS,
        LIBFPTR_FNDT_TICKET_BY_DOC_NUMBER,
        LIBFPTR_FNDT_DOCUMENT_BY_NUMBER,
    ) = RANGE(0, 14)

    (
        LIBFPTR_UT_FIRMWARE,
        LIBFPTR_UT_CONFIGURATION,
        LIBFPTR_UT_TEMPLATES,
        LIBFPTR_UT_CONTROL_UNIT,
        LIBFPTR_UT_BOOT,
    ) = RANGE(0, 5)

    (
        LIBFPTR_FNOP_REGISTRATION,
        LIBFPTR_FNOP_CHANGE_FN,
        LIBFPTR_FNOP_CHANGE_PARAMETERS,
        LIBFPTR_FNOP_CLOSE_ARCHIVE,
    ) = RANGE(0, 4)

    (
        LIBFPTR_OFD_CHANNEL_NONE,
        LIBFPTR_OFD_CHANNEL_USB,
        LIBFPTR_OFD_CHANNEL_PROTO,
    ) = RANGE(0, 3)

    (
        LIBFPTR_PST_POWER_SUPPLY,
        LIBFPTR_PST_RTC_BATTERY,
        LIBFPTR_PST_BATTERY,
    ) = RANGE(0, 3)

    (
        LIBFPTR_RT_LAST_DOCUMENT_LINES,
        LIBFPTR_RT_FN_DOCUMENT_TLVS,
        LIBFPTR_RT_EXEC_USER_SCRIPT,
    ) = RANGE(0, 3)

    (
        LIBFPTR_LOG_ERROR,
        LIBFPTR_LOG_WARN,
        LIBFPTR_LOG_INFO,
        LIBFPTR_LOG_DEBUG,
    ) = RANGE(0, 4)

    (
        LIBFPTR_NT_FURS,
        LIBFPTR_NT_MEDICINES,
        LIBFPTR_NT_TOBACCO,
    ) = RANGE(0, 3)

    (
        LIBFPTR_UMO_GET_SIZE,
        LIBFPTR_UMO_READ_DATA,
        LIBFPTR_UMO_WRITE_DATA,
        LIBFPTR_UMO_READ_STRING,
        LIBFPTR_UMO_WRITE_STRING,
        LIBFPTR_UMO_COMMIT,
    ) = RANGE(0, 6)

    (
        LIBFPTR_GUI_PARENT_NATIVE,
        LIBFPTR_GUI_PARENT_QT,
    ) = RANGE(0, 2)

    (
        LIBFPTR_DEFER_NONE,
        LIBFPTR_DEFER_PRE,
        LIBFPTR_DEFER_POST,
    ) = RANGE(0, 3)

    LIBFPTR_SETTING_LIBRARY_PATH = "LibraryPath"

    LIBFPTR_SETTING_MODEL = "Model"

    LIBFPTR_SETTING_PORT = "Port"

    LIBFPTR_SETTING_BAUDRATE = "BaudRate"

    LIBFPTR_SETTING_BITS = "Bits"

    LIBFPTR_SETTING_PARITY = "Parity"

    LIBFPTR_SETTING_STOPBITS = "StopBits"

    LIBFPTR_SETTING_IPADDRESS = "IPAddress"

    LIBFPTR_SETTING_IPPORT = "IPPort"

    LIBFPTR_SETTING_MACADDRESS = "MACAddress"

    LIBFPTR_SETTING_COM_FILE = "ComFile"

    LIBFPTR_SETTING_USB_DEVICE_PATH = "UsbDevicePath"

    LIBFPTR_SETTING_BT_AUTOENABLE = "AutoEnableBluetooth"

    LIBFPTR_SETTING_BT_AUTODISABLE = "AutoDisableBluetooth"

    LIBFPTR_SETTING_ACCESS_PASSWORD = "AccessPassword"

    LIBFPTR_SETTING_USER_PASSWORD = "UserPassword"

    LIBFPTR_SETTING_OFD_CHANNEL = "OfdChannel"

    LIBFPTR_SETTING_EXISTED_COM_FILES = "ExistedComFiles"

    LIBFPTR_MODEL_UNKNOWN = 0

    LIBFPTR_MODEL_ATOL_25F = 57

    LIBFPTR_MODEL_ATOL_30F = 61

    LIBFPTR_MODEL_ATOL_55F = 62

    LIBFPTR_MODEL_ATOL_22F = 63

    LIBFPTR_MODEL_ATOL_52F = 64

    LIBFPTR_MODEL_ATOL_11F = 67

    LIBFPTR_MODEL_ATOL_77F = 69

    LIBFPTR_MODEL_ATOL_90F = 72

    LIBFPTR_MODEL_ATOL_60F = 75

    LIBFPTR_MODEL_ATOL_42FS = 77

    LIBFPTR_MODEL_ATOL_15F = 78

    LIBFPTR_MODEL_ATOL_50F = 80

    LIBFPTR_MODEL_ATOL_20F = 81

    LIBFPTR_MODEL_ATOL_91F = 82

    LIBFPTR_MODEL_ATOL_92F = 84

    LIBFPTR_MODEL_ATOL_SIGMA_10 = 86

    LIBFPTR_MODEL_ATOL_50 = 100

    LIBFPTR_MODEL_ATOL_AUTO = 500

    LIBFPTR_PORT_BR_1200 = 1200

    LIBFPTR_PORT_BR_2400 = 2400

    LIBFPTR_PORT_BR_4800 = 4800

    LIBFPTR_PORT_BR_9600 = 9600

    LIBFPTR_PORT_BR_19200 = 19200

    LIBFPTR_PORT_BR_38400 = 38400

    LIBFPTR_PORT_BR_57600 = 57600

    LIBFPTR_PORT_BR_115200 = 115200

    LIBFPTR_FNS_INITIAL = 0

    LIBFPTR_FNS_CONFIGURED = 1

    LIBFPTR_FNS_FISCAL_MODE = 3

    LIBFPTR_FNS_POSTFISCAL_MODE = 7

    LIBFPTR_FNS_ACCESS_ARCHIVE = 15

    LIBFPTR_RT_CLOSED = 0

    LIBFPTR_RT_SELL = 1

    LIBFPTR_RT_SELL_RETURN = 2

    LIBFPTR_RT_SELL_CORRECTION = 7

    LIBFPTR_RT_SELL_RETURN_CORRECTION = 8

    LIBFPTR_RT_BUY = 4

    LIBFPTR_RT_BUY_RETURN = 5

    LIBFPTR_RT_BUY_CORRECTION = 9

    LIBFPTR_RT_BUY_RETURN_CORRECTION = 10

    LIBFPTR_FFD_UNKNOWN = 0

    LIBFPTR_FFD_1_0 = 100

    LIBFPTR_FFD_1_0_5 = 105

    LIBFPTR_FFD_1_1 = 110

    LIBFPTR_TT_DEFAULT = 0

    LIBFPTR_TT_OSN = 1

    LIBFPTR_TT_USN_INCOME = 2

    LIBFPTR_TT_USN_INCOME_OUTCOME = 4

    LIBFPTR_TT_ENVD = 8

    LIBFPTR_TT_ESN = 16

    LIBFPTR_TT_PATENT = 32

    LIBFPTR_AT_NONE = 0

    LIBFPTR_AT_BANK_PAYING_AGENT = 1

    LIBFPTR_AT_BANK_PAYING_SUBAGENT = 2

    LIBFPTR_AT_PAYING_AGENT = 4

    LIBFPTR_AT_PAYING_SUBAGENT = 8

    LIBFPTR_AT_ATTORNEY = 16

    LIBFPTR_AT_COMMISSION_AGENT = 32

    LIBFPTR_AT_ANOTHER = 64

    LIBFPTR_FN_DOC_REGISTRATION = 1

    LIBFPTR_FN_DOC_OPEN_SHIFT = 2

    LIBFPTR_FN_DOC_RECEIPT = 3

    LIBFPTR_FN_DOC_BSO = 4

    LIBFPTR_FN_DOC_CLOSE_SHIFT = 5

    LIBFPTR_FN_DOC_CLOSE_FN = 6

    LIBFPTR_FN_DOC_OPERATOR_CONFIRMATION = 7

    LIBFPTR_FN_DOC_REREGISTRATION = 11

    LIBFPTR_FN_DOC_EXCHANGE_STATUS = 21

    LIBFPTR_FN_DOC_CORRECTION = 31

    LIBFPTR_FN_DOC_BSO_CORRECTION = 41


    DEFAULT_BUFF_SIZE = 512

    CREATE_METHOD = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    DESTROY_METHOD = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    GET_VERSION_METHOD = ctypes.CFUNCTYPE(ctypes.c_char_p)

    METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                              ctypes.c_void_p)

    IS_OPENED_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                        ctypes.c_void_p)

    GET_ERROR_CODE_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                             ctypes.c_void_p)
    GET_ERROR_DESCRIPTION_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                                    ctypes.c_void_p,
                                                    ctypes.c_wchar_p,
                                                    ctypes.c_int)

    SET_SETTINGS_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                           ctypes.c_void_p,
                                           ctypes.c_wchar_p)
    GET_SETTINGS_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                           ctypes.c_void_p,
                                           ctypes.c_wchar_p,
                                           ctypes.c_int)

    SET_SINGLE_SETTING_METHOD = ctypes.CFUNCTYPE(None,
                                                 ctypes.c_void_p,
                                                 ctypes.c_wchar_p,
                                                 ctypes.c_wchar_p)
    GET_SINGLE_SETTING_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                                 ctypes.c_void_p,
                                                 ctypes.c_wchar_p,
                                                 ctypes.c_wchar_p,
                                                 ctypes.c_int)

    SET_BYTEARRAY_METHOD = ctypes.CFUNCTYPE(None,
                                            ctypes.c_void_p,
                                            ctypes.c_int,
                                            ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int)
    GET_BYTEARRAY_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                            ctypes.c_void_p,
                                            ctypes.c_int,
                                            ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int)

    SET_INT_METHOD = ctypes.CFUNCTYPE(None,
                                      ctypes.c_void_p,
                                      ctypes.c_int,
                                      ctypes.c_uint)
    GET_INT_METHOD = ctypes.CFUNCTYPE(ctypes.c_uint,
                                      ctypes.c_void_p,
                                      ctypes.c_int)

    SET_BOOL_METHOD = ctypes.CFUNCTYPE(None,
                                       ctypes.c_void_p,
                                       ctypes.c_int,
                                       ctypes.c_int)
    GET_BOOL_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                       ctypes.c_void_p,
                                       ctypes.c_int)

    SET_DOUBLE_METHOD = ctypes.CFUNCTYPE(None,
                                         ctypes.c_void_p,
                                         ctypes.c_int,
                                         ctypes.c_double)
    GET_DOUBLE_METHOD = ctypes.CFUNCTYPE(ctypes.c_double,
                                         ctypes.c_void_p,
                                         ctypes.c_int)

    SET_STRING_METHOD = ctypes.CFUNCTYPE(None,
                                         ctypes.c_void_p,
                                         ctypes.c_int,
                                         ctypes.c_wchar_p)
    GET_STRING_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                         ctypes.c_void_p,
                                         ctypes.c_int,
                                         ctypes.c_wchar_p, ctypes.c_int)

    SET_DATETIME_METHOD = ctypes.CFUNCTYPE(None,
                                           ctypes.c_void_p,
                                           ctypes.c_int,
                                           ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                           ctypes.c_int,
                                           ctypes.c_int)
    GET_DATETIME_METHOD = ctypes.CFUNCTYPE(None,
                                           ctypes.c_void_p,
                                           ctypes.c_int,
                                           ctypes.POINTER(ctypes.c_int),
                                           ctypes.POINTER(ctypes.c_int),
                                           ctypes.POINTER(ctypes.c_int),
                                           ctypes.POINTER(ctypes.c_int),
                                           ctypes.POINTER(ctypes.c_int),
                                           ctypes.POINTER(ctypes.c_int))

    LOG_WRITE_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                        ctypes.c_wchar_p,
                                        ctypes.c_int,
                                        ctypes.c_wchar_p)

    SHOW_PROPERTIES_METHOD = ctypes.CFUNCTYPE(ctypes.c_int,
                                              ctypes.c_void_p,
                                              ctypes.c_int,
                                              ctypes.c_void_p)

    def __init__(self, lib_path):
        assert sys.version_info >= (2, 6)
        self.lib_path = lib_path
        if platform.system() == 'Windows':
            if not self.lib_path.endswith('fptr10.dll'):
                self.lib_path = os.path.join(self.lib_path, 'fptr10.dll')
            try:
                ctypes.CDLL(os.path.join(os.path.dirname(self.lib_path), 'msvcp140.dll'), mode=ctypes.RTLD_LOCAL)
                self.library = ctypes.CDLL(self.lib_path, mode=ctypes.RTLD_LOCAL)
            except OSError:
                self.lib_path = os.path.join(QueryValueEx(OpenKey(HKEY_LOCAL_MACHINE, "Software\\ATOL\\Drivers\\10.0\\KKT"), "INSTALL_DIR")[0], 'bin\\fptr10.dll')
                ctypes.CDLL(os.path.join(os.path.dirname(self.lib_path), 'msvcp140.dll'), mode=ctypes.RTLD_LOCAL)
                self.library = ctypes.CDLL(self.lib_path, mode=ctypes.RTLD_LOCAL)
        else:
            if not self.lib_path.endswith('libfptr10.so'):
                self.lib_path = os.path.join(self.lib_path, 'libfptr10.so')
            self.library = ctypes.CDLL(self.lib_path, mode=ctypes.RTLD_LOCAL)

        self.interface = ctypes.c_void_p(0)
        _create = self.CREATE_METHOD(('libfptr_create', self.library))
        _create(ctypes.pointer(self.interface))

        self._setByteArray = self.SET_BYTEARRAY_METHOD(
            ('libfptr_set_param_bytearray', self.library))
        self._getByteArray = self.GET_BYTEARRAY_METHOD(
            ('libfptr_get_param_bytearray', self.library))
        self._setInt = self.SET_INT_METHOD(('libfptr_set_param_int', self.library))
        self._getInt = self.GET_INT_METHOD(('libfptr_get_param_int', self.library))
        self._setBool = self.SET_BOOL_METHOD(('libfptr_set_param_bool', self.library))
        self._getBool = self.GET_BOOL_METHOD(('libfptr_get_param_bool', self.library))
        self._setDouble = self.SET_DOUBLE_METHOD(('libfptr_set_param_double', self.library))
        self._getDouble = self.GET_DOUBLE_METHOD(('libfptr_get_param_double', self.library))
        self._setDateTime = self.SET_DATETIME_METHOD(('libfptr_set_param_datetime', self.library))
        self._getDateTime = self.GET_DATETIME_METHOD(('libfptr_get_param_datetime', self.library))
        self._setString = self.SET_STRING_METHOD(('libfptr_set_param_str', self.library))
        self._getString = self.GET_STRING_METHOD(('libfptr_get_param_str', self.library))
        self._setSettings = self.SET_SETTINGS_METHOD(('libfptr_set_settings', self.library))
        self._getSettings = self.GET_SETTINGS_METHOD(('libfptr_get_settings', self.library))
        self._getSingleSetting = self.GET_SINGLE_SETTING_METHOD(
            ('libfptr_get_single_setting', self.library))
        self._setSingleSetting = self.SET_SINGLE_SETTING_METHOD(
            ('libfptr_set_single_setting', self.library))
        self._getVersion = self.GET_VERSION_METHOD(('libfptr_get_version_string', self.library))
        self._isOpened = self.IS_OPENED_METHOD(('libfptr_is_opened', self.library))
        self._errorCode = self.GET_ERROR_CODE_METHOD(('libfptr_error_code', self.library))
        self._errorDescription = self.GET_ERROR_DESCRIPTION_METHOD(('libfptr_error_description', self.library))
        self._logWrite = self.LOG_WRITE_METHOD(('libfptr_log_write', self.library))
        self._showProperties = self.SHOW_PROPERTIES_METHOD(('libfptr_show_properties', self.library))

    def __del__(self):
        destroy = self.DESTROY_METHOD(('libfptr_destroy', self.library))
        destroy(ctypes.pointer(self.interface))

    def version(self):
        return self._getVersion()

    def logWrite(self, tag, level, message):
        return self._logWrite(tag, level, message)

    def showProperties(self, parentType, parent):
        return self._showProperties(self.interface, parentType, parent)

    def isOpened(self):
        return self._isOpened(self.interface)

    def errorCode(self):
        return self._errorCode(self.interface)

    def errorDescription(self):
        buff = ctypes.create_unicode_buffer(self.DEFAULT_BUFF_SIZE)
        size = self._errorDescription(self.interface, buff, self.DEFAULT_BUFF_SIZE)
        if size > self.DEFAULT_BUFF_SIZE:
            buff = ctypes.create_unicode_buffer(size)
            self._errorDescription(self.interface, buff, size)
        return buff.value

    def setSettings(self, settings):
        return self._setSettings(self.interface, json.dumps(settings))

    def getSettings(self):
        buff = ctypes.create_unicode_buffer(self.DEFAULT_BUFF_SIZE)
        size = self._getSettings(self.interface, buff, self.DEFAULT_BUFF_SIZE)
        if size > self.DEFAULT_BUFF_SIZE:
            buff = ctypes.create_unicode_buffer(size)
            self._getSettings(self.interface, buff, size)
        return json.loads(buff.value)

    def setSingleSetting(self, key, value):
        self._setSingleSetting(self.interface, key, value)

    def getSingleSetting(self, key):
        buff = ctypes.create_unicode_buffer(self.DEFAULT_BUFF_SIZE)
        size = self._getSingleSetting(self.interface, key, buff, self.DEFAULT_BUFF_SIZE)
        if size > self.DEFAULT_BUFF_SIZE:
            buff = ctypes.create_unicode_buffer(size)
            self._getSingleSetting(self.interface, key, buff, size)
        return buff.value

    def setParam(self, paramId, param):
        if isinstance(param, int):
            self._setInt(self.interface, ctypes.c_int(paramId), ctypes.c_uint(param))
        elif isinstance(param, bool):
            self._setBool(self.interface, ctypes.c_int(paramId), ctypes.c_int(param))
        elif isinstance(param, float):
            self._setDouble(self.interface, ctypes.c_int(paramId), ctypes.c_double(param))
        elif isinstance(param, list):
            self._setByteArray(self.interface, ctypes.c_int(paramId),
                               (ctypes.c_ubyte * len(param))(*param), len(param))
        elif isinstance(param, bytearray):
            self._setByteArray(self.interface, ctypes.c_int(paramId),
                               (ctypes.c_ubyte * len(param))(*param), len(param))
        elif isinstance(param, datetime.datetime):
            self._setDateTime(self.interface, ctypes.c_int(paramId), param.date().year,
                              param.date().month,
                              param.date().day,
                              param.time().hour, param.time().minute, param.time().second)
        elif isinstance(param, TEXT):
            self._setString(self.interface, ctypes.c_int(paramId), ctypes.c_wchar_p(param))
        else:
            raise Exception(u'Неподдерживаемый тип параметра')

    def getParamInt(self, paramId):
        value = self._getInt(self.interface, ctypes.c_int(paramId))
        return value

    def getParamBool(self, paramId):
        value = self._getBool(self.interface, ctypes.c_int(paramId))
        return value != 0

    def getParamDouble(self, paramId):
        value = self._getDouble(self.interface, ctypes.c_int(paramId))
        return value

    def getParamByteArray(self, paramId):
        value = (ctypes.c_ubyte * self.DEFAULT_BUFF_SIZE)()
        size = self._getByteArray(self.interface, ctypes.c_int(paramId),
                                  ctypes.cast(value, ctypes.POINTER(ctypes.c_ubyte)),
                                  self.DEFAULT_BUFF_SIZE)
        if size > self.DEFAULT_BUFF_SIZE:
            answer = (ctypes.c_ubyte * size)()
            size = self._getByteArray(self.interface, ctypes.c_int(paramId),
                                      ctypes.cast(value, ctypes.POINTER(ctypes.c_ubyte)), size)
        return value[:size]

    def getParamDateTime(self, paramId):
        year = ctypes.c_int(0)
        month = ctypes.c_int(0)
        day = ctypes.c_int(0)
        hour = ctypes.c_int(0)
        minute = ctypes.c_int(0)
        second = ctypes.c_int(0)
        self._getDateTime(self.interface, ctypes.c_int(paramId), ctypes.pointer(year),
                          ctypes.pointer(month),
                          ctypes.pointer(day),
                          ctypes.pointer(hour), ctypes.pointer(minute), ctypes.pointer(second))
        return datetime.datetime(year.value, month.value, day.value, hour.value, minute.value,
                                 second.value)

    def getParamString(self, paramId):
        value = ctypes.create_unicode_buffer(self.DEFAULT_BUFF_SIZE)
        size = self._getString(self.interface, ctypes.c_int(paramId), value, self.DEFAULT_BUFF_SIZE)
        if size > self.DEFAULT_BUFF_SIZE:
            value = ctypes.create_unicode_buffer(size)
            self._getString(self.interface, ctypes.c_int(paramId), value, size)
        return value.value

    def applySingleSettings(self):
        _method = self.METHOD(('libfptr_apply_single_settings', self.library))
        return _method(self.interface)

    def open(self):
        _method = self.METHOD(('libfptr_open', self.library))
        return _method(self.interface)

    def close(self):
        _method = self.METHOD(('libfptr_close', self.library))
        return _method(self.interface)

    def resetParams(self):
        _method = self.METHOD(('libfptr_reset_params', self.library))
        return _method(self.interface)

    def runCommand(self):
        _method = self.METHOD(('libfptr_run_command', self.library))
        return _method(self.interface)

    def beep(self):
        _method = self.METHOD(('libfptr_beep', self.library))
        return _method(self.interface)

    def openDrawer(self):
        _method = self.METHOD(('libfptr_open_drawer', self.library))
        return _method(self.interface)

    def cut(self):
        _method = self.METHOD(('libfptr_cut', self.library))
        return _method(self.interface)

    def devicePoweroff(self):
        _method = self.METHOD(('libfptr_device_poweroff', self.library))
        return _method(self.interface)

    def deviceReboot(self):
        _method = self.METHOD(('libfptr_device_reboot', self.library))
        return _method(self.interface)

    def openShift(self):
        _method = self.METHOD(('libfptr_open_shift', self.library))
        return _method(self.interface)

    def resetSummary(self):
        _method = self.METHOD(('libfptr_reset_summary', self.library))
        return _method(self.interface)

    def initDevice(self):
        _method = self.METHOD(('libfptr_init_device', self.library))
        return _method(self.interface)

    def queryData(self):
        _method = self.METHOD(('libfptr_query_data', self.library))
        return _method(self.interface)

    def cashIncome(self):
        _method = self.METHOD(('libfptr_cash_income', self.library))
        return _method(self.interface)

    def cashOutcome(self):
        _method = self.METHOD(('libfptr_cash_outcome', self.library))
        return _method(self.interface)

    def openReceipt(self):
        _method = self.METHOD(('libfptr_open_receipt', self.library))
        return _method(self.interface)

    def cancelReceipt(self):
        _method = self.METHOD(('libfptr_cancel_receipt', self.library))
        return _method(self.interface)

    def closeReceipt(self):
        _method = self.METHOD(('libfptr_close_receipt', self.library))
        return _method(self.interface)

    def checkDocumentClosed(self):
        _method = self.METHOD(('libfptr_check_document_closed', self.library))
        return _method(self.interface)

    def receiptTotal(self):
        _method = self.METHOD(('libfptr_receipt_total', self.library))
        return _method(self.interface)

    def receiptTax(self):
        _method = self.METHOD(('libfptr_receipt_tax', self.library))
        return _method(self.interface)

    def registration(self):
        _method = self.METHOD(('libfptr_registration', self.library))
        return _method(self.interface)

    def payment(self):
        _method = self.METHOD(('libfptr_payment', self.library))
        return _method(self.interface)

    def report(self):
        _method = self.METHOD(('libfptr_report', self.library))
        return _method(self.interface)

    def printText(self):
        _method = self.METHOD(('libfptr_print_text', self.library))
        return _method(self.interface)

    def printCliche(self):
        _method = self.METHOD(('libfptr_print_cliche', self.library))
        return _method(self.interface)

    def beginNonfiscalDocument(self):
        _method = self.METHOD(('libfptr_begin_nonfiscal_document', self.library))
        return _method(self.interface)

    def endNonfiscalDocument(self):
        _method = self.METHOD(('libfptr_end_nonfiscal_document', self.library))
        return _method(self.interface)

    def printBarcode(self):
        _method = self.METHOD(('libfptr_print_barcode', self.library))
        return _method(self.interface)

    def printPicture(self):
        _method = self.METHOD(('libfptr_print_picture', self.library))
        return _method(self.interface)

    def printPictureByNumber(self):
        _method = self.METHOD(('libfptr_print_picture_by_number', self.library))
        return _method(self.interface)

    def uploadPictureFromFile(self):
        _method = self.METHOD(('libfptr_upload_picture_from_file', self.library))
        return _method(self.interface)

    def clearPictures(self):
        _method = self.METHOD(('libfptr_clear_pictures', self.library))
        return _method(self.interface)

    def writeDeviceSettingRaw(self):
        _method = self.METHOD(('libfptr_write_device_setting_raw', self.library))
        return _method(self.interface)

    def readDeviceSettingRaw(self):
        _method = self.METHOD(('libfptr_read_device_setting_raw', self.library))
        return _method(self.interface)

    def commitSettings(self):
        _method = self.METHOD(('libfptr_commit_settings', self.library))
        return _method(self.interface)

    def initSettings(self):
        _method = self.METHOD(('libfptr_init_settings', self.library))
        return _method(self.interface)

    def resetSettings(self):
        _method = self.METHOD(('libfptr_reset_settings', self.library))
        return _method(self.interface)

    def writeDateTime(self):
        _method = self.METHOD(('libfptr_write_date_time', self.library))
        return _method(self.interface)

    def writeLicense(self):
        _method = self.METHOD(('libfptr_write_license', self.library))
        return _method(self.interface)

    def fnOperation(self):
        _method = self.METHOD(('libfptr_fn_operation', self.library))
        return _method(self.interface)

    def fnQueryData(self):
        _method = self.METHOD(('libfptr_fn_query_data', self.library))
        return _method(self.interface)

    def fnWriteAttributes(self):
        _method = self.METHOD(('libfptr_fn_write_attributes', self.library))
        return _method(self.interface)

    def externalDevicePowerOn(self):
        _method = self.METHOD(('libfptr_external_device_power_on', self.library))
        return _method(self.interface)

    def externalDevicePowerOff(self):
        _method = self.METHOD(('libfptr_external_device_power_off', self.library))
        return _method(self.interface)

    def externalDeviceWriteData(self):
        _method = self.METHOD(('libfptr_external_device_write_data', self.library))
        return _method(self.interface)

    def externalDeviceReadData(self):
        _method = self.METHOD(('libfptr_external_device_read_data', self.library))
        return _method(self.interface)

    def operatorLogin(self):
        _method = self.METHOD(('libfptr_operator_login', self.library))
        return _method(self.interface)

    def processJson(self):
        _method = self.METHOD(('libfptr_process_json', self.library))
        return _method(self.interface)

    def readDeviceSetting(self):
        _method = self.METHOD(('libfptr_read_device_setting', self.library))
        return _method(self.interface)

    def writeDeviceSetting(self):
        _method = self.METHOD(('libfptr_write_device_setting', self.library))
        return _method(self.interface)

    def beginReadRecords(self):
        _method = self.METHOD(('libfptr_begin_read_records', self.library))
        return _method(self.interface)

    def readNextRecord(self):
        _method = self.METHOD(('libfptr_read_next_record', self.library))
        return _method(self.interface)

    def endReadRecords(self):
        _method = self.METHOD(('libfptr_end_read_records', self.library))
        return _method(self.interface)

    def userMemoryOperation(self):
        _method = self.METHOD(('libfptr_user_memory_operation', self.library))
        return _method(self.interface)

    def continuePrint(self):
        _method = self.METHOD(('libfptr_continue_print', self.library))
        return _method(self.interface)

    def initMgm(self):
        _method = self.METHOD(('libfptr_init_mgm', self.library))
        return _method(self.interface)

    def utilFormTlv(self):
        _method = self.METHOD(('libfptr_util_form_tlv', self.library))
        return _method(self.interface)

    def utilFormNomenclature(self):
        _method = self.METHOD(('libfptr_util_form_nomenclature', self.library))
        return _method(self.interface)

    def utilMapping(self):
        _method = self.METHOD(('libfptr_util_mapping', self.library))
        return _method(self.interface)

    def readModelFlags(self):
        _method = self.METHOD(('libfptr_read_model_flags', self.library))
        return _method(self.interface)


