#测试模型

import numpy as np
import tensorflow as tf
import model.cnn_model as model



def evaluate(image_array):
    with tf.Graph().as_default():
        BATCH_SIZE = 1
        N_CLASSES = 7
        image = tf.cast(image_array, tf.float32)
        image = tf.reshape(image, [1, 48, 48, 1])

        logit = model.inference(image, BATCH_SIZE, N_CLASSES, regularizer=None, reuse=False)

        #logit = tf.nn.softmax(logit)

        x = tf.placeholder(tf.float32, shape=[48, 48])

        logs_train_dir = "C:/Users/huang/Desktop/train/log/train/"

        saver = tf.train.Saver()

        with tf.Session() as sess:
            ckpt = tf.train.get_checkpoint_state(logs_train_dir)
            if ckpt and ckpt.model_checkpoint_path:
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')
                saver.restore(sess=sess, save_path=ckpt.model_checkpoint_path)
            else:
                print('No checkpoint file found')

            prediction = sess.run(logit, feed_dict={x: image_array})
            max_index = np.argmax(prediction)

           # if max_index == 0:
                #print('This is anger with possibility %.6f' % prediction[:, 0])
          #  if max_index == 1:
            #    print('This is disgust with possibility %.6f' % prediction[:, 1])
           # if max_index == 2:
           #     print('This is fear with possibility %.6f' % prediction[:, 2])
           # if max_index == 3:
           #     print('This is happy with possibility %.6f' % prediction[:, 3])
            #if max_index == 4:
           #     print('This is sad with possibility %.6f' % prediction[:, 4])
            #if max_index == 5:
           #     print('This is surprised with possibility %.6f' % prediction[:, 5])
            #if max_index == 6:
            #    print('This is normal with possibility %.6f' % prediction[:, 6])
    return max_index