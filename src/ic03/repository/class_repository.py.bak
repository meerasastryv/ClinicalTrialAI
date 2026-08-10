from ..models.class_model import ClassModel


class ClassRepository:

    def __init__(self):
        self.classes = []

    def add(self, cls: ClassModel):
        self.classes.append(cls)

    def get_all(self):
        return self.classes

    def find_by_name(self, name):
        for cls in self.classes:
            if cls.name == name:
                return cls
        return None
