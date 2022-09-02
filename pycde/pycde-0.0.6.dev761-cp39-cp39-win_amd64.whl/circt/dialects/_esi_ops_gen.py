
# Autogenerated by mlir-tblgen; don't manually edit.

from ._ods_common import _cext as _ods_cext
from ._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _esi_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


@_ods_cext.register_dialect
class _Dialect(_ods_ir.Dialect):
  DIALECT_NAMESPACE = "esi"
  pass


@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CapnpDecodeOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.decode.capnp"

  _ODS_REGIONS = (0, True)

  def __init__(self, decodedData, clk, valid, capnpBits, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(clk))
    operands.append(_get_op_result_or_value(valid))
    operands.append(_get_op_result_or_value(capnpBits))
    results.append(decodedData)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def clk(self):
    return self.operation.operands[0]

  @builtins.property
  def valid(self):
    return self.operation.operands[1]

  @builtins.property
  def capnpBits(self):
    return self.operation.operands[2]

  @builtins.property
  def decodedData(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CapnpEncodeOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.encode.capnp"

  _ODS_REGIONS = (0, True)

  def __init__(self, capnpBits, clk, valid, dataToEncode, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(clk))
    operands.append(_get_op_result_or_value(valid))
    operands.append(_get_op_result_or_value(dataToEncode))
    results.append(capnpBits)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def clk(self):
    return self.operation.operands[0]

  @builtins.property
  def valid(self):
    return self.operation.operands[1]

  @builtins.property
  def dataToEncode(self):
    return self.operation.operands[2]

  @builtins.property
  def capnpBits(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ChannelBufferOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.buffer"

  _ODS_REGIONS = (0, True)

  def __init__(self, output, clk, rst, input, *, stages=None, name=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(clk))
    operands.append(_get_op_result_or_value(rst))
    operands.append(_get_op_result_or_value(input))
    if stages is not None: attributes["stages"] = stages
    if name is not None: attributes["name"] = name
    results.append(output)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def clk(self):
    return self.operation.operands[0]

  @builtins.property
  def rst(self):
    return self.operation.operands[1]

  @builtins.property
  def input(self):
    return self.operation.operands[2]

  @builtins.property
  def stages(self):
    if "stages" not in self.operation.attributes:
      return None
    return _ods_ir.IntegerAttr(self.operation.attributes["stages"])

  @stages.setter
  def stages(self, value):
    if value is not None:
      self.operation.attributes["stages"] = value
    elif "stages" in self.operation.attributes:
      del self.operation.attributes["stages"]

  @stages.deleter
  def stages(self):
    del self.operation.attributes["stages"]

  @builtins.property
  def name(self):
    if "name" not in self.operation.attributes:
      return None
    return _ods_ir.StringAttr(self.operation.attributes["name"])

  @name.setter
  def name(self, value):
    if value is not None:
      self.operation.attributes["name"] = value
    elif "name" in self.operation.attributes:
      del self.operation.attributes["name"]

  @name.deleter
  def name(self):
    del self.operation.attributes["name"]

  @builtins.property
  def output(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CosimEndpointOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.cosim"

  _ODS_REGIONS = (0, True)

  def __init__(self, recv, clk, rst, send, name, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(clk))
    operands.append(_get_op_result_or_value(rst))
    operands.append(_get_op_result_or_value(send))
    attributes["name"] = name
    results.append(recv)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def clk(self):
    return self.operation.operands[0]

  @builtins.property
  def rst(self):
    return self.operation.operands[1]

  @builtins.property
  def send(self):
    return self.operation.operands[2]

  @builtins.property
  def name(self):
    return _ods_ir.StringAttr(self.operation.attributes["name"])

  @name.setter
  def name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["name"] = value

  @builtins.property
  def recv(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class NoneSourceOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.none"

  _ODS_REGIONS = (0, True)

  def __init__(self, out, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    results.append(out)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def out(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class NullSourceOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.null"

  _ODS_REGIONS = (0, True)

  def __init__(self, out, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    results.append(out)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def out(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class PipelineStageOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.stage"

  _ODS_REGIONS = (0, True)

  def __init__(self, output, clk, rst, input, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(clk))
    operands.append(_get_op_result_or_value(rst))
    operands.append(_get_op_result_or_value(input))
    results.append(output)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def clk(self):
    return self.operation.operands[0]

  @builtins.property
  def rst(self):
    return self.operation.operands[1]

  @builtins.property
  def input(self):
    return self.operation.operands[2]

  @builtins.property
  def output(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class RequestInOutChannelOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.req.inout"

  _ODS_REGIONS = (0, True)

  def __init__(self, receiving, servicePort, sending, clientNamePath, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(sending))
    attributes["servicePort"] = servicePort
    attributes["clientNamePath"] = clientNamePath
    results.append(receiving)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def sending(self):
    return self.operation.operands[0]

  @builtins.property
  def receiving(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class RequestToClientConnectionOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.req.to_client"

  _ODS_REGIONS = (0, True)

  def __init__(self, receiving, servicePort, clientNamePath, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    attributes["servicePort"] = servicePort
    attributes["clientNamePath"] = clientNamePath
    results.append(receiving)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def receiving(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class RequestToServerConnectionOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.req.to_server"

  _ODS_REGIONS = (0, True)

  def __init__(self, servicePort, sending, clientNamePath, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(sending))
    attributes["servicePort"] = servicePort
    attributes["clientNamePath"] = clientNamePath
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def sending(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ServiceDeclInOutOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.inout"

  _ODS_REGIONS = (0, True)

  def __init__(self, inner_sym, inType, outType, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    attributes["inner_sym"] = inner_sym
    attributes["inType"] = inType
    attributes["outType"] = outType
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inner_sym(self):
    return _ods_ir.StringAttr(self.operation.attributes["inner_sym"])

  @inner_sym.setter
  def inner_sym(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["inner_sym"] = value

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ServiceDeclOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.decl"

  _ODS_REGIONS = (1, True)

  def __init__(self, sym_name, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    attributes["sym_name"] = sym_name
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def sym_name(self):
    return _ods_ir.StringAttr(self.operation.attributes["sym_name"])

  @sym_name.setter
  def sym_name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["sym_name"] = value

  @builtins.property
  def ports(self):
    return self.regions[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ServiceHierarchyMetadataOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.hierarchy.metadata"

  _ODS_REGIONS = (0, True)

  def __init__(self, service_symbol, serverNamePath, impl_type, clients, *, impl_details=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    attributes["service_symbol"] = service_symbol
    attributes["serverNamePath"] = serverNamePath
    attributes["impl_type"] = impl_type
    if impl_details is not None: attributes["impl_details"] = impl_details
    attributes["clients"] = clients
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def impl_type(self):
    return _ods_ir.StringAttr(self.operation.attributes["impl_type"])

  @impl_type.setter
  def impl_type(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["impl_type"] = value

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ServiceImplementReqOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.impl_req"

  _ODS_REGIONS = (1, True)

  def __init__(self, outputs, service_symbol, impl_type, inputs, *, impl_opts=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(inputs))
    attributes["service_symbol"] = service_symbol
    attributes["impl_type"] = impl_type
    if impl_opts is not None: attributes["impl_opts"] = impl_opts
    results.extend(outputs)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inputs(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def impl_type(self):
    return _ods_ir.StringAttr(self.operation.attributes["impl_type"])

  @impl_type.setter
  def impl_type(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["impl_type"] = value

  @builtins.property
  def outputs(self):
    _ods_variadic_group_length = len(self.operation.results) - 1 + 1
    return self.operation.results[0:0 + _ods_variadic_group_length]

  @builtins.property
  def portReqs(self):
    return self.regions[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ServiceInstanceOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.instance"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, service_symbol, impl_type, inputs, *, impl_opts=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(inputs))
    attributes["service_symbol"] = service_symbol
    attributes["impl_type"] = impl_type
    if impl_opts is not None: attributes["impl_opts"] = impl_opts
    results.extend(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inputs(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def impl_type(self):
    return _ods_ir.StringAttr(self.operation.attributes["impl_type"])

  @impl_type.setter
  def impl_type(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["impl_type"] = value

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ToClientOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.to_client"

  _ODS_REGIONS = (0, True)

  def __init__(self, inner_sym, type, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    attributes["inner_sym"] = inner_sym
    attributes["type"] = type
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inner_sym(self):
    return _ods_ir.StringAttr(self.operation.attributes["inner_sym"])

  @inner_sym.setter
  def inner_sym(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["inner_sym"] = value

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ToServerOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.service.to_server"

  _ODS_REGIONS = (0, True)

  def __init__(self, inner_sym, type, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    attributes["inner_sym"] = inner_sym
    attributes["type"] = type
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inner_sym(self):
    return _ods_ir.StringAttr(self.operation.attributes["inner_sym"])

  @inner_sym.setter
  def inner_sym(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["inner_sym"] = value

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class UnwrapSVInterfaceOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.unwrap.iface"

  _ODS_REGIONS = (0, True)

  def __init__(self, chanInput, interfaceSource, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(chanInput))
    operands.append(_get_op_result_or_value(interfaceSource))
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def chanInput(self):
    return self.operation.operands[0]

  @builtins.property
  def interfaceSource(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class UnwrapValidReadyOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.unwrap.vr"

  _ODS_REGIONS = (0, True)

  def __init__(self, rawOutput, valid, chanInput, ready, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(chanInput))
    operands.append(_get_op_result_or_value(ready))
    results.append(rawOutput)
    results.append(valid)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def chanInput(self):
    return self.operation.operands[0]

  @builtins.property
  def ready(self):
    return self.operation.operands[1]

  @builtins.property
  def rawOutput(self):
    return self.operation.results[0]

  @builtins.property
  def valid(self):
    return self.operation.results[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class WrapSVInterfaceOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.wrap.iface"

  _ODS_REGIONS = (0, True)

  def __init__(self, output, interfaceSink, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(interfaceSink))
    results.append(output)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def interfaceSink(self):
    return self.operation.operands[0]

  @builtins.property
  def output(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class WrapValidReadyOp(_ods_ir.OpView):
  OPERATION_NAME = "esi.wrap.vr"

  _ODS_REGIONS = (0, True)

  def __init__(self, chanOutput, ready, rawInput, valid, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(rawInput))
    operands.append(_get_op_result_or_value(valid))
    results.append(chanOutput)
    results.append(ready)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def rawInput(self):
    return self.operation.operands[0]

  @builtins.property
  def valid(self):
    return self.operation.operands[1]

  @builtins.property
  def chanOutput(self):
    return self.operation.results[0]

  @builtins.property
  def ready(self):
    return self.operation.results[1]
