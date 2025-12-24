from pathlib import Path

from strain_relief.compute_strain import compute_strain

# Current directory
_current_dir: Path = Path(__file__).resolve().parent
# Configuration directory path
config_dir: Path = _current_dir / "hydra_config"

__all__ = [
    "compute_strain",
    "config_dir"
]
