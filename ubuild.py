def main(build):
    build.packages.install("aiohttp")
    build.packages.install("attrs")
    build.packages.install("async-timeout")
    build.packages.install("git+https://github.com/Tinche/cattrs.git#cattrs")
    build.packages.install("flask")
    build.packages.install("gunicorn")
    build.packages.install("jupyter")
    build.packages.install("matplotlib")
    build.packages.install("marshmallow")
    build.packages.install("pydantic")
    build.packages.install("schematics")
    build.packages.install("tabulate")
