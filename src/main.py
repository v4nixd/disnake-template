class Main:
    instance = None

    def __init__(self) -> None:
        print("Main initialized")

    @staticmethod
    def get_instance() -> Main:
        if not Main.instance:
            Main.instance = Main()
        return Main.instance


if __name__ == "__main__":
    main = Main.get_instance()
