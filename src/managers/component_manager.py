from src.utils.templates.class_starter import starter


class component_manager(starter):
    def __init__(self, config_manager, log_manager):
        super().__init__(config_manager, log_manager)

        self.lm.log.info("Component manager initialized.")

    def run(self, objs, managers):
        for obj in objs:
            for component in obj.properties.keys():
                if component in managers:
                    managers[component].component(obj, obj.properties[component])
