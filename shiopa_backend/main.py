from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from shiopa_backend.apps.store import models as store_models
from shiopa_backend.apps.users import models as user_models

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "Her"}


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": [store_models, user_models]},
    generate_schemas=True,
    add_exception_handlers=True,
)


TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": [store_models, "aerich.models", user_models],
            "default_connection": "default",
        },
    },
}
