from sklearn.linear_model import LinearRegression

class Predictor:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, students):
        X = [s.to_features() for s in students]
        y = [0.6 * s.midterm_score + 0.2 * s.study_hours + 0.2 * s.attendance for s in students]
        self.model.fit(X, y)

    def predict(self, student):
        return self.model.predict([student.to_features()])[0]
