class GuardarLogResponse():

    def __init__(self, hash = str) -> None:
        self.hash = hash
    
    def to_JSON(self):
        return {
            'hash': self.hash
        }