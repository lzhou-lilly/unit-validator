import argparse
import csv
from pathlib import Path
from typing import cast

import yaml
from pydantic import BaseModel

from .unit_standardizer import UnitStandardizer


class ConfigModel(BaseModel):
    units: dict[str, dict[str, list[str]]]


def load_config(yaml_path: Path) -> ConfigModel:
    """Load units configuration from YAML file."""
    config = yaml.safe_load(yaml_path.open("r"))
    config_model = ConfigModel.model_validate(config)
    return config_model


def process_tsv(txt_path: Path, tsv_path: Path, config: ConfigModel) -> None:
    with txt_path.open("r") as fi, tsv_path.open("w") as fo:
        # Read with automatic header detection
        reader = csv.DictReader(fi, delimiter="\t")

        # Check if "unit" column exists
        if reader.fieldnames is None:
            raise ValueError("Input TSV file has no headers")

        if "unit" not in reader.fieldnames:
            raise ValueError("Input TSV file must have a 'unit' column")

        unit_standardizer = UnitStandardizer(units=config.units)

        # Preserve all original columns and add validation errors column
        output_fieldnames = list(reader.fieldnames)
        if "unit_validation_errors" not in output_fieldnames:
            output_fieldnames.append("unit_validation_errors")

        writer = csv.DictWriter(fo, fieldnames=output_fieldnames, delimiter="\t")
        writer.writeheader()

        for row in reader:
            unit = row.get("unit", "").strip()

            if not unit:
                pass
            else:
                try:
                    errors = unit_standardizer.check(unit)
                    if errors:
                        row["unit_validation_errors"] = "; ".join(errors)
                    else:
                        row["unit_validation_errors"] = "✅ All is good"
                except Exception:  # noqa: BLE001
                    row["unit_validation_errors"] = "⛔ Parse Error"
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate units in a TSV file using YAML configuration"
    )
    parser.add_argument("tsv_file", type=Path, help="Path to tsv file with units on each row")
    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        default=Path("unit-standardizer.yaml"),
        help="Path to YAML configuration file (default: unit-standardizer.yaml)",
    )

    args = parser.parse_args()

    # Load configuration and process TSV
    units_config = load_config(cast("Path", args.config))
    input_path = cast("Path", args.tsv_file)
    output_path = input_path.with_suffix(".output.tsv")
    process_tsv(input_path, output_path, units_config)
