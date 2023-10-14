from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.PasswordManagement
@winfunctype('ADVAPI32.dll')
def MSChapSrvChangePassword(ServerName: win32more.Windows.Win32.Foundation.PWSTR, UserName: win32more.Windows.Win32.Foundation.PWSTR, LmOldPresent: win32more.Windows.Win32.Foundation.BOOLEAN, LmOldOwfPassword: POINTER(win32more.Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD), LmNewOwfPassword: POINTER(win32more.Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD), NtOldOwfPassword: POINTER(win32more.Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD), NtNewOwfPassword: POINTER(win32more.Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def MSChapSrvChangePassword2(ServerName: win32more.Windows.Win32.Foundation.PWSTR, UserName: win32more.Windows.Win32.Foundation.PWSTR, NewPasswordEncryptedWithOldNt: POINTER(win32more.Windows.Win32.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD), OldNtOwfPasswordEncryptedWithNewNt: POINTER(win32more.Windows.Win32.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD), LmPresent: win32more.Windows.Win32.Foundation.BOOLEAN, NewPasswordEncryptedWithOldLm: POINTER(win32more.Windows.Win32.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD), OldLmOwfPasswordEncryptedWithNewLmOrNt: POINTER(win32more.Windows.Win32.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD)) -> UInt32: ...
class CYPHER_BLOCK(EasyCastStructure):
    data: win32more.Windows.Win32.Foundation.CHAR * 8
class ENCRYPTED_LM_OWF_PASSWORD(EasyCastStructure):
    data: win32more.Windows.Win32.System.PasswordManagement.CYPHER_BLOCK * 2
class LM_OWF_PASSWORD(EasyCastStructure):
    data: win32more.Windows.Win32.System.PasswordManagement.CYPHER_BLOCK * 2
class SAMPR_ENCRYPTED_USER_PASSWORD(EasyCastStructure):
    Buffer: Byte * 516
make_ready(__name__)
