import constants
from typing import Any


def setup(channel: int, direction: int, pull_up_down: int = constants.PUD_OFF, initial: None = None) -> None:
    pass


def cleanup(channel: int = None) -> None:
    pass


def output(channel: int, value: int) -> None:
    pass


def input(channel: int) -> int:
    pass


def setmode(mode: int) -> None:
    pass


def getmode(mode: int) -> Any:
    pass


def add_event_callback(gpio: None, callback: Any) -> None:
    pass


def add_event_detect(gpio: None, edge: int, callback: Any = None, bouncetime: float = None) -> None:
    pass


def remove_event_detect(gpio: None) -> None:
    pass


def event_detected(channel: int) -> int:
    pass


def wait_for_edge(channel: int, edge: int, bouncetime: float = None, timeout: float = None) -> int:
    pass


def gpio_function(channel: int) -> Any:
    pass


def setwarnings(state: bool) -> None:
    pass
