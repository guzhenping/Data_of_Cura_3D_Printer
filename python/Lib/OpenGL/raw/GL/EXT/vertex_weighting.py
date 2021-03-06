'''OpenGL extension EXT.vertex_weighting

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_vertex_weighting'
_DEPRECATED = False
GL_MODELVIEW1_STACK_DEPTH_EXT = constant.Constant( 'GL_MODELVIEW1_STACK_DEPTH_EXT', 0x8502 )
glget.addGLGetConstant( GL_MODELVIEW1_STACK_DEPTH_EXT, (1,) )
GL_MODELVIEW1_MATRIX_EXT = constant.Constant( 'GL_MODELVIEW1_MATRIX_EXT', 0x8506 )
glget.addGLGetConstant( GL_MODELVIEW1_MATRIX_EXT, (4,4) )
GL_VERTEX_WEIGHTING_EXT = constant.Constant( 'GL_VERTEX_WEIGHTING_EXT', 0x8509 )
GL_MODELVIEW1_EXT = constant.Constant( 'GL_MODELVIEW1_EXT', 0x850A )
GL_CURRENT_VERTEX_WEIGHT_EXT = constant.Constant( 'GL_CURRENT_VERTEX_WEIGHT_EXT', 0x850B )
glget.addGLGetConstant( GL_CURRENT_VERTEX_WEIGHT_EXT, (1,) )
GL_VERTEX_WEIGHT_ARRAY_EXT = constant.Constant( 'GL_VERTEX_WEIGHT_ARRAY_EXT', 0x850C )
GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT = constant.Constant( 'GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT', 0x850D )
glget.addGLGetConstant( GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT, (1,) )
GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT = constant.Constant( 'GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT', 0x850E )
glget.addGLGetConstant( GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT, (1,) )
GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT = constant.Constant( 'GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT', 0x850F )
glget.addGLGetConstant( GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT, (1,) )
GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT = constant.Constant( 'GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT', 0x8510 )
glVertexWeightfEXT = platform.createExtensionFunction( 
'glVertexWeightfEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLfloat,),
doc='glVertexWeightfEXT(GLfloat(weight)) -> None',
argNames=('weight',),
deprecated=_DEPRECATED,
)

glVertexWeightfvEXT = platform.createExtensionFunction( 
'glVertexWeightfvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLfloatArray,),
doc='glVertexWeightfvEXT(GLfloatArray(weight)) -> None',
argNames=('weight',),
deprecated=_DEPRECATED,
)

glVertexWeightPointerEXT = platform.createExtensionFunction( 
'glVertexWeightPointerEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,constants.GLenum,constants.GLsizei,ctypes.c_void_p,),
doc='glVertexWeightPointerEXT(GLsizei(size), GLenum(type), GLsizei(stride), c_void_p(pointer)) -> None',
argNames=('size','type','stride','pointer',),
deprecated=_DEPRECATED,
)


def glInitVertexWeightingEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
