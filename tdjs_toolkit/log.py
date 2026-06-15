from pathlib import Path
import datetime

def timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')

class log:
    def __init__(self, appname = "Python"):
        self.appname = appname
    def info(self, text):
        if not isinstance(text, str):
            return None
        out = f"{timestamp()} {self.appname}[INFO] {text}"
        print(out)
        return out
    def warning(self, text):
        if not isinstance(text, str):
            return None
        out = f"{timestamp()} {self.appname}[WARNING] {text}"
        print(out)
        return out
    def error(self, text):
        if not isinstance(text, str):
            return None
        out = f"{timestamp()} {self.appname}[ERROR] {text}"
        print(out)
        return out
    def custom(self, text, logtype = "APP"):
        if not isinstance(text, str):
            return None
        out = f"{timestamp()} {self.appname}[{logtype.upper()}] {text}"
        print(out)
        return out





class Logsession:
    def __init__(self, appname = "python", log_dir: Path = Path(".logs")):
        """
        We recommend using variables to hold Logsession() and another
        one that holds something like `<Logsession var>.logtypes
        for this to work properly.

        example usage:

        x = tdjs.log.Logsession(appname="Libtest")

        x.log(x.logtypes.error("error"))

        :param appname: optional Name of the app for logging
        :param log_dir: optional Logging folder where logs will be stored.
        """

        self.startmsg = "[TDJS.Loglib] Logsession started"

        self.logtypes = log(appname=appname)
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.logfile = log_dir / f"{timestamp()}.log"
        self.logfile.touch()
        self.latest_log = log_dir / "latest.log"
        self.latest_log.touch()
        self.logfile.write_text(self.startmsg)
        self.latest_log.write_text(self.startmsg)

        self.appname = appname
    def log(self, text: str):
        out = self.logfile.read_text()
        out += f"\n{text}"
        self.logfile.write_text(out)
        out = self.latest_log.read_text()
        out += f"\n{text}"
        self.latest_log.write_text(out)
