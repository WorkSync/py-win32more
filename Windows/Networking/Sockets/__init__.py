from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Background
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Networking.Connectivity
import Windows.Networking.Sockets
import Windows.Security.Credentials
import Windows.Security.Cryptography.Certificates
import Windows.Storage.Streams
import Windows.Web
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class BandwidthStatistics(EasyCastStructure):
    OutboundBitsPerSecond: UInt64
    InboundBitsPerSecond: UInt64
    OutboundBitsPerSecondInstability: UInt64
    InboundBitsPerSecondInstability: UInt64
    OutboundBandwidthPeaked: Boolean
    InboundBandwidthPeaked: Boolean
class ControlChannelTrigger(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.ControlChannelTrigger'
    @winrt_factorymethod
    def CreateControlChannelTrigger(cls: Windows.Networking.Sockets.IControlChannelTriggerFactory, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
    @winrt_factorymethod
    def CreateControlChannelTriggerEx(cls: Windows.Networking.Sockets.IControlChannelTriggerFactory, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32, resourceRequestType: Windows.Networking.Sockets.ControlChannelTriggerResourceType) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
    @winrt_mixinmethod
    def get_ControlChannelTriggerId(self: Windows.Networking.Sockets.IControlChannelTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerKeepAliveIntervalInMinutes(self: Windows.Networking.Sockets.IControlChannelTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def put_ServerKeepAliveIntervalInMinutes(self: Windows.Networking.Sockets.IControlChannelTrigger, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentKeepAliveIntervalInMinutes(self: Windows.Networking.Sockets.IControlChannelTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def get_TransportObject(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_KeepAliveTrigger(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def get_PushNotificationTrigger(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def UsingTransport(self: Windows.Networking.Sockets.IControlChannelTrigger, transport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def WaitForPushEnabled(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
    @winrt_mixinmethod
    def DecreaseNetworkKeepAliveInterval(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Void: ...
    @winrt_mixinmethod
    def FlushTransport(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_IsWakeFromLowPowerSupported(self: Windows.Networking.Sockets.IControlChannelTrigger2) -> Boolean: ...
    ControlChannelTriggerId = property(get_ControlChannelTriggerId, None)
    ServerKeepAliveIntervalInMinutes = property(get_ServerKeepAliveIntervalInMinutes, put_ServerKeepAliveIntervalInMinutes)
    CurrentKeepAliveIntervalInMinutes = property(get_CurrentKeepAliveIntervalInMinutes, None)
    TransportObject = property(get_TransportObject, None)
    KeepAliveTrigger = property(get_KeepAliveTrigger, None)
    PushNotificationTrigger = property(get_PushNotificationTrigger, None)
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
ControlChannelTriggerContract: UInt32 = 196608
ControlChannelTriggerResetReason = Int32
ControlChannelTriggerResetReason_FastUserSwitched: ControlChannelTriggerResetReason = 0
ControlChannelTriggerResetReason_LowPowerExit: ControlChannelTriggerResetReason = 1
ControlChannelTriggerResetReason_QuietHoursExit: ControlChannelTriggerResetReason = 2
ControlChannelTriggerResetReason_ApplicationRestart: ControlChannelTriggerResetReason = 3
ControlChannelTriggerResourceType = Int32
ControlChannelTriggerResourceType_RequestSoftwareSlot: ControlChannelTriggerResourceType = 0
ControlChannelTriggerResourceType_RequestHardwareSlot: ControlChannelTriggerResourceType = 1
ControlChannelTriggerStatus = Int32
ControlChannelTriggerStatus_HardwareSlotRequested: ControlChannelTriggerStatus = 0
ControlChannelTriggerStatus_SoftwareSlotAllocated: ControlChannelTriggerStatus = 1
ControlChannelTriggerStatus_HardwareSlotAllocated: ControlChannelTriggerStatus = 2
ControlChannelTriggerStatus_PolicyError: ControlChannelTriggerStatus = 3
ControlChannelTriggerStatus_SystemError: ControlChannelTriggerStatus = 4
ControlChannelTriggerStatus_TransportDisconnected: ControlChannelTriggerStatus = 5
ControlChannelTriggerStatus_ServiceUnavailable: ControlChannelTriggerStatus = 6
class DatagramSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.DatagramSocket'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Sockets.DatagramSocket: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IDatagramSocket) -> Windows.Networking.Sockets.DatagramSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IDatagramSocket) -> Windows.Networking.Sockets.DatagramSocketInformation: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IDatagramSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Networking.Sockets.IDatagramSocket, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectWithEndpointPairAsync(self: Windows.Networking.Sockets.IDatagramSocket, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindServiceNameAsync(self: Windows.Networking.Sockets.IDatagramSocket, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindEndpointAsync(self: Windows.Networking.Sockets.IDatagramSocket, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def JoinMulticastGroup(self: Windows.Networking.Sockets.IDatagramSocket, host: Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def GetOutputStreamAsync(self: Windows.Networking.Sockets.IDatagramSocket, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IOutputStream]: ...
    @winrt_mixinmethod
    def GetOutputStreamWithEndpointPairAsync(self: Windows.Networking.Sockets.IDatagramSocket, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IOutputStream]: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: Windows.Networking.Sockets.IDatagramSocket, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.DatagramSocket, Windows.Networking.Sockets.DatagramSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: Windows.Networking.Sockets.IDatagramSocket, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def BindServiceNameAndAdapterAsync(self: Windows.Networking.Sockets.IDatagramSocket2, localServiceName: WinRT_String, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelIOAsync(self: Windows.Networking.Sockets.IDatagramSocket3) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableTransferOwnership(self: Windows.Networking.Sockets.IDatagramSocket3, taskId: Guid) -> Void: ...
    @winrt_mixinmethod
    def EnableTransferOwnershipWithConnectedStandbyAction(self: Windows.Networking.Sockets.IDatagramSocket3, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnership(self: Windows.Networking.Sockets.IDatagramSocket3, socketId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContext(self: Windows.Networking.Sockets.IDatagramSocket3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContextAndKeepAliveTime(self: Windows.Networking.Sockets.IDatagramSocket3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def GetEndpointPairsAsync(cls: Windows.Networking.Sockets.IDatagramSocketStatics, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    @winrt_classmethod
    def GetEndpointPairsWithSortOptionsAsync(cls: Windows.Networking.Sockets.IDatagramSocketStatics, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class DatagramSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.DatagramSocketControl'
    @winrt_mixinmethod
    def get_QualityOfService(self: Windows.Networking.Sockets.IDatagramSocketControl) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_mixinmethod
    def put_QualityOfService(self: Windows.Networking.Sockets.IDatagramSocketControl, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IDatagramSocketControl) -> Byte: ...
    @winrt_mixinmethod
    def put_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IDatagramSocketControl, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_InboundBufferSizeInBytes(self: Windows.Networking.Sockets.IDatagramSocketControl2) -> UInt32: ...
    @winrt_mixinmethod
    def put_InboundBufferSizeInBytes(self: Windows.Networking.Sockets.IDatagramSocketControl2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DontFragment(self: Windows.Networking.Sockets.IDatagramSocketControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_DontFragment(self: Windows.Networking.Sockets.IDatagramSocketControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MulticastOnly(self: Windows.Networking.Sockets.IDatagramSocketControl3) -> Boolean: ...
    @winrt_mixinmethod
    def put_MulticastOnly(self: Windows.Networking.Sockets.IDatagramSocketControl3, value: Boolean) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
    InboundBufferSizeInBytes = property(get_InboundBufferSizeInBytes, put_InboundBufferSizeInBytes)
    DontFragment = property(get_DontFragment, put_DontFragment)
    MulticastOnly = property(get_MulticastOnly, put_MulticastOnly)
class DatagramSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.DatagramSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IDatagramSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_LocalPort(self: Windows.Networking.Sockets.IDatagramSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteAddress(self: Windows.Networking.Sockets.IDatagramSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemotePort(self: Windows.Networking.Sockets.IDatagramSocketInformation) -> WinRT_String: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
class DatagramSocketMessageReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.DatagramSocketMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_RemoteAddress(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemotePort(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def GetDataReader(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> Windows.Storage.Streams.DataReader: ...
    @winrt_mixinmethod
    def GetDataStream(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> Windows.Storage.Streams.IInputStream: ...
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
    LocalAddress = property(get_LocalAddress, None)
class IControlChannelTrigger(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7d1431a7-ee96-40e8-a1-99-87-03-cd-96-9e-c3')
    @winrt_commethod(6)
    def get_ControlChannelTriggerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServerKeepAliveIntervalInMinutes(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ServerKeepAliveIntervalInMinutes(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_CurrentKeepAliveIntervalInMinutes(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_TransportObject(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(11)
    def get_KeepAliveTrigger(self) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_commethod(12)
    def get_PushNotificationTrigger(self) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_commethod(13)
    def UsingTransport(self, transport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(14)
    def WaitForPushEnabled(self) -> Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
    @winrt_commethod(15)
    def DecreaseNetworkKeepAliveInterval(self) -> Void: ...
    @winrt_commethod(16)
    def FlushTransport(self) -> Void: ...
    ControlChannelTriggerId = property(get_ControlChannelTriggerId, None)
    ServerKeepAliveIntervalInMinutes = property(get_ServerKeepAliveIntervalInMinutes, put_ServerKeepAliveIntervalInMinutes)
    CurrentKeepAliveIntervalInMinutes = property(get_CurrentKeepAliveIntervalInMinutes, None)
    TransportObject = property(get_TransportObject, None)
    KeepAliveTrigger = property(get_KeepAliveTrigger, None)
    PushNotificationTrigger = property(get_PushNotificationTrigger, None)
class IControlChannelTrigger2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('af00d237-51be-4514-97-25-35-56-e1-87-95-80')
    @winrt_commethod(6)
    def get_IsWakeFromLowPowerSupported(self) -> Boolean: ...
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
class IControlChannelTriggerEventDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1b36e047-89bb-4236-96-ac-71-d0-12-bb-48-69')
    @winrt_commethod(6)
    def get_ControlChannelTrigger(self) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
    ControlChannelTrigger = property(get_ControlChannelTrigger, None)
class IControlChannelTriggerFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('da4b7cf0-8d71-446f-88-c3-b9-51-84-a2-d6-cd')
    @winrt_commethod(6)
    def CreateControlChannelTrigger(self, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
    @winrt_commethod(7)
    def CreateControlChannelTriggerEx(self, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32, resourceRequestType: Windows.Networking.Sockets.ControlChannelTriggerResourceType) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
class IControlChannelTriggerResetEventDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6851038e-8ec4-42fe-9b-b2-21-e9-1b-7b-fc-b1')
    @winrt_commethod(6)
    def get_ResetReason(self) -> Windows.Networking.Sockets.ControlChannelTriggerResetReason: ...
    @winrt_commethod(7)
    def get_HardwareSlotReset(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SoftwareSlotReset(self) -> Boolean: ...
    ResetReason = property(get_ResetReason, None)
    HardwareSlotReset = property(get_HardwareSlotReset, None)
    SoftwareSlotReset = property(get_SoftwareSlotReset, None)
class IDatagramSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7fe25bbb-c3bc-4677-84-46-ca-28-a4-65-a3-af')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.DatagramSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.DatagramSocketInformation: ...
    @winrt_commethod(8)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(9)
    def ConnectAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ConnectWithEndpointPairAsync(self, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def BindServiceNameAsync(self, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def BindEndpointAsync(self, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def JoinMulticastGroup(self, host: Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(14)
    def GetOutputStreamAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IOutputStream]: ...
    @winrt_commethod(15)
    def GetOutputStreamWithEndpointPairAsync(self, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IOutputStream]: ...
    @winrt_commethod(16)
    def add_MessageReceived(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.DatagramSocket, Windows.Networking.Sockets.DatagramSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_MessageReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class IDatagramSocket2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d83ba354-9a9d-4185-a2-0a-14-24-c9-c2-a7-cd')
    @winrt_commethod(6)
    def BindServiceNameAndAdapterAsync(self, localServiceName: WinRT_String, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
class IDatagramSocket3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('37544f09-ab92-4306-9a-c1-0c-38-12-83-d9-c6')
    @winrt_commethod(6)
    def CancelIOAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def EnableTransferOwnership(self, taskId: Guid) -> Void: ...
    @winrt_commethod(8)
    def EnableTransferOwnershipWithConnectedStandbyAction(self, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_commethod(9)
    def TransferOwnership(self, socketId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TransferOwnershipWithContext(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_commethod(11)
    def TransferOwnershipWithContextAndKeepAliveTime(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: Windows.Foundation.TimeSpan) -> Void: ...
class IDatagramSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('52ac3f2e-349a-4135-bb-58-b7-9b-26-47-d3-90')
    @winrt_commethod(6)
    def get_QualityOfService(self) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_commethod(7)
    def put_QualityOfService(self, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_commethod(8)
    def get_OutboundUnicastHopLimit(self) -> Byte: ...
    @winrt_commethod(9)
    def put_OutboundUnicastHopLimit(self, value: Byte) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class IDatagramSocketControl2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('33ead5c2-979c-4415-82-a1-3c-fa-f6-46-c1-92')
    @winrt_commethod(6)
    def get_InboundBufferSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_InboundBufferSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_DontFragment(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_DontFragment(self, value: Boolean) -> Void: ...
    InboundBufferSizeInBytes = property(get_InboundBufferSizeInBytes, put_InboundBufferSizeInBytes)
    DontFragment = property(get_DontFragment, put_DontFragment)
class IDatagramSocketControl3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d4eb8256-1f6d-4598-9b-57-d4-2a-00-1d-f3-49')
    @winrt_commethod(6)
    def get_MulticastOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_MulticastOnly(self, value: Boolean) -> Void: ...
    MulticastOnly = property(get_MulticastOnly, put_MulticastOnly)
class IDatagramSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5f1a569a-55fb-48cd-97-06-7a-97-4f-7b-15-85')
    @winrt_commethod(6)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_LocalPort(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def get_RemotePort(self) -> WinRT_String: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
class IDatagramSocketMessageReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9e2ddca2-1712-4ce4-b1-79-8c-65-2c-6d-10-7e')
    @winrt_commethod(6)
    def get_RemoteAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_RemotePort(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def GetDataReader(self) -> Windows.Storage.Streams.DataReader: ...
    @winrt_commethod(10)
    def GetDataStream(self) -> Windows.Storage.Streams.IInputStream: ...
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
    LocalAddress = property(get_LocalAddress, None)
class IDatagramSocketStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e9c62aee-1494-4a21-bb-7e-85-89-fc-75-1d-9d')
    @winrt_commethod(6)
    def GetEndpointPairsAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    @winrt_commethod(7)
    def GetEndpointPairsWithSortOptionsAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
class IMessageWebSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('33727d08-34d5-4746-ad-7b-8d-de-5b-c2-ef-88')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.MessageWebSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.MessageWebSocketInformation: ...
    @winrt_commethod(8)
    def add_MessageReceived(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.MessageWebSocket, Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MessageReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
class IMessageWebSocket2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bed0cee7-f9c8-440a-9a-d5-73-72-81-d9-74-2e')
    @winrt_commethod(6)
    def add_ServerCustomValidationRequested(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.MessageWebSocket, Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServerCustomValidationRequested(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMessageWebSocket3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('59d9defb-71af-4349-84-87-91-1f-cf-68-15-97')
    @winrt_commethod(6)
    def SendNonfinalFrameAsync(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_commethod(7)
    def SendFinalFrameAsync(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
class IMessageWebSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8118388a-c629-4f0a-80-fb-81-fc-05-53-88-62')
    @winrt_commethod(6)
    def get_MaxMessageSize(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_MaxMessageSize(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_MessageType(self) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_commethod(9)
    def put_MessageType(self, value: Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    MaxMessageSize = property(get_MaxMessageSize, put_MaxMessageSize)
    MessageType = property(get_MessageType, put_MessageType)
class IMessageWebSocketControl2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e30fd791-080c-400a-a7-12-27-df-a9-e7-44-d8')
    @winrt_commethod(6)
    def get_DesiredUnsolicitedPongInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DesiredUnsolicitedPongInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_ActualUnsolicitedPongInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_ReceiveMode(self) -> Windows.Networking.Sockets.MessageWebSocketReceiveMode: ...
    @winrt_commethod(10)
    def put_ReceiveMode(self, value: Windows.Networking.Sockets.MessageWebSocketReceiveMode) -> Void: ...
    @winrt_commethod(11)
    def get_ClientCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(12)
    def put_ClientCertificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ReceiveMode = property(get_ReceiveMode, put_ReceiveMode)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class IMessageWebSocketMessageReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('478c22ac-4c4b-42ed-9e-d7-1e-f9-f9-4f-a3-d5')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_commethod(7)
    def GetDataReader(self) -> Windows.Storage.Streams.DataReader: ...
    @winrt_commethod(8)
    def GetDataStream(self) -> Windows.Storage.Streams.IInputStream: ...
    MessageType = property(get_MessageType, None)
class IMessageWebSocketMessageReceivedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('89ce06fd-dd6f-4a07-87-f9-f9-eb-4d-89-d8-3d')
    @winrt_commethod(6)
    def get_IsMessageComplete(self) -> Boolean: ...
    IsMessageComplete = property(get_IsMessageComplete, None)
class IServerMessageWebSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e3ac9240-813b-5efd-7e-11-ae-23-05-fc-77-f1')
    @winrt_commethod(6)
    def add_MessageReceived(self, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerMessageWebSocket, Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MessageReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Control(self) -> Windows.Networking.Sockets.ServerMessageWebSocketControl: ...
    @winrt_commethod(9)
    def get_Information(self) -> Windows.Networking.Sockets.ServerMessageWebSocketInformation: ...
    @winrt_commethod(10)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(11)
    def add_Closed(self, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerMessageWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def CloseWithStatus(self, code: UInt16, reason: WinRT_String) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class IServerMessageWebSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('69c2f051-1c1f-587a-45-19-21-81-61-01-92-b7')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_commethod(7)
    def put_MessageType(self, value: Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    MessageType = property(get_MessageType, put_MessageType)
class IServerMessageWebSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fc32b45f-4448-5505-6c-c9-09-af-a8-91-5f-5d')
    @winrt_commethod(6)
    def get_BandwidthStatistics(self) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(7)
    def get_Protocol(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
class IServerStreamWebSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2ced5bbf-74f6-55e4-79-df-91-32-68-0d-fe-e8')
    @winrt_commethod(6)
    def get_Information(self) -> Windows.Networking.Sockets.ServerStreamWebSocketInformation: ...
    @winrt_commethod(7)
    def get_InputStream(self) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(8)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(9)
    def add_Closed(self, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerStreamWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def CloseWithStatus(self, code: UInt16, reason: WinRT_String) -> Void: ...
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class IServerStreamWebSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fc32b45f-4448-5505-6c-c9-09-ab-a8-91-5f-5d')
    @winrt_commethod(6)
    def get_BandwidthStatistics(self) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(7)
    def get_Protocol(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
class ISocketActivityContext(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('43b04d64-4c85-4396-a6-37-1d-97-3f-6e-bd-49')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, None)
class ISocketActivityContextFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b99fc3c3-088c-4388-83-ae-25-25-13-8e-04-9a')
    @winrt_commethod(6)
    def Create(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Networking.Sockets.SocketActivityContext: ...
class ISocketActivityInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8d8a42e4-a87e-4b74-99-68-18-5b-25-11-de-fe')
    @winrt_commethod(6)
    def get_TaskId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SocketKind(self) -> Windows.Networking.Sockets.SocketActivityKind: ...
    @winrt_commethod(9)
    def get_Context(self) -> Windows.Networking.Sockets.SocketActivityContext: ...
    @winrt_commethod(10)
    def get_DatagramSocket(self) -> Windows.Networking.Sockets.DatagramSocket: ...
    @winrt_commethod(11)
    def get_StreamSocket(self) -> Windows.Networking.Sockets.StreamSocket: ...
    @winrt_commethod(12)
    def get_StreamSocketListener(self) -> Windows.Networking.Sockets.StreamSocketListener: ...
    TaskId = property(get_TaskId, None)
    Id = property(get_Id, None)
    SocketKind = property(get_SocketKind, None)
    Context = property(get_Context, None)
    DatagramSocket = property(get_DatagramSocket, None)
    StreamSocket = property(get_StreamSocket, None)
    StreamSocketListener = property(get_StreamSocketListener, None)
class ISocketActivityInformationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8570b47a-7e7d-4736-80-41-13-27-a6-54-3c-56')
    @winrt_commethod(6)
    def get_AllSockets(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Networking.Sockets.SocketActivityInformation]: ...
    AllSockets = property(get_AllSockets, None)
class ISocketActivityTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('45f406a7-fc9f-4f81-ac-ad-35-5f-ef-51-e6-7b')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.Networking.Sockets.SocketActivityTriggerReason: ...
    @winrt_commethod(7)
    def get_SocketInformation(self) -> Windows.Networking.Sockets.SocketActivityInformation: ...
    Reason = property(get_Reason, None)
    SocketInformation = property(get_SocketInformation, None)
class ISocketErrorStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('828337f4-7d56-4d8e-b7-b4-a0-7d-d7-c1-bc-a9')
    @winrt_commethod(6)
    def GetStatus(self, hresult: Int32) -> Windows.Networking.Sockets.SocketErrorStatus: ...
class IStreamSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('69a22cf3-fc7b-4857-af-38-f6-e7-de-6a-5b-49')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.StreamSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.StreamSocketInformation: ...
    @winrt_commethod(8)
    def get_InputStream(self) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(9)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(10)
    def ConnectWithEndpointPairAsync(self, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ConnectAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ConnectWithEndpointPairAndProtectionLevelAsync(self, endpointPair: Windows.Networking.EndpointPair, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ConnectWithProtectionLevelAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def UpgradeToSslAsync(self, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, validationHostName: Windows.Networking.HostName) -> Windows.Foundation.IAsyncAction: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class IStreamSocket2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('29d0e575-f314-4d09-ad-f0-0f-bd-96-7f-bd-9f')
    @winrt_commethod(6)
    def ConnectWithProtectionLevelAndAdapterAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
class IStreamSocket3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3f430b00-9d28-4854-ba-c3-23-01-94-1e-c2-23')
    @winrt_commethod(6)
    def CancelIOAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def EnableTransferOwnership(self, taskId: Guid) -> Void: ...
    @winrt_commethod(8)
    def EnableTransferOwnershipWithConnectedStandbyAction(self, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_commethod(9)
    def TransferOwnership(self, socketId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TransferOwnershipWithContext(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_commethod(11)
    def TransferOwnershipWithContextAndKeepAliveTime(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: Windows.Foundation.TimeSpan) -> Void: ...
class IStreamSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fe25adf1-92ab-4af3-99-92-0f-4c-85-e3-6c-c4')
    @winrt_commethod(6)
    def get_NoDelay(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_NoDelay(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_KeepAlive(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_KeepAlive(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_OutboundBufferSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_OutboundBufferSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_QualityOfService(self) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_commethod(13)
    def put_QualityOfService(self, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_commethod(14)
    def get_OutboundUnicastHopLimit(self) -> Byte: ...
    @winrt_commethod(15)
    def put_OutboundUnicastHopLimit(self, value: Byte) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
    KeepAlive = property(get_KeepAlive, put_KeepAlive)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class IStreamSocketControl2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c2d09a56-060f-44c1-b8-e2-1f-bf-60-bd-62-c5')
    @winrt_commethod(6)
    def get_IgnorableServerCertificateErrors(self) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
class IStreamSocketControl3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c56a444c-4e74-403e-89-4c-b3-1c-ae-5c-73-42')
    @winrt_commethod(6)
    def get_SerializeConnectionAttempts(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SerializeConnectionAttempts(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ClientCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def put_ClientCertificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    SerializeConnectionAttempts = property(get_SerializeConnectionAttempts, put_SerializeConnectionAttempts)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class IStreamSocketControl4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('964e2b3d-ec27-4888-b3-ce-c7-4b-41-84-23-ad')
    @winrt_commethod(6)
    def get_MinProtectionLevel(self) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(7)
    def put_MinProtectionLevel(self, value: Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
    MinProtectionLevel = property(get_MinProtectionLevel, put_MinProtectionLevel)
class IStreamSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3b80ae30-5e68-4205-88-f0-dc-85-d2-e2-5d-ed')
    @winrt_commethod(6)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_LocalPort(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteHostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def get_RemoteAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(10)
    def get_RemoteServiceName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_RemotePort(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_RoundTripTimeStatistics(self) -> Windows.Networking.Sockets.RoundTripTimeStatistics: ...
    @winrt_commethod(13)
    def get_BandwidthStatistics(self) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(14)
    def get_ProtectionLevel(self) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(15)
    def get_SessionKey(self) -> Windows.Storage.Streams.IBuffer: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteHostName = property(get_RemoteHostName, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemoteServiceName = property(get_RemoteServiceName, None)
    RemotePort = property(get_RemotePort, None)
    RoundTripTimeStatistics = property(get_RoundTripTimeStatistics, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    SessionKey = property(get_SessionKey, None)
class IStreamSocketInformation2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('12c28452-4bdc-4ee4-97-6a-cf-13-0e-9d-92-e3')
    @winrt_commethod(6)
    def get_ServerCertificateErrorSeverity(self) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(8)
    def get_ServerCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class IStreamSocketListener(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ff513437-df9f-4df0-bf-82-0e-c5-d7-b3-5a-ae')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.StreamSocketListenerControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.StreamSocketListenerInformation: ...
    @winrt_commethod(8)
    def BindServiceNameAsync(self, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def BindEndpointAsync(self, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def add_ConnectionReceived(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.StreamSocketListener, Windows.Networking.Sockets.StreamSocketListenerConnectionReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ConnectionReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
class IStreamSocketListener2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('658dc13e-bb3e-4458-b2-32-ed-10-88-69-4b-98')
    @winrt_commethod(6)
    def BindServiceNameWithProtectionLevelAsync(self, localServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def BindServiceNameWithProtectionLevelAndAdapterAsync(self, localServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
class IStreamSocketListener3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4798201c-bdf8-4919-85-42-28-d4-50-e7-45-07')
    @winrt_commethod(6)
    def CancelIOAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def EnableTransferOwnership(self, taskId: Guid) -> Void: ...
    @winrt_commethod(8)
    def EnableTransferOwnershipWithConnectedStandbyAction(self, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_commethod(9)
    def TransferOwnership(self, socketId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TransferOwnershipWithContext(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
class IStreamSocketListenerConnectionReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0c472ea9-373f-447b-85-b1-dd-d4-54-88-03-ba')
    @winrt_commethod(6)
    def get_Socket(self) -> Windows.Networking.Sockets.StreamSocket: ...
    Socket = property(get_Socket, None)
class IStreamSocketListenerControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('20d8c576-8d8a-4dba-97-22-a1-6c-4d-98-49-80')
    @winrt_commethod(6)
    def get_QualityOfService(self) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_commethod(7)
    def put_QualityOfService(self, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
class IStreamSocketListenerControl2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('948bb665-2c3e-404b-b8-b0-8e-b2-49-a2-b0-a1')
    @winrt_commethod(6)
    def get_NoDelay(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_NoDelay(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_KeepAlive(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_KeepAlive(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_OutboundBufferSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_OutboundBufferSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_OutboundUnicastHopLimit(self) -> Byte: ...
    @winrt_commethod(13)
    def put_OutboundUnicastHopLimit(self, value: Byte) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
    KeepAlive = property(get_KeepAlive, put_KeepAlive)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class IStreamSocketListenerInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e62ba82f-a63a-430b-bf-62-29-e9-3e-56-33-b4')
    @winrt_commethod(6)
    def get_LocalPort(self) -> WinRT_String: ...
    LocalPort = property(get_LocalPort, None)
class IStreamSocketStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a420bc4a-6e2e-4af5-b5-56-35-5a-e0-cd-4f-29')
    @winrt_commethod(6)
    def GetEndpointPairsAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    @winrt_commethod(7)
    def GetEndpointPairsWithSortOptionsAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
class IStreamWebSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bd4a49d8-b289-45bb-97-eb-c7-52-52-05-a8-43')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.StreamWebSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.StreamWebSocketInformation: ...
    @winrt_commethod(8)
    def get_InputStream(self) -> Windows.Storage.Streams.IInputStream: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
class IStreamWebSocket2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aa4d08cb-93f5-4678-82-36-57-cc-e5-41-7e-d5')
    @winrt_commethod(6)
    def add_ServerCustomValidationRequested(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.StreamWebSocket, Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServerCustomValidationRequested(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IStreamWebSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b4f478b1-a45a-48db-95-3a-64-5b-7d-96-4c-07')
    @winrt_commethod(6)
    def get_NoDelay(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_NoDelay(self, value: Boolean) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
class IStreamWebSocketControl2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('215d9f7e-fa58-40da-9f-11-a4-8d-af-e9-50-37')
    @winrt_commethod(6)
    def get_DesiredUnsolicitedPongInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DesiredUnsolicitedPongInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_ActualUnsolicitedPongInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_ClientCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(10)
    def put_ClientCertificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class IWebSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f877396f-99b1-4e18-bc-08-85-0c-9a-df-15-6e')
    @winrt_commethod(6)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(7)
    def ConnectAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def SetRequestHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def add_Closed(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.IWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Closed(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def CloseWithStatus(self, code: UInt16, reason: WinRT_String) -> Void: ...
    OutputStream = property(get_OutputStream, None)
class IWebSocketClosedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ceb78d07-d0a8-4703-a0-91-c8-c2-c0-91-5b-c3')
    @winrt_commethod(6)
    def get_Code(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Reason(self) -> WinRT_String: ...
    Code = property(get_Code, None)
    Reason = property(get_Reason, None)
class IWebSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2ec4bdc3-d9a5-455a-98-11-de-24-d4-53-37-e9')
    @winrt_commethod(6)
    def get_OutboundBufferSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_OutboundBufferSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_ServerCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(9)
    def put_ServerCredential(self, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(10)
    def get_ProxyCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(11)
    def put_ProxyCredential(self, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedProtocols(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    SupportedProtocols = property(get_SupportedProtocols, None)
class IWebSocketControl2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('79c3be03-f2ca-461e-af-4e-96-65-bc-2d-06-20')
    @winrt_commethod(6)
    def get_IgnorableServerCertificateErrors(self) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
class IWebSocketErrorStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('27cdf35b-1f61-4709-8e-02-61-28-3a-da-4e-9d')
    @winrt_commethod(6)
    def GetStatus(self, hresult: Int32) -> Windows.Web.WebErrorStatus: ...
class IWebSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5e01e316-c92a-47a5-b2-5f-07-84-76-39-d1-81')
    @winrt_commethod(6)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_BandwidthStatistics(self) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(8)
    def get_Protocol(self) -> WinRT_String: ...
    LocalAddress = property(get_LocalAddress, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
class IWebSocketInformation2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ce1d39ce-a1b7-4d43-82-69-8d-5b-98-1b-d4-7a')
    @winrt_commethod(6)
    def get_ServerCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrorSeverity(self) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class IWebSocketServerCustomValidationRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ffeffe48-022a-4ab7-8b-36-e1-0a-f4-64-0e-6b')
    @winrt_commethod(6)
    def get_ServerCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrorSeverity(self) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(10)
    def Reject(self) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class MessageWebSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.MessageWebSocket'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Sockets.MessageWebSocket: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IMessageWebSocket) -> Windows.Networking.Sockets.MessageWebSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IMessageWebSocket) -> Windows.Networking.Sockets.MessageWebSocketInformation: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: Windows.Networking.Sockets.IMessageWebSocket, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.MessageWebSocket, Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: Windows.Networking.Sockets.IMessageWebSocket, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IWebSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Networking.Sockets.IWebSocket, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: Windows.Networking.Sockets.IWebSocket, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Networking.Sockets.IWebSocket, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.IWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Networking.Sockets.IWebSocket, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: Windows.Networking.Sockets.IWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def add_ServerCustomValidationRequested(self: Windows.Networking.Sockets.IMessageWebSocket2, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.MessageWebSocket, Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerCustomValidationRequested(self: Windows.Networking.Sockets.IMessageWebSocket2, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SendNonfinalFrameAsync(self: Windows.Networking.Sockets.IMessageWebSocket3, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def SendFinalFrameAsync(self: Windows.Networking.Sockets.IMessageWebSocket3, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class MessageWebSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.MessageWebSocketControl'
    @winrt_mixinmethod
    def get_MaxMessageSize(self: Windows.Networking.Sockets.IMessageWebSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxMessageSize(self: Windows.Networking.Sockets.IMessageWebSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Networking.Sockets.IMessageWebSocketControl) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_mixinmethod
    def put_MessageType(self: Windows.Networking.Sockets.IMessageWebSocketControl, value: Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IWebSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IWebSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: Windows.Networking.Sockets.IWebSocketControl, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: Windows.Networking.Sockets.IWebSocketControl, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedProtocols(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketControl2) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_DesiredUnsolicitedPongInterval(self: Windows.Networking.Sockets.IMessageWebSocketControl2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DesiredUnsolicitedPongInterval(self: Windows.Networking.Sockets.IMessageWebSocketControl2, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ActualUnsolicitedPongInterval(self: Windows.Networking.Sockets.IMessageWebSocketControl2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ReceiveMode(self: Windows.Networking.Sockets.IMessageWebSocketControl2) -> Windows.Networking.Sockets.MessageWebSocketReceiveMode: ...
    @winrt_mixinmethod
    def put_ReceiveMode(self: Windows.Networking.Sockets.IMessageWebSocketControl2, value: Windows.Networking.Sockets.MessageWebSocketReceiveMode) -> Void: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: Windows.Networking.Sockets.IMessageWebSocketControl2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: Windows.Networking.Sockets.IMessageWebSocketControl2, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    MaxMessageSize = property(get_MaxMessageSize, put_MaxMessageSize)
    MessageType = property(get_MessageType, put_MessageType)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    SupportedProtocols = property(get_SupportedProtocols, None)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ReceiveMode = property(get_ReceiveMode, put_ReceiveMode)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class MessageWebSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.MessageWebSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IWebSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IWebSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Networking.Sockets.IWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    LocalAddress = property(get_LocalAddress, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class MessageWebSocketMessageReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_mixinmethod
    def GetDataReader(self: Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs) -> Windows.Storage.Streams.DataReader: ...
    @winrt_mixinmethod
    def GetDataStream(self: Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_IsMessageComplete(self: Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs2) -> Boolean: ...
    MessageType = property(get_MessageType, None)
    IsMessageComplete = property(get_IsMessageComplete, None)
MessageWebSocketReceiveMode = Int32
MessageWebSocketReceiveMode_FullMessage: MessageWebSocketReceiveMode = 0
MessageWebSocketReceiveMode_PartialMessage: MessageWebSocketReceiveMode = 1
class RoundTripTimeStatistics(EasyCastStructure):
    Variance: UInt32
    Max: UInt32
    Min: UInt32
    Sum: UInt32
class ServerMessageWebSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.ServerMessageWebSocket'
    @winrt_mixinmethod
    def add_MessageReceived(self: Windows.Networking.Sockets.IServerMessageWebSocket, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerMessageWebSocket, Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: Windows.Networking.Sockets.IServerMessageWebSocket, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IServerMessageWebSocket) -> Windows.Networking.Sockets.ServerMessageWebSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IServerMessageWebSocket) -> Windows.Networking.Sockets.ServerMessageWebSocketInformation: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IServerMessageWebSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Networking.Sockets.IServerMessageWebSocket, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerMessageWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Networking.Sockets.IServerMessageWebSocket, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: Windows.Networking.Sockets.IServerMessageWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class ServerMessageWebSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.ServerMessageWebSocketControl'
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Networking.Sockets.IServerMessageWebSocketControl) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_mixinmethod
    def put_MessageType(self: Windows.Networking.Sockets.IServerMessageWebSocketControl, value: Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    MessageType = property(get_MessageType, put_MessageType)
class ServerMessageWebSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.ServerMessageWebSocketInformation'
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IServerMessageWebSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Networking.Sockets.IServerMessageWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IServerMessageWebSocketInformation) -> Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
class ServerStreamWebSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.ServerStreamWebSocket'
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IServerStreamWebSocket) -> Windows.Networking.Sockets.ServerStreamWebSocketInformation: ...
    @winrt_mixinmethod
    def get_InputStream(self: Windows.Networking.Sockets.IServerStreamWebSocket) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IServerStreamWebSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Networking.Sockets.IServerStreamWebSocket, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerStreamWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Networking.Sockets.IServerStreamWebSocket, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: Windows.Networking.Sockets.IServerStreamWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class ServerStreamWebSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.ServerStreamWebSocketInformation'
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IServerStreamWebSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Networking.Sockets.IServerStreamWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IServerStreamWebSocketInformation) -> Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
SocketActivityConnectedStandbyAction = Int32
SocketActivityConnectedStandbyAction_DoNotWake: SocketActivityConnectedStandbyAction = 0
SocketActivityConnectedStandbyAction_Wake: SocketActivityConnectedStandbyAction = 1
class SocketActivityContext(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.SocketActivityContext'
    @winrt_factorymethod
    def Create(cls: Windows.Networking.Sockets.ISocketActivityContextFactory, data: Windows.Storage.Streams.IBuffer) -> Windows.Networking.Sockets.SocketActivityContext: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Networking.Sockets.ISocketActivityContext) -> Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, None)
class SocketActivityInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.SocketActivityInformation'
    @winrt_mixinmethod
    def get_TaskId(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Guid: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Networking.Sockets.ISocketActivityInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SocketKind(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.SocketActivityKind: ...
    @winrt_mixinmethod
    def get_Context(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.SocketActivityContext: ...
    @winrt_mixinmethod
    def get_DatagramSocket(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.DatagramSocket: ...
    @winrt_mixinmethod
    def get_StreamSocket(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.StreamSocket: ...
    @winrt_mixinmethod
    def get_StreamSocketListener(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.StreamSocketListener: ...
    @winrt_classmethod
    def get_AllSockets(cls: Windows.Networking.Sockets.ISocketActivityInformationStatics) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Networking.Sockets.SocketActivityInformation]: ...
    TaskId = property(get_TaskId, None)
    Id = property(get_Id, None)
    SocketKind = property(get_SocketKind, None)
    Context = property(get_Context, None)
    DatagramSocket = property(get_DatagramSocket, None)
    StreamSocket = property(get_StreamSocket, None)
    StreamSocketListener = property(get_StreamSocketListener, None)
    AllSockets = property(get_AllSockets, None)
SocketActivityKind = Int32
SocketActivityKind_None: SocketActivityKind = 0
SocketActivityKind_StreamSocketListener: SocketActivityKind = 1
SocketActivityKind_DatagramSocket: SocketActivityKind = 2
SocketActivityKind_StreamSocket: SocketActivityKind = 3
class SocketActivityTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.SocketActivityTriggerDetails'
    @winrt_mixinmethod
    def get_Reason(self: Windows.Networking.Sockets.ISocketActivityTriggerDetails) -> Windows.Networking.Sockets.SocketActivityTriggerReason: ...
    @winrt_mixinmethod
    def get_SocketInformation(self: Windows.Networking.Sockets.ISocketActivityTriggerDetails) -> Windows.Networking.Sockets.SocketActivityInformation: ...
    Reason = property(get_Reason, None)
    SocketInformation = property(get_SocketInformation, None)
SocketActivityTriggerReason = Int32
SocketActivityTriggerReason_None: SocketActivityTriggerReason = 0
SocketActivityTriggerReason_SocketActivity: SocketActivityTriggerReason = 1
SocketActivityTriggerReason_ConnectionAccepted: SocketActivityTriggerReason = 2
SocketActivityTriggerReason_KeepAliveTimerExpired: SocketActivityTriggerReason = 3
SocketActivityTriggerReason_SocketClosed: SocketActivityTriggerReason = 4
class SocketError(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.SocketError'
    @winrt_classmethod
    def GetStatus(cls: Windows.Networking.Sockets.ISocketErrorStatics, hresult: Int32) -> Windows.Networking.Sockets.SocketErrorStatus: ...
SocketErrorStatus = Int32
SocketErrorStatus_Unknown: SocketErrorStatus = 0
SocketErrorStatus_OperationAborted: SocketErrorStatus = 1
SocketErrorStatus_HttpInvalidServerResponse: SocketErrorStatus = 2
SocketErrorStatus_ConnectionTimedOut: SocketErrorStatus = 3
SocketErrorStatus_AddressFamilyNotSupported: SocketErrorStatus = 4
SocketErrorStatus_SocketTypeNotSupported: SocketErrorStatus = 5
SocketErrorStatus_HostNotFound: SocketErrorStatus = 6
SocketErrorStatus_NoDataRecordOfRequestedType: SocketErrorStatus = 7
SocketErrorStatus_NonAuthoritativeHostNotFound: SocketErrorStatus = 8
SocketErrorStatus_ClassTypeNotFound: SocketErrorStatus = 9
SocketErrorStatus_AddressAlreadyInUse: SocketErrorStatus = 10
SocketErrorStatus_CannotAssignRequestedAddress: SocketErrorStatus = 11
SocketErrorStatus_ConnectionRefused: SocketErrorStatus = 12
SocketErrorStatus_NetworkIsUnreachable: SocketErrorStatus = 13
SocketErrorStatus_UnreachableHost: SocketErrorStatus = 14
SocketErrorStatus_NetworkIsDown: SocketErrorStatus = 15
SocketErrorStatus_NetworkDroppedConnectionOnReset: SocketErrorStatus = 16
SocketErrorStatus_SoftwareCausedConnectionAbort: SocketErrorStatus = 17
SocketErrorStatus_ConnectionResetByPeer: SocketErrorStatus = 18
SocketErrorStatus_HostIsDown: SocketErrorStatus = 19
SocketErrorStatus_NoAddressesFound: SocketErrorStatus = 20
SocketErrorStatus_TooManyOpenFiles: SocketErrorStatus = 21
SocketErrorStatus_MessageTooLong: SocketErrorStatus = 22
SocketErrorStatus_CertificateExpired: SocketErrorStatus = 23
SocketErrorStatus_CertificateUntrustedRoot: SocketErrorStatus = 24
SocketErrorStatus_CertificateCommonNameIsIncorrect: SocketErrorStatus = 25
SocketErrorStatus_CertificateWrongUsage: SocketErrorStatus = 26
SocketErrorStatus_CertificateRevoked: SocketErrorStatus = 27
SocketErrorStatus_CertificateNoRevocationCheck: SocketErrorStatus = 28
SocketErrorStatus_CertificateRevocationServerOffline: SocketErrorStatus = 29
SocketErrorStatus_CertificateIsInvalid: SocketErrorStatus = 30
SocketMessageType = Int32
SocketMessageType_Binary: SocketMessageType = 0
SocketMessageType_Utf8: SocketMessageType = 1
SocketProtectionLevel = Int32
SocketProtectionLevel_PlainSocket: SocketProtectionLevel = 0
SocketProtectionLevel_Ssl: SocketProtectionLevel = 1
SocketProtectionLevel_SslAllowNullEncryption: SocketProtectionLevel = 2
SocketProtectionLevel_BluetoothEncryptionAllowNullAuthentication: SocketProtectionLevel = 3
SocketProtectionLevel_BluetoothEncryptionWithAuthentication: SocketProtectionLevel = 4
SocketProtectionLevel_Ssl3AllowWeakEncryption: SocketProtectionLevel = 5
SocketProtectionLevel_Tls10: SocketProtectionLevel = 6
SocketProtectionLevel_Tls11: SocketProtectionLevel = 7
SocketProtectionLevel_Tls12: SocketProtectionLevel = 8
SocketProtectionLevel_Unspecified: SocketProtectionLevel = 9
SocketQualityOfService = Int32
SocketQualityOfService_Normal: SocketQualityOfService = 0
SocketQualityOfService_LowLatency: SocketQualityOfService = 1
SocketSslErrorSeverity = Int32
SocketSslErrorSeverity_None: SocketSslErrorSeverity = 0
SocketSslErrorSeverity_Ignorable: SocketSslErrorSeverity = 1
SocketSslErrorSeverity_Fatal: SocketSslErrorSeverity = 2
class StreamSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamSocket'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Sockets.StreamSocket: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IStreamSocket) -> Windows.Networking.Sockets.StreamSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IStreamSocket) -> Windows.Networking.Sockets.StreamSocketInformation: ...
    @winrt_mixinmethod
    def get_InputStream(self: Windows.Networking.Sockets.IStreamSocket) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IStreamSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectWithEndpointPairAsync(self: Windows.Networking.Sockets.IStreamSocket, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Networking.Sockets.IStreamSocket, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectWithEndpointPairAndProtectionLevelAsync(self: Windows.Networking.Sockets.IStreamSocket, endpointPair: Windows.Networking.EndpointPair, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectWithProtectionLevelAsync(self: Windows.Networking.Sockets.IStreamSocket, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UpgradeToSslAsync(self: Windows.Networking.Sockets.IStreamSocket, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, validationHostName: Windows.Networking.HostName) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ConnectWithProtectionLevelAndAdapterAsync(self: Windows.Networking.Sockets.IStreamSocket2, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelIOAsync(self: Windows.Networking.Sockets.IStreamSocket3) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableTransferOwnership(self: Windows.Networking.Sockets.IStreamSocket3, taskId: Guid) -> Void: ...
    @winrt_mixinmethod
    def EnableTransferOwnershipWithConnectedStandbyAction(self: Windows.Networking.Sockets.IStreamSocket3, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnership(self: Windows.Networking.Sockets.IStreamSocket3, socketId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContext(self: Windows.Networking.Sockets.IStreamSocket3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContextAndKeepAliveTime(self: Windows.Networking.Sockets.IStreamSocket3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def GetEndpointPairsAsync(cls: Windows.Networking.Sockets.IStreamSocketStatics, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    @winrt_classmethod
    def GetEndpointPairsWithSortOptionsAsync(cls: Windows.Networking.Sockets.IStreamSocketStatics, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class StreamSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamSocketControl'
    @winrt_mixinmethod
    def get_NoDelay(self: Windows.Networking.Sockets.IStreamSocketControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_NoDelay(self: Windows.Networking.Sockets.IStreamSocketControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeepAlive(self: Windows.Networking.Sockets.IStreamSocketControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeepAlive(self: Windows.Networking.Sockets.IStreamSocketControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IStreamSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IStreamSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_QualityOfService(self: Windows.Networking.Sockets.IStreamSocketControl) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_mixinmethod
    def put_QualityOfService(self: Windows.Networking.Sockets.IStreamSocketControl, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IStreamSocketControl) -> Byte: ...
    @winrt_mixinmethod
    def put_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IStreamSocketControl, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: Windows.Networking.Sockets.IStreamSocketControl2) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_SerializeConnectionAttempts(self: Windows.Networking.Sockets.IStreamSocketControl3) -> Boolean: ...
    @winrt_mixinmethod
    def put_SerializeConnectionAttempts(self: Windows.Networking.Sockets.IStreamSocketControl3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: Windows.Networking.Sockets.IStreamSocketControl3) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: Windows.Networking.Sockets.IStreamSocketControl3, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_MinProtectionLevel(self: Windows.Networking.Sockets.IStreamSocketControl4) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def put_MinProtectionLevel(self: Windows.Networking.Sockets.IStreamSocketControl4, value: Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
    KeepAlive = property(get_KeepAlive, put_KeepAlive)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    SerializeConnectionAttempts = property(get_SerializeConnectionAttempts, put_SerializeConnectionAttempts)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
    MinProtectionLevel = property(get_MinProtectionLevel, put_MinProtectionLevel)
class StreamSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_LocalPort(self: Windows.Networking.Sockets.IStreamSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteHostName(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemoteAddress(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemoteServiceName(self: Windows.Networking.Sockets.IStreamSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemotePort(self: Windows.Networking.Sockets.IStreamSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoundTripTimeStatistics(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.Sockets.RoundTripTimeStatistics: ...
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def get_SessionKey(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Networking.Sockets.IStreamSocketInformation2) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Networking.Sockets.IStreamSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Networking.Sockets.IStreamSocketInformation2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Networking.Sockets.IStreamSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteHostName = property(get_RemoteHostName, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemoteServiceName = property(get_RemoteServiceName, None)
    RemotePort = property(get_RemotePort, None)
    RoundTripTimeStatistics = property(get_RoundTripTimeStatistics, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    SessionKey = property(get_SessionKey, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class StreamSocketListener(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamSocketListener'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Sockets.StreamSocketListener: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IStreamSocketListener) -> Windows.Networking.Sockets.StreamSocketListenerControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IStreamSocketListener) -> Windows.Networking.Sockets.StreamSocketListenerInformation: ...
    @winrt_mixinmethod
    def BindServiceNameAsync(self: Windows.Networking.Sockets.IStreamSocketListener, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindEndpointAsync(self: Windows.Networking.Sockets.IStreamSocketListener, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_ConnectionReceived(self: Windows.Networking.Sockets.IStreamSocketListener, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.StreamSocketListener, Windows.Networking.Sockets.StreamSocketListenerConnectionReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionReceived(self: Windows.Networking.Sockets.IStreamSocketListener, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def BindServiceNameWithProtectionLevelAsync(self: Windows.Networking.Sockets.IStreamSocketListener2, localServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindServiceNameWithProtectionLevelAndAdapterAsync(self: Windows.Networking.Sockets.IStreamSocketListener2, localServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelIOAsync(self: Windows.Networking.Sockets.IStreamSocketListener3) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableTransferOwnership(self: Windows.Networking.Sockets.IStreamSocketListener3, taskId: Guid) -> Void: ...
    @winrt_mixinmethod
    def EnableTransferOwnershipWithConnectedStandbyAction(self: Windows.Networking.Sockets.IStreamSocketListener3, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnership(self: Windows.Networking.Sockets.IStreamSocketListener3, socketId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContext(self: Windows.Networking.Sockets.IStreamSocketListener3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
class StreamSocketListenerConnectionReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamSocketListenerConnectionReceivedEventArgs'
    @winrt_mixinmethod
    def get_Socket(self: Windows.Networking.Sockets.IStreamSocketListenerConnectionReceivedEventArgs) -> Windows.Networking.Sockets.StreamSocket: ...
    Socket = property(get_Socket, None)
class StreamSocketListenerControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamSocketListenerControl'
    @winrt_mixinmethod
    def get_QualityOfService(self: Windows.Networking.Sockets.IStreamSocketListenerControl) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_mixinmethod
    def put_QualityOfService(self: Windows.Networking.Sockets.IStreamSocketListenerControl, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_mixinmethod
    def get_NoDelay(self: Windows.Networking.Sockets.IStreamSocketListenerControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_NoDelay(self: Windows.Networking.Sockets.IStreamSocketListenerControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeepAlive(self: Windows.Networking.Sockets.IStreamSocketListenerControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeepAlive(self: Windows.Networking.Sockets.IStreamSocketListenerControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IStreamSocketListenerControl2) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IStreamSocketListenerControl2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IStreamSocketListenerControl2) -> Byte: ...
    @winrt_mixinmethod
    def put_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IStreamSocketListenerControl2, value: Byte) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    NoDelay = property(get_NoDelay, put_NoDelay)
    KeepAlive = property(get_KeepAlive, put_KeepAlive)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class StreamSocketListenerInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamSocketListenerInformation'
    @winrt_mixinmethod
    def get_LocalPort(self: Windows.Networking.Sockets.IStreamSocketListenerInformation) -> WinRT_String: ...
    LocalPort = property(get_LocalPort, None)
class StreamWebSocket(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamWebSocket'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Sockets.StreamWebSocket: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IStreamWebSocket) -> Windows.Networking.Sockets.StreamWebSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IStreamWebSocket) -> Windows.Networking.Sockets.StreamWebSocketInformation: ...
    @winrt_mixinmethod
    def get_InputStream(self: Windows.Networking.Sockets.IStreamWebSocket) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IWebSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Networking.Sockets.IWebSocket, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: Windows.Networking.Sockets.IWebSocket, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Networking.Sockets.IWebSocket, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.IWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Networking.Sockets.IWebSocket, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: Windows.Networking.Sockets.IWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def add_ServerCustomValidationRequested(self: Windows.Networking.Sockets.IStreamWebSocket2, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.StreamWebSocket, Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerCustomValidationRequested(self: Windows.Networking.Sockets.IStreamWebSocket2, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class StreamWebSocketControl(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamWebSocketControl'
    @winrt_mixinmethod
    def get_NoDelay(self: Windows.Networking.Sockets.IStreamWebSocketControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_NoDelay(self: Windows.Networking.Sockets.IStreamWebSocketControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IWebSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IWebSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: Windows.Networking.Sockets.IWebSocketControl, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: Windows.Networking.Sockets.IWebSocketControl, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedProtocols(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketControl2) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_DesiredUnsolicitedPongInterval(self: Windows.Networking.Sockets.IStreamWebSocketControl2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DesiredUnsolicitedPongInterval(self: Windows.Networking.Sockets.IStreamWebSocketControl2, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ActualUnsolicitedPongInterval(self: Windows.Networking.Sockets.IStreamWebSocketControl2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: Windows.Networking.Sockets.IStreamWebSocketControl2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: Windows.Networking.Sockets.IStreamWebSocketControl2, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    SupportedProtocols = property(get_SupportedProtocols, None)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class StreamWebSocketInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.StreamWebSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IWebSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IWebSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Networking.Sockets.IWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    LocalAddress = property(get_LocalAddress, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class WebSocketClosedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.WebSocketClosedEventArgs'
    @winrt_mixinmethod
    def get_Code(self: Windows.Networking.Sockets.IWebSocketClosedEventArgs) -> UInt16: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.Networking.Sockets.IWebSocketClosedEventArgs) -> WinRT_String: ...
    Code = property(get_Code, None)
    Reason = property(get_Reason, None)
class WebSocketError(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.WebSocketError'
    @winrt_classmethod
    def GetStatus(cls: Windows.Networking.Sockets.IWebSocketErrorStatics, hresult: Int32) -> Windows.Web.WebErrorStatus: ...
class WebSocketKeepAlive(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.WebSocketKeepAlive'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Sockets.WebSocketKeepAlive: ...
    @winrt_mixinmethod
    def Run(self: Windows.ApplicationModel.Background.IBackgroundTask, taskInstance: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
class WebSocketServerCustomValidationRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs'
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def Reject(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
make_head(_module, 'BandwidthStatistics')
make_head(_module, 'ControlChannelTrigger')
make_head(_module, 'DatagramSocket')
make_head(_module, 'DatagramSocketControl')
make_head(_module, 'DatagramSocketInformation')
make_head(_module, 'DatagramSocketMessageReceivedEventArgs')
make_head(_module, 'IControlChannelTrigger')
make_head(_module, 'IControlChannelTrigger2')
make_head(_module, 'IControlChannelTriggerEventDetails')
make_head(_module, 'IControlChannelTriggerFactory')
make_head(_module, 'IControlChannelTriggerResetEventDetails')
make_head(_module, 'IDatagramSocket')
make_head(_module, 'IDatagramSocket2')
make_head(_module, 'IDatagramSocket3')
make_head(_module, 'IDatagramSocketControl')
make_head(_module, 'IDatagramSocketControl2')
make_head(_module, 'IDatagramSocketControl3')
make_head(_module, 'IDatagramSocketInformation')
make_head(_module, 'IDatagramSocketMessageReceivedEventArgs')
make_head(_module, 'IDatagramSocketStatics')
make_head(_module, 'IMessageWebSocket')
make_head(_module, 'IMessageWebSocket2')
make_head(_module, 'IMessageWebSocket3')
make_head(_module, 'IMessageWebSocketControl')
make_head(_module, 'IMessageWebSocketControl2')
make_head(_module, 'IMessageWebSocketMessageReceivedEventArgs')
make_head(_module, 'IMessageWebSocketMessageReceivedEventArgs2')
make_head(_module, 'IServerMessageWebSocket')
make_head(_module, 'IServerMessageWebSocketControl')
make_head(_module, 'IServerMessageWebSocketInformation')
make_head(_module, 'IServerStreamWebSocket')
make_head(_module, 'IServerStreamWebSocketInformation')
make_head(_module, 'ISocketActivityContext')
make_head(_module, 'ISocketActivityContextFactory')
make_head(_module, 'ISocketActivityInformation')
make_head(_module, 'ISocketActivityInformationStatics')
make_head(_module, 'ISocketActivityTriggerDetails')
make_head(_module, 'ISocketErrorStatics')
make_head(_module, 'IStreamSocket')
make_head(_module, 'IStreamSocket2')
make_head(_module, 'IStreamSocket3')
make_head(_module, 'IStreamSocketControl')
make_head(_module, 'IStreamSocketControl2')
make_head(_module, 'IStreamSocketControl3')
make_head(_module, 'IStreamSocketControl4')
make_head(_module, 'IStreamSocketInformation')
make_head(_module, 'IStreamSocketInformation2')
make_head(_module, 'IStreamSocketListener')
make_head(_module, 'IStreamSocketListener2')
make_head(_module, 'IStreamSocketListener3')
make_head(_module, 'IStreamSocketListenerConnectionReceivedEventArgs')
make_head(_module, 'IStreamSocketListenerControl')
make_head(_module, 'IStreamSocketListenerControl2')
make_head(_module, 'IStreamSocketListenerInformation')
make_head(_module, 'IStreamSocketStatics')
make_head(_module, 'IStreamWebSocket')
make_head(_module, 'IStreamWebSocket2')
make_head(_module, 'IStreamWebSocketControl')
make_head(_module, 'IStreamWebSocketControl2')
make_head(_module, 'IWebSocket')
make_head(_module, 'IWebSocketClosedEventArgs')
make_head(_module, 'IWebSocketControl')
make_head(_module, 'IWebSocketControl2')
make_head(_module, 'IWebSocketErrorStatics')
make_head(_module, 'IWebSocketInformation')
make_head(_module, 'IWebSocketInformation2')
make_head(_module, 'IWebSocketServerCustomValidationRequestedEventArgs')
make_head(_module, 'MessageWebSocket')
make_head(_module, 'MessageWebSocketControl')
make_head(_module, 'MessageWebSocketInformation')
make_head(_module, 'MessageWebSocketMessageReceivedEventArgs')
make_head(_module, 'RoundTripTimeStatistics')
make_head(_module, 'ServerMessageWebSocket')
make_head(_module, 'ServerMessageWebSocketControl')
make_head(_module, 'ServerMessageWebSocketInformation')
make_head(_module, 'ServerStreamWebSocket')
make_head(_module, 'ServerStreamWebSocketInformation')
make_head(_module, 'SocketActivityContext')
make_head(_module, 'SocketActivityInformation')
make_head(_module, 'SocketActivityTriggerDetails')
make_head(_module, 'SocketError')
make_head(_module, 'StreamSocket')
make_head(_module, 'StreamSocketControl')
make_head(_module, 'StreamSocketInformation')
make_head(_module, 'StreamSocketListener')
make_head(_module, 'StreamSocketListenerConnectionReceivedEventArgs')
make_head(_module, 'StreamSocketListenerControl')
make_head(_module, 'StreamSocketListenerInformation')
make_head(_module, 'StreamWebSocket')
make_head(_module, 'StreamWebSocketControl')
make_head(_module, 'StreamWebSocketInformation')
make_head(_module, 'WebSocketClosedEventArgs')
make_head(_module, 'WebSocketError')
make_head(_module, 'WebSocketKeepAlive')
make_head(_module, 'WebSocketServerCustomValidationRequestedEventArgs')
