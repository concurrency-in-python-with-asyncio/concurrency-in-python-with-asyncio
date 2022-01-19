from chapter_14.listing_14_8 import CustomFuture


class CustomTask(CustomFuture):

    def __init__(self, coro, loop):
        super(CustomTask, self).__init__()
        self._coro = coro
        self._loop = loop
        self._current_result = None
        self._task_state = None
        loop.register_task(self)  # A

    def step(self):  # B
        try:
            if self._task_state is None:
                self._task_state = self._coro.send(None)
            if isinstance(self._task_state, CustomFuture):  # C
                self._task_state.add_done_callback(self._future_done)
        except StopIteration as si:
            self.set_result(si.value)

    def _future_done(self, result):  # D
        self._current_result = result
        try:
            self._task_state = self._coro.send(self._current_result)
        except StopIteration as si:
            self.set_result(si.value)
