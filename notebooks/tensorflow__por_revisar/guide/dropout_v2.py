import tensorflow as tf

d = tf.nn.dropout(tf.range(10), rate=1 - (0.2))
z = tf.compat.v1.zeros_like(d, optimize=False)
