# coding:utf-8
__author__ = 'renjieguan'

from sklearn.metrics import r2_score
import numpy as np


def performance_metric(y_true, y_predict):
    """计算并返回预测值相比于预测值的分数"""

    score = r2_score(y_true, y_predict)

    return score


def performance_metric2(y_true, y_predict):
    """计算并返回预测值相比于预测值的分数"""
    y_mean = np.mean(y_true)
    tot = 0 #total sum of squares
    res = 0 #residual sum of squares
    for i in range(len(y_true)):
        tot += np.square(y_true[i] - y_mean)
        res += np.square(y_predict[i] - y_true[i])
    score = 1 - res/tot
    return score


score = performance_metric2([3, -0.5, 2, 7, 4.2], [2.5, 0.0, 2.1, 7.8, 5.3])
print "Model has a coefficient of determination, R^2, of {:.3f}.".format(score)


