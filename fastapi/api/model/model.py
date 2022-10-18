from pydantic import BaseModel


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def to_list(self):
        return [self.sepal_length, self.sepal_width, self.petal_length, self.petal_width]


class IrisResponse(BaseModel):
    species: str
