import json
from typing import Final
from urllib.request import Request, urlopen


GITHUB_OWNER_NAME: Final[str] = "ripto1027"
GITHUB_REPO_NAME: Final[str] = "PdfEditor"

def get_release() -> None:
    api_url: str = f"https://api.github.com/{GITHUB_OWNER_NAME}/{GITHUB_REPO_NAME}/releases/latest"
    request: Request = Request(api_url)

    with urlopen(request) as response:
        latest_release_data: dict = json.load(response)

    asset_data: dict | None = next(
        (item for item in latest_release_data.get("assets", [])),
        None
    )