from gamemode import Output, Gamemode

class Idle(Gamemode):
    def process_screen(self, screen):
        return Output(Output.DO_NOTHING, 0)