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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.System.RemoteDesktop
class IInteractiveSessionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.IInteractiveSessionStatics'
    _iid_ = Guid('{60884631-dd3a-4576-9c8d-e8027618bdce}')
    @winrt_commethod(6)
    def get_IsRemote(self) -> Boolean: ...
    IsRemote = property(get_IsRemote, None)
class _InteractiveSession_Meta_(ComPtr.__class__):
    pass
class InteractiveSession(ComPtr, metaclass=_InteractiveSession_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.InteractiveSession'
    @winrt_classmethod
    def get_IsRemote(cls: win32more.Windows.System.RemoteDesktop.IInteractiveSessionStatics) -> Boolean: ...
    _InteractiveSession_Meta_.IsRemote = property(get_IsRemote.__wrapped__, None)
make_ready(__name__)
