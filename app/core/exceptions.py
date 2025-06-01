class NotFoundException(Exception):
    def __init__(self, message: str | None = None):
        self.message = message
        super().__init__(self.message)

