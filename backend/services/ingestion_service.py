from pathlib import Path
import shutil


def ingest_local_lab(source_folder: str, lab_id: str) -> dict:
    """
    Copy lab guide markdown files into the knowledge-base/lab-guides folder.
    """

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
