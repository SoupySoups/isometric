import src.managers.application_manager as application_manager

# Set up the application manager
am = application_manager.application_manager()


def main():
    am.dm.load_data('levels/test_level.tmx')
    am.run()


if __name__ == "__main__":
    main()
