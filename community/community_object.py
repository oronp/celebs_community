class Agent:
    def __init__(self, name: str, reports: list, images_reports: list = None):
        self.name = name
        self.reports = reports
        self.image_reports = images_reports or []


class Troll(Agent):
    pass
