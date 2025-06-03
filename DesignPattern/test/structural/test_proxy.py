import unittest

from Structural import Proxy


class ProxyTest(unittest.TestCase):
    def test_Proxy(self):
        teacher = Proxy.TeacherDAO()
        proxy_teacher = Proxy.TeacherDAOProxy(teacher)
        self.assertEqual(teacher.doClass(), proxy_teacher.doClass())
