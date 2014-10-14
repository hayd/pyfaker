import unittest
from pyfaker.utils import call_fmt, to_camel, get_locales


class TestCallFormat(unittest.TestCase):

    def setUp(self):
        def f0(): return "fff"
        self.f0 = f0

        def f1(): pass

        def g0(): return "ggg"
        f1.g0 = g0
        self.f1 = f1

        def f2(): pass

        def g1(): pass

        def h0(): return "hhh"
        g1.h0 = h0
        f2.g1 = g1
        self.f2 = f2

        class A(object):

            @classmethod
            def b(self):
                return "bbb"

            def Bf(self):
                pass
            Bf.c = lambda: "ccc"

            class BC(object):

                @classmethod
                def c(self):
                    return "ccc"
        self.A = A

    def test_f0(self):
        result = call_fmt.format('{f0}', **self.__dict__)
        self.assertEqual(result, 'fff')

    def test_f1(self):
        result = call_fmt.format('{f1.g0}', **self.__dict__)
        self.assertEqual(result, 'ggg')

    def test_f2(self):
        result = call_fmt.format('{f2.g1.h0}', **self.__dict__)
        self.assertEqual(result, 'hhh')

    def test_A_b(self):
        result = call_fmt.format('{A.b}', **self.__dict__)
        self.assertEqual(result, 'bbb')

    def test_A_Bf_c(self):
        result = call_fmt.format('{A.Bf.c}', **self.__dict__)
        self.assertEqual(result, 'ccc')

    def test_A_BC_c(self):
        result = call_fmt.format('{A.BC.c}', **self.__dict__)
        self.assertEqual(result, 'ccc')
