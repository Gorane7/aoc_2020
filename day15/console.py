

class Console:

    def __init__(self, rawProgram, callbacks):
        self.commands = {
            "acc": self.accumulate,
            "jmp": self.jump,
            "nop": self.noOperation
        }
        self.program = self.processProgram(rawProgram)
        self.accumulator = 0
        self.index = 0
        self.running = True
        self.commandHistory = []
        self.callbacks = callbacks

        self.printCommands = False
        self.printExitReason = True
        self.printExitWarning = False

        self.exitOnLoop = True
        self.exitOnEnd = True

    def noOperation(self, amount):
        self.index += 1
        if self.printCommands:
            print(f"Executed no operation")

    def accumulate(self, amount):
        self.accumulator += amount
        self.index += 1
        if self.printCommands:
            print(f"Increased accumulator value to {self.accumulator}")

    def jump(self, amount):
        self.index += amount
        if self.printCommands:
            print(f"Increased index from {self.index - amount} to {self.index}")

    def switch(self, a, b, index=None):
        if self.program[index][0] == self.commands[a]:
            self.program[index][0] = self.commands[b]
            return True
        if self.program[index][0] == self.commands[b]:
            self.program[index][0] = self.commands[a]
            return True
        return False

    def processLine(self, line):
        split = line.strip().split(" ")
        return [self.commands[split[0]], int(split[1])]

    def processProgram(self, rawProgram):
        return list(map(self.processLine, rawProgram))

    def shouldRun(self):
        normal = self.index >= len(self.program)
        loop = self.index in self.commandHistory
        running = not self.running

        if self.index >= len(self.program):
            normal = normal and self.exitOnEnd
            if self.printExitReason and normal:
                print("Program reached normal exit condition")
            elif self.printExitWarning:
                print("Program reached normal exit condition, but condition was disabled")
        if self.index in self.commandHistory:
            loop = loop and self.exitOnLoop
            if self.printExitReason and loop:
                print("Infinite loop detected")
            elif self.printExitWarning:
                print("Infinite loop detected, but condition was disabled")
        if not self.running:
            if self.printExitReason:
                print("Force shutdown")
        return not (running or normal or loop)

    def run(self):
        while self.shouldRun():
            self.commandHistory.append(self.index)
            self.program[self.index][0](self.program[self.index][1])
