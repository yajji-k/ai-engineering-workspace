from fastapi import FastAPI

from app.api import chat_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Engineering Workspace",
        version="1.0.0",
    )

    app.include_router(chat_router)

    return app


app = create_app()


def main() -> None:
    import uvicorn

    uvicorn.run(
        "main:app",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()