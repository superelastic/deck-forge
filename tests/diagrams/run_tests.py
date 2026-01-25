#!/usr/bin/env python3
"""
Diagram Generation Test Runner

Validates Mermaid and Matplotlib diagram generation with PASS/FAIL feedback
for iterative refinement. Designed to provide actionable error messages.

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py mermaid_flowchart_01  # Run specific test
    python run_tests.py --validate CODE    # Validate inline code
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional


class DiagramType(Enum):
    MERMAID_FLOWCHART = "mermaid_flowchart"
    MERMAID_SEQUENCE = "mermaid_sequence"
    MERMAID_STATE = "mermaid_state"
    MERMAID_BLOCK = "mermaid_block"
    MATPLOTLIB_LINE = "matplotlib_line"
    MATPLOTLIB_BAR = "matplotlib_bar"
    MATPLOTLIB_PIE = "matplotlib_pie"


@dataclass
class TestResult:
    test_id: str
    passed: bool
    message: str
    details: Optional[str] = None


def detect_diagram_type(code: str) -> Optional[DiagramType]:
    """Detect diagram type from code content."""
    code_lower = code.lower()

    if "flowchart" in code_lower or "graph " in code_lower:
        return DiagramType.MERMAID_FLOWCHART
    elif "sequencediagram" in code_lower:
        return DiagramType.MERMAID_SEQUENCE
    elif "statediagram" in code_lower:
        return DiagramType.MERMAID_STATE
    elif "block-beta" in code_lower:
        return DiagramType.MERMAID_BLOCK
    elif "plt.plot" in code or "ax.plot" in code:
        return DiagramType.MATPLOTLIB_LINE
    elif "plt.bar" in code or "ax.bar" in code:
        return DiagramType.MATPLOTLIB_BAR
    elif "plt.pie" in code or "ax.pie" in code:
        return DiagramType.MATPLOTLIB_PIE

    return None


def validate_mermaid_syntax(code: str, test_id: str) -> TestResult:
    """Validate Mermaid diagram syntax using mmdc (mermaid-cli)."""

    # Check if mmdc is available
    try:
        subprocess.run(["mmdc", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return TestResult(
            test_id=test_id,
            passed=False,
            message="mermaid-cli (mmdc) not installed",
            details="Install with: npm install -g @mermaid-js/mermaid-cli"
        )

    # Write code to temp file and validate
    with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False) as f:
        f.write(code)
        input_path = f.name

    output_path = tempfile.mktemp(suffix='.svg')

    try:
        result = subprocess.run(
            ["mmdc", "-i", input_path, "-o", output_path, "-q"],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            # Parse error message for line numbers
            error_msg = result.stderr or result.stdout
            return TestResult(
                test_id=test_id,
                passed=False,
                message="mermaid parse error",
                details=error_msg.strip()
            )

        # Check output file exists and has content
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            return TestResult(
                test_id=test_id,
                passed=True,
                message="syntax valid, renders correctly"
            )
        else:
            return TestResult(
                test_id=test_id,
                passed=False,
                message="render failed - no output produced"
            )

    except subprocess.TimeoutExpired:
        return TestResult(
            test_id=test_id,
            passed=False,
            message="render timeout - diagram may be too complex"
        )
    finally:
        # Cleanup temp files
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)


def validate_matplotlib_syntax(code: str, test_id: str) -> TestResult:
    """Validate Matplotlib code syntax and execution."""

    # Create a temp directory for output
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "output.svg")

        # Inject output path into code
        # Replace any savefig call with our temp path
        modified_code = re.sub(
            r"plt\.savefig\([^)]+\)",
            f"plt.savefig('{output_path}', format='svg')",
            code
        )

        # If no savefig, add one
        if "savefig" not in code:
            modified_code += f"\nplt.savefig('{output_path}', format='svg')\nplt.close()"

        # Write to temp file and execute
        script_path = os.path.join(tmpdir, "test_chart.py")
        with open(script_path, 'w') as f:
            f.write(modified_code)

        try:
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=tmpdir
            )

            if result.returncode != 0:
                # Parse Python error
                error_lines = result.stderr.strip().split('\n')
                # Find the most relevant error line
                for line in reversed(error_lines):
                    if 'Error' in line or 'error' in line:
                        return TestResult(
                            test_id=test_id,
                            passed=False,
                            message=f"matplotlib syntax error",
                            details='\n'.join(error_lines[-5:])
                        )
                return TestResult(
                    test_id=test_id,
                    passed=False,
                    message="matplotlib execution error",
                    details=result.stderr.strip()
                )

            # Check SVG was created
            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                return TestResult(
                    test_id=test_id,
                    passed=True,
                    message="syntax valid, SVG generated"
                )
            else:
                return TestResult(
                    test_id=test_id,
                    passed=False,
                    message="execution succeeded but no SVG output"
                )

        except subprocess.TimeoutExpired:
            return TestResult(
                test_id=test_id,
                passed=False,
                message="execution timeout"
            )


def validate_diagram(code: str, test_id: str, diagram_type: Optional[DiagramType] = None) -> TestResult:
    """Validate diagram code based on detected or specified type."""

    if diagram_type is None:
        diagram_type = detect_diagram_type(code)

    if diagram_type is None:
        return TestResult(
            test_id=test_id,
            passed=False,
            message="could not detect diagram type",
            details="Code must contain Mermaid keywords (flowchart, sequenceDiagram, stateDiagram, block-beta) or Matplotlib plot functions"
        )

    if diagram_type.value.startswith("mermaid"):
        return validate_mermaid_syntax(code, test_id)
    else:
        return validate_matplotlib_syntax(code, test_id)


def load_test_fixture(fixtures_dir: Path, test_id: str) -> tuple[str, Optional[str]]:
    """Load test input and optional expected output."""
    input_file = fixtures_dir / f"{test_id}_input.md"

    if not input_file.exists():
        raise FileNotFoundError(f"Test fixture not found: {input_file}")

    with open(input_file) as f:
        input_content = f.read()

    # Look for expected output file
    expected_content = None
    for ext in ['.mermaid', '.mmd', '.py']:
        expected_file = fixtures_dir / f"{test_id}_expected{ext}"
        if expected_file.exists():
            with open(expected_file) as f:
                expected_content = f.read()
            break

    return input_content, expected_content


def extract_code_from_response(response: str) -> Optional[str]:
    """Extract diagram code from a markdown code block."""
    # Match ```mermaid, ```python, or plain ``` blocks
    patterns = [
        r'```mermaid\n(.*?)```',
        r'```python\n(.*?)```',
        r'```\n(.*?)```'
    ]

    for pattern in patterns:
        match = re.search(pattern, response, re.DOTALL)
        if match:
            return match.group(1).strip()

    return None


def run_test(fixtures_dir: Path, test_id: str, generated_code: Optional[str] = None) -> TestResult:
    """Run a single test case."""
    try:
        input_content, expected = load_test_fixture(fixtures_dir, test_id)
    except FileNotFoundError as e:
        return TestResult(test_id=test_id, passed=False, message=str(e))

    # If generated code provided, validate it
    if generated_code:
        code = extract_code_from_response(generated_code) or generated_code
        return validate_diagram(code, test_id)

    # If expected output exists, validate it (for testing the golden files)
    if expected:
        return validate_diagram(expected, test_id)

    return TestResult(
        test_id=test_id,
        passed=False,
        message="no code to validate",
        details="Provide generated_code or ensure expected output file exists"
    )


def list_tests(fixtures_dir: Path) -> list[str]:
    """List all available test IDs."""
    tests = set()
    for f in fixtures_dir.glob("*_input.md"):
        test_id = f.stem.replace("_input", "")
        tests.add(test_id)
    return sorted(tests)


def format_result(result: TestResult) -> str:
    """Format test result for output."""
    status = "PASS" if result.passed else "FAIL"
    output = f"{status}: {result.test_id} - {result.message}"
    if result.details:
        # Indent details
        details = '\n  '.join(result.details.split('\n'))
        output += f"\n  {details}"
    return output


def main():
    parser = argparse.ArgumentParser(description="Diagram Generation Test Runner")
    parser.add_argument("test_id", nargs="?", help="Specific test ID to run")
    parser.add_argument("--validate", metavar="CODE", help="Validate inline code")
    parser.add_argument("--list", action="store_true", help="List available tests")
    parser.add_argument("--fixtures", default=None, help="Path to fixtures directory")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    # Determine fixtures directory
    if args.fixtures:
        fixtures_dir = Path(args.fixtures)
    else:
        fixtures_dir = Path(__file__).parent / "fixtures"

    # Handle --validate for inline code
    if args.validate:
        test_id = args.test_id or "inline"
        result = validate_diagram(args.validate, test_id)
        print(format_result(result))
        sys.exit(0 if result.passed else 1)

    # Handle --list
    if args.list:
        tests = list_tests(fixtures_dir)
        if tests:
            print("Available tests:")
            for t in tests:
                print(f"  {t}")
        else:
            print("No test fixtures found in", fixtures_dir)
        return

    # Run tests
    if args.test_id:
        test_ids = [args.test_id]
    else:
        test_ids = list_tests(fixtures_dir)

    if not test_ids:
        print("No tests found. Create fixtures in", fixtures_dir)
        sys.exit(1)

    results = []
    for test_id in test_ids:
        result = run_test(fixtures_dir, test_id)
        results.append(result)

    # Output results
    if args.json:
        output = [
            {
                "test_id": r.test_id,
                "passed": r.passed,
                "message": r.message,
                "details": r.details
            }
            for r in results
        ]
        print(json.dumps(output, indent=2))
    else:
        for result in results:
            print(format_result(result))

    # Summary
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    print(f"\n{passed}/{total} tests passed")

    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
