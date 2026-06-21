from pathlib import Path
import shutil
import requests
import os
import subprocess


def ingest_local_lab(source_folder: str, lab_id: str) -> dict:
    source_path = Path(source_folder)
    target_path = Path("knowledge-base") / "labguides" / lab_id

    if not source_path.exists():
        return {
            "success": False,
            "message": f"Source folder not found: {source_folder}"
        }

    target_path.mkdir(parents=True, exist_ok=True)

    copied_files = []

    for md_file in source_path.rglob("*.md"):
        destination = target_path / md_file.name
        shutil.copy(md_file, destination)
        copied_files.append(str(destination))

    return {
        "success": True,
        "lab_id": lab_id,
        "files_copied": copied_files
    }


def ingest_github_markdown(
    raw_file_url: str,
    lab_id: str,
    file_name: str
) -> dict:
    target_path = Path("knowledge-base") / "labguides" / lab_id
    target_path.mkdir(parents=True, exist_ok=True)

    response = requests.get(raw_file_url)

    if response.status_code != 200:
        return {
            "success": False,
            "message": f"Failed to download file. Status code: {response.status_code}"
        }

    destination = target_path / file_name

    with open(destination, "w", encoding="utf-8") as file:
        file.write(response.text)

    return {
        "success": True,
        "lab_id": lab_id,
        "file_saved": str(destination)
    }


def ingest_github_repository(repo_url: str, lab_id: str) -> dict:
    clone_folder = f"/tmp/{lab_id}"

    if os.path.exists(clone_folder):
        subprocess.run(["rm", "-rf", clone_folder])

    clone_result = subprocess.run(
        ["git", "clone", repo_url, clone_folder],
        capture_output=True,
        text=True
    )

    if clone_result.returncode != 0:
        return {
            "success": False,
            "message": "Failed to clone GitHub repository.",
            "error": clone_result.stderr
        }

    target_path = Path("knowledge-base") / "labguides" / lab_id
    target_path.mkdir(parents=True, exist_ok=True)

    copied_files = []

    for md_file in Path(clone_folder).rglob("*.md"):
        destination = target_path / md_file.name
        shutil.copy(md_file, destination)
        copied_files.append(str(destination))

    return {
        "success": True,
        "lab_id": lab_id,
        "files_copied": copied_files
    }