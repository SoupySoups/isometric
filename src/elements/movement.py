class movement:
    def __init__(self):
        self.object_queue = []

    def component(self, obj, fields):
        if fields.use_keyboard:
            self.object_queue.append(obj)
