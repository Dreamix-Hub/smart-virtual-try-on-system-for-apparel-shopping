class AppException(Exception):
    def __init__(self, msg: str, code: str, status_code: int) -> None:
        self.message = msg
        self.code = code
        self.status_code = status_code
        
        super().__init__(msg)
        
        