import numpy as np
from sklearn.externals import joblib
import models.makeModel
def SMOreg(obj,rbX,rbY):

    input = np.array([[obj.screen_num_7, obj.show_num_7, obj.money_num_7, obj.audience_num_7, obj.director_effect,
                       obj.distributor_effect, obj.month, obj.nationality, obj.before_grade, obj.after_grade, obj.age,
                       obj.actor_effect]], dtype=np.float64)
    if rbX == 0 and rbY == 0:
        dict = models.makeModel.modeling(input)

        return dict

    else:
        # load model
        clf2 = joblib.load('models/SMOreg.pkl')
        audience_num = clf2.predict(rbX.transform(input))
        audience_num = np.expand_dims(audience_num, 0)
        audience_num = audience_num.T
        audience_num = rbY.inverse_transform(audience_num)
        audience_num = np.squeeze(audience_num)

        return {'audience_num':audience_num, 'rbX':rbX, 'rbY':rbY}
