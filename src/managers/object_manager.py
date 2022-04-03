import src.managers.component_manager as component_manager


class object_manager:
    def __init__(self, config_manager, logging_manager) -> None:
        self.lm = logging_manager
        self.cm = config_manager

        self.objects = []

        self.ctm = component_manager.component_manager(self.cm, self.lm)

        self.lm.log.info("Object manager initialized.")

    def load_from_id_dict(self, id_dict: dict) -> None:
        for id in id_dict.keys():
            obj = id_dict[id]
            components = {}
            for property in obj.properties.keys():
                if property.startswith("component"):
                    components[property.split(".", 1)[-1]] = {
                        "src": obj.properties[property],
                        "args": {},
                    }
                elif len(property.split(".", 1)) > 1:
                    if type(obj.properties[property]) is str and obj.properties[property].startswith("attribute."): # Value is a reference
                        if obj.properties[property].split(".", 2)[1] == "self": # Reference is to self
                            components[property.split(".", 1)[0]]["args"][property.split(".", 2)[-1]] = getattr(obj, obj.properties[property].split(".", 2)[-1])
                        else: # Reference is to another component
                            components[property.split(".", 1)[0]]["args"][property.split(".", 1)[-1]] = components[obj.properties[property].split(".")[1]]['args'][obj.properties[property].split(".", 2)[-1]]
                    else: # Value is a literal
                        components[property.split(".", 1)[0]]["args"][property.split(".", 1)[-1]] = obj.properties[property]
                else:
                    raise AttributeError(f"Invalid property: {property}")

            self.new_object(
                obj.name if obj.name is not None else id, components=components
            )

    def new_object(self, id: str, components: dict) -> list:
        new = object(id)

        for component in components.keys():
            try:
                new.add_component(
                    self.ctm.create_component(
                        components[component]["src"], **components[component]["args"]
                    )
                )
            except KeyError:
                raise AttributeError(
                    f'Component "{component}" properties missing or invalid.'
                )

        self.objects.append(new)

        print(new.components)

        return self.objects


class object:
    def __init__(self, id: str) -> None:
        self.id = id
        self.components = []

    def add_component(self, component) -> list:
        self.components.append(component)
        return self.components

    def remove_component(self, component) -> list:
        self.components.remove(component)
        return self.components
