from src.components.basic_component import template


class component(template):
    def __init__(self, args) -> None:
        super().__init__(args)
        # Program your component here.
        print(self.arguments)
