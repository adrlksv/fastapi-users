def get_app_options(
    host: str,
    port: int,
    workers: int,
    timeout: int
) -> dict:
    return {
        "access_log": "-",
        "error_log": "-",
        "bind": f"{host}:{port}",
        "timeout": timeout,
        "workers": workers,
        "logger_class": "",
        "worker_class": "uvicorn.workers.UvicornWorker",
    }
