import pytest
from task_1.main import data_extraction

@pytest.mark.parametrize('expected_visitors',[10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9])
def test_popularuty_with_params(data_extraction, expected_visitors):
    for data in data_extraction:
        if data.Popularity < expected_visitors:
            message = (
                f"{data.Websites} (Frontend:{data.Front_end}|Backend:{data.Back_end}) "
                f"has {data.Popularity} unique visitors per month. "
                f"(Expected more than {expected_visitors})"
            )
            pytest.fail(message, pytrace=False)