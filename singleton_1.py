class Settings:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.tema = "claro"
    
if __name__ == "__main__":
    st1 = Settings()

    st1.tema = "escuro"
    st2 = Settings()

    print(st1 is st2)
    print(st2.tema)