from .logger import GunicornLogger


def get_app_options(
    host: str,
    port: int,
    workers: int,
    timeout: int,
    log_level: str,
) -> dict:
    return {
        "access_log": "-",
        "error_log": "-",
        "bind": f"{host}:{port}",
        "loglevel": log_level,
        "logger_class": GunicornLogger,
        "timeout": timeout,
        "workers": workers,
        "worker_class": "uvicorn.workers.UvicornWorker",
    }
