import logging
from sys import stdout


class logging_manager:
    def __init__(self, log_level) -> None:
        self.log_level = log_level
        logging.basicConfig(
            format="%(asctime)s - [%(name)s | %(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
            filename="game.log",
            filemode="w",
            level=getattr(logging, str(self.log_level).upper()),
        )
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.StreamHandler(stdout))

        self.log.info("Logging manager initialized.")

    def switch_log_level(self, log_level):
        self.log_level = log_level
        self.log.setLevel(getattr(logging, str(self.log_level).upper()))
