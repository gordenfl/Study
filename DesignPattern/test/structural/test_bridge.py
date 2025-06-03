import unittest
from Structural import Bridge


class BridgeTest(unittest.TestCase):
    def test_CellPhoneWeixin(self):
        weixin = Bridge.MessageWeixin()
        email = Bridge.MessageEmail()
        sms = Bridge.MessageSMS()

        weixin_cellphone = Bridge.CellPhoneDevice(weixin)
        email_pc = Bridge.PCDevice(email)
        sms_notebook = Bridge.NotebookDevice(sms)
        #这里六个东西可以各种组合 
        
        message = "Hello world!"
        user = "all"

        obj1 = weixin_cellphone.SendMessage(message, user)
        #print(obj1)
        self.assertEqual(obj1, "From:Cellphone " +
                         "[send Weixin message]"+message+" To:"+user)

        obj2 = email_pc.SendMessage(message, user)
        #print(obj2)
        self.assertEqual(obj2, "From:PC " +
                         "[send Email message]"+message+" To:"+user)

        obj3 = sms_notebook.SendMessage(message, user)
        #print(obj3)
        self.assertEqual(obj3, "From:Notebook " +
                         "[send SMS message]"+message+" To:"+user)
