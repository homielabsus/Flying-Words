"""PReLU(x) = max(0, x) + slope * min(0, x) = Relu(x) + (-slope) * Relu(-x): the same numbers with operations every ONNX Runtime engine has."""
import sys, numpy as np, onnx
from onnx import helper, numpy_helper
src, dst = sys.argv[1], sys.argv[2]
m = onnx.load(src); g = m.graph
inits = {i.name: i for i in g.initializer}
nodes, minus1 = [], numpy_helper.from_array(np.array(-1, dtype=np.float32), 'prelu_minus_one'); g.initializer.append(minus1)
for n in g.node:
    if n.op_type != 'PRelu': nodes.append(n); continue
    x, s, y = n.input[0], n.input[1], n.output[0]
    slope = numpy_helper.to_array(inits[s]); neg = numpy_helper.from_array((-slope).astype(np.float32), s + '_neg'); g.initializer.append(neg)
    p = y + '_'
    nodes += [helper.make_node('Relu', [x], [p + 'pos']), helper.make_node('Mul', [x, 'prelu_minus_one'], [p + 'flip']), helper.make_node('Relu', [p + 'flip'], [p + 'negpart']),
              helper.make_node('Mul', [p + 'negpart', s + '_neg'], [p + 'scaled']), helper.make_node('Add', [p + 'pos', p + 'scaled'], [y])]
del g.node[:]; g.node.extend(nodes)
used = {i for n in g.node for i in n.input}
keep = [i for i in g.initializer if i.name in used]; del g.initializer[:]; g.initializer.extend(keep)
onnx.checker.check_model(m); onnx.save(m, dst); print('saved', dst)
