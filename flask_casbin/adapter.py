
from casbin import persist


class IOAdapter(persist.Adapter):
    def __init__(self, fd):
        self._fd = fd

    def load_policy(self, model):
        if not hasattr(self._fd, "readline"):
            raise RuntimeError(f"No {self._fd} readable object")

        self._load_policy(model)

    def save_policy(self, model):
        pass

    def _load_policy(self, model):
            line = self._fd.readline()
            while line:
                persist.load_policy_line(line.decode().strip(), model)
                line = self._fd.readline()
