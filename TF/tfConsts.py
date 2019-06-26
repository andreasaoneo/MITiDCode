import tensorflow as tf

tf.reset_default_graph()

constOne = tf.constant(15, dtype = tf.float32)
constTwo = tf.constant(3, dtype = tf.float32)
add_one_operation = constOne + constTwo

print(add_one_operation)

with tf.Session() as sess:
    print(sess.run(add_one_operation))
