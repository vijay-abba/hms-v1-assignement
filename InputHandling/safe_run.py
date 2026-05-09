from exceptions.custom_expections import HMSBaseException
from utils.custome_print import ColPt


def safe_run(func, *args, **kwargs):

    try:
        return func(*args, **kwargs)
    except HMSBaseException as e:
    #    ColPt.red(f"[Error] {e.message}")
       print(f"[Error] {e.message}")
    except KeyboardInterrupt as e:
        ColPt.yellow(f"[Info] Operation cancelled by user")
    except Exception as e:
        ColPt.red(f"[UNEXPECTED ERROR ] {e}")
