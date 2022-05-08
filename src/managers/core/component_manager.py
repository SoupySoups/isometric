from src.managers.core.logging_manager import logging_manager


class component_manager:
    def __init__(self):
        self.components = {}

        logging_manager().log.debug("Component manager initialized.")

    def register_component(self, name: str):
        def decorator(function):
            self.components[name] = function
            return function

        return decorator

    def run(self, objs, managers):
        for obj in objs:
            for component in obj.properties.keys():
                if component in managers:
                    managers[component].component(obj, obj.properties[component])
                else:
                    logging_manager().log.warning(f"Component {component} not found.")
