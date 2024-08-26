from ..type_impls import *


def test_record_type_order():
    A = RecordType(Record("A", "A", 0, [("foo", IntegerInstanceType)]))
    B = RecordType(Record("B", "B", 1, [("bar", IntegerInstanceType)]))
    C = RecordType(Record("C", "C", 2, [("baz", IntegerInstanceType)]))
    a = A
    b = B
    c = C

    assert a >= a
    assert not a >= b
    assert not b >= a
    assert not a >= c
    assert not c >= a
    assert not b >= c
    assert not c >= b

    A = RecordType(Record("A", "A", 0, [("foo", IntegerInstanceType)]))
    B = RecordType(
        Record(
            "B", "B", 0, [("foo", IntegerInstanceType), ("bar", IntegerInstanceType)]
        )
    )
    C = RecordType(Record("C", "C", 0, [("foo", InstanceType(AnyType()))]))
    assert not A >= B
    assert not C >= B
    assert C >= A


def test_union_type_order():
    A = RecordType(Record("A", "A", 0, [("foo", IntegerInstanceType)]))
    B = RecordType(Record("B", "B", 1, [("bar", IntegerInstanceType)]))
    C = RecordType(Record("C", "C", 2, [("baz", IntegerInstanceType)]))
    abc = UnionType([A, B, C])
    ab = UnionType([A, B])
    a = A
    c = C

    assert a >= a
    assert ab >= a
    assert not a >= ab
    assert abc >= ab
    assert not ab >= abc
    assert not c >= a
    assert not a >= c
    assert abc >= c
    assert not ab >= c


def test_list_type_equality():
    type1 = Type()  # Replace with the actual way to instantiate `Type`
    type2 = Type()  # Another `Type` object, could be the same or different

    list1 = ListType(typ=type1)
    list2 = ListType(typ=type1)
    list3 = ListType(typ=type2)

    assert list1 == list2
    assert list1 != list3
