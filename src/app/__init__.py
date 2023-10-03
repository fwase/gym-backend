from fastapi import FastAPI

from src.api.routers.person import router as person_router

main_app = FastAPI()


@main_app.get("/health-check")
def get_person():
    return {"message": "OK"}


main_app.include_router(person_router)
