from datetime import datetime

from freezegun import freeze_time

from src.core.entity.check_in import CheckIn
from src.core.use_cases.check_in.make_check_in import MakeCheckIn
from src.infra.repository.check_in_repository_memory import CheckInRepositoryMemory


@freeze_time("2022-09-30")
def test_make_check_in():
    person_id = "999"
    check_in_repository_memory = CheckInRepositoryMemory()
    make_check_in = MakeCheckIn(check_in_repository_memory, person_id)
    executed_check_in = make_check_in.execute()
    expected_check_in = CheckIn(1, person_id, datetime.now())

    assert executed_check_in.__eq__(expected_check_in)
