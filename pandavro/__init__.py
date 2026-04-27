from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, Generator, Iterable, Optional

import fastavro
import numpy as np
import pandas as pd
from pandas import DatetimeTZDtype

NUMPY_TO_AVRO_TYPES = {
    np.dtype('?'): 'boolean',
    # pd.[U]Int[6/16/32/64]Dtype() is covered by these numpy types
    np.int8: 'int',
    np.int16: 'int',
    np.int32: 'int',
    np.uint8: {'type': 'int', 'unsigned': True},
    np.uint16: {'type': 'int', 'unsigned': True},
    np.uint32: {'type': 'int', 'unsigned': True},
    np.int64: 'long',
    np.uint64: {'type': 'long', 'unsigned': True},
    np.dtype('O'): 'complex',  # FIXME: Don't automatically store objects as strings
    np.str_: 'string',
    np.float32: 'float',
    np.float64: 'double',
    np.datetime64: {'type': 'long', 'logicalType': 'timestamp-micros'},
    DatetimeTZDtype: {'type': 'long', 'logicalType': 'timestamp-micros'},
    pd.Timestamp: {'type': 'long', 'logicalType': 'timestamp-micros'},
}

# This is used for forced conversion to Pandas NA-dtypes
AVRO_TO_PANDAS_TYPES = {}
# We use this extra dict for unsigned ints, adding it allows the dicts to stay a nice simple mapping
AVRO_TO_PANDAS_UNSIGNED_TYPES = {}

# This is used to convert Pandas NA-dtypes to python so fastavro can write
PANDAS_TO_PYTHON_TYPES = {}

# Pandas 0.24 added support for nullable integers. Include those in the supported
# integer dtypes if present, otherwise ignore them.

# Int8 and Int16 don't exist in Pandas NA-dtypes
AVRO_TO_PANDAS_TYPES['int'] = pd.Int32Dtype
AVRO_TO_PANDAS_TYPES['long'] = pd.Int64Dtype
AVRO_TO_PANDAS_UNSIGNED_TYPES['int'] = pd.UInt32Dtype

# Recognize these Pandas dtypes
NUMPY_TO_AVRO_TYPES[pd.StringDtype()] = 'string'
NUMPY_TO_AVRO_TYPES[pd.BooleanDtype()] = 'boolean'

# Convert these to python first
PANDAS_TO_PYTHON_TYPES[np.bool_] = bool

# Indicate the optional return datatype
AVRO_TO_PANDAS_TYPES['string'] = pd.StringDtype
AVRO_TO_PANDAS_TYPES['boolean'] = pd.BooleanDtype


def __type_infer(t):
    # Binary data has to be handled separately from the other dtypes because it
    # requires a parameter, the buffer size.
    pass


def __complex_field_infer(df, field, nested_record_names):
    pass


def __fields_infer(df, nested_record_names):
    pass


def __convert_field_micros_to_millis(field):
    pass


def schema_infer(df, times_as_micros=True):
    """
    Infers the Avro schema of a pandas DataFrame

    Args:
        df: DataFrame to infer the schema of
        times_as_micros:
            Whether timestamps should be stored as microseconds (default)
            or milliseconds (as expected by Apache Hive)
    """
    pass


def __file_to_dataframe(
    f,
    schema,
    na_dtypes=False,
    columns: Optional[Iterable[str]] = None,
    exclude: Optional[Iterable[str]] = None,
    nrows: Optional[int] = None,
    **kwargs,
):
    pass


def read_avro(file_path_or_buffer, schema=None, na_dtypes=False, columns: Optional[Iterable[str]] = None, **kwargs):
    """
    Avro file reader.

    Args:
        file_path_or_buffer: Input file path (str or pathlib.Path) or file-like object.
        schema: Avro schema.
        na_dtypes: Read int, long, string, boolean types back as Pandas NA-supporting datatypes.
        columns: Sequence, subset of columns to load in memory.
        **kwargs: Keyword argument to pandas.DataFrame.from_records.

    Returns:
        Class of pd.DataFrame.
    """
    pass


def from_avro(file_path_or_buffer, schema=None, na_dtypes=False, **kwargs):
    """
    Avro file reader.

    Delegates to the `read_avro` method to remain backward compatible.

    Args:
        file_path_or_buffer: Input file path or file-like object.
        schema: Avro schema.
        na_dtypes: Read int, long, string, boolean types back as Pandas NA-supporting datatypes.
        **kwargs: Keyword argument to pandas.DataFrame.from_records.

    Returns:
        Class of pd.DataFrame.
    """
    pass


def __to_fastavro_records(df: pd.DataFrame) -> Generator[Dict[str, Any], None, None]:
    "Converts a DataFrame to a fastavro record compatible iterable."
    pass


def to_avro(file_path_or_buffer, df, schema=None, append=False,
            times_as_micros=True, **kwargs):
    """
    Avro file writer.

    Args:
        file_path_or_buffer:
            Output file path (str or pathlib.Path) or file-like object.
        df: pd.DataFrame.
        schema: Dict of Avro schema.
            If it's set None, inferring schema.
        append: Boolean to control if will append to existing file
        times_as_micros: If True (default), save datetimes with microseconds resolution. If False, save with millisecond
            resolution instead.
        kwargs: Keyword arguments to fastavro.writer
    """
    pass
