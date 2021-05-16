from chapter_14.listing_14_8 import CustomFuture


class CustomTask(CustomFuture):

    def __init__(self, coro, loop):
        super(CustomTask, self).__init__()
        self.coro = coro
        self.loop = loop
        self.current_result = None
        self.task_state = None
        loop.register_task(self)  # A

    def step(self):  # B
        try:
            if self.task_state is None:
                self.task_state = self.coro.send(None)
            if isinstance(self.task_state, CustomFuture):  # C
                self.task_state.add_done_callback(self._future_done)
        except StopIteration as si:
            self.set_result(si.value)

    def _future_done(self, result):  # D
        self.current_result = result
        try:
            self.task_state = self.coro.send(self.current_result)
        except StopIteration as si:
            self.set_result(si.value)
