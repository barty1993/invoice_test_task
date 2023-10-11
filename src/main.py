from contextlib import AsyncExitStack

import uvicorn
from aiopg.sa import create_engine
from fastapi import FastAPI

from config import Config


def run_app(config: Config):
    app = FastAPI()

    @app.on_event("startup")
    async def engine_setup():
        _exit_stack = AsyncExitStack()
        engine = await _exit_stack.enter_async_context(
            create_engine(config.POSTGRES_DSN.unicode_string())
        )
        app.state._db_exit_stack = _exit_stack
        app.state.engine = engine

    @app.on_event("shutdown")
    async def close_engine():
        print("Cleaning Engine")
        await app.state._db_exit_stack.aclose()
        print("Engine cleaned")

    return app


if __name__ == "__main__":
    config = Config()
    app = run_app(config)
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
