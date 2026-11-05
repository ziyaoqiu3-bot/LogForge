# LogForge

A lightweight, pure-Python tool for log parsing and structured financial report generation.

## Highlights & Technical Features

1. **Zero External Dependencies**: Built entirely on Python's standard library and plain syntax, so the underlying logic stays clear and easy to follow.
2. **High-Precision Financial Settlement**: Uses `decimal.Decimal` instead of `float` for all currency handling, eliminating floating-point precision loss.
3. **Strict Alignment Formatting**: Uses fixed-width format specifiers (e.g. `%-15s`, `%10.2f`) to produce neatly aligned, structured text reports.
4. **Safe Resource Handling**: Uses the `with open` context manager so files are always closed properly, even when errors occur.
5. **Clean Repository Layout**: A pre-configured `.gitignore` excludes `.pyc` bytecode files and `__pycache__` folders.

## Quick Start

Run the main script directly from your terminal:

```bash
python logforge.py
```

# LogForge

LogForge는 경량화된 순수 Python 기반의 로그 파싱 및 재무 구조화 보고서 생성 도구입니다.

## 주요 특징 및 기술적 강점

1. **외부 의존성 제로 (Zero External Dependencies)**: Python 표준 라이브러리와 기본 문법만으로 구축되어 내부 로직이 명확합니다.
2. **고정밀 재무 정산**: 통화 처리 시 `float` 대신 `decimal.Decimal`을 사용하여 부동소수점 정밀도 손실을 방지합니다.
3. **엄격한 정렬 포맷팅**: 고정 폭 포맷 지정자(예: `%-15s`, `%10.2f`)를 적용하여 깔끔하게 정렬된 구조화 텍스트 보고서를 출력합니다.
4. **안전한 리소스 관리**: `with open` 컨텍스트 매니저를 사용하여 오류가 발생해도 파일이 안전하게 닫히도록 보장합니다.
5. **깔끔한 리포지토리 구조**: 사전 설정된 `.gitignore`가 `.pyc` 바이트코드 파일과 `__pycache__` 폴더를 자동으로 제외합니다.

## 빠른 시작 (Quick Start)

터미널에서 메인 스크립트를 직접 실행하세요.

```bash
python logforge.py
```

# LogForge

LogForge 是一个轻量级、纯 Python 实现的日志解析与财务结构化报告生成工具。

## 项目亮点与技术特性

1. **零外部依赖（Zero External Dependencies）**：完全基于 Python 标准库和基础语法构建，底层逻辑清晰易懂。
2. **高精度财务结算**：处理货币时使用 `decimal.Decimal` 而非 `float`，避免浮点数精度损失。
3. **严格的对齐格式化**：使用固定宽度的格式占位符（如 `%-15s`、`%10.2f`），输出整齐对齐的结构化文本报告。
4. **安全的资源管理**：采用 `with open` 上下文管理器，即使发生异常也能确保文件被正确关闭。
5. **简洁的仓库结构**：预置 `.gitignore`，自动排除 `.pyc` 字节码文件和 `__pycache__` 文件夹。

## 快速开始（Quick Start）

在终端中直接运行主脚本：

```bash
python logforge.py
```
