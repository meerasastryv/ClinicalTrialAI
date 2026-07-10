import threading


class ExecutionContext:
    """
    Maintains a thread-local execution stack.
    """

    _local = threading.local()

    @classmethod
    def _get_stack(cls):
        if not hasattr(cls._local, "stack"):
            cls._local.stack = []
        return cls._local.stack

    @classmethod
    def push(cls, method_name: str):
        cls._get_stack().append(method_name)

    @classmethod
    def pop(cls):
        stack = cls._get_stack()
        if stack:
            stack.pop()

    @classmethod
    def current(cls):
        stack = cls._get_stack()
        if stack:
            return stack[-1]
        return None

    @classmethod
    def caller(cls):
        stack = cls._get_stack()
        if len(stack) >= 2:
            return stack[-2]
        return None

    @classmethod
    def clear(cls):
        cls._local.stack = []
