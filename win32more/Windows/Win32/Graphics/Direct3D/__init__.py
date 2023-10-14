from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D
import win32more.Windows.Win32.System.Com
D3D_FL9_1_REQ_TEXTURE1D_U_DIMENSION: UInt32 = 2048
D3D_FL9_3_REQ_TEXTURE1D_U_DIMENSION: UInt32 = 4096
D3D_FL9_1_REQ_TEXTURE2D_U_OR_V_DIMENSION: UInt32 = 2048
D3D_FL9_3_REQ_TEXTURE2D_U_OR_V_DIMENSION: UInt32 = 4096
D3D_FL9_1_REQ_TEXTURECUBE_DIMENSION: UInt32 = 512
D3D_FL9_3_REQ_TEXTURECUBE_DIMENSION: UInt32 = 4096
D3D_FL9_1_REQ_TEXTURE3D_U_V_OR_W_DIMENSION: UInt32 = 256
D3D_FL9_1_DEFAULT_MAX_ANISOTROPY: UInt32 = 2
D3D_FL9_1_IA_PRIMITIVE_MAX_COUNT: UInt32 = 65535
D3D_FL9_2_IA_PRIMITIVE_MAX_COUNT: UInt32 = 1048575
D3D_FL9_1_SIMULTANEOUS_RENDER_TARGET_COUNT: UInt32 = 1
D3D_FL9_3_SIMULTANEOUS_RENDER_TARGET_COUNT: UInt32 = 4
D3D_FL9_1_MAX_TEXTURE_REPEAT: UInt32 = 128
D3D_FL9_2_MAX_TEXTURE_REPEAT: UInt32 = 2048
D3D_FL9_3_MAX_TEXTURE_REPEAT: UInt32 = 8192
D3D_SHADER_FEATURE_DOUBLES: UInt32 = 1
D3D_SHADER_FEATURE_COMPUTE_SHADERS_PLUS_RAW_AND_STRUCTURED_BUFFERS_VIA_SHADER_4_X: UInt32 = 2
D3D_SHADER_FEATURE_UAVS_AT_EVERY_STAGE: UInt32 = 4
D3D_SHADER_FEATURE_64_UAVS: UInt32 = 8
D3D_SHADER_FEATURE_MINIMUM_PRECISION: UInt32 = 16
D3D_SHADER_FEATURE_11_1_DOUBLE_EXTENSIONS: UInt32 = 32
D3D_SHADER_FEATURE_11_1_SHADER_EXTENSIONS: UInt32 = 64
D3D_SHADER_FEATURE_LEVEL_9_COMPARISON_FILTERING: UInt32 = 128
D3D_SHADER_FEATURE_TILED_RESOURCES: UInt32 = 256
D3D_SHADER_FEATURE_STENCIL_REF: UInt32 = 512
D3D_SHADER_FEATURE_INNER_COVERAGE: UInt32 = 1024
D3D_SHADER_FEATURE_TYPED_UAV_LOAD_ADDITIONAL_FORMATS: UInt32 = 2048
D3D_SHADER_FEATURE_ROVS: UInt32 = 4096
D3D_SHADER_FEATURE_VIEWPORT_AND_RT_ARRAY_INDEX_FROM_ANY_SHADER_FEEDING_RASTERIZER: UInt32 = 8192
D3D_SHADER_FEATURE_WAVE_OPS: UInt32 = 16384
D3D_SHADER_FEATURE_INT64_OPS: UInt32 = 32768
D3D_SHADER_FEATURE_VIEW_ID: UInt32 = 65536
D3D_SHADER_FEATURE_BARYCENTRICS: UInt32 = 131072
D3D_SHADER_FEATURE_NATIVE_16BIT_OPS: UInt32 = 262144
D3D_SHADER_FEATURE_SHADING_RATE: UInt32 = 524288
D3D_SHADER_FEATURE_RAYTRACING_TIER_1_1: UInt32 = 1048576
D3D_SHADER_FEATURE_SAMPLER_FEEDBACK: UInt32 = 2097152
D3D_SHADER_FEATURE_ATOMIC_INT64_ON_TYPED_RESOURCE: UInt32 = 4194304
D3D_SHADER_FEATURE_ATOMIC_INT64_ON_GROUP_SHARED: UInt32 = 8388608
D3D_SHADER_FEATURE_DERIVATIVES_IN_MESH_AND_AMPLIFICATION_SHADERS: UInt32 = 16777216
D3D_SHADER_FEATURE_RESOURCE_DESCRIPTOR_HEAP_INDEXING: UInt32 = 33554432
D3D_SHADER_FEATURE_SAMPLER_DESCRIPTOR_HEAP_INDEXING: UInt32 = 67108864
D3D_SHADER_FEATURE_WAVE_MMA: UInt32 = 134217728
D3D_SHADER_FEATURE_ATOMIC_INT64_ON_DESCRIPTOR_HEAP_RESOURCE: UInt32 = 268435456
WKPDID_D3DDebugObjectName: Guid = Guid('{429b8c22-9188-4b0c-8742-acb0bf85c200}')
WKPDID_D3DDebugObjectNameW: Guid = Guid('{4cca5fd8-921f-42c8-8566-70caf2a9b741}')
WKPDID_CommentStringW: Guid = Guid('{d0149dc0-90e8-4ec8-8144-e900ad266bb2}')
WKPDID_D3D12UniqueObjectId: Guid = Guid('{1b39de15-ec04-4bae-ba4d-8cef79fc04c1}')
D3D_COMPONENT_MASK_X: UInt32 = 1
D3D_COMPONENT_MASK_Y: UInt32 = 2
D3D_COMPONENT_MASK_Z: UInt32 = 4
D3D_COMPONENT_MASK_W: UInt32 = 8
D3D_TEXTURE_LAYOUT_ROW_MAJOR: Guid = Guid('{b5dc234f-72bb-4bec-9705-8cf258df6b6c}')
D3D_TEXTURE_LAYOUT_64KB_STANDARD_SWIZZLE: Guid = Guid('{4c0f29e3-3f5f-4d35-84c9-bc0983b62c28}')
class D3DMATRIX(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        m: Single * 16
        class _Anonymous_e__Struct(EasyCastStructure):
            _11: Single
            _12: Single
            _13: Single
            _14: Single
            _21: Single
            _22: Single
            _23: Single
            _24: Single
            _31: Single
            _32: Single
            _33: Single
            _34: Single
            _41: Single
            _42: Single
            _43: Single
            _44: Single
class D3DVECTOR(EasyCastStructure):
    x: Single
    y: Single
    z: Single
D3D_CBUFFER_TYPE = Int32
D3D_CT_CBUFFER: D3D_CBUFFER_TYPE = 0
D3D_CT_TBUFFER: D3D_CBUFFER_TYPE = 1
D3D_CT_INTERFACE_POINTERS: D3D_CBUFFER_TYPE = 2
D3D_CT_RESOURCE_BIND_INFO: D3D_CBUFFER_TYPE = 3
D3D10_CT_CBUFFER: D3D_CBUFFER_TYPE = 0
D3D10_CT_TBUFFER: D3D_CBUFFER_TYPE = 1
D3D11_CT_CBUFFER: D3D_CBUFFER_TYPE = 0
D3D11_CT_TBUFFER: D3D_CBUFFER_TYPE = 1
D3D11_CT_INTERFACE_POINTERS: D3D_CBUFFER_TYPE = 2
D3D11_CT_RESOURCE_BIND_INFO: D3D_CBUFFER_TYPE = 3
D3D_DRIVER_TYPE = Int32
D3D_DRIVER_TYPE_UNKNOWN: D3D_DRIVER_TYPE = 0
D3D_DRIVER_TYPE_HARDWARE: D3D_DRIVER_TYPE = 1
D3D_DRIVER_TYPE_REFERENCE: D3D_DRIVER_TYPE = 2
D3D_DRIVER_TYPE_NULL: D3D_DRIVER_TYPE = 3
D3D_DRIVER_TYPE_SOFTWARE: D3D_DRIVER_TYPE = 4
D3D_DRIVER_TYPE_WARP: D3D_DRIVER_TYPE = 5
D3D_FEATURE_LEVEL = Int32
D3D_FEATURE_LEVEL_1_0_CORE: D3D_FEATURE_LEVEL = 4096
D3D_FEATURE_LEVEL_9_1: D3D_FEATURE_LEVEL = 37120
D3D_FEATURE_LEVEL_9_2: D3D_FEATURE_LEVEL = 37376
D3D_FEATURE_LEVEL_9_3: D3D_FEATURE_LEVEL = 37632
D3D_FEATURE_LEVEL_10_0: D3D_FEATURE_LEVEL = 40960
D3D_FEATURE_LEVEL_10_1: D3D_FEATURE_LEVEL = 41216
D3D_FEATURE_LEVEL_11_0: D3D_FEATURE_LEVEL = 45056
D3D_FEATURE_LEVEL_11_1: D3D_FEATURE_LEVEL = 45312
D3D_FEATURE_LEVEL_12_0: D3D_FEATURE_LEVEL = 49152
D3D_FEATURE_LEVEL_12_1: D3D_FEATURE_LEVEL = 49408
D3D_FEATURE_LEVEL_12_2: D3D_FEATURE_LEVEL = 49664
D3D_FORMAT_COMPONENT_INTERPRETATION = Int32
D3DFCI_TYPELESS: D3D_FORMAT_COMPONENT_INTERPRETATION = 0
D3DFCI_FLOAT: D3D_FORMAT_COMPONENT_INTERPRETATION = -4
D3DFCI_SNORM: D3D_FORMAT_COMPONENT_INTERPRETATION = -3
D3DFCI_UNORM: D3D_FORMAT_COMPONENT_INTERPRETATION = -2
D3DFCI_SINT: D3D_FORMAT_COMPONENT_INTERPRETATION = -1
D3DFCI_UINT: D3D_FORMAT_COMPONENT_INTERPRETATION = 1
D3DFCI_UNORM_SRGB: D3D_FORMAT_COMPONENT_INTERPRETATION = 2
D3DFCI_BIASED_FIXED_2_8: D3D_FORMAT_COMPONENT_INTERPRETATION = 3
D3D_FORMAT_COMPONENT_NAME = Int32
D3DFCN_R: D3D_FORMAT_COMPONENT_NAME = -4
D3DFCN_G: D3D_FORMAT_COMPONENT_NAME = -3
D3DFCN_B: D3D_FORMAT_COMPONENT_NAME = -2
D3DFCN_A: D3D_FORMAT_COMPONENT_NAME = -1
D3DFCN_D: D3D_FORMAT_COMPONENT_NAME = 0
D3DFCN_S: D3D_FORMAT_COMPONENT_NAME = 1
D3DFCN_X: D3D_FORMAT_COMPONENT_NAME = 2
D3D_FORMAT_LAYOUT = Int32
D3DFL_STANDARD: D3D_FORMAT_LAYOUT = 0
D3DFL_CUSTOM: D3D_FORMAT_LAYOUT = -1
D3D_FORMAT_TYPE_LEVEL = Int32
D3DFTL_NO_TYPE: D3D_FORMAT_TYPE_LEVEL = 0
D3DFTL_PARTIAL_TYPE: D3D_FORMAT_TYPE_LEVEL = -2
D3DFTL_FULL_TYPE: D3D_FORMAT_TYPE_LEVEL = -1
D3D_INCLUDE_TYPE = Int32
D3D_INCLUDE_LOCAL: D3D_INCLUDE_TYPE = 0
D3D_INCLUDE_SYSTEM: D3D_INCLUDE_TYPE = 1
D3D10_INCLUDE_LOCAL: D3D_INCLUDE_TYPE = 0
D3D10_INCLUDE_SYSTEM: D3D_INCLUDE_TYPE = 1
D3D_INTERPOLATION_MODE = Int32
D3D_INTERPOLATION_UNDEFINED: D3D_INTERPOLATION_MODE = 0
D3D_INTERPOLATION_CONSTANT: D3D_INTERPOLATION_MODE = 1
D3D_INTERPOLATION_LINEAR: D3D_INTERPOLATION_MODE = 2
D3D_INTERPOLATION_LINEAR_CENTROID: D3D_INTERPOLATION_MODE = 3
D3D_INTERPOLATION_LINEAR_NOPERSPECTIVE: D3D_INTERPOLATION_MODE = 4
D3D_INTERPOLATION_LINEAR_NOPERSPECTIVE_CENTROID: D3D_INTERPOLATION_MODE = 5
D3D_INTERPOLATION_LINEAR_SAMPLE: D3D_INTERPOLATION_MODE = 6
D3D_INTERPOLATION_LINEAR_NOPERSPECTIVE_SAMPLE: D3D_INTERPOLATION_MODE = 7
D3D_MIN_PRECISION = Int32
D3D_MIN_PRECISION_DEFAULT: D3D_MIN_PRECISION = 0
D3D_MIN_PRECISION_FLOAT_16: D3D_MIN_PRECISION = 1
D3D_MIN_PRECISION_FLOAT_2_8: D3D_MIN_PRECISION = 2
D3D_MIN_PRECISION_RESERVED: D3D_MIN_PRECISION = 3
D3D_MIN_PRECISION_SINT_16: D3D_MIN_PRECISION = 4
D3D_MIN_PRECISION_UINT_16: D3D_MIN_PRECISION = 5
D3D_MIN_PRECISION_ANY_16: D3D_MIN_PRECISION = 240
D3D_MIN_PRECISION_ANY_10: D3D_MIN_PRECISION = 241
D3D_NAME = Int32
D3D_NAME_UNDEFINED: D3D_NAME = 0
D3D_NAME_POSITION: D3D_NAME = 1
D3D_NAME_CLIP_DISTANCE: D3D_NAME = 2
D3D_NAME_CULL_DISTANCE: D3D_NAME = 3
D3D_NAME_RENDER_TARGET_ARRAY_INDEX: D3D_NAME = 4
D3D_NAME_VIEWPORT_ARRAY_INDEX: D3D_NAME = 5
D3D_NAME_VERTEX_ID: D3D_NAME = 6
D3D_NAME_PRIMITIVE_ID: D3D_NAME = 7
D3D_NAME_INSTANCE_ID: D3D_NAME = 8
D3D_NAME_IS_FRONT_FACE: D3D_NAME = 9
D3D_NAME_SAMPLE_INDEX: D3D_NAME = 10
D3D_NAME_FINAL_QUAD_EDGE_TESSFACTOR: D3D_NAME = 11
D3D_NAME_FINAL_QUAD_INSIDE_TESSFACTOR: D3D_NAME = 12
D3D_NAME_FINAL_TRI_EDGE_TESSFACTOR: D3D_NAME = 13
D3D_NAME_FINAL_TRI_INSIDE_TESSFACTOR: D3D_NAME = 14
D3D_NAME_FINAL_LINE_DETAIL_TESSFACTOR: D3D_NAME = 15
D3D_NAME_FINAL_LINE_DENSITY_TESSFACTOR: D3D_NAME = 16
D3D_NAME_BARYCENTRICS: D3D_NAME = 23
D3D_NAME_SHADINGRATE: D3D_NAME = 24
D3D_NAME_CULLPRIMITIVE: D3D_NAME = 25
D3D_NAME_TARGET: D3D_NAME = 64
D3D_NAME_DEPTH: D3D_NAME = 65
D3D_NAME_COVERAGE: D3D_NAME = 66
D3D_NAME_DEPTH_GREATER_EQUAL: D3D_NAME = 67
D3D_NAME_DEPTH_LESS_EQUAL: D3D_NAME = 68
D3D_NAME_STENCIL_REF: D3D_NAME = 69
D3D_NAME_INNER_COVERAGE: D3D_NAME = 70
D3D10_NAME_UNDEFINED: D3D_NAME = 0
D3D10_NAME_POSITION: D3D_NAME = 1
D3D10_NAME_CLIP_DISTANCE: D3D_NAME = 2
D3D10_NAME_CULL_DISTANCE: D3D_NAME = 3
D3D10_NAME_RENDER_TARGET_ARRAY_INDEX: D3D_NAME = 4
D3D10_NAME_VIEWPORT_ARRAY_INDEX: D3D_NAME = 5
D3D10_NAME_VERTEX_ID: D3D_NAME = 6
D3D10_NAME_PRIMITIVE_ID: D3D_NAME = 7
D3D10_NAME_INSTANCE_ID: D3D_NAME = 8
D3D10_NAME_IS_FRONT_FACE: D3D_NAME = 9
D3D10_NAME_SAMPLE_INDEX: D3D_NAME = 10
D3D10_NAME_TARGET: D3D_NAME = 64
D3D10_NAME_DEPTH: D3D_NAME = 65
D3D10_NAME_COVERAGE: D3D_NAME = 66
D3D11_NAME_FINAL_QUAD_EDGE_TESSFACTOR: D3D_NAME = 11
D3D11_NAME_FINAL_QUAD_INSIDE_TESSFACTOR: D3D_NAME = 12
D3D11_NAME_FINAL_TRI_EDGE_TESSFACTOR: D3D_NAME = 13
D3D11_NAME_FINAL_TRI_INSIDE_TESSFACTOR: D3D_NAME = 14
D3D11_NAME_FINAL_LINE_DETAIL_TESSFACTOR: D3D_NAME = 15
D3D11_NAME_FINAL_LINE_DENSITY_TESSFACTOR: D3D_NAME = 16
D3D11_NAME_DEPTH_GREATER_EQUAL: D3D_NAME = 67
D3D11_NAME_DEPTH_LESS_EQUAL: D3D_NAME = 68
D3D11_NAME_STENCIL_REF: D3D_NAME = 69
D3D11_NAME_INNER_COVERAGE: D3D_NAME = 70
D3D12_NAME_BARYCENTRICS: D3D_NAME = 23
D3D12_NAME_SHADINGRATE: D3D_NAME = 24
D3D12_NAME_CULLPRIMITIVE: D3D_NAME = 25
D3D_PARAMETER_FLAGS = Int32
D3D_PF_NONE: D3D_PARAMETER_FLAGS = 0
D3D_PF_IN: D3D_PARAMETER_FLAGS = 1
D3D_PF_OUT: D3D_PARAMETER_FLAGS = 2
D3D_PRIMITIVE = Int32
D3D_PRIMITIVE_UNDEFINED: D3D_PRIMITIVE = 0
D3D_PRIMITIVE_POINT: D3D_PRIMITIVE = 1
D3D_PRIMITIVE_LINE: D3D_PRIMITIVE = 2
D3D_PRIMITIVE_TRIANGLE: D3D_PRIMITIVE = 3
D3D_PRIMITIVE_LINE_ADJ: D3D_PRIMITIVE = 6
D3D_PRIMITIVE_TRIANGLE_ADJ: D3D_PRIMITIVE = 7
D3D_PRIMITIVE_1_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 8
D3D_PRIMITIVE_2_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 9
D3D_PRIMITIVE_3_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 10
D3D_PRIMITIVE_4_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 11
D3D_PRIMITIVE_5_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 12
D3D_PRIMITIVE_6_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 13
D3D_PRIMITIVE_7_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 14
D3D_PRIMITIVE_8_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 15
D3D_PRIMITIVE_9_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 16
D3D_PRIMITIVE_10_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 17
D3D_PRIMITIVE_11_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 18
D3D_PRIMITIVE_12_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 19
D3D_PRIMITIVE_13_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 20
D3D_PRIMITIVE_14_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 21
D3D_PRIMITIVE_15_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 22
D3D_PRIMITIVE_16_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 23
D3D_PRIMITIVE_17_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 24
D3D_PRIMITIVE_18_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 25
D3D_PRIMITIVE_19_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 26
D3D_PRIMITIVE_20_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 27
D3D_PRIMITIVE_21_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 28
D3D_PRIMITIVE_22_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 29
D3D_PRIMITIVE_23_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 30
D3D_PRIMITIVE_24_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 31
D3D_PRIMITIVE_25_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 32
D3D_PRIMITIVE_26_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 33
D3D_PRIMITIVE_27_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 34
D3D_PRIMITIVE_28_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 35
D3D_PRIMITIVE_29_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 36
D3D_PRIMITIVE_30_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 37
D3D_PRIMITIVE_31_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 38
D3D_PRIMITIVE_32_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 39
D3D10_PRIMITIVE_UNDEFINED: D3D_PRIMITIVE = 0
D3D10_PRIMITIVE_POINT: D3D_PRIMITIVE = 1
D3D10_PRIMITIVE_LINE: D3D_PRIMITIVE = 2
D3D10_PRIMITIVE_TRIANGLE: D3D_PRIMITIVE = 3
D3D10_PRIMITIVE_LINE_ADJ: D3D_PRIMITIVE = 6
D3D10_PRIMITIVE_TRIANGLE_ADJ: D3D_PRIMITIVE = 7
D3D11_PRIMITIVE_UNDEFINED: D3D_PRIMITIVE = 0
D3D11_PRIMITIVE_POINT: D3D_PRIMITIVE = 1
D3D11_PRIMITIVE_LINE: D3D_PRIMITIVE = 2
D3D11_PRIMITIVE_TRIANGLE: D3D_PRIMITIVE = 3
D3D11_PRIMITIVE_LINE_ADJ: D3D_PRIMITIVE = 6
D3D11_PRIMITIVE_TRIANGLE_ADJ: D3D_PRIMITIVE = 7
D3D11_PRIMITIVE_1_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 8
D3D11_PRIMITIVE_2_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 9
D3D11_PRIMITIVE_3_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 10
D3D11_PRIMITIVE_4_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 11
D3D11_PRIMITIVE_5_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 12
D3D11_PRIMITIVE_6_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 13
D3D11_PRIMITIVE_7_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 14
D3D11_PRIMITIVE_8_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 15
D3D11_PRIMITIVE_9_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 16
D3D11_PRIMITIVE_10_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 17
D3D11_PRIMITIVE_11_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 18
D3D11_PRIMITIVE_12_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 19
D3D11_PRIMITIVE_13_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 20
D3D11_PRIMITIVE_14_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 21
D3D11_PRIMITIVE_15_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 22
D3D11_PRIMITIVE_16_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 23
D3D11_PRIMITIVE_17_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 24
D3D11_PRIMITIVE_18_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 25
D3D11_PRIMITIVE_19_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 26
D3D11_PRIMITIVE_20_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 27
D3D11_PRIMITIVE_21_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 28
D3D11_PRIMITIVE_22_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 29
D3D11_PRIMITIVE_23_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 30
D3D11_PRIMITIVE_24_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 31
D3D11_PRIMITIVE_25_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 32
D3D11_PRIMITIVE_26_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 33
D3D11_PRIMITIVE_27_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 34
D3D11_PRIMITIVE_28_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 35
D3D11_PRIMITIVE_29_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 36
D3D11_PRIMITIVE_30_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 37
D3D11_PRIMITIVE_31_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 38
D3D11_PRIMITIVE_32_CONTROL_POINT_PATCH: D3D_PRIMITIVE = 39
D3D_PRIMITIVE_TOPOLOGY = Int32
D3D_PRIMITIVE_TOPOLOGY_UNDEFINED: D3D_PRIMITIVE_TOPOLOGY = 0
D3D_PRIMITIVE_TOPOLOGY_POINTLIST: D3D_PRIMITIVE_TOPOLOGY = 1
D3D_PRIMITIVE_TOPOLOGY_LINELIST: D3D_PRIMITIVE_TOPOLOGY = 2
D3D_PRIMITIVE_TOPOLOGY_LINESTRIP: D3D_PRIMITIVE_TOPOLOGY = 3
D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST: D3D_PRIMITIVE_TOPOLOGY = 4
D3D_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP: D3D_PRIMITIVE_TOPOLOGY = 5
D3D_PRIMITIVE_TOPOLOGY_TRIANGLEFAN: D3D_PRIMITIVE_TOPOLOGY = 6
D3D_PRIMITIVE_TOPOLOGY_LINELIST_ADJ: D3D_PRIMITIVE_TOPOLOGY = 10
D3D_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ: D3D_PRIMITIVE_TOPOLOGY = 11
D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ: D3D_PRIMITIVE_TOPOLOGY = 12
D3D_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ: D3D_PRIMITIVE_TOPOLOGY = 13
D3D_PRIMITIVE_TOPOLOGY_1_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 33
D3D_PRIMITIVE_TOPOLOGY_2_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 34
D3D_PRIMITIVE_TOPOLOGY_3_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 35
D3D_PRIMITIVE_TOPOLOGY_4_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 36
D3D_PRIMITIVE_TOPOLOGY_5_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 37
D3D_PRIMITIVE_TOPOLOGY_6_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 38
D3D_PRIMITIVE_TOPOLOGY_7_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 39
D3D_PRIMITIVE_TOPOLOGY_8_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 40
D3D_PRIMITIVE_TOPOLOGY_9_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 41
D3D_PRIMITIVE_TOPOLOGY_10_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 42
D3D_PRIMITIVE_TOPOLOGY_11_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 43
D3D_PRIMITIVE_TOPOLOGY_12_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 44
D3D_PRIMITIVE_TOPOLOGY_13_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 45
D3D_PRIMITIVE_TOPOLOGY_14_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 46
D3D_PRIMITIVE_TOPOLOGY_15_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 47
D3D_PRIMITIVE_TOPOLOGY_16_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 48
D3D_PRIMITIVE_TOPOLOGY_17_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 49
D3D_PRIMITIVE_TOPOLOGY_18_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 50
D3D_PRIMITIVE_TOPOLOGY_19_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 51
D3D_PRIMITIVE_TOPOLOGY_20_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 52
D3D_PRIMITIVE_TOPOLOGY_21_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 53
D3D_PRIMITIVE_TOPOLOGY_22_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 54
D3D_PRIMITIVE_TOPOLOGY_23_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 55
D3D_PRIMITIVE_TOPOLOGY_24_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 56
D3D_PRIMITIVE_TOPOLOGY_25_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 57
D3D_PRIMITIVE_TOPOLOGY_26_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 58
D3D_PRIMITIVE_TOPOLOGY_27_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 59
D3D_PRIMITIVE_TOPOLOGY_28_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 60
D3D_PRIMITIVE_TOPOLOGY_29_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 61
D3D_PRIMITIVE_TOPOLOGY_30_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 62
D3D_PRIMITIVE_TOPOLOGY_31_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 63
D3D_PRIMITIVE_TOPOLOGY_32_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 64
D3D10_PRIMITIVE_TOPOLOGY_UNDEFINED: D3D_PRIMITIVE_TOPOLOGY = 0
D3D10_PRIMITIVE_TOPOLOGY_POINTLIST: D3D_PRIMITIVE_TOPOLOGY = 1
D3D10_PRIMITIVE_TOPOLOGY_LINELIST: D3D_PRIMITIVE_TOPOLOGY = 2
D3D10_PRIMITIVE_TOPOLOGY_LINESTRIP: D3D_PRIMITIVE_TOPOLOGY = 3
D3D10_PRIMITIVE_TOPOLOGY_TRIANGLELIST: D3D_PRIMITIVE_TOPOLOGY = 4
D3D10_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP: D3D_PRIMITIVE_TOPOLOGY = 5
D3D10_PRIMITIVE_TOPOLOGY_LINELIST_ADJ: D3D_PRIMITIVE_TOPOLOGY = 10
D3D10_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ: D3D_PRIMITIVE_TOPOLOGY = 11
D3D10_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ: D3D_PRIMITIVE_TOPOLOGY = 12
D3D10_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ: D3D_PRIMITIVE_TOPOLOGY = 13
D3D11_PRIMITIVE_TOPOLOGY_UNDEFINED: D3D_PRIMITIVE_TOPOLOGY = 0
D3D11_PRIMITIVE_TOPOLOGY_POINTLIST: D3D_PRIMITIVE_TOPOLOGY = 1
D3D11_PRIMITIVE_TOPOLOGY_LINELIST: D3D_PRIMITIVE_TOPOLOGY = 2
D3D11_PRIMITIVE_TOPOLOGY_LINESTRIP: D3D_PRIMITIVE_TOPOLOGY = 3
D3D11_PRIMITIVE_TOPOLOGY_TRIANGLELIST: D3D_PRIMITIVE_TOPOLOGY = 4
D3D11_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP: D3D_PRIMITIVE_TOPOLOGY = 5
D3D11_PRIMITIVE_TOPOLOGY_LINELIST_ADJ: D3D_PRIMITIVE_TOPOLOGY = 10
D3D11_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ: D3D_PRIMITIVE_TOPOLOGY = 11
D3D11_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ: D3D_PRIMITIVE_TOPOLOGY = 12
D3D11_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ: D3D_PRIMITIVE_TOPOLOGY = 13
D3D11_PRIMITIVE_TOPOLOGY_1_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 33
D3D11_PRIMITIVE_TOPOLOGY_2_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 34
D3D11_PRIMITIVE_TOPOLOGY_3_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 35
D3D11_PRIMITIVE_TOPOLOGY_4_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 36
D3D11_PRIMITIVE_TOPOLOGY_5_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 37
D3D11_PRIMITIVE_TOPOLOGY_6_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 38
D3D11_PRIMITIVE_TOPOLOGY_7_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 39
D3D11_PRIMITIVE_TOPOLOGY_8_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 40
D3D11_PRIMITIVE_TOPOLOGY_9_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 41
D3D11_PRIMITIVE_TOPOLOGY_10_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 42
D3D11_PRIMITIVE_TOPOLOGY_11_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 43
D3D11_PRIMITIVE_TOPOLOGY_12_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 44
D3D11_PRIMITIVE_TOPOLOGY_13_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 45
D3D11_PRIMITIVE_TOPOLOGY_14_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 46
D3D11_PRIMITIVE_TOPOLOGY_15_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 47
D3D11_PRIMITIVE_TOPOLOGY_16_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 48
D3D11_PRIMITIVE_TOPOLOGY_17_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 49
D3D11_PRIMITIVE_TOPOLOGY_18_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 50
D3D11_PRIMITIVE_TOPOLOGY_19_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 51
D3D11_PRIMITIVE_TOPOLOGY_20_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 52
D3D11_PRIMITIVE_TOPOLOGY_21_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 53
D3D11_PRIMITIVE_TOPOLOGY_22_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 54
D3D11_PRIMITIVE_TOPOLOGY_23_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 55
D3D11_PRIMITIVE_TOPOLOGY_24_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 56
D3D11_PRIMITIVE_TOPOLOGY_25_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 57
D3D11_PRIMITIVE_TOPOLOGY_26_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 58
D3D11_PRIMITIVE_TOPOLOGY_27_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 59
D3D11_PRIMITIVE_TOPOLOGY_28_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 60
D3D11_PRIMITIVE_TOPOLOGY_29_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 61
D3D11_PRIMITIVE_TOPOLOGY_30_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 62
D3D11_PRIMITIVE_TOPOLOGY_31_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 63
D3D11_PRIMITIVE_TOPOLOGY_32_CONTROL_POINT_PATCHLIST: D3D_PRIMITIVE_TOPOLOGY = 64
D3D_REGISTER_COMPONENT_TYPE = Int32
D3D_REGISTER_COMPONENT_UNKNOWN: D3D_REGISTER_COMPONENT_TYPE = 0
D3D_REGISTER_COMPONENT_UINT32: D3D_REGISTER_COMPONENT_TYPE = 1
D3D_REGISTER_COMPONENT_SINT32: D3D_REGISTER_COMPONENT_TYPE = 2
D3D_REGISTER_COMPONENT_FLOAT32: D3D_REGISTER_COMPONENT_TYPE = 3
D3D10_REGISTER_COMPONENT_UNKNOWN: D3D_REGISTER_COMPONENT_TYPE = 0
D3D10_REGISTER_COMPONENT_UINT32: D3D_REGISTER_COMPONENT_TYPE = 1
D3D10_REGISTER_COMPONENT_SINT32: D3D_REGISTER_COMPONENT_TYPE = 2
D3D10_REGISTER_COMPONENT_FLOAT32: D3D_REGISTER_COMPONENT_TYPE = 3
D3D_RESOURCE_RETURN_TYPE = Int32
D3D_RETURN_TYPE_UNORM: D3D_RESOURCE_RETURN_TYPE = 1
D3D_RETURN_TYPE_SNORM: D3D_RESOURCE_RETURN_TYPE = 2
D3D_RETURN_TYPE_SINT: D3D_RESOURCE_RETURN_TYPE = 3
D3D_RETURN_TYPE_UINT: D3D_RESOURCE_RETURN_TYPE = 4
D3D_RETURN_TYPE_FLOAT: D3D_RESOURCE_RETURN_TYPE = 5
D3D_RETURN_TYPE_MIXED: D3D_RESOURCE_RETURN_TYPE = 6
D3D_RETURN_TYPE_DOUBLE: D3D_RESOURCE_RETURN_TYPE = 7
D3D_RETURN_TYPE_CONTINUED: D3D_RESOURCE_RETURN_TYPE = 8
D3D10_RETURN_TYPE_UNORM: D3D_RESOURCE_RETURN_TYPE = 1
D3D10_RETURN_TYPE_SNORM: D3D_RESOURCE_RETURN_TYPE = 2
D3D10_RETURN_TYPE_SINT: D3D_RESOURCE_RETURN_TYPE = 3
D3D10_RETURN_TYPE_UINT: D3D_RESOURCE_RETURN_TYPE = 4
D3D10_RETURN_TYPE_FLOAT: D3D_RESOURCE_RETURN_TYPE = 5
D3D10_RETURN_TYPE_MIXED: D3D_RESOURCE_RETURN_TYPE = 6
D3D11_RETURN_TYPE_UNORM: D3D_RESOURCE_RETURN_TYPE = 1
D3D11_RETURN_TYPE_SNORM: D3D_RESOURCE_RETURN_TYPE = 2
D3D11_RETURN_TYPE_SINT: D3D_RESOURCE_RETURN_TYPE = 3
D3D11_RETURN_TYPE_UINT: D3D_RESOURCE_RETURN_TYPE = 4
D3D11_RETURN_TYPE_FLOAT: D3D_RESOURCE_RETURN_TYPE = 5
D3D11_RETURN_TYPE_MIXED: D3D_RESOURCE_RETURN_TYPE = 6
D3D11_RETURN_TYPE_DOUBLE: D3D_RESOURCE_RETURN_TYPE = 7
D3D11_RETURN_TYPE_CONTINUED: D3D_RESOURCE_RETURN_TYPE = 8
D3D_SHADER_CBUFFER_FLAGS = Int32
D3D_CBF_USERPACKED: D3D_SHADER_CBUFFER_FLAGS = 1
D3D10_CBF_USERPACKED: D3D_SHADER_CBUFFER_FLAGS = 1
D3D_SHADER_INPUT_FLAGS = Int32
D3D_SIF_USERPACKED: D3D_SHADER_INPUT_FLAGS = 1
D3D_SIF_COMPARISON_SAMPLER: D3D_SHADER_INPUT_FLAGS = 2
D3D_SIF_TEXTURE_COMPONENT_0: D3D_SHADER_INPUT_FLAGS = 4
D3D_SIF_TEXTURE_COMPONENT_1: D3D_SHADER_INPUT_FLAGS = 8
D3D_SIF_TEXTURE_COMPONENTS: D3D_SHADER_INPUT_FLAGS = 12
D3D_SIF_UNUSED: D3D_SHADER_INPUT_FLAGS = 16
D3D10_SIF_USERPACKED: D3D_SHADER_INPUT_FLAGS = 1
D3D10_SIF_COMPARISON_SAMPLER: D3D_SHADER_INPUT_FLAGS = 2
D3D10_SIF_TEXTURE_COMPONENT_0: D3D_SHADER_INPUT_FLAGS = 4
D3D10_SIF_TEXTURE_COMPONENT_1: D3D_SHADER_INPUT_FLAGS = 8
D3D10_SIF_TEXTURE_COMPONENTS: D3D_SHADER_INPUT_FLAGS = 12
D3D_SHADER_INPUT_TYPE = Int32
D3D_SIT_CBUFFER: D3D_SHADER_INPUT_TYPE = 0
D3D_SIT_TBUFFER: D3D_SHADER_INPUT_TYPE = 1
D3D_SIT_TEXTURE: D3D_SHADER_INPUT_TYPE = 2
D3D_SIT_SAMPLER: D3D_SHADER_INPUT_TYPE = 3
D3D_SIT_UAV_RWTYPED: D3D_SHADER_INPUT_TYPE = 4
D3D_SIT_STRUCTURED: D3D_SHADER_INPUT_TYPE = 5
D3D_SIT_UAV_RWSTRUCTURED: D3D_SHADER_INPUT_TYPE = 6
D3D_SIT_BYTEADDRESS: D3D_SHADER_INPUT_TYPE = 7
D3D_SIT_UAV_RWBYTEADDRESS: D3D_SHADER_INPUT_TYPE = 8
D3D_SIT_UAV_APPEND_STRUCTURED: D3D_SHADER_INPUT_TYPE = 9
D3D_SIT_UAV_CONSUME_STRUCTURED: D3D_SHADER_INPUT_TYPE = 10
D3D_SIT_UAV_RWSTRUCTURED_WITH_COUNTER: D3D_SHADER_INPUT_TYPE = 11
D3D_SIT_RTACCELERATIONSTRUCTURE: D3D_SHADER_INPUT_TYPE = 12
D3D_SIT_UAV_FEEDBACKTEXTURE: D3D_SHADER_INPUT_TYPE = 13
D3D10_SIT_CBUFFER: D3D_SHADER_INPUT_TYPE = 0
D3D10_SIT_TBUFFER: D3D_SHADER_INPUT_TYPE = 1
D3D10_SIT_TEXTURE: D3D_SHADER_INPUT_TYPE = 2
D3D10_SIT_SAMPLER: D3D_SHADER_INPUT_TYPE = 3
D3D11_SIT_UAV_RWTYPED: D3D_SHADER_INPUT_TYPE = 4
D3D11_SIT_STRUCTURED: D3D_SHADER_INPUT_TYPE = 5
D3D11_SIT_UAV_RWSTRUCTURED: D3D_SHADER_INPUT_TYPE = 6
D3D11_SIT_BYTEADDRESS: D3D_SHADER_INPUT_TYPE = 7
D3D11_SIT_UAV_RWBYTEADDRESS: D3D_SHADER_INPUT_TYPE = 8
D3D11_SIT_UAV_APPEND_STRUCTURED: D3D_SHADER_INPUT_TYPE = 9
D3D11_SIT_UAV_CONSUME_STRUCTURED: D3D_SHADER_INPUT_TYPE = 10
D3D11_SIT_UAV_RWSTRUCTURED_WITH_COUNTER: D3D_SHADER_INPUT_TYPE = 11
class D3D_SHADER_MACRO(EasyCastStructure):
    Name: win32more.Windows.Win32.Foundation.PSTR
    Definition: win32more.Windows.Win32.Foundation.PSTR
D3D_SHADER_VARIABLE_CLASS = Int32
D3D_SVC_SCALAR: D3D_SHADER_VARIABLE_CLASS = 0
D3D_SVC_VECTOR: D3D_SHADER_VARIABLE_CLASS = 1
D3D_SVC_MATRIX_ROWS: D3D_SHADER_VARIABLE_CLASS = 2
D3D_SVC_MATRIX_COLUMNS: D3D_SHADER_VARIABLE_CLASS = 3
D3D_SVC_OBJECT: D3D_SHADER_VARIABLE_CLASS = 4
D3D_SVC_STRUCT: D3D_SHADER_VARIABLE_CLASS = 5
D3D_SVC_INTERFACE_CLASS: D3D_SHADER_VARIABLE_CLASS = 6
D3D_SVC_INTERFACE_POINTER: D3D_SHADER_VARIABLE_CLASS = 7
D3D10_SVC_SCALAR: D3D_SHADER_VARIABLE_CLASS = 0
D3D10_SVC_VECTOR: D3D_SHADER_VARIABLE_CLASS = 1
D3D10_SVC_MATRIX_ROWS: D3D_SHADER_VARIABLE_CLASS = 2
D3D10_SVC_MATRIX_COLUMNS: D3D_SHADER_VARIABLE_CLASS = 3
D3D10_SVC_OBJECT: D3D_SHADER_VARIABLE_CLASS = 4
D3D10_SVC_STRUCT: D3D_SHADER_VARIABLE_CLASS = 5
D3D11_SVC_INTERFACE_CLASS: D3D_SHADER_VARIABLE_CLASS = 6
D3D11_SVC_INTERFACE_POINTER: D3D_SHADER_VARIABLE_CLASS = 7
D3D_SHADER_VARIABLE_FLAGS = Int32
D3D_SVF_USERPACKED: D3D_SHADER_VARIABLE_FLAGS = 1
D3D_SVF_USED: D3D_SHADER_VARIABLE_FLAGS = 2
D3D_SVF_INTERFACE_POINTER: D3D_SHADER_VARIABLE_FLAGS = 4
D3D_SVF_INTERFACE_PARAMETER: D3D_SHADER_VARIABLE_FLAGS = 8
D3D10_SVF_USERPACKED: D3D_SHADER_VARIABLE_FLAGS = 1
D3D10_SVF_USED: D3D_SHADER_VARIABLE_FLAGS = 2
D3D11_SVF_INTERFACE_POINTER: D3D_SHADER_VARIABLE_FLAGS = 4
D3D11_SVF_INTERFACE_PARAMETER: D3D_SHADER_VARIABLE_FLAGS = 8
D3D_SHADER_VARIABLE_TYPE = Int32
D3D_SVT_VOID: D3D_SHADER_VARIABLE_TYPE = 0
D3D_SVT_BOOL: D3D_SHADER_VARIABLE_TYPE = 1
D3D_SVT_INT: D3D_SHADER_VARIABLE_TYPE = 2
D3D_SVT_FLOAT: D3D_SHADER_VARIABLE_TYPE = 3
D3D_SVT_STRING: D3D_SHADER_VARIABLE_TYPE = 4
D3D_SVT_TEXTURE: D3D_SHADER_VARIABLE_TYPE = 5
D3D_SVT_TEXTURE1D: D3D_SHADER_VARIABLE_TYPE = 6
D3D_SVT_TEXTURE2D: D3D_SHADER_VARIABLE_TYPE = 7
D3D_SVT_TEXTURE3D: D3D_SHADER_VARIABLE_TYPE = 8
D3D_SVT_TEXTURECUBE: D3D_SHADER_VARIABLE_TYPE = 9
D3D_SVT_SAMPLER: D3D_SHADER_VARIABLE_TYPE = 10
D3D_SVT_SAMPLER1D: D3D_SHADER_VARIABLE_TYPE = 11
D3D_SVT_SAMPLER2D: D3D_SHADER_VARIABLE_TYPE = 12
D3D_SVT_SAMPLER3D: D3D_SHADER_VARIABLE_TYPE = 13
D3D_SVT_SAMPLERCUBE: D3D_SHADER_VARIABLE_TYPE = 14
D3D_SVT_PIXELSHADER: D3D_SHADER_VARIABLE_TYPE = 15
D3D_SVT_VERTEXSHADER: D3D_SHADER_VARIABLE_TYPE = 16
D3D_SVT_PIXELFRAGMENT: D3D_SHADER_VARIABLE_TYPE = 17
D3D_SVT_VERTEXFRAGMENT: D3D_SHADER_VARIABLE_TYPE = 18
D3D_SVT_UINT: D3D_SHADER_VARIABLE_TYPE = 19
D3D_SVT_UINT8: D3D_SHADER_VARIABLE_TYPE = 20
D3D_SVT_GEOMETRYSHADER: D3D_SHADER_VARIABLE_TYPE = 21
D3D_SVT_RASTERIZER: D3D_SHADER_VARIABLE_TYPE = 22
D3D_SVT_DEPTHSTENCIL: D3D_SHADER_VARIABLE_TYPE = 23
D3D_SVT_BLEND: D3D_SHADER_VARIABLE_TYPE = 24
D3D_SVT_BUFFER: D3D_SHADER_VARIABLE_TYPE = 25
D3D_SVT_CBUFFER: D3D_SHADER_VARIABLE_TYPE = 26
D3D_SVT_TBUFFER: D3D_SHADER_VARIABLE_TYPE = 27
D3D_SVT_TEXTURE1DARRAY: D3D_SHADER_VARIABLE_TYPE = 28
D3D_SVT_TEXTURE2DARRAY: D3D_SHADER_VARIABLE_TYPE = 29
D3D_SVT_RENDERTARGETVIEW: D3D_SHADER_VARIABLE_TYPE = 30
D3D_SVT_DEPTHSTENCILVIEW: D3D_SHADER_VARIABLE_TYPE = 31
D3D_SVT_TEXTURE2DMS: D3D_SHADER_VARIABLE_TYPE = 32
D3D_SVT_TEXTURE2DMSARRAY: D3D_SHADER_VARIABLE_TYPE = 33
D3D_SVT_TEXTURECUBEARRAY: D3D_SHADER_VARIABLE_TYPE = 34
D3D_SVT_HULLSHADER: D3D_SHADER_VARIABLE_TYPE = 35
D3D_SVT_DOMAINSHADER: D3D_SHADER_VARIABLE_TYPE = 36
D3D_SVT_INTERFACE_POINTER: D3D_SHADER_VARIABLE_TYPE = 37
D3D_SVT_COMPUTESHADER: D3D_SHADER_VARIABLE_TYPE = 38
D3D_SVT_DOUBLE: D3D_SHADER_VARIABLE_TYPE = 39
D3D_SVT_RWTEXTURE1D: D3D_SHADER_VARIABLE_TYPE = 40
D3D_SVT_RWTEXTURE1DARRAY: D3D_SHADER_VARIABLE_TYPE = 41
D3D_SVT_RWTEXTURE2D: D3D_SHADER_VARIABLE_TYPE = 42
D3D_SVT_RWTEXTURE2DARRAY: D3D_SHADER_VARIABLE_TYPE = 43
D3D_SVT_RWTEXTURE3D: D3D_SHADER_VARIABLE_TYPE = 44
D3D_SVT_RWBUFFER: D3D_SHADER_VARIABLE_TYPE = 45
D3D_SVT_BYTEADDRESS_BUFFER: D3D_SHADER_VARIABLE_TYPE = 46
D3D_SVT_RWBYTEADDRESS_BUFFER: D3D_SHADER_VARIABLE_TYPE = 47
D3D_SVT_STRUCTURED_BUFFER: D3D_SHADER_VARIABLE_TYPE = 48
D3D_SVT_RWSTRUCTURED_BUFFER: D3D_SHADER_VARIABLE_TYPE = 49
D3D_SVT_APPEND_STRUCTURED_BUFFER: D3D_SHADER_VARIABLE_TYPE = 50
D3D_SVT_CONSUME_STRUCTURED_BUFFER: D3D_SHADER_VARIABLE_TYPE = 51
D3D_SVT_MIN8FLOAT: D3D_SHADER_VARIABLE_TYPE = 52
D3D_SVT_MIN10FLOAT: D3D_SHADER_VARIABLE_TYPE = 53
D3D_SVT_MIN16FLOAT: D3D_SHADER_VARIABLE_TYPE = 54
D3D_SVT_MIN12INT: D3D_SHADER_VARIABLE_TYPE = 55
D3D_SVT_MIN16INT: D3D_SHADER_VARIABLE_TYPE = 56
D3D_SVT_MIN16UINT: D3D_SHADER_VARIABLE_TYPE = 57
D3D_SVT_INT16: D3D_SHADER_VARIABLE_TYPE = 58
D3D_SVT_UINT16: D3D_SHADER_VARIABLE_TYPE = 59
D3D_SVT_FLOAT16: D3D_SHADER_VARIABLE_TYPE = 60
D3D_SVT_INT64: D3D_SHADER_VARIABLE_TYPE = 61
D3D_SVT_UINT64: D3D_SHADER_VARIABLE_TYPE = 62
D3D10_SVT_VOID: D3D_SHADER_VARIABLE_TYPE = 0
D3D10_SVT_BOOL: D3D_SHADER_VARIABLE_TYPE = 1
D3D10_SVT_INT: D3D_SHADER_VARIABLE_TYPE = 2
D3D10_SVT_FLOAT: D3D_SHADER_VARIABLE_TYPE = 3
D3D10_SVT_STRING: D3D_SHADER_VARIABLE_TYPE = 4
D3D10_SVT_TEXTURE: D3D_SHADER_VARIABLE_TYPE = 5
D3D10_SVT_TEXTURE1D: D3D_SHADER_VARIABLE_TYPE = 6
D3D10_SVT_TEXTURE2D: D3D_SHADER_VARIABLE_TYPE = 7
D3D10_SVT_TEXTURE3D: D3D_SHADER_VARIABLE_TYPE = 8
D3D10_SVT_TEXTURECUBE: D3D_SHADER_VARIABLE_TYPE = 9
D3D10_SVT_SAMPLER: D3D_SHADER_VARIABLE_TYPE = 10
D3D10_SVT_SAMPLER1D: D3D_SHADER_VARIABLE_TYPE = 11
D3D10_SVT_SAMPLER2D: D3D_SHADER_VARIABLE_TYPE = 12
D3D10_SVT_SAMPLER3D: D3D_SHADER_VARIABLE_TYPE = 13
D3D10_SVT_SAMPLERCUBE: D3D_SHADER_VARIABLE_TYPE = 14
D3D10_SVT_PIXELSHADER: D3D_SHADER_VARIABLE_TYPE = 15
D3D10_SVT_VERTEXSHADER: D3D_SHADER_VARIABLE_TYPE = 16
D3D10_SVT_PIXELFRAGMENT: D3D_SHADER_VARIABLE_TYPE = 17
D3D10_SVT_VERTEXFRAGMENT: D3D_SHADER_VARIABLE_TYPE = 18
D3D10_SVT_UINT: D3D_SHADER_VARIABLE_TYPE = 19
D3D10_SVT_UINT8: D3D_SHADER_VARIABLE_TYPE = 20
D3D10_SVT_GEOMETRYSHADER: D3D_SHADER_VARIABLE_TYPE = 21
D3D10_SVT_RASTERIZER: D3D_SHADER_VARIABLE_TYPE = 22
D3D10_SVT_DEPTHSTENCIL: D3D_SHADER_VARIABLE_TYPE = 23
D3D10_SVT_BLEND: D3D_SHADER_VARIABLE_TYPE = 24
D3D10_SVT_BUFFER: D3D_SHADER_VARIABLE_TYPE = 25
D3D10_SVT_CBUFFER: D3D_SHADER_VARIABLE_TYPE = 26
D3D10_SVT_TBUFFER: D3D_SHADER_VARIABLE_TYPE = 27
D3D10_SVT_TEXTURE1DARRAY: D3D_SHADER_VARIABLE_TYPE = 28
D3D10_SVT_TEXTURE2DARRAY: D3D_SHADER_VARIABLE_TYPE = 29
D3D10_SVT_RENDERTARGETVIEW: D3D_SHADER_VARIABLE_TYPE = 30
D3D10_SVT_DEPTHSTENCILVIEW: D3D_SHADER_VARIABLE_TYPE = 31
D3D10_SVT_TEXTURE2DMS: D3D_SHADER_VARIABLE_TYPE = 32
D3D10_SVT_TEXTURE2DMSARRAY: D3D_SHADER_VARIABLE_TYPE = 33
D3D10_SVT_TEXTURECUBEARRAY: D3D_SHADER_VARIABLE_TYPE = 34
D3D11_SVT_HULLSHADER: D3D_SHADER_VARIABLE_TYPE = 35
D3D11_SVT_DOMAINSHADER: D3D_SHADER_VARIABLE_TYPE = 36
D3D11_SVT_INTERFACE_POINTER: D3D_SHADER_VARIABLE_TYPE = 37
D3D11_SVT_COMPUTESHADER: D3D_SHADER_VARIABLE_TYPE = 38
D3D11_SVT_DOUBLE: D3D_SHADER_VARIABLE_TYPE = 39
D3D11_SVT_RWTEXTURE1D: D3D_SHADER_VARIABLE_TYPE = 40
D3D11_SVT_RWTEXTURE1DARRAY: D3D_SHADER_VARIABLE_TYPE = 41
D3D11_SVT_RWTEXTURE2D: D3D_SHADER_VARIABLE_TYPE = 42
D3D11_SVT_RWTEXTURE2DARRAY: D3D_SHADER_VARIABLE_TYPE = 43
D3D11_SVT_RWTEXTURE3D: D3D_SHADER_VARIABLE_TYPE = 44
D3D11_SVT_RWBUFFER: D3D_SHADER_VARIABLE_TYPE = 45
D3D11_SVT_BYTEADDRESS_BUFFER: D3D_SHADER_VARIABLE_TYPE = 46
D3D11_SVT_RWBYTEADDRESS_BUFFER: D3D_SHADER_VARIABLE_TYPE = 47
D3D11_SVT_STRUCTURED_BUFFER: D3D_SHADER_VARIABLE_TYPE = 48
D3D11_SVT_RWSTRUCTURED_BUFFER: D3D_SHADER_VARIABLE_TYPE = 49
D3D11_SVT_APPEND_STRUCTURED_BUFFER: D3D_SHADER_VARIABLE_TYPE = 50
D3D11_SVT_CONSUME_STRUCTURED_BUFFER: D3D_SHADER_VARIABLE_TYPE = 51
D3D_SRV_DIMENSION = Int32
D3D_SRV_DIMENSION_UNKNOWN: D3D_SRV_DIMENSION = 0
D3D_SRV_DIMENSION_BUFFER: D3D_SRV_DIMENSION = 1
D3D_SRV_DIMENSION_TEXTURE1D: D3D_SRV_DIMENSION = 2
D3D_SRV_DIMENSION_TEXTURE1DARRAY: D3D_SRV_DIMENSION = 3
D3D_SRV_DIMENSION_TEXTURE2D: D3D_SRV_DIMENSION = 4
D3D_SRV_DIMENSION_TEXTURE2DARRAY: D3D_SRV_DIMENSION = 5
D3D_SRV_DIMENSION_TEXTURE2DMS: D3D_SRV_DIMENSION = 6
D3D_SRV_DIMENSION_TEXTURE2DMSARRAY: D3D_SRV_DIMENSION = 7
D3D_SRV_DIMENSION_TEXTURE3D: D3D_SRV_DIMENSION = 8
D3D_SRV_DIMENSION_TEXTURECUBE: D3D_SRV_DIMENSION = 9
D3D_SRV_DIMENSION_TEXTURECUBEARRAY: D3D_SRV_DIMENSION = 10
D3D_SRV_DIMENSION_BUFFEREX: D3D_SRV_DIMENSION = 11
D3D10_SRV_DIMENSION_UNKNOWN: D3D_SRV_DIMENSION = 0
D3D10_SRV_DIMENSION_BUFFER: D3D_SRV_DIMENSION = 1
D3D10_SRV_DIMENSION_TEXTURE1D: D3D_SRV_DIMENSION = 2
D3D10_SRV_DIMENSION_TEXTURE1DARRAY: D3D_SRV_DIMENSION = 3
D3D10_SRV_DIMENSION_TEXTURE2D: D3D_SRV_DIMENSION = 4
D3D10_SRV_DIMENSION_TEXTURE2DARRAY: D3D_SRV_DIMENSION = 5
D3D10_SRV_DIMENSION_TEXTURE2DMS: D3D_SRV_DIMENSION = 6
D3D10_SRV_DIMENSION_TEXTURE2DMSARRAY: D3D_SRV_DIMENSION = 7
D3D10_SRV_DIMENSION_TEXTURE3D: D3D_SRV_DIMENSION = 8
D3D10_SRV_DIMENSION_TEXTURECUBE: D3D_SRV_DIMENSION = 9
D3D10_1_SRV_DIMENSION_UNKNOWN: D3D_SRV_DIMENSION = 0
D3D10_1_SRV_DIMENSION_BUFFER: D3D_SRV_DIMENSION = 1
D3D10_1_SRV_DIMENSION_TEXTURE1D: D3D_SRV_DIMENSION = 2
D3D10_1_SRV_DIMENSION_TEXTURE1DARRAY: D3D_SRV_DIMENSION = 3
D3D10_1_SRV_DIMENSION_TEXTURE2D: D3D_SRV_DIMENSION = 4
D3D10_1_SRV_DIMENSION_TEXTURE2DARRAY: D3D_SRV_DIMENSION = 5
D3D10_1_SRV_DIMENSION_TEXTURE2DMS: D3D_SRV_DIMENSION = 6
D3D10_1_SRV_DIMENSION_TEXTURE2DMSARRAY: D3D_SRV_DIMENSION = 7
D3D10_1_SRV_DIMENSION_TEXTURE3D: D3D_SRV_DIMENSION = 8
D3D10_1_SRV_DIMENSION_TEXTURECUBE: D3D_SRV_DIMENSION = 9
D3D10_1_SRV_DIMENSION_TEXTURECUBEARRAY: D3D_SRV_DIMENSION = 10
D3D11_SRV_DIMENSION_UNKNOWN: D3D_SRV_DIMENSION = 0
D3D11_SRV_DIMENSION_BUFFER: D3D_SRV_DIMENSION = 1
D3D11_SRV_DIMENSION_TEXTURE1D: D3D_SRV_DIMENSION = 2
D3D11_SRV_DIMENSION_TEXTURE1DARRAY: D3D_SRV_DIMENSION = 3
D3D11_SRV_DIMENSION_TEXTURE2D: D3D_SRV_DIMENSION = 4
D3D11_SRV_DIMENSION_TEXTURE2DARRAY: D3D_SRV_DIMENSION = 5
D3D11_SRV_DIMENSION_TEXTURE2DMS: D3D_SRV_DIMENSION = 6
D3D11_SRV_DIMENSION_TEXTURE2DMSARRAY: D3D_SRV_DIMENSION = 7
D3D11_SRV_DIMENSION_TEXTURE3D: D3D_SRV_DIMENSION = 8
D3D11_SRV_DIMENSION_TEXTURECUBE: D3D_SRV_DIMENSION = 9
D3D11_SRV_DIMENSION_TEXTURECUBEARRAY: D3D_SRV_DIMENSION = 10
D3D11_SRV_DIMENSION_BUFFEREX: D3D_SRV_DIMENSION = 11
D3D_TESSELLATOR_DOMAIN = Int32
D3D_TESSELLATOR_DOMAIN_UNDEFINED: D3D_TESSELLATOR_DOMAIN = 0
D3D_TESSELLATOR_DOMAIN_ISOLINE: D3D_TESSELLATOR_DOMAIN = 1
D3D_TESSELLATOR_DOMAIN_TRI: D3D_TESSELLATOR_DOMAIN = 2
D3D_TESSELLATOR_DOMAIN_QUAD: D3D_TESSELLATOR_DOMAIN = 3
D3D11_TESSELLATOR_DOMAIN_UNDEFINED: D3D_TESSELLATOR_DOMAIN = 0
D3D11_TESSELLATOR_DOMAIN_ISOLINE: D3D_TESSELLATOR_DOMAIN = 1
D3D11_TESSELLATOR_DOMAIN_TRI: D3D_TESSELLATOR_DOMAIN = 2
D3D11_TESSELLATOR_DOMAIN_QUAD: D3D_TESSELLATOR_DOMAIN = 3
D3D_TESSELLATOR_OUTPUT_PRIMITIVE = Int32
D3D_TESSELLATOR_OUTPUT_UNDEFINED: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 0
D3D_TESSELLATOR_OUTPUT_POINT: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 1
D3D_TESSELLATOR_OUTPUT_LINE: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 2
D3D_TESSELLATOR_OUTPUT_TRIANGLE_CW: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 3
D3D_TESSELLATOR_OUTPUT_TRIANGLE_CCW: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 4
D3D11_TESSELLATOR_OUTPUT_UNDEFINED: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 0
D3D11_TESSELLATOR_OUTPUT_POINT: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 1
D3D11_TESSELLATOR_OUTPUT_LINE: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 2
D3D11_TESSELLATOR_OUTPUT_TRIANGLE_CW: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 3
D3D11_TESSELLATOR_OUTPUT_TRIANGLE_CCW: D3D_TESSELLATOR_OUTPUT_PRIMITIVE = 4
D3D_TESSELLATOR_PARTITIONING = Int32
D3D_TESSELLATOR_PARTITIONING_UNDEFINED: D3D_TESSELLATOR_PARTITIONING = 0
D3D_TESSELLATOR_PARTITIONING_INTEGER: D3D_TESSELLATOR_PARTITIONING = 1
D3D_TESSELLATOR_PARTITIONING_POW2: D3D_TESSELLATOR_PARTITIONING = 2
D3D_TESSELLATOR_PARTITIONING_FRACTIONAL_ODD: D3D_TESSELLATOR_PARTITIONING = 3
D3D_TESSELLATOR_PARTITIONING_FRACTIONAL_EVEN: D3D_TESSELLATOR_PARTITIONING = 4
D3D11_TESSELLATOR_PARTITIONING_UNDEFINED: D3D_TESSELLATOR_PARTITIONING = 0
D3D11_TESSELLATOR_PARTITIONING_INTEGER: D3D_TESSELLATOR_PARTITIONING = 1
D3D11_TESSELLATOR_PARTITIONING_POW2: D3D_TESSELLATOR_PARTITIONING = 2
D3D11_TESSELLATOR_PARTITIONING_FRACTIONAL_ODD: D3D_TESSELLATOR_PARTITIONING = 3
D3D11_TESSELLATOR_PARTITIONING_FRACTIONAL_EVEN: D3D_TESSELLATOR_PARTITIONING = 4
class ID3DBlob(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8ba5fb08-5195-40e2-ac58-0d989c3a0102}')
    @commethod(3)
    def GetBufferPointer(self) -> VoidPtr: ...
    @commethod(4)
    def GetBufferSize(self) -> UIntPtr: ...
class ID3DDestructionNotifier(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a06eb39a-50da-425b-8c31-4eecd6c270f3}')
    @commethod(3)
    def RegisterDestructionCallback(self, callbackFn: win32more.Windows.Win32.Graphics.Direct3D.PFN_DESTRUCTION_CALLBACK, pData: VoidPtr, pCallbackID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterDestructionCallback(self, callbackID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ID3DInclude(ComPtr):
    extends: None
    @commethod(0)
    def Open(self, IncludeType: win32more.Windows.Win32.Graphics.Direct3D.D3D_INCLUDE_TYPE, pFileName: win32more.Windows.Win32.Foundation.PSTR, pParentData: VoidPtr, ppData: POINTER(VoidPtr), pBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(1)
    def Close(self, pData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_DESTRUCTION_CALLBACK(pData: VoidPtr) -> Void: ...
make_ready(__name__)
