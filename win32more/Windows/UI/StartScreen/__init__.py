from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Perception.Spatial
import win32more.Windows.System
import win32more.Windows.UI
import win32more.Windows.UI.Popups
import win32more.Windows.UI.StartScreen
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ForegroundText = Int32
ForegroundText_Dark: ForegroundText = 0
ForegroundText_Light: ForegroundText = 1
class IJumpList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IJumpList'
    _iid_ = Guid('{b0234c3e-cd6f-4cb6-a611-61fd505f3ed1}')
    @winrt_commethod(6)
    def get_Items(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.StartScreen.JumpListItem]: ...
    @winrt_commethod(7)
    def get_SystemGroupKind(self) -> win32more.Windows.UI.StartScreen.JumpListSystemGroupKind: ...
    @winrt_commethod(8)
    def put_SystemGroupKind(self, value: win32more.Windows.UI.StartScreen.JumpListSystemGroupKind) -> Void: ...
    @winrt_commethod(9)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Items = property(get_Items, None)
    SystemGroupKind = property(get_SystemGroupKind, put_SystemGroupKind)
class IJumpListItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IJumpListItem'
    _iid_ = Guid('{7adb6717-8b5d-4820-995b-9b418dbe48b0}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.UI.StartScreen.JumpListItemKind: ...
    @winrt_commethod(7)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemovedByUser(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_GroupName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_GroupName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_Logo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_Logo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Kind = property(get_Kind, None)
    Arguments = property(get_Arguments, None)
    RemovedByUser = property(get_RemovedByUser, None)
    Description = property(get_Description, put_Description)
    DisplayName = property(get_DisplayName, put_DisplayName)
    GroupName = property(get_GroupName, put_GroupName)
    Logo = property(get_Logo, put_Logo)
class IJumpListItemStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IJumpListItemStatics'
    _iid_ = Guid('{f1bfc4e8-c7aa-49cb-8dde-ecfccd7ad7e4}')
    @winrt_commethod(6)
    def CreateWithArguments(self, arguments: WinRT_String, displayName: WinRT_String) -> win32more.Windows.UI.StartScreen.JumpListItem: ...
    @winrt_commethod(7)
    def CreateSeparator(self) -> win32more.Windows.UI.StartScreen.JumpListItem: ...
class IJumpListStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IJumpListStatics'
    _iid_ = Guid('{a7e0c681-e67e-4b74-8250-3f322c4d92c3}')
    @winrt_commethod(6)
    def LoadCurrentAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.StartScreen.JumpList]: ...
    @winrt_commethod(7)
    def IsSupported(self) -> Boolean: ...
class ISecondaryTile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ISecondaryTile'
    _iid_ = Guid('{9e9e51e0-2bb5-4bc0-bb8d-42b23abcc88d}')
    @winrt_commethod(6)
    def put_TileId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_TileId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Arguments(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_ShortName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_ShortName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Logo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(15)
    def get_Logo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_SmallLogo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(17)
    def get_SmallLogo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(18)
    def put_WideLogo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(19)
    def get_WideLogo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(20)
    def put_LockScreenBadgeLogo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(21)
    def get_LockScreenBadgeLogo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(22)
    def put_LockScreenDisplayBadgeAndTileText(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def get_LockScreenDisplayBadgeAndTileText(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_TileOptions(self, value: win32more.Windows.UI.StartScreen.TileOptions) -> Void: ...
    @winrt_commethod(25)
    def get_TileOptions(self) -> win32more.Windows.UI.StartScreen.TileOptions: ...
    @winrt_commethod(26)
    def put_ForegroundText(self, value: win32more.Windows.UI.StartScreen.ForegroundText) -> Void: ...
    @winrt_commethod(27)
    def get_ForegroundText(self) -> win32more.Windows.UI.StartScreen.ForegroundText: ...
    @winrt_commethod(28)
    def put_BackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(29)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(30)
    def RequestCreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(31)
    def RequestCreateAsyncWithPoint(self, invocationPoint: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(32)
    def RequestCreateAsyncWithRect(self, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(33)
    def RequestCreateAsyncWithRectAndPlacement(self, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(34)
    def RequestDeleteAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(35)
    def RequestDeleteAsyncWithPoint(self, invocationPoint: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(36)
    def RequestDeleteAsyncWithRect(self, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(37)
    def RequestDeleteAsyncWithRectAndPlacement(self, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(38)
    def UpdateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    TileId = property(get_TileId, put_TileId)
    Arguments = property(get_Arguments, put_Arguments)
    ShortName = property(get_ShortName, put_ShortName)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Logo = property(get_Logo, put_Logo)
    SmallLogo = property(get_SmallLogo, put_SmallLogo)
    WideLogo = property(get_WideLogo, put_WideLogo)
    LockScreenBadgeLogo = property(get_LockScreenBadgeLogo, put_LockScreenBadgeLogo)
    LockScreenDisplayBadgeAndTileText = property(get_LockScreenDisplayBadgeAndTileText, put_LockScreenDisplayBadgeAndTileText)
    TileOptions = property(get_TileOptions, put_TileOptions)
    ForegroundText = property(get_ForegroundText, put_ForegroundText)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
class ISecondaryTile2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ISecondaryTile2'
    _iid_ = Guid('{b2f6cc35-3250-4990-923c-294ab4b694dd}')
    @winrt_commethod(6)
    def put_PhoneticName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_PhoneticName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_VisualElements(self) -> win32more.Windows.UI.StartScreen.SecondaryTileVisualElements: ...
    @winrt_commethod(9)
    def put_RoamingEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_RoamingEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def add_VisualElementsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.StartScreen.SecondaryTile, win32more.Windows.UI.StartScreen.VisualElementsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_VisualElementsRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PhoneticName = property(get_PhoneticName, put_PhoneticName)
    VisualElements = property(get_VisualElements, None)
    RoamingEnabled = property(get_RoamingEnabled, put_RoamingEnabled)
class ISecondaryTileFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ISecondaryTileFactory'
    _iid_ = Guid('{57f52ca0-51bc-4abf-8ebf-627a0398b05a}')
    @winrt_commethod(6)
    def CreateTile(self, tileId: WinRT_String, shortName: WinRT_String, displayName: WinRT_String, arguments: WinRT_String, tileOptions: win32more.Windows.UI.StartScreen.TileOptions, logoReference: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.StartScreen.SecondaryTile: ...
    @winrt_commethod(7)
    def CreateWideTile(self, tileId: WinRT_String, shortName: WinRT_String, displayName: WinRT_String, arguments: WinRT_String, tileOptions: win32more.Windows.UI.StartScreen.TileOptions, logoReference: win32more.Windows.Foundation.Uri, wideLogoReference: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.StartScreen.SecondaryTile: ...
    @winrt_commethod(8)
    def CreateWithId(self, tileId: WinRT_String) -> win32more.Windows.UI.StartScreen.SecondaryTile: ...
class ISecondaryTileFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ISecondaryTileFactory2'
    _iid_ = Guid('{274b8a3b-522d-448e-9eb2-d0672ab345c8}')
    @winrt_commethod(6)
    def CreateMinimalTile(self, tileId: WinRT_String, displayName: WinRT_String, arguments: WinRT_String, square150x150Logo: win32more.Windows.Foundation.Uri, desiredSize: win32more.Windows.UI.StartScreen.TileSize) -> win32more.Windows.UI.StartScreen.SecondaryTile: ...
class ISecondaryTileStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ISecondaryTileStatics'
    _iid_ = Guid('{99908dae-d051-4676-87fe-9ec242d83c74}')
    @winrt_commethod(6)
    def Exists(self, tileId: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.StartScreen.SecondaryTile]]: ...
    @winrt_commethod(8)
    def FindAllForApplicationAsync(self, applicationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.StartScreen.SecondaryTile]]: ...
    @winrt_commethod(9)
    def FindAllForPackageAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.StartScreen.SecondaryTile]]: ...
class ISecondaryTileVisualElements(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ISecondaryTileVisualElements'
    _iid_ = Guid('{1d8df333-815e-413f-9f50-a81da70a96b2}')
    @winrt_commethod(6)
    def put_Square30x30Logo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def get_Square30x30Logo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def put_Square70x70Logo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(9)
    def get_Square70x70Logo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def put_Square150x150Logo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(11)
    def get_Square150x150Logo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_Wide310x150Logo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(13)
    def get_Wide310x150Logo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(14)
    def put_Square310x310Logo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(15)
    def get_Square310x310Logo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_ForegroundText(self, value: win32more.Windows.UI.StartScreen.ForegroundText) -> Void: ...
    @winrt_commethod(17)
    def get_ForegroundText(self) -> win32more.Windows.UI.StartScreen.ForegroundText: ...
    @winrt_commethod(18)
    def put_BackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(19)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(20)
    def put_ShowNameOnSquare150x150Logo(self, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_ShowNameOnSquare150x150Logo(self) -> Boolean: ...
    @winrt_commethod(22)
    def put_ShowNameOnWide310x150Logo(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def get_ShowNameOnWide310x150Logo(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_ShowNameOnSquare310x310Logo(self, value: Boolean) -> Void: ...
    @winrt_commethod(25)
    def get_ShowNameOnSquare310x310Logo(self) -> Boolean: ...
    Square30x30Logo = property(get_Square30x30Logo, put_Square30x30Logo)
    Square70x70Logo = property(get_Square70x70Logo, put_Square70x70Logo)
    Square150x150Logo = property(get_Square150x150Logo, put_Square150x150Logo)
    Wide310x150Logo = property(get_Wide310x150Logo, put_Wide310x150Logo)
    Square310x310Logo = property(get_Square310x310Logo, put_Square310x310Logo)
    ForegroundText = property(get_ForegroundText, put_ForegroundText)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ShowNameOnSquare150x150Logo = property(get_ShowNameOnSquare150x150Logo, put_ShowNameOnSquare150x150Logo)
    ShowNameOnWide310x150Logo = property(get_ShowNameOnWide310x150Logo, put_ShowNameOnWide310x150Logo)
    ShowNameOnSquare310x310Logo = property(get_ShowNameOnSquare310x310Logo, put_ShowNameOnSquare310x310Logo)
class ISecondaryTileVisualElements2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ISecondaryTileVisualElements2'
    _iid_ = Guid('{fd2e31d0-57dc-4794-8ecf-5682f5f3e6ef}')
    @winrt_commethod(6)
    def put_Square71x71Logo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def get_Square71x71Logo(self) -> win32more.Windows.Foundation.Uri: ...
    Square71x71Logo = property(get_Square71x71Logo, put_Square71x71Logo)
class ISecondaryTileVisualElements3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ISecondaryTileVisualElements3'
    _iid_ = Guid('{56b55ad6-d15c-40f4-81e7-57ffd8f8a4e9}')
    @winrt_commethod(6)
    def put_Square44x44Logo(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def get_Square44x44Logo(self) -> win32more.Windows.Foundation.Uri: ...
    Square44x44Logo = property(get_Square44x44Logo, put_Square44x44Logo)
class ISecondaryTileVisualElements4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ISecondaryTileVisualElements4'
    _iid_ = Guid('{66566117-b544-40d2-8d12-74d4ec24d04c}')
    @winrt_commethod(6)
    def get_MixedRealityModel(self) -> win32more.Windows.UI.StartScreen.TileMixedRealityModel: ...
    MixedRealityModel = property(get_MixedRealityModel, None)
class IStartScreenManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IStartScreenManager'
    _iid_ = Guid('{4a1dcbcb-26e9-4eb4-8933-859eb6ecdb29}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def SupportsAppListEntry(self, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> Boolean: ...
    @winrt_commethod(8)
    def ContainsAppListEntryAsync(self, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def RequestAddAppListEntryAsync(self, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    User = property(get_User, None)
class IStartScreenManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IStartScreenManager2'
    _iid_ = Guid('{08a716b6-316b-4ad9-acb8-fe9cf00bd608}')
    @winrt_commethod(6)
    def ContainsSecondaryTileAsync(self, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def TryRemoveSecondaryTileAsync(self, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IStartScreenManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IStartScreenManagerStatics'
    _iid_ = Guid('{7865ef0f-b585-464e-8993-34e8f8738d48}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.UI.StartScreen.StartScreenManager: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.UI.StartScreen.StartScreenManager: ...
class ITileMixedRealityModel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ITileMixedRealityModel'
    _iid_ = Guid('{b0764e5b-887d-4242-9a19-3d0a4ea78031}')
    @winrt_commethod(6)
    def put_Uri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def put_BoundingBox(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingBox]) -> Void: ...
    @winrt_commethod(9)
    def get_BoundingBox(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingBox]: ...
    Uri = property(get_Uri, put_Uri)
    BoundingBox = property(get_BoundingBox, put_BoundingBox)
class ITileMixedRealityModel2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.ITileMixedRealityModel2'
    _iid_ = Guid('{439470b2-d7c5-410b-8319-9486a27b6c67}')
    @winrt_commethod(6)
    def put_ActivationBehavior(self, value: win32more.Windows.UI.StartScreen.TileMixedRealityModelActivationBehavior) -> Void: ...
    @winrt_commethod(7)
    def get_ActivationBehavior(self) -> win32more.Windows.UI.StartScreen.TileMixedRealityModelActivationBehavior: ...
    ActivationBehavior = property(get_ActivationBehavior, put_ActivationBehavior)
class IVisualElementsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IVisualElementsRequest'
    _iid_ = Guid('{c138333a-9308-4072-88cc-d068db347c68}')
    @winrt_commethod(6)
    def get_VisualElements(self) -> win32more.Windows.UI.StartScreen.SecondaryTileVisualElements: ...
    @winrt_commethod(7)
    def get_AlternateVisualElements(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.StartScreen.SecondaryTileVisualElements]: ...
    @winrt_commethod(8)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.UI.StartScreen.VisualElementsRequestDeferral: ...
    VisualElements = property(get_VisualElements, None)
    AlternateVisualElements = property(get_AlternateVisualElements, None)
    Deadline = property(get_Deadline, None)
class IVisualElementsRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IVisualElementsRequestDeferral'
    _iid_ = Guid('{a1656eb0-0126-4357-8204-bd82bb2a046d}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IVisualElementsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.StartScreen.IVisualElementsRequestedEventArgs'
    _iid_ = Guid('{7b6fc982-3a0d-4ece-af96-cd17e1b00b2d}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.UI.StartScreen.VisualElementsRequest: ...
    Request = property(get_Request, None)
class JumpList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.StartScreen.IJumpList
    _classid_ = 'Windows.UI.StartScreen.JumpList'
    @winrt_mixinmethod
    def get_Items(self: win32more.Windows.UI.StartScreen.IJumpList) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.StartScreen.JumpListItem]: ...
    @winrt_mixinmethod
    def get_SystemGroupKind(self: win32more.Windows.UI.StartScreen.IJumpList) -> win32more.Windows.UI.StartScreen.JumpListSystemGroupKind: ...
    @winrt_mixinmethod
    def put_SystemGroupKind(self: win32more.Windows.UI.StartScreen.IJumpList, value: win32more.Windows.UI.StartScreen.JumpListSystemGroupKind) -> Void: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.UI.StartScreen.IJumpList) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def LoadCurrentAsync(cls: win32more.Windows.UI.StartScreen.IJumpListStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.StartScreen.JumpList]: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.UI.StartScreen.IJumpListStatics) -> Boolean: ...
    Items = property(get_Items, None)
    SystemGroupKind = property(get_SystemGroupKind, put_SystemGroupKind)
class JumpListItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.StartScreen.IJumpListItem
    _classid_ = 'Windows.UI.StartScreen.JumpListItem'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.StartScreen.IJumpListItem) -> win32more.Windows.UI.StartScreen.JumpListItemKind: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.UI.StartScreen.IJumpListItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemovedByUser(self: win32more.Windows.UI.StartScreen.IJumpListItem) -> Boolean: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.UI.StartScreen.IJumpListItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.UI.StartScreen.IJumpListItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.UI.StartScreen.IJumpListItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.UI.StartScreen.IJumpListItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_GroupName(self: win32more.Windows.UI.StartScreen.IJumpListItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_GroupName(self: win32more.Windows.UI.StartScreen.IJumpListItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Logo(self: win32more.Windows.UI.StartScreen.IJumpListItem) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Logo(self: win32more.Windows.UI.StartScreen.IJumpListItem, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def CreateWithArguments(cls: win32more.Windows.UI.StartScreen.IJumpListItemStatics, arguments: WinRT_String, displayName: WinRT_String) -> win32more.Windows.UI.StartScreen.JumpListItem: ...
    @winrt_classmethod
    def CreateSeparator(cls: win32more.Windows.UI.StartScreen.IJumpListItemStatics) -> win32more.Windows.UI.StartScreen.JumpListItem: ...
    Kind = property(get_Kind, None)
    Arguments = property(get_Arguments, None)
    RemovedByUser = property(get_RemovedByUser, None)
    Description = property(get_Description, put_Description)
    DisplayName = property(get_DisplayName, put_DisplayName)
    GroupName = property(get_GroupName, put_GroupName)
    Logo = property(get_Logo, put_Logo)
JumpListItemKind = Int32
JumpListItemKind_Arguments: JumpListItemKind = 0
JumpListItemKind_Separator: JumpListItemKind = 1
JumpListSystemGroupKind = Int32
JumpListSystemGroupKind_None: JumpListSystemGroupKind = 0
JumpListSystemGroupKind_Frequent: JumpListSystemGroupKind = 1
JumpListSystemGroupKind_Recent: JumpListSystemGroupKind = 2
class SecondaryTile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.StartScreen.ISecondaryTile
    _classid_ = 'Windows.UI.StartScreen.SecondaryTile'
    @winrt_factorymethod
    def CreateMinimalTile(cls: win32more.Windows.UI.StartScreen.ISecondaryTileFactory2, tileId: WinRT_String, displayName: WinRT_String, arguments: WinRT_String, square150x150Logo: win32more.Windows.Foundation.Uri, desiredSize: win32more.Windows.UI.StartScreen.TileSize) -> win32more.Windows.UI.StartScreen.SecondaryTile: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.StartScreen.SecondaryTile: ...
    @winrt_factorymethod
    def CreateTile(cls: win32more.Windows.UI.StartScreen.ISecondaryTileFactory, tileId: WinRT_String, shortName: WinRT_String, displayName: WinRT_String, arguments: WinRT_String, tileOptions: win32more.Windows.UI.StartScreen.TileOptions, logoReference: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.StartScreen.SecondaryTile: ...
    @winrt_factorymethod
    def CreateWideTile(cls: win32more.Windows.UI.StartScreen.ISecondaryTileFactory, tileId: WinRT_String, shortName: WinRT_String, displayName: WinRT_String, arguments: WinRT_String, tileOptions: win32more.Windows.UI.StartScreen.TileOptions, logoReference: win32more.Windows.Foundation.Uri, wideLogoReference: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.StartScreen.SecondaryTile: ...
    @winrt_factorymethod
    def CreateWithId(cls: win32more.Windows.UI.StartScreen.ISecondaryTileFactory, tileId: WinRT_String) -> win32more.Windows.UI.StartScreen.SecondaryTile: ...
    @winrt_mixinmethod
    def put_TileId(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Arguments(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ShortName(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ShortName(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_SmallLogo(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_SmallLogo(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_WideLogo(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_WideLogo(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_LockScreenBadgeLogo(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_LockScreenBadgeLogo(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_LockScreenDisplayBadgeAndTileText(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LockScreenDisplayBadgeAndTileText(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> Boolean: ...
    @winrt_mixinmethod
    def put_TileOptions(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: win32more.Windows.UI.StartScreen.TileOptions) -> Void: ...
    @winrt_mixinmethod
    def get_TileOptions(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.UI.StartScreen.TileOptions: ...
    @winrt_mixinmethod
    def put_ForegroundText(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: win32more.Windows.UI.StartScreen.ForegroundText) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundText(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.UI.StartScreen.ForegroundText: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.UI.StartScreen.ISecondaryTile, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def RequestCreateAsync(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestCreateAsyncWithPoint(self: win32more.Windows.UI.StartScreen.ISecondaryTile, invocationPoint: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestCreateAsyncWithRect(self: win32more.Windows.UI.StartScreen.ISecondaryTile, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestCreateAsyncWithRectAndPlacement(self: win32more.Windows.UI.StartScreen.ISecondaryTile, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestDeleteAsync(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestDeleteAsyncWithPoint(self: win32more.Windows.UI.StartScreen.ISecondaryTile, invocationPoint: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestDeleteAsyncWithRect(self: win32more.Windows.UI.StartScreen.ISecondaryTile, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestDeleteAsyncWithRectAndPlacement(self: win32more.Windows.UI.StartScreen.ISecondaryTile, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def UpdateAsync(self: win32more.Windows.UI.StartScreen.ISecondaryTile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def put_PhoneticName(self: win32more.Windows.UI.StartScreen.ISecondaryTile2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PhoneticName(self: win32more.Windows.UI.StartScreen.ISecondaryTile2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VisualElements(self: win32more.Windows.UI.StartScreen.ISecondaryTile2) -> win32more.Windows.UI.StartScreen.SecondaryTileVisualElements: ...
    @winrt_mixinmethod
    def put_RoamingEnabled(self: win32more.Windows.UI.StartScreen.ISecondaryTile2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RoamingEnabled(self: win32more.Windows.UI.StartScreen.ISecondaryTile2) -> Boolean: ...
    @winrt_mixinmethod
    def add_VisualElementsRequested(self: win32more.Windows.UI.StartScreen.ISecondaryTile2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.StartScreen.SecondaryTile, win32more.Windows.UI.StartScreen.VisualElementsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisualElementsRequested(self: win32more.Windows.UI.StartScreen.ISecondaryTile2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def Exists(cls: win32more.Windows.UI.StartScreen.ISecondaryTileStatics, tileId: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.UI.StartScreen.ISecondaryTileStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.StartScreen.SecondaryTile]]: ...
    @winrt_classmethod
    def FindAllForApplicationAsync(cls: win32more.Windows.UI.StartScreen.ISecondaryTileStatics, applicationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.StartScreen.SecondaryTile]]: ...
    @winrt_classmethod
    def FindAllForPackageAsync(cls: win32more.Windows.UI.StartScreen.ISecondaryTileStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.StartScreen.SecondaryTile]]: ...
    TileId = property(get_TileId, put_TileId)
    Arguments = property(get_Arguments, put_Arguments)
    ShortName = property(get_ShortName, put_ShortName)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Logo = property(get_Logo, put_Logo)
    SmallLogo = property(get_SmallLogo, put_SmallLogo)
    WideLogo = property(get_WideLogo, put_WideLogo)
    LockScreenBadgeLogo = property(get_LockScreenBadgeLogo, put_LockScreenBadgeLogo)
    LockScreenDisplayBadgeAndTileText = property(get_LockScreenDisplayBadgeAndTileText, put_LockScreenDisplayBadgeAndTileText)
    TileOptions = property(get_TileOptions, put_TileOptions)
    ForegroundText = property(get_ForegroundText, put_ForegroundText)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    PhoneticName = property(get_PhoneticName, put_PhoneticName)
    VisualElements = property(get_VisualElements, None)
    RoamingEnabled = property(get_RoamingEnabled, put_RoamingEnabled)
class SecondaryTileVisualElements(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements
    _classid_ = 'Windows.UI.StartScreen.SecondaryTileVisualElements'
    @winrt_mixinmethod
    def put_Square30x30Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Square30x30Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Square70x70Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Square70x70Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Square150x150Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Square150x150Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Wide310x150Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Wide310x150Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Square310x310Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Square310x310Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ForegroundText(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: win32more.Windows.UI.StartScreen.ForegroundText) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundText(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> win32more.Windows.UI.StartScreen.ForegroundText: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ShowNameOnSquare150x150Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowNameOnSquare150x150Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowNameOnWide310x150Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowNameOnWide310x150Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowNameOnSquare310x310Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowNameOnSquare310x310Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements) -> Boolean: ...
    @winrt_mixinmethod
    def put_Square71x71Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements2, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Square71x71Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements2) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Square44x44Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements3, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Square44x44Logo(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements3) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_MixedRealityModel(self: win32more.Windows.UI.StartScreen.ISecondaryTileVisualElements4) -> win32more.Windows.UI.StartScreen.TileMixedRealityModel: ...
    Square30x30Logo = property(get_Square30x30Logo, put_Square30x30Logo)
    Square70x70Logo = property(get_Square70x70Logo, put_Square70x70Logo)
    Square150x150Logo = property(get_Square150x150Logo, put_Square150x150Logo)
    Wide310x150Logo = property(get_Wide310x150Logo, put_Wide310x150Logo)
    Square310x310Logo = property(get_Square310x310Logo, put_Square310x310Logo)
    ForegroundText = property(get_ForegroundText, put_ForegroundText)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ShowNameOnSquare150x150Logo = property(get_ShowNameOnSquare150x150Logo, put_ShowNameOnSquare150x150Logo)
    ShowNameOnWide310x150Logo = property(get_ShowNameOnWide310x150Logo, put_ShowNameOnWide310x150Logo)
    ShowNameOnSquare310x310Logo = property(get_ShowNameOnSquare310x310Logo, put_ShowNameOnSquare310x310Logo)
    Square71x71Logo = property(get_Square71x71Logo, put_Square71x71Logo)
    Square44x44Logo = property(get_Square44x44Logo, put_Square44x44Logo)
    MixedRealityModel = property(get_MixedRealityModel, None)
class StartScreenManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.StartScreen.IStartScreenManager
    _classid_ = 'Windows.UI.StartScreen.StartScreenManager'
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.UI.StartScreen.IStartScreenManager) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def SupportsAppListEntry(self: win32more.Windows.UI.StartScreen.IStartScreenManager, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> Boolean: ...
    @winrt_mixinmethod
    def ContainsAppListEntryAsync(self: win32more.Windows.UI.StartScreen.IStartScreenManager, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestAddAppListEntryAsync(self: win32more.Windows.UI.StartScreen.IStartScreenManager, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def ContainsSecondaryTileAsync(self: win32more.Windows.UI.StartScreen.IStartScreenManager2, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryRemoveSecondaryTileAsync(self: win32more.Windows.UI.StartScreen.IStartScreenManager2, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.UI.StartScreen.IStartScreenManagerStatics) -> win32more.Windows.UI.StartScreen.StartScreenManager: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.UI.StartScreen.IStartScreenManagerStatics, user: win32more.Windows.System.User) -> win32more.Windows.UI.StartScreen.StartScreenManager: ...
    User = property(get_User, None)
class TileMixedRealityModel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.StartScreen.ITileMixedRealityModel
    _classid_ = 'Windows.UI.StartScreen.TileMixedRealityModel'
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.UI.StartScreen.ITileMixedRealityModel, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.UI.StartScreen.ITileMixedRealityModel) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_BoundingBox(self: win32more.Windows.UI.StartScreen.ITileMixedRealityModel, value: win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingBox]) -> Void: ...
    @winrt_mixinmethod
    def get_BoundingBox(self: win32more.Windows.UI.StartScreen.ITileMixedRealityModel) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingBox]: ...
    @winrt_mixinmethod
    def put_ActivationBehavior(self: win32more.Windows.UI.StartScreen.ITileMixedRealityModel2, value: win32more.Windows.UI.StartScreen.TileMixedRealityModelActivationBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_ActivationBehavior(self: win32more.Windows.UI.StartScreen.ITileMixedRealityModel2) -> win32more.Windows.UI.StartScreen.TileMixedRealityModelActivationBehavior: ...
    Uri = property(get_Uri, put_Uri)
    BoundingBox = property(get_BoundingBox, put_BoundingBox)
    ActivationBehavior = property(get_ActivationBehavior, put_ActivationBehavior)
TileMixedRealityModelActivationBehavior = Int32
TileMixedRealityModelActivationBehavior_Default: TileMixedRealityModelActivationBehavior = 0
TileMixedRealityModelActivationBehavior_None: TileMixedRealityModelActivationBehavior = 1
TileOptions = UInt32
TileOptions_None: TileOptions = 0
TileOptions_ShowNameOnLogo: TileOptions = 1
TileOptions_ShowNameOnWideLogo: TileOptions = 2
TileOptions_CopyOnDeployment: TileOptions = 4
TileSize = Int32
TileSize_Default: TileSize = 0
TileSize_Square30x30: TileSize = 1
TileSize_Square70x70: TileSize = 2
TileSize_Square150x150: TileSize = 3
TileSize_Wide310x150: TileSize = 4
TileSize_Square310x310: TileSize = 5
TileSize_Square71x71: TileSize = 6
TileSize_Square44x44: TileSize = 7
class VisualElementsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.StartScreen.IVisualElementsRequest
    _classid_ = 'Windows.UI.StartScreen.VisualElementsRequest'
    @winrt_mixinmethod
    def get_VisualElements(self: win32more.Windows.UI.StartScreen.IVisualElementsRequest) -> win32more.Windows.UI.StartScreen.SecondaryTileVisualElements: ...
    @winrt_mixinmethod
    def get_AlternateVisualElements(self: win32more.Windows.UI.StartScreen.IVisualElementsRequest) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.StartScreen.SecondaryTileVisualElements]: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.UI.StartScreen.IVisualElementsRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.StartScreen.IVisualElementsRequest) -> win32more.Windows.UI.StartScreen.VisualElementsRequestDeferral: ...
    VisualElements = property(get_VisualElements, None)
    AlternateVisualElements = property(get_AlternateVisualElements, None)
    Deadline = property(get_Deadline, None)
class VisualElementsRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.StartScreen.IVisualElementsRequestDeferral
    _classid_ = 'Windows.UI.StartScreen.VisualElementsRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.StartScreen.IVisualElementsRequestDeferral) -> Void: ...
class VisualElementsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.StartScreen.IVisualElementsRequestedEventArgs
    _classid_ = 'Windows.UI.StartScreen.VisualElementsRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.StartScreen.IVisualElementsRequestedEventArgs) -> win32more.Windows.UI.StartScreen.VisualElementsRequest: ...
    Request = property(get_Request, None)
make_head(_module, 'IJumpList')
make_head(_module, 'IJumpListItem')
make_head(_module, 'IJumpListItemStatics')
make_head(_module, 'IJumpListStatics')
make_head(_module, 'ISecondaryTile')
make_head(_module, 'ISecondaryTile2')
make_head(_module, 'ISecondaryTileFactory')
make_head(_module, 'ISecondaryTileFactory2')
make_head(_module, 'ISecondaryTileStatics')
make_head(_module, 'ISecondaryTileVisualElements')
make_head(_module, 'ISecondaryTileVisualElements2')
make_head(_module, 'ISecondaryTileVisualElements3')
make_head(_module, 'ISecondaryTileVisualElements4')
make_head(_module, 'IStartScreenManager')
make_head(_module, 'IStartScreenManager2')
make_head(_module, 'IStartScreenManagerStatics')
make_head(_module, 'ITileMixedRealityModel')
make_head(_module, 'ITileMixedRealityModel2')
make_head(_module, 'IVisualElementsRequest')
make_head(_module, 'IVisualElementsRequestDeferral')
make_head(_module, 'IVisualElementsRequestedEventArgs')
make_head(_module, 'JumpList')
make_head(_module, 'JumpListItem')
make_head(_module, 'SecondaryTile')
make_head(_module, 'SecondaryTileVisualElements')
make_head(_module, 'StartScreenManager')
make_head(_module, 'TileMixedRealityModel')
make_head(_module, 'VisualElementsRequest')
make_head(_module, 'VisualElementsRequestDeferral')
make_head(_module, 'VisualElementsRequestedEventArgs')
