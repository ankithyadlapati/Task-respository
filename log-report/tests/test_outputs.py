import json
import re
from collections import Counter
from pathlib import Path

REPORT = Path("/app/report.json")
LOG = Path("/app/access.log")


def _load_report():
    assert REPORT.exists(), "no report.json found at /app/report.json"
    return json.loads(REPORT.read_text())


def _log_lines():
    with open(LOG) as f:
        return [line.strip() for line in f if line.strip()]


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and contains a single valid JSON object."""
    data = _load_report()
    assert isinstance(data, dict)


def test_total_requests_matches_log():
    """Criterion 2: total_requests equals the number of non-blank log lines."""
    data = _load_report()
    expected = len(_log_lines())
    assert data.get("total_requests") == expected, (
        f"expected total_requests={expected}, got {data.get('total_requests')}"
    )


def test_unique_ips_matches_log():
    """Criterion 3: unique_ips equals the count of distinct client IPs."""
    data = _load_report()
    expected = len({line.split()[0] for line in _log_lines()})
    assert data.get("unique_ips") == expected, (
        f"expected unique_ips={expected}, got {data.get('unique_ips')}"
    )


def test_top_path_matches_log():
    """Criterion 4: top_path equals the single most frequently requested path."""
    data = _load_report()
    paths = Counter()
    for line in _log_lines():
        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1
    expected = paths.most_common(1)[0][0]
    assert data.get("top_path") == expected, (
        f"expected top_path={expected!r}, got {data.get('top_path')!r}"
    )
