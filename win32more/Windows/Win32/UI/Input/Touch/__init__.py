from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Input.Touch
@winfunctype('USER32.dll')
def GetTouchInputInfo(hTouchInput: win32more.Windows.Win32.UI.Input.Touch.HTOUCHINPUT, cInputs: UInt32, pInputs: POINTER(win32more.Windows.Win32.UI.Input.Touch.TOUCHINPUT), cbSize: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseTouchInputHandle(hTouchInput: win32more.Windows.Win32.UI.Input.Touch.HTOUCHINPUT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RegisterTouchWindow(hwnd: win32more.Windows.Win32.Foundation.HWND, ulFlags: win32more.Windows.Win32.UI.Input.Touch.REGISTER_TOUCH_WINDOW_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnregisterTouchWindow(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsTouchWindow(hwnd: win32more.Windows.Win32.Foundation.HWND, pulFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetGestureInfo(hGestureInfo: win32more.Windows.Win32.UI.Input.Touch.HGESTUREINFO, pGestureInfo: POINTER(win32more.Windows.Win32.UI.Input.Touch.GESTUREINFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetGestureExtraArgs(hGestureInfo: win32more.Windows.Win32.UI.Input.Touch.HGESTUREINFO, cbExtraArgs: UInt32, pExtraArgs: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseGestureInfoHandle(hGestureInfo: win32more.Windows.Win32.UI.Input.Touch.HGESTUREINFO) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetGestureConfig(hwnd: win32more.Windows.Win32.Foundation.HWND, dwReserved: UInt32, cIDs: UInt32, pGestureConfig: POINTER(win32more.Windows.Win32.UI.Input.Touch.GESTURECONFIG), cbSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetGestureConfig(hwnd: win32more.Windows.Win32.Foundation.HWND, dwReserved: UInt32, dwFlags: UInt32, pcIDs: POINTER(UInt32), pGestureConfig: POINTER(win32more.Windows.Win32.UI.Input.Touch.GESTURECONFIG), cbSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
class GESTURECONFIG(EasyCastStructure):
    dwID: win32more.Windows.Win32.UI.Input.Touch.GESTURECONFIG_ID
    dwWant: UInt32
    dwBlock: UInt32
GESTURECONFIG_ID = UInt32
GID_BEGIN: GESTURECONFIG_ID = 1
GID_END: GESTURECONFIG_ID = 2
GID_ZOOM: GESTURECONFIG_ID = 3
GID_PAN: GESTURECONFIG_ID = 4
GID_ROTATE: GESTURECONFIG_ID = 5
GID_TWOFINGERTAP: GESTURECONFIG_ID = 6
GID_PRESSANDTAP: GESTURECONFIG_ID = 7
GID_ROLLOVER: GESTURECONFIG_ID = 7
class GESTUREINFO(EasyCastStructure):
    cbSize: UInt32
    dwFlags: UInt32
    dwID: UInt32
    hwndTarget: win32more.Windows.Win32.Foundation.HWND
    ptsLocation: win32more.Windows.Win32.Foundation.POINTS
    dwInstanceID: UInt32
    dwSequenceID: UInt32
    ullArguments: UInt64
    cbExtraArgs: UInt32
class GESTURENOTIFYSTRUCT(EasyCastStructure):
    cbSize: UInt32
    dwFlags: UInt32
    hwndTarget: win32more.Windows.Win32.Foundation.HWND
    ptsLocation: win32more.Windows.Win32.Foundation.POINTS
    dwInstanceID: UInt32
HGESTUREINFO = IntPtr
HTOUCHINPUT = IntPtr
class IInertiaProcessor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{18b00c6d-c5ee-41b1-90a9-9d4a929095ad}')
    @commethod(3)
    def get_InitialOriginX(self, x: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_InitialOriginX(self, x: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_InitialOriginY(self, y: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_InitialOriginY(self, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_InitialVelocityX(self, x: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_InitialVelocityX(self, x: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_InitialVelocityY(self, y: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_InitialVelocityY(self, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InitialAngularVelocity(self, velocity: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_InitialAngularVelocity(self, velocity: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_InitialExpansionVelocity(self, velocity: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_InitialExpansionVelocity(self, velocity: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_InitialRadius(self, radius: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_InitialRadius(self, radius: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BoundaryLeft(self, left: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BoundaryLeft(self, left: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_BoundaryTop(self, top: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_BoundaryTop(self, top: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_BoundaryRight(self, right: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_BoundaryRight(self, right: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_BoundaryBottom(self, bottom: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_BoundaryBottom(self, bottom: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_ElasticMarginLeft(self, left: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_ElasticMarginLeft(self, left: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ElasticMarginTop(self, top: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_ElasticMarginTop(self, top: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_ElasticMarginRight(self, right: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_ElasticMarginRight(self, right: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_ElasticMarginBottom(self, bottom: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_ElasticMarginBottom(self, bottom: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_DesiredDisplacement(self, displacement: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_DesiredDisplacement(self, displacement: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_DesiredRotation(self, rotation: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_DesiredRotation(self, rotation: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_DesiredExpansion(self, expansion: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_DesiredExpansion(self, expansion: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_DesiredDeceleration(self, deceleration: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_DesiredDeceleration(self, deceleration: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_DesiredAngularDeceleration(self, deceleration: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_DesiredAngularDeceleration(self, deceleration: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_DesiredExpansionDeceleration(self, deceleration: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_DesiredExpansionDeceleration(self, deceleration: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_InitialTimestamp(self, timestamp: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_InitialTimestamp(self, timestamp: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def Process(self, completed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def ProcessTime(self, timestamp: UInt32, completed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def Complete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def CompleteTime(self, timestamp: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IManipulationProcessor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a22ac519-8300-48a0-bef4-f1be8737dba4}')
    @commethod(3)
    def get_SupportedManipulations(self, manipulations: POINTER(win32more.Windows.Win32.UI.Input.Touch.MANIPULATION_PROCESSOR_MANIPULATIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_SupportedManipulations(self, manipulations: win32more.Windows.Win32.UI.Input.Touch.MANIPULATION_PROCESSOR_MANIPULATIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PivotPointX(self, pivotPointX: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_PivotPointX(self, pivotPointX: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_PivotPointY(self, pivotPointY: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_PivotPointY(self, pivotPointY: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PivotRadius(self, pivotRadius: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_PivotRadius(self, pivotRadius: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CompleteManipulation(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ProcessDown(self, manipulatorId: UInt32, x: Single, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ProcessMove(self, manipulatorId: UInt32, x: Single, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ProcessUp(self, manipulatorId: UInt32, x: Single, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ProcessDownWithTime(self, manipulatorId: UInt32, x: Single, y: Single, timestamp: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ProcessMoveWithTime(self, manipulatorId: UInt32, x: Single, y: Single, timestamp: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ProcessUpWithTime(self, manipulatorId: UInt32, x: Single, y: Single, timestamp: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetVelocityX(self, velocityX: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetVelocityY(self, velocityY: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetExpansionVelocity(self, expansionVelocity: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetAngularVelocity(self, angularVelocity: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_MinimumScaleRotateRadius(self, minRadius: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_MinimumScaleRotateRadius(self, minRadius: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
InertiaProcessor = Guid('{abb27087-4ce0-4e58-a0cb-e24df96814be}')
MANIPULATION_PROCESSOR_MANIPULATIONS = Int32
MANIPULATION_NONE: MANIPULATION_PROCESSOR_MANIPULATIONS = 0
MANIPULATION_TRANSLATE_X: MANIPULATION_PROCESSOR_MANIPULATIONS = 1
MANIPULATION_TRANSLATE_Y: MANIPULATION_PROCESSOR_MANIPULATIONS = 2
MANIPULATION_SCALE: MANIPULATION_PROCESSOR_MANIPULATIONS = 4
MANIPULATION_ROTATE: MANIPULATION_PROCESSOR_MANIPULATIONS = 8
MANIPULATION_ALL: MANIPULATION_PROCESSOR_MANIPULATIONS = 15
ManipulationProcessor = Guid('{597d4fb0-47fd-4aff-89b9-c6cfae8cf08e}')
REGISTER_TOUCH_WINDOW_FLAGS = UInt32
TWF_FINETOUCH: REGISTER_TOUCH_WINDOW_FLAGS = 1
TWF_WANTPALM: REGISTER_TOUCH_WINDOW_FLAGS = 2
TOUCHEVENTF_FLAGS = UInt32
TOUCHEVENTF_MOVE: TOUCHEVENTF_FLAGS = 1
TOUCHEVENTF_DOWN: TOUCHEVENTF_FLAGS = 2
TOUCHEVENTF_UP: TOUCHEVENTF_FLAGS = 4
TOUCHEVENTF_INRANGE: TOUCHEVENTF_FLAGS = 8
TOUCHEVENTF_PRIMARY: TOUCHEVENTF_FLAGS = 16
TOUCHEVENTF_NOCOALESCE: TOUCHEVENTF_FLAGS = 32
TOUCHEVENTF_PEN: TOUCHEVENTF_FLAGS = 64
TOUCHEVENTF_PALM: TOUCHEVENTF_FLAGS = 128
class TOUCHINPUT(EasyCastStructure):
    x: Int32
    y: Int32
    hSource: win32more.Windows.Win32.Foundation.HANDLE
    dwID: UInt32
    dwFlags: win32more.Windows.Win32.UI.Input.Touch.TOUCHEVENTF_FLAGS
    dwMask: win32more.Windows.Win32.UI.Input.Touch.TOUCHINPUTMASKF_MASK
    dwTime: UInt32
    dwExtraInfo: UIntPtr
    cxContact: UInt32
    cyContact: UInt32
TOUCHINPUTMASKF_MASK = UInt32
TOUCHINPUTMASKF_TIMEFROMSYSTEM: TOUCHINPUTMASKF_MASK = 1
TOUCHINPUTMASKF_EXTRAINFO: TOUCHINPUTMASKF_MASK = 2
TOUCHINPUTMASKF_CONTACTAREA: TOUCHINPUTMASKF_MASK = 4
class _IManipulationEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4f62c8da-9c53-4b22-93df-927a862bbb03}')
    @commethod(3)
    def ManipulationStarted(self, x: Single, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ManipulationDelta(self, x: Single, y: Single, translationDeltaX: Single, translationDeltaY: Single, scaleDelta: Single, expansionDelta: Single, rotationDelta: Single, cumulativeTranslationX: Single, cumulativeTranslationY: Single, cumulativeScale: Single, cumulativeExpansion: Single, cumulativeRotation: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ManipulationCompleted(self, x: Single, y: Single, cumulativeTranslationX: Single, cumulativeTranslationY: Single, cumulativeScale: Single, cumulativeExpansion: Single, cumulativeRotation: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_ready(__name__)
