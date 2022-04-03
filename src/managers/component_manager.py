from importlib import import_module as load_component_module


class component_manager:
    def __init__(self, config_manager, log_manager):
        self.cm = config_manager
        self.lm = log_manager

        self.lm.log.info("Component manager initialized.")

    def create_component(mgr_self, path: str, **kwargs):
        try:
            component_module = load_component_module(path)
        except ModuleNotFoundError:
            raise Exception(f"Component module not found. Source: {path}")

        try:

            class component(component_module.component):
                def __init__(self, path: str) -> None:
                    super().__init__(kwargs)
                    self.path = path
                    self.component_module = component_module
                    self.name = self.component_module.__name__.split(".")[-1]
                    try:
                        self.update = self.component_module.update
                    except AttributeError:
                        self.update = lambda: None

                    mgr_self.lm.log.debug(f'Component "{self.name}" loaded.')

                def __repr__(self):
                    return f"Component({self.name})"

        except AttributeError:
            raise Exception(
                f"Component module does not contain a component class and is invalid. Source: {path}"
            )

        except TypeError:
            raise Exception(
                f"Component module does not have argument input and is invalid. Source: {path}"
            )

        return component(path)
