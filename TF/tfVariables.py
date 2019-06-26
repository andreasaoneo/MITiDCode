import tensorflow as tf
import matplotlib.pyplot as plt

tf.reset_default_graph()

input_data = tf.placeholder(dtype=tf.float32, shape=[None, 2])

double_operation = input_data * 2

with tf.Session() as sess:
    res = sess.run(double_operation, feed_dict={input_data: [[-3, 9], [1, 9]]})
    plt.plot(res)
    print(res)

plt.show()
