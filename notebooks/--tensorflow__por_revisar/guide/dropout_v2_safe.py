import tensorflow.compat.v1 as tf

d = tf.nn.dropout(tf.range(10), 0.2)
z = tf.zeros_like(d, optimize=False)
