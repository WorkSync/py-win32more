from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.DXCore
import win32more.Windows.Win32.System.Com
_FACDXCORE: UInt32 = 2176
DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS: Guid = Guid('{8c47866b-7583-450d-f0f0-6bada895af4b}')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS: Guid = Guid('{0c9ece4d-2f6e-4f01-8c96-e89e331b47b1}')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE: Guid = Guid('{248e2800-a793-4724-abaa-23a6de1be090}')
@winfunctype('DXCORE.dll')
def DXCoreCreateAdapterFactory(riid: POINTER(Guid), ppvFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DXCoreAdapterMemoryBudget(EasyCastStructure):
    budget: UInt64
    currentUsage: UInt64
    availableForReservation: UInt64
    currentReservation: UInt64
class DXCoreAdapterMemoryBudgetNodeSegmentGroup(EasyCastStructure):
    nodeIndex: UInt32
    segmentGroup: win32more.Windows.Win32.Graphics.DXCore.DXCoreSegmentGroup
DXCoreAdapterPreference = UInt32
DXCoreAdapterPreference_Hardware: DXCoreAdapterPreference = 0
DXCoreAdapterPreference_MinimumPower: DXCoreAdapterPreference = 1
DXCoreAdapterPreference_HighPerformance: DXCoreAdapterPreference = 2
DXCoreAdapterProperty = UInt32
DXCoreAdapterProperty_InstanceLuid: DXCoreAdapterProperty = 0
DXCoreAdapterProperty_DriverVersion: DXCoreAdapterProperty = 1
DXCoreAdapterProperty_DriverDescription: DXCoreAdapterProperty = 2
DXCoreAdapterProperty_HardwareID: DXCoreAdapterProperty = 3
DXCoreAdapterProperty_KmdModelVersion: DXCoreAdapterProperty = 4
DXCoreAdapterProperty_ComputePreemptionGranularity: DXCoreAdapterProperty = 5
DXCoreAdapterProperty_GraphicsPreemptionGranularity: DXCoreAdapterProperty = 6
DXCoreAdapterProperty_DedicatedAdapterMemory: DXCoreAdapterProperty = 7
DXCoreAdapterProperty_DedicatedSystemMemory: DXCoreAdapterProperty = 8
DXCoreAdapterProperty_SharedSystemMemory: DXCoreAdapterProperty = 9
DXCoreAdapterProperty_AcgCompatible: DXCoreAdapterProperty = 10
DXCoreAdapterProperty_IsHardware: DXCoreAdapterProperty = 11
DXCoreAdapterProperty_IsIntegrated: DXCoreAdapterProperty = 12
DXCoreAdapterProperty_IsDetachable: DXCoreAdapterProperty = 13
DXCoreAdapterProperty_HardwareIDParts: DXCoreAdapterProperty = 14
DXCoreAdapterState = UInt32
DXCoreAdapterState_IsDriverUpdateInProgress: DXCoreAdapterState = 0
DXCoreAdapterState_AdapterMemoryBudget: DXCoreAdapterState = 1
class DXCoreHardwareID(EasyCastStructure):
    vendorID: UInt32
    deviceID: UInt32
    subSysID: UInt32
    revision: UInt32
class DXCoreHardwareIDParts(EasyCastStructure):
    vendorID: UInt32
    deviceID: UInt32
    subSystemID: UInt32
    subVendorID: UInt32
    revisionID: UInt32
DXCoreNotificationType = UInt32
DXCoreNotificationType_AdapterListStale: DXCoreNotificationType = 0
DXCoreNotificationType_AdapterNoLongerValid: DXCoreNotificationType = 1
DXCoreNotificationType_AdapterBudgetChange: DXCoreNotificationType = 2
DXCoreNotificationType_AdapterHardwareContentProtectionTeardown: DXCoreNotificationType = 3
DXCoreSegmentGroup = UInt32
DXCoreSegmentGroup_Local: DXCoreSegmentGroup = 0
DXCoreSegmentGroup_NonLocal: DXCoreSegmentGroup = 1
class IDXCoreAdapter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0db4c7f-fe5a-42a2-bd62-f2a6cf6fc83e}')
    @commethod(3)
    def IsValid(self) -> Boolean: ...
    @commethod(4)
    def IsAttributeSupported(self, attributeGUID: POINTER(Guid)) -> Boolean: ...
    @commethod(5)
    def IsPropertySupported(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty) -> Boolean: ...
    @commethod(6)
    def GetProperty(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty, bufferSize: UIntPtr, propertyData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertySize(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty, bufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsQueryStateSupported(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState) -> Boolean: ...
    @commethod(9)
    def QueryState(self, state: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState, inputStateDetailsSize: UIntPtr, inputStateDetails: VoidPtr, outputBufferSize: UIntPtr, outputBuffer: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsSetStateSupported(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState) -> Boolean: ...
    @commethod(11)
    def SetState(self, state: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState, inputStateDetailsSize: UIntPtr, inputStateDetails: VoidPtr, inputDataSize: UIntPtr, inputData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFactory(self, riid: POINTER(Guid), ppvFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXCoreAdapterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{78ee5945-c36e-4b13-a669-005dd11c0f06}')
    @commethod(3)
    def CreateAdapterList(self, numAttributes: UInt32, filterAttributes: POINTER(Guid), riid: POINTER(Guid), ppvAdapterList: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAdapterByLuid(self, adapterLUID: POINTER(win32more.Windows.Win32.Foundation.LUID), riid: POINTER(Guid), ppvAdapter: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsNotificationTypeSupported(self, notificationType: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType) -> Boolean: ...
    @commethod(6)
    def RegisterEventNotification(self, dxCoreObject: win32more.Windows.Win32.System.Com.IUnknown, notificationType: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType, callbackFunction: win32more.Windows.Win32.Graphics.DXCore.PFN_DXCORE_NOTIFICATION_CALLBACK, callbackContext: VoidPtr, eventCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterEventNotification(self, eventCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXCoreAdapterList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{526c7776-40e9-459b-b711-f32ad76dfc28}')
    @commethod(3)
    def GetAdapter(self, index: UInt32, riid: POINTER(Guid), ppvAdapter: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAdapterCount(self) -> UInt32: ...
    @commethod(5)
    def IsStale(self) -> Boolean: ...
    @commethod(6)
    def GetFactory(self, riid: POINTER(Guid), ppvFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Sort(self, numPreferences: UInt32, preferences: POINTER(win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterPreference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsAdapterPreferenceSupported(self, preference: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterPreference) -> Boolean: ...
@winfunctype_pointer
def PFN_DXCORE_NOTIFICATION_CALLBACK(notificationType: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType, object: win32more.Windows.Win32.System.Com.IUnknown, context: VoidPtr) -> Void: ...
make_ready(__name__)
