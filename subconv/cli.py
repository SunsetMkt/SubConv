#!/usr/bin/env python3

from . import config


def main():
    import os
    import uvicorn

    app_config = config.get_app_config()
    DISALLOW_ROBOTS = bool(eval(os.environ.get("DISALLOW_ROBOTS", "False")))

    print("host:", app_config.HOST)
    print("port:", app_config.PORT)
    print("default template:", app_config.DEFAULT_TEMPLATE)
    if DISALLOW_ROBOTS:
        print("robots: Disallow")
    else:
        print("robots: Allow")

    uvicorn.run(
        "subconv.app:app",
        host=app_config.HOST,
        port=app_config.PORT,
        workers=4,
        proxy_headers=True,
        forwarded_allow_ips="*",
    )
