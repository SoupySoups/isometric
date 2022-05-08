import src.managers.core.application_manager as application_manager


def main():
    # Set up the application manager
    am = application_manager.application_manager()

    am.load_level("levels/test_level.tmx")
    am.run()


if __name__ == "__main__":
    main()
