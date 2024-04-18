from tortoise import Tortoise


async def setup_db() -> None:
    await Tortoise.init(
        db_url="sqlite://./src/database/db.sqlite3",
        modules={
            "models": [
                "src.database.models.books",
                "src.database.models.genres"
            ]
        }
    )

    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()
