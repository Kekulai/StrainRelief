from pathlib import Path

from strain_relief.compute_strain import compute_strain

# Directories
project_dir: Path = Path(__file__).resolve().parents[2]
src_dir: Path = project_dir / "src"
test_dir: Path = project_dir / "tests"
data_dir: Path = project_dir / "data"

# the above don't work on pip installs, so adding this:
# Current directory
current_dir: Path = Path(__file__).resolve().parent
config_dir: Path = current_dir / "hydra_config"

__all__ = [
    "compute_strain",
    "project_dir",
    "src_dir",
    "test_dir",
    "data_dir",
]
