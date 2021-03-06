

from bson.binary import Binary
from bson.code import Code
from bson.int64 import Int64
from bson.decimal128 import Decimal128
from bson.py3compat import PY3


def test_qop_ne_1(monty_find, mongo_find):
    docs = [
        {"a": 1},
        {"a": 0}
    ]
    spec = {"a": {"$ne": 1}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    assert mongo_c.count() == 1
    assert monty_c.count() == mongo_c.count()
    assert next(mongo_c) == next(monty_c)


def test_qop_ne_2(monty_find, mongo_find):
    docs = [
        {"a": [1]},
        {"a": 1}
    ]
    spec = {"a": {"$ne": 1}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    assert mongo_c.count() == 0
    assert monty_c.count() == mongo_c.count()


def test_qop_ne_3(monty_find, mongo_find):
    docs = [
        {"a": [1]},
        {"a": [[1], 2]}
    ]
    spec = {"a": {"$ne": [1]}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    assert mongo_c.count() == 0
    assert monty_c.count() == mongo_c.count()


def test_qop_ne_4(monty_find, mongo_find):
    docs = [
        {"a": [2, 1]},
        {"a": [1, 2]},
        {"a": [[2, 1], 3]},
        {"a": [[1, 2], 3]},
    ]
    spec = {"a": {"$ne": [2, 1]}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    assert mongo_c.count() == 2
    assert monty_c.count() == mongo_c.count()
    for i in range(2):
        assert next(mongo_c) == next(monty_c)


def test_qop_ne_5(monty_find, mongo_find):
    docs = [
        {"a": [{"b": Binary(b"00")}]},
        {"a": [{"b": Binary(b"01")}]},
    ]
    spec = {"a.b": {"$ne": b"01"}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    count = 1 if PY3 else 2
    assert mongo_c.count() == count
    assert monty_c.count() == mongo_c.count()
    for i in range(count):
        assert next(mongo_c) == next(monty_c)


def test_qop_ne_6(monty_find, mongo_find):
    docs = [
        {"a": [{"b": Code("a")}]},
    ]
    spec = {"a.b": {"$ne": "a"}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    assert mongo_c.count() == 1
    assert monty_c.count() == mongo_c.count()


def test_qop_ne_7(monty_find, mongo_find):
    docs = [
        {"a": [{"b": "a"}]},
    ]
    spec = {"a.b": {"$ne": Code("a")}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    assert mongo_c.count() == 1
    assert monty_c.count() == mongo_c.count()


def test_qop_ne_8(monty_find, mongo_find):
    docs = [
        {"a": 1},
    ]
    spec = {"a": {"$ne": Int64(1)}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    assert mongo_c.count() == 0
    assert monty_c.count() == mongo_c.count()


def test_qop_ne_9(monty_find, mongo_find):
    docs = [
        {"a": 1},
        {"a": 1.0},
    ]
    spec = {"a": {"$ne": Decimal128("1")}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    assert mongo_c.count() == 0
    assert monty_c.count() == mongo_c.count()


def test_qop_ne_10(monty_find, mongo_find):
    docs = [
        {"a": 1},
        {"a": 1.0},
    ]
    spec = {"a": {"$ne": Decimal128("1.0")}}

    monty_c = monty_find(docs, spec)
    mongo_c = mongo_find(docs, spec)

    assert mongo_c.count() == 0
    assert monty_c.count() == mongo_c.count()
