import logging


def quit(logger: logging.Logger = None) -> None:
    """Quits the application."""
    import pygame

    if logger is not None:
        logger.log.info("Quitting.")
    pygame.quit()
    exit()