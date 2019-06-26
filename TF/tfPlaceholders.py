import tensorflow as tf
import matplotlib.pyplot as plt

tf.reset_default_graph()

input_data = tf.placeholder(dtype=tf.float32, shape=[None,2])

double_operation = input_data * 2

with tf.Session() as sess:
    print(sess.run(double_operation, feed_dict={input_data: [[8, 2], [3, 4]]}))
    plt.plot(sess.run(double_operation, feed_dict={input_data: [[6, 2], [3, 4]]}))

plt.show()
