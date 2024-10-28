import subprocess

# paths to tool
GOBUSTER_PATH = "/add/path/to/GOBUSTER"
FFUF_PATH = "/add/path/to/ffuf"
WENUM_PATH = "/add/path/to/wenum"
FEROXBUSTER_PATH = "/add/path/to/feroxbuster"

# execute xommand and capture output
def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

#classes for each tool
class Gobuster:
    def __init__(self, url, wordlist):
        self.url = url
        self.wordlist = wordlist

    def run(self):
        command = f"{GOBUSTER_PATH} dir -u {self.url} -w {self.wordlist}"
        output, error = execute_command(command)
        if error:
            print("Error running Gobuster:", error)
        else:
            print("Gobuster results:\n", output)

class FFUF:
    def __init__(self, url, wordlist):
        self.url = url
        self.wordlist = wordlist

    def run(self):
        command = f"{FFUF_PATH} -u {self.url}/FUZZ -w {self.wordlist}"
        output, error = execute_command(command)
        if error:
            print("Error running FFUF:", error)
        else:
            print("FFUF results:\n", output)

class Wenum:
    def __init__(self, url, options=""):
        self.url = url
        self.options = options

    def run(self):
        command = f"{WENUM_PATH} {self.url} {self.options}"
        output, error = execute_command(command)
        if error:
            print("Error running Wenum:", error)
        else:
            print("Wenum results:\n", output)

class Feroxbuster:
    def __init__(self, url, wordlist):
        self.url = url
        self.wordlist = wordlist

    def run(self):
        command = f"{FEROXBUSTER_PATH} -u {self.url} -w {self.wordlist}"
        output, error = execute_command(command)
        if error:
            print("Error running Feroxbuster:", error)
        else:
            print("Feroxbuster results:\n", output)

#main func
def run_web_fuzzing_toolkit(url, wordlist):
    print(f"Starting web fuzzing on {url}...\n")

    gobuster = Gobuster(url, wordlist)
    ffuf = FFUF(url, wordlist)
    wenum = Wenum(url)
    feroxbuster = Feroxbuster(url, wordlist)


    print("Running Gobuster...")
    gobuster.run()

    print("Running FFUF...")
    ffuf.run()

    print("Running Wenum...")
    wenum.run()

    print("Running Feroxbuster...")
    feroxbuster.run()

# Enter specific urls and path to wordlists
if __name__ == "__main__":
    target_url = "http://example.com"
    wordlist_path = "/path/to/wordlist.txt"
    run_web_fuzzing_toolkit(target_url, wordlist_path)
