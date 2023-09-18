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
import win32more.Windows.Graphics.DirectX
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DirectXAlphaMode = Int32
DirectXAlphaMode_Unspecified: DirectXAlphaMode = 0
DirectXAlphaMode_Premultiplied: DirectXAlphaMode = 1
DirectXAlphaMode_Straight: DirectXAlphaMode = 2
DirectXAlphaMode_Ignore: DirectXAlphaMode = 3
DirectXColorSpace = Int32
DirectXColorSpace_RgbFullG22NoneP709: DirectXColorSpace = 0
DirectXColorSpace_RgbFullG10NoneP709: DirectXColorSpace = 1
DirectXColorSpace_RgbStudioG22NoneP709: DirectXColorSpace = 2
DirectXColorSpace_RgbStudioG22NoneP2020: DirectXColorSpace = 3
DirectXColorSpace_Reserved: DirectXColorSpace = 4
DirectXColorSpace_YccFullG22NoneP709X601: DirectXColorSpace = 5
DirectXColorSpace_YccStudioG22LeftP601: DirectXColorSpace = 6
DirectXColorSpace_YccFullG22LeftP601: DirectXColorSpace = 7
DirectXColorSpace_YccStudioG22LeftP709: DirectXColorSpace = 8
DirectXColorSpace_YccFullG22LeftP709: DirectXColorSpace = 9
DirectXColorSpace_YccStudioG22LeftP2020: DirectXColorSpace = 10
DirectXColorSpace_YccFullG22LeftP2020: DirectXColorSpace = 11
DirectXColorSpace_RgbFullG2084NoneP2020: DirectXColorSpace = 12
DirectXColorSpace_YccStudioG2084LeftP2020: DirectXColorSpace = 13
DirectXColorSpace_RgbStudioG2084NoneP2020: DirectXColorSpace = 14
DirectXColorSpace_YccStudioG22TopLeftP2020: DirectXColorSpace = 15
DirectXColorSpace_YccStudioG2084TopLeftP2020: DirectXColorSpace = 16
DirectXColorSpace_RgbFullG22NoneP2020: DirectXColorSpace = 17
DirectXColorSpace_YccStudioGHlgTopLeftP2020: DirectXColorSpace = 18
DirectXColorSpace_YccFullGHlgTopLeftP2020: DirectXColorSpace = 19
DirectXColorSpace_RgbStudioG24NoneP709: DirectXColorSpace = 20
DirectXColorSpace_RgbStudioG24NoneP2020: DirectXColorSpace = 21
DirectXColorSpace_YccStudioG24LeftP709: DirectXColorSpace = 22
DirectXColorSpace_YccStudioG24LeftP2020: DirectXColorSpace = 23
DirectXColorSpace_YccStudioG24TopLeftP2020: DirectXColorSpace = 24
DirectXPixelFormat = Int32
DirectXPixelFormat_Unknown: DirectXPixelFormat = 0
DirectXPixelFormat_R32G32B32A32Typeless: DirectXPixelFormat = 1
DirectXPixelFormat_R32G32B32A32Float: DirectXPixelFormat = 2
DirectXPixelFormat_R32G32B32A32UInt: DirectXPixelFormat = 3
DirectXPixelFormat_R32G32B32A32Int: DirectXPixelFormat = 4
DirectXPixelFormat_R32G32B32Typeless: DirectXPixelFormat = 5
DirectXPixelFormat_R32G32B32Float: DirectXPixelFormat = 6
DirectXPixelFormat_R32G32B32UInt: DirectXPixelFormat = 7
DirectXPixelFormat_R32G32B32Int: DirectXPixelFormat = 8
DirectXPixelFormat_R16G16B16A16Typeless: DirectXPixelFormat = 9
DirectXPixelFormat_R16G16B16A16Float: DirectXPixelFormat = 10
DirectXPixelFormat_R16G16B16A16UIntNormalized: DirectXPixelFormat = 11
DirectXPixelFormat_R16G16B16A16UInt: DirectXPixelFormat = 12
DirectXPixelFormat_R16G16B16A16IntNormalized: DirectXPixelFormat = 13
DirectXPixelFormat_R16G16B16A16Int: DirectXPixelFormat = 14
DirectXPixelFormat_R32G32Typeless: DirectXPixelFormat = 15
DirectXPixelFormat_R32G32Float: DirectXPixelFormat = 16
DirectXPixelFormat_R32G32UInt: DirectXPixelFormat = 17
DirectXPixelFormat_R32G32Int: DirectXPixelFormat = 18
DirectXPixelFormat_R32G8X24Typeless: DirectXPixelFormat = 19
DirectXPixelFormat_D32FloatS8X24UInt: DirectXPixelFormat = 20
DirectXPixelFormat_R32FloatX8X24Typeless: DirectXPixelFormat = 21
DirectXPixelFormat_X32TypelessG8X24UInt: DirectXPixelFormat = 22
DirectXPixelFormat_R10G10B10A2Typeless: DirectXPixelFormat = 23
DirectXPixelFormat_R10G10B10A2UIntNormalized: DirectXPixelFormat = 24
DirectXPixelFormat_R10G10B10A2UInt: DirectXPixelFormat = 25
DirectXPixelFormat_R11G11B10Float: DirectXPixelFormat = 26
DirectXPixelFormat_R8G8B8A8Typeless: DirectXPixelFormat = 27
DirectXPixelFormat_R8G8B8A8UIntNormalized: DirectXPixelFormat = 28
DirectXPixelFormat_R8G8B8A8UIntNormalizedSrgb: DirectXPixelFormat = 29
DirectXPixelFormat_R8G8B8A8UInt: DirectXPixelFormat = 30
DirectXPixelFormat_R8G8B8A8IntNormalized: DirectXPixelFormat = 31
DirectXPixelFormat_R8G8B8A8Int: DirectXPixelFormat = 32
DirectXPixelFormat_R16G16Typeless: DirectXPixelFormat = 33
DirectXPixelFormat_R16G16Float: DirectXPixelFormat = 34
DirectXPixelFormat_R16G16UIntNormalized: DirectXPixelFormat = 35
DirectXPixelFormat_R16G16UInt: DirectXPixelFormat = 36
DirectXPixelFormat_R16G16IntNormalized: DirectXPixelFormat = 37
DirectXPixelFormat_R16G16Int: DirectXPixelFormat = 38
DirectXPixelFormat_R32Typeless: DirectXPixelFormat = 39
DirectXPixelFormat_D32Float: DirectXPixelFormat = 40
DirectXPixelFormat_R32Float: DirectXPixelFormat = 41
DirectXPixelFormat_R32UInt: DirectXPixelFormat = 42
DirectXPixelFormat_R32Int: DirectXPixelFormat = 43
DirectXPixelFormat_R24G8Typeless: DirectXPixelFormat = 44
DirectXPixelFormat_D24UIntNormalizedS8UInt: DirectXPixelFormat = 45
DirectXPixelFormat_R24UIntNormalizedX8Typeless: DirectXPixelFormat = 46
DirectXPixelFormat_X24TypelessG8UInt: DirectXPixelFormat = 47
DirectXPixelFormat_R8G8Typeless: DirectXPixelFormat = 48
DirectXPixelFormat_R8G8UIntNormalized: DirectXPixelFormat = 49
DirectXPixelFormat_R8G8UInt: DirectXPixelFormat = 50
DirectXPixelFormat_R8G8IntNormalized: DirectXPixelFormat = 51
DirectXPixelFormat_R8G8Int: DirectXPixelFormat = 52
DirectXPixelFormat_R16Typeless: DirectXPixelFormat = 53
DirectXPixelFormat_R16Float: DirectXPixelFormat = 54
DirectXPixelFormat_D16UIntNormalized: DirectXPixelFormat = 55
DirectXPixelFormat_R16UIntNormalized: DirectXPixelFormat = 56
DirectXPixelFormat_R16UInt: DirectXPixelFormat = 57
DirectXPixelFormat_R16IntNormalized: DirectXPixelFormat = 58
DirectXPixelFormat_R16Int: DirectXPixelFormat = 59
DirectXPixelFormat_R8Typeless: DirectXPixelFormat = 60
DirectXPixelFormat_R8UIntNormalized: DirectXPixelFormat = 61
DirectXPixelFormat_R8UInt: DirectXPixelFormat = 62
DirectXPixelFormat_R8IntNormalized: DirectXPixelFormat = 63
DirectXPixelFormat_R8Int: DirectXPixelFormat = 64
DirectXPixelFormat_A8UIntNormalized: DirectXPixelFormat = 65
DirectXPixelFormat_R1UIntNormalized: DirectXPixelFormat = 66
DirectXPixelFormat_R9G9B9E5SharedExponent: DirectXPixelFormat = 67
DirectXPixelFormat_R8G8B8G8UIntNormalized: DirectXPixelFormat = 68
DirectXPixelFormat_G8R8G8B8UIntNormalized: DirectXPixelFormat = 69
DirectXPixelFormat_BC1Typeless: DirectXPixelFormat = 70
DirectXPixelFormat_BC1UIntNormalized: DirectXPixelFormat = 71
DirectXPixelFormat_BC1UIntNormalizedSrgb: DirectXPixelFormat = 72
DirectXPixelFormat_BC2Typeless: DirectXPixelFormat = 73
DirectXPixelFormat_BC2UIntNormalized: DirectXPixelFormat = 74
DirectXPixelFormat_BC2UIntNormalizedSrgb: DirectXPixelFormat = 75
DirectXPixelFormat_BC3Typeless: DirectXPixelFormat = 76
DirectXPixelFormat_BC3UIntNormalized: DirectXPixelFormat = 77
DirectXPixelFormat_BC3UIntNormalizedSrgb: DirectXPixelFormat = 78
DirectXPixelFormat_BC4Typeless: DirectXPixelFormat = 79
DirectXPixelFormat_BC4UIntNormalized: DirectXPixelFormat = 80
DirectXPixelFormat_BC4IntNormalized: DirectXPixelFormat = 81
DirectXPixelFormat_BC5Typeless: DirectXPixelFormat = 82
DirectXPixelFormat_BC5UIntNormalized: DirectXPixelFormat = 83
DirectXPixelFormat_BC5IntNormalized: DirectXPixelFormat = 84
DirectXPixelFormat_B5G6R5UIntNormalized: DirectXPixelFormat = 85
DirectXPixelFormat_B5G5R5A1UIntNormalized: DirectXPixelFormat = 86
DirectXPixelFormat_B8G8R8A8UIntNormalized: DirectXPixelFormat = 87
DirectXPixelFormat_B8G8R8X8UIntNormalized: DirectXPixelFormat = 88
DirectXPixelFormat_R10G10B10XRBiasA2UIntNormalized: DirectXPixelFormat = 89
DirectXPixelFormat_B8G8R8A8Typeless: DirectXPixelFormat = 90
DirectXPixelFormat_B8G8R8A8UIntNormalizedSrgb: DirectXPixelFormat = 91
DirectXPixelFormat_B8G8R8X8Typeless: DirectXPixelFormat = 92
DirectXPixelFormat_B8G8R8X8UIntNormalizedSrgb: DirectXPixelFormat = 93
DirectXPixelFormat_BC6HTypeless: DirectXPixelFormat = 94
DirectXPixelFormat_BC6H16UnsignedFloat: DirectXPixelFormat = 95
DirectXPixelFormat_BC6H16Float: DirectXPixelFormat = 96
DirectXPixelFormat_BC7Typeless: DirectXPixelFormat = 97
DirectXPixelFormat_BC7UIntNormalized: DirectXPixelFormat = 98
DirectXPixelFormat_BC7UIntNormalizedSrgb: DirectXPixelFormat = 99
DirectXPixelFormat_Ayuv: DirectXPixelFormat = 100
DirectXPixelFormat_Y410: DirectXPixelFormat = 101
DirectXPixelFormat_Y416: DirectXPixelFormat = 102
DirectXPixelFormat_NV12: DirectXPixelFormat = 103
DirectXPixelFormat_P010: DirectXPixelFormat = 104
DirectXPixelFormat_P016: DirectXPixelFormat = 105
DirectXPixelFormat_Opaque420: DirectXPixelFormat = 106
DirectXPixelFormat_Yuy2: DirectXPixelFormat = 107
DirectXPixelFormat_Y210: DirectXPixelFormat = 108
DirectXPixelFormat_Y216: DirectXPixelFormat = 109
DirectXPixelFormat_NV11: DirectXPixelFormat = 110
DirectXPixelFormat_AI44: DirectXPixelFormat = 111
DirectXPixelFormat_IA44: DirectXPixelFormat = 112
DirectXPixelFormat_P8: DirectXPixelFormat = 113
DirectXPixelFormat_A8P8: DirectXPixelFormat = 114
DirectXPixelFormat_B4G4R4A4UIntNormalized: DirectXPixelFormat = 115
DirectXPixelFormat_P208: DirectXPixelFormat = 130
DirectXPixelFormat_V208: DirectXPixelFormat = 131
DirectXPixelFormat_V408: DirectXPixelFormat = 132
DirectXPixelFormat_SamplerFeedbackMinMipOpaque: DirectXPixelFormat = 189
DirectXPixelFormat_SamplerFeedbackMipRegionUsedOpaque: DirectXPixelFormat = 190
DirectXPrimitiveTopology = Int32
DirectXPrimitiveTopology_Undefined: DirectXPrimitiveTopology = 0
DirectXPrimitiveTopology_PointList: DirectXPrimitiveTopology = 1
DirectXPrimitiveTopology_LineList: DirectXPrimitiveTopology = 2
DirectXPrimitiveTopology_LineStrip: DirectXPrimitiveTopology = 3
DirectXPrimitiveTopology_TriangleList: DirectXPrimitiveTopology = 4
DirectXPrimitiveTopology_TriangleStrip: DirectXPrimitiveTopology = 5
