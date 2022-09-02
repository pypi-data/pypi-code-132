
# Autogenerated by mlir-tblgen; don't manually edit.

from ._ods_common import _cext as _ods_cext
from ._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _hwarith_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


@_ods_cext.register_dialect
class _Dialect(_ods_ir.Dialect):
  DIALECT_NAMESPACE = "hwarith"
  pass


@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class AddOp(_ods_ir.OpView):
  OPERATION_NAME = "hwarith.add"

  _ODS_REGIONS = (0, True)

  def __init__(self, inputs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(inputs))
    _ods_context = _ods_get_default_loc_context(loc)
    results = _ods_ir.InferTypeOpInterface(AddOp).inferReturnTypes(
        operands=operands,
        attributes=_ods_ir.DictAttr.get(attributes, context=_ods_context),
        context=_ods_context,
        loc=loc)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inputs(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ConstantOp(_ods_ir.OpView):
  OPERATION_NAME = "hwarith.constant"

  _ODS_REGIONS = (0, True)

  def __init__(self, rawValue, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    attributes["rawValue"] = rawValue
    _ods_result_type_source_attr = attributes["rawValue"]
    _ods_derived_result_type = (
        _ods_ir.TypeAttr(_ods_result_type_source_attr).value
        if _ods_ir.TypeAttr.isinstance(_ods_result_type_source_attr) else
        _ods_result_type_source_attr.type)
    results.extend([_ods_derived_result_type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def rawValue(self):
    return _ods_ir.IntegerAttr(self.operation.attributes["rawValue"])

  @rawValue.setter
  def rawValue(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["rawValue"] = value

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class DivOp(_ods_ir.OpView):
  OPERATION_NAME = "hwarith.div"

  _ODS_REGIONS = (0, True)

  def __init__(self, inputs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(inputs))
    _ods_context = _ods_get_default_loc_context(loc)
    results = _ods_ir.InferTypeOpInterface(DivOp).inferReturnTypes(
        operands=operands,
        attributes=_ods_ir.DictAttr.get(attributes, context=_ods_context),
        context=_ods_context,
        loc=loc)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inputs(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CastOp(_ods_ir.OpView):
  OPERATION_NAME = "hwarith.cast"

  _ODS_REGIONS = (0, True)

  def __init__(self, out, in_, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(in_))
    results.append(out)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def in_(self):
    return self.operation.operands[0]

  @builtins.property
  def out(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ICmpOp(_ods_ir.OpView):
  OPERATION_NAME = "hwarith.icmp"

  _ODS_REGIONS = (0, True)

  def __init__(self, predicate, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    attributes["predicate"] = predicate
    _ods_context = _ods_get_default_loc_context(loc)
    results = _ods_ir.InferTypeOpInterface(ICmpOp).inferReturnTypes(
        operands=operands,
        attributes=_ods_ir.DictAttr.get(attributes, context=_ods_context),
        context=_ods_context,
        loc=loc)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MulOp(_ods_ir.OpView):
  OPERATION_NAME = "hwarith.mul"

  _ODS_REGIONS = (0, True)

  def __init__(self, inputs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(inputs))
    _ods_context = _ods_get_default_loc_context(loc)
    results = _ods_ir.InferTypeOpInterface(MulOp).inferReturnTypes(
        operands=operands,
        attributes=_ods_ir.DictAttr.get(attributes, context=_ods_context),
        context=_ods_context,
        loc=loc)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inputs(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SubOp(_ods_ir.OpView):
  OPERATION_NAME = "hwarith.sub"

  _ODS_REGIONS = (0, True)

  def __init__(self, inputs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(inputs))
    _ods_context = _ods_get_default_loc_context(loc)
    results = _ods_ir.InferTypeOpInterface(SubOp).inferReturnTypes(
        operands=operands,
        attributes=_ods_ir.DictAttr.get(attributes, context=_ods_context),
        context=_ods_context,
        loc=loc)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inputs(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def result(self):
    return self.operation.results[0]
