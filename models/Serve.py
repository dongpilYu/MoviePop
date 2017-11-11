import numpy as np
import weka.core.jvm as jvm
import weka.core.serialization as serialization
from weka.classifiers import Classifier
from weka.core.converters import Loader
from weka.core.converters import ndarray_to_instances


def SimpleLogistic(obj):
    jvm.start(packages=True)

    r = open("new_models/input_classification.arff")
    lines = r.readlines()
    lines = lines[:-1]
    lines += "%d,%d,%d,%d,%d,%d,%d,%d,%f,%f,%d,%d,%d\n" % (
        int(obj.screen_num_7), int(obj.show_num_7), int(obj.money_num_7), int(obj.audience_num_7),
        int(obj.director_effect), int(obj.distributor_effect), int(obj.month), int(obj.nationality),
        float(obj.after_grade), float(obj.before_grade), int(obj.age), int(obj.actor_effect), 1)
    r.close()

    w = open("new_models/input_classification.arff", 'w')
    w.writelines(lines)
    w.close()

    # load model
    cls = Classifier(jobject=serialization.read("new_models/SimpleLogistic.model"))
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("new_models/input_classification.arff")
    # 분류이기 때문에 예측 데이터 타입이 nominal이라 numpy로 받을 수 없음.

    data.class_is_last()
    for index, inst in enumerate(data):
        audience_class = cls.classify_instance(inst)

    jvm.stop()
    return audience_class + 1  # index가 0부터라 +1


def SimpleLogistic_before(obj):
    jvm.start(packages=True)

    r = open("new_models/input_classification_before.arff")
    lines = r.readlines()
    lines = lines[:-1]
    lines += "%d,%d,%d,%d,%d,%d,%d,%f,%f,%d,%d,%d\n" % (
        int(obj.screen_num_7), int(obj.show_num_7), int(obj.money_num_7), int(obj.audience_num_7),
        int(obj.director_effect), int(obj.distributor_effect), int(obj.nationality),
        float(obj.after_grade), float(obj.before_grade), int(obj.age), int(obj.actor_effect), 1)
    r.close()

    w = open("new_models/input_classification_before.arff", 'w')
    w.writelines(lines)
    w.close()

    # load model
    cls = Classifier(jobject=serialization.read("new_models/SimpleLogistic_before.model"))
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("new_models/input_classification_before.arff")
    # 분류이기 때문에 예측 데이터 타입이 nominal이라 numpy로 받을 수 없음.

    data.class_is_last()
    for index, inst in enumerate(data):
        audience_class = cls.classify_instance(inst)

    jvm.stop()
    return audience_class + 1  # index가 0부터라 +1


def SMOreg(obj):
    jvm.start(packages=True)

    # load model
    cls = Classifier(jobject=serialization.read("new_models/SMOreg.model"))
    input = np.array([[obj.screen_num_7, obj.show_num_7, obj.money_num_7, obj.audience_num_7, obj.director_effect,
                       obj.distributor_effect, obj.month, obj.nationality, obj.before_grade, obj.after_grade, obj.age,
                       obj.actor_effect, 0]], dtype=np.float64)
    instance = ndarray_to_instances(input, relation="input")

    for index, inst in enumerate(instance):
        audience_num = cls.classify_instance(inst)

    jvm.stop()
    return audience_num


def SMOreg_before(obj):
    jvm.start(packages=True)

    # load model
    cls = Classifier(jobject=serialization.read("new_models/SMOreg_before.model"))
    input = np.array([[obj.screen_num_7, obj.show_num_7, obj.money_num_7, obj.audience_num_7, obj.director_effect,
                       obj.distributor_effect, obj.nationality, obj.before_grade, obj.after_grade, obj.age,
                       obj.actor_effect, 0]], dtype=np.float64)
    instance = ndarray_to_instances(input, relation="input")

    for index, inst in enumerate(instance):
        audience_num = cls.classify_instance(inst)

    jvm.stop()
    return audience_num
