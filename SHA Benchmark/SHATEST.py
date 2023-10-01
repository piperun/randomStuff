import time
import subprocess
import sys
import signal

class LANGBENCHMARK:
    def __init__(self, mode, filename):
        self.mode = mode
        self.filename = filename
        self.lambdaexp = {
            "P2": lambda: subprocess.run(["py", "Z:\Programming\Python\SHA Benchmark\sha.py", "-f", self.filename, "-s", "560000", "-2"]),
            "P5": lambda: subprocess.run(["py", "Z:\Programming\Python\SHA Benchmark\sha.py", "-f", self.filename, "-s", "560000", "-5"]),
            "C2": lambda: subprocess.run(["Z:\\Programming\\C#\\hashbench\\bin\\Release\\netcoreapp3.1\\hashbench.exe", "-f", self.filename, "-2"]),
            "C5": lambda: subprocess.run(["Z:\\Programming\\C#\\hashbench\\bin\\Release\\netcoreapp3.1\\hashbench.exe", "-f", self.filename, "-5"]),
        }
        self.MODES = {
            "PP": ["Python-sha256", "Python-sha512"],
            "CP2": ["C#-sha256", "Python-sha256"],
            "CP5": ["C#-sha512", "Python-sha512"],
            "CC": ["C#-sha256", "Python-sha512"],
        }
        if self.mode == "PP":
            self.func1 = self.lambdaexp["P2"]
            self.func2 = self.lambdaexp["P5"]
        elif self.mode == "CP2":
            self.func1 = self.lambdaexp["C2"]
            self.func2 = self.lambdaexp["P2"]
        elif self.mode == "CP5":
            self.func1 = self.lambdaexp["C5"]
            self.func2 = self.lambdaexp["P5"]
        elif self.mode == "CC":
            self.func1 = self.lambdaexp["C2"]
            self.func2 = self.lambdaexp["C5"]
    pass

    def timeit(self):
        start = time.time()
        self.func1()
        end = time.time()
        print(end - start, self.MODES[self.mode][0], "\n")

        start = time.time()
        self.func2()
        end = time.time()
        print(end - start, self.MODES[self.mode][1], "\n")


class PARALLEL:
    def __init__(self, mode, path):
        self.funclist = []
        self.mode = mode
        self.path = path
        self.lambdaexp = {
            "T": lambda: subprocess.run(["Z:\\Programming\\C#\\hashbench\\bin\\Release\\netcoreapp3.1\\hashbench.exe", "-f", self.path, "-T"]),
            "M": lambda: subprocess.run(["Z:\\Programming\\C#\\hashbench\\bin\\Release\\netcoreapp3.1\\hashbench.exe", "-f", self.path, "-P"]),
            "L": lambda: subprocess.run(["Z:\\Programming\\C#\\hashbench\\bin\\Release\\netcoreapp3.1\\hashbench.exe", "-f", self.path, "-L"]),
        }
        self.MODES = {
            "T": "Multithreaded",
            "M": "Parallel",
            "L": "Loop",
        }
        for i in range(len(self.mode)):
            self.funclist.append(self.lambdaexp[self.mode[i]])
        pass

    def timeit(self):
        for i in range(0, len(self.funclist)):
            start = time.time()
            self.funclist[i]()
            end = time.time()
            print(end - start, self.MODES[self.mode[i]], "\n")
            pass
        pass
    pass


def funcmode(mode, path):
    for i in range(0, len(mode)):
        if mode[i] in "CP":
            return LANGBENCHMARK(mode, path)
        elif mode[i] in "TML":
            return PARALLEL(mode, path)


def main():    
    bench = funcmode("MTL", "Z:\\TEST\\120mb64")
    maxnum = 2
    for i in range(0, maxnum):
        bench.timeit()
        print(f"Done {i+1} loops of {maxnum}")
    pass

if __name__ == "__main__":
    main()
    pass

