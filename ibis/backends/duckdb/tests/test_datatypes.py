import pytest
from pytest import param

import ibis.expr.datatypes as dt
from ibis.backends.duckdb.datatypes import parse


@pytest.mark.parametrize(
    ("typ", "expected"),
    [
        param(typ, expected, id=typ.lower())
        for typ, expected in [
            ("BIGINT", dt.int64),
            ("INT8", dt.int64),
            ("LONG", dt.int64),
            ("BOOLEAN", dt.boolean),
            ("BOOL", dt.boolean),
            ("LOGICAL", dt.boolean),
            ("BLOB", dt.binary),
            ("BYTEA", dt.binary),
            ("BINARY", dt.binary),
            ("VARBINARY", dt.binary),
            ("DATE", dt.date),
            ("DOUBLE", dt.float64),
            ("FLOAT8", dt.float64),
            ("NUMERIC", dt.Decimal(18, 3)),
            ("DECIMAL", dt.Decimal(18, 3)),
            ("DECIMAL(10, 3)", dt.Decimal(10, 3)),
            ("INTEGER", dt.int32),
            ("INT4", dt.int32),
            ("INT", dt.int32),
            ("SIGNED", dt.int32),
            ("INTERVAL", dt.interval),
            ("REAL", dt.float32),
            ("FLOAT4", dt.float32),
            ("FLOAT", dt.float32),
            ("SMALLINT", dt.int16),
            ("INT2", dt.int16),
            ("SHORT", dt.int16),
            ("TIME", dt.time),
            ("TIMESTAMP", dt.Timestamp("UTC")),
            ("DATETIME", dt.Timestamp("UTC")),
            ("TINYINT", dt.int8),
            ("INT1", dt.int8),
            ("UBIGINT", dt.uint64),
            ("UINTEGER", dt.uint32),
            ("USMALLINT", dt.uint16),
            ("UTINYINT", dt.uint8),
            ("UUID", dt.uuid),
            ("VARCHAR", dt.string),
            ("CHAR", dt.string),
            ("BPCHAR", dt.string),
            ("TEXT", dt.string),
            ("STRING", dt.string),
            ("INTEGER[]", dt.Array(dt.int32)),
            ("MAP(STRING, BIGINT)", dt.Map(dt.string, dt.int64)),
            (
                "STRUCT(a INT, b TEXT, c MAP(TEXT, FLOAT8[])[])",
                dt.Struct(
                    dict(
                        a=dt.int32,
                        b=dt.string,
                        c=dt.Array(dt.Map(dt.string, dt.Array(dt.float64))),
                    )
                ),
            ),
            ("INTEGER[][]", dt.Array(dt.Array(dt.int32))),
            ("TIMESTAMP_TZ", dt.Timestamp("UTC")),
            ("TIMESTAMP_SEC", dt.Timestamp("UTC", scale=0)),
            ("TIMESTAMP_S", dt.Timestamp("UTC", scale=0)),
            ("TIMESTAMP_MS", dt.Timestamp("UTC", scale=3)),
            ("TIMESTAMP_US", dt.Timestamp("UTC", scale=6)),
            ("TIMESTAMP_NS", dt.Timestamp("UTC", scale=9)),
            ("JSON", dt.json),
        ]
    ],
)
def test_parser(typ, expected):
    ty = parse(typ)
    assert ty == expected
