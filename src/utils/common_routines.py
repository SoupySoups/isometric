def quit() -> None:
    """Quits the application."""
    import pygame
    from src.managers.core.logging_manager import logging_manager

    logging_manager().log.info("Quitting.")
    pygame.quit()
    exit()
