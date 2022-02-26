class Config():
    def __init__(self) -> None:
        self.setting = 1
        self.destination = 'Cloud'

    def _change_to_onprem(self):
        self.destination = 'On premise'