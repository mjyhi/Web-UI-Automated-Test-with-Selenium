"""测试运行入口（生成 HTML 报告）。"""

import os
import sys
import unittest

import HtmlTestRunner


def main() -> int:
    """发现并执行用例，生成 HTML 报告。"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)
    sys.path.insert(0, project_root)

    test_dir = os.path.join(base_dir, "testcases")
    report_dir = os.path.join(base_dir, "reports")
    os.makedirs(report_dir, exist_ok=True)

    suite = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    runner = HtmlTestRunner.HTMLTestRunner(
        output=report_dir,
        report_title="UI Automation Report",
        report_name="ui_test_report",
        combine_reports=True,
        add_timestamp=True,
    )
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
