from abc import ABC, ABCMeta, abstractmethod


class MessageInterface(metaclass=ABCMeta):
    @abstractmethod
    def sendmessage(self, message, user):
        pass


class MessageSMS(MessageInterface):
    def sendmessage(self, message, user):
        return "[send SMS message]"+message+" To:"+user


class MessageWeixin(MessageInterface):
    def sendmessage(self, message, user):
        return "[send Weixin message]"+message+" To:"+user


class MessageEmail(MessageInterface):
    def sendmessage(self, message, user):
        return "[send Email message]"+message+" To:"+user


class ITDeviceInterface(metaclass=ABCMeta):
    def __init__(self, messager):
        self.bridge = messager

    def SendMessage(self, msg, user):
        return self.bridge.sendmessage(msg, user)


class PCDevice(ITDeviceInterface):
    def __init__(self, messager):
        super().__init__(messager)

    def SendMessage(self, message, user):
        return "From:PC "+super().SendMessage(message, user)


class CellPhoneDevice(ITDeviceInterface):
    def __init__(self, messager):
        super().__init__(messager)

    def SendMessage(self, message, user):
        return "From:Cellphone "+super().SendMessage(message, user)


class NotebookDevice(ITDeviceInterface):
    def __init__(self, messager):
        super().__init__(messager)

    def SendMessage(self, message, user):
        return "From:Notebook "+super().SendMessage(message, user)
