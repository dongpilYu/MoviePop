import numpy as np
import weka.core.jvm as jvm
import weka.core.serialization as serialization
from weka.classifiers import Classifier
from weka.core.converters import Loader
from weka.core.converters import ndarray_to_instances
import os
from sklearn.svm import SVR
from sklearn.externals import joblib


def SMOreg(obj):

    # load model
    print(123)
    clf2 = joblib.load('models/SMOreg.pkl')
    print(456)
    input = np.array([obj.screen_num_7, obj.show_num_7, obj.money_num_7, obj.audience_num_7, obj.director_effect,
                       obj.distributor_effect, obj.month, obj.nationality, obj.before_grade, obj.after_grade, obj.age,
                       obj.actor_effect], dtype=np.float64)
    print(789)
    input.reshape(1,-1)
    print(000)
    #instance = ndarray_to_instances(input, relation="input")

    #for index, inst in enumerate(instance):
    #    audience_num = clf2.classify_instance(inst)

    audience_num = clf2.predict(input)

    return audience_num

"""

def SimpleLogistic(obj):
    jvm.start(packages=True)

    r = open("models/input_classification.arff")
    lines = r.readlines()
    lines = lines[:-1]
    lines += "%d,%d,%d,%d,%d,%d,%d,%d,%f,%f,%d,%d,%d\n" % (
        int(obj.screen_num_7), int(obj.show_num_7), int(obj.money_num_7), int(obj.audience_num_7),
        int(obj.director_effect), int(obj.distributor_effect), int(obj.month), int(obj.nationality),
        float(obj.after_grade), float(obj.before_grade), int(obj.age), int(obj.actor_effect), 1)
    r.close()

    w = open("models/input_classification.arff", 'w')
    w.writelines(lines)
    w.close()

    # load model
    cls = Classifier(jobject=serialization.read("models/SimpleLogistic.model"))
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("models/input_classification.arff")
    # 분류이기 때문에 예측 데이터 타입이 nominal이라 numpy로 받을 수 없음.

    data.class_is_last()
    for index, inst in enumerate(data):
        audience_class = cls.classify_instance(inst)

    # jvm.stop()
    return audience_class + 1  # index가 0부터라 +1


def SimpleLogistic_before(obj):
    jvm.start(packages=True)

    r = open("models/input_classification_before.arff")
    lines = r.readlines()
    lines = lines[:-1]
    lines += "%d,%d,%d,%d,%d,%d,%d,%f,%f,%d,%d,%d\n" % (
        int(obj.screen_num_7), int(obj.show_num_7), int(obj.money_num_7), int(obj.audience_num_7),
        int(obj.director_effect), int(obj.distributor_effect), int(obj.nationality),
        float(obj.after_grade), float(obj.before_grade), int(obj.age), int(obj.actor_effect), 1)
    r.close()

    w = open("models/input_classification_before.arff", 'w')
    w.writelines(lines)
    w.close()

    # load model
    cls = Classifier(jobject=serialization.read("models/SimpleLogistic_before.model"))
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("models/input_classification_before.arff")
    # 분류이기 때문에 예측 데이터 타입이 nominal이라 numpy로 받을 수 없음.

    data.class_is_last()
    for index, inst in enumerate(data):
        audience_class = cls.classify_instance(inst)

    # jvm.stop()
    return audience_class + 1  # index가 0부터라 +1


def SMOreg(obj):
    jvm.start(packages=True)

    # load model
    cls = Classifier(jobject=serialization.read("models/SMOreg.model"))
    input = np.array([[obj.screen_num_7, obj.show_num_7, obj.money_num_7, obj.audience_num_7, obj.director_effect,
                       obj.distributor_effect, obj.month, obj.nationality, obj.before_grade, obj.after_grade, obj.age,
                       obj.actor_effect, 0]], dtype=np.float64)
    instance = ndarray_to_instances(input, relation="input")

    for index, inst in enumerate(instance):
        audience_num = cls.classify_instance(inst)



    # jvm.stop()
    return audience_num


def SMOreg_before(obj):
    jvm.start(packages=True)

    # load model
    cls = Classifier(jobject=serialization.read("models/SMOreg_before.model"))
    input = np.array([[obj.screen_num_7, obj.show_num_7, obj.money_num_7, obj.audience_num_7, obj.director_effect,
                       obj.distributor_effect, obj.nationality, obj.before_grade, obj.after_grade, obj.age,
                       obj.actor_effect, 0]], dtype=np.float64)
    instance = ndarray_to_instances(input, relation="input")

    for index, inst in enumerate(instance):
        audience_num = cls.classify_instance(inst)

    # jvm.stop()
    return audience_num

"""