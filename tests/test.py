import unittest

from pipe_operator import (
    padd, psub, pmul, pmatmul, ptruediv, pfloordiv, pmod, ppow,
    pneg, ppos, pabs, pinvert, pnot_, pindex, ptruth,
    plshift, prshift, pand_, por_, pxor,
    peq, pne, plt, ple, pgt, pge,
    pconcat, pcontains, pcountOf, pindexOf, plength_hint,
    getitem, setitem, delitem, iconcat,
    pitemgetter, pattrgetter, pmethodcaller,
)


class TestArithmetic(unittest.TestCase):
    def test_basic_arithmetic(self):
        self.assertEqual(2 | padd(3), 5)
        self.assertEqual(5 | psub(2), 3)
        self.assertEqual(4 | pmul(3), 12)
        self.assertEqual(7 | pfloordiv(2), 3)
        self.assertEqual(7 | ptruediv(2), 3.5)
        self.assertEqual(7 | pmod(3), 1)
        self.assertEqual(2 | ppow(3), 8)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 | ptruediv(0)


class TestUnary(unittest.TestCase):
    def test_unary_ops(self):
        self.assertEqual(5 | pneg(), -5)
        self.assertEqual(-7 | ppos(), -7)
        self.assertEqual(-7 | pabs(), 7)

    def test_not_index_truth(self):
        self.assertIs(True  | pnot_(), False)
        self.assertIs(False | pnot_(), True)
        self.assertEqual(10 | pindex(), 10)
        self.assertIs([] | ptruth(), False)
        self.assertIs([0] | ptruth(), True)


class TestBitwise(unittest.TestCase):
    def test_bitwise_and_shifts(self):
        self.assertEqual(5 | pand_(3), 1)
        self.assertEqual(5 | por_(2), 7)
        self.assertEqual(5 | pxor(1), 4)
        self.assertEqual(1 | plshift(3), 8)
        self.assertEqual(8 | prshift(2), 2)


class TestComparisons(unittest.TestCase):
    def test_comparisons(self):
        self.assertIs(2 | peq(2), True)
        self.assertIs(2 | pne(3), True)
        self.assertIs(2 | plt(3), True)
        self.assertIs(2 | ple(2), True)
        self.assertIs(3 | pgt(2), True)
        self.assertIs(3 | pge(3), True)


class TestSequencesAndMappings(unittest.TestCase):
    def test_concat_and_iconcat(self):
        # concat (returns new object)
        self.assertEqual([1] | pconcat([2]), [1, 2])

        # iconcat (in-place; returns the same object)
        lst = [1]
        result = lst | iconcat([2, 3])
        self.assertIs(result, lst)
        self.assertEqual(lst, [1, 2, 3])

    def test_contains_count_index_length_hint(self):
        s = "banana"
        self.assertIs(s | pcontains("na"), True)
        self.assertEqual(s | pcountOf("a"), 3)
        self.assertEqual(s | pindexOf("a"), 1)
        self.assertEqual([1, 2, 3] | plength_hint(), 3)


class TestItemAccessAndMutation(unittest.TestCase):
    def test_getitem_setitem_delitem(self):
        data = {"x": 1}
        # getitem
        self.assertEqual(data | getitem("x"), 1)

        # setitem returns None but mutates in-place
        ret = data | setitem("y", 2)
        self.assertIs(ret, None)
        self.assertEqual(data["y"], 2)

        # delitem returns None and mutates in-place
        ret = data | delitem("x")
        self.assertIs(ret, None)
        self.assertNotIn("x", data)


class Obj:
    def __init__(self):
        self.a = {"k": 10}
    def greet(self, name):
        return f"hi {name}"


class TestFactories(unittest.TestCase):
    def test_itemgetter_attrgetter_methodcaller(self):
        # itemgetter against mapping
        self.assertEqual({"k": 10} | pitemgetter("k"), 10)

        # attrgetter to fetch attribute
        o = Obj()
        self.assertEqual(o | pattrgetter("a"), {"k": 10})

        # methodcaller to invoke a method
        self.assertEqual("abc" | pmethodcaller("upper"), "ABC")
        self.assertEqual(o | pmethodcaller("greet", "sam"), "hi sam")


if __name__ == "__main__":
    unittest.main()


