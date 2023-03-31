import enum
class Verb:
    class Valancy:
        def __init__(self,takes_subject: bool,amount_of_objects: tuple[int,int]) -> None:
            self.takes_subject=takes_subject
            self.amount_of_objects=amount_of_objects
    def __init__(self,valancy: Valancy) -> None:
        self.valancy=valancy
        pass