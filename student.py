class Student:
    def __init__(self, name, study_hours, midterm_score, attendance):
        self.name = name
        self.study_hours = study_hours
        self.midterm_score = midterm_score
        self.attendance = attendance

    def to_features(self):
        return [self.study_hours, self.midterm_score, self.attendance]
