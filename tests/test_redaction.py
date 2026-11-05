import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("edition", ["claude", "codex"])
def test_no_other_credential_on_same_line_is_emitted(edition, tmp_path):
    script = ROOT / edition / "skills/checalo/scripts/scan_secrets.py"
    spec = importlib.util.spec_from_file_location("scanner_" + edition, script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    first, second = "alpha-value-123", "beta-value-456"
    source = tmp_path / "config.py"
    source.write_text(f"TOKEN_A='{first}'; TOKEN_B='{second}'\n", encoding="utf8")
    findings = module.scan_file(source, [("fixture", re.compile(re.escape(first)), "high", "fixture pattern")], str(tmp_path))
    assert findings
    serialized = json.dumps(findings)
    assert first not in serialized and second not in serialized
    assert findings[0]["line"] == 1


@pytest.mark.parametrize("edition", ["claude", "codex"])
def test_cli_json_and_summary_keep_generated_credentials_private(edition, tmp_path):
    script = ROOT / edition / "skills/checalo/scripts/scan_secrets.py"
    first, second = "gh" + "p_" + "aB7" * 12, "gh" + "p_" + "cD8" * 12
    (tmp_path / "config.py").write_text(f"TOKEN_A='{first}'; TOKEN_B='{second}'\n", encoding="utf8")
    for mode in ["--json", "--summary"]:
        result = subprocess.run([sys.executable, "-B", str(script), str(tmp_path), mode], capture_output=True, text=True)
        assert result.returncode == 1
        assert first not in result.stdout + result.stderr
        assert second not in result.stdout + result.stderr
        if mode == "--json":
            assert json.loads(result.stdout)["metadata"]["total_findings"] > 0


@pytest.mark.parametrize("edition", ["claude", "codex"])
@pytest.mark.parametrize("name", ["scan_secrets.py", "check_lockfiles.py"])
def test_help_is_available_without_scanning(edition, name):
    script = ROOT / edition / "skills/checalo/scripts" / name
    result = subprocess.run([sys.executable, "-B", str(script), "--help"], capture_output=True, text=True)
    assert result.returncode == 0 and "Usage:" in result.stdout
